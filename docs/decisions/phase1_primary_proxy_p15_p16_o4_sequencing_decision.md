# Phase 1 Primary Proxy Qualification — `P1-5` / `P1-6` / `O-4` Sequencing and Research-Span Owner Decision

**Status:** APPROVED — sequencing and research-span boundary recorded

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Disposition of ambiguities `A-1 … A-6`; the operational split of `P1-5` into rule and derived date; the `R-1 … R-4` exhaustiveness question; the semantics of a bounded `O-4` research span; and the separation of any `O-4` Research Cutoff from `P1-6` |
| Decision status | **APPROVED** |
| Owner dispositions recorded | `OD-P15-01` … `OD-P15-06` |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Controlling Frozen Baseline authority | [`../experiment_spec.md`](../experiment_spec.md) §6 (look-ahead prohibition), §7 (Drawdown Reference High), §14.6 / OD-12 (Baseline period and dataset cutoff), §17 Invariant 17, §19.1 |
| Related Owner Decisions | **D-6**, **D-8**, **D-10** (Stage D); Stage-G authorization semantics; [`…hg6_capability_interpretation_decision.md`](phase1_primary_proxy_hg6_capability_interpretation_decision.md); [`…sc6_post_base_segment_interpretation_decision.md`](phase1_primary_proxy_sc6_post_base_segment_interpretation_decision.md); [`…hg9_revision_restatement_decision.md`](phase1_primary_proxy_hg9_revision_restatement_decision.md); [`…stage_g_bounded_reapplication_decision.md`](phase1_primary_proxy_stage_g_bounded_reapplication_decision.md) — **all unchanged** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| `R-1 … R-4` finding | **Interpretation B — illustrative candidate principles**, offered under a broader already-frozen Owner power |
| `P1-5` | **OPEN** — interpretation clarified; **rule not selected; date NOT YET DERIVED** |
| `P1-6` | **OPEN** — no Baseline Dataset Cutoff selected |
| `O-4` | **OPEN** — no methodology research performed or authorized by this decision |
| `HG-8` | **NOT EVALUABLE** ×3 — not reapplied |
| `OJ-1` | **NOT REACHED — DEFERRED**; **not exercised** |
| Candidate classification | **QUALIFICATION INCOMPLETE** ×3 — unchanged |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage G | **OPEN** — this is not a Stage-G artifact and not a Stage-G closure |
| Stage H | **NOT BEGUN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision** recording sequencing semantics and a research-span boundary. It
is an interpretation of existing requirements, not evidence, not a gate result, and not a stage
result. **No external research was authorized or performed.**

> **It is NOT a modification of the Phase-0 Baseline, and NOT a modification of the frozen
> qualification criteria.**

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and
`1e8bc85` remains the criteria-freeze boundary.

This decision contains **no Baseline result, no performance claim, no historical value, no selected
date, and no selected start-date rule.**

---

## 2. Problem statement

`HG-8` is the sole remaining qualification-blocking gate for the three C-1 candidates. Its root
cause is `O-4` — no methodology version history or publisher change log has been located, despite
Stage-D authorization D-2 to retrieve one.

`HG-8` is written span-relative: *no methodology break across the **intended span**, or every break
dated and documented*. The intended span is bounded below by the Baseline measured-performance start
(`P1-5`, extended backward by any warm-up actually used) and above by the Baseline Dataset Cutoff
(`P1-6`). Both remain **OPEN**. A bounded `O-4` authorization therefore cannot be written without
first settling what bounds it.

The repository-only reconstruction that preceded this decision identified six ambiguities blocking
that step:

| # | Ambiguity |
| - | --------- |
| `A-1` | Whether any part of `P1-5` can be decided before `P1-2` |
| `A-2` | That rule `R-2`'s required input is `O-4`'s output — a circularity |
| `A-3` | Whether deciding `P1-5` / `P1-6` for C-1 prejudges C-2A |
| `A-4` | Whether `R-1 … R-4` is an exhaustive normative choice set — the criteria-freeze question |
| `A-5` | Whether `P1-6` must be fixed before `O-4`, or a research ceiling suffices |
| `A-6` | Whether the base-date-onward floor is established at observation level |

This decision disposes of all six. **It does not resolve `P1-5`, `P1-6`, `O-4`, or `HG-8`.**

---

## 3. Authority hierarchy

Applied in this order, highest first:

| Rank | Authority | Bearing here |
| ---- | --------- | ------------ |
| 1 | **Frozen Phase-0 Baseline** — `../experiment_spec.md` | §14.6 / OD-12 create `P1-5` and `P1-6` and state their substantive requirements; §6 and §7 bound look-ahead and the Reference High; Invariant 17 forbids retroactive parameter-setting |
| 2 | **OD-01 … OD-14** — `phase0_baseline_decisions.md` | OD-12 supplies the "longest defensible continuous history" standard and the anti-cherry-picking rationale; OD-14 fixes partial-first-year funding |
| 3 | **Frozen qualification criteria** — criteria freeze `1e8bc85` | `HG-8`'s span-relative wording; `AC-1`, `AC-4`, `AC-5`; `SC-17`, `SC-18`, `SC-19`; `OJ-1` |
| 4 | **Committed Phase-1 Owner Decisions** | **D-6** (pre-base-date exclusion), **D-8** (no live-start inference), **D-10** (OD-12 evidentiary standard), `G-OD-08` (`HG-8` documentary standard), `HG6-OD-03/04` (warm-up permissive), `SC6-OD-03/04/08` (`SC-6` scope), `HG9-OD-07/10` (restatement channels) |
| 5 | **Committed Phase-1 evidence artifacts** | Stage-C `O-4`; Stage-D `H-1 … H-8`, segment maps, warm-up finding; Stage-G bounded reapplication |
| 6 | **This decision** | Sequencing and research-span semantics only |

Where this decision could be read as differing from any higher rank, **the higher rank governs.**

---

## 4. Owner dispositions

### 4.1 `OD-P15-01` — `P1-5` is split into rule and derived date

**ADOPTED.**

`P1-5` is to be understood operationally as two separable acts:

1. an **Owner-selected start-date principle / rule**; and
2. the **exact Baseline measured-performance start date** derived from that rule after the
   Phase-1-approved Primary Proxy is known.

- **The rule MAY be fixed before `P1-2`.**
- **The date MUST NOT be finalized before `P1-2`** where its derivation depends on the identity or
  evidence state of the approved Primary Proxy.

> **This is an interpretation of the existing `P1-5` requirement, not a new criterion.**

**Coexistence verified.** §14.6 binds the history to "the Phase-1-**approved** Primary Proxy" — which
is what makes the *date* proxy-dependent. Frozen study design §10.2 states "The Owner selects a
**principle**; the date follows from it deterministically" — which is what makes the *rule*
proxy-independent. `AC-5` requires the start date to be "derived from a rule, never chosen." The
split is already latent in these texts; recording it required **no change to any normative frozen
text**, so **`SC-18` is not triggered** and no conflict is returned to the Owner.

### 4.2 `OD-P15-02` — `R-2` circularity

**ADOPTED.**

`R-2` — *first date after the last dated methodology change, provided continuity holds thereafter* —
**must not be used to derive the `P1-5` date before `O-4` is completed.** Its required input is the
methodology-chain reconstruction that `O-4` is intended to establish.

If `R-2` remains an available Owner principle, **`O-4` must first be performed under an independently
bounded research scope.**

> **The `O-4` research scope must not be chosen from the outcome of `O-4` itself.**

This is the operative safeguard against the hazard at §11.5. It is recorded here, **before** any
`O-4` research, so that the span is an output of a pre-committed boundary rather than an input tuned
to a known answer — the same `AC-1` discipline followed by the `HG-6`, `SC-6` and `HG-9`
interpretations.

### 4.3 `OD-P15-03` — C-1 must not prejudge C-2A

**ADOPTED.**

- **No C-1-derived calendar date is to be frozen as `P1-5` or `P1-6` before `P1-2`.**
- The start-date **principle** may be fixed now **only if it is genuinely candidate-neutral**.
- The eventual `P1-5` date and `P1-6` apply to the **Phase-1-approved Primary Proxy**, not
  independently to every candidate.

> **Nothing in this decision resolves, constructs, disqualifies, or otherwise changes C-2A.**

C-2A remains an **UNCONSTRUCTED ROUTE** under `G-OD-05`, QUALIFICATION INCOMPLETE, with `O-3`, its
FX leg, and `HG-4` unresolved **by deliberate withholding, not by failure**. `OJ-2` and `OJ-4` are
unexercised and are not reached by this decision.

### 4.4 `OD-P15-04` — `R-1 … R-4` exhaustiveness

**RESOLVED — Interpretation B.** See §5 for the full finding and its evidentiary basis.

### 4.5 `OD-P15-05` — `O-4` may use a separate Research Cutoff

**ADOPTED, coexistence verified.** See §7.

**`P1-6` is NOT required merely to bound `O-4` research.** A separate **`O-4` Research Cutoff** may
be established as a study/research parameter subject to the five conditions at §7.2.

**No `O-4` Research Cutoff is chosen by this decision.** No already-committed repository boundary
determines one mechanically; the smallest defensible alternatives are returned at §7.4 for later
Owner choice.

### 4.6 `OD-P15-06` — Base Value Date as `O-4` scoping floor

**ADOPTED in the narrow sense only.** See §8. Conflict checks against **D-8** and **`SC6-OD-03`**
performed and **no conflict found**.

---

## 5. `R-1 … R-4` exhaustiveness finding

### 5.1 The question

Whether frozen study design §10.2's list is:

- **A** — an exhaustive normative choice set; or
- **B** — illustrative candidate principles under a broader already-frozen rule that the Owner
  selects a defensible principle and the date follows deterministically.

### 5.2 Finding

> **Interpretation B is adopted. It is clearly supported by frozen authority.**

The conclusion does **not** rest on the word "for example" — that phrase does not appear in §10.2 —
but on five independent textual signals in the frozen artifacts themselves.

### 5.3 Basis

| # | Signal | Text |
| - | ------ | ---- |
| 1 | **The heading frames the list as an offer** | §10.2 is titled *"Candidate start-date **rules** to be **offered, not chosen**"*. The study's role is to *offer*; the list constrains the study, not the Owner |
| 2 | **The operative sentence takes a general object** | *"The Owner selects a **principle**; the date follows from it deterministically."* — "a principle", not "one of the above rules" |
| 3 | **Deliberate drafting contrast inside the same frozen artifact** | §6.4 reads *"Every historical segment of every candidate **MUST** be classified into **exactly one of**"*. The drafter demonstrably knew how to write a closed, mandatory set and did so elsewhere. §10.2 carries **no MUST, no "exactly one of", no "only"** |
| 4 | **§14 reserves the power unqualified** | The Owner-only list includes *"choose the Baseline start date"* — with no reference to `R-1 … R-4` and no restriction to them |
| 5 | **`AC-5`'s concern is post-hoc selection, not menu limitation** | *"**Start date derived from a rule, never chosen** — the study hands over facts and **candidate** rules only (§10)"*. Its named failure mode is *"Choosing the start date after seeing strategy performance — OD-12's explicit prohibition"* |

### 5.4 The strongest counter-argument, addressed rather than omitted

Two approved evidence artifacts enumerate `R-1 … R-4` among "the frozen criteria":

> *"The frozen criteria — `HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6`, `SC-1 … SC-20`,
> handoffs `H-1 … H-8` and rules `R-1 … R-4` — are fixed by the study decision…"*

This is **accepted as accurate and is not weakened**: `R-1 … R-4` **are** frozen. But *frozen* and
*exhaustive* are different properties, and the same sentence disambiguates itself:

- It bundles `R-1 … R-4` with **`H-1 … H-8`**, which are *facts to be gathered* — plainly not a
  closed set constraining the Owner's discretion. The sentence therefore means "fixed elements of the
  study design", not "closed normative choice sets".
- `R-1 … R-4` sit in **§10 (P1-5 handoff)**, not in **§5 (Qualification criteria — FROZEN)**. Every
  Owner-Decision coexistence check in this repository recites the criteria register as
  `HG` / `CT` / `ND` / `OJ` / `SC`. **`R-n` appears in none of them.**
- What the freeze secures is the **offer**: the study may not withdraw a rule, add a fifth, or
  re-weight them in order to steer the Owner. That is `AC-1` and `AC-4` doing their work. It is not a
  ceiling on the Owner's own §14 power.

### 5.5 Consequence recorded

> **No new criterion is created by the Owner selecting a start-date principle outside `R-1 … R-4`,
> provided that principle already satisfies the frozen OD-12 / §14.6 requirements.**

Those requirements remain fully binding on any such principle:

1. the **longest defensible continuous history** available from the approved Primary Proxy;
2. **justified by data availability and methodology**;
3. **not selected after inspecting strategy performance**;
4. consistent with §6, §7, and the **D-10** evidentiary standard.

**`R-5` is NOT invented, and no principle is selected.** Nothing in §5 identifies, names, endorses,
or ranks a principle. The finding is one of interpretive scope only.

### 5.6 What would still trigger `SC-18`

`SC-18` **would** fire, and the matter would return to Owner Review, if:

- a proposed principle required adding, removing, weakening, widening, renumbering, or re-weighting
  any `HG`, `CT`, `ND`, `OJ`, `SC` or `AC` item; or
- a proposed principle required amending OD-12, §14.6, §6, §7, or any Frozen Baseline text; or
- `R-1 … R-4` themselves needed to be edited, withdrawn, or extended **within the frozen artifact**.

None of these is required by this decision, and none is performed.

---

## 6. `P1-5` rule / date interpretation

### 6.1 The two components

| Component | Nature | Depends on `P1-2`? | May be fixed now? |
| --------- | ------ | ------------------ | ----------------- |
| **`P1-5` (rule)** | Owner-selected start-date principle | **No** — candidate-neutral by construction | **Yes**, if genuinely candidate-neutral |
| **`P1-5` (date)** | Deterministic derivation of the rule against the approved proxy's evidence | **Yes** | **No** |

### 6.2 Substance of the date

`P1-5` is, in substance, the **measured Baseline performance start**. §14.6 and §7 both define
warm-up by reference to it — *observations preceding the measured performance start* — so it is
distinct from, and later than or equal to, any warm-up start. It is **not** the earliest available
observation, **not** the warm-up start, and **not** the earliest admissible observation, though the
last of these constrains it from below.

### 6.3 State of the four offered rules for C-1, recorded as fact

Recorded from committed evidence, **without selecting among them**:

| Rule | State on the current C-1 record | Source |
| ---- | ------------------------------- | ------ |
| `R-1` | **Not presently applicable** — `H-1` is NOT ESTABLISHED ×3 | Stage-D §11; `SC6-OD-07` |
| `R-2` | Applicable in principle, but **its input is `O-4`'s output** | `OD-P15-02` |
| `R-3` | **Not presently applicable** — no admissible warm-up exists for C-1 at all | Stage-D §12 |
| `R-4` | **Not presently applicable** — the excluded segment is UNCHARACTERIZED, not CHARACTERIZED | Stage-D §7.1; D-6 |

This is a statement about the current evidentiary state, **not** a finding that any rule is invalid,
and **not** a recommendation. Each may become applicable if the underlying evidence changes — `R-1`
if `H-1` is established, `R-3` / `R-4` if `OJ-1` is exercised, `R-2` once `O-4` completes.

### 6.4 Warm-up consequence

Under `HG6-OD-03`, §7 warm-up is **permissive, not mandatory**: *"Absence of admissible pre-start
warm-up history does NOT by itself cause `HG-6` to be NOT EVALUABLE or FAIL."* Where no admissible
warm-up is used, the Reference High initializes from within the measured period, per the frozen
construction.

Two consequences, both recorded without deciding anything:

1. **If no pre-measurement warm-up is used, `O-4` does not need methodology continuity before the
   Baseline start** — no pre-start observation enters the Baseline, and pre-span methodology changes
   cannot affect in-span values.
2. **If optional warm-up is later used, its span becomes part of the methodology-continuity
   requirement** — warm-up observations drive the Reference High and every subsequent drawdown zone,
   and §6 reaches them (study design §6.5; Stage-D §12).

For C-1 the warm-up extension is **presently empty**, because warm-up observations exist only inside
the `SC-6`-excluded segment. It can become non-empty **only** through `OJ-1`, which is not exercised.

> **The Frozen Reference-High rule is unaltered.** `reference_high(t) = max(daily closes available
> through t)` stands exactly as frozen.

### 6.5 `P1-5` is NOT closed

> **`P1-5` remains OPEN.** Its governing interpretation is clarified and its rule-selection boundary
> is clarified. **No rule is selected. No date is derived.**
>
> **Interpretation of `P1-5` must not be represented as completion of `P1-5`.**

---

## 7. `O-4` research-span semantics

### 7.1 The proposition `HG-8` needs established

Recorded so that a later bounded `O-4` authorization has a stated target:

> **For the intended span, the candidate's governing methodology chain is reconstructable: every
> methodology change effective within that span is identified and dated from authoritative
> documentary evidence, or it is authoritatively established that no such change occurred within
> it.**

Three qualifiers from committed authority travel with it:

- **`G-OD-08`** — "dated and documented" does **not** require a publisher-side decision document;
  authoritative issuer or other authoritative primary evidence may establish a change and its date.
  The `N-3` publisher-side provenance gap alone does **not** fail `HG-8`, and `N-3` remains OPEN.
- **`SC-4`** is not triggered where a change is dated; **`SC-3`** still applies if the chain itself is
  not reconstructable.
- **D-10** is the stricter *study-level* OD-12 standard and has **never been declared satisfied** by
  any candidate. `HG-8` is the gate; D-10 is not collapsed into it.

### 7.2 Coverage standard

The span is `[ lower bound , upper bound ]`, closed at both ends, where the lower bound is
`min(P1-5 date, warm-up start)` and the upper bound is the applicable cutoff.

> **The coverage standard is enumerative, not incidental.** A search that returns only
> already-known changes cannot distinguish *no change occurred* from *no change was found*. This is
> the absence-of-evidence / evidence-of-absence line, and it must not be collapsed.

`O-4` must therefore establish either an authoritative enumeration sufficient to determine which
changes fall inside the interval, or an authoritative statement of no change within it.

### 7.3 The `O-4` Research Cutoff — conditions

`P1-6` is **not** required to bound `O-4`. A separate **`O-4` Research Cutoff** may be established
as a study/research parameter, provided **all** of the following hold:

1. it is **named distinctly** from the Baseline Dataset Cutoff;
2. it **expressly does not resolve or modify `P1-6`**;
3. it is **fixed and recorded before `O-4` evidence is compiled**;
4. its justification is **research reproducibility and bounded scope**, never candidate
   qualification outcome;
5. if it **coincides** with another study cutoff or with the eventual `P1-6`, the artifact states
   that **the coincidence carries no normative meaning**.

These mirror the discipline frozen study design §11 already imposes on the Primary Proxy
Qualification Research Cutoff, and the ring-fencing already applied to the two existing study
cutoffs.

### 7.4 No cutoff is chosen — alternatives returned

**No already-committed repository boundary determines an `O-4` Research Cutoff mechanically.** The
two existing study cutoffs are ring-fenced parameters of *other* studies and adopting either would
be borrowing, not derivation. The smallest defensible alternative set is returned for later Owner
choice, **unranked and without recommendation**:

| # | Alternative | Properties |
| - | ----------- | ---------- |
| **K1** | The **date of the bounded `O-4` authorization itself** | Satisfies condition 3 by construction — necessarily fixed before evidence is compiled. Self-documenting. Requires no reference to any other study |
| **K2** | The **current Stage-G evidence boundary** — the date of the committed bounded-reapplication evidence boundary | A committed repository boundary, so reproducible from the repository alone. Does **not** determine itself mechanically; adopting it is still an Owner choice |
| **K3** | An **explicitly stated fixed calendar date** chosen by the Owner independent of both | Maximum Owner control; carries the largest justification burden under condition 4 |

Each would require the condition-5 no-meaning statement if it coincided with `2026-07-31`,
`2026-08-10`, or the eventual `P1-6`.

---

## 8. Base Value Date scoping-floor semantics

### 8.1 The disposition

For **C-1 `O-4` methodology research only**, the published **Base Value Date** may serve as the
**methodology-research scoping floor**, while **D-6 / `SC-6` remain controlling and `OJ-1` remains
unexercised**.

The reason is narrow and entirely derivative: the pre-base-date segment is excluded from measured
performance, from Reference-High warm-up, and from other qualification use under D-6 and §6.4, so no
observation before it can enter the intended span. Methodology changes effective before the floor
cannot affect values inside the span.

### 8.2 What this expressly does NOT establish

- the **first live observation**;
- the **first actual observation**;
- a **launch date**;
- **`H-1`** — which remains **NOT ESTABLISHED**;
- **admissibility of the Base Value Date itself** as measured performance;
- **`P1-5`**;
- **warm-up availability**;
- **full historical admissibility**.

### 8.3 Conflict check — **D-8**

**D-8** holds that the live-start date must **not** be inferred from the Base Value Date, and that
"presumed live" must **not** be upgraded to established LIVE.

> **No conflict.** The floor is derived from the **exclusion boundary** established by D-6, not from
> any inference about live status. It asserts nothing about when the series went live, when it
> launched, or when it was first observed. `H-1` remains NOT ESTABLISHED and the base-date-onward
> segment remains **presumed** live, with presumption expressly not evidence.

### 8.4 Conflict check — **`SC6-OD-03`**

**`SC6-OD-03`** holds that nothing may reopen, weaken, or modify D-6.

> **No conflict.** This disposition **depends on** D-6 remaining fully controlling and is void if D-6
> is ever revisited. It does not un-exclude the pre-base-date segment, does not permit its use for
> any purpose, and does not treat `SC-6` as anything other than the segment-level exclusion D-6
> established.

### 8.5 A precision recorded rather than papered over

The excluded segment's last observation and the published Base Value Date are **distinct dates**, the
former preceding the latter. Setting the floor at the Base Value Date therefore excludes marginally
**more** than D-6 strictly requires, which for the enumeration of dated methodology changes is
immaterial but is recorded so that the two dates are never silently equated.

Separately, and as recorded at `A-6`: because the post-base-date spine was never obtained
(ACCESS-LIMITED), **the first actual post-base observation date is NOT ESTABLISHED for any of the
three C-1 series.** The floor is therefore established at **segment level, not observation level** —
which is sufficient for methodology-chain research, and insufficient for deriving a `P1-5` date.

---

## 9. `P1-6` separation

- **`P1-6` remains OPEN.** No Baseline Dataset Cutoff is selected.
- **No research cutoff may silently become `P1-6`.** This applies to the FX Residual Decomposition
  Research Cutoff, to the Empirical Alignment Study cutoff, to any future `O-4` Research Cutoff, and
  to any retrieval timestamp or publication date.
- `P1-6`'s function is the **reproducibility pin** required by §14.6 / OD-12: once frozen, the
  original Baseline result must remain reproducible against it, and newer observations must not
  silently alter it.
- **`HG-12` PASS does not set `P1-6`.** `HG-12`'s own frozen text records that it is "a capability
  finding only; it does not set P1-6."
- **Full-span retrievability remains unestablished and remains a `P1-6` matter**, exactly as recorded
  in the bounded-reapplication evidence. Capability was demonstrated at minimal scale only.
- Under `HG9-OD-07`, `P1-6` addresses the **forward**-restatement channel and does **not** eliminate
  the separate **backward**-restatement channel; `HG9-OD-10`'s downstream disclosure obligation
  stands and is not designed here.

---

## 10. `OJ-1` preservation

> **`OJ-1` is NOT exercised. It remains NOT REACHED — DEFERRED.**

For the present `O-4` critical path, the **currently controlling D-6 / `SC-6` exclusion is used
exactly as recorded**.

- This is **not a permanent waiver** of `OJ-1`.
- If `OJ-1` is later exercised, any consequence for the historical span, for warm-up availability,
  for the `O-4` scoping floor, or for `HG-8` **must be evaluated separately**.
- The three §6.5 admissibility questions — non-live history for measured performance, for
  Reference-High warm-up only, or for neither — remain open and undecided.
- `SC6-OD-08` is unchanged: the excluded segment is not authorized for measured performance, for
  warm-up, or for any other qualification purpose.

---

## 11. Anti-circularity and criteria-freeze analysis

### 11.1 The five distinctions, applied

| # | Category | Present here? | Assessment |
| - | -------- | ------------- | ---------- |
| 1 | **Interpreting already-frozen `P1-5` semantics** | **Yes** | `OD-P15-01`'s rule/date split is latent in §14.6 and §10.2. Legitimate |
| 2 | **Selecting a previously reserved Owner principle** | **No — not performed** | No principle is selected. §5.5 records only that selection is *not foreclosed*; §6.3 records the applicability state of the four offered rules as fact |
| 3 | **Creating a new criterion after evidence was observed** | **No** | `R-5` is not invented. No `HG` / `CT` / `ND` / `OJ` / `SC` / `AC` item is added, removed, weakened, widened, renumbered, or re-weighted. `R-1 … R-4` are not edited, withdrawn, or extended |
| 4 | **Bounding research for reproducibility** | **Yes** | §7's `O-4` Research Cutoff conditions and §8's scoping floor bound research so a later authorization is finite and reproducible. Legitimate |
| 5 | **Shrinking a qualification span because evidence is difficult to recover** | **No — and expressly guarded** | See §11.5 |

Items 1, 2 and 4 may be legitimate; **items 3 and 5 have not occurred, silently or otherwise.**

### 11.2 Why this is not criterion engineering

Three independent facts:

1. **No performance quantity has ever been computed in this study.** The §7.1 structural guarantee
   holds at every stage; `ND-1 … ND-7` are quarantined and were not used, including in the analysis
   underlying this decision. OD-12's and `SC-17`'s prohibition is specifically about **strategy
   performance**, and none exists to inspect.
2. **The `SC-6` floor was not created to relieve `HG-8`.** D-6 was decided at Stage D on independent
   evidentiary grounds — the absence of segment-specific publisher characterization — and it was
   **adverse to the candidate when made**: it destroyed *all* warm-up availability for C-1 and turned
   the §6.5 hazard from theoretical into concrete. A ruling that worsened the candidate's position
   cannot coherently be recast as engineering in its favour.
3. **The semantics are fixed before the evidence is gathered.** This decision is recorded **before**
   any `O-4` research, in the same `AC-1` posture as the `HG-6`, `SC-6` and `HG-9` interpretations —
   so the span is an output of a pre-committed boundary, not an input fitted to a known answer.

**Recorded against self-interest, because the chronology is not uniformly favourable:** `O-4` was
opened at **Stage C**, *before* D-6 was decided at Stage D. The difficulty of recovering methodology
history was therefore already known when the exclusion was ruled. Fact 2 answers this for D-6 itself,
on the strength of the independent grounds and the adverse effect. **It does not extend to any future
choice**, which is why §11.5 exists.

### 11.3 The `SC-6` floor is a constraint being read out, not a date chosen

The floor at §8 follows deterministically from D-6, `SC-6`, §6.4 and `SC6-OD-03` — all committed
before this question arose. It is **required** on the current record, not merely practical, and it is
reversible only through `OJ-1`, which is preserved unexercised at §10.

> **This is a prior Owner ruling being applied, not a date selected to evade `SC-6`.**

### 11.4 Named-rule evaluation

| Rule | Assessment |
| ---- | ---------- |
| **`AC-1`** — criteria frozen before evidence | **Not violated.** `1e8bc85` intact; no criterion changed; semantics recorded before `O-4` runs |
| **`AC-5`** — start date derived from a rule, never chosen | **Not violated, and reinforced.** No date is derived and no rule is selected. `OD-P15-01` preserves derivation-from-a-rule as the only permitted route; `OD-P15-02` forbids the one route whose input would come from the research it bounds |
| **Invariant 17** — no retroactive optimization presented as pre-specified | **Not triggered now.** No parameter is set. It becomes live the moment `P1-5` or `P1-6` is set, and governs the justification recorded at that time |
| **`SC-17`** — no proxy selected on strategy performance; no `ND-n` as discriminator | **NOT triggered.** No proxy selected; no `ND-n` used or proposed |
| **`SC-18`** — any frozen criterion would need to change after evidence is seen | **NOT triggered.** See §11.6 |
| **`SC-19`** — coverage regression against an approved artifact | **NOT triggered.** No prior finding is narrowed, withdrawn, or downgraded. D-6, D-8, D-10, `HG6-OD-*`, `SC6-OD-*`, `HG9-OD-*` and the bounded-reapplication result are preserved in full |

Also maintained: **`AC-2`** — no performance quantity computed; **`AC-3`** — `ND-1 … ND-7` not used;
**`AC-4`** — the three C-1 candidates treated symmetrically, with no candidate-specific span or rule
proposed; **`AC-6`** — point-in-time discipline preserved, `HG9-OD-10`'s obligation left live;
**`AC-8`** — no scoring, weighting, or ranking, including in the §7.4 alternative set.

### 11.5 The hazard that remains live, named explicitly

> **Illegitimate, and expressly not performed here:** selecting a **later** start date, or an
> **earlier** cutoff, whose operative justification is that it reduces the methodology history that
> must be reconstructed — thereby converting `HG-8` from NOT EVALUABLE to PASS by shrinking the span
> rather than by finding evidence.

Two concrete pressure points exist on the record and are named so they cannot be reached silently:

1. **`R-2`** narrows the span by exactly the amount of methodology history that is hard to recover.
   `OD-P15-02` addresses it directly: `O-4` must be bounded independently first, and **the `O-4`
   research scope must not be chosen from the outcome of `O-4` itself.**
2. **A cutoff earlier than the `N-3` effective date** would place that dated methodology change
   outside the span and remove one documented break from the `HG-8` burden.

Neither is prohibited. **Both require the Owner to record the actual basis for the choice**, so a
later reader can distinguish principle from convenience. This decision does not make either choice.

### 11.6 `SC-18` disposition

**Considered and NOT triggered.**

Recording every disposition above required **no change to any normative frozen text** — not to the
Frozen Baseline, not to OD-01 … OD-14, not to `HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`,
`OJ-1 … OJ-6`, `SC-1 … SC-20`, `AC-1 … AC-8`, and not to `R-1 … R-4` themselves, which are neither
edited nor extended. **Coexistence check performed at each disposition, and no conflict found.**

The conditions that **would** trigger `SC-18` are recorded at §5.6 so the boundary stays visible.

---

## 12. Resulting governance state

| Item | State |
| ---- | ----- |
| **Frozen Phase-0 Baseline** | **UNCHANGED.** OD-01 … OD-14 untouched |
| **Criteria freeze** | **UNCHANGED.** `1e8bc85` remains the boundary |
| `P1-5` | **OPEN** — interpretation clarified; **rule NOT selected; date NOT YET DERIVED** |
| `P1-6` | **OPEN** — no Baseline Dataset Cutoff selected |
| `O-4` | **OPEN** — no research performed; no research authorized by this decision |
| `O-4` Research Cutoff | **NOT SET** — conditions recorded; alternatives returned |
| `HG-8`, C-1 ×3 | **NOT EVALUABLE** — not reapplied |
| `HG-6`, C-1 ×3 | **PASS** — unchanged |
| `HG-9`, C-1 ×3 | **PASS**, with its recorded limitations — unchanged |
| `HG-12`, C-1 ×3 | **PASS** — unchanged; capability only; full-span retrievability unestablished |
| `HG-11`, C-1 ×3 | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; not PASS; non-eliminating; carried to `OJ-6` — unchanged |
| `H-1` | **NOT ESTABLISHED** — unchanged |
| `OJ-1` | **NOT REACHED — DEFERRED**; **not exercised** |
| `OJ-2`, `OJ-4`, `OJ-6` | **Unexercised** |
| `P1-9` | **PARTIAL** — unchanged |
| C-1 classification | **QUALIFICATION INCOMPLETE** ×3. None DISQUALIFIED; none a QUALIFIED SURVIVOR |
| C-2A | **UNCHANGED** in every respect |
| Primary Proxy | **NOT APPROVED — P1-2 remains OPEN** |
| Stage G | **OPEN** — not a Stage-G artifact; not a closure |
| Stage H | **NOT BEGUN** |
| Phase 2 | **BLOCKED** |

---

## 13. What this decision does NOT establish

- **`P1-5`** — not resolved, not closed; **no rule selected, no date derived**.
- **`P1-6`** — not resolved; **no cutoff selected**.
- **`O-4`** — not researched, not resolved, not authorized.
- **An `O-4` Research Cutoff** — not chosen.
- **`HG-8`** — not applied, not reapplied, not satisfied.
- **`H-1`**, first live observation, first actual observation, launch date — none established.
- **`OJ-1`** — not exercised; the excluded segment remains excluded.
- **Warm-up availability** — not established; presently empty for C-1.
- **Full historical-span admissibility** — not established.
- **Point-in-time equivalence** — not established.
- **Full-span retrievability** — not established.
- **A start-date principle** — none selected, endorsed, ranked, or recommended.
- **Candidate qualification, ranking, or Primary Proxy selection** — none.
- **`OJ-6`** — not exercised.
- **Stage-G closure** — not effected.

---

## 14. Next authorized decision boundary

The next step is **an Owner Decision, not research.** Nothing in this artifact authorizes `O-4`.

A bounded `O-4` authorization becomes possible once the Owner:

1. **selects a start-date principle** — from `R-1 … R-4` or, per §5.5, another principle satisfying
   OD-12 / §14.6 — recorded **before** `O-4` runs; and
2. **fixes an `O-4` Research Cutoff** under the §7.3 conditions, from §7.4's alternatives or
   otherwise.

With the floor at §8 and that ceiling, the span is finite and a bounded `O-4` authorization can be
written against the §7.1 proposition and the §7.2 enumerative coverage standard.

The sequence thereafter, subject to separate authorization at each step:

```
bounded O-4 research
  → HG-8 application (explicit Stage-G reapplication authorization required)
  → Stage-G survivor classification (G-OD-14 three-outcome reporting)
  → comparative criteria, ONLY among qualified survivors
  → OJ-6  →  P1-2
  → P1-5 date derived  →  P1-6 fixed
  → final historical retrieval, pinned to P1-6
```

**Zero qualified survivors remains a valid, reportable outcome**, and would itself be materially
useful evidence.

---

## 15. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 untouched; §6, §7, §14.6, Invariant 17
  and the Reference-High construction unaltered.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary. `R-1 … R-4` are neither edited, withdrawn, nor extended.
- **`SC-18` considered and NOT triggered.** No normative frozen text required change.
- **`SC-17` and `SC-19` considered and NOT triggered.**
- **D-6, D-8 and D-10 are unchanged and fully controlling.** Conflict checks against D-8 and
  `SC6-OD-03` performed; **no conflict found**.
- **The `HG-6` capability interpretation, the `SC-6` post-base-date interpretation, the `HG-9`
  decision, the Stage-G authorization semantics, and the bounded Stage-G reapplication are all
  unchanged.** No prior artifact was modified and no history was rewritten.
- **`HG-6` PASS ×3, `HG-9` PASS ×3, `HG-12` PASS ×3 preserved exactly.** `HG-11` preserved exactly as
  BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED: not PASS, non-eliminating, carried to
  `OJ-6`.
- **`HG-8` remains NOT EVALUABLE ×3 and was not reapplied. `O-4` remains OPEN.**
- **`P1-5` remains OPEN. `P1-6` remains OPEN.** No rule selected, no date derived, no cutoff set.
- **`OJ-1` remains NOT REACHED — DEFERRED and was not exercised.**
- **`H-1` remains NOT ESTABLISHED.**
- **All three C-1 candidates remain QUALIFICATION INCOMPLETE.** None DISQUALIFIED; none a QUALIFIED
  SURVIVOR.
- **C-2A is unchanged**, and was neither resolved nor constructed.
- **No Primary Proxy is approved. P1-2 remains OPEN.** `OJ-6` remains Owner-reserved.
- **No external access was performed**, no document retrieved, no observation retrieved, no external
  store inspected for new substantive evidence, and no `O-4` research conducted.
- **No performance quantity was computed.** `ND-1 … ND-7` were not used.
- **No historical value appears in this artifact.**
- **Stage G remains OPEN. Stage H has not begun. Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. `OD-P15-01` … `OD-P15-06` recorded. `R-1 … R-4`: **Interpretation
B** — illustrative, frozen as an offer, not a ceiling on Owner discretion; `SC-18` not triggered;
`R-5` not invented. `P1-5`: **OPEN** — rule/date split recorded, rule NOT selected, date NOT YET
DERIVED. `P1-6`: **OPEN** — no cutoff selected; no research cutoff may silently become it. `O-4`:
**OPEN** — floor and cutoff conditions recorded, research NOT authorized. `HG-8`: **NOT EVALUABLE**
×3. `OJ-1`: **NOT REACHED — DEFERRED**, unexercised. Candidates: **QUALIFICATION INCOMPLETE**. Stage
G: **OPEN**. Primary Proxy: **NOT APPROVED — P1-2 remains OPEN**. Phase 2: **BLOCKED**.**
