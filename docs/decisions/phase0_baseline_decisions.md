# Phase 0 — Baseline Owner Decision Record

**Status:** Accepted

**Scope:** Phase 0 — Baseline Specification

**Baseline status:** Frozen — Owner Approved

**Freeze documented:** 2026-08-11

---

## Purpose and precedence

This document records the **reasoning and decision history** that produced the
Frozen Phase 0 Baseline. It explains *why* Owner Decisions OD-01 through OD-14
were selected.

**It is not the normative strategy specification.**

The normative Baseline is [`docs/experiment_spec.md`](../experiment_spec.md).

> **Precedence:** If wording in this decision-history artifact conflicts with the
> Frozen experiment specification, [`docs/experiment_spec.md`](../experiment_spec.md)
> governs Baseline behavior.

This artifact contains no Baseline results and no performance claims.

### Relationship to exploratory work

No deterministic Baseline backtest had been implemented or run in this repository
before the Freeze, and no reproducible Baseline performance result existed.

Exploratory external analysis and partial historical observations did exist
before the Freeze, and they helped motivate the experiment design — for example,
the questions of whether month-end-only drawdown observation could miss important
intramonth drawdowns, whether Daily Drawdown Trigger behavior deserved
investigation, whether pure drawdown timing and drawdown timing with a DCA floor
should be separated into distinct strategies, and whether waiting for drawdowns
could create meaningful cash drag.

That exploratory work was preliminary and its performance estimates were rough
and unverified. It is **hypothesis-forming context, not part of the reproducible
Baseline evidence**, and it is not validation of Strategies A, B, or C. Nothing
in this record quantifies it, and no figure from it appears anywhere in this
repository.

The research pipeline is therefore:

```
Exploratory analysis / hypothesis formation
  → Phase 0 specification and Owner Decisions
    → Baseline Freeze
      → Phase 1 Data Foundation
        → Phase 2 deterministic reproducible Baseline backtest
          → Baseline evidence
```

Only the final stage produces Baseline evidence.

---

## Decision index

| ID | Decision | Status |
| -- | -------- | ------ |
| [OD-01](#od-01--strategy-a-purchase-decision-date) | Strategy A purchase decision date | Approved |
| [OD-02](#od-02--drawdown-reference-high) | Drawdown Reference High | Approved |
| [OD-03](#od-03--signal-observation-timing) | Signal observation timing | Approved |
| [OD-04](#od-04--execution-price-convention) | Execution price convention | Approved |
| [OD-05](#od-05--strategy-c-month-end-processing-order) | Strategy C month-end processing order | Approved |
| [OD-06](#od-06--same-month-trigger-escalation) | Same-month trigger escalation | Approved |
| [OD-07](#od-07--cash-return-assumption) | Cash return assumption | Approved |
| [OD-08](#od-08--baseline-evaluation-metrics) | Baseline evaluation metrics | Approved |
| [OD-09](#od-09--strategy-b-high-zone-behavior) | Strategy B High-zone behavior | Approved |
| [OD-10](#od-10--annual-satellite-budget-availability) | Annual satellite budget availability | Approved |
| [OD-11](#od-11--fees--fund-expenses--tracking-difference) | Fees / fund expenses / tracking difference | Approved |
| [OD-12](#od-12--backtest-period) | Backtest period | Approved |
| [OD-13](#od-13--monthly-allocation-and-budget-commitment-boundary) | Monthly allocation and budget commitment boundary | Approved |
| [OD-14](#od-14--first-partial-year-funding) | First partial-year funding | Approved |

---

## OD-01 — Strategy A Purchase Decision Date

**Status:** Approved

### Question

The control strategy needed a fixed, mechanical monthly decision date. Leaving it
unstated would have allowed month-start, month-end, or an arbitrary calendar day
to be chosen later — potentially after seeing results — and the term "month" was
not formally defined.

### Decision

- "Month" means **calendar month**.
- Strategy A makes its monthly allocation decision on the **final trading day** of
  each calendar month.
- Strategy A requests **1.0 unit**.
- The decision defines the **decision date only**; execution timing and the
  applicable valuation are governed separately by OD-04.

### Rationale

- Gives the control a fixed mechanical timing.
- Avoids introducing a second market-timing hypothesis into the control. A
  control whose entry date was itself a tunable choice would confound the
  comparison the experiment is trying to make.
- Aligns cleanly with monthly comparison and with the Strategy C month-end
  fallback structure, so all three strategies share the same monthly boundary.

### Consequences

- The decision date is fixed and no longer selectable after the fact.
- Execution still follows OD-04, so Strategy A's decision and its fill remain
  distinct events.

### Deferred / Related Work

- Execution date and applicable NAV: OD-04, resolved with Phase-1 evidence.

---

## OD-02 — Drawdown Reference High

**Status:** Approved

### Question

Drawdown is meaningless without a reference. Several mutually incompatible
references were plausible: month-end ATH, daily closing ATH, intraday high ATH,
investment-start-date high, and full-history high. Each produces different
trigger frequencies and different zone assignments from the same market path.

### Decision

- The Baseline Reference High is the **Daily Closing All-Time High**: the highest
  daily closing value observable up to and including the current decision date.
- The current market value and the Reference High MUST use the **same price
  series and the same observation basis**.
- Historical observations preceding the measured performance start MAY be used to
  initialize the ATH.
- Future observations MUST NOT be used.
- Intraday highs are excluded from the Baseline.

### Rationale

- A closing-price-to-closing-price comparison is deterministic and symmetric.
- It avoids mixing intraday peaks with closing observations, which would deepen
  measured drawdown on one side of the ratio only.
- It preserves historical market information available before the simulation
  start, rather than artificially resetting the reference at the start date.

### Consequences

- The Reference High never decreases within a run.
- A new closing high sets drawdown to 0%.
- The choice is a research parameter like any other: alternative references are
  Phase-4 sensitivity work, not Baseline edits.

### Deferred / Related Work

- Alternative Reference High definitions: Phase 4 sensitivity (S-6).
- Numeric comparison tolerance at zone boundaries: methodology (M-7).

---

## OD-03 — Signal Observation Timing

**Status:** Approved

### Question

At what moment of a trading day is a drawdown condition considered observed? This
determines whether a same-day execution is even logically possible.

### Decision

Daily Drawdown Signals are evaluated **only after the confirmed daily close**, in
this order:

1. Observe the confirmed daily close.
2. Add it to the information available as of that date.
3. Update the Daily Closing ATH.
4. Compute drawdown.
5. Evaluate the strategy rule.
6. Generate a Signal and, where applicable, a Purchase Request.
7. Execution occurs separately.

Signal and Execution remain separate events, and the same confirmed close MUST
NOT retrospectively serve as the fill price for the Signal it generated.

### Rationale

- Prevents look-ahead and impossible execution assumptions. A close cannot be
  both the trigger and the fill without assuming the decision was made before the
  information that produced it existed.

### Consequences

- Every Signal necessarily precedes its own execution in time.
- If the close sets a new ATH, drawdown is 0% and no drawdown trigger fires.

### Deferred / Related Work

- The concrete fill valuation: OD-04, Phase-1 evidence (P1-1).

---

## OD-04 — Execution Price Convention

**Status:** Approved (principle), with Phase-1 resolution

### Question

Which valuation converts an accepted Purchase Request into exposure? The intended
live implementation target is a Japanese mutual fund, whose applicable NAV is not
observable at order time, so no convention could be adopted from convenience
alone.

### Decision

- **Principle approved:** signal generation and execution MUST remain separate.
- The Baseline execution model MUST use the **earliest realistically obtainable
  valuation / NAV** after the Signal becomes observable.
- Retrospective execution at the signal-generating close is **prohibited**.
- The exact `Signal Date → order timing → Execution Date → applicable NAV`
  mapping is **delegated to Phase 1** and must come from authoritative product
  documentation.

### Rationale

- The intended live implementation is a Japanese mutual fund, not an
  instantaneously fillable instrument.
- Order and NAV timing can materially affect crash-period results, which is
  precisely where Strategies B and C differ most from A.
- Execution realism must be evidence-based rather than convenient. Adopting
  same-day-close, next-open, or next-close because it is easy to implement would
  embed an unexamined assumption into every result.

### Consequences

- Phase 2 implementation cannot begin until the mapping exists.
- Results will be interpretable only against a documented execution model.

### Deferred / Related Work

- Phase-1 evidence (P1-1): order cutoff timing, application/order date, execution
  or contract date, NAV determination timing, the JST-to-U.S.-session
  relationship, holiday handling, and whether the convention is historically
  reproducible.

---

## OD-05 — Strategy C Month-End Processing Order

**Status:** Approved

### Question

On the final trading day of a month, Strategy C could in principle evaluate both
a Daily Drawdown Trigger and the Month-End Fallback. The specification needed a
defined order, and needed to state what happens when month-end drawdown is at or
below -20% — a case that "should not normally occur" but can.

### Decision

- The final trading day first receives **normal Daily Signal evaluation**.
- The Daily Trigger has **priority**.
- The Month-End Fallback is evaluated **only** when no Daily Trigger has committed
  an allocation for that calendar month.
- A month-end `DD <= -20%` is a normal **2.0-unit** Daily Trigger.
- A month-end `-20% < DD <= -10%` is a normal **1.0-unit** Daily Trigger.

### Rationale

- Avoids artificial month-end special cases. The edge case is removed by ordering
  rather than by asserting it cannot happen.
- Keeps the daily and month-end state transition deterministic.

### Consequences

- The month-end edge case is no longer an exception; it is ordinary daily
  behavior that happens to occur on the last trading day.
- Because the Daily Trigger is evaluated first, the fallback is reachable only
  when `DD > -10%`, where it requests 0.5 units. In the `-20% < DD <= -10%` band
  the daily and fallback readings would both yield 1.0 unit, so the ordering
  changes no allocation.

---

## OD-06 — Same-Month Trigger Escalation

**Status:** Approved

### Question

If a 1.0-unit allocation is committed early in a month and a deeper drawdown
appears later in the same month, may the strategy top up, replace, or escalate
the earlier allocation?

### Decision

- At most **one committed satellite allocation per calendar month**.
- No later top-up, even if a stronger drawdown tier appears.
- Stronger later Signals remain observable and are recorded as evidence; their
  execution is suppressed with an explicit reason.
- Escalation is **not** Baseline behavior.

### Rationale

- Keeps the Baseline as a single 0 / 0.5 / 1.0 / 2.0 allocation choice, rather
  than turning it into a staged averaging-down strategy.
- Isolates escalation as a separate later hypothesis, so that the Baseline result
  measures one mechanism at a time.

### Consequences

- A month in which drawdown deepens sharply after an early commitment will show a
  suppressed stronger Signal in the evidence record — a visible, auditable cost
  of the rule rather than a hidden one.

### Deferred / Related Work

- Escalation variants: Phase 4 sensitivity (S-3). They MUST NOT be presented
  retroactively as Baseline evidence.

---

## OD-07 — Cash Return Assumption

**Status:** Approved

### Question

Strategies B and C hold uninvested satellite budget for extended periods;
Strategy A does not. How that cash is valued directly affects the fairness of the
comparison.

### Decision

- Unused satellite budget is **nominal JPY cash at 0% return**.
- Its economic value remains in TTEV and in terminal comparisons.
- Unused fractional units, including 0.5-unit increments, carry forward.
- Units do not expire.

### Rationale

- Isolates the variable-DCA timing hypothesis from a separate cash-management
  return hypothesis.
- Prevents unused budget from disappearing from portfolio accounting.
- Gives no artificial yield advantage to the variable strategies, which would
  otherwise be rewarded for waiting by an assumption rather than by the strategy
  itself.

### Consequences

- Cash drag in B and C is fully visible rather than masked by an assumed yield.
- The comparison neither penalizes nor subsidizes holding cash.

### Deferred / Related Work

- Non-zero cash, money-market, deposit, and risk-free-rate scenarios: Phase 4
  sensitivity (S-4).

---

## OD-08 — Baseline Evaluation Metrics

**Status:** Approved

### Question

"Improve capital deployment" had to be operationalized before any Baseline result
existed, otherwise the deciding metric could be chosen after seeing which one
favored a preferred strategy.

### Decision

- **Primary Metric: Terminal Total Economic Value (TTEV)** =
  market value of acquired NASDAQ exposure + remaining unused satellite cash,
  evaluated at a **common comparison date**.
- **Required Secondary Metrics:** total funding supplied; total amount invested;
  remaining cash; units / shares acquired; average acquisition cost; number of
  purchases; reserve utilization; reserve exhaustion events; maximum portfolio
  drawdown; money-weighted return / XIRR.
- Rolling-window analysis is required later for regime dependence and robustness.
- Overlapping rolling windows alone do not justify statistical significance
  claims.
- External funding and internal deployment remain conceptually separate: annual
  funding is common external funding; moving satellite cash into exposure is an
  internal allocation, not a new contribution.

### Rationale

- Acquisition price alone can reward excessive waiting while hiding opportunity
  cost — a strategy that almost never buys can post an excellent average price
  and a poor outcome.
- TTEV keeps invested and uninvested economic value comparable across strategies
  with different deployment schedules.

### Consequences

- No single efficiency metric can decide superiority.
- Metric definitions must be fixed before results are inspected.

### Deferred / Related Work

- Exact secondary-metric formulas (M-1), rolling-window lengths (M-2),
  rolling-window boundary-state initialization (M-3), TTEV treatment of a
  committed-but-unexecuted allocation (M-5), reserve-exhaustion counting (M-6),
  and statistical methodology (M-8): methodology review.

---

## OD-09 — Strategy B High-Zone Behavior

**Status:** Approved

### Question

The earlier draft assigned an allocation to every drawdown zone for Strategy B,
including `DD > -10%`. Read literally, that made a purchase condition true on
every trading day, so Strategy B could never skip a month — contradicting its
stated concept and collapsing the distinction between B and C.

### Decision

Strategy B:

- `DD > -10%` → **WAIT / 0 units**
- `-20% < DD <= -10%` → **1.0 unit**
- `DD <= -20%` → **2.0 units**
- No fallback. The 0.5-unit size is **not used by Strategy B**.

Strategy roles:

- **A** — Fixed DCA control
- **B** — Pure Drawdown Timing
- **C** — Drawdown Timing with a DCA Floor

### Rationale

- Prevents Strategy B from degenerating into an automatic first-trading-day
  0.5-unit purchase, which would have made it a near-duplicate of C.
- Makes the B-versus-C comparison directly measure the cost and benefit of the
  DCA floor and the associated cash drag.

### Consequences

- Strategy B may go months, or longer, with no allocation at all.
- The three strategies now occupy genuinely distinct research roles, which is
  what makes the comparison informative.

---

## OD-10 — Annual Satellite Budget Availability

**Status:** Approved

### Question

"12 units per year" did not state when the units become available. Under monthly
accrual, a 2.0-unit trigger in January would be capped by availability; under a
start-of-year grant it would not.

### Decision

- **12.0 new units available in full at the start of every normal calendar year.**
- Not monthly accrual.
- Unused units carry forward without expiry.
- No future-year borrowing.
- Identical funding capacity and identical funding timing for A, B, and C.

### Rationale

- The experiment is about reallocating an annual funding capacity *through time*.
- Monthly release would artificially prevent larger purchases during early-year
  drawdowns, which would suppress exactly the behavior the experiment exists to
  measure.

### Consequences

- Availability within a calendar month can only decrease, never increase.
- A deep early-year drawdown is fully fundable.

### Deferred / Related Work

- Artificial boundary state for rolling-window experiments remains a methodology
  requirement (M-3). OD-10 does not define it.

---

## OD-11 — Fees / Fund Expenses / Tracking Difference

**Status:** Approved (principle), with Phase-1 resolution

### Question

Applying a cost model to proxy data risks double-counting costs already embedded
in a NAV series, and assuming tracking difference equals the stated expense ratio
would manufacture precision the evidence does not support.

### Decision

- Costs MUST NOT be silently ignored **or** double-counted.
- When actual fund NAV data are used, costs already embedded in the published NAV
  MUST NOT be deducted again.
- When a proxy is used, its return composition MUST be established before any
  adjustment is applied.
- Tracking difference MUST NOT be assumed equal to the stated expense ratio.
- Where evidence does not support a defensible historical product-cost
  reconstruction, an unadjusted proxy result and a separately identified
  cost-adjusted scenario MAY both be reported.
- Exact treatment is delegated to Phase 1.

### Rationale

- Avoids false precision.
- Avoids double-counting.
- Prevents unsupported reconstruction of historical product costs.

### Consequences

- Any cost model must be explicit, reproducible, evidence-based, and
  distinguishable from the raw proxy return.

### Deferred / Related Work

- Phase-1 evidence: proxy return composition (P1-3) and evidence-based cost /
  expense treatment (P1-4).

---

## OD-12 — Backtest Period

**Status:** Approved (principle), with Phase-1 resolution

### Question

Choosing a start date after seeing performance is a form of post-hoc selection,
and a moving dataset would make an originally reported result irreproducible.

### Decision

- The Full-History Baseline uses the **longest defensible continuous history** of
  the Phase-1-approved Primary Proxy.
- The start date is determined by data availability and methodology, **not** by
  performance inspection.
- Pre-performance data may serve as **ATH warm-up only** and MUST NOT enter
  measured performance.
- Phase 1 establishes a fixed **Baseline Dataset Cutoff**.
- Later data are separate **extended** or **out-of-sample** evidence.
- Rolling-window analysis is separate from the Full-History Baseline.

### Rationale

- Prevents start-date cherry-picking.
- Preserves reproducibility of the originally reported Baseline result: newer
  observations must not silently alter it.

### Consequences

- The Baseline result is permanently tied to a stated cutoff.
- Extending the data produces additional evidence, not a revised Baseline.

### Deferred / Related Work

- Phase-1 evidence: approved Primary Proxy (P1-2), exact Baseline start date
  (P1-5), fixed Baseline Dataset Cutoff (P1-6), currency treatment (P1-7).

---

## OD-13 — Monthly Allocation and Budget Commitment Boundary

**Status:** Approved

### Question

Because execution can occur after the decision date — potentially in a later
month or year — the specification had to state exactly when budget is consumed,
which month an allocation belongs to, and what happens to later signals while an
earlier request is still pending.

### Decision

Conceptual state model:

```
Market Observation
  → Signal
    → Purchase Request
      → Budget Validation
        → Allocation Commitment / Unit Reservation
          → Execution Pending
            → Execution
```

At Purchase Request acceptance:

- Accepted units are **reserved immediately** and removed from available units
  immediately.
- The allocation is attributed to the **acceptance calendar month** and the
  **budget year available at acceptance**.
- Delayed execution does **not** change that attribution.
- Execution does **not** deduct the reserved budget a second time.
- A request is **capped at currently available units**.
- Future-year units cannot later enlarge an old capped request.
- Once an allocation is committed, later same-month Signals cannot create another
  Purchase Request.
- A delayed prior-month execution does **not** consume the next month's
  allocation.

### Rationale

- Execution may occur after the decision date, month, or year.
- Monthly strategy state and product settlement timing must not be conflated.
- Prevents double-counting and budget-year leakage.

### Consequences

- A December decision executing in January still belongs to December and to that
  year's budget.
- A new calendar month can independently generate an allocation while an earlier
  month's request is still pending.

### Deferred / Related Work

- Execution-failure retry, cancellation, and reservation-release semantics:
  methodology (M-4). One requirement is already fixed: failed or cancelled
  execution MUST NOT cause reserved economic value to disappear from accounting.
- Zero-unit-acceptance semantics for reason codes and reserve-exhaustion
  counting: methodology (M-6).

---

## OD-14 — First Partial-Year Funding

**Status:** Approved

### Question

OD-10 grants 12.0 units at the beginning of each calendar year, and OD-12 leaves
the Baseline start date to Phase 1. If the approved performance start falls after
1 January, the first year's grant size was undetermined. This was the final
strategy-rule issue identified by the independent Owner Review of OD-01 through
OD-13.

### Decision

- If Full-History Baseline performance begins **after 1 January**, the first
  measured year receives the **full 12.0 units at the simulation performance
  start**.
- **No proration** by months remaining, days remaining, fraction of year elapsed,
  or any other time-based accrual method.
- A, B, and C receive **identical** starting-year funding.
- The fact that the first measured year is a partial calendar year MUST be
  reported explicitly with the Baseline result.
- Applies **only** to the Full-History Baseline start boundary. It is **not** a
  rolling-window initialization rule.

### Rationale

- Preserves OD-10's annual-capacity concept: capacity is annual, and the strategy
  decides when to deploy it.
- Avoids reintroducing monthly-accrual logic for the first year only, which OD-10
  had deliberately rejected.
- Avoids arbitrary proration conventions, each of which would be a silent
  research parameter.

### Consequences

- In a partial first year, **Strategy A may structurally carry more units
  forward**, because it can request at most 1.0 unit per remaining month while B
  and C may deploy larger amounts sooner.
- **This is an intended property of the approved Baseline and MUST NOT be
  retroactively "corrected" after results are observed.** The mandatory
  partial-year disclosure exists so that this property is visible to any reader
  of the result.

### Deferred / Related Work

- Rolling-window artificial boundary-state initialization remains a methodology
  requirement (M-3), separate from OD-14.

---

## Phase 0 Baseline Freeze

**Status:** Owner Approved

**Freeze documented:** 2026-08-11

Record of the freeze:

- **OD-01 through OD-14 were individually approved** by the Owner.
- The **Cross-Decision Consistency Review passed** — no unresolved cross-decision
  inconsistency was identified after OD-13.
- An **independent Owner Review passed** after OD-14 resolved the final
  strategy-rule issue that review identified (first partial-year funding).
- The **OD-14 revision was reviewed and approved**.
- The Owner **explicitly approved the Phase 0 Baseline Freeze**.
- **No repository-implemented deterministic Baseline backtest had been run before
  the Freeze,** and no reproducible Baseline performance result existed. No code
  has been written and no data has been obtained in this repository.
- **Exploratory external analysis preceded the Freeze.** Partial historical
  observations and rough, unverified performance estimates existed before
  repository initialization and helped motivate the research question and
  experiment design. They are hypothesis-forming context, **not** Baseline
  evidence, and were not used to tune the Frozen rules against an observed
  Baseline result. See
  [Relationship to exploratory work](#relationship-to-exploratory-work).

### Normative artifact

The Frozen normative specification is
[`docs/experiment_spec.md`](../experiment_spec.md). This decision record explains
reasoning only.

### What the Freeze does not settle

Freezing the strategy specification did not resolve, and did not require
resolving:

- Phase-1 Blocking Evidence Requirements (P1-1 … P1-9)
- Methodology Requirements (M-1 … M-8)
- Phase-4 Deferred Sensitivity Questions (S-1 … S-6)

These remain open and are recorded in
[Section 19 of the specification](../experiment_spec.md#19-open-items-register).
Phase-1 items remain **hard gates before Phase 2 implementation**.

### Change control after the Freeze

Subsequent changes to thresholds, sizing, cash assumptions, escalation behavior,
annual budget, Reference High definition, or any other Baseline rule are **not
Baseline changes** unless the research governance explicitly creates a **new
Baseline version**.

Ordinary sensitivity analysis MUST be reported separately from the Frozen
Baseline and MUST NOT be presented as pre-specified Baseline evidence.

Frozen means pre-specified. It does not mean validated, and it does not mean
approved for live investment use.
