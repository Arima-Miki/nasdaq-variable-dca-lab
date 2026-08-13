#!/usr/bin/env python3
"""Mode-E Phase E2 — month/year boundary hardening, accounting invariants,
invalid-input guards, and the no-metric-path governance guard.

NON-FORMAL — SIMULATION TRIAL. Engine state only; no economic claim.

Expectations are hand-derived and recorded in each fixture BEFORE execution.
Comparisons are exact rationals; no tolerance policy is adopted. M-7 stays OPEN.
"""
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import copy, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
from engine import Engine, FixtureError, load  # noqa: E402

FAILS = []


def R(x):
    return Fraction(Decimal(str(x)))


def check(name, got, want):
    ok = got == want
    print(f"  {'PASS' if ok else 'FAIL'}  {name:58s} got={got} want={want}")
    if not ok:
        FAILS.append(name)


def ok(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name:58s} {detail}")
    if not cond:
        FAILS.append(name)


def fx(fid):
    return load(ROOT / "fixtures" / f"{fid}.json")


def identity(eng, where):
    """granted == available + outstanding reserved + executed."""
    ok(f"identity {where}",
       eng.granted == eng.available + eng.reserved_outstanding + eng.executed_units,
       f"{eng.granted} == {eng.available} + {eng.reserved_outstanding} + {eng.executed_units}")


def run_fixture(fid):
    f = fx(fid)
    eng = Engine(f).run()
    exp = f["hand_derived_expectations"]
    print(f"\n--- {fid}: {f['scenario_name']} ---")

    # allocations
    if "allocations" not in exp:
        FAILS.append(f"{fid}: fixture has no hand-derived allocation expectations")
        print(f"  FAIL  {fid} fixture missing hand-derived allocations")
        return eng, exp
    check(f"{fid} allocation count", len(eng.allocations), len(exp["allocations"]))
    for i, (a, w) in enumerate(zip(eng.allocations, exp["allocations"])):
        for k in ("committed_on", "attributed_month", "attributed_budget_year", "executed_on"):
            if k in w:
                check(f"{fid} alloc[{i}].{k}", a.get(k), w[k])
        for k in ("accepted_units", "execution_close", "exposure_units_acquired"):
            if k in w:
                check(f"{fid} alloc[{i}].{k}", R(a[k]), R(w[k]))

    # terminal state
    ts = eng.terminal_state()
    for k, v in exp["terminal_state"].items():
        got = ts[k]
        if isinstance(v, str):
            check(f"{fid} terminal.{k}", R(got), R(v))
        else:
            check(f"{fid} terminal.{k}", got, v)

    identity(eng, fid)
    for inv in eng.invariants():
        ok(f"{fid} {inv['invariant']}", inv["pass"])
    return eng, exp


def main():
    print("=" * 78)
    print("E1 REGRESSION")
    print("=" * 78)
    import subprocess
    r = subprocess.run([sys.executable, str(ROOT / "tests" / "test_s3_strategy_b.py")],
                       capture_output=True, text=True)
    ok("E1 S3 regression unchanged", r.returncode == 0 and "ALL CHECKS PASS" in r.stdout,
       r.stdout.strip().splitlines()[-1] if r.stdout else "")

    print("\n" + "=" * 78); print("MONTH BOUNDARIES"); print("=" * 78)
    run_fixture("E2-M1")
    eng2, _ = run_fixture("E2-M2")
    # M2 explicit attribution trace
    a = eng2.allocations[0]
    ok("E2-M2 attribution follows ACCEPTANCE month, not execution month",
       a["attributed_month"] == "2021-03" and a["executed_on"].startswith("2022-") is False
       and a["executed_on"][:7] == "2021-04",
       f"committed={a['committed_on']} attributed={a['attributed_month']} executed={a['executed_on']}")
    run_fixture("E2-M3")
    eng4, _ = run_fixture("E2-M4")
    ok("E2-M4 month turnover manufactures no purchase request",
       not any(e["event"] in ("PURCHASE_REQUEST", "COMMITMENT") for e in eng4.events))

    print("\n" + "=" * 78); print("YEAR BOUNDARIES"); print("=" * 78)
    engY, expY = run_fixture("E2-Y")

    # Y2/Y3 state trace: replay observation-by-observation
    print("\n  state trace (E2-Y):")
    f = fx("E2-Y")
    for cut in ("2021-12-31", "2022-01-03"):
        sub = copy.deepcopy(f)
        keep = [o for o in f["observations"] if o["date"] <= cut]
        sub["observations"] = keep
        e = Engine(sub).run()
        w = expY[f"state_at_{cut.replace('-', '_')}_close"]
        print(f"    at {cut} close: granted={e.granted} available={e.available} "
              f"reserved={e.reserved_outstanding} executed={e.executed_units}")
        check(f"E2-Y @{cut} granted", R(e.granted), R(w["granted"]))
        check(f"E2-Y @{cut} available", R(e.available), R(w["available"]))
        check(f"E2-Y @{cut} reserved_outstanding", R(e.reserved_outstanding), R(w["reserved_outstanding"]))
        check(f"E2-Y @{cut} executed", R(e.executed_units), R(w["executed"]))
        identity(e, f"E2-Y @{cut}")

    ok("E2-Y reservation survived year-end (not erased at 1 Jan)",
       any(ev["event"] == "EXECUTION" and ev["date"].startswith("2022-01-03")
           and ev["allocation_month"] == "2021-12" for ev in engY.events))
    ok("E2-Y execution did NOT consume the new year's grant",
       R(engY.terminal_state()["budget_units_available"]) == R("22.0"),
       "24.0 granted - 1.0 (2021 commitment) - 1.0 (2022 commitment) = 22.0")
    ok("E2-Y prior-year allocation keeps its 2021 budget year",
       engY.allocations[0]["attributed_budget_year"] == "2021")

    run_fixture("E2-Y4")
    engY4 = Engine(fx("E2-Y4")).run()
    ok("E2-Y4 OD-14: full 12.0 granted, NOT prorated for a mid-year start",
       engY4.granted == Decimal("12.0"), f"granted={engY4.granted}")

    print("\n" + "=" * 78); print("MULTI-YEAR"); print("=" * 78)
    engMY, expMY = run_fixture("E2-MY")
    grants = [e for e in engMY.events if e["event"] == "BUDGET_GRANT"]
    check("E2-MY grant count (one per calendar year)", len(grants), 3)
    check("E2-MY grant years", [g["year"] for g in grants], [2021, 2022, 2023])
    ok("E2-MY sparse years funded despite non-January first observation",
       grants[1]["date"] == "2022-04-01" and grants[2]["date"] == "2023-09-01",
       f"{grants[1]['date']}, {grants[2]['date']}")
    ok("E2-MY no duplicate grant in any year",
       len({g["year"] for g in grants}) == len(grants))

    print("\n" + "=" * 78); print("INVALID-INPUT GUARDS (fail-fast, never repair)"); print("=" * 78)
    base = fx("E2-M1")

    def expect_error(name, mutate):
        bad = copy.deepcopy(base)
        mutate(bad)
        try:
            Engine(bad).run()
            ok(name, False, "NO ERROR RAISED — engine silently accepted invalid input")
        except FixtureError as e:
            ok(name, True, f"FixtureError: {e}")
        except Exception as e:  # noqa: BLE001
            ok(name, False, f"wrong exception type: {type(e).__name__}: {e}")

    expect_error("zero close rejected", lambda b: b["observations"][1].update(close="0"))
    expect_error("negative close rejected", lambda b: b["observations"][1].update(close="-5"))
    expect_error("non-increasing dates rejected",
                 lambda b: b["observations"].__setitem__(2, {"date": "2021-01-04", "close": "100"}))
    expect_error("duplicate date rejected",
                 lambda b: b["observations"].insert(2, {"date": "2021-01-05", "close": "90"}))
    expect_error("malformed numeric rejected", lambda b: b["observations"][1].update(close="abc"))
    expect_error("malformed date rejected", lambda b: b["observations"][1].update(date="2021-13-99"))
    expect_error("missing observations rejected", lambda b: b.__setitem__("observations", []))
    expect_error("bad unit_value rejected", lambda b: b["parameters"].update(unit_value_jpy="0"))
    try:
        Engine(fx("E2-M1"), strategy="A")
        ok("unimplemented strategy rejected", False, "NO ERROR RAISED")
    except FixtureError as e:
        ok("unimplemented strategy rejected", True, f"FixtureError: {e}")

    print("\n" + "=" * 78); print("NO-METRIC-PATH GUARD (governance invariant)"); print("=" * 78)
    banned = ["cagr", "xirr", "total_return", "totalreturn", "tracking_error", "trackingerror",
              "annualised", "annualized", "sharpe", "performance_metric", "pnl", "profit"]
    # Inspect EXECUTABLE TOKENS ONLY. Comments and docstrings legitimately name the
    # banned metrics — that is the prohibition text itself — so a raw text scan gives
    # false positives. Tokenizing and discarding COMMENT/STRING tokens tests the code.
    import tokenize, io as _io, keyword as _kw
    ident = set()
    for pth in sorted((ROOT / "engine").glob("*.py")):
        with open(pth, "rb") as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.NAME and not _kw.iskeyword(tok.string):
                    ident.add(tok.string.lower())
    hits = sorted(i for i in ident if any(b in i for b in banned))
    ok("no economic-metric identifier in engine source", not hits, f"hits={hits}")

    eng = Engine(fx("E2-MY")).run()
    keys = set(eng.terminal_state()) | {e["event"] for e in eng.events}
    bad_keys = [k for k in keys if any(b in k.lower() for b in
                ["return", "cagr", "xirr", "tracking", "performance", "profit", "pnl", "yield"])]
    ok("no economic-metric field in engine output", not bad_keys, f"fields={bad_keys}")

    print("\n" + "=" * 78)
    print("RESULT:", "ALL E2 CHECKS PASS" if not FAILS else f"FAILURES ({len(FAILS)}): " + "; ".join(FAILS))
    print("=" * 78)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
