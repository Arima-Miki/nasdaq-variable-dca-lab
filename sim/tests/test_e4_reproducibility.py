#!/usr/bin/env python3
"""Mode-E Phase E4 — determinism, replay and evidence-safety hardening.

NON-FORMAL — SIMULATION TRIAL. Engine state only; no economic claim.

E4 adds NO strategy semantics and NO economic functionality. It establishes
that the PRESERVED engine, given the same code, strategy, fixture and
configuration, produces the same mechanical result and a correctly
attributable evidence package.

Nothing here writes into the real evidence store. Replay comparisons use a
temporary store so that E1/E2/E3 evidence cannot be touched by testing.
"""
from decimal import Decimal
from pathlib import Path
import copy, json, os, shutil, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT / "engine"))
from engine import Engine, load  # noqa: E402
import run_mode_e as driver  # noqa: E402

FAILS = []

# Replay matrix: each entry exercises a materially distinct engine path.
MATRIX = [
    ("S1",    "A", "Strategy A — month-end allocation path"),
    ("S3",    "B", "Strategy B — canonical drawdown-trigger fixture"),
    ("S1",    "C", "Strategy C — month-end fallback path"),
    ("E2-Y",  "B", "Calendar boundary — December commit -> January execution"),
    ("E2-MY", "B", "Sparse multi-year"),
    ("S10",   "B", "Threshold boundary — one tick either side of both zones"),
]

# manifest fields that describe the ENVIRONMENT/PROVENANCE rather than the
# mechanical result. Classified explicitly (E4 §4) rather than excluded for
# convenience: within one replay these are ALSO expected to be identical,
# because the driver takes no wall-clock, no RNG and no environment input.
PROVENANCE_FIELDS = {
    "simulator_commit", "repository_worktree_clean",
    "simulator_paths_match_commit", "simulator_paths_scope", "run_date",
}


def ok(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name:64s} {detail}")
    if not cond:
        FAILS.append(name)


def fx(fid):
    return load(ROOT / "fixtures" / f"{fid}.json")


def run_into(store, fid, st, run_id):
    """Execute the REAL driver against a temporary store."""
    orig = driver.STORE
    driver.STORE = Path(store)
    try:
        return driver.main(fid, st, run_id)
    finally:
        driver.STORE = orig


def read_outputs(store, run_id):
    return {f: (Path(store) / run_id / f).read_bytes() for f in driver.OUTPUT_FILES}


# ---------------------------------------------------------------- replay
def replay_matrix():
    print("=" * 80); print("DETERMINISTIC REPLAY MATRIX"); print("=" * 80)
    for fid, st, why in MATRIX:
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            rid = f"E4-{fid}-{st}-REPLAY"
            run_into(d1, fid, st, rid)
            run_into(d2, fid, st, rid)
            a, b = read_outputs(d1, rid), read_outputs(d2, rid)

            engine_files = [f for f in driver.OUTPUT_FILES if f != "manifest.json"]
            same_engine = all(a[f] == b[f] for f in engine_files)
            ok(f"{fid}/{st} engine outputs byte-identical on replay", same_engine, why)
            if not same_engine:
                for f in engine_files:
                    if a[f] != b[f]:
                        print(f"        DIFFERS: {f}")

            # Manifest: compare mechanical fields and provenance fields apart,
            # so that a difference is CLASSIFIED rather than hidden.
            ma, mb = json.loads(a["manifest.json"]), json.loads(b["manifest.json"])
            mech_diff = [k for k in set(ma) | set(mb)
                         if k not in PROVENANCE_FIELDS and ma.get(k) != mb.get(k)]
            prov_diff = [k for k in PROVENANCE_FIELDS if ma.get(k) != mb.get(k)]
            ok(f"{fid}/{st} manifest mechanical fields identical", not mech_diff,
               f"differing={mech_diff}")
            ok(f"{fid}/{st} manifest provenance fields identical too (no env input)",
               not prov_diff, f"differing={prov_diff}")
            ok(f"{fid}/{st} manifest byte-identical", a["manifest.json"] == b["manifest.json"])


# ------------------------------------------------- strategy-label integrity
def strategy_label_integrity():
    print("\n" + "=" * 80); print("STRATEGY-LABEL INTEGRITY (through the real driver)"); print("=" * 80)
    for st in ("A", "B", "C"):
        with tempfile.TemporaryDirectory() as d:
            rid = f"E4-LABEL-{st}"
            eng, _, out = run_into(d, "S6", st, rid)
            man = json.loads((out / "manifest.json").read_text())
            ts = json.loads((out / "terminal_state.json").read_text())["terminal_state"]
            ok(f"manifest == requested == engine == state, strategy {st}",
               man["strategy_rule_id"] == f"Strategy {st}"
               and eng.strategy == st and ts["strategy"] == st,
               f"manifest={man['strategy_rule_id']!r} engine={eng.strategy!r} state={ts['strategy']!r}")

    # A run MUST FAIL rather than write evidence when the labels disagree.
    # Simulate the exact E3 defect: driver asked for A, engine actually ran B.
    print("\n  negative test — reproduce the E3 driver defect and require a hard failure:")
    with tempfile.TemporaryDirectory() as d:
        real_engine = driver.Engine

        class WrongStrategyEngine(real_engine):
            def __init__(self, fixture, strategy="B"):
                super().__init__(fixture, strategy="B")   # discards the request

        driver.Engine = WrongStrategyEngine
        try:
            run_into(d, "S6", "A", "E4-LABEL-NEGATIVE")
            ok("mislabelled run is refused", False, "NO ERROR — evidence would have been written")
        except driver.EvidenceSafetyError as e:
            wrote = (Path(d) / "E4-LABEL-NEGATIVE").exists()
            ok("mislabelled run is refused", not wrote, f"EvidenceSafetyError: {e}")
            ok("no evidence directory created by the refused run", not wrote)
        except Exception as e:  # noqa: BLE001
            ok("mislabelled run is refused", False, f"wrong exception: {type(e).__name__}: {e}")
        finally:
            driver.Engine = real_engine


# --------------------------------------------------- fixture-hash integrity
def fixture_hash_integrity():
    print("\n" + "=" * 80); print("FIXTURE IDENTITY / HASH INTEGRITY"); print("=" * 80)
    import hashlib
    for fid, st, _ in MATRIX[:3]:
        with tempfile.TemporaryDirectory() as d:
            _, _, out = run_into(d, fid, st, f"E4-FXH-{fid}-{st}")
            man = json.loads((out / "manifest.json").read_text())
            actual = hashlib.sha256((ROOT / "fixtures" / f"{fid}.json").read_bytes()).hexdigest()
            ok(f"{fid} manifest dataset_id == requested fixture", man["dataset_id"] == fid)
            ok(f"{fid} manifest dataset_sha256 == SHA-256 of the loaded file",
               man["dataset_sha256"] == actual, actual[:16] + "...")

    # Changing a fixture MUST change the recorded hash. Done on a temporary
    # controlled copy — no preserved fixture is altered.
    print("\n  mutation test on a TEMPORARY COPY (no preserved fixture is modified):")
    with tempfile.TemporaryDirectory() as tmpfix, tempfile.TemporaryDirectory() as d:
        src = ROOT / "fixtures" / "S3.json"
        before = src.read_bytes()
        tmp_fixtures = Path(tmpfix) / "fixtures"
        tmp_fixtures.mkdir()
        shutil.copy(src, tmp_fixtures / "S3.json")

        data = json.loads((tmp_fixtures / "S3.json").read_text())
        data["observations"][-1]["close"] = str(Decimal(data["observations"][-1]["close"]) + 1)
        (tmp_fixtures / "S3.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

        orig_root = driver.REPO
        driver.REPO = Path(tmpfix)          # driver reads REPO/"sim"/"fixtures"
        (Path(tmpfix) / "sim").mkdir(exist_ok=True)
        shutil.move(str(tmp_fixtures), str(Path(tmpfix) / "sim" / "fixtures"))
        try:
            _, _, out = run_into(d, "S3", "B", "E4-FXH-MUTATED")
            mutated_hash = json.loads((out / "manifest.json").read_text())["dataset_sha256"]
        finally:
            driver.REPO = orig_root

        import hashlib as _h
        original_hash = _h.sha256(before).hexdigest()
        ok("mutating the fixture changes the recorded dataset_sha256",
           mutated_hash != original_hash, f"{original_hash[:12]} -> {mutated_hash[:12]}")
        ok("preserved S3 fixture is byte-unchanged by this test",
           src.read_bytes() == before)


# ------------------------------------------------------ code identity
def code_identity():
    print("\n" + "=" * 80); print("SIMULATOR CODE IDENTITY"); print("=" * 80)
    with tempfile.TemporaryDirectory() as d:
        _, _, out = run_into(d, "S3", "B", "E4-CODEID")
        man = json.loads((out / "manifest.json").read_text())

    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    ok("manifest records the actual HEAD commit", man["simulator_commit"] == head, head[:12])
    ok("manifest separates repository cleanliness from simulator identity",
       "repository_worktree_clean" in man and "simulator_paths_match_commit" in man,
       f"repo_clean={man.get('repository_worktree_clean')} "
       f"sim_matches={man.get('simulator_paths_match_commit')}")
    ok("simulator_paths_scope is declared", man.get("simulator_paths_scope") == "sim/")

    sim_dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--", "sim"],
                               capture_output=True, text=True).stdout.strip()
    ok("simulator_paths_match_commit agrees with git for sim/",
       man["simulator_paths_match_commit"] == (sim_dirty == ""),
       "sim/ dirty" if sim_dirty else "sim/ matches HEAD")
    # Truthfulness: the field must never be asserted true while sim/ is dirty.
    if sim_dirty:
        ok("dirty sim/ is reported honestly (not falsified to true)",
           man["simulator_paths_match_commit"] is False,
           "E4 edits are pending review, so False is the correct value here")


# ------------------------------------------------------ event ordering
def event_ordering():
    print("\n" + "=" * 80); print("EVENT-ORDER DETERMINISM"); print("=" * 80)
    # A fixture whose log contains the full mechanical vocabulary.
    eng = Engine(fx("E2-MY"), strategy="C").run()
    kinds = [e["event"] for e in eng.events]
    required = ["OBSERVATION", "BUDGET_GRANT", "ATH_UPDATE", "DRAWDOWN",
                "PURCHASE_REQUEST", "COMMITMENT", "EXECUTION"]
    present = [k for k in required if k in kinds]
    ok("coverage run contains the mechanical event vocabulary",
       len(present) >= 6, f"present={present}")

    seqs = [[(e["date"], e["event"]) for e in Engine(fx("E2-MY"), strategy="C").run().events]
            for _ in range(3)]
    ok("event order identical across 3 in-process runs", seqs[0] == seqs[1] == seqs[2],
       f"{len(seqs[0])} events")

    # Under a DIFFERENT PYTHONHASHSEED, in a fresh interpreter.
    prog = (
        "import sys,json;sys.path.insert(0,%r);"
        "from engine import Engine,load;"
        "e=Engine(load(%r),strategy='C').run();"
        "print(json.dumps([(x['date'],x['event']) for x in e.events]))"
        % (str(ROOT / "engine"), str(ROOT / "fixtures" / "E2-MY.json"))
    )
    outs = []
    for seed in ("0", "1", "42", "12345"):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        r = subprocess.run([sys.executable, "-c", prog], capture_output=True, text=True, env=env)
        outs.append(r.stdout.strip())
    ok("event order identical across 4 PYTHONHASHSEED values",
       len(set(outs)) == 1 and outs[0], "seeds 0/1/42/12345")

    ok("no RNG or wall-clock symbol reachable in engine or driver",
       not _forbidden_symbols(), f"hits={_forbidden_symbols()}")


def _forbidden_symbols():
    import tokenize, keyword
    banned = {"random", "randint", "shuffle", "uuid", "uuid4", "now", "today",
              "utcnow", "monotonic", "perf_counter"}
    hits = set()
    for p in sorted((ROOT / "engine").glob("*.py")):
        with open(p, "rb") as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.NAME and not keyword.iskeyword(tok.string):
                    if tok.string in banned:
                        hits.add(f"{p.name}:{tok.string}")
    return sorted(hits)


# ------------------------------------------------------ serialization
def serialization():
    print("\n" + "=" * 80); print("SERIALIZATION DETERMINISM"); print("=" * 80)
    with tempfile.TemporaryDirectory() as d:
        _, _, out = run_into(d, "E2-MY", "C", "E4-SER")
        for f in driver.OUTPUT_FILES:
            raw = (out / f).read_bytes()
            ok(f"{f}: valid UTF-8", _is_utf8(raw))
            ok(f"{f}: ends with exactly one final newline",
               raw.endswith(b"\n") and not raw.endswith(b"\n\n"))
            ok(f"{f}: LF only, no CR", b"\r" not in raw)
            ok(f"{f}: no absolute path or host identity leaked",
               not any(s in raw for s in (b"/home/", str(Path.home()).encode(),
                                          b"research-materials", b"/tmp")))
            ok(f"{f}: key order stable across re-serialization",
               json.dumps(json.loads(raw), indent=2, ensure_ascii=False).encode() + b"\n" == raw)

        ts = json.loads((out / "terminal_state.json").read_text())["terminal_state"]
        numeric = [k for k, v in ts.items() if isinstance(v, str) and _numeric(v)]
        ok("Decimal values serialized as exact strings, never floats",
           all(isinstance(ts[k], str) for k in numeric) and
           not any(isinstance(v, float) for v in ts.values()),
           f"{len(numeric)} numeric fields")
        raw_all = (out / "terminal_state.json").read_bytes()
        ok("no float artefacts (e/E notation or .0000000000000001) in output",
           b"e-" not in raw_all and b"e+" not in raw_all)


def _is_utf8(b):
    try:
        b.decode("utf-8"); return True
    except UnicodeDecodeError:
        return False


def _numeric(v):
    try:
        Decimal(v); return True
    except Exception:
        return False


# ------------------------------------------------------ environment
def environment():
    print("\n" + "=" * 80); print("ENVIRONMENT DEPENDENCE"); print("=" * 80)
    prog = (
        "import sys,json;sys.path.insert(0,%r);"
        "from engine import Engine,load;"
        "e=Engine(load(%r),strategy='C').run();"
        "print(json.dumps(e.terminal_state()))" % (str(ROOT / "engine"),
                                                   str(ROOT / "fixtures" / "E2-MY.json"))
    )
    envs = {
        "baseline": {},
        "TZ=Pacific/Kiritimati": {"TZ": "Pacific/Kiritimati"},
        "TZ=Etc/GMT+12": {"TZ": "Etc/GMT+12"},
        "LC_ALL=tr_TR.UTF-8": {"LC_ALL": "tr_TR.UTF-8", "LANG": "tr_TR.UTF-8"},
        "LC_ALL=de_DE.UTF-8": {"LC_ALL": "de_DE.UTF-8", "LANG": "de_DE.UTF-8"},
        "PYTHONHASHSEED=99": {"PYTHONHASHSEED": "99"},
    }
    results = {}
    for label, extra in envs.items():
        r = subprocess.run([sys.executable, "-c", prog], capture_output=True, text=True,
                           env=dict(os.environ, **extra), cwd=str(Path(tempfile.gettempdir())))
        results[label] = r.stdout.strip()
    distinct = set(results.values())
    ok("terminal state identical across TZ / locale / hash-seed / cwd", len(distinct) == 1,
       f"{len(envs)} environments, {len(distinct)} distinct result(s)")
    if len(distinct) != 1:
        for k, v in results.items():
            print(f"        {k}: {v[:100]}")

    # cwd independence, explicitly: engine resolves paths from __file__.
    r = subprocess.run([sys.executable, "-c", prog], capture_output=True, text=True,
                       cwd="/", env=dict(os.environ))
    ok("engine runs correctly from an unrelated working directory (cwd=/)",
       r.returncode == 0 and r.stdout.strip() == results["baseline"])


# ------------------------------------------------ evidence-store safety
def evidence_safety():
    print("\n" + "=" * 80); print("EVIDENCE-STORE OVERWRITE PROTECTION"); print("=" * 80)
    with tempfile.TemporaryDirectory() as d:
        run_into(d, "S3", "B", "E4-GUARD")
        before = read_outputs(d, "E4-GUARD")
        try:
            run_into(d, "S3", "B", "E4-GUARD")
            ok("re-using a run_id FAILS CLOSED", False,
               "NO ERROR — preserved evidence would be silently overwritten")
        except driver.EvidenceSafetyError as e:
            ok("re-using a run_id FAILS CLOSED", True, str(e)[:90])
        after = read_outputs(d, "E4-GUARD")
        ok("existing evidence is byte-unchanged after the refused write", before == after)

        # Refusal must also hold when a DIFFERENT strategy reuses the id — the
        # dangerous case, since it would silently rewrite history with new content.
        try:
            run_into(d, "S3", "C", "E4-GUARD")
            ok("re-using a run_id with different content FAILS CLOSED", False, "NO ERROR")
        except driver.EvidenceSafetyError:
            ok("re-using a run_id with different content FAILS CLOSED", True)
        ok("evidence still byte-unchanged", read_outputs(d, "E4-GUARD") == before)

    print("\n  real store is untouched by this test suite:")
    ok("tests never write to the real evidence store",
       driver.STORE == Path.home() / "research-materials" / "nasdaq-variable-dca-lab"
       / "simulation-trial-mode-e", "driver.STORE restored after every temp run")


def main():
    print("=" * 80)
    print("MODE-E PHASE E4 — REPRODUCIBILITY / EVIDENCE-SAFETY HARDENING")
    print("=" * 80)
    replay_matrix()
    strategy_label_integrity()
    fixture_hash_integrity()
    code_identity()
    event_ordering()
    serialization()
    environment()
    evidence_safety()
    print("\n" + "=" * 80)
    print("RESULT:", "ALL E4 CHECKS PASS" if not FAILS
          else f"FAILURES ({len(FAILS)}): " + "; ".join(FAILS[:12]))
    print("=" * 80)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
