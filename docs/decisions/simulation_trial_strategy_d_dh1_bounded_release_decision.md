# Simulation Trial — Strategy D Stage D-H1: Bounded Release of `NDXJPY` `1985-01-31 → 1987-07-26`

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.**
`DH1-REL-1` **APPROVE WITH CONDITIONS** · `DH1-REL-2` **ACCEPT** · `DH1-REL-3` **APPROVE**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13)
**Controlling D-H1 policy:** `docs/decisions/simulation_trial_strategy_d_dh1_dataset_selection_policy.md`,
commit `f8332a543f7bab4c8b5f42974813ccd70be9137f`,
tag `simulation-trial-strategy-d-dh1-dataset-selection-policy-20260814` — **not modified by this artifact.**
**Controlling D-H1 deterministic rule:** `docs/decisions/simulation_trial_strategy_d_dh1_deterministic_selection_rule.md`,
commit `f025bbf0dd5df9a4b037936822b1ced4e263948c`,
tag `simulation-trial-strategy-d-dh1-deterministic-selection-rule-20260814` — **not modified by this artifact.**
**Prior, narrower NDXJPY release (does NOT cover this span — see §3):**
`docs/decisions/simulation_trial_mode_p_ndxjpy_bounded_release_decision.md`,
commit `73d6f512a5034a7e0164bfd19d69816460debb20`,
tag `simulation-trial-mode-p-ndxjpy-bounded-release-20260814` — **not modified by this artifact.**
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
3. The D-H1 dataset-selection **policy** (`f8332a5`) was frozen **before** any D-H1 candidate was
   selected.
4. The D-H1 deterministic **selection rule** was frozen at `f025bbf` **before** it was executed.
5. The rule was executed **without price-value inspection** — only metadata (checksums, provenance
   text, a dates-only spine file, and existing policy text) was read.
6. It mechanically selected `NDXJPY`, window `1985-01-31 → 1987-07-26`, on the first tier evaluated
   (Option A), with no tie-break needed.
7. **No Strategy-D result for this window existed when the window was selected** — the selection
   trace (`selection_trace.json`) and this decision are both dated after selection, before any value
   inspection.
8. **No price value from the selected window was inspected before freeze.** The freeze record
   (`PROVENANCE.md` in the selection-evidence store) states explicitly what was and was not read.

This chronology is the entire basis for calling the eventual Strategy-D run on this window
"independent" in any sense (§9).

---

## 2. Selected D-H1 input — provenance verification

| Field | Value |
| --- | --- |
| Instrument | `NDXJPY` |
| Source | Stage-D `E-01`, `AdditionalData_NDXJPY.csv`, Nasdaq, retrieved 2026-08-11 |
| Selected window | `1985-01-31 → 1987-07-26` |
| Window duration | `906` calendar days (`DH1-R3`: `(2020-06-26 − 2018-01-02).days`) |
| Observed rows | `627` |
| Weekday-count denominator | `647` |
| Continuity ratio | `627 / 647 ≈ 0.9691 ≥ 0.90` (`DH1-R6`) |
| Temporal distance from D-H0 start | `11,118` calendar days `≥ 1,825`-day backstop (`DH1-R5`) |
| Stage-D parent-file checksum | `316dd1a882002d28430a60a966a31601e3224b2bc84346c906f64715b38d52b0` |
| Selection trace | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh1-selection/selection_trace.json`, sha256 `fddffddf6d5a06ebee4aa0c9a7299b6429b15e87626b03411bbc853325d459ca` |
| Freeze provenance | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh1-selection/PROVENANCE.md`, sha256 `a1c50f42e660211086a3019756ae077e4e3fa8eb75a83ed8e3c2ec0ac5098fa6` |

All values above are **re-stated from**, not re-derived by, the selection trace — this artifact performs
no new computation and inspects no price value.

**The Owner has accepted this mechanically selected result and directed: do not re-run the selection
rule, do not substitute another window, do not inspect an alternative candidate.** This is the one-shot
D-H1 input selected under the frozen rule.

---

## 3. The prior NDXJPY release does NOT cover this span

Re-read directly against `73d6f512a5034a7e0164bfd19d69816460debb20` (re-verified unchanged, checksum
`2bf10377ae5fc3e72d3dd3e7e291bbffb8b8f9dc2e37b09e2c1a378b3d3a375c`, this task):

- §6 of that decision states the **minimum bounded release** as `NDXJPY` **only**, the already-held
  Stage-D snapshot **only**, **span `2018-01-02 → 2020-06-26` only**, and lists **"span extension"**
  first among explicitly **prohibited** actions.
- Nothing in that decision purports to cover, extend to, or pre-authorize use of any other span of the
  same `E-01` file.

**This decision does not reinterpret the old release as covering `1985-01-31 → 1987-07-26`.** It is a
wholly new, additively-scoped release, justified independently below — not an extension of `73d6f51`.

---

## 4. Exact state of the restriction for this new span

The same three provisions bear on the held material, re-assessed for the new span (this reasoning was
already performed once, as the `RETENTION_NOT_PERMITTED` test, during rule execution — restated here
for the decision record, not re-derived):

| Provision | Verbatim effect | Bearing on `1985-01-31 → 1987-07-26` |
| --- | --- | --- |
| **`D-5`** (Stage-D) | *"retrieval is not analysis; `SC-16` triggers only if a determination would require analysing values"* | **Permissive**, same as for the 2018-2020 span — nothing about this provision is span-specific |
| **`S.2` minimisation rule** (criteria freeze `1e8bc85`) | *"retain the minimum material necessary and do not analyse the values"* | **The operative restriction**, uniformly, over the whole `E-01` file — cured here by the same mechanism (an express, narrow Owner release) as it was for the 2018-2020 span |
| Stage-D `PROVENANCE.md` | *"retained for local audit and re-verification only"* | Same self-imposed retention scope; widened here, narrowly, exactly as `73d6f51` widened it for the other span |

**No new obstruction found.** `73d6f51` §4 found "HARD BLOCKER: None found" on an analysis that
contains no span-specific clause; that finding extends cleanly to this span. The **only** reason this
span was not already usable is that `73d6f51`'s own release was deliberately narrow (§3) — not because
any additional prohibition applies here. **Owner release is therefore sufficient, exactly as it was for
the first span.**

### Stop conditions checked and NOT triggered (re-checked for this span)

| Condition | Assessment |
| --- | --- |
| **`SC-16`** | Not triggered — Mode P / D-H1 mechanical validation makes no qualification determination; identical reasoning to `73d6f51` §2, `D-5` applies without modification |
| **`SC-18`** | Not engaged — no frozen criterion changes; the D-H1 policy (`f8332a5`) and rule (`f025bbf`) are both unmodified by this release |
| **`AC-1`** | Untouched — this artifact changes no criterion |
| **`P1-8`** / redistribution | Unaffected — nothing published, redistributed, or committed beyond this decision text |
| `S.2` external-storage rule | Satisfied and preserved — the released bytes remain in the external evidence store; the repository holds no raw data |

**No independent repository provision prohibits this bounded use.**

---

## 5. §18.4.7 — anti-contamination acceptance, extended to this span

`NDXJPY` remains one of the three active `C-1` qualification candidates, **regardless of which span of
its data is used**. `73d6f51` already accepted that running any Simulation Trial on `NDXJPY` values
creates permanent, irreversible entanglement (§18.4.7: *"Blinding is neither claimed nor practical"*).
This release **extends, not duplicates**, that same accepted cost to a second span of the same
instrument:

**What every future qualification artifact must now disclose (extended).** Any artifact deciding
`O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`, Stage G, Stage H, or Primary Proxy selection — for **any**
candidate — must state that Simulation Trial results exist on `NDXJPY` for **both** the `2018-01-02 →
2020-06-26` span (`73d6f51`) **and** the `1985-01-31 → 1987-07-26` span (this decision), and affirm
neither was used normatively.

**What must remain logically separated.** Mechanical Strategy-D behaviour on this window is **not**
evidence about `NDXJPY`'s suitability, continuity, return composition, licensing, or qualification.

**What cannot be inferred from any resulting D-H1 result — ever.** That `NDXJPY` is suitable or
unsuitable as a Primary Proxy candidate; anything about `O-4`, `HG-8`, `P1-2`, `P1-5`, `P1-6`, or `H-1`;
that its data quality is adequate for formal work; that Strategy D is economically superior or inferior
to A/B/C; or that this D-H1 result generalizes beyond this one window.

---

## 6. Limitation classification

### HARD BLOCKER
**None found.**

### CONDITIONAL / ACCEPTABLE WITH DISCLOSURE
- The `S.2` non-analysis undertaking over this span — cured **only** by this express release.
- §18.4.7 entanglement, extended to a second `NDXJPY` span — cured by the extended acceptance (§5).
- Stage-D retention scope *"local audit and re-verification only"* — widened, narrowly, by this release.

### NON-BLOCKING IMPERFECTION
- Single price series; no cross-source corroboration — irrelevant to mechanical validation, same as
  `73d6f51`.
- Back-tested vs. actual history for this earlier segment is, if anything, **more** likely to be
  back-tested than the 2018-2020 segment (Stage-D `E-09` records no launch-date register for the JPY
  series at all) — **not established**, and **not** a blocker for a disclosed, non-formal, mechanical
  D-H1 run, exactly as the same uncertainty was not a blocker for `73d6f51`.

### FORMAL-ONLY ISSUE
- Return composition (`P1-3`) — unchanged, unverified, not this artifact's concern.
- `P1-1`, `P1-4`, `P1-7`, `P1-8`, `P1-9`, `M-1…M-8` — all unchanged and unaffected.

---

## 7. Owner Decision Sheet

> ### `DH1-REL-1` — Release decision
> **Question.** May the already-held Stage-D `NDXJPY` (`E-01`) bytes be released from the `S.2`
> non-analysis undertaking and Stage-D retention scope, for the D-H1 window `1985-01-31 →
> 1987-07-26` only, for Strategy-D Stage D-H1 independent mechanical validation?
>
> **Disposition: APPROVE WITH CONDITIONS `[APPROVED — OWNER DECISION 2026-08-14]`** (§8).
>
> **Controlling reason.** No repository provision prohibits it (§4). `D-5` is permissive; `SC-16`
> governs study determinations and D-H1 mechanical validation makes none; `SC-18` is not engaged;
> §18.4.7 imposes disclosure, not prohibition. The prior release (`73d6f51`) does not cover this span
> and is not reinterpreted to do so (§3) — this is an independent, additively-scoped release resting
> on the same underlying, span-general eight-axis/S.2 analysis. **Owner release is therefore
> sufficient.**
>
> **Unresolved even if approved:** `P1-2`, `P1-3`, `P1-9`, `O-4`, `HG-8`, `H-1`, all `M-x`. No
> candidate is qualified; no Primary Proxy exists; no Strategy-D adoption occurs.

> ### `DH1-REL-2` — §18.4.7 anti-contamination acceptance, extended
> **Question.** Accept the resulting disclosure duty and separation requirements, extended to a
> second `NDXJPY` span?
>
> **Disposition: ACCEPT `[ACCEPTED — OWNER DECISION 2026-08-14]`.** The Owner has expressly accepted
> that a second set of Simulation Trial results on `NDXJPY`, once observed, cannot be unseen.
>
> **Exact ongoing cost.** Every future artifact deciding `O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`, Stage
> G, Stage H, or Primary Proxy selection — for **any** candidate — must state that D-H1 results on
> this `NDXJPY` span were known and affirm they were not used normatively, **in addition to** the
> existing `73d6f51` disclosure. §18.4.7 is **not** weakened by this acceptance.

> ### `DH1-REL-3` — Dataset classification
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
> - `STRATEGY D STAGE D-H1 — DETERMINISTICALLY SELECTED BEFORE VALUE INSPECTION`
> - `ONE-SHOT INDEPENDENT VALIDATION INPUT`
> - `BACK-TESTED VS ACTUAL HISTORY NOT ESTABLISHED FOR THIS SEGMENT`
> - `RETURN COMPOSITION DECLARED, NOT VERIFIED — P1-3 OPEN`

No further Owner decisions are required **to complete the release itself**. A separate authorization
is required before execution (§10).

---

## 8. Minimum bounded release, as approved

`NDXJPY` **only** — `XNDXJPY` and `XNDXNNRJPY` are **not** released under this decision. The
already-held Stage-D `E-01` snapshot **only**, byte-identical, checksum-verified before use against
the Stage-D `SHA256SUMS` (`316dd1a882002d28430a60a966a31601e3224b2bc84346c906f64715b38d52b0`, verified
OK on 2026-08-14, during rule execution). Window **`1985-01-31 → 1987-07-26` only**.

**Prohibited:** replacement or enrichment; span extension beyond `1985-01-31 → 1987-07-26`; a second
source; source blending; `XNDXJPY`; `XNDXNNRJPY`; fresh acquisition; web/API/curl use; any
qualification-state change; any formal metric; TTEV or any governed economic metric; result promotion;
Phase-2 use; and any inference that `NDXJPY` is the Primary Proxy.

**Traceability.** The eventual D-H1 dataset record must cite Stage-D item `E-01`, its original
retrieval date **2026-08-11**, its Stage-D SHA-256, and this decision's commit — so the released
material remains traceable to its original provenance. **The Stage-D evidence store is read-only to
this work and MUST NOT be modified**; a separate D-H1 evidence store is used (already created at
`~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh1-selection/`). Raw data
remains **structurally outside** the repository, as `S.2` requires.

---

## 9. Independent-validation status — permitted and prohibited claims

**Permitted claim, if a Strategy-D mechanical run on this window later succeeds:** Strategy D was
executed on a window selected and frozen (§1, `DH1-R12`) before Strategy-D behavior on that window was
inspected.

**Prohibited claims — none of the following may be inferred automatically from that result:**
statistical generalization; robustness across regimes; economic superiority; formal validation; or
Strategy D adoption. Each requires its own later decision and its own evidence — this release
authorizes none of them.

---

## 10. Strategy-D execution boundary — release and execution are NOT combined here

**Repository precedent requires separation.** The prior `NDXJPY` bounded release (`73d6f51`) did not
itself authorize or perform the first Mode-P historical run: `73d6f51` §8 states execution as **the
next instruction**, not an action taken within that same decision, and the actual repository history
confirms this — `73d6f51` (the release) and `da85b66` (the first plumbing/execution-adjacent commit)
are two separate commits, roughly 24 minutes apart, under two separately authorized tasks. This
decision follows that same precedent: **it authorizes release only.**

**D-H1 INPUT RELEASED — STRATEGY D NOT YET EXECUTED.**

The exact next authorization required is a separate Owner task authorizing the first D-H1 mechanical
Strategy-D run on this released input, bounded to mechanical-only outputs (observations, zone
classifications, allocations, tranche types, commitments, reservations, executions, suppressions,
monthly capacity, funding/accounting state, invariant results, terminal mechanical state — never
terminal market value, TTEV, return, CAGR, XIRR, Sharpe, or any A/B/C/D ranking), per §18.4.3 and
`MP-D3`'s existing definition-free output boundary, extended to Strategy D by `f16a815`/`486b994`.

---

## 11. Failure-handling policy (recorded now, for the future execution task)

If the future execution discovers corrupt bytes, a checksum mismatch, a schema defect, a continuity
violation, or a provenance conflict: **STOP.** Do not select a replacement candidate. Return to Owner
Review under the frozen one-shot/replacement policy (`f8332a5`, `f025bbf` `DH1-R14`/`DH1-R15`).

If Strategy D itself fails mechanically: preserve the failing evidence; do not modify Strategy D
silently; classify the failure as an implementation defect, a loader/plumbing defect, an evidence
defect, or a semantic defect. If a substantive Strategy-D semantic change is required after seeing
D-H1 behavior, the existing D-H1 input **cannot** independently validate the modified Strategy-D
version (`f8332a5` §15 / `DH1-R14`, extended from the strategy to its input) — that consequence is
preserved explicitly here, in advance, for the future task to inherit.

---

## 12. State preservation

Unchanged by this artifact: `O4-PARTIAL ×3` · `GAP-A ×3` · `GAP-B ×2` · `HG-8 NOT EVALUABLE ×3` ·
`P1-2 OPEN` · `P1-5 OPEN` · `P1-6 OPEN` · `H-1 NOT ESTABLISHED` · `P1-9 PARTIAL` ·
`C-1 ×3 QUALIFICATION INCOMPLETE` · **no Primary Proxy** · Stage G **OPEN** · Stage H **NOT BEGUN** ·
Phase 2 **BLOCKED** · `M-1 … M-8` unresolved · Mode P / D-H1 **NON-FORMAL and NON-PROMOTABLE**. The
Frozen Baseline, the criteria freeze `1e8bc85`, the D-H1 policy (`f8332a5`), and the D-H1 deterministic
rule (`f025bbf`) are **not altered**. The prior `NDXJPY` release (`73d6f51`) is **not altered** and its
own span remains exactly `2018-01-02 → 2020-06-26`.

---

## 13. Scope

This decision does not retrieve data, select or re-select a candidate, execute Strategy D, execute
A/B/C, perform economic evaluation, modify any qualification-lane state, resolve any `P1-x`/`M-x` item,
or treat any Simulation Trial output as formal evidence.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. Release only — Strategy-D execution
is a separate, not-yet-authorized future task (§10). No price value was inspected in preparing or
approving this artifact. `f8332a5`, `f025bbf`, `73d6f51`, and every preserved Strategy-D artifact are
unchanged.**
