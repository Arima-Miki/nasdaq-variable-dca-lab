# Phase 1 Primary Proxy Qualification — Stage-G Bounded Reapplication Owner Decision

**Status:** APPROVED — bounded reapplication preserved

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Preservation of the bounded Stage-G reapplication of `HG-6` and `HG-12` for the three C-1 candidates, and reconciliation of the resulting C-1 gate state |
| Decision status | **APPROVED** |
| Supporting evidence | [`../evidence/phase1_primary_proxy_stage_g_bounded_reapplication_evidence.md`](../evidence/phase1_primary_proxy_stage_g_bounded_reapplication_evidence.md) |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Controlling interpretations | [`…stage_g_authorization_decision.md`](phase1_primary_proxy_stage_g_authorization_decision.md); [`…hg6_capability_interpretation_decision.md`](phase1_primary_proxy_hg6_capability_interpretation_decision.md); [`…sc6_post_base_segment_interpretation_decision.md`](phase1_primary_proxy_sc6_post_base_segment_interpretation_decision.md); [`…hg9_revision_restatement_decision.md`](phase1_primary_proxy_hg9_revision_restatement_decision.md) — all **unchanged** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| Stage G as a whole | **REMAINS OPEN** — `HG-8` unresolved. **This is not a Stage-G closure artifact** |
| Candidate classification | **QUALIFICATION INCOMPLETE** for all three C-1 candidates |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage H | **NOT BEGUN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It preserves the result of a bounded, authorized reapplication
of two hard gates.

> **It is NOT a modification of the Phase-0 Baseline, NOT a modification of the frozen qualification
> criteria, and NOT a Stage-G closure.**

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged.

This decision contains **no Baseline result, no performance claim, and no historical value.**

---

## 2. Decision

### 2.1 The reapplication is preserved

**APPROVED**, for `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`:

| Gate | Previous | **Preserved result** |
| ---- | -------- | -------------------- |
| `HG-6` | NOT EVALUABLE | **PASS** |
| `HG-12` | NOT EVALUABLE | **PASS** |

Each rests on evidence and interpretations that were committed **before** the reapplication was
performed, and each carries the reasoning and conditions recorded in the supporting evidence
artifact.

### 2.2 Preservation is additive

> **The previous Stage-G execution result remains preserved as the result of the application
> performed under the semantics then in force.**

It is **not rewritten**, and no Git history is altered. This decision records a **new layer** applied
later, under interpretations that did not exist when the original application was made.

### 2.3 Resulting C-1 gate state

Identical for all three candidates, which are carried **distinctly** and are **not collapsed**:

| Gate | Result |
| ---- | ------ |
| `HG-1` | PASS |
| `HG-2` | PASS |
| `HG-3` | PASS |
| `HG-4` | PASS |
| `HG-5` | PASS |
| **`HG-6`** | **PASS** |
| `HG-7` | PASS |
| **`HG-8`** | **NOT EVALUABLE** |
| `HG-9` | PASS — by committed Owner Decision, with its recorded limitations |
| `HG-10` | PASS |
| **`HG-11`** | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED** |
| **`HG-12`** | **PASS** |
| `HG-13` | PASS |

### 2.4 Four distinctions preserved explicitly

1. **`HG-11` is NOT PASS.**
2. **`HG-11` is expressly non-eliminating** under F-11 and `G-OD-02`, and is carried to `OJ-6` as an
   attached Owner condition.
3. > **`HG-8` is the sole remaining qualification-blocking gate for the C-1 candidates.**
   >
   > It must **NOT** be described as the sole non-PASS gate — `HG-11` is also not PASS, while being
   > non-eliminating.
4. **`O-4` is the root cause of `HG-8` NOT EVALUABLE.**

### 2.5 Candidate classification

**QUALIFICATION INCOMPLETE** for `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`.

**No candidate is DISQUALIFIED. No candidate is yet a QUALIFIED SURVIVOR.**

---

## 3. Record of correction

Recorded once, for auditability, and **not propagated**: during Owner Review of the bounded
reapplication, three summary statements in the reapplication report were identified as inaccurate
and were corrected before preservation. They are **not** preserved as statements of state, and none
of them is repeated here as a current finding.

**The correct formulation, which governs:**

| Gate | State |
| ---- | ----- |
| `HG-8` | **NOT EVALUABLE**, and **qualification-blocking** |
| `HG-9` | **PASS**, under the committed Owner Decision |
| `HG-11` | **not PASS**, but **expressly non-eliminating** |

> **`HG-8` is the sole remaining qualification-blocking gate for the C-1 candidates.**

---

## 4. What this decision does NOT establish

- **Full historical-span admissibility** — not established.
- **`H-1`** — remains **NOT ESTABLISHED**.
- **Point-in-time equivalence** — not established.
- **`OJ-1`** — not exercised; remains NOT REACHED — DEFERRED.
- **`OJ-6`** — not exercised; Owner-reserved.
- **`P1-5`, `P1-6`** — not set; both remain OPEN.
- **`HG-8` satisfaction** — not established.
- **`O-4` resolution** — not achieved; remains OPEN.
- **`HG-11` PASS** — not established.
- **Candidate qualification, ranking, or Primary Proxy selection** — none.
- **Stage-G closure** — not effected. Stage G remains OPEN.

---

## 5. C-2A

**Outside this reapplication and unchanged in every respect:** `HG-6`, `HG-12`, `O-3`, the FX-leg
state, and its classification are all preserved as previously recorded. Nothing about C-2A was
re-evaluated.

---

## 6. Anti-circularity confirmation

- **No performance quantity was computed** at any point in the reapplication.
- **`ND-1 … ND-7` were not used.**
- **`AC-1`** — the controlling interpretations were committed **before** the reapplication, so
  semantics were not fitted to a result already seen.
- **`AC-4`** — the three candidates were carried symmetrically and distinctly.
- **`AC-8`** — no scoring, no weighting, no ranking; no comparison among candidates was performed.

---

## 7. Publication and external-material boundary

**No historical value is recorded in this repository.** Publisher wording is characterised, not
reproduced.

The ratified capability evidence remains **structurally outside** the repository and is unmodified.
Not committed: retrieval artifacts; the external provenance index; checksum files; endpoint captures;
access-policy captures; any token-bearing or redacted source page; and checksums of raw publisher
observations. Redistribution terms remain **UNCLEAR** on the Stage-F record; the fail-closed
publication policy applies and nothing is cleared for republication.

---

## 8. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **The previous Stage-G execution result was preserved, not rewritten.** No history was altered.
- **No prior artifact was modified** — including the Stage-G authorization artifact, the `HG-6` and
  `SC-6` interpretations, the `HG-9` decision, and all Stage-C/D/E/F artifacts.
- **`HG-6` = PASS and `HG-12` = PASS** for all three C-1 candidates; **`HG-9` = PASS** by its own
  committed decision.
- **`HG-8` remains NOT EVALUABLE; `O-4` remains OPEN.**
- **`HG-11` remains bounded and non-eliminating.**
- **`H-1` remains NOT ESTABLISHED.**
- **All three C-1 candidates remain QUALIFICATION INCOMPLETE.** No candidate is DISQUALIFIED; none
  is a QUALIFIED SURVIVOR.
- **C-2A is unchanged.**
- **No Primary Proxy is approved. P1-2 remains OPEN.** `OJ-1` and `OJ-6` remain unexercised.
- **Stage G remains OPEN. Stage H has not begun. Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Bounded Stage-G reapplication: PRESERVED, additive. `HG-6`: PASS
×3. `HG-12`: PASS ×3. `HG-9`: PASS ×3 by committed decision. `HG-8`: NOT EVALUABLE — the sole
remaining qualification-blocking gate, root cause `O-4`. `HG-11`: not PASS, non-eliminating,
carried to `OJ-6`. Candidates: QUALIFICATION INCOMPLETE. Stage G: OPEN. Primary Proxy: NOT APPROVED
— P1-2 remains OPEN. Phase 2: BLOCKED.**
