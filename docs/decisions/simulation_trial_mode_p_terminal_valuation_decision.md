# Simulation Trial — Mode P: Terminal-Valuation Decision for the First Economic Evaluation

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.**
`MP-EV-D1` **APPROVE** · `MP-EV-D2` **APPROVE** · `MP-EV-D3` **APPROVE WITH NARROW SCOPE** ·
`MP-EV-D4` **APPROVE**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13)
**Controlling Mode-P authority:** Decision Boundary `91378fe` · Execution Plan `535de39` ·
NDXJPY bounded-release Decision `73d6f51` · driver preservation `da85b66`,
tag `simulation-trial-mode-p-first-historical-run-20260814`
**Preceding analysis:** governance-analysis work product drafted 2026-08-14,
`docs/research/simulation_trial_mode_p_terminal_valuation_decision_request.md` (retained locally as a
historical record of the critical-path analysis; not committed to this repository — this artifact is
the self-contained authoritative decision and supersedes it for all normative purposes).

**One artifact, self-contained.** Following the pattern of `91378fe` and `73d6f51`, this decision does
not require the reader to cross-reference an uncommitted draft. Every approved disposition is restated
here in full.

---

## 1. What this decision is for

The currently-approved Mode-P Decision Boundary (`91378fe`, `MP-D3` as amended) **absolutely
prohibits** reporting *"terminal exposure valued at the final observation,"* `TTEV`, or *"any terminal
portfolio valuation"* from a Mode-P run — a prohibition reaffirmed after an earlier drafting defect was
caught and corrected.

The Owner has asked the narrowest useful next economic question: the terminal economic value of
Strategies A, B and C over the already-preserved historical window (`MP-H2-A/B/C-001`, commit
`da85b66`). **That quantity is, by formula, identical to Baseline v2 §13.1's `TTEV`.** It cannot be
computed or reported under the current `MP-D3` boundary. This decision is the **minimum, explicitly
bounded amendment** that permits it — nothing more.

---

## 2. Critical-path findings — accepted

| Item | Finding | Disposition |
| --- | --- | --- |
| `P1-1` / `OD-04` | Only the narrow **terminal-valuation-price** sub-question is load-bearing here. The **execution-price** question (`MP-R-02`) is untouched and not re-examined. | Resolved for Mode-P purposes only by `MP-EV-D1` below. General `P1-1` remains **OPEN**. |
| `P1-3` | Not required for the arithmetic (units × price + cash needs no knowledge of return composition). Remains a disclosure limitation on **economic interpretation** only. | No new decision needed; standing disclosure (`"Return composition declared, not verified — P1-3 OPEN"`) carries forward unchanged. |
| `M-1` | Not required for this first Level-1 terminal-value comparison — average acquisition cost, XIRR cash-flow convention, and drawdown-measurement basis are not invoked. | Remains **OPEN**, not on the critical path. |
| `M-5` | **Genuinely load-bearing for this specific preserved run.** Strategy A committed `1.0` unit and Strategy C committed `0.5` unit on `2020-06-26` — the dataset's own final observation — so under `MP-R-02` no execution is possible within this window; both sit reserved-but-unexecuted at the comparison date. Strategy B has zero outstanding reservation. | Resolved for Mode-P presentation purposes only by `MP-EV-D2` below. General `M-5` (for Phase 2) remains **OPEN**. |
| `M-8` | Not required — this is a single-path, non-statistical, non-probabilistic observation. | Remains **OPEN**, not on the critical path. |

No item beyond this table is pulled onto the critical path. `P1-2`, `P1-4`–`P1-9`, `M-2`, `M-3`, `M-4`,
`M-6`, `M-7`, `O-4`, `HG-8` are unaffected and unresolved.

---

## 3. Approved decisions

> ### `MP-EV-D1` — Terminal valuation price convention **`[APPROVED — OWNER DECISION 2026-08-14]`**
>
> For this bounded Mode-P economic evaluation, already-acquired exposure units are valued at the
> **close of the final available observation in the released Mode-P dataset** (`2020-06-26`, close
> `1000`) — the single common comparison date required by §13.1, using the same series `MP-R-02`
> already executes against.
>
> This is deliberately **not** the same question as `MP-R-02` (which prices *execution* — how many
> units a given cash amount buys). `MP-R-02` is untouched and unre-examined by this decision.
>
> Declared in every output as **PROVISIONAL TERMINAL VALUATION CONVENTION — MODE P ONLY**. It is
> **NOT a `P1-1` determination**; it does not establish any formal signal-to-NAV mapping; it does not
> alter `MP-R-02`; it does not alter qualification state.

> ### `MP-EV-D2` — Treatment of committed-but-unexecuted reservations **`[APPROVED — OWNER DECISION 2026-08-14]`**
>
> Outstanding reserved-but-unexecuted allocations remain represented as **cash**, not exposure, at the
> comparison date, because no exposure units were actually acquired before the preserved dataset
> ended. Per §12.2/§12.6, reserved units are removed from *available* budget but the corresponding cash
> was never converted into exposure, so it stays on the cash side of the ledger — and it is disclosed
> **separately**, never silently folded in or dropped.
>
> **A Mode-P terminal report under this decision MUST therefore include, at minimum, all four of:**
>
> 1. cash available (unreserved, undeployed);
> 2. cash reserved but unexecuted;
> 3. total cash not converted into acquired exposure (the sum of 1 + 2);
> 4. acquired exposure units (and their `MP-EV-D1` valuation).
>
> This is **PROVISIONAL `M-5` PRESENTATION — MODE P ONLY**. It does **NOT** resolve `M-5` in general;
> the formal Phase-2 treatment remains **OPEN**.

> ### `MP-EV-D3` — Reportable-output boundary amendment (extends `MP-D3`) **`[APPROVED WITH NARROW SCOPE — OWNER DECISION 2026-08-14]`**
>
> `MP-D3` is amended to additionally permit **exactly** the following, and nothing beyond it:
>
> 1. terminal valuation price (`MP-EV-D1`);
> 2. terminal market value of actually acquired exposure;
> 3. unused / unconverted cash;
> 4. outstanding reserved cash, disclosed separately (`MP-EV-D2`);
> 5. combined terminal economic value / `TTEV` — under the mandatory label
>    **`MODE-P TERMINAL ECONOMIC VALUE — NOT BASELINE TTEV — SIMULATION-TRIAL ONLY`**. This is
>    textually and structurally identical to §13.1's formula but is barred from citation as Baseline
>    evidence by §18.4.3, exactly as `MP-R-01` is "algebraically identical" to §4.0 without resolving
>    `M-7`;
> 6. factual absolute differences among A / B / C (e.g. "Strategy B holds ¥X more cash and Y fewer
>    exposure units than Strategy A"), computed from the already-permitted fields above;
> 7. a simple, non-annualized, single-path, funding-relative return percentage —
>    `(terminal economic value − cumulative funding)/cumulative funding` — **conditioned** on its
>    denominator already being unambiguous under existing authority. **That condition is satisfied**:
>    `cash_granted_jpy` is already an existing, already-permitted, already-reported engine field
>    (`¥360,000`, identical for Strategies A, B and C by Invariant 3 and by the preserved `MP-H2`
>    terminal states), so no additional methodology decision is required to fix it. If a future
>    reporting attempt needs a denominator this decision does not already fix, the percentage MUST be
>    **deferred** rather than opening a new methodology question.
>
> **Explicitly still prohibited, unchanged:** `CAGR`; `XIRR`; any annualized or time-weighted return;
> rolling-window statistics; significance testing; probabilistic claims; formal strategy ranking;
> Primary Proxy inference; qualification use; any statement of comparative performance, superiority, or
> economic benefit/cost between strategies.
>
> §18.4.3's bar on **"strategy superiority"** from **any** Simulation Trial output is **structural and
> permanent** — no Owner Decision within the Simulation Trial lane can lift it. Reaching it requires a
> formal Phase-2 execution under §18.4.4, which remains **BLOCKED**.

> ### `MP-EV-D4` — Anti-contamination reaffirmation **`[APPROVED — OWNER DECISION 2026-08-14]`**
>
> Restates the standing §18.4.7 obligation already attached by the NDXJPY release (`73d6f51`),
> unchanged and unweakened. Any future artifact deciding `O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`,
> Stage G, Stage H, or Primary Proxy selection MUST explicitly state that:
>
> - the preserved Mode-P NDXJPY results were known;
> - the observed A/B/C mechanical differences were known;
> - those observations were not used to resolve qualification questions;
> - no Primary Proxy inference is made;
> - `O-4`, all `P1-x`, `HG-8`, Stage G and Stage H remain unchanged.

---

## 4. Interpretation boundary

§18.4.3 is preserved without exception. Mode-P output under this decision MAY report **factual**
economic quantities and **factual** differences (§3, item 6). It MUST NOT label any strategy
**superior, inferior, better, worse, optimal, or economically proven**, and MUST NOT describe retained
cash as **beneficial or costly** as a formal Mode-P conclusion.

**This restriction governs Mode-P *output* — the artifacts, manifests, and reports this decision
authorizes.** It does **not** restrict the Owner's own private use of the reported provisional
observations to form a future research hypothesis. Nothing in this decision, or in the observations it
permits reporting, may itself assert or imply such a conclusion.

---

## 5. Strategy D — explicitly out of scope

The Owner has observed, from the preserved mechanical result, that Strategy B retained substantially
more unused cash than Strategy A or C, and has an informal future hypothesis in mind (a possible
Strategy D variant permitting a second unit on an intra-month escalation from Normal to Large-Drop).
**This decision does not register, define, implement, or test Strategy D, or any hypothesis about it.**
It is noted here only so the record is complete; it is not adopted, scheduled, or authorized by this
artifact in any way.

---

## 6. Execution-plan requirement — none needed

Baseline v2 §18.4.1's requirement for *"its own separate Owner Decision and execution plan"* governs
**authorizing a mode** (Mode E or Mode P) in the first place. This decision does not authorize a new
mode; it narrowly amends the already-authorized `MP-D3` boundary within the already-authorized Mode P,
exactly as `MP-R-01` and `MP-R-02` did inside the Decision Boundary (`91378fe`) itself, and as the
NDXJPY bounded-release amendment (`73d6f51`) did — neither required a separate execution plan. The
existing Execution Plan (`535de39`) already covers "implement the minimum loader and driver" (step P4)
as the template for the minimal reporting-layer work this decision authorizes; no new plan document is
warranted, and none is created here.

---

## 7. State preservation

Unchanged by this artifact: `O4-PARTIAL ×3` · `GAP-A ×3` · `GAP-B ×2` · `HG-8 NOT EVALUABLE ×3` ·
`P1-2 OPEN` · `P1-5 OPEN` · `P1-6 OPEN` · `H-1 NOT ESTABLISHED` · `P1-9 PARTIAL` ·
`C-1 ×3 QUALIFICATION INCOMPLETE` · **no Primary Proxy** · Stage G **OPEN** · Stage H **NOT BEGUN** ·
Phase 2 **BLOCKED** · `M-1, M-2, M-3, M-4, M-6, M-7, M-8` unresolved · `M-5` unresolved **in general**
(resolved only for this Mode-P presentation, `MP-EV-D2`) · `P1-1` unresolved **in general** (resolved
only for this Mode-P terminal-valuation convention, `MP-EV-D1`) · Mode P **NON-FORMAL and
NON-PROMOTABLE**. The Frozen Baseline, §13.1's `TTEV` definition, and the criteria freeze `1e8bc85` are
**not altered**. No preserved `MP-H1`/`MP-H2` evidence is modified.

---

## 8. Resulting readiness

If implemented, the minimum remaining engineering is a new, minimal reporting layer — not a new engine,
not new strategy logic — that reads the already-preserved `MP-H2-*-001` terminal states, applies
`MP-EV-D1`/`MP-EV-D2`, and writes a new manifest under a new run ID with all mandatory labels carried
forward unchanged. **This decision does not authorize that implementation.** It STOPS here, for Owner
Review of the implementation task as a separate step.
