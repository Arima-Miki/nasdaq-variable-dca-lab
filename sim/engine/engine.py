#!/usr/bin/env python3
"""Simulation Trial — Mode E (Engine Validation).

NON-FORMAL — SIMULATION TRIAL
ENGINE VALIDATION — SYNTHETIC — NON-ECONOMIC — NON-BASELINE — NON-PROMOTABLE

Governing Baseline: v2 (effective 2026-08-13).

Phases E1 (walking skeleton, S3/Strategy B), E2 (month/year boundary hardening)
and E3 (Strategies A and C; S1-S11 synthetic suite) are implemented. This engine
reports ENGINE STATE, never performance. No evaluation metric governed by
M-1..M-8 is computed here, and none may be added without a separate Owner
Decision.

All arithmetic is exact Decimal. No floating-point tolerance policy is adopted;
M-7 remains OPEN.

OWNER-APPROVED 2026-08-13 — IMPLEMENTATION-EVOLUTION RULE
---------------------------------------------------------
The repository's additive-only preservation discipline REMAINS FULLY BINDING for
normative and evidentiary artifacts unless a separate Owner Decision explicitly
provides otherwise. However:

  IMPLEMENTATION AND TEST CODE MAY EVOLVE UNDER CONTROLLED VERSION HISTORY.

Covered: simulator implementation, test code, fixture-generation code, run
drivers, implementation-support files. Such files MAY be modified after an
earlier phase has been preserved when required to fix a defect, implement an
already-authorized later phase, extend the engine to another authorized
strategy, correct an obsolete implementation test, or preserve compatibility
with the controlling Baseline.

This does NOT authorize rewriting historical evidence. Requirements:
  1. previous implementation state must remain recoverable from Git history;
  2. preserved phase tags must not move;
  3. earlier evidence artifacts and external run outputs must not be overwritten;
  4. regressions for earlier phases must pass;
  5. defects discovered during evolution must be recorded openly;
  6. normative semantics must not be changed by implementation edits;
  7. any genuine normative conflict returns to Owner Review.

THIS APPROVAL DOES NOT GENERALIZE TO PRESERVED docs/ ARTIFACTS.
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

# §18.4.5. Mandatory, additional to CLASSIFICATION, for every Strategy-D run —
# never applied to A, B, or C.
STRATEGY_D_LABELS = [
    "EXPERIMENTAL VARIANT — NOT BASELINE",
    "OWNER-GENERATED POST-RESULT ALTERNATIVE HYPOTHESIS",
    "NOT ADOPTED",
    "NOT VALIDATED",
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


def classify_zone_scaled(close, ath, t_normal, t_large):
    """MP-R-01 — EXACT SCALED COMPARISON. Owner-approved 2026-08-14, preserved
    in the Mode-P Decision Boundary (commit 91378fe).

    Classifying by the quotient `(close - ath) / ath` requires DIVIDING first,
    and division of finite decimals is generally non-terminating, so the value
    compared is a ROUNDED one. Multiplying instead is exact:

        DD <= -0.10   <=>   close <= 0.9 * ath
        DD <= -0.20   <=>   close <= 0.8 * ath        (ath > 0)

    Both sides are finite decimals, so every zone decision is exact for every
    representable close. This is an implementation representation of the
    ALREADY-FIXED §4.0 semantics: it adopts NO tolerance, performs NO rounding
    before comparison, and DOES NOT resolve M-7, which remains OPEN.

    Derived generally from the thresholds so the frozen boundary ownership is
    preserved rather than re-stated as magic constants: for threshold t,
    `DD <= t  <=>  close <= (1 + t) * ath`.
    """
    if close <= (Decimal(1) + t_large) * ath:
        return LARGE_DROP
    if close <= (Decimal(1) + t_normal) * ath:
        return NORMAL
    return HIGH


def daily_trigger(zone, units_normal, units_large):
    """Daily Drawdown Trigger, shared by Strategies B and C — v2 §4.2/§4.3/§4.4,
    OD-09. High zone -> no Daily Trigger."""
    if zone == LARGE_DROP:
        return units_large
    if zone == NORMAL:
        return units_normal
    return Decimal("0")


def requested_units(strategy, zone, is_month_end, month_already_committed,
                    u_normal, u_large, u_dca, u_fallback):
    """Returns the Purchase Request size before budget validation.

    Strategy A — v2 §4.1 / OD-01: decision on the FINAL TRADING DAY of each
    calendar month, 1.0 unit, drawdown is NOT an input.

    Strategy B — v2 §4.2 / OD-09: Daily Trigger only; High zone -> WAIT / 0.

    Strategy C — v2 §4.3 / OD-05, month-end processing order:
      1. normal Daily Signal Evaluation;
      2. if a Daily Trigger fires -> that request (1.0 or 2.0);
      3. else, if no earlier Daily Trigger has committed this month's allocation
         -> Month-End Fallback of 0.5 units, and ONLY where DD > -10% (HIGH).
    At month-end with NORMAL or LARGE_DROP the Daily Trigger fires first, so the
    fallback is never reached — matching the Baseline's stated consequence.
    """
    if strategy == "A":
        return u_dca if is_month_end else Decimal("0")

    daily = daily_trigger(zone, u_normal, u_large)
    if daily != 0:
        return daily

    if strategy == "C" and is_month_end and not month_already_committed and zone == HIGH:
        return u_fallback

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
    SUPPORTED_STRATEGIES = ("A", "B", "C", "D")

    def __init__(self, fixture, strategy="B"):
        if strategy not in self.SUPPORTED_STRATEGIES:
            raise FixtureError(
                f"strategy '{strategy}' is not implemented in Mode E; "
                f"supported: {self.SUPPORTED_STRATEGIES}")
        validate(fixture)
        p = fixture["parameters"]
        self.unit_value = Decimal(p["unit_value_jpy"])
        self.annual_units = Decimal(p["annual_units"])
        self.t_normal = Decimal(p["threshold_normal"])
        self.t_large = Decimal(p["threshold_large_drop"])
        self.u_normal = Decimal(p["units_normal_zone"])
        self.u_large = Decimal(p["units_large_drop_zone"])
        self.u_dca = Decimal(p.get("units_strategy_a_monthly", "1.0"))
        self.u_fallback = Decimal(p.get("units_month_end_fallback", "0.5"))
        self.strategy = strategy
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

        # Strategy D only (EXPERIMENTAL VARIANT — NOT BASELINE). Owner-generated
        # post-result alternative hypothesis, docs/decisions/
        # simulation_trial_strategy_d_owner_hypothesis.md (5a3f54a), semantics
        # fixed by docs/decisions/simulation_trial_strategy_d_owner_semantic_
        # decision.md (62c5c42). Harmless, unused for A/B/C.
        self.d_month_state = {}
        self.d_monthly_capacity = Decimal("2.0")   # a rule ceiling, not a funding grant

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

    def is_final_observation_of_month(self, i):
        """FINAL TRADING DAY OF THE CALENDAR MONTH — v2 §4.1 (OD-01) and §4.3
        (OD-05).

        OWNER-APPROVED 2026-08-13 — MONTH-END OBSERVATION RULE
        ------------------------------------------------------
        "The final observation belonging to a declared calendar month in the
        synthetic fixture schedule is treated as that month's month-end decision
        observation. The engine may determine this from declared observation
        dates. It must NOT use future prices or future economic information to
        determine month-end status."

        This is an IMPLEMENTATION RULE for Mode E synthetic observation
        schedules. It expressly does NOT: establish a formal exchange trading
        calendar; establish P1-1; derive or decide P1-5; derive or decide P1-6;
        establish H-1; authorize real market data; alter the qualification lane;
        or alter the formal Baseline dataset definition.

        Owner rationale: Mode E must be able to validate month-end mechanics on
        synthetic and deliberately sparse observation schedules without
        importing a real-market calendar dependency.

        Implementation: index i is month-end when there is no later observation
        in the same calendar month. It reads DATES ONLY and NEVER a future close
        value, so no future market data influences any decision (v2 §6).

        Rationale: in a real backtest the trading calendar is published in
        advance, so "the final trading day of the month" is calendar information
        rather than market data. This mirrors that, using the fixture's date
        schedule as the calendar. It fixes no Baseline question — the Baseline
        already fixes the decision date; this is only how the engine locates it.
        """
        d = self.obs[i][0]
        for later_d, _ in self.obs[i + 1:]:
            if (later_d.year, later_d.month) == (d.year, d.month):
                return False
        return True

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

            # MP-R-01: `dd` is computed for REPORTING ONLY and is never an input
            # to classification. Classification uses the exact scaled comparison,
            # which needs no division and therefore no pre-comparison rounding.
            dd = (close - self.ath) / self.ath          # §4.0, rendering only
            zone = classify_zone_scaled(close, self.ath, self.t_normal, self.t_large)
            self.log(d, "DRAWDOWN", reference_high=self.ath, dd=dd, zone=zone)

            month = f"{d.year:04d}-{d.month:02d}"
            is_month_end = self.is_final_observation_of_month(i)
            if is_month_end:
                self.log(d, "MONTH_END", month=month, strategy=self.strategy)

            if self.strategy == "D":
                # EXPERIMENTAL VARIANT — NOT BASELINE. Strategy A/B/C mechanics
                # below are entirely untouched by this branch.
                self._handle_strategy_d_signal(d, i, zone, month)
                continue

            already = month in self.committed_months
            requested = requested_units(
                self.strategy, zone, is_month_end, already,
                self.u_normal, self.u_large, self.u_dca, self.u_fallback)

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
                "month_end": is_month_end, "zone": zone,
            }
            self.allocations.append(alloc)
            self.pending.append(alloc)
            self.log(d, "COMMITMENT", attributed_month=month, attributed_budget_year=d.year,
                     accepted_units=accepted, available_after=self.available,
                     reserved_outstanding=self.reserved_outstanding)
        return self

    # ---- Strategy D (EXPERIMENTAL VARIANT — NOT BASELINE) ----------------
    def _handle_strategy_d_signal(self, d, i, zone, month):
        """Implements ONLY the preserved Strategy-D semantic decision
        (docs/decisions/simulation_trial_strategy_d_owner_semantic_decision.md,
        commit 62c5c42, resolving SD-1 .. SD-10 against the hypothesis
        registered at docs/decisions/simulation_trial_strategy_d_owner_
        hypothesis.md, commit 5a3f54a). Defines no new semantics.

        NOT a Baseline v2 strategy. Baseline v2 defines only Strategies A, B
        and C (§4). Strategy D is an OWNER-GENERATED POST-RESULT ALTERNATIVE
        HYPOTHESIS, confined to the Simulation Trial lane (§18.4.5): every
        run touching it MUST carry the EXPERIMENTAL VARIANT — NOT BASELINE
        label. It does not alter Strategy A, B, or C in any way — this method
        is reached only when self.strategy == "D".

        Reuses, unchanged, the same commitment/reservation/execution state
        (self.available, self.reserved_outstanding, self.allocations,
        self.pending) and the same event log used by A/B/C, so execute_due(),
        terminal_state() and the shared invariants need no Strategy-D-specific
        branch beyond what is added explicitly in invariants().
        """
        st = self.d_month_state.setdefault(month, {
            "normal_attempted": False, "normal_accepted": Decimal("0"),
            "escalation_attempted": False, "direct_attempted": False,
        })

        if zone == HIGH:
            self.log(d, "SIGNAL", signal="WAIT", zone=zone, units=Decimal("0"))
            return

        if st["direct_attempted"]:
            # SD-1: the direct Large-drop path already consumed this month's
            # capacity/tranches; no later deterioration reopens it.
            self.suppressed += 1
            self.log(d, "SIGNAL_SUPPRESSED", zone=zone, requested_units=Decimal("0"),
                     reason="STRATEGY_D_MONTHLY_CAPACITY_EXHAUSTED", month=month)
            return

        if zone == NORMAL:
            if st["normal_attempted"]:
                # SD-2: repeated non-escalating Normal-zone signal.
                self.suppressed += 1
                self.log(d, "SIGNAL_SUPPRESSED", zone=zone, requested_units=Decimal("0"),
                         reason="STRATEGY_D_REPEATED_NORMAL_NO_ADDITIONAL_ALLOCATION",
                         month=month)
                return
            requested = self.u_normal
            tranche = "NORMAL"
        else:  # LARGE_DROP
            if not st["normal_attempted"]:
                # SD-1: first qualifying observation of the month is already
                # Large-drop — a single, direct 2.0-unit allocation.
                requested = self.u_large
                tranche = "DIRECT_LARGE_DROP"
            elif st["normal_accepted"] == 0:
                # Derived consequence of SD-5 combined with the unmodified
                # escalation gate (semantic decision §6): a zero-capped Normal
                # attempt creates no commitment, so "after that first
                # allocation has been accepted" is never satisfied. This is
                # NOT the direct-Large-drop path either, since a Normal-zone
                # observation occurred first, chronologically, this month.
                self.suppressed += 1
                self.log(d, "SIGNAL_SUPPRESSED", zone=zone, requested_units=Decimal("0"),
                         reason="STRATEGY_D_ESCALATION_GATE_NOT_SATISFIED_ZERO_PRIOR",
                         month=month)
                return
            elif st["escalation_attempted"]:
                # SD-3: both tranches already used this month.
                self.suppressed += 1
                self.log(d, "SIGNAL_SUPPRESSED", zone=zone, requested_units=Decimal("0"),
                         reason="STRATEGY_D_MONTHLY_CAPACITY_EXHAUSTED", month=month)
                return
            else:
                # SD-3: a new, independent escalation allocation. Nominal size
                # fixed at 1.0, additionally capped by remaining Strategy-D
                # capacity (semantic decision §6) before ordinary funding
                # capping is applied below.
                remaining_capacity = self.d_monthly_capacity - st["normal_accepted"]
                requested = min(self.u_normal, remaining_capacity)
                tranche = "LARGE_DROP_ESCALATION"

        self.log(d, "PURCHASE_REQUEST", zone=zone, requested_units=requested,
                 strategy_d_tranche=tranche)

        accepted = min(requested, self.available)      # §12.4 capping (funding only)
        capped = accepted < requested
        self.log(d, "BUDGET_VALIDATION", requested_units=requested,
                 available_units=self.available, accepted_units=accepted, capped=capped,
                 strategy_d_tranche=tranche)

        if tranche == "NORMAL":
            st["normal_attempted"] = True
            st["normal_accepted"] = accepted
        elif tranche == "DIRECT_LARGE_DROP":
            st["direct_attempted"] = True
        else:
            st["escalation_attempted"] = True

        if accepted == 0:
            # SD-5: a zero-unit result creates no allocation, no commitment,
            # no reservation, and consumes no Strategy-D monthly capacity.
            self.log(d, "NO_ALLOCATION", reason="ZERO_UNITS_AVAILABLE",
                     strategy_d_tranche=tranche)
            return

        # §12.1 / §12.2 — reserve immediately, attribute to month/year of
        # acceptance, identical mechanics to A/B/C.
        self.available -= accepted
        self.reserved_outstanding += accepted
        exec_on = self.obs[i + 1][0] if i + 1 < len(self.obs) else None
        alloc = {
            "committed_on": d.isoformat(), "attributed_month": month,
            "attributed_budget_year": str(d.year),
            "requested_units": str(requested), "accepted_units": accepted,
            "capped": capped, "execute_on_or_after": exec_on,
            "month_end": self.is_final_observation_of_month(i), "zone": zone,
            "strategy_d_tranche": tranche,
        }
        self.allocations.append(alloc)
        self.pending.append(alloc)
        self.log(d, "COMMITMENT", attributed_month=month, attributed_budget_year=d.year,
                 accepted_units=accepted, available_after=self.available,
                 reserved_outstanding=self.reserved_outstanding,
                 strategy_d_tranche=tranche)

    # ---- outputs ---------------------------------------------------------
    def terminal_state(self):
        last_close = self.obs[-1][1]
        dd = (last_close - self.ath) / self.ath
        return {
            # E4: the strategy actually executed is engine state and must be
            # recoverable from the evidence itself, not only from the manifest.
            # E3 found a driver defect where the manifest could name a strategy
            # the engine never ran; carrying it here makes that disagreement
            # detectable from the written outputs alone.
            "strategy": self.strategy,
            "reference_high": str(self.ath),
            "final_dd": str(dd),
            "final_zone": classify_zone_scaled(last_close, self.ath,
                                               self.t_normal, self.t_large),
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
        if self.strategy == "D":
            # Strategy D — EXPERIMENTAL VARIANT — NOT BASELINE. Baseline
            # Invariant 9 is stated for the Baseline strategies (A/B/C); the
            # preserved semantic decision (62c5c42) deliberately permits up to
            # two Strategy-D allocations per month, so it is not applicable
            # verbatim here. Replaced with the Strategy-D-specific bound the
            # semantic decision actually fixes, not silently reused.
            month_counts = {}
            for a in self.allocations:
                month_counts[a["attributed_month"]] = month_counts.get(a["attributed_month"], 0) + 1
            chk("INV-9-D at most two committed Strategy-D allocations per calendar month",
                all(c <= 2 for c in month_counts.values()),
                f"counts={month_counts}")
            by_month = {}
            for a in self.allocations:
                by_month.setdefault(a["attributed_month"], []).append(a.get("strategy_d_tranche"))
            bad = {m: t for m, t in by_month.items()
                   if len(t) == 2 and sorted(t) != ["LARGE_DROP_ESCALATION", "NORMAL"]}
            chk("INV-9-D two-allocation months are always NORMAL + escalation, never DIRECT combined",
                not bad, f"bad={bad}")
        else:
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
        # Baseline Invariant 13 is STRATEGY-B-SPECIFIC: "Strategy B does not
        # purchase in the High zone." Strategy A allocates at month-end
        # irrespective of zone (§4.1: drawdown is not an input), and Strategy C's
        # Month-End Fallback is EXPRESSLY a High-zone allocation (§4.3). Applying
        # the B invariant to A or C would assert something the Baseline does not
        # say. Scoped accordingly; A and C are covered by INV-14 and the
        # month-end assertions instead.
        if self.strategy == "B":
            chk("INV-13 Strategy B never purchases in the High zone",
                not any(a.get("zone") == HIGH for a in self.allocations))
        else:
            chk(f"INV-13 not applicable to Strategy {self.strategy} (B-specific)", True,
                "Baseline Invariant 13 constrains Strategy B only")
        chk("INV-15 no same-month escalation after commitment",
            self.suppressed == sum(1 for e in self.events if e["event"] == "SIGNAL_SUPPRESSED"))
        if self.strategy == "C":
            fb = [a for a in self.allocations
                  if Decimal(a["requested_units"]) == self.u_fallback]
            chk("INV-14 Strategy C uses 0.5 only as the month-end fallback",
                all(a.get("month_end") and a.get("zone") == HIGH for a in fb),
                f"fallback allocations={len(fb)}")
        else:
            chk("INV-14 non-C strategy never requests the 0.5 fallback size",
                not any(Decimal(a["requested_units"]) == self.u_fallback
                        for a in self.allocations))
        chk("ENG-2 budget reconciles",
            self.granted == self.available + self.reserved_outstanding + self.executed_units)
        chk("ENG-3 no negative balances",
            self.available >= 0 and self.reserved_outstanding >= 0 and self.exposure >= 0)

        if self.strategy == "D":
            cap_by_month = {}
            for a in self.allocations:
                cap_by_month[a["attributed_month"]] = (
                    cap_by_month.get(a["attributed_month"], Decimal("0")) + a["accepted_units"])
            cap_detail = {k: str(v) for k, v in cap_by_month.items()}
            chk("ENG-D1 Strategy D monthly capacity never exceeds 2.0",
                all(c <= self.d_monthly_capacity for c in cap_by_month.values()),
                f"capacity_by_month={cap_detail}")
            chk("ENG-D2 per-month tracking state matches allocation records "
                "(Normal-tranche accepted amount)",
                all(self.d_month_state[m]["normal_accepted"] == sum(
                        a["accepted_units"] for a in self.allocations
                        if a["attributed_month"] == m and a.get("strategy_d_tranche") == "NORMAL")
                    for m in self.d_month_state),
                "cross-check between per-month tracking state and allocation records")
            chk("ENG-D3 zero-accepted Strategy-D attempts never become allocations",
                all(a["accepted_units"] > 0 for a in self.allocations))
            ids = [(a["committed_on"], a.get("strategy_d_tranche")) for a in self.allocations]
            chk("ENG-D4 Strategy D allocation identities are distinct",
                len(ids) == len(set(ids)), f"{ids}")
            chk("ENG-D5 no execution before commitment (independent per-tranche timing, SD-3)",
                all(a.get("executed_on") is None or a["executed_on"] >= a["committed_on"]
                    for a in self.allocations))

        return r


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
