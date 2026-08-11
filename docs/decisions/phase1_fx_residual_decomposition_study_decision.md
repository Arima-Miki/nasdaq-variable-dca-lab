# Phase 1 FX Residual Decomposition Study — Owner Decision

**Status:** APPROVED, with scope limits

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-11

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Authorization of the Phase-1 FX Residual Decomposition Study, its approved research construct, and its execution boundaries |
| Decision status | **APPROVED, with scope limits** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| P1-5 / P1-6 | **OPEN — unchanged by this decision** |
| Nissay FX provider | **NOT IDENTIFIED** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It authorizes **one study**, with one approved
research construct, under explicit boundaries.

> **It is NOT a modification of the Phase-0 Baseline, and it is NOT an Evidence Artifact.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and it does
  not create, amend, or supersede any of them.
- The normative Baseline remains [`docs/experiment_spec.md`](../experiment_spec.md). Where
  this decision and that specification could be read as differing, **the specification
  governs Baseline behavior**.
- It records **Owner authorization only**. It contains **no empirical results**, and no
  future empirical result may be written into it. Study findings belong in a Phase-1
  Evidence Artifact produced at Stage F and separately reviewed.
- The preceding Phase-1 Owner Decision,
  [`phase1_ttm_qualification_decision.md`](phase1_ttm_qualification_decision.md), remains in
  force. This decision **extends** it from a research *input* authorization to a bounded
  study *execution* authorization; it does not weaken any of its limitations.

---

## 2. Research objective

> **Of the post-alignment daily-return residual between the Nissay NASDAQ100 Index Fund NAV
> and the Nasdaq JPY candidate series, what share co-moves with, and is removed by,
> substituting a Japan-side customer-TTM FX convention for the WM-class FX convention
> embedded in the Nasdaq JPY series?**

The residual under investigation is the one recorded in the approved
[`phase1_empirical_alignment_study.md`](../evidence/phase1_empirical_alignment_study.md)
§12, which that artifact deliberately left undecomposed.

The study exploits a **documented asymmetry in the fund's own valuation rule**, recorded in
the approved alignment artifact §2 from the Nissay 請求目論見書: foreign equities are valued
at 「金融商品取引所における計算日に知りうる直近の日の最終相場」 while foreign-currency assets
are converted at 「国内における計算日の対顧客電信売買相場の仲値」. The fund's NAV for a
Japanese business day therefore combines an equity observation from the prior U.S. session
with an FX observation from the Japanese calculation date itself, whereas the Nasdaq JPY
candidate converts that same prior U.S. session at a WM-class fix on that same prior U.S.
date.

The study is designed to be capable of concluding that FX observation convention explains
**little or none** of the residual. A negative result is a valid and reportable outcome.

---

## 3. Owner Decisions D-1 … D-7

### D-1 — Synthetic research construct

**APPROVED WITH SCOPE LIMIT. S1 is approved. S2 is NOT approved.**

#### S1 — approved

**Return-space FX substitution.** Conceptually:

```
existing Nasdaq JPY candidate return
  −  an explicit approximation of the Nasdaq-side FX return
  +  the qualified Japan-side TTM FX return
```

The research question S1 exists to answer is whether replacing the FX **observation
convention** reduces the already-observed fund-vs-candidate residual **in the structurally
predicted way**.

S1 is a **research construct only**. It is **NOT**:

- an approved Primary Proxy;
- a new Baseline index;
- an investable index;
- a Phase-2 backtest input;
- evidence that Nissay uses MUFG/MURC;
- evidence that H.10 equals WMR.

#### Mathematical wording requirement — binding

For multiplicative price components, the log transformation is **additive by identity**:

```
P_JPY = P_USD × FX      ⇒      Δ log P_JPY = Δ log P_USD + Δ log FX
```

> **Log-return additivity MUST NOT be described as an approximation, and MUST NOT be
> attributed to "negligible cross-terms". It is an identity.**

The approximation in this study lies **elsewhere**, and must remain explicit wherever the
construct is described:

1. **The Nasdaq-side FX component is unavailable.** The WM Company Closing Spot rate that
   Nasdaq documents as its EOD FX input is commercially restricted. The study therefore
   **approximates** that component with an approved research approximation / control
   (D-6).
2. **The Japan-side component is substituted, not recovered.** The study substitutes a
   **qualified approximation** of the fund's Japan-side conversion concept — it does not
   reconstruct Nissay's actual conversion.
3. **The structural replacement assumption itself** — that the candidate's JPY return
   decomposes into a USD-return component and a single index-level FX component that may be
   cleanly exchanged — is an assumption about index construction, not a mathematical fact,
   and must be stated as such.

#### S2 — NOT approved

The following is **outside approved scope**:

- constructing `USD-denominated Nasdaq index × Japan-side TTM` as a new level-space
  synthetic JPY index;
- retrieving a USD-denominated Nasdaq candidate series **merely to enable S2**.

S2 may be reconsidered only under a **new Owner Review**.

---

### D-2 — FX residual decomposition execution

**APPROVED.**

Execution of the Phase-1 FX Residual Decomposition Study is authorized **after the required
staged validation gates**.

This approval does **not** authorize skipping stages or fail-closed gates. Each stage is
separately reviewable, and a failed gate halts the study rather than triggering a
workaround.

---

### D-3 — Research cutoff

**APPROVED.**

The study may define **its own research cutoff**, determined by the following rule:

> The **latest common date consistently and reproducibly supported by all mandatory study
> inputs under the approved annotation-preserving retrieval path.**

Requirements:

- The cutoff MUST be derived from **source availability**, not convenience.
- The exact resulting cutoff, and the reason it is the latest valid common date, MUST be
  recorded — as a **Stage-A determination**, reported in the study's evidence record, not in
  this authorization artifact.
- The cutoff MUST be **fixed before any statistic is computed** and applied uniformly.
- It is named the **FX Residual Decomposition Research Cutoff**.

> **It MUST NOT be called, treated as, or allowed to resolve the Baseline Dataset Cutoff.
> P1-6 remains OPEN.**

---

### D-4 — 2024-08-07 sensitivity treatment

**APPROVED.**

On 2024-08-07 the published quotation was suspended and a second quotation issued.

| Treatment | Reading | Role |
| --------- | ------- | ---- |
| **Primary** | final / second-publication TTM ≈ **147.04** JPY/USD | Primary |
| **Mandatory sensitivity** | initial / first-publication TTM ≈ **144.80** JPY/USD | Required |
| **Mandatory robustness** | leave the affected observation out | Required |

Approximate difference: **≈ ¥2.24 ≈ 1.55 %**.

Binding conditions:

- **The study must never silently select one historical reading.**
- If the study's substantive conclusion **changes** across the final, initial, and
  leave-one-out treatments, the result MUST be classified as
  **sensitivity-dependent / unstable**, and MUST NOT be presented as a stable FX
  explanation.
- **Unavailable publication timestamps MUST NOT be inferred.** No timestamp exists for
  either publication, nor for the publisher's display update.

This decision restates and operationalizes the condition already imposed by
[`phase1_ttm_qualification_decision.md`](phase1_ttm_qualification_decision.md) §5.

---

### D-5 — Data retrieval and local research use

**APPROVED FOR LOCAL PHASE-1 RESEARCH ONLY.**

The study may locally retrieve the **minimum data necessary** for the approved research,
including where required by the approved S1 design:

- Nissay NAV observations;
- existing Nasdaq JPY candidate observations;
- FRB H.10 USD/JPY observations;
- MUFG/MURC historical USD/JPY TTM observations;
- source metadata necessary for provenance and integrity validation.

BOJ data may be retrieved **only** if required by the approved design as a
diagnostic / control, and **not merely because it is available**.

Boundaries:

- **Prefer the smallest sufficient dataset.**
- **Raw data MUST remain outside the public repository.**
- **No redistribution approval is implied.**
- **No raw downloaded market or source dataset may be committed.**

---

### D-6 — Nasdaq-side FX approximation

**APPROVED WITH EXPLICIT LIMITATION.**

FRB H.10 USD/JPY may be used as an **explicit research approximation / control** for the
unavailable Nasdaq-side WM Company Closing Spot FX leg.

- It MUST **always** be labelled as an approximation.
- It MUST NOT be stated or implied that **H.10 = WMR**.
- It MUST NOT be stated or implied that H.10 reproduces the exact Nasdaq FX conversion.
- USD-denominated Nasdaq candidate series MUST NOT be retrieved for this study unless a new
  Owner Review authorizes S2 or another design requiring them.

The observation-time difference is **date-dependent**: JST observes no daylight saving while
the United Kingdom and the United States both do, on transition dates that are not always
identical. **No fixed-hour relationship may be asserted**, and any relative-timing statement
must use calendar-aware conversion per observation date.

---

### D-7 — Derived statistics and public-repository publication

**MODIFIED / SPLIT BOUNDARY.**

#### Approved now — local calculation

Once the relevant execution stage is reached, the study may **calculate derived statistics
locally**, including regression coefficients, residual RMSE, annualized tracking error,
residual variance reduction, correlation, mean residual / bias, sample counts, and
robustness statistics.

#### NOT automatically approved — publication

> **Publication of derived statistics into the PUBLIC repository is NOT blanket-approved
> merely because they were calculated.**

- **Stage F MUST include an explicit publication-boundary review.**
- Before committing final empirical evidence, each **class** of derived result must be
  assessed for publication suitability under the recorded evidence and licensing
  constraints.
- **If uncertain: STOP for Owner Review.**
- **Permission to use raw data locally MUST NOT be assumed to imply permission to publish
  transformed results.**

---

## 4. Identification strategy

The study must be able to distinguish

> "FX convention explains part of the residual"

from

> "the synthetic transformation merely changed the series."

Subtracting any series of comparable scale will change a residual. Variance reduction alone
therefore proves nothing.

### 4.1 Counterfactual comparison — one factor at a time

| Object | Index construction | Observation dates | Equity leg | FX convention |
| ------ | ------------------ | ----------------- | ---------- | ------------- |
| Candidate JPY series | Nasdaq | index dates | prior U.S. close | **WM-class EOD, index date** |
| **S1 construct** | Nasdaq — *unchanged* | *unchanged* | *unchanged* | **Japan customer TTM, calculation date** |
| Fund NAV | Nissay (unobserved) | Japan business dates | prior knowable U.S. close | Japan customer TTM (concept) |

Only the FX convention differs between the first two rows. Everything else — index
construction, weighting, return version, dividend treatment, calculation calendar, and the
observation dates themselves — is inherited unchanged from the Nasdaq series.

### 4.2 The identification requirement

The structural hypothesis makes a **point prediction**: the observed residual should carry
the FX-convention difference at **unit exposure**. The study's primary identification
statistic is therefore the **estimated exposure of the residual to the FX-convention
difference, anchored at 1**, not a correlation and not a variance reduction taken alone.

A variance reduction may be reported as evidence of an FX component **only if** the
estimated exposure supports it.

### 4.3 Required falsification arms

- a **placebo** arm in which the FX-convention difference is shifted off its aligned
  position, which should collapse the estimated exposure toward zero;
- a **concept control** arm using a different Japan-side rate concept observed at a
  different time of day, to test whether the mechanism is specific to a Japan-morning
  customer rate or merely to any Japan-side FX series;
- an **orientation check**, since all FX series must be handled as JPY per 1 USD;
- an **independent ceiling**: the dispersion of the FX-convention difference bounds the
  contribution it can make regardless of the estimated exposure.

### 4.4 Alignment discipline

The **lag −1 observation-time alignment** established by the approved
[`phase1_empirical_alignment_study.md`](../evidence/phase1_empirical_alignment_study.md) is
**adopted as an input and is not re-estimated**. The lag set MUST NOT be re-searched.
Re-deriving it is permitted only as a consistency check, and a disagreement is a **red flag
on the study design**, not a licence to change the alignment.

The alignment commitments of that artifact are inherited verbatim: **no forward-fill, no
interpolation, no synthesized observations, and no blind calendar-offset arithmetic.**
Pairing is by ordered valid observations.

---

## 5. Stage structure and fail-closed gates

| Stage | Content | Fail-closed stop condition |
| ----- | ------- | -------------------------- |
| **A — Acquisition & provenance** | Retrieve mandatory inputs to a location outside the repository; record provenance, retrieval timestamps, checksums, coverage; run retrieval-integrity validation; determine the research cutoff | Any integrity validation fails; a mandatory source is unusable; coverage regression against recorded evidence; annotation mismatch |
| **B — Calendar normalization & residual reproduction** | Build the pairing; attach FX legs; verify orientation; **reproduce the approved alignment statistics** | **Reproduction failure is a hard stop.** If the residual does not reproduce approved evidence, the pipeline is wrong and nothing downstream is trustworthy |
| **C — FX difference construction** | Build the FX-convention difference on the pairing; compute its independent ceiling | Materially asymmetric coverage loss across arms |
| **D — Decomposition** | Estimated exposure, variance reduction, and the supporting diagnostics | Sign inconsistent with the orientation check |
| **E — Robustness & sensitivity** | The pre-declared arms, including the three mandatory 2024-08-07 treatments, placebo, and concept control | Conclusion class differs across arms → classify as sensitivity-dependent / unstable and stop |
| **F — Evidence recording** | Draft the Phase-1 Evidence Artifact; **explicit publication-boundary review under D-7** | Publication suitability uncertain → **STOP for Owner Review** |

**Owner Review gates:** after Stage A (sources, terms handling, frozen cutoff), after
Stage B (reproduction gate), and at Stage F (publication boundary and artifact approval).

Stages C–E constitute a single analytical pass. Metrics, thresholds, subsets, and arms are
**pre-declared** and MUST NOT be added, widened, or re-optimized after results are seen. Any
change after Stage D requires returning to the Owner.

---

## 6. Data-handling boundary

- All raw working data MUST live **structurally outside the Git repository** — not inside an
  ignored repository directory. A `.gitignore` entry is a safety net, not the boundary.
- **No raw downloaded market or source dataset may be committed**, in any format.
- Provenance material — checksums, manifests, acquisition logs — is **Stage-A working
  material by default** and is not committed unless its public-repository suitability is
  separately established.
- Individual source values may appear in repository artifacts **only** as targeted evidence
  citations, consistent with existing practice, never as a dataset.
- No credentials of any kind are introduced. No brokerage or production trading credentials
  exist in, or are relevant to, this research environment.

---

## 7. Explicit non-claims

This decision, and any study executed under it, does **NOT** establish:

- Nissay's actual FX provider — **MUFG/MURC is NOT identified as Nissay's FX provider**;
- Nissay's actual fixing time, rate type, holiday convention, rounding, or fallback rules;
- that approximately **09:55 JST** is an established MUFG determination time — it may be
  described **only** as conventional, secondary-source based, or an explicit sensitivity
  assumption;
- any quantitative re-fixing threshold — **no approximately-¥1 threshold is established and
  none may be modelled**;
- that **H.10 equals WMR**, or reproduces Nasdaq's FX conversion;
- the true Nissay benchmark, or the meaning of 「配当込み」;
- an approved **Primary Proxy**;
- an approved **Baseline FX convention**;
- that **FX observation convention explains the residual** — that is the question under
  test, not a premise;
- any causal attribution of the remaining residual;
- any strategy performance, profitability, or comparison among Strategies A, B, and C.

---

## 8. Relationship to the Phase-1 open items

This decision **does not change** any status recorded in
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements),
which remains the authoritative register.

| # | Requirement | Status | Relationship to this decision |
| - | ----------- | ------ | ----------------------------- |
| **P1-2** | Approved Primary Proxy | **OPEN — unchanged** | The study MUST NOT select `NDXJPY`, `XNDXJPY`, or `XNDXNNRJPY` as Primary Proxy, propose one, or rank them. All candidates are carried symmetrically, and the FX-convention difference is candidate-neutral by construction. If the work later makes the candidates more empirically distinguishable, that is **evidence available to a subsequent, separately reviewed Owner decision** — never the decision itself |
| **P1-5** | Exact Baseline start date | **OPEN — unchanged** | The study window implies no Baseline start date |
| **P1-6** | Fixed Baseline Dataset Cutoff | **OPEN — unchanged** | The FX Residual Decomposition Research Cutoff is a **study parameter only** and MUST NOT resolve or modify P1-6 |
| **P1-7** | Currency treatment | SUBSTANTIALLY ADVANCED — unchanged by authorization alone | The item this study is scoped to serve. No status may be upgraded by authorization; only by approved evidence |
| **P1-8** | Licensing / redistribution | PARTIAL — unchanged | D-5 authorizes bounded local use only. **Nothing is cleared for redistribution.** D-7 keeps publication of derived statistics under separate review |
| **P1-9** | Revision / restatement behaviour | PARTIAL — unchanged | D-4 exists because of it |

---

## 9. Boundaries that remain unchanged

- **Phase 0 is Frozen and unchanged. OD-01 … OD-14 are untouched.**
- **P1-2 remains OPEN. No Primary Proxy is approved.**
- **P1-5 remains OPEN. P1-6 remains OPEN.**
- **No Baseline FX convention is approved.**
- **MUFG/MURC is NOT identified as Nissay's actual FX provider.**
- **Approximately 09:55 JST is NOT an established MUFG fixing time.**
- **No approximately-¥1 re-fixing threshold is established.**
- **FX observation convention is NOT yet proven to explain the residual.**
- **Phase 2 remains BLOCKED.** The Phase-1 blocking evidence requirements and the
  methodology requirements in
  [`docs/experiment_spec.md` §19](../experiment_spec.md#19-open-items-register) are
  unchanged by this decision.

---

## 10. Evidence references

| Artifact | Role |
| -------- | ---- |
| [`../evidence/phase1_empirical_alignment_study.md`](../evidence/phase1_empirical_alignment_study.md) | Establishes the lag −1 alignment adopted by this study, and the undecomposed residual it exists to investigate |
| [`../evidence/phase1_fx_source_research.md`](../evidence/phase1_fx_source_research.md) | Pins the Nasdaq-side FX convention from primary Nasdaq documents; establishes WMR as commercially restricted and H.10 / BOJ as public alternatives |
| [`../evidence/phase1_japan_side_ttm_qualification.md`](../evidence/phase1_japan_side_ttm_qualification.md) | Qualifies the Japan-side TTM candidate; source of the retrieval hazards, re-fixing semantics, and the 2024-08-07 case |
| [`phase1_ttm_qualification_decision.md`](phase1_ttm_qualification_decision.md) | The preceding Phase-1 Owner Decision, extended but not weakened by this one |
| [`../experiment_spec.md`](../experiment_spec.md) | Normative Frozen Baseline — **unchanged** |

---

## 11. Confirmations

- **This is an Owner authorization, not empirical evidence. No study result is recorded
  here, and none may be added later.**
- **S1 is approved. S2 is NOT approved.**
- **Log-return additivity is an identity, not an approximation. The approximation is the
  structural replacement of the unavailable Nasdaq-side FX component and the substitution of
  the qualified Japan-side component.**
- **No raw market or source data may be committed to this repository.**
- **Publication of derived statistics remains subject to a separate Stage-F review.**
- **No Primary Proxy is approved. P1-2 remains OPEN.**
- **P1-5 and P1-6 remain OPEN.**
- **The Frozen Phase-0 Baseline and OD-01 … OD-14 are unchanged.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Status: APPROVED, with scope limits.
S1 approved; S2 not approved. P1-2, P1-5, and P1-6 remain OPEN. Phase 2 remains BLOCKED.**
