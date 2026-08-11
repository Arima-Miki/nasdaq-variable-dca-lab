# Phase 1 Evidence Artifact — FX Residual Decomposition Study

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **FX Residual Decomposition Study** |
| Research dates | **2026-08-11** (all source access dates 2026-08-11) |
| Authorising decision | [`docs/decisions/phase1_fx_residual_decomposition_study_decision.md`](../decisions/phase1_fx_residual_decomposition_study_decision.md) (D-1 … D-7) |
| Analytical window | **2023-04-03 → 2026-07-31** (first aligned observation → research cutoff) |
| FX Residual Decomposition Research Cutoff | **2026-07-31** — a study parameter only |
| Owner Review | **APPROVED** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Publication classification | **PUBLIC QUALITATIVE EVIDENCE** |
| Detailed numerical evidence | **LOCAL RESEARCH RECORD — intentionally not reproduced in this artifact** (see [§10](#10-publication-boundary)) |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Nissay FX provider | **NOT IDENTIFIED** |
| Nissay fixing time | **NOT ESTABLISHED** |
| Phase 2 | **BLOCKED** |

> **What the approval means.** The Owner has approved **the research evidence recorded in this
> artifact** — the study's design, its stage structure, its qualitative findings, and its stated
> limits.
>
> The Owner has **not** identified Nissay's FX provider, has **not** established any fixing time,
> has **not** approved a Primary Proxy, has **not** approved a Baseline FX convention, and has
> **not** unblocked Phase 2.

> **On the absence of numbers.** This artifact deliberately records qualitative findings only.
> The detailed numerical results exist as a complete local research record. They are **withheld
> by policy, not missing**. See [§10](#10-publication-boundary) and [§11](#11-local-evidence-boundary).

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and does not
govern Baseline behavior. The observation-time alignment evidence this study builds on is
[`phase1_empirical_alignment_study.md`](phase1_empirical_alignment_study.md). The FX source survey
is [`phase1_fx_source_research.md`](phase1_fx_source_research.md) and the Japan-side source
qualification is [`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md),
with its bounded Owner Decision in
[`phase1_ttm_qualification_decision.md`](../decisions/phase1_ttm_qualification_decision.md).

This artifact is written to be self-contained. A future researcher with no access to the session
in which the study was run should be able to understand what was asked, how it was tested, what
was found, what was deliberately left unresolved, and what was deliberately not published, from
this file alone.

---

## 2. Research question

The approved Empirical Alignment Study established a one-observation timing relationship between
the Nissay NASDAQ100 Index Fund NAV and the Nasdaq JPY candidate series, and recorded that a
**material daily-return residual remained after that timing alignment**. That artifact explicitly
declined to attribute the residual to any cause, and recorded exactly one approved research
direction: an FX residual decomposition.

This study asks that question:

> **Can differences in FX observation and conversion convention explain a material component of
> the post-alignment residual between the fund NAV and the Nasdaq JPY candidate series?**

The question is well-posed because the fund's own valuation rule, quoted from the Nissay
請求目論見書 in the alignment artifact, combines an equity observation from the most recent
knowable prior close with a foreign-currency conversion struck on the Japanese calculation date,
whereas a Nasdaq JPY index converts that same prior session at a fix associated with the index
date. The two conversion points therefore sit on opposite sides of the U.S. close.

The study was designed to be capable of concluding that FX convention explains little or nothing.
A negative result would have been reported as such.

---

## 3. Prior evidence relied upon

Only what is necessary is restated here; each source artifact remains authoritative for its own
study.

1. **The observation-time relationship had already been established.** The lag −1 alignment was
   adopted as an input and was **not** re-estimated by this study.
2. **FX convention remained a first-order unresolved candidate** for the residual. The FX source
   survey pinned the Nasdaq-side documented convention from primary Nasdaq material and
   established that the corresponding benchmark rate is commercially restricted and not
   obtainable for this repository.
3. **MUFG/MURC TTM had been qualified for local Phase-1 research only**, as a *candidate
   approximation of a concept*, under explicit non-claims.
4. **No actual Nissay FX provider, fixing time, rate type, holiday convention, rounding, or
   fallback rule had been established**, and none is established here.
5. **No Primary Proxy had been approved.** P1-2 was open before this study and remains open.

---

## 4. Study design — stage structure

The study was executed as six separately reviewable stages, each with fail-closed stop
conditions. The stage structure is itself durable evidence of how the result was produced.

| Stage | Purpose | Gate |
| ----- | ------- | ---- |
| **A — Source acquisition and provenance** | Retrieve the minimum required inputs to a working area **structurally outside** the repository; record provenance and checksums; establish coverage by parsing; validate known retrieval hazards; determine the research cutoff | Any integrity failure, coverage regression, or unusable mandatory source halts the study |
| **B — Reproduction gate** | Independently reproduce the approved Empirical Alignment Study from freshly retrieved data using an independently written pipeline | **Reproduction failure is a hard stop.** If the prior approved evidence cannot be reproduced, nothing downstream is trustworthy |
| **C — Construction gate** | Establish FX orientation from primary source text, build the calendar, construct the FX differential and the approved return-space research construct, and validate them structurally | Orientation, alignment, or construction failure halts the study |
| **D — Identification and residual decomposition** | Test the pre-specified structural hypothesis; measure residual substitution; run the pre-declared falsification arms | Inconsistent measurement space, mismatched sample dates, or a design change halts the study |
| **E — Robustness and sensitivity** | Execute only pre-declared robustness arms; treat the unresolved feature identified in Stage D as a first-class question | Instability across point-in-time branches would have reclassified the outcome |
| **F — Publication-boundary review and evidence recording** | Review source publication and reuse terms per source; record public evidence within the resulting boundary | Uncertain publication rights stop for Owner Review |

Two disciplines applied throughout and are recorded because they constrain how the result may be
read:

- **Pre-declaration.** Metrics, thresholds, subsets, robustness arms, the influence method, and
  the numerical reproduction tolerance were each fixed **in writing before** the corresponding
  results were computed. Nothing was widened, split, merged, or re-optimised afterwards.
- **No silent gap-filling.** No forward-fill, no interpolation, no synthesized observations, no
  nearest-observation substitution, and no calendar-offset arithmetic were used at any stage. Where
  a required input was unavailable for an observation, the observation was dropped and counted.

---

## 5. FX differential construction

Conceptually, for each valid analytical observation:

```
d  =  change in the Japan-side TTM approximation
    − change in the U.S.-side FX reference approximation
```

The two legs are attached to different date concepts, and the distinction is essential:

- the **Japan-side leg** attaches to the Japanese calculation dates;
- the **U.S.-side leg** attaches to the index observation dates already fixed by the approved
  lag −1 alignment.

Inputs and their roles:

| Input | Role |
| ----- | ---- |
| **MUFG/MURC TTM** | The Owner-qualified **Japan-side approximation**, used strictly within the bounded authorization already recorded. It is a candidate approximation of a *concept*, not a reconstruction of the fund's conversion |
| **FRB H.10 USD/JPY** | The **U.S.-side approximation / control** for the unavailable index-side benchmark component, used and labelled only as an approximation |
| **BOJ 17:00 JST spot** | A **concept control** — a different Japan-side rate concept observed at a different time of day, used to test whether any effect is specific or generic |

Explicitly:

- **Neither approximation is asserted to be the actual production fixing** used by the fund or by
  the index publisher.
- The Japan-side archive distinguishes an initial and a final publication on one date within the
  window — **2024-08-07** — and that distinction was preserved from acquisition onward and was
  **never collapsed** before the mandatory sensitivity treatment was applied. The recorded
  branch evidence for that date is held in
  [`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md) and is
  **not restated here**.
- The construction is entirely **date-level**. **No intraday fixing timestamp was used, assumed,
  or inferred at any point.** The commonly cited approximate Japanese morning fixing convention
  was not required to build anything in this study and was not used numerically.

Raw values, per-date reconstructed series, and the per-date differential are **not published**
(see [§10](#10-publication-boundary)).

---

## 6. Identification model

The methodology is public; the estimates are not.

The structural relationship tested was:

```
epsilon_t  =  alpha  +  beta * d_t  +  eta_t
```

where `epsilon` is the observed fund-versus-candidate return residual and `d` is the FX-convention
differential defined above.

**Why an exposure test rather than a fit test.** Subtracting any series of comparable scale will
change a residual. A variance reduction on its own therefore demonstrates nothing. The structural
hypothesis makes a sharper prediction: if the FX-convention differential is genuinely *present in*
the residual, the residual should carry it at a structurally expected exposure — not merely
correlate with it. The primary identification evidence is therefore the **estimated exposure**,
assessed against the structurally expected order, and supported by the residual reduction only
when the exposure supports it.

**Measurement-space discipline.** The differential is defined exactly in log-return space, where
the decomposition of a currency-converted index return into a local-return component and an FX
component is an identity rather than an approximation. The prior approved artifact reported its
residual metrics in simple-return space. The two spaces were therefore kept strictly separate: the
structural test was run in log space, and the before/after substitution measurement was computed in
simple-return space using an exact conversion. **The two spaces were never mixed**, so no
linearisation error was introduced.

**Where the approximation actually lies.** Not in the algebra. It lies in (a) approximating an
unavailable index-side FX component, (b) substituting a qualified approximation for the Japan-side
component, and (c) the structural assumption that a candidate's converted return decomposes into a
local-return component and a single index-level FX component that may be cleanly exchanged. Item
(c) is an assumption about index construction, not a mathematical fact.

**Falsification arms** were pre-declared: an Owner-approved observation-adjacent placebo in both
directions; a different-concept Japan-side control; an orientation check; and an independent
dispersion check bounding the scale of any possible contribution.

Numerical estimates, intervals, fit statistics, residual metrics, and reduction measures are
**not published**.

---

## 7. Qualitative findings

### Finding 1 — Material support for the FX-convention hypothesis

The tested FX-convention hypothesis received **material empirical support**. The correctly aligned
FX differential explained a **substantial structural component** of the residual previously
observed between the fund NAV and the Nasdaq JPY candidate series, under the qualified
approximations.

### Finding 2 — Exposure of order one, but systematically above unit exposure

The estimated relationship was structurally consistent with a strong FX component: the exposure was
positive and of order one, and was clearly unlike zero in every arm examined. However, the estimated
exposure remained **systematically above unit exposure**, and this excess **persisted under every
pre-declared robustness check**.

**The cause of this excess is not established.** It is recorded as a robust but unexplained
empirical feature. Structural explanations that remain open — none of them tested or preferred here
— include the possibility that the U.S.-side approximation differs from the actual index-side
component, that the Japan-side approximation differs in amplitude from the fund's actual rate, or
that a further residual component co-varies with the differential. **No causal attribution is
made.**

### Finding 3 — Date attachment matters, at the date level

A pre-declared two-element attachment sensitivity was run: the Japan-side rate attached to the
calculation date, versus attached to the preceding Japanese business day. The **prospectus-consistent
calculation-date attachment materially outperformed** the preceding-business-day alternative, which
showed essentially no explanatory power and made the substitution worse.

This supports a **date-level** attachment interpretation, and it does so **without requiring any
intraday timing assumption**.

It does **NOT**:

- establish Nissay's intraday fixing time;
- identify Nissay's FX provider;
- close **P1-1**.

### Finding 4 — The adjacent-observation placebo behaved differently

The Owner-approved observation-adjacent placebo, run in both directions, **did not reproduce the
correctly aligned relationship**. Its estimated exposure was of the opposite sign and its
explanatory strength was substantially weaker. The correctly aligned position was the only arm
exhibiting the structurally predicted behaviour.

### Finding 5 — The concept control was weaker but non-zero

The BOJ 17:00 JST concept control — a different Japan-side rate concept observed at a different
time of day — retained **clear evidence of a broader Japan-side FX and date effect**, but the
qualified TTM-like approximation provided **materially stronger** support on both exposure and
explanatory strength.

The evidence therefore supports a **Japan-side FX convention component, with additional support for
a TTM-like component specifically**. It does **not** identify the actual production convention, and
the control was not forced to discriminate further than the evidence allows.

### Finding 6 — Robustness

The principal conclusion remained stable across every pre-declared arm:

- the three mandatory point-in-time branches for the one in-window re-fixing date, **2024-08-07**
  — final, initial, and leave-one-out (branch evidence recorded in
  [`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md));
- split-window checks;
- the large-move sensitivity, at the previously approved threshold;
- the complementary ordinary-observation sensitivity;
- the candidate-observation-span sensitivity, including the one-span subset;
- candidate-series symmetry checks;
- a bounded influence diagnostic, which found the conclusion **not** attributable to a small set of
  influential dates.

Restricting to the cleanest span class moved the estimated exposure toward the structurally
expected value and improved explanatory strength, without reaching it.

### Finding 7 — Candidate neutrality

The three candidate Nasdaq JPY series behaved **sufficiently similarly** in this study that it
provides **no basis for ranking them**. The FX differential is common to all three by construction,
and all arms were run symmetrically.

**P1-2 remains OPEN. No Primary Proxy is approved, proposed, or implied.**

### Finding 8 — A structured residual remains

After accounting for the tested FX-convention component, a **non-trivial and structured** residual
remained. It is not unstructured noise.

Two named Phase-1 research questions are retained and are **not** addressed here:

1. **Anomalous behaviour in the span-0 observation class** — the Japan-only dates on which the
   paired index observation does not advance.
2. **Strong negative short-lag autocorrelation in the post-FX residual**, which persisted at
   materially the same strength after the FX component was removed.

No attempt is made in this artifact to explain either.

---

## 8. What the study establishes

Narrowly, and **under the qualified approximations**:

1. **FX observation and conversion convention is a material structural contributor** to the
   observed fund-versus-candidate residual.
2. **The effect depends materially on correct date attachment.**
3. **The conclusion survives the pre-declared robustness and sensitivity checks**, including all
   three mandatory point-in-time branches.
4. **A TTM-like Japan-side approximation provides stronger support than the BOJ concept control**,
   while the control itself remains non-zero.
5. **The residual is materially reduced but not eliminated.**
6. **Additional residual structure remains**, and is retained as open research.

It also establishes, as process evidence, that the approved Empirical Alignment Study **was
independently reproduced** on a fresh environment, from a fresh retrieval, with an independently
written pipeline, before any new analysis was permitted to proceed.

---

## 9. What the study does NOT establish

The study does **not** establish any of the following:

- the actual **Nissay FX provider** — **MUFG/MURC is not identified as it**;
- Nissay's actual **fixing time**;
- Nissay's actual **conversion algorithm**, holiday convention, rounding, or fallback rules;
- the exact **Nasdaq production FX source** applying to every candidate series;
- that the **MUFG/MURC TTM equals Nissay's actual rate**;
- that **FRB H.10 equals** the index-side benchmark rate;
- the **cause of the exposure exceeding unit exposure**;
- the **cause of the remaining residual**, which is not decomposed into expenses, dividend
  treatment, futures basis, cash timing, tax, tracking difference, or any other component;
- an approved **Primary Proxy**;
- the **Baseline start date**;
- the **Baseline Dataset Cutoff**;
- completion of **P1-8**;
- any statement about **profitability**, **strategy superiority**, or any comparison among
  Strategies A, B and C;
- any **Phase-2 backtest result**.

No formal statistical significance is claimed. Interval estimates were used descriptively only,
consistent with the existing methodology position that statistical claims require a methodology
that has not yet been approved.

---

## 10. Publication boundary

Stage F-1 reviewed publication and reuse terms **separately** for each source: **Nissay Asset
Management**, **Nasdaq / Global Index Watch**, **Federal Reserve Board H.10**, **MUFG**, **MURC**,
and the **Bank of Japan**. MUFG and MURC were assessed as distinct publishers; no located text
binds them jointly.

The review applied a **conservative fail-closed publication policy**: where a located terms text
restricts reuse, or does not address the publication of derived results, the project does not treat
the available evidence as sufficient to authorise public reproduction in this repository.

Consequently, the following are **not published**:

- **raw source series**, in any format;
- **reconstructed or transformed per-date series**, including the FX differential and the
  return-space research construct;
- **detailed Stage B–E numerical results** — estimates, intervals, fit statistics, residual
  metrics, reduction measures, control and placebo estimates, influence outputs, and
  per-class tables;
- **internal retrieval endpoint identities** and internal access details;
- the **Stage-A acquisition manifest**, including its per-file rows.

What **is** published is intentionally limited to: the research question and its provenance, the
methodology and stage structure, source roles at an appropriate level, the qualitative findings,
the limitations, the open questions, and the consequences for project state.

Two points are recorded precisely, because the distinction matters:

> **This artifact does not state that publication of the detailed statistics is prohibited.** It
> states that **the project does not treat the available terms evidence as sufficient to authorise
> their public reproduction in this repository**. Those are different claims, and only the second
> is made.

> **No statement is made that any prior retrieval was unlawful or breached any terms.** Equally, the
> fact that a retrieval previously succeeded is **not** treated as evidence of permission for
> further retrieval, redistribution, or publication.

The one source whose terms are explicitly permissive with attribution is the Bank of Japan.
Because the study's results are **jointly derived** from several sources, the conservative
composition rule applies: a jointly derived result can be no more publishable than its least-clear
contributing source. Permissions are not averaged.

Existing approved Evidence Artifacts are **unchanged** by this review. Nothing already published is
extended, and nothing already published is retroactively altered; any future change of that kind
would require a separate Owner Decision.

---

## 11. Local evidence boundary

The detailed quantitative evidence exists as a **complete local research record**, held in a working
area structurally outside this repository. It includes:

- the primary regression outputs and their interval estimates;
- residual metrics before and after the FX substitution;
- the full sensitivity and robustness tables;
- placebo and concept-control outputs;
- influence diagnostics;
- construction and structural-validation checks;
- calendar and coverage reconciliations;
- acquisition records, provenance metadata, and integrity-validation results.

These are **intentionally non-public**, not absent. The public artifact is a durable **qualitative**
research record; it is not the complete research payload.

A future researcher should expect to re-derive the numerical results from the documented
methodology and the named sources, subject to obtaining their own access and their own view of the
applicable reuse rights. The pre-declared conventions, the stage gates, and the construction rules
recorded here are sufficient to reconstruct the study design.

---

## 12. Phase-1 requirement impact

Statuses as represented by this artifact. **No item is upgraded merely because this artifact was
recorded.** The open-items register in
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements)
remains the authoritative list of requirements and is **unchanged** by this study.

| # | Requirement | Status | Basis |
| - | ----------- | ------ | ----- |
| **P1-1** | Signal → order → execution date → applicable NAV mapping | **SUBSTANTIALLY ADVANCED / OPEN** | Date-level attachment evidence is materially strengthened by Finding 3. The order-to-NAV leg, application-cutoff history, distributor-specific cutoffs, and any intraday fixing question remain unresolved. **This does not close P1-1.** |
| **P1-2** | Approved Primary Proxy | **OPEN** | Finding 7. The three candidates behaved sufficiently similarly that no ranking basis exists. **Untouched by this study.** |
| **P1-3** | Proxy return composition / dividend treatment | **PARTIAL / OPEN** | Not resolved by this study. |
| **P1-4** | Cost / expense treatment | **PARTIAL / OPEN** | Not resolved by this study. The remaining residual was deliberately **not** decomposed into cost or expense components. |
| **P1-5** | Exact Baseline start date | **OPEN** | Unchanged. The study window implies no Baseline start date. |
| **P1-6** | Fixed Baseline Dataset Cutoff | **OPEN** | Unchanged. The FX Residual Decomposition Research Cutoff is a **study parameter only** and does not resolve or modify P1-6. |
| **P1-7** | Currency treatment | **SUBSTANTIALLY ADVANCED** | The item this study was scoped to serve. FX convention is now demonstrated to be a first-order empirical contributor **under the qualified approximations**. It does **not** reach RESOLVED: the actual production convention on either side remains unidentified, and the exposure excess is unexplained. |
| **P1-8** | Licensing / redistribution | **SUBSTANTIALLY ADVANCED / OPEN** | Terms were located and read for sources previously unassessed, and the four distinct questions — local use, raw redistribution, derived-result publication, and provenance publication — are now separated. **Not resolved**, and this does not unblock anything. |
| **P1-9** | Revision / restatement behaviour | **Unchanged from prior approved state** | The one in-window re-fixing event (**2024-08-07**) was handled under the mandatory three-branch treatment, as recorded in [`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md); no new restatement testing was performed. |

**Phase 2 remains BLOCKED.** The Phase-1 blocking evidence requirements and the methodology
requirements in [`docs/experiment_spec.md` §19](../experiment_spec.md#19-open-items-register) are
unchanged by this study.

---

## 13. Limitations

1. **Both FX legs are approximations.** Neither is asserted to be the actual production fixing, and
   the magnitude of the approximation error on the index-side leg cannot be measured without the
   restricted benchmark data.
2. **The exposure excess above unit exposure is unexplained** and is the single most important
   open feature of the result.
3. **The window is short and single-regime**, and begins at fund inception; it cannot be extended
   earlier.
4. **The study window ends at the research cutoff**, which is shorter than the window of the prior
   approved alignment study, because it is bounded by the latest date consistently supported by all
   required inputs through their annotation-preserving retrieval paths.
5. **One re-fixing event falls inside the window — 2024-08-07.** It was handled under three
   mandatory branches rather than a single silent choice (see
   [`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md)), but no
   publication timestamps exist for either publication and none were inferred.
6. **Observations were dropped where a required FX input was unavailable**, principally around
   holidays affecting one calendar but not the other. These were counted, not filled.
7. **A structured residual remains** after the FX component is accounted for.
8. **Single pass, no out-of-sample confirmation.** Conventions were pre-declared and not optimised,
   but this remains exploratory rather than confirmatory work.
9. **No statistical significance is claimed**, and no causal attribution is made anywhere in this
   artifact.
10. **Detailed numerical evidence is not publicly reproduced here**, by policy.

---

## 14. Open research questions

Carried forward explicitly, and **not** investigated in this artifact:

1. Why is the estimated FX exposure systematically above unit exposure?
2. What explains the span-0 residual behaviour?
3. What explains the strong negative short-lag autocorrelation remaining after FX adjustment?
4. What components explain the remaining residual?
5. Can authoritative or licensed source access eventually support public numeric reproduction of
   this study's results?
6. Which Primary Proxy, if any, should eventually be approved?

---

## 15. Confirmations

- **This artifact records qualitative research evidence only.** Detailed numerical results are
  intentionally withheld under the project's conservative publication policy, and exist as a local
  research record.
- **No raw, reconstructed, or transformed source series is published.**
- **No internal retrieval endpoint identity and no acquisition manifest is published.**
- **No claim is made that any prior retrieval was unlawful or breached any terms**, and no
  permission is inferred from prior retrieval having succeeded.
- **No Japanese bank is identified as Nissay's FX provider.**
- **No fixing time is established**; the construction is entirely date-level.
- **No re-fixing threshold is modelled.**
- **No Primary Proxy is approved. P1-2 remains OPEN.**
- **P1-5 and P1-6 remain OPEN.** **P1-8 is SUBSTANTIALLY ADVANCED and remains OPEN.**
- **No Baseline FX convention is approved.**
- **The Frozen Phase-0 Baseline and OD-01 … OD-14 are unchanged.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Evidence Artifact. Owner Review: APPROVED.
Publication classification: PUBLIC QUALITATIVE EVIDENCE — detailed numerical results intentionally
withheld under the project's conservative publication policy.
Primary Proxy: NOT APPROVED — P1-2 remains OPEN. Phase 2 remains BLOCKED.**
