# Simulation Trial — Strategy D: Owner-Generated Post-Result Alternative Hypothesis

**Status:** **REGISTERED BY OWNER APPROVAL, 2026-08-14 — OWNER-GENERATED POST-RESULT ALTERNATIVE
HYPOTHESIS.** Registration only. **NOT ADOPTED · NOT VALIDATED · NOT AUTHORIZED FOR IMPLEMENTATION OR
EVALUATION.**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Governing Baseline:** v2 (effective 2026-08-13) — unchanged by this artifact
**Governing Simulation Trial authority:** §18.3–18.4, in particular §18.4.5 (Experimental rule
variants) and §18.4.7 (Anti-contamination)
**Related but distinct precedent:** `docs/decisions/alternative_rule_hypothesis_register.md`
(`AR-01`) — see §0 below for why Strategy D is **not** an `AR-nn` entry in that register.

---

## 0. Artifact class and location — reasoning recorded, not assumed

Repository precedent for recording a strategy-rule hypothesis is
`alternative_rule_hypothesis_register.md`, which lives in `docs/decisions/`. This artifact follows
that **location** precedent. It deliberately does **not** follow it by becoming a new `AR-nn` entry
inside that file, for a reason the register's own text makes structural rather than stylistic:

> That register's title is **"Pre-Phase-2 Alternative Rule Hypothesis Register."** Its stated purpose
> (§1.1) is **anti-hindsight recording** — proving a rule idea was proposed *before* any result
> existed. `AR-01` satisfies that: it was proposed 2026-08-11, before any backtest of any kind had
> been run in this repository.

**Strategy D cannot satisfy that condition, and must not be recorded as if it could.** It was proposed
**after** inspecting the preserved Mode-P economic comparison for Strategies A, B and C
(`MP-EV`/`MP-EV2`, decision `00b2b4a`). Filing it as an `AR-nn` entry in the Pre-Phase-2 register would
misstate its provenance and would blur the very distinction that register exists to preserve. A
**separate, distinctly classified artifact** is therefore the correct — not merely convenient —
choice. §18.4.5's requirement that an experimental variant be *"separately recorded under the existing
hypothesis-register discipline"* is read here as requiring the same **rigor and structure** the
register demonstrates (dated provenance, explicit non-authorization, documented open semantics), not
as requiring literal insertion into a register whose own scope excludes this entry by definition.

This artifact is **not** part of the `AR-nn` series. It uses its own identifier prefix, `SD-` (Strategy
D), for internal open-question tracking, to avoid any collision with `AR-nn`, `P1-n`, `M-n`, `S-n`, or
`OD-nn`.

---

## 1. Status

**REGISTERED — OWNER-GENERATED POST-RESULT ALTERNATIVE HYPOTHESIS.** Registration approved by the
Owner, 2026-08-14. This approval is for hypothesis registration only; it does **not** authorize
implementation, simulation, or resolution of any open Strategy-D semantic (§9). No implementation, no
execution, no new data, no economic result exists for Strategy D anywhere in this repository or its
external evidence stores.

## 2. Date

Proposed by the Owner: 2026-08-14, after inspection of the preserved `MP-EV`/`MP-EV2` A/B/C economic
comparison. Drafted as a governance artifact: 2026-08-14.

## 3. Governing authority

Baseline v2 (`docs/experiment_spec_v2.md`) §3 (state model), §4.2/§4.3 (Strategy B/C), §10/§12
(monthly exclusivity, commitment, reservation), §18.3–18.4 (Simulation Trial lane), §19 (open items).
Mode-P Decision Boundary (`91378fe`), NDXJPY release (`73d6f51`), terminal-valuation decision
(`00b2b4a`), valuation-layer preservation (`e475717`). None of these is modified by this artifact.

## 4. Origin / chronology

1. `MP-H1`/`MP-H2` (commit `da85b66`): Strategies A, B, C executed mechanically over the released
   NDXJPY window (`2018-01-02`→`2020-06-26`). No economic quantity computed.
2. `MP-EV`/`MP-EV2` (commits `00b2b4a`, `e475717`): terminal economic value computed under `MP-EV-D1`
   through `MP-EV-D4`. Result showed Strategy B retaining materially more undeployed cash than A or C
   over this specific, disclosed-drawdown-biased window.
3. **Only after inspecting that result**, the Owner proposed Strategy D, explicitly motivated by
   Strategy B's observed undeployed-cash pattern.

> **This chronology is preserved permanently and must never be restated as if Strategy D preceded the
> A/B/C result.**

## 5. Owner hypothesis — stated, not yet formalized

Recorded here as the Owner stated it (§6 below performs the formalization step):

1. Same annual funding capacity as A/B/C.
2. Same drawdown-zone definitions and threshold ownership (`-10%`/`-20%`, §4.0) unless repository
   authority says otherwise.
3. First eligible observation in a calendar month reaching the Normal trigger may generate a first
   1.0-unit allocation.
4. If, **after that first allocation has been accepted**, the drawdown deteriorates into the
   Large-drop zone **within the same calendar month**, one additional 1.0-unit allocation may be
   generated.
5. Possible monthly total: `1.0` (Normal only), `2.0` (Normal then Large-drop deterioration), or `0`
   (no trigger).
6. The second allocation must **not** be generated merely because the month's first qualifying
   observation is *already* Large-drop, unless intended semantics and existing mechanics clearly imply
   otherwise — **left open, not decided, by the Owner's own instruction.**
7. Ambiguous cases must not be silently decided.

## 6. Relationship to Strategy B — and to `AR-01`

**Inherited from Strategy B (§4.2) unchanged, as proposed:**

- Pure daily drawdown timing; no month-end fallback contemplated (Strategy D is explicitly "derived
  from Strategy B," which has none — see `SD-6` below for why this is recorded as inherited-by-analogy
  rather than stated outright).
- Same 1.0-unit Normal-zone and conceptual 2.0-unit Large-drop-zone entitlement sizes.
- Same annual funding capacity and timing (Invariant 3-class treatment).
- Same `-10%`/`-20%` threshold ownership (§4.0).

**Changed from Strategy B:**

- Strategy B requests its **full** zone-appropriate size (1.0 or 2.0) in a **single** Purchase Request
  at whichever zone is first reached that month (§4.2 table). Strategy D instead proposes an
  **order-dependent, incremental** path: up to 1.0 now, and *conditionally* up to 1.0 more later in the
  same month, **only** if the deterioration is observed strictly after the first acceptance.
- Strategy B is symmetric in zone-arrival order (direct-to-Large-drop and
  Normal-then-Large-drop reach the same 2.0-unit outcome). Strategy D's proposal is explicitly
  **asymmetric**: Normal-then-Large-drop may reach `2.0`; direct-to-Large-drop is **explicitly left
  undecided** (§5 item 6) rather than assumed to also reach `2.0`.

**Relationship to `AR-01` (Monthly Cumulative Allocation Cap):** both proposals describe a
zone-determined **cumulative monthly entitlement** rather than a single fixed-size request, and both
therefore stand as **alternatives to**, not clarifications of, §10/OD-06/Invariant 15 (same-month
escalation exclusion) — exactly as `AR-01.6.2` records for `AR-01`. Strategy D is **narrower** than
`AR-01`'s general entitlement formula: it is a two-step, order-sensitive sequence rather than a
zone-current, order-independent cap, and it explicitly declines to specify direct-to-Large-drop
behavior rather than deriving it from a general formula. **Strategy D is not an instance of `AR-01`,
does not inherit `AR-01`'s open-question resolutions, and `AR-01` remains RECORDED — NOT ADOPTED,
unaffected by this artifact.**

## 7. Known post-result contamination — binding disclosure

> **Strategy D was proposed by the Owner after inspection of the preserved first Mode-P economic
> comparison (`MP-EV`/`MP-EV2`, commits `00b2b4a`/`e475717`). Its design was motivated specifically
> by Strategy B's observed accumulation of undeployed funding on the released NDXJPY window
> (`2018-01-02`→`2020-06-26`). That window is therefore hypothesis-generating data for Strategy D,
> not independent evidence, and cannot serve as independent validation of Strategy D.**

Consequences, permanent and non-negotiable:

- Strategy D **fails** the anti-hindsight test `AR-01` satisfies. It must never be described as
  pre-registered, and this artifact's own existence is the proof of the opposite.
- **Every future artifact that reports, discusses, or evaluates Strategy D on the currently-released
  NDXJPY window MUST restate this disclosure**, exactly as §18.4.7 already requires every future
  qualification artifact to disclose that NDXJPY Mode-P results were known.
- A favorable Strategy-D result on this window, however produced, may **never** be promoted,
  relabelled, or retrospectively presented as independent validation, evidence of superiority, or
  support for adopting Strategy D as a Baseline or formal strategy.
- This disclosure obligation applies **regardless of outcome** — a favorable or unfavorable result on
  the seen window is equally hypothesis-generating, never confirmatory.

## 8. Proposed mechanical semantics — formalized, not implemented

| Aspect | Formalization | Basis |
| --- | --- | --- |
| Inherited mechanics | Daily observation evaluation (§8); no month-end fallback; `-10%`/`-20%` threshold ownership (§4.0); annual grant/carry-forward (§11.1); zero-yield unused cash (§11.3) | §5 items 1–2; Strategy B analogy |
| Monthly allocation limit | **Changed from** §10's strict one-committed-allocation-per-month: up to **two** committed allocations possible in one calendar month, each `1.0` unit, under the conditions in §5 items 3–4 | §5 items 3–5; contradicts §10/OD-06/Invariant 15 exactly as `AR-01` does (§6 above) |
| Annual funding treatment | Unchanged; identical capacity and timing to A/B/C | §5 item 1 |
| "Accepted" for purposes of enabling the top-up | Read as **Allocation Commitment / Unit Reservation** (§3, §12.2) — the Owner's own wording ("after that first allocation has been accepted") maps directly onto the state model's "Commitment" state, not "Execution." This is a genuine improvement in precision over `AR-01`'s E-1, whose "executed" wording created a blocking ambiguity `AR-01` never resolved. | §5 item 4, read against §3/§12.2 |
| Trigger ordering within a month | Necessarily across **different trading days** — each day yields one decision at one confirmed close (§8), so "after acceptance" can only mean a later trading day's Large-drop reading, never same-day resequencing | §3, §8 |
| Reservation/accounting treatment | **Open** — see `SD-3` | — |
| Execution timing | Inherited: execution occurs at each allocation's own applicable valuation, independently, following §12.3 | §12.3 (unchanged as proposed) |

## 9. Open semantics — recorded as OPEN, not decided

**None of the following is decided here. Choosing an implementation-convenient reading for any of them
is exactly what this artifact exists to prevent.**

| # | Open question | Blocking for implementation? |
| - | -------------- | :--: |
| **`SD-1`** ⚠ | **Direct-to-Large-drop behavior.** If the month's first qualifying observation is already `DD ≤ -20%`, does Strategy D request `1.0`, `2.0` (matching Strategy B), or `0`? Explicitly left open by the Owner (§5 item 6). | **Yes** |
| **`SD-2`** | **Repeated Normal-zone signals after the first.** If a second, third, … trading day in the same month is Normal-zone but not Large-drop, does anything further fire? No text addresses this; the safest non-inferred reading is "no" (matching existing monthly-exclusivity suppression), but that reading is **not adopted here**. | Yes |
| **`SD-3`** | **Accounting model for the top-up.** Is it a **second, separate committed allocation** (changing the meaning of "allocations_committed" / Invariant-9-style counts and `M-1`'s "number of purchases") or an **upward revision of the same allocation** (conflicting with §12.2/§12.4, both written for one acceptance event)? Directly analogous to `AR-01`'s `E-6`. | Yes |
| **`SD-4`** | **Capping interaction.** If the first `1.0`-unit request is capped below `1.0` by insufficient available annual budget (§12.4), does that still count as "accepted" for purposes of enabling the second request, and against what base is the second request sized? | Yes |
| **`SD-5`** | **Budget-exhaustion / zero-unit acceptance for the second stage.** If available budget reaches zero between the first acceptance and the Large-drop deterioration, is a `0`-unit second acceptance recorded (and does it count as a committed allocation, per §12.7's still-open reasoning for the frozen Baseline, which does not automatically transfer — see `AR-01` `E-15`)? | Yes |
| **`SD-6`** | **Month-end fallback.** Strategy D is described as "derived from Strategy B," which has none (§4.2). Nothing explicitly states Strategy D has no fallback; it is only inferred by analogy. | No (recording), yes (implementation) |
| **`SD-7`** | **Cross-month execution interaction with the top-up gate.** If the first allocation's *execution* (not commitment) lands in a later month, does that affect eligibility for a same-month top-up decided while execution is still pending? Given the top-up gate is keyed to *acceptance* (§8 above), this is likely unaffected — but is **not decided here**. | Yes |
| **`SD-8`** | **Evidentiary-record and reason-code extension.** No existing event type distinguishes a "top-up commitment" from an independent first commitment or from existing monthly-exclusivity suppression. §5.1/`M-1`/`M-6`-class work would be required. | Yes |
| **`SD-9`** | **Strategy identity.** Resolved by construction: the Owner named it "Strategy D," a new identifier alongside unchanged A/B/C, never a redefinition of B — satisfying `AR-01.9.3`'s "separate strategy identity" contamination control by default. | No — resolved |
| **`SD-10`** | **Boundary-ownership/tolerance treatment.** Inherited unchanged from §4.0 by §5 item 2; if ever implemented in Mode P, `MP-R-01`'s exact-scaled-comparison convention would apply identically, resolving no additional tolerance question. | No — resolved |

`SD-1` is the single most consequential open item: it determines whether Strategy D's maximum monthly
allocation is symmetric or asymmetric with Strategy B's, and no default may be inferred.

## 10. What this hypothesis does NOT establish

Recording Strategy D does **not**:

- adopt it, or express intent to adopt it;
- approve it as a strategy rule;
- authorize its implementation, in code or otherwise;
- authorize any backtest, simulation, or hypothetical evaluation of it;
- authorize evaluating it inside the currently-released NDXJPY window or any other dataset;
- modify Baseline v2, any Owner Decision, or any Baseline Invariant;
- modify, expand, or resolve `S-3` (§19.3) or `AR-01`;
- resolve any `SD-n` open question;
- change any `P1-x`, `M-x`, `O-4`, `HG-8`, Primary Proxy, Stage G, Stage H, or Phase-2 state;
- assert that Strategy D is superior, equivalent, or inferior to A, B, or C;
- assert that Strategy B's behavior is a defect, an oversight, or in need of correction — §10's
  same-month exclusion was a **deliberate** Baseline choice (§10, worked example under OD-06), and
  Strategy D is recorded as an alternative to it, not a fix for it.

## 11. Requirements before implementation

All of the following, in addition to normal engineering practice:

1. A separate Owner Decision resolving at minimum the **blocking** items in §9 (`SD-1` through
   `SD-5`, `SD-7`, `SD-8`) — mirroring how `AR-01`'s `E-1`/`E-10` were flagged as blocking and left
   unresolved.
2. Explicit Owner authorization to extend `engine.py`'s `SUPPORTED_STRATEGIES` — the engine currently
   implements only `("A", "B", "C")`, and `engine.py`'s own preserved header states that
   implementation evolution is permitted only "to extend the engine to another **already-authorized**
   strategy." Strategy D is not yet authorized.
3. A manifest label of **`EXPERIMENTAL VARIANT — NOT BASELINE`** on every future run touching Strategy
   D, per §18.4.5, in addition to the standing `MP-D3`/`MP-EV-D3`-class labels and the §7 contamination
   disclosure above.
4. All four preserved regression suites (E1–E4, Mode-P DATA-READY) must continue to pass unchanged;
   Strategy A/B/C mechanics and outputs must not shift by one bit.
5. If implementation ever occurs, it happens strictly inside the Simulation Trial lane (Mode E first,
   for mechanical validation on synthetic data, then Mode P) — never Phase 2, which remains BLOCKED.

## 12. Requirements before any independent evaluation

Distinct from, and strictly additional to, §11:

1. A dataset window Strategy D has **never been run against**, frozen (hashed, dated, boundaries fixed)
   **before** Strategy D is executed on it.
2. That freeze must occur under its own bounded acquisition/release authorization, following the exact
   precedent this repository already used for the NDXJPY release (`73d6f51`) — not reused informally.
3. Metrics and reporting boundary fixed **before** any Strategy-D result on that window is inspected
   (Invariant 17 / §13.6 discipline, applied by analogy even though Strategy D is Simulation-Trial-only
   and not Phase-2 evidence).
4. Every resulting artifact restates the §7 contamination disclosure and additionally states that this
   *second* window was genuinely unseen by Strategy D at the time of its design.
5. Even a favorable out-of-sample result remains **NON-FORMAL — SIMULATION TRIAL** and does not by
   itself authorize Phase 2, a Baseline amendment, or adoption of Strategy D.

## 13. Independent-validation path — proposed, not executed

### Stage D-H0 — hypothesis-generation window (the already-released NDXJPY span)

**Permitted uses**, once Strategy D is eventually implemented under §11: mechanical debugging;
comparing event ordering and accounting identities against A/B/C on already-understood data; confirming
`SD-3`/`SD-4`/`SD-8`-class implementation choices behave as specified; regression-style sanity checks.

**Prohibited use, absolutely and permanently**: citing any Stage D-H0 result as evidence that Strategy D
performs better, worse, or differently than A/B/C in any generalizable sense. It is seen data with
respect to Strategy D by construction (§7).

### Stage D-H1 — independent evaluation (not selected, not retrieved, not begun here)

A genuinely unseen window would need to satisfy, at minimum: (a) not previously inspected by any Mode-P
run involving Strategy D; (b) frozen before Strategy D is executed against it, under its own bounded
release authorization; (c) sufficient span for the same engine-state coverage purpose Mode-P already
requires (`MP-P-D1`-class reasoning) — **not** selected for drawdown richness, and **not** derived by
inspecting Strategy D's behavior first.

**Whether such a window would need to be `P1-5`/`P1-6`-derived is deliberately left unaddressed here.**
A *provisional*, Mode-P-scoped second window, selected and frozen the same way the NDXJPY window was
(source-selection policy, ledger, bounded release), would plausibly suffice for a provisional
out-of-sample *comparison inside Mode P*, subject to all of the same anti-contamination and
non-promotion rules — but this is recorded as a **possibility to be decided later**, not a derivation of
`P1-5`/`P1-6`, and not a commitment to any specific dataset, source, or span. No dataset is proposed,
selected, or retrieved by this artifact.

## 14. Qualification-state preservation

Unchanged by this artifact: `O4-PARTIAL ×3` · `GAP-A ×3` · `GAP-B ×2` · `HG-8 NOT EVALUABLE ×3` ·
`P1-2 OPEN` · `P1-5 OPEN` · `P1-6 OPEN` · `H-1 NOT ESTABLISHED` · `P1-9 PARTIAL` ·
`C-1 ×3 QUALIFICATION INCOMPLETE` · **no Primary Proxy** · Stage G **OPEN** · Stage H **NOT BEGUN** ·
Phase 2 **BLOCKED** · all `M-1…M-8` unresolved · `AR-01` unaffected, still RECORDED — NOT ADOPTED · the
Frozen Baseline, `experiment_spec_v2.md`, and the criteria freeze `1e8bc85` **not altered**. No
preserved `MP-H1`/`MP-H2`/`MP-EV`/`MP-EV2` evidence is touched by this artifact.

## 15. Promotion / interpretation barrier

> **An old Stage D-H0 result is never promoted. Strategy D reaching Phase 2, Baseline-candidate status,
> or any formal claim requires, at minimum, a fresh Stage D-H1 independent evaluation under its own
> bounded authorization — never a relabelling of Stage D-H0 output**, mirroring §18.4.4's promotion
> barrier for the existing Simulation Trial lane exactly.

No governed economic metric beyond what `MP-EV-D3` already permits may ever be computed for Strategy D
without its own separate Owner Decision extending that boundary the same way `MP-EV-D1`…`D4` extended
`MP-D3`.

---

**End of entry. Status: REGISTERED — OWNER-GENERATED POST-RESULT ALTERNATIVE HYPOTHESIS. NOT ADOPTED,
NOT VALIDATED, NOT AUTHORIZED FOR IMPLEMENTATION OR EVALUATION. Registered by Owner approval
2026-08-14, after the preserved Mode-P economic comparison existed. The Frozen Baseline and `AR-01`
are unchanged.**
