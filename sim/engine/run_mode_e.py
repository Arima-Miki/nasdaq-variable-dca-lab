#!/usr/bin/env python3
"""Mode-E run driver. Writes manifest, event log, terminal state and assertion
results to the external Mode-E store, OUTSIDE the Git worktree.

NON-FORMAL — SIMULATION TRIAL. Engine state only; no evaluation metric.
"""
import json, os, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from engine import Engine, load, CLASSIFICATION  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
STORE = Path.home() / "research-materials" / "nasdaq-variable-dca-lab" / "simulation-trial-mode-e"


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a],
                          capture_output=True, text=True).stdout.strip()


def sha256(p):
    import hashlib
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class EvidenceSafetyError(RuntimeError):
    """Raised INSTEAD of writing, whenever a write would damage or misdescribe
    the evidence record. Every check that raises this runs BEFORE any file is
    created, so a failed run leaves the store byte-for-byte as it was."""


OUTPUT_FILES = ("manifest.json", "event_log.json", "terminal_state.json", "assertions.json")


def simulator_paths_match_commit():
    """E4 CODE-IDENTITY CHECK.

    `git status --porcelain` over the whole repository conflates two very
    different situations:

      (a) the simulator implementation has uncommitted edits  -> evidence is
          NOT reproducible from the recorded commit;
      (b) unrelated untracked research drafts sit in the worktree -> evidence
          IS reproducible; the repository is merely not pristine.

    The Owner-mandated M01/M02 drafts put this repository permanently in state
    (b). Reporting a bare `worktree_clean: false` is truthful but useless, and
    setting it true would be a lie. So both facts are recorded separately, and
    THIS field is the one that bears on reproducibility: it is scoped to the
    simulator paths only.
    """
    return git("status", "--porcelain", "--", "sim") == ""


def main(fixture_id="S3", strategy="B", run_id="E1-S3-B-001", run_date="2026-08-13"):
    """run_id distinguishes E1 from E2 evidence; E1 outputs are never overwritten."""
    fx_path = REPO / "sim" / "fixtures" / f"{fixture_id}.json"
    fx = load(fx_path)
    # E3 DEFECT FIX (recorded openly). The first form of this line was
    # `Engine(fx).run()`, which DISCARDED the `strategy` argument and always ran
    # Strategy B while the manifest recorded whatever was requested. With only
    # Strategy B implemented (E1/E2) it produced no wrong output, but the moment
    # A and C became runnable it would have written Strategy-B engine state under
    # a Strategy-A or Strategy-C label. Caught before any E3 evidence was written.
    eng = Engine(fx, strategy=strategy).run()

    out = STORE / run_id

    # ---- E4 EVIDENCE-SAFETY GATE (all checks precede any write) ----------
    #
    # DEFECT FIXED IN E4, recorded openly: the previous form of this function
    # called `out.mkdir(parents=True, exist_ok=True)` and then wrote each output
    # unconditionally. Re-using a run ID therefore SILENTLY OVERWROTE preserved
    # E1/E2/E3 evidence, with no error and no trace. Under Baseline v2 §18.4.4
    # ("an old experimental run is never promoted; it is re-run, or it is not
    # formal") destroying prior evidence by accident is exactly the failure the
    # store exists to prevent. The driver now FAILS CLOSED.
    existing = [f for f in OUTPUT_FILES if (out / f).exists()]
    if existing:
        raise EvidenceSafetyError(
            f"run_id '{run_id}' already holds evidence ({', '.join(existing)}). "
            f"Refusing to overwrite preserved evidence. Choose a new run_id. "
            f"E4 provides no in-place replacement workflow by design.")

    # Strategy-label integrity, end to end. The manifest, the object actually
    # constructed, and the state the engine wrote must name ONE strategy.
    ts_preview = eng.terminal_state()
    if not (strategy == eng.strategy == ts_preview["strategy"]):
        raise EvidenceSafetyError(
            f"strategy-label disagreement: requested={strategy!r} "
            f"engine={eng.strategy!r} terminal_state={ts_preview['strategy']!r}. "
            f"Refusing to write evidence.")

    # Fixture identity. The hash recorded in the manifest must be the hash of
    # the file this run actually loaded.
    dataset_sha = sha256(fx_path)
    if fx.get("fixture_id") not in (None, fixture_id):
        raise EvidenceSafetyError(
            f"fixture identity disagreement: requested {fixture_id!r} but the "
            f"loaded file declares {fx.get('fixture_id')!r}.")

    out.mkdir(parents=True, exist_ok=True)

    manifest = {
        "classification": CLASSIFICATION,
        "prohibited_uses": [
            "investment performance", "expected return", "historical performance",
            "Baseline result", "qualification evidence", "strategy superiority",
            "support for any live-investment decision",
        ],
        "run_id": run_id,
        "execution_mode": "E",
        "baseline_version": "v2",
        "governing_authorization": "simulation_trial_mode_e_authorization_decision.md",
        "simulator_commit": git("rev-parse", "HEAD"),
        # E4: these two replace the former single `simulator_worktree_clean`,
        # which conflated repository tidiness with simulator reproducibility.
        # See simulator_paths_match_commit() for why the distinction matters.
        "repository_worktree_clean": git("status", "--porcelain") == "",
        "simulator_paths_match_commit": simulator_paths_match_commit(),
        "simulator_paths_scope": "sim/",
        "strategy_rule_id": f"Strategy {strategy}",
        "rule_status": {
            "A": "BASELINE RULE (frozen, Baseline v2 §4.1, OD-01)",
            "B": "BASELINE RULE (frozen, Baseline v2 §4.2, OD-09)",
            "C": "BASELINE RULE (frozen, Baseline v2 §4.3, OD-05)",
        }[strategy],
        "dataset_id": fixture_id,
        "dataset_class": "synthetic",
        "dataset_sha256": dataset_sha,
        "parameters": fx["parameters"],
        "date_range": [fx["observations"][0]["date"], fx["observations"][-1]["date"]],
        "assumptions": [
            "Execution valuation rule is a declared FIXTURE PARAMETER, not a Baseline "
            "execution-price determination. P1-1 and OD-04 untouched.",
            "Exact Decimal arithmetic; no floating-point tolerance policy. M-7 remains OPEN.",
            "No execution-failure scenario (M-4 avoided). No zero-unit acceptance semantics "
            "or reason codes (M-6 avoided).",
        ],
        "outputs_produced": ["event_log.json", "terminal_state.json", "assertions.json"],
        "outputs_excluded": [
            "NO evaluation metric governed by M-1..M-8: no TTEV, XIRR, CAGR, total or "
            "annualised return, tracking statistic, or any performance measure."
        ],
        # E3: these were hardcoded to the E1 walking-skeleton situation. A manifest
        # that understates its own coverage is as much an evidence defect as one
        # that overstates it, so they are now derived from the actual run.
        "known_limitations": [
            f"Single run: Strategy {strategy}, fixture {fixture_id}. Engine state only.",
            "Synthetic fixture. NOT market data. No economic or performance claim.",
            "Invariant 18 is not reachable within a single-strategy run.",
            "M-7 remains OPEN: exact Decimal arithmetic, no tolerance policy adopted.",
        ],
        "run_date": run_date,
    }

    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "event_log.json").write_text(json.dumps(
        {"classification": CLASSIFICATION, "run_id": run_id, "events": eng.events},
        indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "terminal_state.json").write_text(json.dumps(
        {"classification": CLASSIFICATION, "run_id": run_id, "terminal_state": eng.terminal_state()},
        indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    inv = eng.invariants()
    (out / "assertions.json").write_text(json.dumps(
        {"classification": CLASSIFICATION, "run_id": run_id,
         "all_pass": all(i["pass"] for i in inv), "invariants": inv},
        indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"run_id={run_id} out={out}")
    print("all_invariants_pass=", all(i["pass"] for i in inv))
    return eng, inv, out


if __name__ == "__main__":
    import sys as _s
    if len(_s.argv) >= 4:
        main(_s.argv[1], _s.argv[2], _s.argv[3])
    else:
        main()
