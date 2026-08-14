# Simulation Trial — Strategy D: Owner Semantic Decision (SD-1, SD-2, SD-3, SD-5, SD-6)

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** Additive to, and does not modify,
`docs/decisions/simulation_trial_strategy_d_owner_hypothesis.md` (commit `5a3f54a`, tag
`simulation-trial-strategy-d-hypothesis-20260814`), which remains historical authority exactly as
preserved. **Registration/semantic decision only — NOT ADOPTED · NOT VALIDATED · NOT AUTHORIZED FOR
IMPLEMENTATION OR EVALUATION.**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Governing Baseline:** v2 (effective 2026-08-13) — unchanged by this artifact
**Governing Simulation Trial authority:** §18.3–18.4 (unchanged); the preserved Strategy-D hypothesis
(`5a3f54a`), whose `SD-1`…`SD-10` definitions this artifact re-evaluates without editing.

---

## 1. Authority and chronology

This artifact is **purely additive**. It does not amend, correct, or retroactively reinterpret
`5a3f54a`. That artifact's statement that `SD-1`…`SD-8` were open was accurate at the moment of its
preservation. The chronology is:

1. A/B/C existed and were mechanically tested (`MP-H1`/`MP-H2`, commit `da85b66`).
2. The Owner inspected the preserved Mode-P economic comparison (`MP-EV`/`MP-EV2`, commits
   `00b2b4a`/`e475717`).
3. The Owner generated Strategy D as a post-result hypothesis, motivated by Strategy B's observed
   undeployed-cash pattern.
4. Strategy D was registered at `5a3f54a` with `SD-1`…`SD-8` open.
5. The Owner resolved `SD-1` and `SD-3` (recorded in the prior revision of this artifact).
6. **The Owner now additionally resolves `SD-2`, `SD-5`, and `SD-6`**, recorded here.

Governing text re-verified for this task: Baseline v2 §3 (state model), §4.2 (Strategy B), §4.3
(Strategy C month-end fallback), §10 (monthly exclusivity), §11.1–11.3 (funding), §12.1–12.7
(commitment/reservation/capping/execution), §12.7 (zero-unit-acceptance semantics), §5.1 (evidentiary
record), `engine.py`'s `SUPPORTED_STRATEGIES = ("A", "B", "C")` and its preserved
implementation-evolution rule. None of these texts is modified by this artifact. No conflict was found
between the decisions below and controlling authority — every decision remains confined to the
Simulation Trial lane exactly as `AR-01` and `5a3f54a` already establish is permitted.

---

## 2. `SD-1` — Direct-to-Large-drop behavior. **RESOLVED BY OWNER — unchanged, reaffirmed.**

> If the month's first qualifying observation is already Large-drop (`DD ≤ -20%`), Strategy D may
> request the full `2.0` units immediately, as a single allocation. No further Strategy-D allocation
> may subsequently be generated in that calendar month merely because drawdown becomes deeper.

## 3. `SD-3` — Incremental allocation accounting. **RESOLVED BY OWNER — unchanged, reaffirmed.**

> The later Large-drop top-up is a new, independent allocation / Purchase Request, not a resize or
> amendment of allocation #1. Both allocations draw from one shared Strategy-D calendar-month
> capacity.

## 4. `SD-2` — Repeated non-escalating Normal signals. **RESOLVED BY OWNER.**

> After Strategy D has generated and accepted its first Normal-zone allocation for a calendar month,
> further qualifying observations that remain in the Normal zone do **not** generate another
> Strategy-D allocation in that month.

Strategy D is therefore **not** "up to two arbitrary purchases per month" — it is a conditional
staged-deployment rule with exactly two possible tranches: the Normal tranche (fires once, first
qualifying Normal event) and the Large-drop escalation tranche (fires at most once, only on a
qualifying Large-drop deterioration strictly after the Normal tranche fired). A later Normal-only
observation matches neither tranche's firing condition and therefore never allocates.

## 5. `SD-5` — Zero-unit capping / acceptance boundary. **RESOLVED BY OWNER.**

> If ordinary funding/capping mechanics reduce a proposed Strategy-D allocation to exactly `0` units,
> no Strategy-D Purchase Request / Commitment is established for that attempt. A zero-unit result
> creates no allocation, no commitment, no reservation, no execution entitlement; does not consume
> Strategy-D monthly capacity merely by being evaluated; and does not, by itself, suppress a later
> otherwise-valid Strategy-D allocation.

This decision must not invent funding; existing funding/capping authority (§12.4) remains fully
binding. It is distinct from — and must not be conflated with — a **positive** capped acceptance below
the nominal tranche size, which remains governed by `SD-4` (§6 below).

## 6. `SD-4`/`SD-5` consistency check — the principal fail-closed check for this task

**Case examined.** First qualifying event is Normal; nominal Strategy-D Normal tranche `= 1.0`; only
`0.5` units can actually be accepted under existing funding/capping; `0.5` is positively committed.
**Question.** Does Strategy-D monthly capacity consumption become (A) the actual accepted amount
(`0.5`), or (B) the nominal tranche entitlement (`1.0`)?

**Resolved: (A) — the actual accepted amount.** This is unambiguous under existing preserved
authority, without requiring a new Owner value judgment:

- §12.4 (Capping): *"accepted units = currently available units, and **only those accepted units are
  reserved**."* The Baseline's accounting model, applied without exception to every units-consuming
  event it governs, always decrements a ledger by the **actual accepted (post-cap) amount**, never the
  nominal pre-cap request.
- §11.2: *"Executed and reserved units reduce available units"* — the same principle, restated for the
  annual ledger.
- The Owner's own `SD-3` wording (prior revision of this artifact) describes capacity being **consumed**
  by what was **committed** — and `SD-3` explicitly defines "committed" as "accepted for execution"
  (§12.1), i.e. the *post-capping* quantity, not a pre-capping nominal figure.

Strategy D's monthly capacity is a **new, Strategy-D-specific** ledger, not inherited from any existing
Baseline provision — but its accounting **behavior** follows the same structural principle every other
ledger in this Baseline already follows. Applying a different rule to this one new ledger, with no
textual basis for the difference, would be the invented convenience this task's discipline forbids;
applying the *same* rule that governs every other ledger in the document is the citation-grounded
default.

**Consequence for the escalation tranche's nominal size.** The escalation tranche's own nominal request
remains fixed at `1.0` (unchanged from the original hypothesis, §5 item 4 of `5a3f54a`) regardless of
how much the Normal tranche actually accepted — it is not "whatever capacity remains." That nominal
`1.0` request is then independently subject to **two** separate limits, applied without exception: (i)
remaining Strategy-D capacity (`2.0` minus whatever was actually accepted for the Normal tranche), and
(ii) ordinary §12.4 funding capping. Both limits apply; neither is waived by the other.

**A second, narrower question surfaced by this check, and resolved by the same method — flagged
prominently.** If the Normal tranche's attempt is capped all the way to **zero** (`SD-5`), can the
Large-drop escalation tranche still fire later in the same month? Two readings were considered:

- *Permissive reading:* `SD-5`'s clause "does not... suppress a later otherwise-valid Strategy-D
  allocation" was intended to keep the escalation tranche available even after a zero-capped Normal
  attempt.
- *Conservative reading (adopted):* the escalation tranche's gate, fixed unchanged since the original
  hypothesis (`5a3f54a` §5 item 4: "**after that first allocation has been accepted**"), requires a
  positive acceptance to have occurred. `SD-5` establishes that a zero-result creates **no commitment**
  — nothing was accepted. `SD-5`'s "does not suppress" clause protects against the zero-attempt causing
  some *unrelated* side effect (e.g. wrongly consuming capacity or blocking an otherwise-independent
  opportunity); it does not — and by its own wording cannot — retroactively manufacture the positive
  acceptance the escalation gate's unmodified text requires. Nor does this scenario qualify as the
  `SD-1` direct-Large-drop path, because a Normal-zone observation occurred chronologically first that
  month, even though it zero-capped.

**Adopted: the conservative reading.** A Normal tranche that zero-caps under `SD-5` does **not** open
the door to the Large-drop escalation tranche later in the same month. In that specific edge case,
Strategy D generates **no** allocation that month, even if the market subsequently reaches Large-drop.
This is not an economic judgment about what would be preferable — it is the literal, unmodified text of
the escalation gate applied to a zero-acceptance state that `SD-5` itself defines as "no commitment."
It is also the more conservative of the two readings, consistent with `SD-5`'s explicit instruction not
to invent funding or manufacture allocations. **This is recorded here for Owner visibility because it
is a non-obvious, mechanically-derived consequence of combining `SD-5` with the unmodified original
gate text — not because it remains open.** No further Owner judgment is required to apply it; a future
Owner Decision could still expressly override it if a different outcome is intended.

---

## 7. `SD-6` — Month-end fallback. **RESOLVED BY OWNER.**

> Strategy D has **no** Strategy-C-style month-end fallback: no automatic `0.5`-unit month-end
> allocation; no fallback merely because no Normal/Large-drop trigger occurred; no fallback merely
> because monthly capacity remains unused; no fallback merely to reduce accumulated undeployed cash.

Strategy D remains a purely drawdown-triggered alternative derived from Strategy B, addressing only
staged deployment across a Normal → Large-drop deterioration. It is not combined with Strategy C's
month-end mechanism. **Strategy C is unmodified by this artifact.**

---

## 8. Shared monthly-capacity definition (restated, unchanged from the prior revision)

```
strategy_d_monthly_capacity(month) = 2.0 units          [a RULE ceiling, not a funding grant]
```

Capacity gates **tranche-firing eligibility** (has the Normal tranche already fired this month? has the
Large-drop tranche — via either path — already fired this month?) and is **numerically consumed** by
the actual accepted amount of each fired tranche (§6). It resets each new calendar month, attributed by
acceptance month (§12.2, inherited — see `SD-7`). It is never a source of funding (§9).

## 9. Annual-funding rule — unchanged

Strategy D receives **no additional annual funding**. Existing annual grant, available-funding,
reservation, carry-forward, and execution accounting (§11.1–§11.3, §12.1–§12.4) remain fully
controlling. If capacity would permit `2.0` but only `1.0` unit of funding is actually available,
Strategy D must not manufacture the missing funding — ordinary §12.4 capping governs, exactly as for
any other strategy's Purchase Request.

---

## 10. Formal Strategy-D rule, current state

| Condition | Behavior |
| --- | --- |
| High zone | No Strategy-D allocation |
| First qualifying event of month is Normal | Nominal request `1.0`, subject to ordinary funding/capping (`SD-4`/§6) |
| Repeated Normal observations, same month | No additional allocation (`SD-2`) |
| Normal tranche positively accepted, later same-month Large-drop | New, independent escalation allocation; nominal request `1.0`, subject to remaining capacity **and** ordinary funding/capping (`SD-3`, §6) |
| Normal tranche zero-capped (`SD-5`), later same-month Large-drop | **No** escalation allocation — gate requires positive prior acceptance, not satisfied (§6) |
| First qualifying event of month is already Large-drop | Nominal request `2.0`, single allocation, subject to ordinary funding/capping (`SD-1`) |
| Repeated Large-drop observations after capacity/tranches exhausted | No further allocation (`SD-1`, `SD-3`) |
| Month end | No fallback (`SD-6`) |
| New calendar month | Capacity/tranche-firing state resets; outstanding commitments/reservations from a prior month continue under existing unmodified mechanics (`SD-7`) |
| Annual funding | Unchanged from A/B/C; capacity is not a funding grant (§9) |

---

## 11. Complete `SD-1`…`SD-10` matrix — final

| ID | Original question | Final state | Authority | Implementation blocking? |
| --- | --- | --- | --- | --- |
| `SD-1` | Direct-to-Large-drop behavior | **RESOLVED BY OWNER** | §2 | No |
| `SD-2` | Repeated non-escalating Normal signals | **RESOLVED BY OWNER** | §4 | No |
| `SD-3` | Accounting model for the top-up | **RESOLVED BY OWNER** | §3 | No |
| `SD-4` | Capping interaction / sizing basis | **RESOLVED BY OWNER + EXISTING AUTHORITY** — actual accepted amount consumes capacity; escalation tranche nominal size fixed at `1.0`, doubly capped by remaining capacity and funding | §6; §12.4, §11.2 | No |
| `SD-5` | Zero-unit acceptance boundary | **RESOLVED BY OWNER**, including the derived escalation-gate consequence in §6 | §5; §6 | No |
| `SD-6` | Month-end fallback | **RESOLVED BY OWNER** — none exists | §7 | No |
| `SD-7` | Cross-month execution interaction with the top-up gate | **RESOLVED — unaffected, reaffirmed** | prior revision §7; §12.2 | No |
| `SD-8` | Evidentiary-record and reason-code extension | **RESOLVED — follows mechanically.** With `SD-1`/`SD-2`/`SD-3`/`SD-4`/`SD-5`/`SD-6`/`SD-7` all fixed, the complete, enumerable set of distinct event/reason-code types is now determinate: (1) Normal-tranche commitment; (2) Large-drop escalation-tranche commitment; (3) direct-Large-drop commitment; (4) `SD-2`-class non-escalating-Normal suppression; (5) monthly-capacity-exhausted suppression (repeated Large-drop after capacity used); (6) `SD-5`-class zero-acceptance non-event; (7) no-signal/High-zone day (inherited from B). Designing the actual schema (field names, exact reason-code strings) is ordinary engineering work, not a remaining semantic question requiring further Owner judgment. | §5.1; §2–§7 of this artifact | **No — semantically resolved.** Schema design remains ordinary implementation work under §11 of `5a3f54a` |
| `SD-9` | Strategy identity | RESOLVED BY CONSTRUCTION — unaffected | `5a3f54a` §9 | No |
| `SD-10` | Boundary-ownership/tolerance treatment | RESOLVED BY CONSTRUCTION/INHERITANCE — unaffected | `5a3f54a` §9 | No |

**No unresolved implementation-blocking semantic remains among `SD-1`…`SD-10`.**

---

## 12. Month/year-boundary verification (semantic level only — nothing executed)

Checked against the already-validated E2/E3/E4 accounting authority, without running anything:

- **Commitment-month attribution / execution in a later month:** unaffected — capacity is attributed by
  acceptance month (§12.2, inherited); execution timing of either tranche never changes which month's
  capacity was consumed.
- **December commitment → January execution:** governed identically to any existing allocation; the
  escalation gate depends only on acceptance, never on execution completion (`SD-7`).
- **Outstanding reservation surviving a month/year boundary:** unaffected; §12.3/§12.6's existing
  non-disappearance requirement is untouched by this artifact.
- **New annual grant / carry-forward:** untouched (§9) — capacity is a monthly, Strategy-D-only
  construct, entirely separate from the annual funding ledger.
- **No double deduction:** unaffected — each tranche is an independent Purchase Request under existing
  §12.1–§12.4 mechanics; capacity bookkeeping is additional, parallel accounting, not a substitute for
  the existing funding ledger.
- **Monthly Strategy-D state reset independent of outstanding execution state:** confirmed explicitly
  (§8/§10 above) — a new calendar month's capacity is unaffected by a prior month's still-pending
  execution.

**No new year-boundary funding rule is created by this artifact.** No conflict found; no STOP required
under this section.

---

## 13. Strategy B and C preservation

Strategy B and Strategy C remain **exactly** as Baseline v2 defines them (§4.2, §4.3); neither is
modified, referenced as needing correction, or affected by any decision in this artifact. Strategy D is,
and remains, an **EXPERIMENTAL ALTERNATIVE HYPOTHESIS** / **OWNER-GENERATED POST-RESULT ALTERNATIVE
HYPOTHESIS** — never described as an improved, corrected, optimized, or superior version of B.

## 14. Post-result contamination disclosure — unchanged, restated

> **Strategy D remains an OWNER-GENERATED POST-RESULT ALTERNATIVE HYPOTHESIS.** It was proposed after
> inspecting the preserved `MP-EV`/`MP-EV2` A/B/C economic comparison, specifically motivated by
> Strategy B's observed undeployed-cash pattern on the released NDXJPY window
> (`2018-01-02`→`2020-06-26`). That window remains Stage D-H0 — hypothesis-generating data only, never
> independent evidence. **Resolving every remaining mechanical semantic in this artifact does not, and
> cannot, cure that post-result contamination; the two are unrelated questions.** This disclosure
> obligation is unweakened and must be restated by every future artifact that reports, discusses, or
> evaluates Strategy D on that window.

## 15. Explicit implementation prohibition — unchanged

This artifact authorizes **none** of the following, regardless of `SD-n` resolution completeness:
modifying `engine.py`; extending `SUPPORTED_STRATEGIES`; implementing monthly Strategy-D capacity or the
second allocation path; adding Strategy-D fixtures or tests; executing Strategy D in any mode; creating
Strategy-D evidence of any kind; retrieving data; performing economic evaluation; beginning Stage D-H1
independent validation; asserting Strategy D is superior, inferior, or an improvement over A, B, or C.

## 16. Remaining authorization required before implementation

Exactly one substantive item remains, unaffected by this artifact's semantic completeness: **explicit
Owner authorization to extend `engine.py`'s `SUPPORTED_STRATEGIES` beyond `("A", "B", "C")`**, per
`engine.py`'s own preserved implementation-evolution rule (extension permitted only for an
"already-authorized" strategy). Ordinary schema/engineering design for `SD-8`'s evidentiary fields
follows as implementation work once that authorization exists. A manifest label of
`EXPERIMENTAL VARIANT — NOT BASELINE` (§18.4.5) and all four preserved regression suites passing
unchanged remain standing requirements from `5a3f54a` §11.

---

## 17. Qualification-state and prior-artifact preservation

Unchanged by this artifact, identically to `5a3f54a` §14: all `P1-x`/`M-x`/`O-4`/`HG-8`/Primary-Proxy/
Stage-G/Stage-H/Phase-2 state; the Frozen Baseline; the criteria freeze `1e8bc85`; `AR-01`. The preserved
Strategy-D hypothesis (`5a3f54a`) is **not edited** — this artifact is purely additive.

---

**End of entry. Status: APPROVED BY OWNER DECISION, 2026-08-14. Records the Owner's resolution of
`SD-1`, `SD-2`, `SD-3`, `SD-5`, and `SD-6`, additive to the Strategy-D hypothesis registered at
`5a3f54a`. All ten `SD-n` items are now semantically resolved; no implementation-blocking ambiguity
remains among them. Does not authorize implementation, simulation, or evaluation of Strategy D — that
requires a separate, later, explicit Owner authorization (§16). The Frozen Baseline, `AR-01`, and
`5a3f54a` are unchanged.**
