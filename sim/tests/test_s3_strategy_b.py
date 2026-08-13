#!/usr/bin/env python3
"""Mode-E verification: engine output vs the hand-derived S3 expectations.

NON-FORMAL — SIMULATION TRIAL. Mechanical correctness only; no economic claim.

Expectations were written into sim/fixtures/S3.json BEFORE the engine existed.
Values are compared as exact rationals, so a decimal-precision rendering
difference cannot mask or manufacture a mismatch. This comparison choice is an
implementation-precision matter and adopts no tolerance policy: M-7 remains OPEN.
"""
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
from engine import Engine, load, classify_zone  # noqa: E402

FX = Path(__file__).resolve().parents[1] / "fixtures" / "S3.json"


def R(x):
    return Fraction(Decimal(str(x)))


def main():
    fx = load(FX)
    eng = Engine(fx).run()
    exp = fx["hand_derived_expectations"]
    fails = []

    def check(name, got, want):
        ok = got == want
        print(f"  {'PASS' if ok else 'FAIL'}  {name:52s} got={got} want={want}")
        if not ok:
            fails.append(name)

    # --- per-observation: ATH, DD, zone -------------------------------------
    dd_events = [e for e in eng.events if e["event"] == "DRAWDOWN"]
    print("Per-observation checks (ATH, drawdown, zone):")
    for e, w in zip(dd_events, exp["per_observation"]):
        d = e["date"]
        check(f"{d} reference_high", R(e["reference_high"]), R(w["ath"]))
        if "dd" in w:
            check(f"{d} drawdown", R(e["dd"]), R(w["dd"]))
        else:
            # Non-terminating exact value: verify the engine emitted the
            # CORRECTLY-ROUNDED decimal of the exact rational at its declared
            # precision. This is exact and deterministic — it is NOT a tolerance,
            # and it adopts no tolerance policy. M-7 remains OPEN.
            num, den = w["dd_exact_rational"].split("/")
            want = Decimal(num) / Decimal(den)
            check(f"{d} drawdown (correctly rounded of {w['dd_exact_rational']})",
                  Decimal(e["dd"]), want)
        check(f"{d} zone", e["zone"], {"HIGH": "HIGH", "NORMAL": "NORMAL",
                                       "LARGE_DROP": "LARGE_DROP"}[w["zone"]])

    # --- allocation ---------------------------------------------------------
    print("\nAllocation checks:")
    wa = exp["allocations"][0]
    check("allocations committed", len(eng.allocations), len(exp["allocations"]))
    a = eng.allocations[0]
    check("committed_on", a["committed_on"], wa["committed_on"])
    check("attributed_month", a["attributed_month"], wa["attributed_month"])
    check("attributed_budget_year", a["attributed_budget_year"], wa["attributed_budget_year"])
    check("accepted_units", R(a["accepted_units"]), R(wa["accepted_units"]))
    check("capped", a["capped"], wa["capped"])
    check("executed_on", a["executed_on"], wa["executed_on"])
    check("execution_close", R(a["execution_close"]), R(wa["execution_close"]))
    check("amount_jpy", R(a["amount_jpy"]), R(wa["amount_jpy"]))
    check("exposure_units_acquired", R(a["exposure_units_acquired"]),
          R(wa["exposure_units_acquired"]))

    # --- terminal state -----------------------------------------------------
    print("\nTerminal-state checks:")
    ts, wt = eng.terminal_state(), exp["terminal_state"]
    for k, v in wt.items():
        got, want = ts[k], v
        if isinstance(want, str) and want.lstrip("-").replace(".", "").isdigit():
            check(k, R(got), R(want))
        else:
            check(k, got, want)

    # --- boundary semantics (fixed by §4.0; does NOT decide M-7) ------------
    print("\nBoundary-semantics checks (Baseline v2 §4.0, fixed):")
    tn, tl = Decimal("-0.10"), Decimal("-0.20")
    check("DD = -10.0% -> NORMAL", classify_zone(Decimal("-0.10"), tn, tl), "NORMAL")
    check("DD = -20.0% -> LARGE_DROP", classify_zone(Decimal("-0.20"), tn, tl), "LARGE_DROP")
    check("DD just above -10% -> HIGH", classify_zone(Decimal("-0.0999"), tn, tl), "HIGH")
    check("DD just below -20% -> LARGE_DROP", classify_zone(Decimal("-0.2001"), tn, tl), "LARGE_DROP")

    # --- invariants ---------------------------------------------------------
    print("\nInvariants:")
    for i in eng.invariants():
        print(f"  {'PASS' if i['pass'] else 'FAIL'}  {i['invariant']}")
        if not i["pass"]:
            fails.append(i["invariant"])

    print(f"\nRESULT: {'ALL CHECKS PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
