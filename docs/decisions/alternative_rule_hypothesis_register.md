# Pre-Phase-2 Alternative Rule Hypothesis Register

**Status:** Open register

**Scope:** Cross-phase — pre-registration of alternative strategy-rule hypotheses

**Register created:** 2026-08-11

---

## 1. Register role and precedence

*This section governs how every entry in this register must be read. It is stated before the
first entry deliberately.*

### 1.1 Purpose

This register preserves **alternative strategy-rule hypotheses** that were proposed **before**
any Phase-2 backtest result existed, together with their provenance, so that a future reader can
verify that a rule idea was not selected with knowledge of results.

Its purpose is **anti-hindsight recording**. It exists because
[`../experiment_spec.md`](../experiment_spec.md) Baseline Invariant 17 prohibits retroactively
optimizing Baseline parameters after results are observed and then presenting them as
pre-specified Baseline evidence. Recording a hypothesis with a verifiable date is the mechanism
by which a later evaluation can demonstrate that it was pre-registered rather than back-fitted.

### 1.2 This register is not a specification

> **This register is NOT a strategy specification, and MUST NOT become one.**

- It does **not** define, and must never be read as defining, how any strategy behaves.
- Nothing in it is normative for any backtest, any implementation, or any result.
- It records **hypotheses and their provenance only**.
- An entry describes a *conceptual proposal*. It is not an executable specification, and an
  entry must not be converted into one by being read as if it were complete.
- No implementation may take a rule from this register. Authorization to implement or evaluate
  anything recorded here would require a separate Owner Decision that does not exist.

### 1.3 Artifact role and precedence

Entries in this register are **Pre-Phase-2 Alternative Rule Hypotheses**. They are a distinct
artifact class from Evidence Artifacts and from Owner Decisions.

> **A register entry is NOT a modification of the Phase-0 Baseline.**

- An entry is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and does
  not create, amend, or supersede any of them.
- The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where an
  entry and that specification could be read as differing, **the specification governs Baseline
  behavior**.
- The Phase-0 decision history remains
  [`phase0_baseline_decisions.md`](phase0_baseline_decisions.md) and is unchanged.
- An entry records a **proposal**. It contains no results, no performance claims, and no
  empirical evaluation, and none may be added to it later. Any future empirical work on a
  registered hypothesis belongs in its own separately reviewed artifact.
- An entry authorizes nothing. See each entry's non-authorization section.

### 1.4 Identifier namespace

Entries are identified as **`AR-nn`** (Alternative Rule). This series is deliberately distinct
from every existing identifier series in the repository — `OD-nn` (Frozen Phase-0 Owner
Decisions), `P1-n` (Phase-1 blocking evidence requirements), `M-n` (methodology requirements),
`S-n` (Phase-4 deferred sensitivity questions) — so that an `AR-nn` reference can never be
mistaken for a Baseline decision.

An `AR-nn` identifier is **stable and carries the entry's provenance**. The descriptive name
attached to an entry is prose only, is non-normative, and may be changed later **without
changing the identity or provenance of the entry**.

Open semantic questions within an entry are identified as **`E-n`**, scoped to that entry.

### 1.5 What registration does and does not do

| Registration **does** | Registration **does NOT** |
| --------------------- | ------------------------- |
| Record that a hypothesis existed, and when | Adopt it |
| Record its semantics as stated by the proposer | Approve it as a strategy rule |
| Record which questions about it remain unresolved | Resolve those questions |
| Record its relationship to the Frozen Baseline | Modify the Frozen Baseline |
| Preserve provenance for later anti-hindsight verification | Authorize implementation, backtesting, or evaluation |
| Provide a citable, stable identifier for future work | Assert that the hypothesis is superior, equivalent, or inferior to any other rule |

### 1.6 Register index

| ID | Descriptive name (non-normative) | Proposed | Proposer | Status |
| -- | -------------------------------- | -------- | -------- | ------ |
| [AR-01](#ar-01--monthly-cumulative-allocation-cap) | Monthly Cumulative Allocation Cap | 2026-08-11 | Owner | **RECORDED — NOT ADOPTED** |

---

# AR-01 — Monthly Cumulative Allocation Cap

## AR-01.1 Status and classification

| Field | Value |
| ----- | ----- |
| Entry ID | **AR-01** — the stable identifier |
| Artifact class | **Pre-Phase-2 Alternative Rule Hypothesis** |
| Descriptive name | **Monthly Cumulative Allocation Cap** — provisional, descriptive, and **non-normative**; may be renamed later without changing the identity or provenance of AR-01 |
| Status | **RECORDED — NOT ADOPTED, NOT VALIDATED, NOT AUTHORIZED FOR IMPLEMENTATION** |
| Executable status | **NOT EXECUTABLE AS STATED** — see [AR-01.7](#ar-017--unresolved-semantics--recorded-as-open), in particular **E-1** and **E-10** |
| Proposal date | **2026-08-11** |
| Proposer | **Owner** |
| Phase-0 Baseline status | **Frozen — Owner Approved. Unchanged by this entry** |
| OD-01 … OD-14 | **Unchanged. This entry is not part of that series** |
| Empirical status | **NONE. No backtest has been run, under this rule or any other, in this repository** |
| Phase 2 | **BLOCKED — unchanged by this entry** |
| P1-1 … P1-9 | **Unchanged by this entry** |
| M-1 … M-8 | **Unchanged by this entry** |

**This entry is explicitly NOT:**

- part of Phase-0 Baseline v1;
- a Baseline amendment;
- an Owner-approved strategy rule;
- an implementation authorization;
- a Phase-2 experiment authorization;
- an empirically validated finding;
- evidence that the proposed rule is superior to the Frozen Baseline, or to anything else.

## AR-01.2 Provenance and anti-hindsight statement

> **This hypothesis was proposed by the Owner on 2026-08-11, before Phase-2 backtesting and
> before any performance comparison of this alternative existed.**

At the moment of proposal, and at the moment of this recording:

- **no deterministic Baseline backtest had been implemented or run in this repository**, and no
  reproducible Baseline performance result existed;
- **Phase 2 was BLOCKED**, with all nine Phase-1 blocking evidence requirements in
  [`../experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements)
  unresolved, no Primary Proxy approved (P1-2 OPEN), no Baseline start date chosen (P1-5 OPEN),
  and no Baseline Dataset Cutoff fixed (P1-6 OPEN);
- **no strategy-performance comparison under this or any alternative rule had been performed,
  observed, or inspected** — including no count of historical occurrences of the condition the
  rule describes, and no examination of any historical period in which such a condition might
  have arisen;
- **no backtest code, methodology code, or data loader existed**, consistent with
  [`../experiment_spec.md` §18.3](../experiment_spec.md#183-relationship-to-phase-1-and-phase-2).

**The purpose of recording the hypothesis now is to prevent future hindsight-driven or
performance-driven rule selection.** Any future evaluation of AR-01 must cite this recording
date, and any result must be reported separately from — and never as — Frozen-Baseline evidence.

The repository must remain able to distinguish, permanently:

| | |
| --- | --- |
| **A** | the **Frozen Phase-0 Baseline**, pre-specified and frozen before any repository-implemented Baseline backtest was run |
| **B** | a **pre-Phase-2 alternative hypothesis**, recorded before any Phase-2 result existed |

**The existence of B does not alter A.**

## AR-01.3 The hypothesis as proposed — conceptual layer

### AR-01.3.1 Two layers, kept strictly separate

This entry records **one** of the following two layers, and deliberately not the other:

| Layer | Content | Recorded here? |
| ----- | ------- | -------------- |
| **1 — Conceptual hypothesis** | What the proposer intends the rule to mean | **Yes** — AR-01.3.2 to AR-01.5 |
| **2 — Executable semantics** | The determinations required before the rule could be implemented unambiguously | **No** — recorded as *open questions* in [AR-01.7](#ar-017--unresolved-semantics--recorded-as-open) |

> **This entry records Layer 1 only. It does not convert the conceptual hypothesis into an
> executable specification, and it must not be read as one.**

### AR-01.3.2 Statement of the concept, as the proposer stated it

> **Within a calendar month, the currently applicable drawdown zone determines the maximum
> cumulative allocation entitlement for that month. Purchases already executed during the same
> calendar month count toward that entitlement.**

Therefore:

```
additional allocation
=
max(
    0,
    allocation entitlement of the currently applicable zone
    - allocation already executed in the current calendar month
)
```

### AR-01.3.3 The proposer's neutral restatement of the same concept

The proposer additionally expressed the intent in terms that do not commit to any
implementation concept:

```
additional allocation
=
max(
    0,
    current applicable monthly entitlement
    - allocation already counted toward that month
)
```

> **Wording note — binding.** The phrase **"allocation already executed"** in AR-01.3.2 is
> preserved exactly as the proposer stated it. It is **NOT** replaced here with "committed",
> "reserved", "accepted", or any other implementation concept. That phrase conflicts with the
> Frozen Baseline's delayed-execution state model, and the conflict is recorded as unresolved
> open questions **E-1** and **E-10** rather than being silently resolved in either direction.
>
> AR-01.3.3 records the proposer's neutral phrasing as an expression of *intent*. It is **not**
> a resolution of E-1 or E-10, and must not be cited as one.

### AR-01.3.4 The intended conceptual distinction — binding on how this entry is read

> **This is NOT permission to purchase repeatedly whenever a threshold is crossed.**
>
> It is: *the currently applicable drawdown zone determines the maximum cumulative allocation
> entitlement for the calendar month, and only the unfilled portion of that entitlement may
> become additional allocation.*

The distinction is material, because at least two structurally different rules could be
described loosely as "same-month escalation", and they do not behave identically:

| Variant | On a shallower trigger followed by a deeper trigger in one calendar month | Monthly total |
| ------- | ------------------------------------------------------------------------ | ------------- |
| Unbounded re-fire — each qualifying trigger generates a full new Purchase Request | the shallower allocation, then a further full deeper allocation | **3.0 units** |
| **AR-01 — bounded cumulative entitlement** | the shallower allocation, then a top-up to the deeper zone's cumulative entitlement | **2.0 units** |

**AR-01 is the second of these.** It is a *bounded* variant.

The unit sizes referenced above are the Frozen Baseline's own sizing parameters
([`../experiment_spec.md` §4.2](../experiment_spec.md#42-strategy-b--daily-drawdown-trigger),
[§4.3](../experiment_spec.md#43-strategy-c--daily-drawdown-trigger--month-end-fallback)),
carried over unchanged by the hypothesis. AR-01 proposes no change to thresholds or sizing.

## AR-01.4 Worked conceptual example

Illustrative only. This is a statement of the proposed rule's arithmetic — **not** a historical
observation, not a simulation, and not a claim that any such sequence has occurred.

| Point in a single calendar month | Applicable zone entitlement | Already allocated this month | Additional allocation |
| -------------------------------- | --------------------------- | ---------------------------- | --------------------- |
| A 10% drawdown zone becomes applicable | 1 unit | 0 | **1 unit** |
| Later in the **same** calendar month, the 20% drawdown zone becomes applicable | 2 units (cumulative) | 1 unit | **1 unit** |
| Later still, while the maximum applicable entitlement remains 2 units | 2 units (cumulative) | 2 units | **0** |

Expressed against the proposed formula:

```
10% zone:   entitlement = 1,  already executed = 0,  additional purchase = 1
20% zone:   entitlement = 2,  already executed = 1,  additional purchase = 1
thereafter: entitlement = 2,  already executed = 2,  additional purchase = 0
```

## AR-01.5 Motivation — the proposed path-dependency question

**Recorded as the proposer's motivation. It is a hypothesis, not a finding, and no part of it is
asserted here to be correct.**

The Owner identified a possible path dependency. Under a strict one-allocation-per-calendar-month
interpretation, two market paths may produce different monthly allocations:

| Path | Sequence within one calendar month | Monthly allocation |
| ---- | ---------------------------------- | ------------------ |
| **A** | the market reaches the deeper drawdown zone directly | the deeper-zone allocation may be executed |
| **B** | the market first reaches a shallower zone, that allocation is executed, and the market later reaches the deeper zone in the same month | the deeper-zone allocation may no longer be executable |

AR-01 proposes to remove or reduce that path dependence by treating the deeper-zone allocation
as a **cumulative monthly entitlement** rather than an entirely separate purchase opportunity.

> **No claim is made that this is an improvement.**
>
> **Nor is the Frozen Baseline's behavior characterized here as a bug, a defect, an oversight,
> or an ambiguity requiring correction.** The repository evidence shows the opposite: same-month
> escalation was **deliberately excluded**, and the shallower-then-deeper scenario was
> **explicitly considered** and its outcome stated (see AR-01.6.2). AR-01 is an **alternative
> design hypothesis to that deliberate Baseline choice**.
>
> Whether path dependence of this kind is an acceptable consequence or a property worth changing
> is **not decided by this entry**.

## AR-01.6 Relationship to the Frozen Phase-0 Baseline

### AR-01.6.1 Non-impact statement

> **The Frozen Phase-0 Baseline is unchanged by this entry.**

- [`../experiment_spec.md`](../experiment_spec.md) is **not modified** by this entry, and
  remains the normative Baseline.
- [`phase0_baseline_decisions.md`](phase0_baseline_decisions.md) is **not modified**.
- **OD-01 through OD-14 are unchanged**, in substance and in wording.
- **No Baseline Invariant is changed.**
- No Phase-1 Evidence Artifact and no Phase-1 Owner Decision is modified by this entry.
- No Phase-1 requirement status (P1-1 … P1-9) and no methodology requirement (M-1 … M-8) is
  changed or resolved.

### AR-01.6.2 AR-01 contradicts the Baseline's operative same-month escalation rule

Recorded plainly, so that the relationship is visible rather than latent.

AR-01 **contradicts** the following operative Frozen provisions. It is therefore an
**alternative to** them, and **cannot be treated as a clarification, refinement, or
interpretation of the Frozen Baseline**:

| Frozen provision | Position |
| ---------------- | -------- |
| [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) (OD-01, OD-06, OD-13) | "Baseline Strategies A, B, and C permit **at most one committed satellite allocation per calendar month**"; "Once an allocation has been committed for a calendar month, no later Signal in that same calendar month MAY generate an additional Purchase Request"; "This remains true even if the later Signal belongs to a **stronger** drawdown tier" |
| [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) worked example (OD-06) | A shallower trigger commits its allocation; a deeper condition later in the same month is "observed and recorded; **no** additional allocation" |
| [§4.4](../experiment_spec.md#44-consolidated-baseline-strategy-matrix) | "Same-month escalation after commitment — Not permitted" for Strategies B and C |
| [§17](../experiment_spec.md#17-baseline-invariants) Invariant 15 | "Same-month escalation is excluded from the Baseline" |

The Frozen Baseline states the purpose of that exclusion: to "prevent repeated firing during
extended drawdown conditions from turning a strategy into uncontrolled repeated buying"
([§10](../experiment_spec.md#10-one-allocation-per-calendar-month)).

> **The Frozen Baseline's treatment of this scenario is explicit and deliberate.** The scenario
> AR-01 addresses was considered and decided under OD-06, with a worked example and a stated
> rationale. AR-01 proposes an alternative to that deliberate design choice; it does not fill a
> gap, and it identifies no error.

### AR-01.6.3 The slot the Frozen Baseline already reserves

The Frozen Baseline anticipated that a variant of this kind might be studied later, and reserved
a place for it **without** approving any particular variant:

- [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) `[DEFERRED — PHASE 4]`:
  "Same-month escalation is **not** part of the Baseline. An escalation variant MAY be studied
  in Phase 4 — Sensitivity Analysis, but MUST NOT be retroactively presented as Baseline
  evidence."
- [§16](../experiment_spec.md#16-no-optimization-before-baseline-evidence) lists "same-month
  escalation variants (excluded from the Baseline by OD-06)" among illustrative Phase-4
  examples, explicitly "not evaluated, endorsed, or scheduled".
- [§19.3](../experiment_spec.md#193-deferred-sensitivity-questions--phase-4) records deferred
  sensitivity question **S-3 — Same-month escalation variants**.

**AR-01 is a specific, bounded instance of the class that S-3 names.** This entry references
S-3; it does **not** modify, expand, or resolve it, and the Frozen register is untouched.

### AR-01.6.4 How AR-01 could ever be applied

[`../experiment_spec.md` §18.2](../experiment_spec.md#182-effect-of-the-freeze) already governs
this, and this entry adds nothing to it. Any change to escalation behavior "MUST be either a
new, explicitly versioned Baseline created under research governance, or sensitivity analysis
reported separately. It MUST NOT be applied as a silent edit to this Frozen Baseline."

Recording AR-01 is neither of those two routes. It is weaker than both: it is a dated record
that an idea exists.

## AR-01.7 Unresolved semantics — recorded as OPEN

**These questions are recorded as OPEN and are deliberately left unresolved.** Answering them
would be inventing rules the proposer has not specified, contrary to the discipline stated in
[`../experiment_spec.md` §0](../experiment_spec.md#0-how-to-read-this-document): "Where a
decision has not been made, this document states that it has not been made. It does not fill the
gap with a plausible default."

### AR-01.7.1 Blocking issues — AR-01 is not executable as stated

> ### ⚠ E-1 and E-10 are BLOCKING
>
> **AR-01 is NOT an executable specification.** Two of the open questions below are not
> refinements but **blocking semantic issues**, and the rule cannot be expressed unambiguously —
> in prose or in code — until the Owner resolves them:
>
> - **E-1 — what "allocation already executed" means.** Read literally against the Frozen
>   delayed-execution state model, an earlier same-month allocation might not yet be *executed*
>   at the time of a later deeper trigger, so the full deeper entitlement would be granted and
>   the monthly total would exceed the cumulative cap the hypothesis itself intends.
> - **E-10 — whether the monthly counter is attributed by allocation month or by execution
>   date.** If measured by execution date, an allocation committed in one calendar month and
>   executed in the next would consume the later month's entitlement.
>
> **Both are recorded as open. Neither is resolved here, and neither may be resolved by
> inference from this entry.**

### AR-01.7.2 The open questions

| # | Open question | Why it is open |
| - | -------------- | -------------- |
| **E-1** ⚠ | **What exactly constitutes "allocation already executed"?** | The Frozen [state model](../experiment_spec.md#3-state-model) separates Signal → Purchase Request → Budget Validation → **Allocation Commitment / Unit Reservation** → Execution Pending → **Execution**. Under [§12.2](../experiment_spec.md#122-effects-at-acceptance) units are reserved at acceptance; under [§12.3](../experiment_spec.md#123-execution-timing) execution "MAY occur in a later calendar month or later calendar year". Because the intended live target is a Japanese mutual fund whose applicable NAV is not observable at order time ([§3](../experiment_spec.md#3-state-model)), execution lags the decision date. Candidate readings: **(a)** committed / reserved units; **(b)** executed units; **(c)** accepted-after-capping units. **Not decided here — see AR-01.7.1.** |
| **E-2** | **Does reserved-or-committed-but-not-yet-executed allocation count toward the entitlement?** | Direct corollary of E-1. Committed units are the only quantity knowable at a later decision date without look-ahead, but the hypothesis as stated says "executed". **Not decided here.** |
| **E-3** | **Treatment of failed or delayed execution.** | [§12.6](../experiment_spec.md#126-execution-failure) defers retry, cancellation, and reservation-release semantics to methodology requirement **M-4**, which is unresolved, fixing only that reserved economic value must not disappear. If a commitment later fails or is cancelled, does the monthly filled amount decrease and re-open entitlement headroom? **Not decided here**, and it cannot be closed before M-4 is. |
| **E-4** | **May entitlement only increase, or can it decrease?** | The hypothesis says the **currently applicable** zone determines entitlement, which reads as instantaneous. Candidate readings: **(a)** current-zone; **(b)** month-to-date high-water (the deepest zone reached so far in the month); **(c)** re-evaluated only when a trigger fires. **Not decided here.** |
| **E-5** | **Behaviour on deep → shallow → deep movement within one calendar month.** | Related to E-4. The `max(0, ·)` floor prevents a negative allocation, but the semantics of a cap that has fallen below what is already allocated are undefined, and the Frozen Baseline contains no sell, unwind, or reversal logic anywhere. Whether the entitlement is fill-only and never unwound is **not decided here**. A related edge case: the Reference High may rise within a month ([§7](../experiment_spec.md#7-drawdown-reference-high) — a new Daily Closing ATH gives `DD = 0%`), so the applicable zone can change through recovery rather than through any allocation event. |
| **E-6** | **Interaction with the existing one-allocation-per-calendar-month rule.** | AR-01 necessarily replaces [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) / OD-06 / Invariant 15 for any strategy adopting it. **How** the replacement is modelled is open: as a **second committed allocation** in the same month (which would contradict Invariant 9's count and change the meaning of "number of purchases" in [§13.2](../experiment_spec.md#132-required-secondary-metrics)), or as an **upward revision of the same monthly allocation** (which would preserve the count but conflict with [§12.2](../experiment_spec.md#122-effects-at-acceptance) and [§12.4](../experiment_spec.md#124-capping), both written for a single acceptance event). **Not decided here.** |
| **E-7** | **Commitment and reservation accounting.** | Each top-up would be an acceptance subject to [§12.4](../experiment_spec.md#124-capping) capping against currently available units. Whether an entitlement that cannot be filled for lack of budget is recorded as an unfilled-entitlement event, and whether it counts toward "reserve exhaustion events" ([§13.2](../experiment_spec.md#132-required-secondary-metrics)), is **not decided here**. |
| **E-8** | **Interaction with annual funding limits.** | Baseline Invariants 3–6 (identical annual funding capacity and timing; exactly 12.0 new units per calendar year; no borrowing of future-year units; carry-forward without expiry) would have to remain binding on any variant. AR-01 as proposed changes only the **rate of deployment**, not the funding — but this is **recorded as a question to be confirmed explicitly, not assumed.** |
| **E-9** | **Interaction with the 0% cash assumption.** | OD-07 / [§11.3](../experiment_spec.md#113-cash-return-assumption) appear unaffected in principle: unused satellite budget remains zero-yield nominal JPY and remains part of total economic value. A different rate of deployment changes the realized cash-versus-exposure mix, which would be an **outcome** rather than a rule question. **Recorded as a question to be confirmed explicitly, not assumed.** |
| **E-10** ⚠ | **Month boundaries, and cross-month execution attribution.** | "Month" means calendar month (OD-01). [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) states that "a delayed execution attributed to a prior calendar month MUST NOT consume the new calendar month's one-allocation limit." **No analogous statement exists for an entitlement counter**, and whether the counter is attributed by allocation month or by execution date is undetermined. **Not decided here — see AR-01.7.1.** It shares its root cause with E-1. |
| **E-11** | **Observation-date versus execution-date treatment, and the unit of measurement.** | Entitlement would have to be evaluated at the decision date on the confirmed close (OD-03, [§8](../experiment_spec.md#8-signal-observation-timing)) using only information available then ([§6](../experiment_spec.md#6-look-ahead-prohibition)). At a later decision date, an earlier same-month allocation may still be pending execution at an unknown valuation. Whether the counter is denominated in **units** (1 unit = JPY 10,000, [§2.3](../experiment_spec.md#23-satellite-investment-baseline--od-07-od-10-od-14)) or in acquired exposure is **not decided here** — noting only that a quantity unknown at the decision date could not be used without conflicting with [§6](../experiment_spec.md#6-look-ahead-prohibition). |
| **E-12** | **Which strategies the variant would apply to, and under what identity.** | Strategy A takes no drawdown input ([§4.1](../experiment_spec.md#41-strategy-a--simple-dca-control)). For Strategies B and C, [§4](../experiment_spec.md#4-strategy-set) states the three research roles "are distinct and MUST be preserved". Whether the variant would be expressed as **new strategy identifiers** evaluated alongside an unchanged A, B, C — rather than as a redefinition of B or C — is **not decided here**. |
| **E-13** | **Strategy C's Month-End Fallback as an entitlement.** | Under [§4.3](../experiment_spec.md#43-strategy-c--daily-drawdown-trigger--month-end-fallback) the 0.5-unit fallback applies only on the final trading day and only when `DD > −10%`. Entitlement for Strategy C would therefore not be a function of zone alone, but of zone **and** whether the day is the month's final trading day. The hypothesis as stated reads entitlement off the zone alone. **Not decided here.** |
| **E-14** | **Evidence-record and metric extensions.** | The evidentiary record requirement in [§5.1](../experiment_spec.md#51-evidentiary-record-requirement) has no field for cumulative monthly allocated units, entitlement at the decision date, or unfilled entitlement, and no reason code distinguishing a top-up acceptance from the existing monthly-exclusivity suppression code. Metric definitions under [§13.6](../experiment_spec.md#136-methodology-remaining-metric-definition-work) (M-1, M-6) would need to be valid under the variant. **None of this is designed here.** |
| **E-15** | **The zero-unit-acceptance argument does not transfer.** | [§12.7](../experiment_spec.md#127-methodology-zero-unit-acceptance-semantics) defers zero-unit-acceptance semantics (M-6) on the reasoning that the question is outcome-neutral for units acquired, because available units can only decrease within a calendar month so a later request would also cap to zero. That reasoning is specific to the Frozen Baseline's one-allocation rule; under an entitlement rule, later requests in the same month are structurally expected. The argument would have to be **re-derived for the variant**. This observation applies to AR-01 only and **does not reopen M-6 for the Frozen Baseline**. |
| **E-16** | **Naming.** | "Monthly Cumulative Allocation Cap" describes a ceiling, while the proposed mechanism is a zone-determined cumulative monthly entitlement filled incrementally. The provisional name is retained as proposed. **`AR-01` is the stable identifier**; the descriptive name is non-normative and may be changed later without affecting the identity or provenance of this entry. |

## AR-01.8 Supporting observations

Two observations recorded during the preparation of this entry are retained **because they help
a future reader understand AR-01**, and for no other reason.

> **Neither is a criticism of the Frozen Baseline, neither is a defect report, and neither
> requires or permits any modification of the Frozen Baseline.** Only the Owner may change that
> specification, under [§18.2](../experiment_spec.md#182-effect-of-the-freeze).

### Observation 1 — how the Baseline describes a suppressed later Signal

Three passages describe the same event with two vocabularies:
[§5.1](../experiment_spec.md#51-evidentiary-record-requirement) refers to "**Signals
suppressed**"; [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) refers to
"**Execution suppression**"; [§12.5](../experiment_spec.md#125-monthly-exclusivity-while-pending)
says "their execution is suppressed".

**All three agree that no additional allocation occurs, so Baseline behaviour is unambiguous.**
The relevance to AR-01 is narrow and forward-looking: under AR-01 a later Signal could be
**partially filled** rather than suppressed, so a future evidentiary record for the variant would
need to distinguish three outcomes rather than two — which is part of open question **E-14**.

### Observation 2 — S-3 names a class, not a specific variant

[§19.3](../experiment_spec.md#193-deferred-sensitivity-questions--phase-4) S-3 reads, in full:
"Same-month escalation variants." As AR-01.3.4 records, at least two structurally different
variants fall within that description.

The relevance to AR-01 is that this entry supplies **one specific instance** of that class, from
outside the frozen document, one-way, **without editing S-3**. No Baseline behaviour depends on
S-3's level of detail, because same-month escalation is excluded from the Baseline entirely.

## AR-01.9 Possible future experimental treatment

**Recorded as options. No route is selected, and selecting one is not required now. Recording
AR-01 authorizes neither route.**

### AR-01.9.1 Evaluating this during Phase 2 would contaminate the primary experiment

| Contamination mechanism | Frozen-Baseline basis |
| ----------------------- | --------------------- |
| Phase 2 exists to implement **the pre-specified rules**; AR-01 is not among them | [§18.3](../experiment_spec.md#183-relationship-to-phase-1-and-phase-2) |
| The Baseline parameters "are tested **first**"; sensitivity analysis belongs to Phase 4 | [§16](../experiment_spec.md#16-no-optimization-before-baseline-evidence) |
| Alternatives "MAY be explored **only after** Baseline evidence is recorded, and MUST be reported separately" | [§16](../experiment_spec.md#16-no-optimization-before-baseline-evidence) |
| Retroactive optimization presented as pre-specified Baseline evidence is prohibited | Invariant 17; [§18.2](../experiment_spec.md#182-effect-of-the-freeze) |
| Same-month escalation is excluded from the Baseline and deferred to Phase 4 | Invariant 15; [§10](../experiment_spec.md#10-one-allocation-per-calendar-month); [§19.3](../experiment_spec.md#193-deferred-sensitivity-questions--phase-4) S-3 |

Even a side-by-side run during Phase 2 would produce a Baseline result and an alternative result
simultaneously, with no recorded ordering — removing the ability to demonstrate that the Baseline
was reported without reference to the alternative. **The sequencing is itself part of the
evidence.**

### AR-01.9.2 Two possibilities, both left open

| Route | Mechanism | When it would apply |
| ----- | --------- | ------------------- |
| **Phase-4 sensitivity analysis under the existing S-3 deferral** | [§10](../experiment_spec.md#10-one-allocation-per-calendar-month) and [§19.3](../experiment_spec.md#193-deferred-sensitivity-questions--phase-4) S-3 already assign same-month escalation here. Reported separately; never presented as Baseline evidence; requires no change to the Frozen Baseline | If the variant is to be studied as a robustness question about the Baseline |
| **A future explicitly versioned Baseline, created under separate research governance** | [§18.2](../experiment_spec.md#182-effect-of-the-freeze): "a new, explicitly versioned Baseline created under research governance". Would require its own pre-specification, its own freeze, and its own decision series. **Phase-0 Baseline v1 would remain untouched** | If the variant is to be a primary object of study rather than a sensitivity |

> **Both possibilities remain open. Neither is chosen, and neither is authorized by the recording
> of AR-01.**

### AR-01.9.3 Contamination controls that would apply to either route

1. **Ordering gate.** The Frozen-Baseline result must exist, be recorded, and be reviewed before
   any variant result is produced.
2. **Separate strategy identity.** Expressed as new strategy identifiers alongside an unchanged
   A, B, C — never as a redefinition of B or C (see E-12 and
   [§4](../experiment_spec.md#4-strategy-set)).
3. **Identical funding.** Same annual capacity and same funding timing (Invariant 3), so that
   only deployment behaviour differs.
4. **Metrics fixed first**, before any result is inspected (Invariant 17,
   [§13.6](../experiment_spec.md#136-methodology-remaining-metric-definition-work)).
5. **No threshold or sizing tuning.** Any change to thresholds or sizing would make it a
   different variant, requiring its own pre-registration.
6. **Separate reporting.** Variant results reported in their own artifact or an unambiguously
   separated section, never inside a Baseline evidence artifact.
7. **Provenance citation.** Every variant result cites this entry's recording date.
8. **No queue-jumping.** The variant depends on exactly the same data foundation as the Baseline;
   P1-1 … P1-9 and M-1 … M-8 gate it identically. Recording AR-01 creates no reason to accelerate
   Phase 1.

## AR-01.10 Explicit non-authorization

Recording AR-01 does **NOT**:

- adopt the rule, or express any intention to adopt it;
- approve it as a strategy rule;
- authorize its implementation, in code or otherwise;
- authorize any backtest, simulation, or hypothetical evaluation of it;
- authorize evaluating it during Phase 2;
- authorize either of the two future treatment routes in AR-01.9.2;
- authorize beginning Phase 2;
- modify the Frozen Phase-0 Baseline, OD-01 … OD-14, or any Baseline Invariant;
- modify, expand, or resolve S-3 or any other deferred sensitivity question;
- resolve any open question E-1 … E-16;
- change any Phase-1 requirement status (P1-1 … P1-9), any methodology requirement
  (M-1 … M-8), the Primary Proxy status, or the Phase-2 gate;
- change the current approved Phase-1 research direction;
- assert that the rule is superior, equivalent, or inferior to the Frozen Baseline;
- assert that the Frozen Baseline's deliberate same-month escalation exclusion is a bug, a
  defect, an oversight, or an ambiguity requiring correction.

## AR-01.11 Confirmations

- **This entry records a proposal only. It contains no empirical result, and none may be added
  to it later.**
- **No backtest, simulation, or performance calculation of any kind was performed.** No return,
  TTEV, CAGR, drawdown, or portfolio quantity was computed.
- **No historical occurrence count was produced**, and no historical period was examined for
  occurrences of the condition the rule describes.
- **No comparison with the Frozen Baseline was performed.**
- **No threshold or allocation size was tuned.**
- **AR-01 is not an executable specification**; E-1 and E-10 are unresolved blocking semantic
  issues.
- **The Frozen Phase-0 Baseline and OD-01 … OD-14 are unchanged.**
- **No Phase-1 Evidence Artifact and no Phase-1 Owner Decision was modified.**
- **P1-1 … P1-9 and M-1 … M-8 are unchanged. P1-2 remains OPEN. P1-5 remains OPEN. P1-6 remains
  OPEN.**
- **The approved next Phase-1 research direction — Primary Proxy Candidate Qualification — is
  unchanged and was not begun by this entry.**
- **Phase 2 remains BLOCKED.**

---

**End of AR-01. Status: RECORDED — NOT ADOPTED, NOT VALIDATED, NOT AUTHORIZED FOR
IMPLEMENTATION. Proposed 2026-08-11, before Phase-2 backtesting and before any performance
comparison of this alternative existed. The Frozen Phase-0 Baseline is unchanged.**
