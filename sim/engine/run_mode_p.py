#!/usr/bin/env python3
"""Mode-P run driver — provisional data path.

NON-FORMAL — SIMULATION TRIAL — MODE P — PROVISIONAL DATA PATH —
NON-BASELINE — NON-PROMOTABLE.

Reuses the preserved Mode-E engine unchanged. This file adapts INPUT and
EXECUTION CONTEXT only; it contains no Strategy A/B/C logic and reinterprets no
strategy mechanic.

Reports only the MP-D3-permitted definition-free engine quantities. No metric
governed by M-1..M-8 is computed anywhere in this module, and none may be added
without a separate Owner Decision.
"""
import json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from engine import Engine  # noqa: E402
from csv_loader import build_fixture  # noqa: E402
from run_mode_e import (EvidenceSafetyError, OUTPUT_FILES,  # noqa: E402
                        simulator_paths_match_commit, git)

REPO = Path(__file__).resolve().parents[2]
STORE = Path.home() / "research-materials" / "nasdaq-variable-dca-lab" / "simulation-trial-mode-p"

CLASSIFICATION_P = [
    "NON-FORMAL — SIMULATION TRIAL",
    "MODE P",
    "PROVISIONAL DATA PATH",
    "PROVISIONAL ECONOMIC SIMULATION",
    "NOT QUALIFIED",
    "NON-BASELINE",
    "NON-PROMOTABLE",
]

CONSTRUCTED_FIXTURE_LABELS = [
    "CONSTRUCTED FIXTURE",
    "NOT HISTORICAL MARKET DATA",
    "NO ECONOMIC CONCLUSION",
    "NOT THE FIRST MODE-P HISTORICAL SIMULATION",
]

PROHIBITED_USES = [
    "investment performance", "expected return", "historical performance",
    "Baseline result", "qualification evidence", "Primary Proxy approval",
    "strategy superiority", "support for any live-investment decision",
]

# MP-D3: the permitted report surface. Terminal market valuation is absent by
# construction, not by filtering — the engine computes none.
PERMITTED_TERMINAL_FIELDS = (
    "strategy", "reference_high", "final_dd", "final_zone",
    "budget_units_granted", "budget_units_available",
    "budget_units_reserved_outstanding", "budget_units_executed",
    "cash_granted_jpy", "cash_deployed_jpy", "cash_remaining_jpy",
    "exposure_units_held", "allocations_committed",
    "signals_suppressed_monthly_exclusivity",
)


def permitted_terminal_state(ts):
    """MP-D3 output boundary. Returns only definition-free engine quantities.

    `exposure_units_held` is a UNIT COUNT, not a valuation: no price is applied
    to it here or anywhere downstream. Multiplying it by a terminal price would
    reconstruct TTEV (§13.1) and engage M-5, which MP-D3 and §18.4.3 both bar.
    """
    return {k: ts[k] for k in PERMITTED_TERMINAL_FIELDS if k in ts}


def main(csv_path, parameters, dataset_id, strategy, run_id,
         dataset_class="constructed", acquisition=None, run_date="2026-08-14",
         extra_columns="reject", store=None, extra_labels=None):
    """Execute one Mode-P run.

    `dataset_class` MUST be "constructed" for fixture validation and
    "provisional" for a real historical dataset (§18.4.9).
    `acquisition` carries the human-in-the-loop record; fields that only make
    sense for real acquisition are marked NOT APPLICABLE rather than fabricated.
    `extra_labels`, if given, are appended verbatim to the manifest
    classification list. Used to carry dataset-specific mandatory disclosure
    labels (e.g. an Owner-imposed §18.4.7 release condition) without altering
    the shared CLASSIFICATION_P/CONSTRUCTED_FIXTURE_LABELS behaviour. Defaults
    to None, which is a no-op — existing callers are unaffected.
    """
    if dataset_class not in ("constructed", "provisional"):
        raise EvidenceSafetyError(
            f"dataset_class must be 'constructed' or 'provisional', got {dataset_class!r}")

    store = Path(store) if store else STORE
    fixture, meta = build_fixture(csv_path, parameters, dataset_id,
                                  extra_columns=extra_columns)
    eng = Engine(fixture, strategy=strategy).run()

    out = store / run_id

    # ---- E4 evidence-safety gate, carried over unweakened -----------------
    existing = [f for f in OUTPUT_FILES if (out / f).exists()]
    if existing:
        raise EvidenceSafetyError(
            f"run_id '{run_id}' already holds evidence ({', '.join(existing)}). "
            f"Refusing to overwrite preserved evidence. Choose a new run_id.")

    ts_all = eng.terminal_state()
    if not (strategy == eng.strategy == ts_all["strategy"]):
        raise EvidenceSafetyError(
            f"strategy-label disagreement: requested={strategy!r} "
            f"engine={eng.strategy!r} state={ts_all['strategy']!r}. Refusing to write.")

    if acquisition is None:
        acquisition = {}
    if dataset_class == "constructed":
        acquisition = {
            "acquisition_method": "NOT APPLICABLE — constructed fixture, authored locally",
            "acquisition_actor": "NOT APPLICABLE — constructed fixture",
            "human_in_the_loop": "NOT APPLICABLE — constructed fixture",
            "retrieval_date": "NOT APPLICABLE — constructed fixture",
            "publisher": "NOT APPLICABLE — constructed fixture",
            **acquisition,
        }

    manifest = {
        "classification": CLASSIFICATION_P + (
            CONSTRUCTED_FIXTURE_LABELS if dataset_class == "constructed" else []) +
            (list(extra_labels) if extra_labels else []),
        "prohibited_uses": PROHIBITED_USES,
        "run_id": run_id,
        "execution_mode": "P",
        "baseline_version": "v2",
        "governing_decision": "simulation_trial_mode_p_decision_boundary.md (91378fe)",
        "governing_plan": "simulation_trial_mode_p_execution_plan.md (535de39)",
        "simulator_commit": git("rev-parse", "HEAD"),
        "repository_worktree_clean": git("status", "--porcelain") == "",
        "simulator_paths_match_commit": simulator_paths_match_commit(),
        "simulator_paths_scope": "sim/",
        "strategy_rule_id": f"Strategy {strategy}",
        "rule_status": {
            "A": "BASELINE RULE (frozen, Baseline v2 §4.1, OD-01)",
            "B": "BASELINE RULE (frozen, Baseline v2 §4.2, OD-09)",
            "C": "BASELINE RULE (frozen, Baseline v2 §4.3, OD-05)",
        }[strategy],
        "dataset_id": dataset_id,
        "dataset_class": dataset_class,
        "dataset_sha256": meta["input_sha256"],
        "input_identity": {k: meta[k] for k in (
            "input_filename", "input_bytes", "observation_count",
            "first_observation", "last_observation", "date_column",
            "close_column", "extra_columns_policy", "extra_columns_seen")},
        "denomination": parameters.get("denomination", "NOT DECLARED"),
        "return_composition": parameters.get("return_composition", "NOT DECLARED"),
        **acquisition,
        "parameters": parameters,
        "date_range": [meta["first_observation"], meta["last_observation"]],
        "configuration_identity": {
            "boundary_rule": "MP-R-01 exact scaled comparison; no tolerance; M-7 OPEN",
            "execution_valuation": "MP-R-02 next available observation's close",
            "decimal_precision": 40,
        },
        "execution_valuation_disclosure":
            "PROVISIONAL EXECUTION VALUATION PLACEHOLDER — NOT A P1-1 DETERMINATION. "
            "Executes at the close of the next available observation strictly after the "
            "signal observation. It ignores order cutoff and NAV settlement lag, so it "
            "executes EARLIER than a real fund would. P1-1 and OD-04 remain unresolved.",
        "assumptions": [
            "Zero costs modelled (P1-4 open).",
            "No FX conversion modelled (P1-7 open).",
            "Return composition is declared, not derived (P1-3 open).",
            "The span carries NO P1-5 / P1-6 significance.",
            "No execution failure modelled (M-4 avoided).",
            "No zero-unit-acceptance semantics (M-6 avoided).",
            "Exact Decimal arithmetic; no tolerance policy. M-7 remains OPEN.",
        ],
        "outputs_produced": list(OUTPUT_FILES),
        "outputs_excluded": [
            "NO metric governed by M-1..M-8: no TTEV, XIRR, CAGR, total or annualised "
            "return, tracking statistic, Sharpe ratio, terminal market valuation, "
            "strategy ranking, or any performance measure. M-1, M-5 and M-8 remain "
            "unresolved.",
        ],
        "known_limitations": [
            f"Single run: Strategy {strategy}, dataset {dataset_id} ({dataset_class}).",
            "Mode-P output is NON-FORMAL and can never become formal by relabelling "
            "(§18.4.2, §18.4.3). Formal use requires a fresh formal execution (§18.4.4).",
            "Invariant 18 is not reachable within a single-strategy run.",
        ],
        "run_date": run_date,
    }
    if dataset_class == "constructed":
        manifest["known_limitations"].insert(0,
            "CONSTRUCTED FIXTURE — invented data. NOT historical market data and NOT "
            "provisional economic evidence. This run is NOT the first Mode-P historical "
            "simulation and must never be described as one.")

    out.mkdir(parents=True, exist_ok=True)
    body = {"classification": manifest["classification"], "run_id": run_id}

    def write(name, payload):
        (out / name).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    write("manifest.json", manifest)
    write("event_log.json", {**body, "events": eng.events})
    write("terminal_state.json", {**body, "terminal_state": permitted_terminal_state(ts_all),
                                  "output_boundary": "MP-D3: definition-free engine quantities "
                                                     "only; no terminal market valuation"})
    inv = eng.invariants()
    write("assertions.json", {**body, "all_pass": all(i["pass"] for i in inv),
                              "invariants": inv})

    print(f"run_id={run_id} out={out} class={dataset_class}")
    print("all_invariants_pass=", all(i["pass"] for i in inv))
    return eng, inv, out, meta
