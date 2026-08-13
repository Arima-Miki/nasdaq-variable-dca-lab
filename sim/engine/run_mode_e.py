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


def main(fixture_id="S3", strategy="B", run_id="E1-S3-B-001", run_date="2026-08-13"):
    """run_id distinguishes E1 from E2 evidence; E1 outputs are never overwritten."""
    fx_path = REPO / "sim" / "fixtures" / f"{fixture_id}.json"
    fx = load(fx_path)
    eng = Engine(fx).run()

    out = STORE / run_id
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
        "simulator_worktree_clean": git("status", "--porcelain") == "",
        "strategy_rule_id": f"Strategy {strategy}",
        "rule_status": "BASELINE RULE (frozen, Baseline v2 §4.2/§4.4)",
        "dataset_id": fixture_id,
        "dataset_class": "synthetic",
        "dataset_sha256": sha256(fx_path),
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
        "known_limitations": [
            f"Strategy B only; fixture {fixture_id}.",
            "Strategies A and C are not implemented in Mode E to date.",
            "Invariants 3 and 14 are unreachable with a single strategy.",
            "Scenarios S1/S2/S4-S11 of the approved suite are not implemented.",
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
