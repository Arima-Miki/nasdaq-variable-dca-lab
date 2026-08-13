#!/usr/bin/env python3
"""Mode-E Phase E3 — Strategies A, B and C across the full synthetic suite.

NON-FORMAL — SIMULATION TRIAL. Engine state only; no economic claim, no ranking.

Expectations come from each fixture's independent reference derivation, written
separately from the engine and never copied from engine output. Comparisons are
exact rationals; no tolerance policy. M-7 stays OPEN.
"""
from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine"))
from engine import Engine, FixtureError, load, HIGH  # noqa: E402

FAILS = []
SUITE = ["S1", "S2", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11"]


def R(x):
    return Fraction(Decimal(str(x)))


def numeric(v):
    try:
        Decimal(str(v)); return True
    except Exception:
        return False


def check(name, got, want):
    if got != want:
        FAILS.append(name)
        print(f"  FAIL  {name:62s} got={got} want={want}")


def ok(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name:62s} {detail}")
    if not cond:
        FAILS.append(name)


def fx(fid):
    return load(ROOT / "fixtures" / f"{fid}.json")


def run(fid, st):
    f = fx(fid)
    eng = Engine(f, strategy=st).run()
    exp = f["hand_derived_expectations"]["per_strategy"][st]
    check(f"{fid}/{st} alloc count", len(eng.allocations), len(exp["allocations"]))
    for i, (a, w) in enumerate(zip(eng.allocations, exp["allocations"])):
        for k in ("committed_on", "attributed_month", "attributed_budget_year", "capped"):
            check(f"{fid}/{st} alloc[{i}].{k}", a.get(k), w[k])
        for k in ("requested_units", "accepted_units"):
            check(f"{fid}/{st} alloc[{i}].{k}", R(a[k]), R(w[k]))
        if "executed_on" in w:
            check(f"{fid}/{st} alloc[{i}].executed_on", a.get("executed_on"), w["executed_on"])
            check(f"{fid}/{st} alloc[{i}].exposure", R(a["exposure_units_acquired"]),
                  R(w["exposure_units_acquired"]))
    ts = eng.terminal_state()
    for k, v in exp["terminal_state"].items():
        if isinstance(v, str) and numeric(v):
            check(f"{fid}/{st} terminal.{k}", R(ts[k]), R(v))
        else:
            check(f"{fid}/{st} terminal.{k}", ts[k], v)
    ok(f"{fid}/{st} identity granted = available + reserved + executed",
       eng.granted == eng.available + eng.reserved_outstanding + eng.executed_units)
    for inv in eng.invariants():
        if not inv["pass"]:
            ok(f"{fid}/{st} {inv['invariant']}", False)
    return eng


def main():
    print("=" * 80); print("FULL SUITE — S1, S2, S4-S11 x Strategies A/B/C"); print("=" * 80)
    for fid in SUITE:
        line = []
        for st in ("A", "B", "C"):
            e = run(fid, st)
            line.append(f"{st}:{len(e.allocations)}a/{e.executed_units}u")
        print(f"  PASS  {fid:5s} {fx(fid)['scenario_name']:52s} " + "  ".join(line))

    print("\n" + "=" * 80); print("S3 + E2 FIXTURES x A/B/C (no strategy breaks another)"); print("=" * 80)
    for fid in ["S3", "E2-M1", "E2-M2", "E2-M3", "E2-M4", "E2-Y", "E2-Y4", "E2-MY"]:
        for st in ("A", "B", "C"):
            e = Engine(fx(fid), strategy=st).run()
            ok(f"{fid}/{st} runs end-to-end and identity holds",
               e.granted == e.available + e.reserved_outstanding + e.executed_units)
            for inv in e.invariants():
                if not inv["pass"]:
                    ok(f"{fid}/{st} {inv['invariant']}", False)

    # Baseline v2 Invariant 3: "All Baseline strategies receive identical annual
    # external funding capacity." This is a CROSS-STRATEGY proposition and cannot
    # be evaluated inside a single run — which is why the per-run assertions.json
    # of E1/E2 recorded it as unreachable. It is asserted here by running one
    # fixture under all three strategies and comparing the FUNDING side only.
    #
    # Funding capacity means what is GRANTED, not what is deployed. Strategies are
    # expected to differ in deployment; if they did not, the experiment would be
    # pointless. Asserting equality of executed units would assert the opposite of
    # the Baseline's purpose, so deployment is printed but deliberately NOT
    # asserted equal.
    print("\n" + "=" * 80); print("INVARIANT 3 — identical annual funding across A/B/C"); print("=" * 80)
    for fid in ["S6", "E2-MY", "S11", "E2-Y4"]:
        engs = {st: Engine(fx(fid), strategy=st).run() for st in ("A", "B", "C")}
        g = {st: e.granted for st, e in engs.items()}
        grants = {st: [(ev["date"], ev["units"]) for ev in e.events if ev["event"] == "BUDGET_GRANT"]
                  for st, e in engs.items()}
        ok(f"INV-3 {fid}: identical granted units across A/B/C",
           g["A"] == g["B"] == g["C"], f"A={g['A']} B={g['B']} C={g['C']}")
        ok(f"INV-3 {fid}: identical grant timing and amounts across A/B/C",
           grants["A"] == grants["B"] == grants["C"], f"{grants['A']}")
        ok(f"INV-3 {fid}: strategy does not alter carry-forward mechanics",
           all(e.granted == e.available + e.reserved_outstanding + e.executed_units
               for e in engs.values()))
        print(f"    (deployment differs by design, not asserted equal: "
              f"{ {st: str(e.executed_units) for st, e in engs.items()} })")

    print("\n" + "=" * 80); print("INVARIANT 14 — Strategy C 0.5 fallback"); print("=" * 80)
    e = Engine(fx("S1"), strategy="C").run()
    fb = [a for a in e.allocations if R(a["requested_units"]) == R("0.5")]
    ok("INV-14 S1/C fallback fires when no daily trigger all month", len(fb) == 3, f"{len(fb)} fallbacks")
    ok("INV-14 S1/C every fallback is at month-end and in the HIGH zone",
       all(a["month_end"] and a["zone"] == HIGH for a in fb))
    for st in ("A", "B"):
        e2 = Engine(fx("S1"), strategy=st).run()
        ok(f"INV-14 S1/{st} never requests the 0.5 fallback size",
           not any(R(a["requested_units"]) == R("0.5") for a in e2.allocations))
    # fallback must not coexist with a primary allocation in the same month
    e3 = Engine(fx("S6"), strategy="C").run()
    months = [a["attributed_month"] for a in e3.allocations]
    ok("INV-14 S6/C at most one allocation per month (no fallback + trigger duplication)",
       len(months) == len(set(months)), f"months={months}")
    ok("INV-14 S6/C no fallback in a month where a daily trigger already committed",
       not any(R(a["requested_units"]) == R("0.5") for a in e3.allocations), f"requests={[a['requested_units'] for a in e3.allocations]}")
    # month-end NORMAL/LARGE => daily trigger, never fallback
    e4 = Engine(fx("S9"), strategy="C").run()
    ok("INV-14 S9/C month-end in NORMAL/LARGE takes the daily trigger, not the fallback",
       all(R(a["requested_units"]) in (R("1.0"), R("2.0")) or a["zone"] == HIGH
           for a in e4.allocations))

    print("\n" + "=" * 80); print("STRATEGY A — month-end-only decision path"); print("=" * 80)
    eA = Engine(fx("S6"), strategy="A").run()
    ok("A: every allocation is on a month-end observation",
       all(a["month_end"] for a in eA.allocations),
       f"{[(a['committed_on'], a['month_end']) for a in eA.allocations]}")
    ok("A: no allocation before the month-end decision point",
       not any(e["event"] == "PURCHASE_REQUEST" and not any(
           m["event"] == "MONTH_END" and m["date"] == e["date"] for m in eA.events)
           for e in eA.events))
    ok("A: drawdown never influences the decision (requests all 1.0 regardless of zone)",
       all(R(a["requested_units"]) == R("1.0") for a in eA.allocations),
       f"zones at commitment={[a['zone'] for a in eA.allocations]}")
    ok("A: one allocation per calendar month",
       len({a["attributed_month"] for a in eA.allocations}) == len(eA.allocations))
    ok("A: month change alone creates no signal",
       len(Engine(fx("E2-M4"), strategy="A").run().allocations) ==
       len([1 for i, o in enumerate(fx("E2-M4")["observations"])
            if i == len(fx("E2-M4")["observations"]) - 1 or
            o["date"][:7] != fx("E2-M4")["observations"][i + 1]["date"][:7]]),
       "A allocates exactly once per month-end, and only there")

    print("\n" + "=" * 80); print("THRESHOLD BOUNDARIES"); print("=" * 80)
    e9 = Engine(fx("S9"), strategy="B").run()
    zones = {ev["date"]: ev["zone"] for ev in e9.events if ev["event"] == "DRAWDOWN"}
    ok("S9 DD exactly -10.0% -> NORMAL", zones["2021-01-05"] == "NORMAL", "close 90 vs ATH 100")
    ok("S9 DD exactly -20.0% -> LARGE_DROP", zones["2021-02-01"] == "LARGE_DROP", "close 80 vs ATH 100")
    e10 = Engine(fx("S10"), strategy="B").run()
    z10 = {ev["date"]: ev["zone"] for ev in e10.events if ev["event"] == "DRAWDOWN"}
    # CORRECTION recorded openly: the first form of these two assertions was WRONG
    # — 8999/10000 is -10.01%, one tick below the -10% threshold, not -20%. The
    # fixture contained no -20.01% case at all. The engine was not at fault; the
    # fixture now covers one tick either side of BOTH thresholds.
    ok("S10 one tick above -10% -> HIGH", z10["2021-01-05"] == "HIGH", "9001/10000 = -9.99%")
    ok("S10 one tick below -10% -> NORMAL", z10["2021-02-01"] == "NORMAL", "8999/10000 = -10.01%")
    ok("S10 one tick above -20% -> NORMAL", z10["2021-03-01"] == "NORMAL", "8001/10000 = -19.99%")
    ok("S10 one tick below -20% -> LARGE_DROP", z10["2021-04-01"] == "LARGE_DROP", "7999/10000 = -20.01%")

    print("\n" + "=" * 80); print("BUDGET / CAPPING / ZERO AVAILABILITY"); print("=" * 80)
    e7 = Engine(fx("S7"), strategy="B").run()
    capped = [a for a in e7.allocations if a["capped"]]
    ok("S7 a capped allocation occurs (accepted = available)", len(capped) >= 1,
       f"{[(a['committed_on'], a['requested_units'], str(a['accepted_units'])) for a in capped]}")
    ok("S7 available never negative", e7.available >= 0, f"available={e7.available}")
    e8 = Engine(fx("S8"), strategy="B").run()
    ok("S8 zero-availability produces NO_ALLOCATION, not a negative balance",
       any(ev["event"] == "NO_ALLOCATION" for ev in e8.events) and e8.available >= 0,
       f"available={e8.available}")

    print("\n" + "=" * 80); print("GUARDS (preserved from E2)"); print("=" * 80)
    import copy
    bad = copy.deepcopy(fx("S1")); bad["observations"][1]["close"] = "0"
    try:
        Engine(bad, strategy="A").run(); ok("zero close still rejected under Strategy A", False)
    except FixtureError:
        ok("zero close still rejected under Strategy A", True)
    try:
        Engine(fx("S1"), strategy="Z"); ok("unsupported strategy id rejected", False)
    except FixtureError:
        ok("unsupported strategy id rejected", True)

    print("\n" + "=" * 80); print("NO-METRIC-PATH GUARD"); print("=" * 80)
    import tokenize, keyword as _kw
    banned = ["cagr", "xirr", "total_return", "tracking_error", "annualised", "annualized",
              "sharpe", "performance_metric", "pnl", "profit", "ranking", "superiority"]
    ident = set()
    for pth in sorted((ROOT / "engine").glob("*.py")):
        with open(pth, "rb") as fh:
            for tok in tokenize.tokenize(fh.readline):
                if tok.type == tokenize.NAME and not _kw.iskeyword(tok.string):
                    ident.add(tok.string.lower())
    ok("no economic-metric identifier in engine source",
       not [i for i in ident if any(b in i for b in banned)])
    keys = set()
    for st in ("A", "B", "C"):
        e = Engine(fx("S6"), strategy=st).run()
        keys |= set(e.terminal_state()) | {ev["event"] for ev in e.events}
    ok("no economic-metric field in engine output",
       not [k for k in keys if any(b in k.lower() for b in
            ["return", "cagr", "xirr", "tracking", "performance", "profit", "pnl", "yield", "rank"])])

    print("\n" + "=" * 80)
    print("RESULT:", "ALL E3 CHECKS PASS" if not FAILS else f"FAILURES ({len(FAILS)}): " + "; ".join(FAILS[:12]))
    print("=" * 80)
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
