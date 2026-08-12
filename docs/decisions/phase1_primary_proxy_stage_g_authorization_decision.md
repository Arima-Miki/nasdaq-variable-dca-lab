# Phase 1 Primary Proxy Qualification — Stage G Authorization Semantics Owner Decision

**Status:** APPROVED — authorization semantics recorded

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Execution semantics for Stage G — hard-gate application: gate-result vocabulary, candidate reporting classes, C-2A entry form, and the disposition of every ambiguity raised in Stage-G authorization preparation |
| Decision status | **APPROVED** |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Preceding evidence boundary | Stage-F closure commit `966c18e8b442dffdd392ff53fa1338673206d227`, tag `phase1-primary-proxy-stage-f-evidence-20260812` |
| Prior stage closures | [Stage C](phase1_primary_proxy_stage_c_closure_decision.md); [Stage D](phase1_primary_proxy_stage_d_closure_decision.md); [Stage E](phase1_primary_proxy_stage_e_closure_decision.md); [Stage F](phase1_primary_proxy_stage_f_closure_decision.md) |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion amended, added, removed, weakened, renumbered, or re-weighted** |
| Stage G | **NOT YET AUTHORIZED TO EXECUTE.** This artifact records the authorization boundary only |
| Stage H | **NOT BEGUN** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision** interpreting the **execution semantics** of an
already-frozen study. It is authorization preparation, not evidence and not a stage result.

> **It is NOT a modification of the Phase-0 Baseline, and NOT a modification of the frozen
> qualification criteria.**

Specifically, this decision does **not**: add a hard gate; remove a hard gate; weaken a hard gate;
change a comparative criterion; change a stop condition; authorize empirical fit analysis;
authorize historical-value retrieval; authorize construction of a C-2 series; select a Primary
Proxy; or amend the Frozen Baseline.

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and
`1e8bc85` remains the criteria-freeze boundary.

This decision contains **no evidence, no gate result, no candidate classification, no Baseline
result, no performance claim, and no historical value.**

---

## 2. Why this artifact exists

Stage-G authorization preparation reconstructed the frozen Stage-G boundary from repository
authority and identified eight points at which the frozen design does not, on its own, determine an
execution rule. Left unresolved, four of them would have made Stage G unable to produce the
per-candidate × per-gate output its own required-evidence column demands, and two of them created a
live risk of a candidate being eliminated by a mechanical reading rather than by evidence.

These decisions resolve those points **without changing what any gate requires**.

---

## 3. Decisions

### 3.1 G-OD-01 — Gate-result vocabulary

**No new generic hard-gate outcome is created.** A generic third outcome such as "conditionally
satisfied", or any equivalent substitute for PASS / FAIL, is **not authorized**. The frozen
PASS / FAIL semantics are unchanged.

Stage G may record three classes of result:

| Class | Meaning |
| ----- | ------- |
| **1. PASS** | Frozen semantics |
| **2. FAIL** | Frozen semantics |
| **3. PRE-EXISTING OWNER-BOUNDED / NON-EVALUABLE STATE** | **Governance metadata** describing why Stage G cannot honestly record PASS or FAIL |

> **Class 3 is not a new frozen gate outcome.** It records the *reason* a gate has no honest
> PASS/FAIL answer, and it must **not** be normalized into either PASS or FAIL.

### 3.2 G-OD-02 — `HG-11` bounded disposition

For **`NDXJPY`**, **`XNDXJPY`** and **`XNDXNNRJPY`**, preserve exactly, under Owner Decision F-11:

> **`HG-11`: BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**

This state **is not PASS**, **is not FAIL**, and is **NON-ELIMINATING** for Stage-G survivor
processing. It must remain visible in every qualification matrix and must be **carried to `OJ-6`**.

Its non-eliminating character is **not a newly invented Stage-G rule**. It is the direct application
of F-11: *UNCLEAR alone shall not mechanically eliminate the candidate at `HG-11`*.

> **F-11 must not be broadened beyond `HG-11`.**

For **C-2A**, preserve:

> **`HG-11`: PARTIAL** — Nasdaq leg **bounded UNCLEAR**; Invesco leg **PERMITTED** for local
> research use; FX leg **NOT YET EVALUABLE**.

C-2A's route-level `HG-11` is therefore **not PASS and not FAIL**, and its unresolved FX leg
**prevents final qualification of the route**.

### 3.3 G-OD-03 — Non-evaluable gate semantics

A gate that cannot be evaluated from the authorized Stage-B through Stage-F evidence is recorded
**NOT EVALUABLE** — or, where an earlier Owner Decision established more specific wording, using
that existing wording.

**NOT EVALUABLE:**

- is **not** PASS;
- is **not** FAIL;
- does **not** mechanically disqualify the candidate;
- does **not** permit the candidate to be declared fully qualified;
- does **not** permit the gate to be skipped;
- does **not** authorize Stage G to gather missing evidence.

A candidate with one or more NOT EVALUABLE hard gates is **QUALIFICATION INCOMPLETE** for Stage-G
completion purposes. It is **not** a failed candidate, and **not** a fully surviving candidate. It
returns to the Owner with the **exact missing evidence or authorization identified**.

> This interpretation does not weaken any hard gate, because **no candidate may receive
> qualification without satisfying every required gate.**

### 3.4 G-OD-04 — Candidate reporting classes

| Class | Definition |
| ----- | ---------- |
| **DISQUALIFIED** | At least one hard gate has an actual **FAIL** |
| **QUALIFICATION INCOMPLETE** | No hard gate has failed, but at least one remains NOT EVALUABLE, PARTIAL, or otherwise unresolved in a manner preventing full qualification |
| **QUALIFIED SURVIVOR** | Every hard gate required for the candidate is resolved sufficiently under the Frozen Baseline and applicable Owner Decisions, with **no FAIL** |

The F-11 `HG-11` bounded state is non-eliminating and **may coexist with QUALIFIED SURVIVOR
status**, but must remain **explicitly attached as an Owner condition** and must be carried to
`OJ-6`.

> This is **reporting and governance terminology only. It does not modify §5.1**, under which a
> candidate failing any gate is disqualified.

### 3.5 G-OD-05 — C-2A entry form

C-2A is authorized to **enter Stage G only as an UNCONSTRUCTED ROUTE**.

> **This is NOT authorization under §9.2 to construct a C-2 series.**

Prohibited: selecting a NAV basis; selecting an FX provider, observation time, or alignment
convention; constructing a JPY series; retrieving FX observations; calculating synthetic values;
resolving `O-3`; resolving `N-2`; resolving `OJ-4`.

Stage G may apply **only** those gates evaluable from existing committed evidence without
construction. Every construction-dependent gate that cannot be evaluated is recorded **NOT
EVALUABLE**, or with its existing more-specific Owner state.

> **C-2A is not disqualified merely because construction was deliberately withheld.** But it cannot
> become a fully qualified survivor while required gates remain non-evaluable.

### 3.6 G-OD-06 — `HG-5` evidence application

**No separate evidence-producing stage is required** for `HG-5` if information already committed in
Stage-B through Stage-F artifacts suffices to apply the frozen gate. Stage G is authorized to
compare existing committed documentary findings against `HG-5`. **This is criterion application,
not new evidence generation.** Nothing may be retrieved and nothing may be calculated.

**For C-1**, apply `HG-5` using the existing documentary findings concerning single published series
identity; the daily / end-of-day observation basis; embedded FX treatment; and the same-series
Reference High / current-value requirement.

**For C-2A**, do **not** resolve `O-3`. If existing evidence does not establish one observation
basis, record `HG-5` **NOT EVALUABLE**.

> **Do not infer FAIL merely from `O-3` being open.**

### 3.7 G-OD-07 — `HG-13` evidence application

Stage G is authorized to perform the documentary consistency comparison `HG-13` requires — the
existing forced-assumption inventory against Frozen Baseline §§4–17. **This is application of an
existing frozen criterion to existing evidence, not new evidence generation.**

**For C-1**, if the existing committed inventory is complete and contains no researcher-selected
forced assumption, apply `HG-13` directly.

**For C-2A**, do **not** invent the missing construction assumptions. If the inventory cannot be
completed without resolving the currently unauthorized C-2 construction choices, record `HG-13`
**NOT EVALUABLE**.

> **Do not convert incompleteness into FAIL.** If an *actually identified* assumption conflicts with
> the Frozen Baseline, **`SC-9` applies normally**.

### 3.8 G-OD-08 — `HG-8` documentary standard

For `HG-8`, "**dated and documented**" does **not** require that every historical methodology change
be documented by a **publisher-side decision document**, unless the Frozen Baseline explicitly says
so. Primary documentary evidence from an authoritative issuer or other authoritative party may
establish that a change occurred and its effective date.

> Therefore the recorded **`N-3` publisher-side provenance gap does not, by itself, cause `HG-8` to
> FAIL.**

`N-3` **remains OPEN**. The provenance gap must **not** be erased or downgraded, and it must **not**
be stated that publisher-side evidence exists where it does not. This decision is **not** generalized
beyond `HG-8`'s requirement.

**`SC-4` is not triggered where the change is dated. `SC-3` still applies if the methodology chain
itself is not reconstructable.**

### 3.9 G-OD-09 — `SC-6` scope

**Owner Decision D-6 is preserved. `SC-6` is a SEGMENT-LEVEL exclusion.** It is **not** in itself an
`HG-6` failure, an `HG-12` failure, or a candidate-level failure.

> **Stage G must not transform the existence of an excluded segment into a hard-gate failure.**

However, if exclusion of that segment leaves insufficient admissible evidence to establish `HG-6` or
`HG-12`, the affected gate is recorded **NOT EVALUABLE** — unless the frozen gate independently
supplies a FAIL condition that is actually met. The capability limitation is recorded explicitly,
and **excluded observations are not used**.

### 3.10 G-OD-10 — `HG-12` pinning standard

For this study, `HG-12` requires reproducible pinning **supportable by the project's authorized
evidence and access state**. The mere theoretical existence of publisher-side observations is not by
itself sufficient.

> **ACCESS-LIMITED does not automatically equal FAIL.**

| If committed evidence establishes… | Then |
| ---------------------------------- | ---- |
| reproducible pinning despite limited access | `HG-12` **may PASS** |
| that reproducible pinning is impossible | `HG-12` **may FAIL** |
| neither proposition | record **NOT EVALUABLE** |

No additional observations and no entitlement-gated material may be retrieved in Stage G. **`H-1`
remains NOT ESTABLISHED** unless existing evidence establishes otherwise.

### 3.11 G-OD-11 — Documentary arithmetic

**Owner Decision E-5 is NOT generalized into a Stage-G calculation authorization.** Stage G remains
documentary and application-only. No arithmetic may be performed unless the frozen gate can be
applied without creating a new empirical quantity.

No Stage-G task presently requires arithmetic. **If arithmetic appears necessary to decide a gate:
STOP for Owner Review.**

### 3.12 G-OD-12 — `OJ-4` timing

`OJ-4` is **not** reached merely because C-2A enters Stage G. It becomes operative **only** if C-2A
reaches the post-hard-gate survivor / selection boundary at which occupying the Primary Proxy role
becomes a live possibility.

> **Do not resolve `OJ-4` during ordinary hard-gate application.**

### 3.13 G-OD-13 — Stage-G evidence boundary

> **Stage G is APPLICATION-ONLY.** It may use only evidence already authorized and recorded through
> Stage F.

Stage G may **not**: browse the web; retrieve external documents; retrieve historical values;
inspect external stores for new substantive evidence; acquire date spines, index observations, NAV
observations, or FX observations; construct any candidate series; calculate returns, drawdowns,
volatility, tracking error, RMSE, MAE, correlation, or regression; compare empirical levels; use
strategy outcomes; or use `ND-1 … ND-7`.

**If a gate cannot be resolved without any of those actions: record it NOT EVALUABLE and return it
to the Owner.**

### 3.14 G-OD-14 — Stage-G completion semantics

Stage G may complete its **application pass** even if some candidates are QUALIFICATION INCOMPLETE.
**It does not need to manufacture PASS / FAIL outcomes where evidence does not support them.**

The completion report must classify **every** candidate as exactly one of QUALIFIED SURVIVOR,
DISQUALIFIED, or QUALIFICATION INCOMPLETE, and must provide the complete per-gate matrix.

| Outcome | Required treatment |
| ------- | ------------------ |
| **Zero QUALIFIED SURVIVORS** | Report explicitly. **Do not rescue a candidate. Do not modify a criterion. Do not authorize Phase 2** |
| **Multiple QUALIFIED SURVIVORS** | Apply the frozen comparative criteria **only among those qualified survivors**. A QUALIFICATION INCOMPLETE candidate must **not** be compared as though it survived |
| **Zero qualified, one or more incomplete** | Report: **"NO CURRENTLY QUALIFIED PRIMARY-PROXY CANDIDATE; ONE OR MORE CANDIDATES REMAIN QUALIFICATION-INCOMPLETE."** This is **not** the same result as all candidates being disqualified |

### 3.15 G-OD-15 — Owner gate

**Stage G remains Owner-gated**, as the frozen design itself requires. Stage G may produce **proposed**
gate findings and candidate classifications; those findings do **not** become the final P1-2 decision
automatically.

After Stage-G execution: **STOP for Owner Review.** Do **not** exercise `OJ-6`, do **not** approve a
Primary Proxy, do **not** begin Stage H, and do **not** begin Phase 2.

---

## 4. Disposition of the authorization-preparation ambiguities

| # | Ambiguity | Disposition |
| - | --------- | ----------- |
| **A-1** | `HG-11`'s bounded state has no PASS/FAIL slot under §5.1 | **G-OD-01 + G-OD-02.** The proposed generic "conditionally satisfied" outcome was **declined**. Instead the pre-existing F-11 state is preserved verbatim as Class-3 governance metadata, is non-eliminating, and may coexist with QUALIFIED SURVIVOR status while remaining attached as an Owner condition carried to `OJ-6` |
| **A-2** | C-2A's §9.2 construction authorization was never given | **G-OD-05.** C-2A enters Stage G as an **UNCONSTRUCTED ROUTE**; this is expressly **not** §9.2 authorization; construction-dependent gates are recorded NOT EVALUABLE; withholding construction is **not** a disqualification |
| **A-3** | `HG-5` and `HG-13` have no evidence-producing stage | **G-OD-06 + G-OD-07.** No new stage is required. Stage G applies both gates to evidence already committed through Stage F, as criterion application rather than evidence generation |
| **A-4** | Whether `HG-8`'s "dated and documented" requires publisher-side documentation | **G-OD-08.** It does not. Authoritative issuer evidence may establish the change and its date; the `N-3` gap alone does not fail `HG-8`; `N-3` remains OPEN; `SC-4` not triggered; `SC-3` still applies |
| **A-5** | Disposition of a non-evaluable gate | **G-OD-03 + G-OD-04.** Recorded NOT EVALUABLE; candidate classified QUALIFICATION INCOMPLETE; returns to the Owner with the exact missing evidence or authorization identified |
| **A-6** | Whether E-5's documentary arithmetic carries to Stage G | **G-OD-11.** It does not. Stage G is documentary and application-only; if arithmetic appears necessary, STOP |
| **A-7** | `SC-6`'s reach into `HG-6` and `HG-12` | **G-OD-09.** `SC-6` remains segment-level and is not itself a gate failure; where exclusion leaves insufficient admissible evidence, the gate is NOT EVALUABLE rather than FAIL |
| **A-8** | Whether `HG-12` "pinnable" is a property of the series or of this project's access | **G-OD-10.** Pinning must be supportable by the project's authorized evidence and access state; ACCESS-LIMITED does not automatically equal FAIL; three-way PASS / FAIL / NOT EVALUABLE treatment applies |

---

## 5. What this decision does NOT do

- It does **not** authorize Stage G to execute. **Stage G remains NOT YET AUTHORIZED.**
- It does **not** add, remove, weaken, or reinterpret the requirement of any hard gate.
- It does **not** change any comparative criterion, stop condition, Owner Judgment, or
  anti-circularity rule.
- It does **not** authorize empirical fit analysis, historical-value retrieval, or any calculation.
- It does **not** authorize construction of a C-2 series, and is **not** the §9.2 authorization.
- It does **not** resolve `O-3`, `N-2` continuity, `N-3`, `N-4`, `OJ-1`, `OJ-3`, `OJ-4`, or `P1-8`.
- It does **not** broaden F-11 beyond `HG-11`.
- It does **not** select a Primary Proxy, exercise `OJ-6`, or unblock Phase 2.
- It does **not** authorize Stage H.

---

## 6. Anti-circularity confirmation

- **No performance quantity was computed**, and none may be at Stage G.
- **`ND-1 … ND-7` remain quarantined** and may not be used at Stage G in any way; `SC-17` fires if
  any is proposed as a discriminator.
- **`AC-1` is respected**: these are execution-semantics decisions about how to *record* results,
  not changes to the criteria, which remain frozen at `1e8bc85`. Any decision that would require a
  criterion to change would trigger `SC-18` and return to the Owner.
- **`AC-4` symmetry**: the reporting classes and gate-result vocabulary apply identically to all
  four candidates.
- **`AC-8`**: no scoring and no weighting is introduced; comparison among qualified survivors
  remains ordinal and reasoned.

---

## 7. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary; **no frozen criterion changed**.
- **Stage G remains application-only.**
- **C-2A's entry is as an unconstructed route only.**
- **No prior Stage-C/D/E/F artifact was modified**, and no history was rewritten.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was evaluated, classified, ranked, or eliminated. No gate was applied.**
- **`OJ-6` remains Owner-reserved.**
- **Stage G has not begun. Stage H has not begun.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Stage-G authorization semantics: RECORDED. Stage G: NOT YET
AUTHORIZED TO EXECUTE. Gate vocabulary: PASS / FAIL / pre-existing Owner-bounded or non-evaluable
state. Candidate classes: QUALIFIED SURVIVOR / DISQUALIFIED / QUALIFICATION INCOMPLETE. C-2A: enters
as an UNCONSTRUCTED ROUTE. `OJ-6`: Owner-reserved. Primary Proxy: NOT APPROVED — P1-2 remains OPEN.
Phase 2: BLOCKED.**
