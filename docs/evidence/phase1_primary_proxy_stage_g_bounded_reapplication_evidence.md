# Phase 1 Evidence Artifact — Primary Proxy Qualification, Stage G: Bounded Reapplication of `HG-6` and `HG-12`

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Primary Proxy Candidate Qualification — Stage G, bounded reapplication** |
| Scope | **`HG-6` and `HG-12` only**, for the three C-1 candidates. No other candidate/gate combination was re-evaluated |
| Application date | **2026-08-12** |
| Authorising decisions | Stage-G authorization semantics [`phase1_primary_proxy_stage_g_authorization_decision.md`](../decisions/phase1_primary_proxy_stage_g_authorization_decision.md); [`…hg6_capability_interpretation_decision.md`](../decisions/phase1_primary_proxy_hg6_capability_interpretation_decision.md); [`…sc6_post_base_segment_interpretation_decision.md`](../decisions/phase1_primary_proxy_sc6_post_base_segment_interpretation_decision.md); [`…hg9_revision_restatement_decision.md`](../decisions/phase1_primary_proxy_hg9_revision_restatement_decision.md) |
| Closure decision | [`phase1_primary_proxy_stage_g_bounded_reapplication_decision.md`](../decisions/phase1_primary_proxy_stage_g_bounded_reapplication_decision.md) |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](../decisions/phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Owner Review | **PENDING — prepared for Owner Review** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged** |
| Criteria-freeze status | **UNCHANGED** |
| Publication classification | **PUBLIC QUALITATIVE EVIDENCE** — gate outcomes, reasoning, and classifications only |
| Historical values | **NONE PUBLISHED.** No observation value, return, or derived statistic appears |
| Source material | Retained **outside** the repository. No retrieval artifact, provenance index, checksum file, endpoint capture, or access-policy capture enters Git |
| Stage G as a whole | **REMAINS OPEN** — `HG-8` is unresolved |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Phase 2 | **BLOCKED** |

> **What this artifact is.** The record of a **bounded, additive** reapplication of two hard gates
> under interpretations settled after the original Stage-G application. It is **not** a Stage-G
> closure artifact, **not** a full rerun, and **not** a retroactive edit of the earlier result.

> **Additive, not corrective.** The previous Stage-G execution result stands as the result of the
> application actually performed under the semantics then in force. This artifact records a **new
> decision layer** applied later, on interpretations and evidence that did not exist at that time.

**Relationship to other documents.** The normative Baseline remains
[`../experiment_spec.md`](../experiment_spec.md). The frozen criteria are **used, never amended,
here**. Stage-C, Stage-D, Stage-E and Stage-F findings remain authoritative for their own stages and
are unmodified.

---

## 2. What was reapplied, and why it could be

| Gate | Why reapplication became possible |
| ---- | --------------------------------- |
| **`HG-6`** | The committed `HG-6` capability interpretation settled that the gate is a construction-capability finding, that pre-start warm-up is permissive, and that `SC-6` alone is not a basis for NOT EVALUABLE or FAIL |
| **`HG-12`** | The committed `SC-6` post-base-date interpretation settled that `SC-6` exclusion is **not established** for the post-base-date segment and adopted **I-1** — capability only, with affirmative LIVE establishment not required — and a bounded, Owner-ratified capability investigation supplied the access evidence |

**Nothing else was re-evaluated.** `HG-1` … `HG-5`, `HG-7`, `HG-8`, `HG-10`, `HG-11` and `HG-13`
retain their existing results. `HG-9` is separately governed by its own committed Owner Decision.

---

## 3. Candidate scope

`NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` — carried **symmetrically and distinctly**, per `AC-4`. The same
outcomes are recorded for each, but candidate identity remains explicit and the three are **not
collapsed into one candidate**.

**C-2A was outside this reapplication** and is unchanged in every respect.

---

## 4. `HG-6` — reasoning and result

### 4.1 Reasoning preserved

- **`HG-6` is a construction-capability finding.** It asks whether the Frozen Baseline §7
  Reference-High construction can operate without look-ahead — not whether an admissible historical
  dataset is already held.
- **The Reference High uses only observations available through *t*.** A running maximum over
  closes available to that point cannot reference the future; the look-ahead freedom is a property
  of the construction itself.
- **Optional pre-start warm-up is not required.** §7 makes warm-up permissive, so its absence does
  not defeat the gate; the Reference High may seed from within the measured period.
- **`SC-6` exclusion of the pre-base-date segment remains fully effective**, and that segment was
  **not used**.
- **`SC-6` alone does not defeat `HG-6`** — excluding *optional* warm-up observations does not make
  the construction incapable of operating without look-ahead.
- **`HG-9` is separate and was not duplicated inside `HG-6`.** The point-in-time / revision question
  belongs to `HG-9` and was neither imported nor inferred here.

Supporting documentary facts, already established at Stages C and E: each candidate is a single
published series with one end-of-day observation basis, with currency conversion embedded in the
same calculation — so the Reference High and the current value necessarily come from the same series
on the same basis, as §7 requires.

### 4.2 Result

| Candidate | Previous | **Reapplied** |
| --------- | -------- | ------------- |
| `NDXJPY` | NOT EVALUABLE | **PASS** |
| `XNDXJPY` | NOT EVALUABLE | **PASS** |
| `XNDXNNRJPY` | NOT EVALUABLE | **PASS** |

---

## 5. `HG-12` — reasoning and result

### 5.1 Reasoning preserved

Six capability elements, each established for each candidate:

1. **Stable candidate identity** — distinct publisher-defined symbol and series definition.
2. **Publisher-direct access** — a publisher-operated route, with no intermediary and no distributor
   in the chain.
3. **Authorized project-side access** — demonstrated within the governance boundary, with no
   account, login, credentials, entitlement request, payment, personal-information disclosure, terms
   acceptance, or access-control bypass.
4. **Reproducible retrieval** — an identical request, issued twice per candidate, returned an
   identical artifact each time.
5. **Pinning** — each artifact was frozen locally and re-verified; the three candidates produced
   three distinct artifacts, confirming the route discriminates by candidate.
6. **Dataset-cutoff capability** — the request is date-parameterised, so a cutoff can be enforced.

Together with:

- **Affirmative `H-1` LIVE establishment is not required for `HG-12`**, under the committed
  interpretation.
- **The post-base-date segment is not `SC-6`-excluded** under that same interpretation.
- **The `SC-6`-excluded pre-base-date segment was not used.**

### 5.2 Conditions attached to the result

- **The PASS remains a capability finding only.**
- **Eventual full-span retrieval remains a `P1-6` matter.** Capability was demonstrated at minimal
  scale; it does not establish that a full intended span is retrievable by the same route.
- **Access-state changes may require `HG-12` re-evaluation.** The finding rests on the access state
  as it stands.

### 5.3 Result

| Candidate | Previous | **Reapplied** |
| --------- | -------- | ------------- |
| `NDXJPY` | NOT EVALUABLE | **PASS** |
| `XNDXJPY` | NOT EVALUABLE | **PASS** |
| `XNDXNNRJPY` | NOT EVALUABLE | **PASS** |

---

## 6. Resulting C-1 gate state

Identical for `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`:

| Gate | Result |
| ---- | ------ |
| `HG-1` | **PASS** |
| `HG-2` | **PASS** |
| `HG-3` | **PASS** |
| `HG-4` | **PASS** |
| `HG-5` | **PASS** |
| `HG-6` | **PASS** — this reapplication |
| `HG-7` | **PASS** |
| `HG-8` | **NOT EVALUABLE** |
| `HG-9` | **PASS** — by committed Owner Decision, with its recorded limitations |
| `HG-10` | **PASS** |
| `HG-11` | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED** |
| `HG-12` | **PASS** — this reapplication |
| `HG-13` | **PASS** |

Four points recorded explicitly, because the distinctions matter:

1. **`HG-11` is NOT PASS.**
2. **`HG-11` is expressly non-eliminating** under F-11 and `G-OD-02`, and is carried to `OJ-6` as an
   attached Owner condition.
3. **`HG-8` is the sole remaining qualification-blocking gate for C-1.** It is *not* described as the
   sole non-PASS gate, because `HG-11` is also not PASS while being non-eliminating.
4. **`O-4` is the root cause of `HG-8` NOT EVALUABLE** — no methodology version history or publisher
   change log has been located.

---

## 7. Candidate classification

| Candidate | Classification |
| --------- | -------------- |
| `NDXJPY` | **QUALIFICATION INCOMPLETE** |
| `XNDXJPY` | **QUALIFICATION INCOMPLETE** |
| `XNDXNNRJPY` | **QUALIFICATION INCOMPLETE** |

**No candidate is DISQUALIFIED. No candidate is yet a QUALIFIED SURVIVOR.** Under `G-OD-04`,
QUALIFIED SURVIVOR requires every required gate to be resolved sufficiently with no FAIL; `HG-8`
remains NOT EVALUABLE.

---

## 8. What this reapplication does NOT establish

- **Full historical-span admissibility** — not established.
- **`H-1`** — remains **NOT ESTABLISHED**.
- **Point-in-time equivalence** — not established; reserved to `HG-9`'s recorded limitations.
- **`OJ-1`** — not exercised; remains NOT REACHED — DEFERRED.
- **`P1-5`** and **`P1-6`** — not set; both remain OPEN.
- **`HG-8` satisfaction** — not established.
- **`O-4` resolution** — not achieved; remains OPEN.
- **`HG-11` PASS** — not established.
- **Candidate qualification or Primary Proxy selection** — neither.

---

## 9. Anti-circularity verification

- **`AC-1`** — the criteria were applied exactly as frozen at `1e8bc85`. No criterion changed, and
  the controlling interpretations were committed **before** this reapplication, not fitted to it.
- **`AC-2`** — **no performance quantity was computed.** No return, drawdown, correlation, tracking
  statistic, or level comparison was calculated at any point.
- **`AC-3`** — `ND-1 … ND-7` were not used.
- **`AC-4`** — the three candidates were carried symmetrically and distinctly; identical outcomes
  reflect an identical evidence base, not collapse.
- **`AC-8`** — no scoring, no weighting, no ranking. No comparison among candidates was performed.

---

## 10. Publication and external-material boundary

**No historical value appears in this artifact** — no observation, return, level, or derived
statistic.

The capability evidence is retained **structurally outside** the repository. Not committed: retrieval
artifacts; the external provenance index; checksum files; endpoint captures; access-policy captures;
any token-bearing or redacted source page; and checksums of raw publisher observations. Publisher
wording is **characterised, not reproduced**.

Redistribution terms for the underlying source remain **UNCLEAR** on the Stage-F record, so the
fail-closed publication policy applies and nothing is cleared for republication.

---

## 11. Limitations

1. **This is a bounded reapplication of two gates**, not a Stage-G rerun. Every other gate result
   stands as previously recorded.
2. **`HG-12`'s capability was demonstrated at minimal scale.** Full-span retrievability is a `P1-6`
   matter and is not established.
3. **`HG-12` depends on the access state as it stands**; a change in that state may require
   re-evaluation.
4. **`HG-6` rests on a construction-capability reading** settled by committed interpretation, not on
   possession of an admissible dataset.
5. **Stage G as a whole remains open** while `HG-8` is unresolved.

---

## 12. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **The previous Stage-G execution result is preserved and was not rewritten.** This artifact is
  additive.
- **No prior artifact was modified**, and no Git history was altered.
- **C-2A is unchanged** and was outside this reapplication.
- **No candidate was ranked, scored, or selected. No Primary Proxy was approved.**
- **`OJ-1` and `OJ-6` remain unexercised.**
- **No external source material, retrieval artifact, or checksum file is committed.**
- **Stage G remains OPEN. Stage H has not begun. Phase 2 remains BLOCKED.**
