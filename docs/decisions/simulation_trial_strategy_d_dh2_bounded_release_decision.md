# Simulation Trial — Strategy D Stage D-H2: Bounded Release of `NDXJPY` `1987-07-27 → 1990-01-18`

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.**
`DH2-REL-1` **APPROVE WITH CONDITIONS** · `DH2-REL-2` **ACCEPT** · `DH2-REL-3` **APPROVE**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13) — unchanged by this artifact
**Controlling D-H2 chain:** D-H2 authorization `3c687c80e2ec51f63e3fd2c9a98af0f320578baf` ·
D-H2 selection execution (deterministic rule `f025bbf0dd5df9a4b037936822b1ced4e263948c` executed) ·
D-H2 selection audit (compliance verified, deferral permitted) ·
D-H2 bounded extraction (DH1-R6 passed, dataset frozen)
**Prior, non-overlapping NDXJPY releases:**
D-H0 Mode-P (`73d6f51`): `2018-01-02 → 2020-06-26`
D-H1 (`b722fb2`): `1985-01-31 → 1987-07-26`
**Governing Strategy-D chain:** hypothesis `5a3f54a` · semantics `62c5c42` · Mode-E E5 `f16a815` ·
D-H0 mechanical validation `486b994`

**This artifact authorizes RELEASE ONLY. It does NOT authorize Strategy-D execution** (§10).

---

## 1. Historical chronology (load-bearing, permanent record)

1. Strategy D was created only **after** Baseline A/B/C results were already known (`5a3f54a`) —
   Strategy D is an Owner-generated **post-result** alternative hypothesis, never an anti-hindsight
   pre-registered rule.
2. D-H0 (mechanical semantics validation, `486b994`) used the **already-seen** `2018-01-02 →
   2020-06-26` `NDXJPY` window — the same span already released and used for the first Mode-P
   historical run.
3. D-H1 dataset-selection **policy** (`f8332a5`) was frozen **before** any D-H1 candidate was
   selected.
4. The D-H1 deterministic **selection rule** was frozen at `f025bbf` **before** it was executed.
5. The D-H1 rule was executed **without price-value inspection** — only metadata (checksums, provenance
   text, dates-only spine file, and existing policy text) was read.
6. It mechanically selected `NDXJPY`, window `1985-01-31 → 1987-07-26`, on the first tier evaluated
   (Option A), with no tie-break needed.
7. **D-H1 mechanical run succeeded; D-H1 economic result was preserved** (`2fb87c3`).
8. The D-H2 authorization approved executing the same frozen rules again for a second, independent validation window.
9. **The D-H2 deterministic selection rule was executed without price-value inspection** — only metadata.
10. It mechanically selected `NDXJPY`, window `1987-07-27 → 1990-01-18`, on the first tier (Option A).
11. D-H2 selection audit confirmed that deferral of DH1-R6 continuity verification to extraction was compliant.
12. **D-H2 bounded extraction executed; DH1-R6 passed (continuity ratio 0.9692 ≥ 0.90).**
13. D-H2 input is now frozen and ready for mechanical execution (authorized separately).

**This chronology is the entire basis for calling both D-H1 and D-H2 "independent validation windows"** (§9).

---

## 2. Selected D-H2 input — provenance verification

| Field | Value |
| --- | --- |
| Instrument | `NDXJPY` |
| Source | Stage-D `E-01`, `AdditionalData_NDXJPY.csv`, Nasdaq, retrieved 2026-08-11 |
| Selected window | `1987-07-27 → 1990-01-18` |
| Window duration | `906` calendar days (same as D-H1 window duration) |
| Observed rows (actual count) | `629` |
| Weekday-count denominator | `649` |
| Continuity ratio (DH1-R6) | `629 / 649 = 0.969183 ≥ 0.90` ✓ |
| Stage-D parent-file checksum | `316dd1a882002d28430a60a966a31601e3224b2bc84346c906f64715b38d52b0` |
| Extracted D-H2 file checksum | `992a40e39b5ec0c037ad2b547e3e78c911c01943cbf68596a67f653827fe654c` |
| Extraction evidence store | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh2-selection/` |
| Freeze timestamp | `2026-08-14 13:20 UTC` |

All values above are **re-stated from**, not re-derived by, the extraction/freeze process — this artifact performs
no new extraction and inspects no price value.

**The Owner has accepted this mechanically extracted and frozen result.** This is the one-shot
D-H2 input selected and extracted under the frozen rule and policy.

---

## 3. The prior NDXJPY releases do NOT cover this span

Re-verified independently:

- D-H0 Mode-P release (`73d6f51`): explicitly covers `2018-01-02 → 2020-06-26` only; explicitly prohibits span extension.
- D-H1 release (`b722fb2`): explicitly covers `1985-01-31 → 1987-07-26` only; explicitly prohibits span extension.

**This decision does not reinterpret the old releases as covering `1987-07-27 → 1990-01-18`.** It is a
wholly new, additively-scoped release, justified independently below — not an extension of either prior release.

---

## 4. Exact state of the restriction for this new span

The same three provisions bear on the held material, re-assessed for the new span (identical reasoning to D-H1):

| Provision | Verbatim effect | Bearing on `1987-07-27 → 1990-01-18` |
| --- | --- | --- |
| **`D-5`** (Stage-D) | *"retrieval is not analysis; `SC-16` triggers only if a determination would require analysing values"* | **Permissive**, same as for prior spans — nothing about this provision is span-specific |
| **`S.2` minimisation rule** (criteria freeze `1e8bc85`) | *"retain the minimum material necessary and do not analyse the values"* | **The operative restriction**, uniformly, over the whole `E-01` file — cured here by the same mechanism (an express, narrow Owner release) as it was for prior spans |
| Stage-D `PROVENANCE.md` | *"retained for local audit and re-verification only"* | Same self-imposed retention scope; widened here, narrowly, for this new span |

**No new obstruction found.** The analysis that cleared NDXJPY for D-H0 and D-H1 contains no span-specific clause;
that finding extends cleanly to this span. The **only** reason this span was not already usable is that prior releases
were deliberately narrow — not because any additional prohibition applies here. **Owner release is therefore sufficient.**

### Stop conditions checked and NOT triggered (re-checked for this span)

| Condition | Assessment |
| --- | --- |
| **`SC-16`** | Not triggered — Mode P / D-H1 / D-H2 mechanical validation makes no qualification determination; identical reasoning to prior releases |
| **`SC-18`** | Not engaged — no frozen criterion changes; the D-H2 policy (`f8332a5`), rule (`f025bbf`), and authorization (`3c687c8`) are all unmodified by this release |
| **`AC-1`** | Untouched — this artifact changes no criterion |
| **`P1-8`** / redistribution | Unaffected — nothing published, redistributed, or committed beyond this decision text |
| `S.2` external-storage rule | Satisfied and preserved — the released bytes remain in the external evidence store; the repository holds no raw data |

**No independent repository provision prohibits this bounded use.**

---

## 5. §18.4.7 — anti-contamination acceptance, extended to this second NDXJPY span

`NDXJPY` remains one of the three active `C-1` qualification candidates, **regardless of which spans of
its data are used**. D-H0 Mode-P and D-H1 already accepted that running Simulation Trial on `NDXJPY` values
creates permanent, irreversible entanglement (§18.4.7: *"Blinding is neither claimed nor practical"*).
This release **extends, not duplicates**, that same accepted cost to a third span of the same instrument:

**What every future qualification artifact must now disclose (extended).** Any artifact deciding
`O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`, Stage G, Stage H, or Primary Proxy selection — for **any**
candidate — must state that Simulation Trial results exist on `NDXJPY` for **three** separate spans:
(1) `2018-01-02 → 2020-06-26` (D-H0 Mode-P, `73d6f51`), (2) `1985-01-31 → 1987-07-26` (D-H1, `b722fb2`),
and (3) `1987-07-27 → 1990-01-18` (D-H2, this decision), and affirm none was used normatively.

**What must remain logically separated.** Mechanical Strategy-D behaviour on this window is **not**
evidence about `NDXJPY`'s suitability, continuity, return composition, licensing, or qualification.

**What cannot be inferred from any resulting D-H2 result — ever.** That `NDXJPY` is suitable or
unsuitable as a Primary Proxy candidate; anything about `O-4`, `HG-8`, `P1-2`, `P1-5`, `P1-6`, or `H-1`;
that its data quality is adequate for formal work; that Strategy D is economically superior, inferior,
or equivalent to A/B/C; that D-H2 result generalization beyond these windows; or that D-H1 and D-H2
together constitute statistical validation.

---

## 6. Limitation classification

### HARD BLOCKER
**None found.**

### CONDITIONAL / ACCEPTABLE WITH DISCLOSURE
- The `S.2` non-analysis undertaking over this span — cured **only** by this express release.
- §18.4.7 entanglement, extended to a third `NDXJPY` span — cured by the extended acceptance (§5).
- Stage-D retention scope *"local audit and re-verification only"* — widened, narrowly, by this release.

### NON-BLOCKING IMPERFECTION
- Single price series; no cross-source corroboration — irrelevant to mechanical validation, same as prior spans.
- Back-tested vs. actual history for this earlier segment is, if anything, **more** likely to be
  back-tested than the 2020 segment — **not established**, and **not** a blocker for a disclosed,
  non-formal, mechanical D-H2 run.

### FORMAL-ONLY ISSUE
- Return composition (`P1-3`) — unchanged, unverified, not this artifact's concern.
- `P1-1`, `P1-4`, `P1-7`, `P1-8`, `P1-9`, `M-1…M-8` — all unchanged and unaffected.

---

## 7. Owner Decision Sheet

> ### `DH2-REL-1` — Release decision
> **Question.** May the already-held Stage-D `NDXJPY` (`E-01`) bytes be released from the `S.2`
> non-analysis undertaking and Stage-D retention scope, for the D-H2 window `1987-07-27 →
> 1990-01-18` only, for Strategy-D Stage D-H2 independent mechanical validation?
>
> **Disposition: APPROVE WITH CONDITIONS `[APPROVED — OWNER DECISION 2026-08-14]`** (§8).
>
> **Controlling reason.** No repository provision prohibits it (§4). `D-5` is permissive; `SC-16`
> governs study determinations and D-H2 mechanical validation makes none; `SC-18` is not engaged;
> §18.4.7 imposes disclosure, not prohibition. The prior releases do not cover this span and are not
> reinterpreted to do so (§3) — this is an independent, additively-scoped release resting on the same
> underlying, span-general eight-axis/S.2 analysis. **Owner release is therefore sufficient.**
>
> **Unresolved even if approved:** `P1-2`, `P1-3`, `P1-9`, `O-4`, `HG-8`, `H-1`, all `M-x`. No
> candidate is qualified; no Primary Proxy exists; no Strategy-D adoption occurs.

> ### `DH2-REL-2` — §18.4.7 anti-contamination acceptance, extended
> **Question.** Accept the resulting disclosure duty and separation requirements, extended to a
> third `NDXJPY` span?
>
> **Disposition: ACCEPT `[ACCEPTED — OWNER DECISION 2026-08-14]`.** The Owner has expressly accepted
> that a third set of Simulation Trial results on `NDXJPY`, once observed, cannot be unseen.
>
> **Exact ongoing cost.** Every future artifact deciding `O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`, Stage
> G, Stage H, or Primary Proxy selection — for **any** candidate — must state that D-H1 results on
> the `1985-01-31 → 1987-07-26` span and D-H2 results on the `1987-07-27 → 1990-01-18` span were known
> and affirm they were not used normatively, **in addition to** the existing D-H0 disclosure. §18.4.7 is
> **not** weakened by this acceptance.

> ### `DH2-REL-3` — Dataset classification
> **Question.** May it be labelled `dataset_class: "provisional"`, and what further labels are
> required?
>
> **Disposition: APPROVE `[APPROVED — OWNER DECISION 2026-08-14]`** — `dataset_class: "provisional"`
> per §18.4.9, **plus** these mandatory labels in the manifest and every output, once execution is
> separately authorized (§10):
>
> - `PROVISIONAL · NOT QUALIFIED · NON-FORMAL · NON-PROMOTABLE · SIMULATION-TRIAL ONLY`
> - `SOURCE: STAGE-D QUALIFICATION EVIDENCE, RELEASED FOR SIMULATION USE ONLY`
> - `NDXJPY IS AN ACTIVE C-1 QUALIFICATION CANDIDATE — THIS RUN IS NOT EVIDENCE ABOUT IT`
> - `NOT A PRIMARY PROXY SELECTION — P1-2 REMAINS OPEN`
> - `STRATEGY D STAGE D-H2 — DETERMINISTICALLY SELECTED BEFORE VALUE INSPECTION`
> - `SECOND INDEPENDENT VALIDATION INPUT (D-H1 IS THE FIRST)`
> - `BACK-TESTED VS ACTUAL HISTORY NOT ESTABLISHED FOR THIS SEGMENT`
> - `RETURN COMPOSITION DECLARED, NOT VERIFIED — P1-3 OPEN`

No further Owner decisions are required **to complete the release itself**. A separate authorization
is required before Strategy-D execution (§10).

---

## 8. Minimum bounded release, as approved

`NDXJPY` **only** — `XNDXJPY` and `XNDXNNRJPY` are **not** released under this decision. The
already-held Stage-D `E-01` snapshot **only**, byte-identical, checksum-verified before use against
the Stage-D `SHA256SUMS` (`316dd1a882002d28430a60a966a31601e3224b2bc84346c906f64715b38d52b0`, verified
OK on 2026-08-14, during extraction). Window **`1987-07-27 → 1990-01-18` only**. Extracted
file: `DH2_NDXJPY_1987-07-27_1990-01-18.csv`, checksum `992a40e39b5ec0c037ad2b547e3e78c911c01943cbf68596a67f653827fe654c`.

**Prohibited:** replacement or enrichment; span extension beyond `1987-07-27 → 1990-01-18`; a second
source; source blending; `XNDXJPY`; `XNDXNNRJPY`; fresh acquisition; web/API/curl use; any
qualification-state change; any formal metric; TTEV or any governed economic metric; result promotion;
Phase-2 use; and any inference that `NDXJPY` is the Primary Proxy.

**Traceability.** The eventual D-H2 mechanical-result checkpoint must cite Stage-D item `E-01`, its original
retrieval date **2026-08-11**, its Stage-D SHA-256, the extracted-window checksum, and this decision's commit
— so the released material remains traceable to its original provenance. **The Stage-D evidence store is read-only
to this work and MUST NOT be modified**; a separate D-H2 evidence store is used (created at
`~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh2-selection/`). Raw data
remains **structurally outside** the repository, as `S.2` requires.

---

## 9. Independent-validation status — permitted and prohibited claims

**Permitted claim, if a Strategy-D mechanical run on this window later succeeds:** Strategy D was
executed on a window selected and frozen (deterministic rule execution, compliance audit, extraction)
before Strategy-D behavior on that window was inspected.

**Prohibited claims — none of the following may be inferred automatically from that result:**
statistical generalization; robustness across regimes; economic superiority; formal validation; or
Strategy D adoption. Each requires its own later decision and its own evidence — this release
authorizes none of them.

---

## 10. Strategy-D execution boundary — release and execution are NOT combined here

**Repository precedent requires separation.** The D-H1 bounded release did not itself authorize or perform
the first D-H1 mechanical run; they are two separate commits. This decision follows that same precedent:
**it authorizes release only.**

**D-H2 INPUT RELEASED — STRATEGY D NOT YET EXECUTED.**

The exact next authorization required is a separate Owner task authorizing the first D-H2 mechanical
Strategy-D run on this released input, bounded to mechanical-only outputs (observations, zone
classifications, allocations, tranche types, commitments, reservations, executions, suppressions,
monthly capacity, funding/accounting state, invariant results, terminal mechanical state — never
terminal market value, TTEV, return, CAGR, XIRR, Sharpe, or any A/B/C/D ranking), per §18.4.3.

---

## 11. Failure-handling policy (recorded now, for the future execution task)

If the future execution discovers corrupt bytes, a checksum mismatch, a schema defect, a continuity
violation, or a provenance conflict: **STOP.** Do not select a replacement candidate. Return to Owner
Review.

If Strategy D itself fails mechanically: preserve the failing evidence; do not modify Strategy D
silently; classify the failure. If a substantive Strategy-D semantic change is required after seeing
D-H2 behavior, the existing D-H2 input **cannot** independently validate the modified Strategy-D version
— that consequence is preserved explicitly here, in advance, for the future task to inherit.

---

## 12. State preservation

Unchanged by this artifact: `O4-PARTIAL ×3` · `GAP-A ×3` · `GAP-B ×2` · `HG-8 NOT EVALUABLE ×3` ·
`P1-2 OPEN` · `P1-5 OPEN` · `P1-6 OPEN` · `H-1 NOT ESTABLISHED` · `P1-9 PARTIAL` ·
`C-1 ×3 QUALIFICATION INCOMPLETE` · **no Primary Proxy** · Stage G **OPEN** · Stage H **NOT BEGUN** ·
Phase 2 **BLOCKED** · `M-1 … M-8` unresolved · Mode P / D-H1 / D-H2 **NON-FORMAL and NON-PROMOTABLE**. The
Frozen Baseline, the criteria freeze `1e8bc85`, the D-H1 policy (`f8332a5`), D-H1 rule (`f025bbf`),
D-H2 authorization (`3c687c8`) are **not altered**. The prior releases (`73d6f51`, `b722fb2`) are
**not altered** and their spans remain exactly as specified.

---

## 13. Scope

This decision does not run Strategy D, execute A/B/C, perform economic evaluation, modify any
qualification-lane state, resolve any `P1-x`/`M-x` item, or treat any Simulation Trial output as formal evidence.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. Release and extraction only —
Strategy-D execution is a separate, not-yet-authorized future task (§10). No price value was inspected
for analysis in preparing or approving this artifact. `f8332a5`, `f025bbf`, `3c687c8`, `b722fb2`, `73d6f51`,
and every preserved Strategy-D and Mode-P artifact are unchanged.**
