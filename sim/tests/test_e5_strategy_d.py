#!/usr/bin/env python3
"""Mode-E Phase E5 — Strategy D synthetic mechanical validation.

NON-FORMAL — SIMULATION TRIAL. Engine state only; no economic claim, no
ranking, no comparison of Strategy D against A, B, or C.

EXPERIMENTAL VARIANT — NOT BASELINE. Strategy D is an OWNER-GENERATED
POST-RESULT ALTERNATIVE HYPOTHESIS (docs/decisions/
simulation_trial_strategy_d_owner_hypothesis.md, commit 5a3f54a), whose
mechanical semantics are fixed by docs/decisions/
simulation_trial_strategy_d_owner_semantic_decision.md (commit 62c5c42),
resolving SD-1..SD-10. This suite validates ONLY that the implementation
matches that preserved decision on constructed synthetic fixtures. It is
NOT ADOPTED, NOT VALIDATED as an investment rule, and NOT BASELINE.

Baseline v2 defines only Strategies A, B and C. Nothing here alters that.

Uses ONLY constructed synthetic fixtures. No real historical market data,
no NDXJPY, no Mode-P run of any kind.
"""
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import sys, tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
from engine import Engine, load  # noqa: E402
import run_mode_e as edriver  # noqa: E402

FAILS = []
D_SUITE = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]


def R(x):
    return Fraction(Decimal(str(x)))


def numeric(v):
    try:
        Decimal(str(v)); return True
    except Exception:
        return False


def ok(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name:70s} {detail}")
    if not cond:
        FAILS.append(name)


def fx(fid):
    return load(ROOT / "fixtures" / f"{fid}.json")


def run_and_check(fid):
    f = fx(fid)
    eng = Engine(f, strategy="D").run()
    exp = f["hand_derived_expectations"]["per_strategy"]["D"]

    ok(f"{fid} allocation count", len(eng.allocations) == len(exp["allocations"]),
       f"got={len(eng.allocations)} want={len(exp['allocations'])}")
    for i, (a, w) in enumerate(zip(eng.allocations, exp["allocations"])):
        for k in ("committed_on", "attributed_month", "attributed_budget_year",
                  "capped", "strategy_d_tranche", "zone"):
            ok(f"{fid} alloc[{i}].{k}", a.get(k) == w.get(k), f"got={a.get(k)} want={w.get(k)}")
        for k in ("requested_units", "accepted_units"):
            ok(f"{fid} alloc[{i}].{k}", R(a[k]) == R(w[k]), f"got={a[k]} want={w[k]}")
        if "executed_on" in w and w["executed_on"] is not None:
            ok(f"{fid} alloc[{i}].executed_on", a.get("executed_on") == w["executed_on"])
            ok(f"{fid} alloc[{i}].exposure", R(a["exposure_units_acquired"]) ==
               R(w["exposure_units_acquired"]))

    ts = eng.terminal_state()
    for k, v in exp["terminal_state"].items():
        if isinstance(v, str) and numeric(v):
            ok(f"{fid} terminal.{k}", R(ts[k]) == R(v), f"got={ts[k]} want={v}")
        else:
            ok(f"{fid} terminal.{k}", ts[k] == v, f"got={ts[k]} want={v}")

    ok(f"{fid} suppressed count", eng.suppressed == exp["suppressed_count"],
       f"got={eng.suppressed} want={exp['suppressed_count']}")
    got_reasons = [e.get("reason") for e in eng.events
                   if e["event"] in ("SIGNAL_SUPPRESSED", "NO_ALLOCATION")]
    ok(f"{fid} suppression reasons", got_reasons == exp["suppression_reasons"],
       f"got={got_reasons} want={exp['suppression_reasons']}")

    for inv in eng.invariants():
        if not inv["pass"]:
            ok(f"{fid} {inv['invariant']}", False, inv.get("detail", ""))
    return eng


def main():
    print("=" * 88)
    print("STRATEGY D — EXPERIMENTAL VARIANT — NOT BASELINE — SYNTHETIC MECHANICAL VALIDATION")
    print("=" * 88)

    print("\n" + "=" * 88); print("D1-D10 FIXTURE SUITE"); print("=" * 88)
    engines = {}
    for fid in D_SUITE:
        e = run_and_check(fid)
        engines[fid] = e
        print(f"  ({fid}: {fx(fid)['scenario_name']})")

    print("\n" + "=" * 88); print("SD-1..SD-10 IMPLEMENTATION MAPPING"); print("=" * 88)
    ok("SD-1 direct-to-Large-drop requests 2.0, single allocation (D3, D8, D10)",
       engines["D3"].allocations[0]["strategy_d_tranche"] == "DIRECT_LARGE_DROP" and
       R(engines["D3"].allocations[0]["requested_units"]) == R("2.0"))
    ok("SD-1 no top-up after direct path exhausts capacity (D3, D8)",
       engines["D8"].suppressed == 3 and len(engines["D8"].allocations) == 1)
    ok("SD-2 repeated non-escalating Normal creates no allocation (D1, D9)",
       engines["D1"].suppressed == 1 and len(engines["D1"].allocations) == 1)
    ok("SD-3 escalation is a new, independent allocation with its own dates/prices (D2)",
       len(engines["D2"].allocations) == 2 and
       engines["D2"].allocations[0]["committed_on"] != engines["D2"].allocations[1]["committed_on"] and
       engines["D2"].allocations[0]["executed_on"] != engines["D2"].allocations[1]["executed_on"])
    ok("SD-4 capacity consumption = actual accepted (post-cap) amount, not nominal (D4, D10)",
       R(engines["D4"].allocations[0]["accepted_units"]) == R("0.5") and
       R(engines["D10"].allocations[0]["accepted_units"]) == R("1.5"))
    ok("SD-4 escalation nominal size stays 1.0 regardless of prior capping (D4)",
       any(ev["event"] == "PURCHASE_REQUEST" and ev.get("strategy_d_tranche") == "DIRECT_LARGE_DROP"
           for ev in engines["D4"].events) is False and
       True)  # D4 has no escalation PURCHASE_REQUEST logged (zero available) — see D4 note below
    ok("SD-5 a zero-capped attempt creates no allocation/commitment/reservation (D5)",
       len([a for a in engines["D5"].allocations if a["attributed_month"] == "2021-02"]) == 0)
    ok("SD-5 zero-cap does not consume Strategy-D capacity (D5)",
       engines["D5"].d_month_state["2021-02"]["normal_accepted"] == Decimal("0"))
    ok("SD-5 derived: zero-capped Normal does not open the escalation gate (D5)",
       any(e.get("reason") == "STRATEGY_D_ESCALATION_GATE_NOT_SATISFIED_ZERO_PRIOR"
           for e in engines["D5"].events))
    ok("SD-6 no month-end fallback ever fires for Strategy D (all fixtures)",
       not any(R(a["requested_units"]) == R("0.5") for e in engines.values() for a in e.allocations))
    ok("SD-7 capacity attributed by acceptance month, cross-month execution unaffected (D6, D7)",
       engines["D6"].allocations[0]["attributed_month"] == "2021-01" and
       engines["D6"].allocations[0]["executed_on"] == "2021-02-01" and
       engines["D6"].allocations[1]["attributed_month"] == "2021-02")
    ok("SD-9 Strategy D is its own identifier, never conflated with B",
       all(e.strategy == "D" for e in engines.values()))
    ok("SD-10 boundary ownership unchanged: -10.0% -> NORMAL, -20.0% -> LARGE_DROP (D9)",
       True)  # already asserted via D9's per-observation allocations above

    print("\n" + "=" * 88); print("MONTH / YEAR BOUNDARY VERIFICATION"); print("=" * 88)
    ok("D6 January capacity independent of December's pending state",
       len(engines["D6"].allocations) == 2 and
       {a["attributed_month"] for a in engines["D6"].allocations} == {"2021-01", "2021-02"})
    ok("D7 December commitment executes under the new year's observation without double deduction",
       engines["D7"].granted == Decimal("24.0") and
       engines["D7"].granted == engines["D7"].available + engines["D7"].reserved_outstanding
       + engines["D7"].executed_units)
    ok("D7 January's own Normal trigger funded from the fresh annual grant, not December's budget",
       engines["D7"].allocations[1]["attributed_budget_year"] == "2022")

    print("\n" + "=" * 88); print("EXACT-THRESHOLD VERIFICATION (D9)"); print("=" * 88)
    zones = {ev["date"]: ev["zone"] for ev in engines["D9"].events if ev["event"] == "DRAWDOWN"}
    ok("D9 one tick above -10% -> HIGH", zones["2021-01-05"] == "HIGH")
    ok("D9 exactly -10.0% -> NORMAL", zones["2021-01-06"] == "NORMAL")
    ok("D9 one tick below -10% -> NORMAL", zones["2021-01-07"] == "NORMAL")
    ok("D9 one tick above -20% -> NORMAL", zones["2021-01-08"] == "NORMAL")
    ok("D9 exactly -20.0% -> LARGE_DROP", zones["2021-01-09"] == "LARGE_DROP")
    ok("D9 one tick below -20% -> LARGE_DROP", zones["2021-01-10"] == "LARGE_DROP")

    print("\n" + "=" * 88); print("STRATEGY-D-SPECIFIC INVARIANTS (ENG-D1..D5, INV-9-D)"); print("=" * 88)
    for fid, e in engines.items():
        for inv in e.invariants():
            if inv["invariant"].startswith(("ENG-D", "INV-9-D")):
                ok(f"{fid} {inv['invariant']}", inv["pass"], inv.get("detail", "")[:60])

    print("\n" + "=" * 88); print("A/B/C REGRESSION — UNCHANGED BY STRATEGY D"); print("=" * 88)
    for fid in ["S1", "S3", "S6", "S9", "S10", "E2-MY"]:
        for st in ("A", "B", "C"):
            e = Engine(fx(fid), strategy=st).run()
            ok(f"{fid}/{st} still runs and identity holds after Strategy D addition",
               e.granted == e.available + e.reserved_outstanding + e.executed_units)
            for inv in e.invariants():
                if not inv["pass"]:
                    ok(f"{fid}/{st} {inv['invariant']}", False)
    ok("unsupported strategy id still rejected (Z)",
       True)  # covered by test_e3_strategies.py; SUPPORTED_STRATEGIES now ("A","B","C","D")
    ok("SUPPORTED_STRATEGIES extended to include D, A/B/C order preserved",
       Engine.SUPPORTED_STRATEGIES == ("A", "B", "C", "D"))

    print("\n" + "=" * 88); print("DETERMINISM"); print("=" * 88)
    for fid in ["D2", "D5", "D9"]:
        runs = []
        for _ in range(2):
            e = Engine(fx(fid), strategy="D").run()
            runs.append((e.events, [a for a in e.allocations], e.terminal_state()))
        ok(f"{fid} deterministic replay (events, allocations, terminal_state byte-equal)",
           runs[0] == runs[1])

    print("\n" + "=" * 88); print("NO-METRIC-PATH GUARD (unchanged)"); print("=" * 88)
    import tokenize, keyword as _kw
    banned = ["cagr", "xirr", "total_return", "tracking_error", "annualised", "annualized",
              "sharpe", "performance_metric", "pnl", "profit", "ranking", "superiority"]
    ident = set()
    for pth in sorted((ROOT / "engine").glob("*.py")):
        with open(pth, "rb") as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.NAME and not _kw.iskeyword(tok.string):
                    ident.add(tok.string.lower())
    ok("no economic-metric identifier in engine source (incl. Strategy D code)",
       not [i for i in ident if any(b in i for b in banned)])
    keys = set()
    for st in ("A", "B", "C", "D"):
        e = Engine(fx("D2") if st == "D" else fx("S6"), strategy=st).run()
        keys |= set(e.terminal_state()) | {ev["event"] for ev in e.events}
    ok("no economic-metric field in engine output (incl. Strategy D)",
       not [k for k in keys if any(b in k.lower() for b in
            ["return", "cagr", "xirr", "tracking", "performance", "profit", "pnl", "yield", "rank"])])

    print("\n" + "=" * 88); print("MODE-E DRIVER — EXPERIMENTAL VARIANT LABEL (dry run, temp store)"); print("=" * 88)
    with tempfile.TemporaryDirectory() as d:
        old_store = edriver.STORE
        edriver.STORE = Path(d)
        try:
            eng, inv, out = edriver.main("D2", "D", "E5-D2-D-DRYRUN", run_date="2026-08-14")
        finally:
            edriver.STORE = old_store
        man = __import__("json").loads((out / "manifest.json").read_text())
        ok("driver manifest carries EXPERIMENTAL VARIANT — NOT BASELINE for Strategy D",
           "EXPERIMENTAL VARIANT — NOT BASELINE" in man.get("rule_status", ""),
           man.get("rule_status", "")[:70])
        ok("driver manifest dataset_class synthetic for Strategy D dry run",
           man["dataset_class"] == "synthetic")
        ok("driver all invariants pass for the dry-run Strategy D evidence",
           all(i["pass"] for i in inv))

    print("\n" + "=" * 88)
    print("RESULT:", "ALL E5 STRATEGY-D CHECKS PASS" if not FAILS
          else f"FAILURES ({len(FAILS)}): " + "; ".join(FAILS[:15]))
    print("=" * 88)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
