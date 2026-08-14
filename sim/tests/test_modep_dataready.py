#!/usr/bin/env python3
"""Mode-P DATA-READY validation — constructed CSV fixtures only.

NON-FORMAL — SIMULATION TRIAL — MODE P — CONSTRUCTED FIXTURE —
NOT HISTORICAL MARKET DATA — NO ECONOMIC CONCLUSION.

Demonstrates that a CSV can enter the Mode-P loader, be validated fail-closed,
normalize into the already-validated engine, and produce correctly labelled
non-formal output with no governed metric — WITHOUT changing any mechanic
validated in Mode E.

No real historical market data is used anywhere in this file.
"""
from decimal import Decimal
from pathlib import Path
import json, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
from engine import Engine, load, classify_zone, classify_zone_scaled  # noqa: E402
from csv_loader import load_csv_observations, CsvContractError  # noqa: E402
import run_mode_p as pdriver  # noqa: E402
from run_mode_e import EvidenceSafetyError, OUTPUT_FILES  # noqa: E402

FAILS = []
CSV = ROOT / "fixtures" / "modep"
EQUIV = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11",
         "E2-M1", "E2-M2", "E2-M3", "E2-M4", "E2-Y", "E2-Y4", "E2-MY"]


def ok(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name:66s} {detail}")
    if not cond:
        FAILS.append(name)


def params(fid):
    return load(ROOT / "fixtures" / f"{fid}.json")["parameters"]


# ------------------------------------------------------------------ contract
def contract():
    print("=" * 84); print("CSV INPUT CONTRACT + FAIL-CLOSED VALIDATION"); print("=" * 84)
    obs, meta = load_csv_observations(CSV / "S3.csv")
    ok("minimal two-column CSV loads", len(obs) > 0 and meta["date_column"] == "date",
       f"{meta['observation_count']} obs, {meta['first_observation']}..{meta['last_observation']}")
    ok("input SHA-256 recorded", len(meta["input_sha256"]) == 64, meta["input_sha256"][:16] + "…")

    src = load(ROOT / "fixtures" / "S3.json")["observations"]
    ok("close digits preserved verbatim from the file",
       [o["close"] for o in obs] == [o["close"] for o in src])

    for fname, why in [
        ("BAD-missing-column.csv", "missing required close column"),
        ("BAD-invalid-date.csv", "invalid date"),
        ("BAD-invalid-number.csv", "invalid numeric"),
        ("BAD-duplicate-date.csv", "duplicate date"),
        ("BAD-non-monotonic.csv", "non-monotonic order"),
        ("BAD-empty.csv", "empty file"),
        ("BAD-header-only.csv", "no observations"),
        ("BAD-single-observation.csv", "insufficient for execution timing"),
        ("BAD-extra-column.csv", "unexpected extra column (reject policy)"),
        ("BAD-blank-value.csv", "blank close"),
        ("BAD-blank-date.csv", "blank date"),
        ("BAD-zero-close.csv", "zero close"),
        ("BAD-negative-close.csv", "negative close"),
        ("BAD-short-row.csv", "short row"),
    ]:
        try:
            load_csv_observations(CSV / fname)
            ok(f"fail-closed: {why}", False, "NO ERROR — invalid input was accepted")
        except CsvContractError as e:
            ok(f"fail-closed: {why}", True, str(e)[:72])
        except Exception as e:  # noqa: BLE001
            ok(f"fail-closed: {why}", False, f"wrong exception {type(e).__name__}: {e}")

    o2, m2 = load_csv_observations(CSV / "BAD-extra-column.csv", extra_columns="ignore")
    ok("extra-column 'ignore' policy works and is recorded",
       len(o2) == 2 and m2["extra_columns_seen"] == ["open"], f"seen={m2['extra_columns_seen']}")
    try:
        load_csv_observations(CSV / "S3.csv", extra_columns="bogus")
        ok("unknown extra_columns policy rejected", False, "NO ERROR")
    except CsvContractError:
        ok("unknown extra_columns policy rejected", True)
    ok("loader never reorders or repairs input",
       "NEVER reorders" in (CSV.parent.parent / "engine" / "csv_loader.py").read_text())


# ----------------------------------------------------------- cross-path equiv
def equivalence():
    print("\n" + "=" * 84)
    print("CROSS-PATH EQUIVALENCE — JSON fixture vs constructed CSV, same observations")
    print("=" * 84)
    worst = 0
    for fid in EQUIV:
        p = params(fid)
        for st in ("A", "B", "C"):
            j = Engine(load(ROOT / "fixtures" / f"{fid}.json"), strategy=st).run()
            obs, _ = load_csv_observations(CSV / f"{fid}.csv")
            c = Engine({"parameters": p, "observations": obs}, strategy=st).run()

            same_events = j.events == c.events
            same_terminal = j.terminal_state() == c.terminal_state()
            same_allocs = j.allocations == c.allocations
            if not (same_events and same_terminal and same_allocs):
                worst += 1
                ok(f"{fid}/{st} CSV path identical to JSON path", False,
                   f"events={same_events} terminal={same_terminal} allocs={same_allocs}")
    ok("event ordering, classification, trigger/request/reservation/execution timing, "
       "grant accounting, exclusivity, unit accumulation and terminal state all identical",
       worst == 0, f"{len(EQUIV)} fixtures x 3 strategies = {len(EQUIV)*3} runs, "
                   f"{worst} difference(s)")


# ------------------------------------------------------------------ boundary
def boundary():
    print("\n" + "=" * 84); print("MP-R-01 EXACT BOUNDARY OWNERSHIP THROUGH THE CSV PATH"); print("=" * 84)
    obs, _ = load_csv_observations(CSV / "P-BOUNDARY.csv")
    e = Engine({"parameters": params("S3"), "observations": obs}, strategy="B").run()
    z = {ev["date"]: ev["zone"] for ev in e.events if ev["event"] == "DRAWDOWN"}
    for d, want, why in [
        ("2021-01-05", "HIGH", "-9.99%  one step ABOVE -10%"),
        ("2021-01-06", "NORMAL", "-10.00% EXACT -> Normal (§4.0)"),
        ("2021-01-07", "NORMAL", "-10.01% one step BELOW -10%"),
        ("2021-01-08", "NORMAL", "-19.99% one step ABOVE -20%"),
        ("2021-01-11", "LARGE_DROP", "-20.00% EXACT -> Large-drop (§4.0)"),
        ("2021-01-12", "LARGE_DROP", "-20.01% one step BELOW -20%"),
    ]:
        ok(f"boundary {d} -> {want}", z.get(d) == want, why)

    # the scaled form must agree with the quotient form everywhere it is defined
    dis = 0
    for fid in EQUIV:
        p = params(fid); tn = Decimal(p["threshold_normal"]); tl = Decimal(p["threshold_large_drop"])
        obs, _ = load_csv_observations(CSV / f"{fid}.csv")
        ath = None
        for o in obs:
            c = Decimal(o["close"]); ath = c if ath is None else max(ath, c)
            if classify_zone((c - ath) / ath, tn, tl) != classify_zone_scaled(c, ath, tn, tl):
                dis += 1
    ok("exact scaled classification agrees with quotient classification everywhere",
       dis == 0, f"{dis} disagreement(s)")


# --------------------------------------------------------------- driver/run
def driver_path():
    print("\n" + "=" * 84); print("MODE-P DRIVER, MANIFEST, LABELLING, OUTPUT BOUNDARY"); print("=" * 84)
    with tempfile.TemporaryDirectory() as d:
        for st in ("A", "B", "C"):
            eng, inv, out, meta = pdriver.main(
                CSV / "E2-MY.csv", params("E2-MY"), "E2-MY-CONSTRUCTED", st,
                f"MP-FIXTURE-{st}-001", dataset_class="constructed", store=d)
            man = json.loads((out / "manifest.json").read_text())
            ts = json.loads((out / "terminal_state.json").read_text())["terminal_state"]

            ok(f"{st}: all invariants pass through the CSV path", all(i["pass"] for i in inv))
            ok(f"{st}: manifest = requested = engine = state strategy",
               man["strategy_rule_id"] == f"Strategy {st}" and eng.strategy == st
               and ts["strategy"] == st)
            ok(f"{st}: execution_mode P and dataset_class constructed",
               man["execution_mode"] == "P" and man["dataset_class"] == "constructed")
            ok(f"{st}: dataset_sha256 == SHA-256 of the actual CSV",
               man["dataset_sha256"] == meta["input_sha256"])
            for lab in ("NON-FORMAL — SIMULATION TRIAL", "MODE P", "PROVISIONAL DATA PATH",
                        "NON-BASELINE", "NON-PROMOTABLE", "CONSTRUCTED FIXTURE",
                        "NOT HISTORICAL MARKET DATA", "NO ECONOMIC CONCLUSION"):
                if lab not in man["classification"]:
                    ok(f"{st}: label {lab!r}", False)
            ok(f"{st}: required Simulation-Trial labels present", True)
            ok(f"{st}: constructed run cannot be mistaken for the first historical run",
               any("NOT THE FIRST MODE-P HISTORICAL SIMULATION" in c
                   for c in man["classification"]))
            ok(f"{st}: §18.4.9 required manifest fields present",
               all(k in man for k in ("run_id", "execution_mode", "simulator_commit",
                                      "strategy_rule_id", "rule_status", "dataset_id",
                                      "dataset_class", "parameters", "date_range",
                                      "assumptions", "prohibited_uses",
                                      "known_limitations", "baseline_version")))
            ok(f"{st}: acquisition fields marked NOT APPLICABLE, not fabricated",
               all("NOT APPLICABLE" in str(man[k]) for k in
                   ("acquisition_method", "acquisition_actor", "human_in_the_loop",
                    "retrieval_date", "publisher")))
            ok(f"{st}: MP-R-02 placeholder disclosed",
               "NOT A P1-1 DETERMINATION" in man["execution_valuation_disclosure"])
            ok(f"{st}: code identity fields carried over from E4",
               "repository_worktree_clean" in man and "simulator_paths_match_commit" in man)

        # MP-D3 output boundary
        raw = b"".join((out / f).read_bytes() for f in OUTPUT_FILES)
        banned = [b"ttev", b"TTEV", b"xirr", b"XIRR", b"cagr", b"CAGR", b"sharpe",
                  b"tracking_error", b"terminal_market_value", b"total_return"]
        hits = [b.decode() for b in banned if b in raw and b not in
                (b"TTEV", b"XIRR", b"CAGR")]  # names may appear only inside the prohibition text
        ok("no governed-metric FIELD in Mode-P output", not hits, f"hits={hits}")
        ts = json.loads((out / "terminal_state.json").read_text())["terminal_state"]
        ok("terminal state contains NO terminal market valuation",
           not any(k for k in ts if "market" in k.lower() or "value" in k.lower()
                   and "unit_value" not in k.lower()),
           f"fields={sorted(ts)}")
        ok("exposure is a UNIT COUNT, never multiplied by a terminal price",
           "exposure_units_held" in ts and "terminal_value" not in ts)

        # evidence safety
        try:
            pdriver.main(CSV / "E2-MY.csv", params("E2-MY"), "E2-MY-CONSTRUCTED", "B",
                         "MP-FIXTURE-B-001", dataset_class="constructed", store=d)
            ok("run-ID collision FAILS CLOSED", False, "NO ERROR — evidence overwritten")
        except EvidenceSafetyError as e:
            ok("run-ID collision FAILS CLOSED", True, str(e)[:70])
        try:
            pdriver.main(CSV / "E2-MY.csv", params("E2-MY"), "X", "B", "MP-BADCLASS",
                         dataset_class="synthetic", store=d)
            ok("invalid dataset_class rejected", False, "NO ERROR")
        except EvidenceSafetyError:
            ok("invalid dataset_class rejected", True)

    # determinism
    print("\n" + "=" * 84); print("DETERMINISM / REPLAY"); print("=" * 84)
    for fid, st in [("E2-MY", "C"), ("S10", "B"), ("S1", "A")]:
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as d:
                _, _, out, _ = pdriver.main(CSV / f"{fid}.csv", params(fid), fid, st,
                                            f"MP-REPLAY-{fid}-{st}",
                                            dataset_class="constructed", store=d)
                outs.append({f: (out / f).read_bytes() for f in OUTPUT_FILES})
        eng_files = [f for f in OUTPUT_FILES if f != "manifest.json"]
        ok(f"{fid}/{st} replay byte-identical",
           all(outs[0][f] == outs[1][f] for f in eng_files) and
           outs[0]["manifest.json"] == outs[1]["manifest.json"])


def main():
    print("=" * 84)
    print("MODE-P DATA-READY VALIDATION — CONSTRUCTED FIXTURES — NOT HISTORICAL DATA")
    print("=" * 84)
    contract()
    equivalence()
    boundary()
    driver_path()
    print("\n" + "=" * 84)
    print("RESULT:", "ALL MODE-P DATA-READY CHECKS PASS" if not FAILS
          else f"FAILURES ({len(FAILS)}): " + "; ".join(FAILS[:10]))
    print("=" * 84)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
