#!/usr/bin/env python3
"""Mode-P terminal-valuation reporting layer.

NON-FORMAL — SIMULATION TRIAL — MODE P — TERMINAL VALUATION — PROVISIONAL —
NOT BASELINE TTEV — SIMULATION-TRIAL ONLY.

Implements MP-EV-D1..D4 (Owner Decision, commit 00b2b4a, tag
simulation-trial-mode-p-terminal-valuation-decision-20260814), which
narrowly amends MP-D3 to permit reporting one new quantity over the
already-preserved FIRST MODE-P HISTORICAL SIMULATION (MP-H2-*-001, commit
da85b66).

This module contains NO Strategy A/B/C logic, NO engine mechanics, and runs
NO new simulation. It reads already-preserved MP-H2-*-001 terminal states
and computes only the fields MP-EV-D3 permits, using exact Decimal
arithmetic. It is a read-only report over frozen prior evidence.
"""
import hashlib
import json
import subprocess
import sys
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 40

REPO = Path(__file__).resolve().parents[2]
STORE = Path.home() / "research-materials" / "nasdaq-variable-dca-lab" / "simulation-trial-mode-p"

DATASET_SHA256 = "94c5ce8f586c89f1f4f3d4409856ab98c511a503e28d84757c7895df311225e7"
DECISION_COMMIT = "00b2b4ac6e982511d5e74394125ed870e7ff6275"
DECISION_TAG = "simulation-trial-mode-p-terminal-valuation-decision-20260814"

# MP-EV-D3, item 7's exact authorized formula:
#   (terminal economic value - cumulative funding) / cumulative funding

CLASSIFICATION_EV = [
    "NON-FORMAL — SIMULATION TRIAL",
    "MODE P",
    "TERMINAL VALUATION",
    "PROVISIONAL",
    "NOT QUALIFIED",
    "NON-BASELINE",
    "NON-PROMOTABLE",
    "MODE-P TERMINAL ECONOMIC VALUE — NOT BASELINE TTEV — SIMULATION-TRIAL ONLY",
    "NDXJPY IS AN ACTIVE C-1 QUALIFICATION CANDIDATE — THIS RUN IS NOT EVIDENCE ABOUT IT",
    "NOT A PRIMARY PROXY SELECTION — P1-2 REMAINS OPEN",
    "SPAN CARRIES NO P1-5 / P1-6 SIGNIFICANCE",
    "BACK-TESTED VS ACTUAL HISTORY NOT ESTABLISHED FOR THIS SEGMENT",
    "RETURN COMPOSITION DECLARED, NOT VERIFIED — P1-3 OPEN",
]

PROHIBITED_USES = [
    "investment performance", "expected return", "historical performance",
    "Baseline result", "qualification evidence", "Primary Proxy approval",
    "strategy superiority", "strategy ranking", "support for any live-investment decision",
    "CAGR", "XIRR", "annualized return", "Sharpe ratio", "tracking statistic",
    "statistical significance claim", "'better'/'worse'/'optimal' characterization",
]

ANTI_CONTAMINATION_DISCLOSURE = (
    "The NDXJPY Mode-P results were already known. The A/B/C mechanical differences "
    "observed in MP-H1/MP-H2 were already known. These results are NOT qualification "
    "evidence. No Primary Proxy inference is made. O-4 remains unchanged. All P1-x "
    "states remain unchanged. HG-8 remains unchanged. Stage G / Stage H remain "
    "unchanged. Phase 2 remains BLOCKED."
)

# MP-EV-D3's exact permitted-field surface. Anything outside this set is a
# defect in this module, not an authorized output.
ALLOWED_RESULT_FIELDS = {
    "strategy", "source_run_id", "source_terminal_state_sha256", "dataset_sha256",
    "simulator_commit", "terminal_valuation_decision_commit",
    "terminal_valuation_decision_tag", "terminal_price", "terminal_price_date",
    "acquired_exposure_units", "exposure_market_value_jpy", "cash_available_jpy",
    "cash_reserved_unexecuted_jpy", "total_unconverted_cash_jpy",
    "combined_terminal_economic_value_jpy", "cumulative_funding_jpy",
    "simple_funding_relative_return",
}
BANNED_NAME_TOKENS = ("cagr", "xirr", "annualiz", "sharpe", "tracking_error",
                       "benchmark", "rank", "superior", "score")

OUTPUT_FILES = ("manifest.json", "result.json")


class EvidenceSafetyError(RuntimeError):
    """Raised INSTEAD of writing or computing, whenever an operation would
    misdescribe evidence, diverge from preserved state, or produce an
    unauthorized field."""


def git(*a):
    return subprocess.run(["git", "-C", str(REPO), *a],
                          capture_output=True, text=True).stdout.strip()


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _verify_terminal_price():
    """MP-EV-D1: verify the terminal price from the preserved dataset itself
    rather than trusting a hardcoded literal."""
    csv_path = STORE / "dataset" / "MP-H1_NDXJPY_2018-01-02_2020-06-26.csv"
    last_line = csv_path.read_text().strip().splitlines()[-1]
    date_str, close_str = last_line.split(",")
    return date_str, Decimal(close_str)


TERMINAL_PRICE_DATE, TERMINAL_PRICE = _verify_terminal_price()


def load_source(source_run_id):
    src = STORE / source_run_id
    manifest = json.loads((src / "manifest.json").read_text())
    ts_doc_text = (src / "terminal_state.json").read_text()
    ts_doc = json.loads(ts_doc_text)
    ts = ts_doc["terminal_state"]
    if manifest["dataset_sha256"] != DATASET_SHA256:
        raise EvidenceSafetyError(f"{source_run_id}: dataset_sha256 mismatch")
    if not manifest.get("simulator_paths_match_commit"):
        raise EvidenceSafetyError(
            f"{source_run_id}: simulator_paths_match_commit is not True — refusing to "
            f"build a terminal-valuation report on a non-preserved-commit source run")
    return manifest, ts, sha256_text(ts_doc_text)


def compute(strategy, source_run_id):
    manifest, ts, ts_sha = load_source(source_run_id)
    if ts["strategy"] != strategy:
        raise EvidenceSafetyError(
            f"strategy label mismatch: requested {strategy!r}, source terminal_state "
            f"declares {ts['strategy']!r}")

    unit_value = Decimal(manifest["parameters"]["unit_value_jpy"])
    acquired_units = Decimal(ts["exposure_units_held"])
    available_units = Decimal(ts["budget_units_available"])
    reserved_units = Decimal(ts["budget_units_reserved_outstanding"])
    cash_remaining = Decimal(ts["cash_remaining_jpy"])
    cash_granted = Decimal(ts["cash_granted_jpy"])

    # MP-EV-D2: cash available and cash reserved-but-unexecuted, kept apart
    # from acquired exposure and disclosed separately.
    cash_available = available_units * unit_value
    cash_reserved = reserved_units * unit_value
    total_unconverted = cash_available + cash_reserved

    # Integrity cross-check against the engine's own already-reported field.
    # Fail closed rather than silently diverge from preserved evidence.
    if total_unconverted != cash_remaining:
        raise EvidenceSafetyError(
            f"{strategy}: computed total_unconverted_cash_jpy {total_unconverted} != "
            f"preserved cash_remaining_jpy {cash_remaining} — accounting is ambiguous")

    # MP-EV-D1: value ONLY actually-acquired (executed) exposure, never the
    # reserved-but-unexecuted portion, at the verified terminal close.
    exposure_market_value = acquired_units * TERMINAL_PRICE
    combined_value = exposure_market_value + total_unconverted

    if cash_granted == 0:
        raise EvidenceSafetyError(f"{strategy}: cumulative funding is zero; return undefined")
    simple_return = (combined_value - cash_granted) / cash_granted

    result = {
        "strategy": strategy,
        "source_run_id": source_run_id,
        "source_terminal_state_sha256": ts_sha,
        "dataset_sha256": manifest["dataset_sha256"],
        "simulator_commit": manifest["simulator_commit"],
        "terminal_valuation_decision_commit": DECISION_COMMIT,
        "terminal_valuation_decision_tag": DECISION_TAG,
        "terminal_price": str(TERMINAL_PRICE),
        "terminal_price_date": TERMINAL_PRICE_DATE,
        "acquired_exposure_units": str(acquired_units),
        "exposure_market_value_jpy": str(exposure_market_value),
        "cash_available_jpy": str(cash_available),
        "cash_reserved_unexecuted_jpy": str(cash_reserved),
        "total_unconverted_cash_jpy": str(total_unconverted),
        "combined_terminal_economic_value_jpy": str(combined_value),
        "cumulative_funding_jpy": str(cash_granted),
        "simple_funding_relative_return": str(simple_return),
    }

    extra = set(result) - ALLOWED_RESULT_FIELDS
    if extra:
        raise EvidenceSafetyError(f"unauthorized field(s) computed: {extra}")
    for k in result:
        low = k.lower()
        if any(t in low for t in BANNED_NAME_TOKENS):
            raise EvidenceSafetyError(f"banned-metric-shaped field name: {k}")

    return result, manifest


def main(strategy, source_run_id, run_id, run_date="2026-08-14", store=None):
    store = Path(store) if store else STORE
    result, source_manifest = compute(strategy, source_run_id)

    out = store / run_id
    existing = [f for f in OUTPUT_FILES if (out / f).exists()]
    if existing:
        raise EvidenceSafetyError(
            f"run_id '{run_id}' already holds evidence ({', '.join(existing)}). "
            f"Refusing to overwrite preserved evidence. Choose a new run_id.")

    manifest = {
        "classification": CLASSIFICATION_EV,
        "prohibited_uses": PROHIBITED_USES,
        "anti_contamination_disclosure": ANTI_CONTAMINATION_DISCLOSURE,
        "run_id": run_id,
        "execution_mode": "P-TERMINAL-VALUATION",
        "baseline_version": "v2",
        "governing_decision": f"simulation_trial_mode_p_terminal_valuation_decision.md "
                               f"({DECISION_COMMIT[:7]}, tag {DECISION_TAG})",
        "governing_mode_p_decision": "simulation_trial_mode_p_decision_boundary.md (91378fe)",
        "valuation_layer_commit": git("rev-parse", "HEAD"),
        "valuation_layer_worktree_clean_sim": git("status", "--porcelain", "--", "sim") == "",
        "source_run_id": source_run_id,
        "source_simulator_commit": result["simulator_commit"],
        "source_manifest_dataset_sha256": result["dataset_sha256"],
        "mp_ev_d1": "Terminal valuation price = close of the dataset's final observation "
                    f"({TERMINAL_PRICE_DATE} = {TERMINAL_PRICE}), verified from the preserved "
                    "dataset file itself. PROVISIONAL TERMINAL VALUATION CONVENTION — MODE P "
                    "ONLY. NOT a P1-1 determination. MP-R-02 untouched.",
        "mp_ev_d2": "Reserved-but-unexecuted allocations remain on the cash side, disclosed "
                    "separately (cash_reserved_unexecuted_jpy) from acquired exposure "
                    "(acquired_exposure_units, which counts ONLY executed units). Not "
                    "converted into exposure units.",
        "mp_ev_d3": "Reportable-output boundary amended narrowly per the governing decision. "
                    "No CAGR, XIRR, annualized return, statistical claim, or "
                    "comparative-superiority statement is computed or permitted. "
                    "simple_funding_relative_return uses the exact authorized formula "
                    "(terminal economic value - cumulative funding) / cumulative funding.",
        "mp_ev_d4": ANTI_CONTAMINATION_DISCLOSURE,
        "run_date": run_date,
    }

    out.mkdir(parents=True, exist_ok=True)

    def write(name, payload):
        (out / name).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    write("manifest.json", manifest)
    write("result.json", {"classification": CLASSIFICATION_EV, "run_id": run_id, **result})

    print(f"run_id={run_id} out={out}")
    return result, manifest, out


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("usage: run_mode_p_terminal.py STRATEGY SOURCE_RUN_ID RUN_ID", file=sys.stderr)
        raise SystemExit(2)
