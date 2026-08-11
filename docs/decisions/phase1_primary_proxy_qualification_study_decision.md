# Phase 1 Primary Proxy Candidate Qualification Study — Owner Decision and Criteria Freeze

**Status:** APPROVED — research authorization and pre-declared qualification criteria

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-11

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** — study authorization **and** criteria freeze |
| Subject | Authorization, scope limits, and pre-declared qualification criteria for the Primary Proxy Candidate Qualification Study |
| Decision status | **APPROVED** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| P1-5 / P1-6 | **OPEN — unchanged by this decision** |
| Pre-launch history admissibility | **UNDECIDED — remains an Owner Decision** |
| Phase 2 | **BLOCKED** |
| Execution authorization | **Stage A may begin only after this artifact is reviewed, accepted, committed, and pushed** |

### 1.1 Artifact role and precedence

This is a **Phase-1 Owner Decision**. It authorizes **one study**, under explicit boundaries, and
freezes the criteria that study must apply.

> **It is NOT a modification of the Phase-0 Baseline, and it is NOT an Evidence Artifact.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and it does not
  create, amend, or supersede any of them.
- The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this
  decision and that specification could be read as differing, **the specification governs
  Baseline behavior**.
- It records **Owner authorization and pre-declared criteria only**. It contains **no empirical
  results**, and no future empirical result may be written into it. Study findings belong in a
  Phase-1 Evidence Artifact produced at Stage H and separately reviewed.
- The preceding Phase-1 Owner Decisions —
  [`phase1_ttm_qualification_decision.md`](phase1_ttm_qualification_decision.md) and
  [`phase1_fx_residual_decomposition_study_decision.md`](phase1_fx_residual_decomposition_study_decision.md)
  — remain in force. This decision neither weakens nor extends their limitations.

### 1.2 Identifier namespaces used in this artifact

Introduced here and scoped to this study:

| Prefix | Meaning |
| ------ | ------- |
| `HG-n` | Hard qualification gate |
| `CT-n` | Comparative / tie-breaking criterion |
| `ND-n` | Non-discriminating information |
| `OJ-n` | Owner judgment required |
| `SC-n` | Fail-closed stop condition |

> **Namespace warning.** The three Owner Decisions recorded in §3 are cited as **`S.1`, `S.2`,
> `S.3`** because that is how the Owner issued them, answering the open design questions of the
> approved Research Design. They are **entirely distinct** from the Frozen Baseline's
> **`S-1` … `S-6`** Phase-4 deferred sensitivity questions in
> [`../experiment_spec.md` §19.3](../experiment_spec.md#193-deferred-sensitivity-questions--phase-4).
> The two must never be conflated.

### 1.3 Relationship to the criteria-freeze requirement

The qualification criteria in §5 are **frozen by this artifact**, before any candidate-specific
research finding exists. This is the study's principal anti-circularity mechanism (§7).

- The criteria MUST NOT be added to, widened, narrowed, split, merged, re-weighted, or otherwise
  changed after candidate-specific evidence is seen.
- Any change required after Stage C opens is a **return to the Owner**, recorded as such.
- **No scoring system is created. No numerical weights are assigned.** Qualification is
  fail-closed and per-candidate; comparison among survivors is ordinal and reasoned, never
  arithmetic.

---

## 2. Research objective

> **What candidate construction, if any, can be shown — on documentary, provenance,
> historical-availability, return-composition, currency-treatment, licensing, and reproducibility
> grounds — to satisfy every requirement the Frozen Phase-0 Baseline places on the Primary Proxy,
> such that it may be presented to the Owner for possible approval under P1-2?**

### 2.1 Framing constraints

1. **Empirical return-space ranking is out of scope and is not reopened.** The approved
   [`../evidence/phase1_empirical_alignment_study.md`](../evidence/phase1_empirical_alignment_study.md)
   §9 records that its level-fit ranking sits inside its own measurement noise and "must not be
   acted upon". The approved
   [`../evidence/phase1_fx_residual_decomposition_study.md`](../evidence/phase1_fx_residual_decomposition_study.md)
   Finding 7 records that its work "provides **no basis for ranking them**".
2. **This is a qualification question, not a similarity question.** P1-2 requires an approved
   **Primary Proxy** for a long-history Baseline backtest
   ([`../experiment_spec.md` §14.1](../experiment_spec.md#141-primary-long-history-proxy-candidate)),
   not a reconstruction of Nissay's undisclosed benchmark. Live-product comparison is a separate
   layer under [§14.3](../experiment_spec.md#143-live-product-validation-candidate).
3. **A "no candidate qualifies" outcome is valid and reportable**, consistent with research
   principle 7 and the Baseline's treatment of negative results. It would itself be a useful
   finding: it would show that P1-2 cannot be resolved from currently available sources.

### 2.2 Explicit non-objectives

This study does not approve a Primary Proxy; does not decide pre-launch-history admissibility;
does not choose a Baseline start date or dataset cutoff; does not identify Nissay's benchmark or
FX provider; does not resolve P1-7; does not unblock Phase 2; and does not revisit AR-01, which
is out of scope for this research.

---

## 3. Owner Decisions S.1 – S.3

### S.1 — Publication capability is NOT a Primary Proxy hard gate

**APPROVED.**

The ability to publish raw values, transformed series, or detailed numerical derived results
publicly is **NOT** itself a hard qualification gate for P1-2.

A candidate may remain eligible if:

- it can be used **legitimately for the project's local research purpose**;
- its **methodology and provenance can be documented sufficiently**;
- the research process can be **reproduced to the extent permitted** by the applicable source
  restrictions;
- any **publication / redistribution restrictions are explicitly preserved**.

Public publication capability may be recorded as a **comparative consideration** (CT-6), a
**reproducibility limitation**, or a **publication-boundary constraint**.

> **It MUST NOT silently become a reason to reject an otherwise methodologically qualified
> candidate.**

Unchanged and still binding: **unknown permission remains UNKNOWN / UNCLEAR**; **technical
accessibility is not evidence of legal permission**; and the project's **conservative fail-closed
publication policy remains in force** for what may be published, as distinct from what may be
qualified.

### S.2 — Documentary research plus limited date-spine metadata is authorized

**APPROVED.**

At the appropriate stages, external research may include:

**A. Documentary / methodology / licensing research.**

**B. Limited date-spine metadata retrieval**, only where necessary to establish historical
availability or continuity. Date-spine metadata means: observation dates; first available date;
last available date; row / observation count; missing-date structure; continuity / gap structure;
identifier continuity; and metadata necessary to distinguish live from pre-launch history.

**This authorization does NOT include empirical value analysis.** It MUST NOT be used to retrieve
or analyse: index levels for performance comparison; returns; fund NAV values for new empirical
comparison; FX values for performance comparison; drawdowns; correlations; regressions; strategy
outcomes; or any information used to rank candidates by historical performance.

> **Minimisation rule.** If a source cannot provide date-spine metadata without also technically
> returning values, **retain the minimum material necessary and do not analyse the values.** The
> retrieval must be recorded, including the fact that values were incidentally returned and were
> not analysed.

Raw and source-derived material MUST remain **structurally outside** the repository — not inside
an ignored repository directory — unless P1-8 later establishes explicit permission.

### S.3 — Limited additional Nissay primary-source research is authorized

**APPROVED, narrowly scoped.**

A bounded primary-source investigation into the meaning of Nissay's 「配当込み」 description is
authorized, where relevant to P1-3 and to Primary Proxy qualification. The objective is to
determine whether **authoritative Nissay material** establishes the return-composition convention
sufficiently to distinguish among concepts such as price return, gross total return, net total
return, notional-net return, or another explicitly defined convention.

Binding limits:

- **Do not infer the answer from empirical fit.** The level-fit and dividend-ratio observations
  in the approved alignment artifact are non-discriminating (ND-1, ND-4).
- **Do not infer the answer merely from the Japanese phrase 「配当込み」.**
- **Do not substitute third-party interpretation for unavailable primary evidence.**
- If reasonable primary-source investigation does not establish the convention, record the result
  as **UNDISCLOSED / NOT ESTABLISHED**.
- **Failure to establish the convention does NOT automatically disqualify any Primary Proxy
  candidate** (see §8.2).
- **This sub-question must not expand into an unbounded research effort.** Its bound is fixed in
  §8.3.

---

## 4. Candidate scope

### 4.1 The candidate set

| ID | Candidate / family | Repository basis | Role in this study |
| -- | ------------------ | ---------------- | ------------------ |
| **C-1** | Nasdaq JPY published index family — `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` | [§14.1](../experiment_spec.md#141-primary-long-history-proxy-candidate) | Qualified as a **family**, then per-series where return composition differs |
| **C-2** | QQQ total-return series combined with an explicitly defined USD/JPY conversion | [§14.2](../experiment_spec.md#142-independent-cross-validation-candidate) | Qualified as a **constructed** candidate; see §9 |
| **C-3** | Nissay NASDAQ100 Index Fund NAV, actual operating period | [§14.3](../experiment_spec.md#143-live-product-validation-candidate) | **Not a Primary Proxy candidate.** Recorded only to document that its exclusion is reasoned: fund inception is structurally incapable of supplying "longest defensible continuous history" under OD-12 |

Within **C-1**, the three series are carried **symmetrically** at every stage, inheriting the
discipline imposed by
[`phase1_fx_residual_decomposition_study_decision.md`](phase1_fx_residual_decomposition_study_decision.md)
§8.

### 4.2 No unrelated proxy families

**No proxy family outside this set may be introduced** unless evidence demonstrates a specific
need **and** Owner Review occurs first. If Stage D or Stage E disqualifies both C-1 and C-2, the
*need* for an additional family becomes documented evidence for a separate Owner Decision — never
a silent expansion of scope.

### 4.3 Facts to be established per candidate

Publisher / administrator; index or instrument definition; return composition; dividend treatment;
currency treatment; live launch date; earliest available historical observation; whether
pre-launch history exists; how the publisher characterizes any pre-launch history; continuity of
the historical series; methodology-change history; revision / restatement behaviour; licensing and
redistribution constraints; local research usability; reproducibility by a future researcher.

Each recorded fact MUST carry an **evidence class** — PRIMARY / NEAR-PRIMARY / SECONDARY /
UNREAD — using the tiering already established in
[`../evidence/phase1_fx_source_research.md`](../evidence/phase1_fx_source_research.md) §4 and
[`../evidence/phase1_japan_side_ttm_qualification.md`](../evidence/phase1_japan_side_ttm_qualification.md)
§4.

---

## 5. Qualification criteria — FROZEN

**Fixed by this artifact before any candidate-specific finding exists.** Qualification is
fail-closed and per-candidate.

### 5.1 A — HARD QUALIFICATION GATES

A candidate failing any gate is **DISQUALIFIED for the Primary Proxy role**. Failure is recorded
with its evidence; it is not worked around.

| # | Gate | Frozen-Baseline basis |
| - | ---- | --------------------- |
| **HG-1** | **Authoritative methodology documentation exists and is readable.** Publisher-issued, identifiable by title and version, and actually extractable | [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources); README reproducibility requirement |
| **HG-2** | **Stable, unambiguous identifier and series definition**, such that a third party could request the same series by the same identifier | [§7](../experiment_spec.md#7-drawdown-reference-high); README reproducibility |
| **HG-3** | **The candidate's own return composition is documented and determinate** — its return version and dividend-reinvestment assumption stated by its publisher. *This concerns the candidate, not Nissay's benchmark (see §8)* | [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources); OD-11 |
| **HG-4** | **Currency treatment is determinate** — FX either embedded with a documented rate source, observation time, and alignment to the index observation date, or externally specified with all three documented | [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources) currency clause |
| **HG-5** | **Single-series compatibility with §7** — daily closing values on one series and one observation basis; Reference High and current value from that same series; no intraday high required | [§7](../experiment_spec.md#7-drawdown-reference-high); [§4.0](../experiment_spec.md#40-drawdown-zone-semantics) |
| **HG-6** | **Reference High constructible without look-ahead**, from observations available at each simulated date | [§6](../experiment_spec.md#6-look-ahead-prohibition); [§7](../experiment_spec.md#7-drawdown-reference-high) |
| **HG-7** | **Drawdown zones applicable deterministically** from the series alone, subject only to M-7 tolerance methodology | [§4.0](../experiment_spec.md#40-drawdown-zone-semantics); M-7 |
| **HG-8** | **Historical continuity with a reconstructable methodology chain** — either no methodology break across the intended span, or every break dated and documented. *This gate concerns documentation of continuity, not admissibility of any segment (see §6)* | [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources); [§6](../experiment_spec.md#6-look-ahead-prohibition) |
| **HG-9** | **Revision / restatement behaviour established well enough to assess look-ahead.** [§6](../experiment_spec.md#6-look-ahead-prohibition) names "retroactively revised series" as a leak and requires the effect to be *assessed in Phase 1 rather than assumed negligible* | [§6](../experiment_spec.md#6-look-ahead-prohibition); P1-9 |
| **HG-10** | **Embedded return components and expenses documented**, so no cost is double-counted and no tracking difference is assumed | [§14.5](../experiment_spec.md#145-cost-and-expense-treatment) / OD-11 |
| **HG-11** | **Legitimate local research use is supportable, and restrictions are preserved** — see the three-way rule in §5.5. **Publication capability is NOT part of this gate (S.1)** | [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources); P1-8; S.1 |
| **HG-12** | **A fixed dataset cutoff is supportable** — the series can be pinned and the result reproduced against that pin. *A capability finding only; it does not set P1-6* | [§14.6](../experiment_spec.md#146-baseline-period-and-dataset-cutoff) / OD-12 |
| **HG-13** | **No assumption is required that is inconsistent with the Frozen Baseline.** Every assumption the construction forces must be listed and checked against §§4–17 | [§18.2](../experiment_spec.md#182-effect-of-the-freeze); Invariants 1–18 |

### 5.2 B — COMPARATIVE / TIE-BREAKING CRITERIA

Applied **only among candidates that have passed every hard gate**, in the order below. Ordinal
and reasoned; **never used to rescue a failed gate**, and **never converted into a score**.

| # | Criterion | Direction | Basis |
| - | --------- | --------- | ----- |
| **CT-1** | Length of **live** continuous history | Longer preferred | OD-12 "longest defensible continuous history" |
| **CT-2** | Proportion of the intended span that is live rather than non-live | Higher preferred | OD-12 "defensible"; [§6](../experiment_spec.md#6-look-ahead-prohibition) |
| **CT-3** | Number of *additional* assumptions the construction forces on the researcher | Fewer preferred | [§18.2](../experiment_spec.md#182-effect-of-the-freeze); parsimony |
| **CT-4** | Evidence tier of the governing methodology | PRIMARY preferred to NEAR-PRIMARY | Established tiering practice |
| **CT-5** | Clarity of local-research-use permission | PERMITTED preferred to UNCLEAR | P1-8; S.1 |
| **CT-6** | Publication / redistribution capability for derived results | Greater capability preferred, **as a comparative consideration only** | **S.1** |
| **CT-7** | Revision behaviour quality | Documented non-revision > documented mechanism > unknown | [§6](../experiment_spec.md#6-look-ahead-prohibition); P1-9 |
| **CT-8** | Warm-up availability — observations before the intended measured start, usable to seed the Reference High | Available preferred | [§7](../experiment_spec.md#7-drawdown-reference-high) warm-up clause |
| **CT-9** | Future access / maintainability risk | Lower preferred | Precedent recorded in [`../evidence/phase1_fx_source_research.md`](../evidence/phase1_fx_source_research.md) §3.4 |

### 5.3 C — NON-DISCRIMINATING INFORMATION

Recorded in the eventual artifact for completeness; **MUST NOT influence qualification or
ranking**. Any use of these to choose a candidate is a design failure and a stop condition
(SC-17).

| # | Item |
| - | ---- |
| **ND-1** | The alignment study's level-fit ordering, cumulative-return gaps, and annualized tracking differences — inside their own measurement noise by that artifact's own §9 |
| **ND-2** | The alignment study's drawdown-zone agreement percentages — a spread of one date out of the matched set, which that artifact states "must not be read as a ranking" |
| **ND-3** | Identical Large-Drop entry dates and shared maximum-drawdown figures |
| **ND-4** | The candidate-series dividend-reinvestment ratio consistency check, which the alignment artifact §10 states "is NOT identification of Nissay's undisclosed benchmark dividend convention" |
| **ND-5** | Every FX Residual Decomposition finding — the FX differential is candidate-neutral by construction and all arms were run symmetrically (Finding 7) |
| **ND-6** | Any correlation, MAE, RMSE, or tracking-error figure from any completed study |
| **ND-7** | Any quantity derived from strategy behaviour or strategy performance, of any kind, from any source |

### 5.4 D — OWNER JUDGMENT REQUIRED

Facts the study establishes; **choices it does not make**.

| # | Judgment | Why it is the Owner's |
| - | -------- | --------------------- |
| **OJ-1** | Admissibility of pre-launch / non-live history under [§6](../experiment_spec.md#6-look-ahead-prohibition) and OD-12 — for measured performance, for warm-up only, or not at all | Normative interpretation of "defensible"; see §6 |
| **OJ-2** | Whether a shorter fully-live history is preferred to a longer partly-non-live one, where CT-1 and CT-2 conflict | OD-12 balances two properties without ordering them |
| **OJ-3** | The return-version selection principle, if Nissay's convention is recorded UNDISCLOSED / NOT ESTABLISHED (§8.2) | A choice, not a finding |
| **OJ-4** | Whether the C-2 construction's additional obligations are acceptable, and whether QQQ may occupy the Primary Proxy role given the [§14.1](../experiment_spec.md#141-primary-long-history-proxy-candidate) / [§14.2](../experiment_spec.md#142-independent-cross-validation-candidate) role separation | [§14](../experiment_spec.md#14-data-source-role-separation-and-data-requirements) assigns roles |
| **OJ-5** | Whether a candidate whose local-research-use permission is **UNCLEAR but not restricted** may be qualified, and on what bounded terms | Precedent: the bounded MUFG/MURC qualification was an Owner Decision, not a research finding |
| **OJ-6** | Final P1-2 approval, or a recorded finding that no candidate qualifies | [§17](../experiment_spec.md#17-baseline-invariants), [§18.3](../experiment_spec.md#183-relationship-to-phase-1-and-phase-2) — the Owner alone |

### 5.5 The three-way licensing rule for HG-11

Derived from repository precedent, and required because S.1 removes publication from the gate
without removing local-use legitimacy from it.

| Located terms | Effect on HG-11 | Precedent |
| ------------- | --------------- | --------- |
| Local research use is **positively RESTRICTED** | **HG-11 FAILS** — candidate disqualified | Fail-closed policy |
| Terms are **entirely unreadable** (cannot be retrieved at all), so no assessment is possible | **HG-11 CANNOT BE EVIDENCED** → stop condition SC-12; the candidate cannot be qualified — *not because its data is unsuitable, but because its terms are unreadable* | Mizuho: "cannot be qualified — not because its data is unsuitable, but because its terms are unreadable" |
| Terms are **readable but silent** — no grant and no prohibition located | **UNCLEAR — escalates to OJ-5**, not an automatic failure | MURC: no terms page, only a disclaimer; the Owner nonetheless issued a bounded qualification decision |

**Absence of a prohibition is not permission.** **Technical accessibility is not permission**, and
prior successful retrieval is not evidence of permission for further retrieval.

---

## 6. Pre-launch history — decision boundary

### 6.1 The rule that governs this section

> **"Available history" MUST NOT be interpreted as "admissible history."**
>
> **The research does NOT decide that any pre-launch history satisfies OD-12.** Admissibility
> remains an Owner Decision (OJ-1).

### 6.2 What the research may establish

Whether such history exists; how the publisher characterizes it, quoted verbatim; its date range;
methodology continuity with the live period; methodology-change history; provenance; and any
associated warnings or limitations the publisher attaches.

### 6.3 The state of repository knowledge, stated precisely

[`../evidence/phase1_empirical_alignment_study.md`](../evidence/phase1_empirical_alignment_study.md)
§3 records that only live Nasdaq history was used, that no pre-launch back-tested values entered
that study, and that "none were required, since all three series have been live since 2020-06."

Three consequences bind this study:

1. The **live-since date is recorded in passing, without a cited primary source**, in an artifact
   whose own study did not depend on it. [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources)
   states the specification asserts **no** history lengths. It MUST be **re-established from
   primary publisher material** and treated until then as unconfirmed.
2. "No pre-launch values entered this study; none were required" **does not establish that such
   values exist.** Their existence is an open question.
3. Nothing in the repository characterizes what any such values would be.

### 6.4 Mandatory segment classification

Every historical segment of every candidate MUST be classified into exactly one of:

| Class | Meaning | Consequence |
| ----- | ------- | ----------- |
| **LIVE** | Calculated and disseminated in real time; no hindsight available to the calculator | Available for OJ-1 consideration |
| **NON-LIVE, CHARACTERIZED** | Publisher states its existence and nature | Admissibility is **OJ-1** |
| **NON-LIVE, UNCHARACTERIZED** | Values exist but status cannot be established | **SC-6** — that segment may not be used; not a licence to use it cautiously |

### 6.5 The warm-up sub-question, kept separate

[§7](../experiment_spec.md#7-drawdown-reference-high) permits observations preceding the measured
performance start to initialize the Daily Closing ATH as **warm-up data**, excluded from measured
performance. Three admissibility questions therefore exist and MUST be reported separately:
non-live history for **measured performance**; for **Reference High warm-up only**; for
**neither**.

The study MUST surface, without deciding, that these are materially different: a non-live segment
containing a hindsight-influenced peak would seed a Reference High that never actually stood,
affecting every subsequent drawdown zone — a [§6](../experiment_spec.md#6-look-ahead-prohibition)
concern even under warm-up-only use.

### 6.6 The evidence standard for OD-12

The study MUST draft, and put to the Owner, a written standard for what would be required before
a segment counts as "defensible continuous history" under OD-12. **The study does not declare
that standard met.**

---

## 7. Anti-circularity rules

### 7.1 The structural guarantee

> **The study computes no performance quantity of any kind, at any stage.**

No returns, correlations, drawdowns, regressions, tracking errors, or strategy outcomes. Proxy
selection is therefore **structurally incapable** of being influenced by strategy performance —
there is no performance quantity in the study to be influenced by.

**Date-spine metadata authorized under S.2 — observation dates, counts, gap structure — is not a
performance quantity and is not prohibited by this rule.** The distinction is exact: counting
observations is permitted; computing anything from their values is not.

### 7.2 The rules

| # | Rule | Prohibited reasoning it blocks |
| - | ---- | ------------------------------ |
| **AC-1** | **Criteria frozen before evidence** — §5 is fixed by this artifact; any change after Stage C opens returns to the Owner | Retro-fitting criteria to a preferred candidate |
| **AC-2** | **Zero performance computation** (§7.1) | "Best backtest"; "most favourable DCA result"; "drawdowns matched desired behaviour"; "return version producing the closest profitable result" |
| **AC-3** | **Category-C quarantine** — existing empirical results are recorded but formally excluded (ND-1 … ND-7) | Laundering the exhausted level-fit ranking into a "qualification" |
| **AC-4** | **Symmetric candidate handling** — all C-1 series and all C-2 components carried identically through every stage | Silent narrowing to a favourite |
| **AC-5** | **Start date derived from a rule, never chosen** — the study hands over facts and candidate rules only (§10) | Choosing the start date after seeing strategy performance — OD-12's explicit prohibition |
| **AC-6** | **Point-in-time eligibility discipline** — historical eligibility judged on what was true and knowable at the time | [§6](../experiment_spec.md#6-look-ahead-prohibition)'s named leaks: backfilled values, retroactively revised series, survivorship-filtered inputs |
| **AC-7** | **Sequencing gate** — P1-2 is approved before any Phase-2 code exists; [§18.3](../experiment_spec.md#183-relationship-to-phase-1-and-phase-2) already forbids backtest code, methodology code, and data loaders | Post-hoc reselection once results exist |
| **AC-8** | **No scoring, no weights** — comparison among survivors is ordinal and reasoned | A tunable selection surface |

### 7.3 Relationship to later sensitivity work

[§16](../experiment_spec.md#16-no-optimization-before-baseline-evidence) and
[§19.3](../experiment_spec.md#193-deferred-sensitivity-questions--phase-4) permit alternative
proxies, return versions, and start dates to be examined in **Phase 4**, reported separately and
never as Baseline evidence. These rules constrain **Baseline qualification**, not later
sensitivity work; Invariant 17 keeps the two distinct.

---

## 8. P1-3 interaction

### 8.1 The decisive distinction

| | Question | Status | Required for P1-2? |
| --- | -------- | ------ | ------------------ |
| **Q-A** | What is the **candidate's own** return composition, per its publisher? | Establishable | **YES — HG-3** |
| **Q-B** | What does Nissay's 「配当込み」 mean? | Undisclosed in the statutory prospectuses already read | **NO** |

P1-2 requires a defensible long-history proxy for NASDAQ-100 exposure, not a reconstruction of
the Nissay benchmark. Making Q-B a precondition would make P1-2 unresolvable by anything this
project can do if the issuer does not publish it.

### 8.2 Handling an unresolved Q-B

If S.3's bounded investigation does not establish the convention, the result is recorded as
**UNDISCLOSED / NOT ESTABLISHED**, and the study MUST then classify the uncertainty as exactly
one of:

| Classification | Meaning | Consequence |
| -------------- | ------- | ----------- |
| **Prevents qualification** | The uncertainty makes some HG-n gate unevidenceable | Recorded per candidate, with the gate identified |
| **Non-discriminating among candidates** | The uncertainty applies equally to all candidates and separates none | Recorded; qualification proceeds |
| **Requires Owner judgment** | Qualification is possible but the return version must be chosen | Escalates to **OJ-3** |

The study MUST NOT: select a return version by closeness of empirical fit; describe any candidate
as "the benchmark" or "benchmark-equivalent"; or treat the dividend-reinvestment consistency check
as evidence about Nissay (ND-4).

If OJ-3 is reached, the study presents the options and their consequences — for example selecting
a return version on a stated conservative principle fixed **before** any Baseline result exists,
with the alternatives carried to Phase 4 under
[§16](../experiment_spec.md#16-no-optimization-before-baseline-evidence). Choosing on a principle
fixed in advance is anti-circular; choosing on best fit is not. **The Owner decides.**

### 8.3 The bound on S.3 — required, so the sub-question cannot expand

The investigation is bounded by a **closed list of authoritative material classes**, declared
before it begins, and a **stop rule**:

1. The Nissay-issued statutory and periodic disclosure documents for this fund, and Nissay-issued
   material describing the fund's benchmark.
2. The benchmark publisher's own definition of any return version Nissay names explicitly.

**Stop rule.** Once the declared classes have been examined without establishing the convention,
the investigation **STOPS** and the result is recorded as UNDISCLOSED / NOT ESTABLISHED. It is not
extended to third-party interpretation, to inference from the phrase itself, to empirical fit, or
to correspondence with the issuer. Extending beyond the declared classes requires a **new Owner
Decision**.

---

## 9. P1-7 interaction and the QQQ + USD/JPY route

### 9.1 The two routes impose materially different obligations

The completed FX Residual Decomposition Study is **not reopened**. Its result is used only as a
statement about the *magnitude class* of FX-convention risk.

| | **Route 1 — native JPY published index (C-1)** | **Route 2 — USD instrument × separately defined USD/JPY (C-2)** |
| --- | --- | --- |
| Where FX lives | **Embedded** in the published series by the index publisher | **Chosen by the researcher**, applied outside the published series |
| Nature of the P1-7 obligation | **Documentary** — establish what is embedded | **Constitutive** — the researcher must *select* rate source, observation time, and alignment, all three of which [§14.4](../experiment_spec.md#144-phase-1-evidence-approval-status-of-data-sources) requires be established |
| Current repository position | Substantially discharged: the index-side convention is pinned from two primary Nasdaq documents | Not begun; **no Baseline FX convention is approved anywhere in the repository** |
| Residual work | Confirm no NDX currency-version methodology **override** exists — recorded as an open unknown in [`../evidence/phase1_fx_source_research.md`](../evidence/phase1_fx_source_research.md) §8 and "not exhaustively checked" | Full source qualification for the chosen rate, plus a new Owner Decision approving a Baseline FX convention |
| Data-availability exposure | None additional | High — the structurally correct benchmark rate is commercially restricted and unobtainable for this repository, so any chosen rate is an explicit approximation |
| Governance precedent | None required | The FX decomposition decision **did not approve S2** — level-space synthetic JPY construction — and stated it "may be reconsidered only under a **new Owner Review**" |

### 9.2 Reading the S2 precedent precisely

That non-approval was scoped to the FX decomposition study and to a Japan-side-TTM construction,
so it does **not** automatically govern a P1-2 QQQ + USD/JPY construction, which is separately
recorded in the frozen [§14.2](../experiment_spec.md#142-independent-cross-validation-candidate)
and predates it. What it establishes is the project's precedent: **level-space synthetic JPY
construction requires explicit Owner authorization and is never an inherited permission.** Any
C-2 construction therefore requires its own Owner authorization before Stage G.

### 9.3 Prohibited assumptions about C-2

The study MUST NOT assume that longer history makes C-2 superior; that ETF exposure is equivalent
to index exposure; that USD/JPY conversion is trivial; or that C-2 is "merely a fallback". Its
methodological obligations MUST be evaluated explicitly, including at minimum: inception and
history depth from a primary source; conceptual equivalence of the instrument's stated objective
to the index exposure the Baseline specifies; distributions and reinvestment convention; **embedded
fund expenses**, since [§14.5](../experiment_spec.md#145-cost-and-expense-treatment) forbids
deducting costs already inside a series and forbids equating tracking difference with the expense
ratio; corporate-action and adjustment conventions; the USD/JPY leg's full source qualification;
calendar alignment under the existing no-forward-fill / no-interpolation / no-synthesized-observation
discipline; reproducibility; and licensing for **both** publishers independently.

### 9.4 The role-separation consequence, to be recorded

[§14.2](../experiment_spec.md#142-independent-cross-validation-candidate) assigns C-2 the role of
testing "whether findings depend on a single index data source". Promoting it to Primary Proxy
would empty that role and leave the three-layer concept with no independent cross-check. This
consequence MUST be recorded as evidence for **OJ-4**; the study does not resolve it.

---

## 10. P1-5 handoff

**The study does not choose the Baseline start date. P1-5 remains OPEN.**

### 10.1 Facts to be handed over, per candidate

| # | Fact |
| - | ---- |
| **H-1** | Earliest **live** observation date, primary-sourced |
| **H-2** | Earliest **available** observation date of any status |
| **H-3** | Segment map: every segment classified LIVE / NON-LIVE CHARACTERIZED / NON-LIVE UNCHARACTERIZED, with dated boundaries |
| **H-4** | Dated methodology changes across the span |
| **H-5** | Gap and non-trading-day inventory; the publication calendar |
| **H-6** | Warm-up feasibility — whether observations exist before each candidate start, and their class |
| **H-7** | Revision / restatement behaviour and any restatement events in the span |
| **H-8** | Any date-specific data-integrity hazard found, of the class already recorded in prior artifacts |

### 10.2 Candidate start-date **rules** to be offered, not chosen

| # | Rule |
| - | ---- |
| **R-1** | First date on which the approved Primary Proxy is continuously **live** through the intended span |
| **R-2** | First date after the **last dated methodology change**, provided continuity holds thereafter |
| **R-3** | First date after which a defined warm-up window of qualifying observations exists to seed the Reference High |
| **R-4** | If OJ-1 admits non-live history, the earliest **characterized** observation, with the non-live segment reported explicitly alongside the Baseline result |

The Owner selects a **principle**; the date follows from it deterministically.

### 10.3 Boundary note

If the resulting start is not a calendar-year boundary, first-year funding is **already fixed by
OD-14** ([§14.6](../experiment_spec.md#146-baseline-period-and-dataset-cutoff),
[§19.4](../experiment_spec.md#194-conditional-owner-decision-items)) and requires no further Owner
Decision. The partial first measured year must be reported with the Baseline result (Invariant 18).

---

## 11. P1-6 boundary

- **The Baseline Dataset Cutoff is not chosen by this study. P1-6 remains OPEN.**
- Any as-of date needed is named the **Primary Proxy Qualification Research Cutoff**, classified
  as a **research parameter only**, derived from source availability rather than convenience,
  fixed and recorded before evidence is compiled, and applied uniformly.
- The eventual artifact MUST state: **it MUST NOT be called, treated as, or allowed to resolve the
  Baseline Dataset Cutoff.**
- Two research cutoffs already exist in approved artifacts, both similarly ring-fenced. If a third
  coincides in value with either, the artifact MUST state that the coincidence carries no meaning.
- What this study **may** contribute to P1-6 is a **capability finding** under HG-12 — whether a
  candidate can support a fixed cutoff reproducibly — never a cutoff.

---

## 12. Staged research process

Global rules binding on every stage: **no performance quantity is computed at any point**; raw and
source-derived material lives **structurally outside** the repository, not in an ignored
repository directory; frozen criteria may not be changed after Stage C opens; retrieval is limited
to what S.2 authorizes; no credentials are involved.

| Stage | **A — Normative requirement extraction** |
| --- | --- |
| Objective | Convert the Frozen Baseline into an itemized, clause-cited register of binding requirements on the Primary Proxy; instantiate §5.1 against those clauses |
| Allowed | Reading repository documents only |
| Prohibited | Any external access; any candidate-specific judgment |
| Required evidence | A requirement register, each row citing its normative clause |
| Failure | A hard gate cannot be traced to a normative clause → remove it or escalate |
| Owner gate | **Yes** — register reviewed before Stage B |
| External retrieval | **No** |
| Local raw retention | N/A |
| Repository entry | Nothing |

| Stage | **B — Candidate set fixing and identifier disambiguation** |
| --- | --- |
| Objective | Fix the candidate set and establish unambiguous identifiers and series definitions (HG-2) |
| Allowed | Repository reading; publisher identifier and definition documents |
| Prohibited | Adding candidates without documented need and Owner Review; any value retrieval |
| Required evidence | Per-candidate identifier, publisher, definition, with evidence class |
| Failure | Identifier ambiguous or definition unlocatable → HG-2 fails |
| Owner gate | No (reported at C) |
| External retrieval | Documentary only |
| Local raw retention | Documents, outside the repository |
| Repository entry | Nothing |

| Stage | **C — Publisher methodology and provenance discovery** |
| --- | --- |
| Objective | Obtain authoritative methodology for every candidate and component; resolve the outstanding NDX currency-version override question |
| Allowed | Retrieval of publisher methodology documents, versions, change histories |
| Prohibited | Any market-value retrieval; any analysis of values |
| Required evidence | Document title, version, date, host, governing passages quoted verbatim |
| Failure | Methodology unidentifiable or unextractable → HG-1 fails |
| Owner gate | **Yes** — sources, terms handling, and any research cutoff. **Criteria are frozen from this point** |
| External retrieval | **Yes**, documentary |
| Local raw retention | Documents, outside the repository |
| Repository entry | Nothing |

| Stage | **D — History, continuity, and pre-launch qualification** |
| --- | --- |
| Objective | Execute §6 in full: existence, characterization, date range, methodology continuity and change history, provenance, warnings; produce the segment map |
| Allowed | Publisher availability statements; **date-spine metadata retrieval under S.2**, subject to the minimisation rule |
| Prohibited | Value analysis of any kind; inferring status from availability; **any admissibility decision** |
| Required evidence | Segment map with dated boundaries and evidence classes; methodology-change log; gap inventory; record of any incidental value return and non-analysis |
| Failure | NON-LIVE UNCHARACTERIZED → SC-6 for that segment; undocumented methodology break → HG-8 fails |
| Owner gate | **Yes** — OJ-1 is put to the Owner here |
| External retrieval | Yes, restricted as above |
| Local raw retention | Date spines and metadata only, outside the repository |
| Repository entry | Nothing |

| Stage | **E — Return-composition and currency-treatment qualification** |
| --- | --- |
| Objective | HG-3, HG-4, HG-10; the §8 three-way classification; the bounded S.3 Nissay investigation; the §9 route-obligation comparison |
| Allowed | Publisher methodology; index-version documentation; the S.3 declared material classes |
| Prohibited | Using ND-n quantities as a composition identifier; approving an FX convention; constructing any series; exceeding the S.3 bound |
| Required evidence | Per-candidate return version, dividend and withholding assumptions, embedded expense components, embedded or required FX convention; the S.3 result including UNDISCLOSED / NOT ESTABLISHED where applicable |
| Failure | Return version indeterminate → HG-3 fails; currency treatment indeterminate → HG-4 fails |
| Owner gate | No (reported at G) |
| External retrieval | Documentary only |
| Local raw retention | Documents only |
| Repository entry | Nothing |

| Stage | **F — Licensing and reproducibility qualification** |
| --- | --- |
| Objective | Per-publisher eight-class matrix; evaluate HG-11 under the §5.5 three-way rule; assess third-party reproducibility |
| Allowed | Reading publisher terms; recording verbatim |
| Prohibited | Inferring permission from accessibility or prior retrieval; legal analysis beyond located text; averaging permissions; **treating publication incapacity as disqualifying (S.1)** |
| Required evidence | Per-publisher matrix across: local research access; automated retrieval; local storage; raw-value redistribution; transformed-series redistribution; derived-statistic publication; methodology / provenance citation; repository inclusion |
| Failure | Local use positively restricted → HG-11 fails; terms entirely unreadable → SC-12; readable but silent → OJ-5 |
| Owner gate | No (reported at G) |
| External retrieval | Documentary only |
| Local raw retention | Terms documents only |
| Repository entry | Nothing |

| Stage | **G — Cross-candidate qualification matrix** |
| --- | --- |
| Objective | Apply §5 fail-closed: hard gates first, then comparative criteria **only** among survivors; record ND-n as excluded |
| Allowed | Applying the frozen criteria to Stage B–F evidence |
| Prohibited | Adding, widening, or re-weighting criteria; any tie-break by empirical fit; declaring a winner; constructing any C-2 series without separate Owner authorization |
| Required evidence | Per-candidate × per-gate pass/fail with citations; survivor comparison; explicit "no candidate qualifies" if that is the outcome |
| Failure | Any criterion change needed → return to Owner; zero survivors → valid outcome, reported |
| Owner gate | **Yes** |
| External retrieval | No |
| Local raw retention | N/A |
| Repository entry | Nothing |

| Stage | **H — Publication-boundary review, evidence recording, Owner Decision preparation** |
| --- | --- |
| Objective | Per-source publication review; draft the Phase-1 Evidence Artifact; prepare the P1-2 decision package with the §10 handoff and start-date rules |
| Allowed | Drafting; classifying what may be published |
| Prohibited | Approving a proxy; upgrading any P1 status; choosing a start date or cutoff; committing before Owner approval |
| Required evidence | Artifact draft plus an explicit publication-boundary determination per source |
| Failure | Publication suitability uncertain → **STOP for Owner Review** |
| Owner gate | **Yes** — artifact approval, then the separate P1-2 decision |
| External retrieval | No |
| Local raw retention | Working record stays local |
| Repository entry | **Only after Owner approval** |

---

## 13. Fail-closed stop conditions

A stop halts the affected line of work and returns to the Owner. It is never resolved by a
workaround, a substitution, or a weaker source.

**Source and methodology**

- **SC-1** Authoritative methodology cannot be identified, or is identified but not extractable.
- **SC-2** A required identifier is ambiguous, or two publishers use the same identifier differently.
- **SC-3** Series definition changes without a reconstructable methodology chain.
- **SC-4** A methodology change is known to have occurred but is undated.

**History and provenance**

- **SC-5** Candidate history provenance cannot be established.
- **SC-6** Pre-launch history exists but its status cannot be determined (NON-LIVE UNCHARACTERIZED).
- **SC-7** The publisher's characterization is available only from secondary sources — secondary
  material is never promoted.
- **SC-8** A gap or discontinuity is observed that the publisher does not explain.

**Normative conflict**

- **SC-9** A candidate requires an assumption inconsistent with the Frozen Baseline (HG-13).
- **SC-10** Use of a segment would conflict with [§6](../experiment_spec.md#6-look-ahead-prohibition)'s
  named leak classes and the conflict cannot be confined to an excluded or warm-up-only segment.
- **SC-11** [§7](../experiment_spec.md#7-drawdown-reference-high) single-series or Reference High
  construction cannot be satisfied.

**Licensing**

- **SC-12** Licensing terms cannot be read at all, so HG-11 cannot be evidenced.
- **SC-13** Local research use is positively restricted.
- **SC-14** Automated retrieval would be required where no automated-access policy can be read.

**Integrity and process**

- **SC-15** A retrieval-integrity hazard of the known class is detected and cannot be validated
  against — a source returning a plausible wrong value instead of an error.
- **SC-16** Date-spine metadata cannot be obtained without retrieving and analysing values.
- **SC-17** Any step would require selecting a proxy on the basis of strategy performance, or any
  ND-n quantity is proposed as a discriminator.
- **SC-18** Any frozen criterion would need to change after evidence is seen.
- **SC-19** Coverage regression against evidence already recorded in an approved artifact.
- **SC-20** The S.3 investigation would need to exceed its §8.3 bound.

**Two rules about stop outcomes**

> **A failed candidate does not imply automatic approval of another.** Each candidate is qualified
> independently against the same frozen gates.

> **Zero qualifying candidates is a valid, reportable outcome**, and would itself be materially
> useful evidence.

---

## 14. Owner-only decisions

The research establishes facts and per-candidate qualification status. It MUST NOT itself:

- approve the Primary Proxy;
- approve use of pre-launch / back-tested / hypothetical / reconstructed history;
- choose the Baseline start date;
- choose the Baseline Dataset Cutoff;
- amend OD-12 or any Owner Decision;
- modify Phase 0;
- unblock Phase 2;
- approve a Baseline FX convention;
- authorize any level-space synthetic JPY construction;
- introduce a new proxy family;
- extend the S.3 investigation beyond its declared bound.

Expected Owner Decisions after evidence exists: **OJ-1** (pre-launch admissibility); **OJ-2**
(live-versus-length trade-off); **OJ-3** (return-version principle); **OJ-4** (C-2 role and
obligations); **OJ-5** (bounded qualification where local-use permission is UNCLEAR); **OJ-6**
(P1-2 approval, or a recorded finding that no candidate qualifies). P1-5 and P1-6 remain separate,
later decisions.

---

## 15. Relationship to the Phase-1 open items

This decision **does not change** any status recorded in
[`../experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements),
which remains the authoritative register. **No status may be upgraded by authorization; only by
approved evidence.**

| # | Requirement | Status | Relationship to this decision |
| - | ----------- | ------ | ----------------------------- |
| **P1-1** | Signal → order → NAV mapping | **Unchanged** | Independent of proxy choice; not addressed by this study |
| **P1-2** | Approved Primary Proxy | **OPEN — unchanged** | The item this study is scoped to serve. The study prepares a decision package; **only the Owner can resolve it** |
| **P1-3** | Proxy return composition | **Unchanged** | HG-3 addresses the candidate side; S.3 bounds the Nissay side; failure to establish the latter does not disqualify candidates |
| **P1-4** | Cost / expense treatment | **Unchanged** | HG-10 documents embedded components per [§14.5](../experiment_spec.md#145-cost-and-expense-treatment) |
| **P1-5** | Baseline start date | **OPEN — unchanged** | Receives the §10 handoff. **The study must not choose the date** |
| **P1-6** | Baseline Dataset Cutoff | **OPEN — unchanged** | §11. Any cutoff is a research parameter only |
| **P1-7** | Currency treatment | **Unchanged** | §9. The completed decomposition study is not reopened |
| **P1-8** | Licensing / redistribution | **Unchanged** | §5.5 and Stage F. **S.1 removes publication capability from the hard gate; it does not relax the publication policy itself** |
| **P1-9** | Revision / restatement behaviour | **Unchanged** | HG-9 |

**Phase 2 remains BLOCKED.** The Phase-1 blocking evidence requirements and the methodology
requirements in [`../experiment_spec.md` §19](../experiment_spec.md#19-open-items-register) are
unchanged by this decision.

---

## 16. Boundaries that remain unchanged

- **Phase 0 is Frozen and unchanged. OD-01 … OD-14 are untouched.**
- **AR-01 is RECORDED only and is out of scope for this research.**
- **P1-2 remains OPEN. No Primary Proxy is approved.**
- **P1-5 remains OPEN. P1-6 remains OPEN.**
- **No Baseline start date and no Baseline Dataset Cutoff is approved.**
- **Pre-launch history admissibility remains UNDECIDED.**
- **No Baseline FX convention is approved.**
- **Phase 2 remains BLOCKED.**

---

## 17. Execution authorization

**Stage A, and any external research, may begin ONLY after this artifact has been reviewed,
accepted, committed, and pushed.** No stage of the study was executed during the preparation of
this artifact, and no external research was performed.

---

## 18. Confirmations

- **This is an Owner authorization and criteria freeze, not empirical evidence. No study result
  is recorded here, and none may be added later.**
- **No external research was performed. No data was retrieved. No web access was used.**
- **No returns, correlations, drawdowns, regressions, or strategy outcomes were computed.**
- **No candidate was ranked, selected, or approved.**
- **Publication capability is not a hard gate (S.1); the conservative fail-closed publication
  policy nevertheless remains in force.**
- **Date-spine metadata is authorized (S.2); empirical value analysis is not.**
- **The S.3 Nissay investigation is bounded by §8.3 and may not expand.**
- **"Available history" is not "admissible history"; admissibility remains an Owner Decision.**
- **The Frozen Phase-0 Baseline and OD-01 … OD-14 are unchanged.**
- **P1-1 … P1-9 and M-1 … M-8 are unchanged.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Status: APPROVED — study authorized and criteria frozen.
No Primary Proxy is approved; P1-2, P1-5, and P1-6 remain OPEN; pre-launch history admissibility
remains UNDECIDED; Phase 2 remains BLOCKED.**
