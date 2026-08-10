# Experiment Specification — Baseline

**Status: Frozen — Owner Approved**

**Phase: 0 — Baseline Specification**

**Revision: incorporates Owner Decisions OD-01 through OD-14 (all APPROVED),
following the Cross-Decision Consistency Review (result: PASS), the independent
Owner Review of OD-01 through OD-13 (result: PASS WITH ONE ADDITIONAL OWNER
DECISION, resolved by OD-14), and approval of the OD-14 revision.**

This document defines **what** will be tested. It contains no code, no
methodology implementation, and no results.

### Freeze statement

The Owner has explicitly approved the **Phase 0 Baseline Freeze**.

- **OD-01 through OD-14 constitute the Frozen Baseline Owner Decisions.**
- The strategy rules for Strategies A, B, and C are now **pre-specified before
  any repository-implemented deterministic Baseline backtest has been run**, and
  before any reproducible Baseline performance result exists.
- Exploratory analysis conducted before repository initialization informed the
  research question and experiment design. Those preliminary observations and
  rough estimates are **not Baseline evidence**, are not reproducible Baseline
  validation of Strategies A, B, or C, and have not been used to tune the Frozen
  rules against an observed Baseline result.
- Phase-1 evidence requirements remain unresolved where documented in
  [Section 19.1](#191-phase-1-blocking-evidence-requirements), and methodology
  requirements remain open where documented in
  [Section 19.2](#192-methodology-requirements-before-implementation). Freezing
  the strategy specification did not resolve them and did not require resolving
  them.
- Those Phase-1 requirements remain **hard gates before Phase 2 implementation**.

**What "Frozen" does not mean:**

- Frozen does **NOT** mean the strategy has been validated.
- Frozen does **NOT** mean the strategy is approved for live investment use.
- Negative results, including a finding that Strategy A outperforms B or C,
  remain valid evidence and MUST be reported.
- Later parameter changes MUST NOT silently modify the Frozen Baseline. Any
  change to thresholds, sizing, cash assumptions, escalation behavior, annual
  budget, or the Reference High definition is a **new Baseline version** created
  under explicit research governance, or else it is sensitivity analysis reported
  separately — never a retroactive edit to this Frozen Baseline.

The decision history explaining *why* OD-01 through OD-14 were selected is
recorded separately in `docs/decisions/phase0_baseline_decisions.md`. Where that
artifact and this specification differ, **this specification governs Baseline
behavior**.

---

## 0. How to read this document

Every substantive item is classified with one of the following markers.

| Marker | Meaning |
| ------ | ------- |
| `[BASELINE — OD-nn]` | Fixed by an approved Owner Decision. Part of the Baseline. Implementation MUST follow it once the Baseline is frozen. |
| `[CONTEXT]` | Recorded contextual input. Not simulated by the initial backtest. |
| `[PHASE-1 EVIDENCE]` | Deliberately delegated by an approved Owner Decision to Phase 1 — Data Foundation. Must be established from evidence, not assumed. Blocking for Phase 2 implementation, **not** for Baseline Freeze. |
| `[METHODOLOGY]` | Deliberately delegated to methodology review before implementation. Not an unresolved Owner Decision. |
| `[DEFERRED — PHASE 4]` | Explicitly excluded from the Baseline; may be studied later as sensitivity analysis. |

Normative keywords (MUST, MUST NOT, MAY, SHOULD) are used deliberately.

Where a decision has not been made, this document states that it has not been
made. It does not fill the gap with a plausible default.

### 0.1 Owner Decision register

| ID | Subject | Status | Primary location in this document |
| -- | ------- | ------ | --------------------------------- |
| OD-01 | Strategy A purchase decision date; "month" = calendar month | APPROVED | [4.1](#41-strategy-a--simple-dca-control) |
| OD-02 | Drawdown Reference High = Daily Closing ATH | APPROVED | [7](#7-drawdown-reference-high) |
| OD-03 | Signal observation timing | APPROVED | [8](#8-signal-observation-timing) |
| OD-04 | Execution price convention (principle approved; mapping to Phase 1) | APPROVED WITH PHASE-1 RESOLUTION | [9](#9-execution-model) |
| OD-05 | Strategy C month-end `DD <= -20%` edge case | APPROVED | [4.3](#43-strategy-c--daily-drawdown-trigger--month-end-fallback) |
| OD-06 | Same-month trigger escalation excluded | APPROVED | [10](#10-one-allocation-per-calendar-month) |
| OD-07 | Cash return assumption = 0% nominal JPY | APPROVED | [11.3](#113-cash-return-assumption) |
| OD-08 | Baseline evaluation metrics; TTEV primary | APPROVED | [13](#13-evaluation-metrics) |
| OD-09 | Strategy B High-zone behavior = WAIT / 0 units | APPROVED | [4.2](#42-strategy-b--daily-drawdown-trigger) |
| OD-10 | Annual satellite budget availability | APPROVED | [11.1](#111-annual-grant-and-carry-forward) |
| OD-11 | Fees / fund expenses / tracking difference | APPROVED WITH PHASE-1 RESOLUTION | [14.5](#145-cost-and-expense-treatment) |
| OD-12 | Backtest period and dataset cutoff | APPROVED WITH PHASE-1 RESOLUTION | [14.6](#146-baseline-period-and-dataset-cutoff) |
| OD-13 | Allocation and budget commitment boundary | APPROVED | [12](#12-allocation-commitment-and-budget-reservation) |
| OD-14 | First partial-year funding at the Full-History Baseline start boundary | APPROVED | [11.1](#111-annual-grant-and-carry-forward) |

---

## 1. Research objective

**Central experiment:**

> Evaluate whether a deterministic variable-DCA satellite strategy for
> NASDAQ-100-related exposure can improve capital deployment relative to simple
> fixed DCA, while preserving reproducibility and eliminating discretionary
> timing.

The experiment is designed to be capable of **rejecting** the hypothesis.

- The variable-DCA strategies MUST NOT be assumed to outperform.
- A result showing Strategy A (simple DCA) equal to or better than B or C is a
  valid outcome and MUST be reported as such.
- "Improve capital deployment" is operationalized by OD-08: the primary decision
  metric is **Terminal Total Economic Value (TTEV)**, supported by the required
  secondary metrics. See [Section 13](#13-evaluation-metrics).

---

## 2. Portfolio context

The satellite strategy exists inside a broader investment structure with a fixed
core and a tactical satellite. This section records **contextual inputs only**.
Nothing in this section is simulated by the initial backtest (see
[Section 15](#15-scope-boundary)).

### 2.1 Core investment — Sony Life `[CONTEXT]`

| Item | Value |
| ---- | ----- |
| Contract | Sony Life conventional variable annuity / variable insurance contract |
| Special account allocation | World Core Equity 100% |
| Monthly premium | JPY 11,685 |
| Handling | Existing contract is maintained |

- The core allocation MUST NOT be dynamically changed by the satellite strategy.
- The Sony Life contract is **not** the primary object of the initial NASDAQ
  variable-DCA experiment.

### 2.2 Core investment — NISA monthly investment `[CONTEXT]`

Monthly total: **JPY 50,000**

| Fund | Monthly amount |
| ---- | -------------- |
| iFree Nikkei 225 Index | JPY 5,000 |
| Tawara No-Load Developed Countries Equity | JPY 18,000 |
| Nissay NASDAQ100 Index Fund | JPY 6,000 |
| eMAXIS Slim S&P 500 | JPY 11,000 |
| SBI iShares Gold Fund (unhedged) | JPY 10,000 |

- Japanese NISA bucket eligibility of each fund is **out of scope** for this
  document.
- This document makes **no claim** about tax eligibility, official NISA
  classification, or tax treatment of any fund listed above.

### 2.3 Satellite investment `[BASELINE — OD-07, OD-10, OD-14]`

| Item | Value |
| ---- | ----- |
| Intended real-world implementation target | Nissay NASDAQ100 Index Fund |
| Annual satellite budget | JPY 120,000 per year |
| Unit definition | 1 unit = JPY 10,000 |
| Annual grant | 12.0 new units per calendar year, granted in full at the start of the year (for a first measured year beginning after 1 January, granted in full at the simulation performance start — OD-14) |

Budget mechanics are specified in [Section 11](#11-budget-accounting) and
[Section 12](#12-allocation-commitment-and-budget-reservation).

---

## 3. State model

`[BASELINE — OD-03, OD-04, OD-13]`

The Baseline distinguishes the following conceptual states. This is a conceptual
model, not an implementation design.

```
Market Observation
  → Signal
    → Purchase Request
      → Budget Validation
        → Allocation Commitment / Unit Reservation
          → Execution Pending
            → Execution
```

| State | Meaning |
| ----- | ------- |
| Market Observation | A confirmed daily closing value becomes observable and is added to available history. |
| Signal | The applicable strategy rule evaluates to a purchase condition at that decision date. |
| Purchase Request | A requested unit quantity produced by the Signal, **before** budget validation. |
| Budget Validation | Available units are checked; the request is capped at available units if necessary. |
| Allocation Commitment / Unit Reservation | The accepted units are reserved and removed from available units immediately. The allocation is attributed to the calendar month and budget year of acceptance. |
| Execution Pending | The committed allocation awaits its applicable execution valuation. |
| Execution | The reserved amount converts into NASDAQ exposure at the applicable valuation. |

Two separations are mandatory and MUST be preserved throughout the
specification, the evidence records, and any future implementation:

> **Signal ≠ Execution**
>
> **Allocation Commitment ≠ Execution**

These separations exist because the intended live implementation target is a
Japanese mutual fund whose applicable NAV is not observable at order time, and
because monthly and annual budget accounting must remain correct when execution
occurs after the decision date.

---

## 4. Strategy set

The initial baseline experiment compares three strategies under **identical
annual funding capacity and identical funding timing**.

| ID | Strategy | Research role |
| -- | -------- | ------------- |
| A | Simple DCA | Fixed DCA control |
| B | Daily Drawdown Trigger | Pure drawdown timing |
| C | Daily Drawdown Trigger + Month-End Fallback | Drawdown timing with a DCA floor |

`[BASELINE — OD-09]` These three research roles are distinct and MUST be
preserved. Strategy B is a pure timing strategy that may skip months entirely.
Strategy C is a timing strategy with a monthly floor that ensures some
allocation occurs in every month in which budget is available.

### 4.0 Drawdown zone semantics

`[BASELINE — OD-02]`

Let `DD(t)` be the drawdown at decision date `t`, expressed as a non-positive
value where `0%` means the current close equals the Reference High:

```
reference_high(t) = max( daily closes available through t )
DD(t) = ( close(t) - reference_high(t) ) / reference_high(t)
```

Zone boundaries are deterministic:

| Zone | Condition | Boundary belongs to |
| ---- | --------- | ------------------- |
| High zone | `DD > -10%` | — |
| Normal drawdown zone | `-20% < DD <= -10%` | `DD = -10.0%` belongs to the Normal drawdown zone |
| Large-drop zone | `DD <= -20%` | `DD = -20.0%` belongs to the Large-drop zone |

The three zones are mutually exclusive and jointly exhaustive over all real
values of `DD`. Zone membership alone does not imply a purchase; each strategy
defines which zones generate a Signal.

If the current close establishes a new Daily Closing ATH, then
`reference_high(t) = close(t)` and `DD(t) = 0%`.

`[METHODOLOGY]` Numeric comparison tolerance and rounding at the exact `-10.0%`
and `-20.0%` boundaries are an implementation-precision question for methodology
review. The boundary **semantics** above are fixed and MUST NOT be changed by
that review.

### 4.1 Strategy A — Simple DCA Control

`[BASELINE — OD-01]`

**Purpose:** provide a fixed-allocation control against which B and C are
compared.

| Item | Value |
| ---- | ----- |
| Annual funding capacity | JPY 120,000 / year (12.0 units) |
| Decision date | The **final trading day of each calendar month** |
| Requested units | 1.0 unit per calendar month |
| Drawdown signal | None |
| Discretionary timing | None |
| Maximum committed allocations per calendar month | 1 |

- OD-01 defines the **decision date only**. It does not define the execution date
  or the execution valuation; those are governed by
  [Section 9](#9-execution-model) (OD-04).
- Strategy A's Purchase Request is subject to the same budget validation and
  commitment rules as B and C ([Section 12](#12-allocation-commitment-and-budget-reservation)).
- Drawdown is not an input to Strategy A. Drawdown fields MAY still be recorded
  in Strategy A evidence records as observational context, but they MUST NOT
  influence the decision.

### 4.2 Strategy B — Daily Drawdown Trigger

`[BASELINE — OD-09]`

Strategy B is a **Pure Daily Drawdown Timing** strategy.

| Condition at decision date | Baseline behavior |
| -------------------------- | ----------------- |
| `DD > -10%` | **WAIT / 0 units.** No Signal, no Purchase Request. |
| `-20% < DD <= -10%` | Request **1.0 unit** |
| `DD <= -20%` | Request **2.0 units** |

- Drawdown is evaluated on every trading day, following the observation order in
  [Section 8](#8-signal-observation-timing).
- There is **no** month-end fallback in Strategy B.
- If no qualifying Daily Drawdown Trigger occurs during a calendar month,
  Strategy B makes **no** satellite allocation for that month.
- The 0.5-unit High-zone allocation is **NOT used by Strategy B**. It exists only
  as Strategy C's Month-End Fallback.
- At most one committed allocation per calendar month
  ([Section 10](#10-one-allocation-per-calendar-month)).

### 4.3 Strategy C — Daily Drawdown Trigger + Month-End Fallback

`[BASELINE — OD-05, OD-09]`

Strategy C uses **the same 1.0 / 2.0-unit Daily Drawdown Triggers as Strategy B**,
plus a month-end floor.

**Daily Drawdown Trigger (all trading days, including the final trading day of
the month):**

| Condition | Requested units |
| --------- | --------------- |
| `DD <= -20%` | 2.0 units |
| `-20% < DD <= -10%` | 1.0 unit |
| `DD > -10%` | No Daily Trigger; monitoring continues |

**Month-end processing order (OD-05).** On the final trading day of a calendar
month, Strategy C MUST evaluate in this order:

1. Perform normal Daily Signal Evaluation.
2. If a Daily Trigger fires, generate the applicable Purchase Request
   (1.0 or 2.0 units).
3. If no Daily Trigger fires **and** no earlier Daily Trigger has already
   committed that month's allocation, evaluate the Month-End Fallback.

**Month-End Fallback:**

| Condition at final trading day | Requested units |
| ------------------------------ | --------------- |
| `DD > -10%` | 0.5 units |

Consequences that MUST be stated explicitly:

- A month-end `DD <= -20%` is a **normal Daily Large-Drop Trigger** requesting
  2.0 units. It is **not** a special fallback case, and it is not an anomaly.
- A month-end `-20% < DD <= -10%` is a **normal Daily Drawdown Trigger**
  requesting 1.0 unit. Because the Daily Trigger is evaluated first on the same
  day, the fallback is never reached in this condition; the resulting allocation
  is 1.0 unit either way, so the two readings are outcome-identical. The fallback
  is therefore specified only for `DD > -10%`.
- The Month-End Fallback exists **only** when no Daily Trigger has committed an
  allocation for that calendar month.
- The 0.5-unit size is used **only** by Strategy C, and **only** as the Month-End
  Fallback.
- At most one committed allocation per calendar month
  ([Section 10](#10-one-allocation-per-calendar-month)).

### 4.4 Consolidated Baseline strategy matrix

| Condition / behavior | Strategy A | Strategy B | Strategy C |
| -------------------- | ---------- | ---------- | ---------- |
| Monthly model | Fixed DCA | Pure drawdown timing | Drawdown timing + DCA floor |
| Decision frequency | Final trading day of each calendar month | Every trading day | Every trading day |
| `DD > -10%` during month | No drawdown decision | WAIT / 0 units | WAIT / 0 units (fallback may apply at month-end) |
| `-20% < DD <= -10%` | No drawdown decision | 1.0-unit trigger | 1.0-unit trigger |
| `DD <= -20%` | No drawdown decision | 2.0-unit trigger | 2.0-unit trigger |
| No trigger committed by month-end | 1.0-unit monthly decision | 0 units | 0.5-unit fallback |
| Maximum committed allocations per calendar month | 1 | 1 | 1 |
| Same-month escalation after commitment | N/A | Not permitted | Not permitted |

All requested quantities above are **Purchase Requests**, which are then subject
to budget validation and may be capped at available units
([Section 12](#12-allocation-commitment-and-budget-reservation)).

---

## 5. Mechanical decision requirement

All strategy decisions MUST be deterministic and fully reducible to
machine-readable state and rules.

Discretionary judgement MUST NOT exist inside strategy logic. Examples of
prohibited reasoning:

- "market looks expensive"
- "this feels like a crash"
- "wait for confirmation"
- "buy more because sentiment is bad"

### 5.1 Evidentiary record requirement

For every simulated decision, the eventual implementation MUST be able to record
at least the following. This is a **conceptual and evidentiary** requirement; no
file format, schema, or column naming is defined at this stage.

| Field | Meaning |
| ----- | ------- |
| decision date | Simulated date on which the rule was evaluated |
| observed market value | Confirmed daily close used by the rule |
| reference high | Daily Closing ATH as of that decision date |
| calculated drawdown | `DD(t)` implied by the two values above |
| strategy ID | A, B, or C |
| trigger type | Which rule branch produced the outcome (daily trigger tier, month-end fallback, fixed monthly, or none) |
| requested units | Units requested before budget validation |
| available units | Units available at that moment |
| accepted / reserved units | Units accepted after capping, reserved immediately |
| allocation month | Calendar month to which the allocation is attributed |
| allocation budget year | Budget year charged at acceptance |
| execution date | Date of the applicable execution valuation (may be later) |
| execution valuation | Valuation actually used for execution |
| purchase amount | Monetary amount executed |
| units / shares acquired | Exposure acquired at execution |
| remaining available units | Available units after reservation |
| reason code | Deterministic code explaining the outcome |

Requirements:

- Decisions that result in **no** allocation MUST also be recordable, so that
  skipped months are auditable rather than inferred from absence.
- `[BASELINE — OD-06, OD-13]` Signals suppressed because the calendar month's
  allocation is already committed MUST be recorded with an explicit reason code
  identifying that cause, and MUST remain distinguishable from both executed
  allocations and no-signal days.

---

## 6. Look-ahead prohibition

Hard research constraint.

- No future market data MAY influence a decision.
- A decision MAY use only information available as of that simulated date.
- The Reference High MUST be constructed from historically observed information
  available at that moment ([Section 7](#7-drawdown-reference-high)).
- Data preprocessing MUST NOT leak future information. This includes, but is not
  limited to: full-sample normalization, full-sample statistics, backfilled
  values, retroactively revised series, and survivorship-filtered inputs.
- `[BASELINE — OD-03]` A Signal generated from a day's confirmed close MUST NOT
  be retrospectively executed at that same closing value.
- `[PHASE-1 EVIDENCE]` Where a data source is revised or restated after the fact,
  the effect on look-ahead MUST be assessed in Phase 1 rather than assumed
  negligible.

---

## 7. Drawdown Reference High

`[BASELINE — OD-02]`

The Baseline Drawdown Reference High is the **highest daily closing value
observable up to and including the current decision date** — the
**Daily Closing All-Time High**.

```
reference_high(t) = max( daily closes available through t )
DD(t)             = ( close(t) - reference_high(t) ) / reference_high(t)
```

Requirements:

- The Reference High and the current market value MUST use the **same price
  series** and the **same observation basis**.
- Intraday highs MUST NOT be used in the Baseline Reference High.
- Historical observations preceding the measured performance start MAY be used to
  initialize the Reference High. Such observations are **warm-up data**
  ([Section 14.6](#146-baseline-period-and-dataset-cutoff)) and MUST NOT be
  included in measured Baseline performance.
- Future observations MUST NOT be used.
- The Reference High MUST be constructed without look-ahead bias.
- The Reference High never decreases within a simulation run.

The definition above is conceptual. It MUST NOT be turned into implementation
code during Phase 0.

This resolves the former Open Question "Drawdown Reference High". Month-end ATH,
intraday-high ATH, and investment-start-date-only high are **not** the Baseline
reference. They MAY be examined in Phase 4 as sensitivity variants.

---

## 8. Signal observation timing

`[BASELINE — OD-03]`

Daily Drawdown Signals are evaluated **only after** the trading day's closing
value has become observable. The logical order for each trading day is:

1. Observe the confirmed daily close.
2. Add that close to the historical information available as of that date.
3. Update the Daily Closing ATH.
4. Calculate the current drawdown.
5. Evaluate the applicable strategy rule.
6. Generate a Signal and, where applicable, a Purchase Request.
7. Execution occurs separately under the execution model
   ([Section 9](#9-execution-model)).

Consequences:

- If the current close establishes a new ATH, the Reference High becomes that
  close and `DD = 0%`.
- A Signal generated using a day's confirmed close MUST NOT be retrospectively
  executed at that same closing value.
- Signal generation and execution are distinct events and MUST be recorded as
  distinct events.

---

## 9. Execution model

`[BASELINE — OD-04, principle approved]`

**Approved Baseline principle:**

- Signal generation and execution MUST remain separate.
- A Purchase Request generated from a confirmed daily closing signal MUST NOT be
  executed retrospectively at the same closing value used to generate that
  signal.
- The Baseline execution model MUST ultimately use the **earliest realistically
  obtainable valuation / NAV** for the intended Nissay NASDAQ100 Index Fund
  purchase after the Signal becomes observable.

**Not yet specified.** The exact mapping

```
Signal Date → Order timing → Execution Date → Applicable NAV
```

is **not** specified, and MUST NOT be invented for convenience. A same-day-close,
next-open, or next-close convention MUST NOT be assumed merely because it is
simple to implement.

### 9.1 `[PHASE-1 EVIDENCE]` Signal-to-order-to-NAV mapping

Phase 1 — Data Foundation MUST establish this mapping from authoritative product
documentation, investigating at minimum:

- applicable order cutoff timing
- application / order date
- execution or contract date
- NAV determination timing
- relationship between Japanese time and the relevant U.S. market session
- non-trading days and holidays in both calendars
- whether the convention can be reproduced historically

This is a **Phase-1 blocking evidence requirement before deterministic backtest
implementation**. It does not block Baseline Freeze of the strategy rules.

---

## 10. One allocation per calendar month

`[BASELINE — OD-01, OD-06, OD-13]`

"Month" in the Baseline means **calendar month**.

Baseline Strategies A, B, and C permit **at most one committed satellite
allocation per calendar month**.

**Purpose:** prevent repeated firing during extended drawdown conditions from
turning a strategy into uncontrolled repeated buying.

Normative statements:

- Once an allocation has been committed for a calendar month, no later Signal in
  that same calendar month MAY generate an additional Purchase Request.
- This remains true even if the later Signal belongs to a **stronger** drawdown
  tier.
- This remains true while the original committed request is still **pending
  execution**.
- Stronger later Signals MUST remain observable and SHOULD be recorded as
  evidence.
- Execution suppression MUST carry an explicit reason code indicating that the
  monthly allocation has already been committed.

**Worked example (OD-06):**

| Sequence within one calendar month | Outcome |
| ---------------------------------- | ------- |
| `DD = -11%` earlier in the month | 1.0-unit allocation committed |
| `DD = -23%` later in the same month | Large-Drop condition observed and recorded; **no** additional allocation |

`[DEFERRED — PHASE 4]` Same-month escalation is **not** part of the Baseline. An
escalation variant MAY be studied in Phase 4 — Sensitivity Analysis, but MUST NOT
be retroactively presented as Baseline evidence.

**Month attribution across execution delay.** A delayed execution attributed to a
prior calendar month MUST NOT consume the new calendar month's one-allocation
limit. A new calendar month MAY therefore independently generate a new allocation
while an earlier month's committed request is awaiting or completing execution
([Section 12](#12-allocation-commitment-and-budget-reservation)).

---

## 11. Budget accounting

The experiment MUST preserve economic fairness.

### 11.1 Annual grant and carry-forward

`[BASELINE — OD-10]`

- At the beginning of each calendar year, each Baseline strategy receives
  **12.0 new satellite units** (JPY 120,000).
- The full annual allocation becomes available **at once**. Units are **NOT**
  released monthly.
- Unused units from prior years carry forward, are added to the new annual
  allocation, and **do not expire**.
- Example: prior-year remainder 4.5 units + new annual allocation 12.0 units =
  **16.5 units** available.
- Strategies A, B, and C receive **identical annual funding capacity and
  identical funding timing**. Strategy rules determine only *when* available
  capital is deployed.
- Future-year allocations MUST NOT be borrowed.
- No carry-forward cap exists in the Baseline.

**First Full-History Baseline partial year `[BASELINE — OD-14]`**

OD-10 governs the beginning of each calendar year. OD-14 governs the single
Full-History Baseline start boundary, and the two rules are complementary:

| Case | Funding made available |
| ---- | ---------------------- |
| Normal subsequent calendar years | 12.0 new units at the beginning of the calendar year |
| First Full-History Baseline year, when measured performance begins after 1 January | 12.0 new units at the **simulation performance start**, without proration |

- If the approved Full-History Baseline performance start date
  ([Section 14.6](#146-baseline-period-and-dataset-cutoff)) falls after the
  beginning of a calendar year, the Baseline strategy receives the **full
  12.0-unit** annual satellite allocation for that starting calendar year at the
  simulation start.
- The first-year allocation MUST NOT be prorated by calendar months remaining,
  trading days remaining, fraction of the calendar year elapsed, or any other
  time-based accrual method.
- Strategies A, B, and C MUST receive the **same** 12.0-unit starting-year
  funding under this rule.
- Example: for an approved performance start of 2009-05-15, the starting-year
  allocation is **12.0 units** — not 8, not 7.5, and not any fraction-of-year
  amount.
- OD-14 does not permit borrowing future-year units and does not reset
  carry-forward units. It changes only the first-partial-year funding boundary.
- The fact that the first measured year is a partial calendar year MUST be
  explicitly reported with the Baseline result.

`[METHODOLOGY]` Budget state at the artificial start boundary of **rolling-window
experiments** is not defined by OD-10 or OD-14, and MUST be specified in the
rolling-window methodology before rolling-window results are produced. OD-14
applies **only** to the Full-History Baseline performance start boundary and MUST
NOT be applied as a rolling-window initialization rule.

### 11.2 Availability, capping, and economic value

- Executed and reserved units reduce available units.
- A strategy MUST NEVER commit more units than are currently available.
- If a Purchase Request exceeds available units, acceptance is capped at
  available units ([Section 12](#12-allocation-commitment-and-budget-reservation)).
- Cash corresponding to unused units remains part of total economic value and
  MUST NOT disappear from portfolio accounting.
- Fractional units are meaningful: 0.5-unit increments MAY carry forward.

### 11.3 Cash return assumption

`[BASELINE — OD-07]`

For the Baseline experiment, **unused satellite budget is zero-yield nominal JPY
cash**.

- Cash return = **0%**.
- Nominal JPY value remains unchanged until deployed.
- Unused cash remains part of total economic value.
- Unused cash MUST be included in terminal portfolio comparisons.
- Unused fractional units MAY carry forward; 0.5-unit increments therefore remain
  economically meaningful.
- Unused units do not expire.

`[DEFERRED — PHASE 4]` Interest-bearing cash, money-market returns, deposit
returns, and historical risk-free-rate proxies are **excluded from the Baseline**
and MAY be evaluated separately in Phase 4 — Sensitivity Analysis.

This resolves the former Open Question "Cash Return Assumption".

---

## 12. Allocation commitment and budget reservation

`[BASELINE — OD-13]`

This section fixes the boundary between **Signal**, **Purchase Request**,
**Budget Commitment**, and **Execution**.

### 12.1 When an allocation becomes committed

A satellite allocation becomes **committed** when a Purchase Request:

1. satisfies the applicable strategy rules,
2. satisfies the monthly-allocation constraint,
3. passes budget validation, and
4. is accepted for execution.

### 12.2 Effects at acceptance

At acceptance:

- Accepted units MUST be **reserved immediately**.
- Reserved units MUST be **removed immediately from available units**.
- The allocation MUST be attributed to the **calendar month in which the Purchase
  Request was accepted**.
- The allocation MUST be attributed to the **annual budget available at the time
  of acceptance**.

### 12.3 Execution timing

- Execution MAY occur in a later calendar month or later calendar year.
- A later execution MUST NOT change the original allocation month or budget year.
- Execution MUST NOT deduct the reserved units from available budget a second
  time.

### 12.4 Capping

If

```
requested units > currently available units
```

then

```
accepted units = currently available units
```

and only those accepted units are reserved.

Future-year budget MUST NOT be used later to increase a Purchase Request that was
capped because of insufficient prior-year budget.

### 12.5 Monthly exclusivity while pending

- Once an allocation has been committed for a calendar month, later Signals in
  that same calendar month MUST NOT create another Purchase Request.
- This holds while the original request is still pending execution.
- Stronger later Signals remain observable; their execution is suppressed with an
  explicit reason.
- A delayed execution attributed to a prior month MUST NOT consume the new
  calendar month's one-allocation limit.

### 12.6 Execution failure

`[METHODOLOGY]` Exact retry, cancellation, and reservation-release behavior
following execution failure is deferred to Execution Methodology.

**However, one requirement is fixed now:** failed or cancelled execution MUST NOT
cause reserved economic value to disappear from portfolio accounting.

### 12.7 `[METHODOLOGY]` Zero-unit acceptance semantics

OD-13 caps acceptance at available units, which permits an acceptance of
**0.0 units** when available units are zero. Whether a zero-unit acceptance
constitutes a "committed allocation" that consumes the calendar month's
one-allocation limit is not stated by OD-13.

This is recorded as an evidence-semantics question rather than an Owner Decision
because it is **outcome-neutral for units acquired**: available units can only
decrease within a calendar month under OD-10 (grants occur only at year start),
so any later request in the same month would also be capped to zero. It
nevertheless affects reason-code assignment and the counting of
`reserve exhaustion events` ([Section 13](#13-evaluation-metrics)), and MUST be
fixed in methodology review before those metrics are reported.

---

## 13. Evaluation metrics

`[BASELINE — OD-08]`

Baseline strategy superiority MUST NOT be determined from acquisition cost alone,
nor from any single efficiency metric.

### 13.1 Primary Baseline Metric

**Terminal Total Economic Value (TTEV)**, evaluated at a common comparison date:

```
TTEV = market value of acquired NASDAQ exposure
     + remaining unused satellite cash
```

The comparison date MUST be common to Strategies A, B, and C.

### 13.2 Required Secondary Metrics

| Metric |
| ------ |
| Total funding supplied |
| Total amount invested |
| Remaining cash |
| Units / shares acquired |
| Average acquisition cost |
| Number of purchases |
| Reserve utilization |
| Reserve exhaustion events |
| Maximum portfolio drawdown |
| Money-weighted return / XIRR |

### 13.3 Funding versus deployment

The following accounting distinction MUST be preserved, and MUST carry into the
XIRR methodology:

- The annual funding supplied to A, B, and C is **common external funding**.
- Movement from satellite cash into NASDAQ exposure is an **internal portfolio
  allocation**, not a new external contribution.

Treating internal deployment as an external cash flow would make the three
strategies non-comparable.

### 13.4 Rolling-window comparison

- Rolling-window comparison MUST later be used to evaluate regime dependence and
  robustness.
- Rolling-window analysis is **separate from** the Full-History Baseline
  ([Section 14.6](#146-baseline-period-and-dataset-cutoff)).
- `[METHODOLOGY]` Exact rolling-window lengths are **not** defined by OD-08.
- `[METHODOLOGY]` Rolling-window boundary-state initialization — including
  satellite budget state and Reference High state at the artificial window start
   — is **not** defined and MUST be specified before rolling-window results are
  produced.
- Window lengths MUST be fixed before results are inspected, consistent with
  Baseline Invariant 17.

### 13.5 Statistical claims

Statistical significance MUST NOT be claimed merely from overlapping rolling
windows, nor from a simple significance test applied without an appropriate
statistical methodology.

### 13.6 `[METHODOLOGY]` Remaining metric-definition work

OD-08 fixes the primary metric and the required secondary metric set. The
following formula details are delegated to methodology review, where they are not
already mathematically obvious:

- whether "average acquisition cost" is a simple or unit-weighted average
- the exact cash-flow convention for XIRR, consistent with
  [Section 13.3](#133-funding-versus-deployment)
- whether "maximum portfolio drawdown" is measured on invested assets or on total
  economic value
- how "reserve utilization" and "reserve exhaustion events" are counted, including
  the zero-unit-acceptance case in
  [Section 12.7](#127-methodology-zero-unit-acceptance-semantics)
- how an allocation that is **committed but not yet executed** at the common
  comparison date is treated in TTEV — specifically, whether its reserved amount
  is counted within "remaining unused satellite cash" (it has not yet been
  converted into exposure) or reported separately. Under
  [Section 12.6](#126-execution-failure) that value MUST NOT vanish from
  accounting; the presentation choice is a methodology matter.

All metric definitions MUST be fixed **before** results are inspected, consistent
with Baseline Invariant 17.

---

## 14. Data-source role separation and data requirements

The intended three-layer data concept is recorded below as **candidates**.

### 14.1 Primary long-history proxy candidate

- NASDAQ-100 Total Return in JPY

**Purpose:** long-history baseline simulation in the currency exposure closest to
the intended Japanese investor implementation.

### 14.2 Independent cross-validation candidate

- QQQ total-return series, combined with USD/JPY conversion where necessary

**Purpose:** test whether findings depend on a single index data source.

### 14.3 Live-product validation candidate

- Nissay NASDAQ100 Index Fund, restricted to its actual operating period

**Purpose:** compare proxy behavior with the actual intended investment product.

### 14.4 `[PHASE-1 EVIDENCE]` Approval status of data sources

**These sources are NOT approved.** Phase 1 MUST investigate, for each candidate:

- actual availability
- history length and coverage
- data quality, including gaps, revisions, and non-trading-day handling
- licensing
- redistribution rights
- total-return treatment, including distribution reinvestment assumptions
- currency treatment
- suitability as a proxy for the intended live product

This document asserts **no** dates, ticker availability, history lengths,
licensing conclusions, or suitability conclusions. Redistribution rights in
particular MUST be established before any raw data is committed to this public
repository.

`[PHASE-1 EVIDENCE]` If a proxy requires currency conversion, the conversion
convention — rate source, observation time, and alignment with the index
observation date — MUST be established in Phase 1 and MUST be consistent with the
single-series requirement in [Section 7](#7-drawdown-reference-high).

### 14.5 Cost and expense treatment

`[BASELINE — OD-11, principle approved]`

Transaction costs, fund expenses, and tracking effects MUST NOT be silently
ignored or double-counted.

- When actual Nissay NASDAQ100 Index Fund NAV data are used, costs already
  reflected in the published NAV MUST NOT be deducted again.
- When an index, ETF, or synthetic proxy is used, Phase 1 MUST document which
  return components and expenses are already embedded in the series, and
  additional adjustments MUST NOT be applied until that is understood.
- Tracking difference MUST NOT be assumed to equal the stated fund expense ratio.
- Any cost model applied to proxy data MUST be explicit, reproducible,
  evidence-based, and distinguishable from the raw proxy return.
- If the evidence does not support a defensible historical product-cost
  reconstruction, the research MAY report an unadjusted proxy result **and** a
  separately identified cost-adjusted scenario, rather than inventing false
  precision.

`[PHASE-1 EVIDENCE]` Exact expense rates and proxy-adjustment methodology are
delegated to Phase 1 — Data Foundation.

### 14.6 Baseline period and dataset cutoff

`[BASELINE — OD-12, principle approved]`

- The Baseline Full-History Backtest MUST use the **longest defensible continuous
  history** available from the Phase-1-approved Primary Proxy, subject to the
  experiment's data and methodology requirements.
- The exact Baseline start date MUST be justified by data availability and
  methodology, and MUST NOT be selected after inspecting strategy performance.
- Historical observations preceding the measured performance start MAY be used
  **only** to initialize approved historical state such as the Daily Closing ATH.
  Such observations are **warm-up data** and MUST NOT be included in measured
  Baseline performance.
- Phase 1 MUST establish a fixed **Baseline Dataset Cutoff**.
- Once frozen, the original Baseline result MUST remain reproducible against that
  cutoff. Newer market observations MUST NOT silently alter the original
  Baseline.
- Later data MAY be evaluated separately as extended evidence or out-of-sample
  evidence, clearly labelled as such.
- Rolling-window analysis is separate from the Full-History Baseline.

`[PHASE-1 EVIDENCE]` The approved Primary Proxy, the exact Baseline start date,
and the Baseline Dataset Cutoff are Phase-1 deliverables. If the approved start
date is not a calendar-year boundary, first-year funding is already fixed by
OD-14 ([Section 11.1](#111-annual-grant-and-carry-forward)) and requires no
further Owner Decision.

---

## 15. Scope boundary

The initial deterministic backtest focuses **only** on the NASDAQ satellite
allocation question.

The first backtest MUST NOT be required to simulate:

- Sony Life contract mechanics
- the full NISA core portfolio
- Japanese tax calculations
- the full histories of all core funds

Those belong to a later portfolio-level integration, and only if the satellite
hypothesis survives baseline testing.

**The initial causal question is:**

> Given the same annual NASDAQ satellite funding capacity, how do Strategies A, B,
> and C differ?

---

## 16. No optimization before baseline evidence

- The Baseline threshold parameters are **-10% / -20%**.
- The Baseline sizing parameters are **0.5 / 1.0 / 2.0 units**, with 0.5 units
  used only by Strategy C as the Month-End Fallback (OD-09).
- The Baseline annual satellite budget is **JPY 120,000 / year**.
- These are tested **first**.
- They MUST NOT be tuned after inspecting results and then presented as Baseline
  evidence.
- Sensitivity analysis belongs to **Phase 4**.
- Alternative candidates MAY be explored only after Baseline evidence is
  recorded, and MUST be reported separately from the pre-specified Baseline.

`[DEFERRED — PHASE 4]` Illustrative examples of what Phase 4 *might* examine.
These are examples only, and are **not** evaluated, endorsed, or scheduled here:

- alternative drawdown thresholds, such as -5% / -15% or -15% / -25%
- alternative sizing ratios, such as 0 / 1 / 2 or 0.5 / 1 / 3
- same-month escalation variants (excluded from the Baseline by OD-06)
- non-zero cash return assumptions (excluded from the Baseline by OD-07)
- alternative annual satellite budgets, such as JPY 60k / 120k / 180k / 240k
- alternative Reference High definitions (the Baseline is fixed by OD-02)

---

## 17. Baseline invariants

These invariants consolidate the approved Decisions. Any implementation, and any
future revision of this document, MUST satisfy all of them.

| # | Invariant |
| - | --------- |
| 1 | No future information may influence a decision. |
| 2 | A confirmed daily close used to generate a Signal cannot also be used as a retrospective execution price for that Signal. |
| 3 | All Baseline strategies receive identical annual external funding capacity. |
| 4 | Each calendar year adds exactly 12.0 new satellite units. |
| 5 | Future-year units cannot be borrowed. |
| 6 | Unused units carry forward without expiration. |
| 7 | Unused satellite cash remains economic value. |
| 8 | Baseline cash return is 0%. |
| 9 | Strategies B and C may commit at most one satellite allocation per calendar month. |
| 10 | A committed allocation reserves its budget immediately. |
| 11 | Execution cannot deduct already-reserved budget a second time. |
| 12 | Execution delay cannot change the allocation's original calendar month or budget year. |
| 13 | Strategy B does not purchase in the High zone. |
| 14 | Strategy C uses 0.5 unit only as Month-End Fallback when no Daily Trigger has committed that month's allocation. |
| 15 | Same-month escalation is excluded from the Baseline. |
| 16 | Negative or hypothesis-rejecting results remain valid evidence. |
| 17 | Baseline parameters must not be retroactively optimized after results are observed and then presented as pre-specified Baseline evidence. |
| 18 | If the Full-History Baseline performance start falls after 1 January, that first calendar year's full 12.0 units become available at the simulation performance start, without proration, identically for A, B, and C; the partial first measured year must be reported with the Baseline result. |

Invariant 9 is stated for Strategies B and C as approved. Strategy A is
structurally limited to one decision per calendar month by OD-01, and is subject
to the same commitment and reservation rules
([Section 12](#12-allocation-commitment-and-budget-reservation)).

---

## 18. Baseline Freeze Gate

**Current status: Frozen — Owner Approved.**

### 18.1 Gate conditions — all completed

| Item | Status |
| ---- | ------ |
| README entry document reviewed | Completed |
| OD-01 through OD-14 | APPROVED |
| Cross-Decision Consistency Review | Completed |
| Cross-Decision Review result | **PASS** — no unresolved cross-decision inconsistency identified after OD-13 |
| Independent Owner Review of OD-01 through OD-13 | **PASS WITH ONE ADDITIONAL OWNER DECISION** |
| Final strategy-rule issue from that review (first partial-year funding) | Resolved by **OD-14** |
| Owner review of the OD-14 revision of `docs/experiment_spec.md` | Completed — APPROVED |
| Confirmation that all approved Decisions are represented correctly | Completed |
| Confirmation that no unresolved strategy-rule Owner Decision remains | Completed — see [Section 19](#19-open-items-register) |
| Explicit Owner approval to mark the Baseline specification **Frozen** | **Granted** |

### 18.2 Effect of the Freeze

- The strategy rules in Sections 3 through 17 are **pre-specified and frozen**,
  established before any repository-implemented deterministic Baseline backtest
  was run and before any reproducible Baseline performance result existed.
  Exploratory pre-repository analysis informed the experiment design but is not
  Baseline evidence.
- This document is the **normative Baseline**. The decision-history artifact
  `docs/decisions/phase0_baseline_decisions.md` records reasoning only and does
  not govern Baseline behavior.
- Any later change to thresholds, sizing, cash assumptions, escalation behavior,
  annual budget, or the Reference High definition MUST be either a new,
  explicitly versioned Baseline created under research governance, or
  sensitivity analysis reported separately. It MUST NOT be applied as a silent
  edit to this Frozen Baseline.
- Frozen means *pre-specified*. It does **not** mean validated, and it does
  **not** mean approved for live investment use
  ([Section 15](#15-scope-boundary)).

### 18.3 Relationship to Phase 1 and Phase 2

Phase-1 evidence requirements did **not** need to be fabricated or prematurely
resolved in order to freeze the **strategy specification**, and freezing did not
resolve them.

Every Phase-1 item required for a valid deterministic backtest remains a **hard
gate before Phase 2 implementation**. Specifically, Phase 2 MUST NOT begin until
the items in [Section 19.1](#191-phase-1-blocking-evidence-requirements) are
resolved with evidence, and the methodology items in
[Section 19.2](#192-methodology-requirements-before-implementation) are fixed
before the metrics they govern are reported.

Until those gates are cleared:

- No backtest code is written.
- No methodology code is written.
- No data loaders are written.
- No Baseline results exist, and none may be cited.

Neither this Freeze nor any later revision may be applied by anyone other than
the Owner.

---

## 19. Open items register

The former Open Questions table is superseded. OD-01 through OD-14 resolved every
previously listed blocking Owner Decision, and OD-14 resolved the former
conditional item C-1. **No unresolved Owner Decision remains.** The items below
are Phase-1 evidence requirements, methodology requirements, and deferred
sensitivity questions — not unresolved Owner Decisions.

### 19.1 Phase-1 Blocking Evidence Requirements

Blocking for **Phase 2 implementation**, not for Baseline Freeze.

| # | Requirement | Source |
| - | ----------- | ------ |
| P1-1 | Exact signal → order → execution date → applicable NAV mapping for the Nissay NASDAQ100 Index Fund, including order cutoff, NAV determination timing, JST/U.S. session relationship, holidays, and historical reproducibility | OD-04, [9.1](#91-phase-1-evidence-signal-to-order-to-nav-mapping) |
| P1-2 | Approved Primary Proxy | OD-12, [14.1](#141-primary-long-history-proxy-candidate), [14.4](#144-phase-1-evidence-approval-status-of-data-sources) |
| P1-3 | Proxy return composition, including total-return and distribution-reinvestment treatment | OD-11, [14.4](#144-phase-1-evidence-approval-status-of-data-sources) |
| P1-4 | Cost / expense treatment supported by evidence, without double-counting or assumed tracking difference | OD-11, [14.5](#145-cost-and-expense-treatment) |
| P1-5 | Exact Baseline start date, justified from approved data and not from performance inspection | OD-12, [14.6](#146-baseline-period-and-dataset-cutoff) |
| P1-6 | Fixed Baseline Dataset Cutoff | OD-12, [14.6](#146-baseline-period-and-dataset-cutoff) |
| P1-7 | Currency treatment where a proxy requires conversion | OD-12, [14.4](#144-phase-1-evidence-approval-status-of-data-sources) |
| P1-8 | Data licensing and redistribution constraints, established before any raw data is committed | [14.4](#144-phase-1-evidence-approval-status-of-data-sources) |
| P1-9 | Data revision / restatement behavior of the approved sources, and its look-ahead implications | [6](#6-look-ahead-prohibition) |

### 19.2 Methodology Requirements before implementation

| # | Requirement | Source |
| - | ----------- | ------ |
| M-1 | Exact formulas for Secondary Metrics where not mathematically obvious | OD-08, [13.6](#136-methodology-remaining-metric-definition-work) |
| M-2 | Rolling-window lengths | OD-08, [13.4](#134-rolling-window-comparison) |
| M-3 | Rolling-window boundary-state initialization, including satellite budget state and Reference High state | OD-10, OD-12, [13.4](#134-rolling-window-comparison) |
| M-4 | Execution-failure retry / cancellation / reservation-release semantics, subject to the fixed requirement that reserved economic value must not disappear | OD-13, [12.6](#126-execution-failure) |
| M-5 | Treatment in TTEV of an allocation committed but not yet executed at the common comparison date | OD-08, OD-13, [13.6](#136-methodology-remaining-metric-definition-work) |
| M-6 | Zero-unit-acceptance semantics and their effect on reason codes and reserve-exhaustion counting | OD-13, [12.7](#127-methodology-zero-unit-acceptance-semantics) |
| M-7 | Numeric comparison tolerance and rounding at the `-10.0%` / `-20.0%` boundaries, without altering the fixed boundary semantics | OD-02, [4.0](#40-drawdown-zone-semantics) |
| M-8 | Statistical methodology, if any statistical claim is to be made at all | OD-08, [13.5](#135-statistical-claims) |

### 19.3 Deferred Sensitivity Questions — Phase 4

| # | Question |
| - | -------- |
| S-1 | Alternative drawdown thresholds |
| S-2 | Alternative sizing ratios |
| S-3 | Same-month escalation variants |
| S-4 | Non-zero cash return assumptions |
| S-5 | Alternative annual satellite budgets |
| S-6 | Alternative Reference High definitions |

### 19.4 Conditional Owner Decision items

**None.**

The previously recorded conditional item C-1 — the size of the first partial
year's unit grant when the approved Baseline performance start is not a
calendar-year boundary — is **resolved by OD-14** and is specified in
[Section 11.1](#111-annual-grant-and-carry-forward). It is no longer an open or
conditional Owner Decision.

No remaining item in this register is resolved by this document.

---

## 20. Revision notes

### 20.0 Phase 0 Baseline Freeze (current)

A status transition only. The Owner explicitly approved the Phase 0 Baseline
Freeze; the document status changed from *Draft — Not Frozen* to
**Frozen — Owner Approved**, the Freeze statement was added to the header, and
[Section 18](#18-baseline-freeze-gate) was updated to show the gate conditions as
completed. **No strategy rule, threshold, unit size, funding rule, timing rule,
metric definition, or delegated requirement was changed.** The Phase-1 evidence
requirements, methodology requirements, and Phase-4 deferred sensitivity
questions in [Section 19](#19-open-items-register) are unchanged and remain open.

### 20.1 OD-14 revision

A minimal-diff revision incorporating OD-14 only. It added OD-14 to the
[Owner Decision register](#01-owner-decision-register), specified the
first-partial-year funding rule in
[Section 11.1](#111-annual-grant-and-carry-forward), added
[Baseline Invariant 18](#17-baseline-invariants), updated the
[Baseline Freeze Gate](#18-baseline-freeze-gate) status, and closed the former conditional
item C-1 in [Section 19.4](#194-conditional-owner-decision-items). OD-01 through
OD-13 semantics were not changed. OD-14 is additive and applies only to the
Full-History Baseline start boundary; it is not a rolling-window initialization
rule, not an accrual rule, and does not affect borrowing or carry-forward.

### 20.2 OD-01 through OD-13 revision

That revision:

- resolved and removed the former blocking Open Questions OQ-1 through OQ-12,
  each of which is now fixed by an approved Owner Decision or explicitly
  delegated;
- added the [state model](#3-state-model), the
  [allocation commitment and reservation section](#12-allocation-commitment-and-budget-reservation),
  the [consolidated strategy matrix](#44-consolidated-baseline-strategy-matrix),
  and the [Baseline invariants](#17-baseline-invariants);
- replaced the Open Questions table with the
  [Open items register](#19-open-items-register), classified by owner of the
  remaining work;
- removed superseded ambiguity, in particular the former "0.5 units in the High
  zone" reading of Strategy B, which OD-09 excludes.

One non-contradictory subsumption is recorded for transparency: under OD-05's
processing order, Strategy C's Month-End Fallback row for
`-20% < DD <= -10%` is unreachable, because the Daily Drawdown Trigger is
evaluated first on the same trading day and requests 1.0 unit. The resulting
allocation is identical under either reading, so this is a simplification rather
than a behavioral change. It is stated explicitly in
[Section 4.3](#43-strategy-c--daily-drawdown-trigger--month-end-fallback).

---

**End of specification. Status: Frozen — Owner Approved.**
