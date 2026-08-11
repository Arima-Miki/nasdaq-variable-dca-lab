# Phase 1 Primary Proxy Qualification — Stage D Closure Owner Decision

**Status:** APPROVED

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-11

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Closure of Stage D; classification of the C-1 pre-base-date segments; `OJ-1` disposition; adoption of the OD-12 evidentiary standard; access-limitation and provenance findings |
| Decision status | **APPROVED** |
| Supporting evidence | [`../evidence/phase1_primary_proxy_stage_d_history_continuity_evidence.md`](../evidence/phase1_primary_proxy_stage_d_history_continuity_evidence.md) |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Prior stage closure | [`phase1_primary_proxy_stage_c_closure_decision.md`](phase1_primary_proxy_stage_c_closure_decision.md) |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion amended, added, renumbered, or re-weighted** |
| OD-12 | **UNCHANGED.** This decision adopts an *evidentiary standard for the study*; it does not alter OD-12 |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage E | **NOT AUTHORIZED** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It closes one stage of an authorized Phase-1 study and records
the determinations arising from its evidence.

> **It is NOT a modification of the Phase-0 Baseline.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and it does not
  create, amend, or supersede any of them — **including OD-12**.
- The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this
  decision and that specification could be read as differing, **the specification governs Baseline
  behavior**.
- It does **not** amend the frozen qualification criteria. `HG-1 … HG-13`, `CT-1 … CT-9`,
  `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and `1e8bc85` remains the
  criteria-freeze boundary.
- This decision contains **no Baseline results, no performance claims, and no historical values.**

---

## 2. Decisions

### 2.1 D-6 — Classification of the C-1 pre-base-date segments

**APPROVED.**

> The pre-base-date segments of **`NDXJPY`**, **`XNDXJPY`** and **`XNDXNNRJPY`** are classified
> **NON-LIVE, UNCHARACTERIZED** under frozen study design §6.4.
>
> **`SC-6` is therefore TRIGGERED for those segments.**

**Reason.** The primary Nasdaq evidence establishes that historical files exist and that Nasdaq may
provide *either* actual historical values *or* back-tested histories. The publisher evidence obtained
does **not** establish which status applies specifically to the pre-base-date segment of these three
candidate series. A generic catalogue-level disclaimer is insufficient to characterize a specific
segment.

**Binding inference prohibitions.** The published Base Value Date is **not** to be treated as proof
of launch date, of live status, or of back-tested status. Status must **not** be inferred from:
availability; the file boundary; the Base Value Date; or structural consistency with the prior
repository statement.

**Consequence.** These segments may **not** currently be used for measured performance, for
Reference-High warm-up, or for candidate qualification requiring admissible history.

**Characterization limits.** This is a **segment-level exclusion on evidentiary grounds**. It is
**not** a declaration that the publisher's historical values are wrong or methodologically invalid,
and it is not a judgment about Nasdaq as a source.

**Revisability.** If future authoritative primary evidence specifically characterizes these
segments, this classification may be revisited through an **explicit Owner Review**, without
rewriting the historical Stage-D finding.

### 2.2 D-7 — `OJ-1` disposition

**`OJ-1` is NOT REACHED** for the C-1 pre-base-date segments at this time.

> **`OJ-1` — DEFERRED: no qualified NON-LIVE CHARACTERIZED segment is presently available for Owner
> admissibility judgment.**

`SC-6` excludes the affected segments **before** `OJ-1` is reached. Accordingly no choice is made
among measured-performance admissibility, warm-up-only admissibility, or neither.

If later primary evidence changes a segment from NON-LIVE, UNCHARACTERIZED to NON-LIVE,
CHARACTERIZED, that segment **returns to the Owner for `OJ-1`**. **No admissibility decision is
silently inherited.**

### 2.3 D-8 — C-1 live-history access limitation

**APPROVED.** The current limitation is **not** classified as `SC-5`.

Recorded:

- **`H-1` = NOT ESTABLISHED** for all three C-1 series;
- **LIVE DATE SPINE = ACCESS-LIMITED.**

**Reason.** The publisher and its publisher-controlled delivery channels are identifiable. The
unresolved issue is **access** to an entitlement-gated live-history spine, **not absence of
identifiable provenance**.

> **`SC-5` is NOT TRIGGERED on the present evidence.**

The live-start date must **not** be inferred from the Base Value Date, and "presumed live" must
**not** be upgraded to established LIVE.

### 2.4 D-9 — Entitlement and registration work

**NOT AUTHORIZED at this time.**

No account creation, no provision of personal information, no data purchase, no commercial
entitlement request, no subscription to any entitlement-gated delivery channel, and no use of
credentials not already explicitly authorized for this study.

The current access limitation is **accepted as a Stage-D research result**.

If a later gate cannot be evaluated without entitlement-gated evidence, the matter returns to the
Owner with: the exact evidence required; why it is necessary; the available access route; expected
cost if known; licensing and redistribution implications; and whether a non-commercial authoritative
alternative exists.

### 2.5 D-10 — The OD-12 evidentiary standard

**APPROVED and ADOPTED** as the Owner-approved evidentiary standard for the remainder of this
Primary Proxy qualification study — the study-level interpretation required by frozen study design
§6.6.

> A segment counts as **"defensible continuous history"** under OD-12 only if **all** of the
> following hold:
>
> 1. its **status is established from primary publisher evidence**;
> 2. its **boundaries are dated** rather than inferred;
> 3. its **methodology chain is reconstructable** and changes are dated;
> 4. its **observation spine is obtainable and pinnable**;
> 5. prohibited hindsight / [§6](../experiment_spec.md#6-look-ahead-prohibition) leak classes are
>    **affirmatively excluded** where relevant, rather than assumed absent;
> 6. its **gap structure is explicable** against the applicable publication rule;
> 7. **revision / restatement behaviour is sufficiently established** to evaluate look-ahead risk.

**This approval establishes the standard. It does NOT declare that any candidate or any segment
currently satisfies it.**

**OD-12 itself is unchanged.** This is an evidentiary interpretation governing the study, not an
amendment to the Frozen Baseline.

### 2.6 D-11 — N-3 provenance gap

**ACCEPTED AS OPEN.**

The 2026-05-01 effective date is supported by primary fund-issuer evidence. The Nasdaq
publisher-side proposal document is retained. **Nasdaq's final publisher-side decision document was
not located.**

> **No closure is manufactured.** The gap is carried into later gate evaluation. No further N-3
> research was authorized in the closure task.

### 2.7 D-12 — Stage-D external storage

**APPROVED.** The Stage-D persistent external research-material location is approved, with its
existing contents and its provenance and checksum structure accepted.

It remains **outside the Git repository**. This approval is **Stage-D-specific** and does **not**
establish a universal repository-wide storage architecture.

---

## 3. Stage-D closure determination

**Stage D is accepted as COMPLETE under the evidence actually obtainable within the authorized
boundary.**

| Item | State |
| ---- | ----- |
| C-1 pre-base-date segments | **NON-LIVE, UNCHARACTERIZED** — `SC-6` triggered — **not usable** |
| C-1 live segment | `H-1` **NOT ESTABLISHED**; date spine **ACCESS-LIMITED**; `SC-5` **not** triggered |
| C-2A | Route-level continuity **incomplete**; `O-3` **OPEN**; FX leg **UNRESOLVED-BY-DESIGN** — and **no qualification failure is inferred** from those intentionally unresolved items |
| N-2 | Documented continuity input; Stage-E expense and return-composition implications **remain open** |
| N-3 | Dated change established from primary fund evidence; Nasdaq final publisher confirmation **remains an open provenance gap** |
| `HG-8` | **No candidate passes or fails at Stage D.** Final gate evaluation remains Stage G |
| Primary Proxy | **NOT APPROVED** |

---

## 4. What this decision does NOT approve

- It does **not** approve a Primary Proxy — P1-2 remains **OPEN**.
- It does **not** pass or fail any hard gate for any candidate.
- It does **not** decide admissibility of any history — `OJ-1` was **not reached**.
- It does **not** declare any candidate or segment to satisfy the adopted OD-12 standard.
- It does **not** choose a Baseline start date or a Baseline Dataset Cutoff — P1-5 and P1-6 remain
  **OPEN**.
- It does **not** select an FX source or convention, and does **not** authorize any C-2 synthetic JPY
  construction.
- It does **not** resolve `O-3`, `O-4`, `O-5`, `O-6`, or `O-7`.
- It does **not** amend OD-12, any Owner Decision, or any frozen criterion.
- It does **not** authorize Stage E, F, or G.
- It does **not** unblock Phase 2.

---

## 5. Anti-circularity confirmation

- **No performance quantity was computed** at any point in Stage D. All arithmetic was on dates.
- **`ND-1 … ND-7` were not used** in reaching any part of this decision.
- The `SC-6` determination rests on **absence of segment-specific publisher characterization** —
  a documentary ground. It was not informed by any candidate's historical behaviour, and no
  comparison between candidates was made.
- `AC-1 … AC-8` were maintained; the three C-1 series were carried identically throughout.
- Incidental value return did not trigger `SC-16`: retrieval is not analysis, and no determination
  required analysing values.

---

## 6. Publication and external-material boundary

**No historical value — from the spine or incidental — is recorded in this repository.** No
publisher data file, date-spine file, provenance index, or checksum file enters Git. All source
material is retained **structurally outside** the repository; an ignored repository directory is not
an acceptable substitute.

Redistribution terms remain **unassessed** for every source used at Stages C and D. Licensing is
Stage-F work, so fail-closed treatment applies and nothing is cleared for republication.

---

## 7. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched, **including OD-12**.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **No prior evidence artifact was rewritten.** Stage-C findings stand; this closure is additive.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked or selected. No gate was evaluated.**
- **`OJ-1` remains NOT REACHED — DEFERRED.**
- **No raw dataset, publisher document, or external provenance material is committed to this
  repository.**
- **Stage E has not begun and is NOT AUTHORIZED.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Stage D: CLOSED. C-1 pre-base-date segments: NON-LIVE,
UNCHARACTERIZED — `SC-6` triggered. `OJ-1`: NOT REACHED — DEFERRED. OD-12 evidentiary standard:
ADOPTED, not satisfied. Primary Proxy: NOT APPROVED — P1-2 remains OPEN. Phase 2: BLOCKED.**
