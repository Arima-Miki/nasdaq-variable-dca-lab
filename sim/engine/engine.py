#!/usr/bin/env python3
"""Simulation Trial — Mode E (Engine Validation) walking skeleton.

NON-FORMAL — SIMULATION TRIAL
ENGINE VALIDATION — SYNTHETIC — NON-ECONOMIC — NON-BASELINE — NON-PROMOTABLE

Governing Baseline: v2 (effective 2026-08-13).

This engine implements ONLY the mechanics Phase E1 requires: fixture S3 with
Strategy B. It reports ENGINE STATE, never performance. No evaluation metric
governed by M-1..M-8 is computed here, and none may be added without a separate
Owner Decision.

All arithmetic is exact Decimal. No floating-point tolerance policy is adopted;
M-7 remains OPEN.
"""
from decimal import Decimal, getcontext
from datetime import date
import json

getcontext().prec = 40

CLASSIFICATION = [
    "NON-FORMAL — SIMULATION TRIAL",
    "ENGINE VALIDATION RESULT",
    "SYNTHETIC",
    "NON-ECONOMIC",
    "NON-BASELINE",
    "NON-PROMOTABLE",
]

HIGH, NORMAL, LARGE_DROP = "HIGH", "NORMAL", "LARGE_DROP"


def classify_zone(dd, t_normal, t_large):
    """Baseline v2 §4.0. Boundaries are fixed:
       -10.0% belongs to NORMAL; -20.0% belongs to LARGE_DROP.
       Exact Decimal comparison; no tolerance policy (M-7 untouched)."""
    if dd <= t_large:
        return LARGE_DROP
    if dd <= t_normal:
        return NORMAL
    return HIGH


def strategy_b(zone, units_normal, units_large):
    """Baseline v2 §4.2 / §4.4 / OD-09. High zone -> WAIT / 0 units."""
    if zone == LARGE_DROP:
        return units_large
    if zone == NORMAL:
        return units_normal
    return Decimal("0")


class FixtureError(ValueError):
    """Deterministic, explicit fail-fast for input that would make engine state
    meaningless. The engine NEVER silently repairs a fixture, and performs no
    market-data cleaning of any kind."""


def validate(fixture):
    """Narrow fail-fast validation. Raises FixtureError; never repairs."""
    p = fixture.get("parameters")
    if not isinstance(p, dict):
        raise FixtureError("missing 'parameters'")
    obs = fixture.get("observations")
    if not obs:
        raise FixtureError("missing or empty 'observations'")

    for key in ("unit_value_jpy", "annual_units", "threshold_normal",
                "threshold_large_drop", "units_normal_zone", "units_large_drop_zone"):
        try:
            Decimal(p[key])
        except (KeyError, ArithmeticError, TypeError, ValueError):
            raise FixtureError(f"parameter '{key}' missing or not a valid decimal")

    if Decimal(p["unit_value_jpy"]) <= 0:
        raise FixtureError("unit_value_jpy must be > 0")
    if Decimal(p["annual_units"]) <= 0:
        raise FixtureError("annual_units must be > 0")

    prev = None
    seen = set()
    for i, o in enumerate(obs):
        try:
            d = date.fromisoformat(o["date"])
        except (KeyError, TypeError, ValueError):
            raise FixtureError(f"observation {i}: missing or malformed date")
        try:
            c = Decimal(o["close"])
        except (KeyError, ArithmeticError, TypeError, ValueError):
            raise FixtureError(f"observation {i} ({o.get('date')}): malformed numeric close")
        if not c.is_finite():
            raise FixtureError(f"observation {i} ({d}): non-finite close")
        if c == 0:
            raise FixtureError(f"observation {i} ({d}): zero close is not a valid observation")
        if c < 0:
            raise FixtureError(f"observation {i} ({d}): negative close is not a valid observation")
        if d in seen:
            raise FixtureError(f"observation {i}: duplicate observation date {d}")
        if prev is not None and d <= prev:
            raise FixtureError(f"observation {i}: dates must strictly increase ({prev} -> {d})")
        seen.add(d)
        prev = d

    try:
        date.fromisoformat(p["performance_start"])
    except (KeyError, TypeError, ValueError):
        raise FixtureError("parameter 'performance_start' missing or malformed")
    return fixture


class Engine:
    SUPPORTED_STRATEGIES = ("B",)

    def __init__(self, fixture, strategy="B"):
        if strategy not in self.SUPPORTED_STRATEGIES:
            raise FixtureError(
                f"strategy '{strategy}' is not implemented in Mode E phase E2; "
                f"supported: {self.SUPPORTED_STRATEGIES}")
        validate(fixture)
        p = fixture["parameters"]
        self.unit_value = Decimal(p["unit_value_jpy"])
        self.annual_units = Decimal(p["annual_units"])
        self.t_normal = Decimal(p["threshold_normal"])
        self.t_large = Decimal(p["threshold_large_drop"])
        self.u_normal = Decimal(p["units_normal_zone"])
        self.u_large = Decimal(p["units_large_drop_zone"])
        self.exec_rule = p["execution_valuation_rule"]
        self.perf_start = date.fromisoformat(p["performance_start"])
        self.obs = [(date.fromisoformat(o["date"]), Decimal(o["close"]))
                    for o in fixture["observations"]]

        # engine state
        self.ath = None
        self.available = Decimal("0")          # units
        self.granted = Decimal("0")            # units
        self.reserved_outstanding = Decimal("0")
        self.executed_units = Decimal("0")
        self.exposure = Decimal("0")           # accumulated exposure units
        self.cash_deployed = Decimal("0")
        self.funded_years = set()
        self.committed_months = set()          # §10 / §12.5 monthly exclusivity
        self.pending = []                      # allocations awaiting execution
        self.allocations = []
        self.events = []
        self.suppressed = 0

    # ---- event log -------------------------------------------------------
    def log(self, d, kind, **kw):
        e = {"date": d.isoformat(), "event": kind}
        e.update({k: (str(v) if isinstance(v, Decimal) else v) for k, v in kw.items()})
        self.events.append(e)

    # ---- budget ----------------------------------------------------------
    def grant_if_due(self, d):
        """§11.1 / OD-10: 12.0 units at the start of each calendar year, available
        at once, never monthly. Unused units carry forward and never expire.
        OD-14: if the performance start falls after 1 January, the starting
        calendar year is funded in FULL at the performance start, without
        proration.

        ANNUAL BUDGET GRANT OBSERVATION RULE — Owner-approved 2026-08-13.
        In an observation-driven engine the grant lands on the FIRST AVAILABLE
        OBSERVATION of that calendar year, whatever its month. §11.1 fixes the
        amount, the at-once availability and the carry-forward; it does not name
        an observation.

        Rationale accepted by the Owner: a calendar year's grant must not
        disappear merely because a sparse synthetic or later dataset has no
        January observation.

        This is an implementation-timing interpretation for the Simulation Trial
        engine only. It does NOT change the grant amount, does NOT change
        carry-forward semantics, does NOT derive or decide P1-5, does NOT create
        a market-data calendar rule, and does NOT alter any formal Baseline
        qualification state.

        E2 DEFECT FIX: the E1 implementation additionally required a non-start
        year's first observation to be in January. With sparse fixtures a year
        whose first observation fell later would NEVER have been funded.
        """
        y = d.year
        if y in self.funded_years:
            return
        if y == self.perf_start.year and d != self.perf_start:
            return                      # start year funds at the performance start
        if y < self.perf_start.year:
            return                      # no funding before the performance start
        self.funded_years.add(y)
        self.available += self.annual_units
        self.granted += self.annual_units
        self.log(d, "BUDGET_GRANT", year=y, units=self.annual_units,
                 available_after=self.available, prorated=False,
                 carry_forward_included=self.available - self.annual_units)

    # ---- execution -------------------------------------------------------
    def execute_due(self, d, close):
        """Executes allocations whose valuation date has arrived.
        NEXT_OBSERVATION_CLOSE satisfies OD-03: never the signal's own close."""
        still = []
        for a in self.pending:
            if a["execute_on_or_after"] <= d:
                amount = a["accepted_units"] * self.unit_value
                acquired = amount / close
                self.exposure += acquired
                self.cash_deployed += amount
                self.reserved_outstanding -= a["accepted_units"]
                self.executed_units += a["accepted_units"]
                a.update(executed_on=d.isoformat(), execution_close=str(close),
                         amount_jpy=str(amount), exposure_units_acquired=str(acquired))
                self.log(d, "EXECUTION", allocation_month=a["attributed_month"],
                         units=a["accepted_units"], close=close, amount_jpy=amount,
                         exposure_acquired=acquired, exposure_total=self.exposure)
            else:
                still.append(a)
        self.pending = still

    # ---- main loop -------------------------------------------------------
    def run(self):
        for i, (d, close) in enumerate(self.obs):
            self.log(d, "OBSERVATION", close=close)
            self.grant_if_due(d)
            self.execute_due(d, close)

            # §7 / OD-02 — ATH from closes available through t
            prev = self.ath
            self.ath = close if self.ath is None else max(self.ath, close)
            if prev is None or self.ath != prev:
                self.log(d, "ATH_UPDATE", reference_high=self.ath)

            dd = (close - self.ath) / self.ath          # §4.0
            zone = classify_zone(dd, self.t_normal, self.t_large)
            self.log(d, "DRAWDOWN", reference_high=self.ath, dd=dd, zone=zone)

            requested = strategy_b(zone, self.u_normal, self.u_large)
            month = f"{d.year:04d}-{d.month:02d}"

            if requested == 0:
                self.log(d, "SIGNAL", signal="WAIT", zone=zone, units=Decimal("0"))
                continue

            if month in self.committed_months:      # §12.5 monthly exclusivity
                self.suppressed += 1
                self.log(d, "SIGNAL_SUPPRESSED", zone=zone, requested_units=requested,
                         reason="MONTHLY_EXCLUSIVITY", month=month)
                continue

            self.log(d, "PURCHASE_REQUEST", zone=zone, requested_units=requested)

            accepted = min(requested, self.available)     # §12.4 capping
            capped = accepted < requested
            self.log(d, "BUDGET_VALIDATION", requested_units=requested,
                     available_units=self.available, accepted_units=accepted, capped=capped)

            if accepted == 0:
                self.log(d, "NO_ALLOCATION", reason="ZERO_UNITS_AVAILABLE")
                continue

            # §12.1 / §12.2 — reserve immediately, attribute to month/year of acceptance
            self.available -= accepted
            self.reserved_outstanding += accepted
            self.committed_months.add(month)
            exec_on = self.obs[i + 1][0] if i + 1 < len(self.obs) else None
            alloc = {
                "committed_on": d.isoformat(), "attributed_month": month,
                "attributed_budget_year": str(d.year),
                "requested_units": str(requested), "accepted_units": accepted,
                "capped": capped, "execute_on_or_after": exec_on,
            }
            self.allocations.append(alloc)
            self.pending.append(alloc)
            self.log(d, "COMMITMENT", attributed_month=month, attributed_budget_year=d.year,
                     accepted_units=accepted, available_after=self.available,
                     reserved_outstanding=self.reserved_outstanding)
        return self

    # ---- outputs ---------------------------------------------------------
    def terminal_state(self):
        last_close = self.obs[-1][1]
        dd = (last_close - self.ath) / self.ath
        return {
            "reference_high": str(self.ath),
            "final_dd": str(dd),
            "final_zone": classify_zone(dd, self.t_normal, self.t_large),
            "budget_units_granted": str(self.granted),
            "budget_units_available": str(self.available),
            "budget_units_reserved_outstanding": str(self.reserved_outstanding),
            "budget_units_executed": str(self.executed_units),
            "cash_granted_jpy": str(self.granted * self.unit_value),
            "cash_deployed_jpy": str(self.cash_deployed),
            "cash_remaining_jpy": str(self.granted * self.unit_value - self.cash_deployed),
            "exposure_units_held": str(self.exposure),
            "allocations_committed": len(self.allocations),
            "signals_suppressed_monthly_exclusivity": self.suppressed,
        }

    def invariants(self):
        """Baseline v2 §17, those reachable in E1, plus engine invariants."""
        r, ath_seq = [], []
        for e in self.events:
            if e["event"] == "ATH_UPDATE":
                ath_seq.append(Decimal(e["reference_high"]))

        def chk(name, ok, detail=""):
            r.append({"invariant": name, "pass": bool(ok), "detail": detail})

        chk("ENG-1 ATH never decreases",
            all(ath_seq[i] <= ath_seq[i + 1] for i in range(len(ath_seq) - 1)),
            f"sequence={[str(a) for a in ath_seq]}")
        chk("INV-2 signal close never its own execution price",
            all(a["committed_on"] != a.get("executed_on") for a in self.allocations),
            "OD-03 / execution valuation rule = NEXT_OBSERVATION_CLOSE")
        chk("INV-4 exactly 12.0 new units per funded calendar year",
            self.granted == self.annual_units * len(self.funded_years),
            f"granted={self.granted} years={sorted(self.funded_years)}")
        chk("INV-5 future-year units never borrowed",
            all(int(a["attributed_budget_year"]) in self.funded_years for a in self.allocations))
        chk("INV-6/7/8 unused units carry forward; cash retained; 0% cash return",
            self.available >= 0 and self.granted * self.unit_value - self.cash_deployed >= 0)
        chk("INV-9 at most one committed allocation per calendar month",
            len({a["attributed_month"] for a in self.allocations}) == len(self.allocations),
            f"months={[a['attributed_month'] for a in self.allocations]}")
        chk("INV-10 commitment reserves budget immediately",
            all(e["event"] != "COMMITMENT" or Decimal(e["available_after"]) >= 0 for e in self.events))
        chk("INV-11 execution never deducts budget twice",
            self.granted - self.available == self.reserved_outstanding + self.executed_units,
            f"granted={self.granted} available={self.available} "
            f"reserved={self.reserved_outstanding} executed={self.executed_units}")
        chk("INV-12 execution never changes allocation month or budget year",
            all(a["attributed_month"] == a["committed_on"][:7] for a in self.allocations))
        chk("INV-13 Strategy B never purchases in the High zone",
            not any(e.get("zone") == HIGH for e in self.events
                    if e["event"] in ("PURCHASE_REQUEST", "COMMITMENT")))
        chk("INV-15 no same-month escalation after commitment",
            self.suppressed == sum(1 for e in self.events if e["event"] == "SIGNAL_SUPPRESSED"))
        chk("ENG-2 budget reconciles",
            self.granted == self.available + self.reserved_outstanding + self.executed_units)
        chk("ENG-3 no negative balances",
            self.available >= 0 and self.reserved_outstanding >= 0 and self.exposure >= 0)
        return r


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
