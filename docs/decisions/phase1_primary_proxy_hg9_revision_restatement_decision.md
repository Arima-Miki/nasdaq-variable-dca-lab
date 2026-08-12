# Phase 1 Primary Proxy Qualification — `HG-9` Revision / Restatement Behaviour Owner Decision

**Status:** APPROVED — `HG-9` resolved for the C-1 candidates

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Resolution of hard gate `HG-9` — revision / restatement behaviour — for the three C-1 candidates, and the interpretation of what the frozen criterion requires |
| Decision status | **APPROVED** |
| Adopted disposition | **H9-I1 — PASS**, with explicit limitations |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Controlling Frozen Baseline authority | [`../experiment_spec.md`](../experiment_spec.md) §6 (look-ahead prohibition), §14.6 / OD-12 (dataset cutoff) |
| Related Owner Decisions | Stage-G authorization semantics; [`…hg6_capability_interpretation_decision.md`](phase1_primary_proxy_hg6_capability_interpretation_decision.md); [`…sc6_post_base_segment_interpretation_decision.md`](phase1_primary_proxy_sc6_post_base_segment_interpretation_decision.md) — all **unchanged** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| `HG-9` result | **PASS** for `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` — carrying the limitations at §5 |
| Point-in-time equivalence | **NOT ESTABLISHED** |
| `P1-9` | **PARTIAL** — unchanged |
| `HG-8` | **NOT EVALUABLE**; `O-4` **OPEN** — unchanged |
| `HG-11` | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; non-eliminating — unchanged |
| Bounded `HG-6` / `HG-12` reapplication | **NOT PRESERVED by this decision** — separate pending action |
| Candidate classification | **QUALIFICATION INCOMPLETE** — unchanged |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It resolves a previously outstanding Owner review of one hard
gate, on the Frozen Baseline and already-authorized repository evidence only. **No new external
research was authorized or performed.**

> **It is NOT a modification of the Phase-0 Baseline, and NOT a modification of the frozen
> qualification criteria.**

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and
`1e8bc85` remains the criteria-freeze boundary.

This decision contains **no Baseline result, no performance claim, and no historical value.**

---

## 2. Owner finding

The Owner finds that `HG-9` requires **revision / restatement behaviour to be established well
enough to assess the look-ahead channel**, and does **NOT** require:

- a complete historical restatement-event log;
- enumeration of every historical revision;
- quantitative reconstruction of every revision magnitude;
- reconstruction of every observation exactly as visible on every historical date;
- a full point-in-time database.

> **The minimum required proposition is narrower: the project must understand the
> revision/restatement mechanism sufficiently to characterize the look-ahead channel rather than
> assume it negligible.**

For the three C-1 candidates, that proposition is **established**.

---

## 3. Decisions

### 3.1 `HG9-OD-01` — Frozen criterion interpretation

The controlling `HG-9` requirement is **revision / restatement behaviour established well enough to
assess look-ahead**. The controlling §6 requirement is that where a source is revised or restated
after the fact, its effect on look-ahead **must be assessed in Phase 1 rather than assumed
negligible**.

> **"Assess" is interpreted here as requiring sufficient characterization of the revision channel.
> It is NOT interpreted as silently requiring complete quantitative historical reconstruction.**

### 3.2 `HG9-OD-02` — Established documentary mechanism

For the C-1 Nasdaq candidates, primary documentary evidence establishes that:

- a recalculation / restatement mechanism **exists**;
- intraday values **are not** recalculated;
- EOD values **may be** recalculated or restated under documented conditions;
- a **stated materiality threshold** exists;
- **publisher discretion** exists;
- **named exception classes** exist.

This is sufficient to establish **how the mechanism operates** at the level `HG-9` requires.

### 3.3 `HG9-OD-03` — Missing event log

**No complete restatement-event log for the candidate span has been established.** That limitation
remains **explicit** and is not diminished by this decision.

However, the Frozen Baseline does **not** require a complete event log as a condition of `HG-9`
satisfaction.

> **Therefore the absence of such a log does not by itself make `HG-9` NOT EVALUABLE or FAIL.**

### 3.4 `HG9-OD-04` — Point-in-time reconstruction

> **Point-in-time equivalence is NOT established.**

The project cannot currently reconstruct every historical observation exactly as it appeared at
every simulated historical date. **This decision does NOT declare otherwise.** Full point-in-time
reconstruction is **not** treated as an unstated `HG-9` requirement.

### 3.5 `HG9-OD-05` — The look-ahead channel remains real

> **The Owner does NOT find revision risk negligible.**

The documented restatement mechanism establishes that **backward restatement is a real look-ahead
channel**. A dataset retrieved later may contain an as-restated value that differs from the value
visible at simulated time *t*.

`HG-9` PASS therefore means: **the revision behaviour is established well enough to assess the
channel.**

It does **NOT** mean the channel does not exist. It does **NOT** mean the channel is harmless. It
does **NOT** mean its magnitude or frequency is known.

### 3.6 `HG9-OD-06` — Materiality-threshold interpretation

> **The documented materiality threshold must NOT be misrepresented as an upper bound on
> restatement magnitude.**

It does **not** establish that revision effects are small. It is evidence about the publisher's
recalculation mechanism — **not** evidence that historical revision distortion is negligible.

### 3.7 `HG9-OD-07` — Dataset freeze and forward restatement

**OD-12 remains controlling.** Once the project freezes and pins a dataset, later publisher
restatements must not silently alter the frozen Baseline result. That addresses the
**forward-restatement reproducibility** channel.

> **It does not eliminate the separate backward-restatement issue** — that the retrieved dataset may
> already contain historical restatements.

### 3.8 `HG9-OD-08` — `CT-7` relationship

**`CT-7` remains a comparative criterion and is NOT converted into a hard-gate requirement.**

Its frozen evidence hierarchy — *documented non-revision > documented mechanism > unknown* — is
nevertheless **consistent** with the interpretation that a documented revision mechanism may satisfy
`HG-9` while remaining **comparatively inferior** to documented non-revision.

**The C-1 candidates remain in the documented-mechanism tier.**

### 3.9 `HG9-OD-09` — `P1-9` state

**`P1-9` remains PARTIAL.** `HG-9` PASS does **not** require `P1-9` to become COMPLETE.

The remaining uncertainty includes: whether historical restatements occurred in the candidate span;
their frequency; their magnitude; complete event-log availability; and point-in-time reconstruction.

> **Do not silently close `P1-9`.**

### 3.10 `HG9-OD-10` — Downstream treatment

The residual **backward-restatement risk must remain visible downstream**. A later Baseline or
backtest using an as-restated pinned dataset **must not silently represent that dataset as
point-in-time equivalent**.

Appropriate downstream treatment may include an explicit limitation, a sensitivity treatment, or
another Owner-approved control. **This decision does not design that control; it records the
obligation only.** Phase 2 is not begun.

### 3.11 `HG9-OD-11` — Candidate symmetry

The `HG-9` finding applies **identically** to `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`. They share the
same publisher-side recalculation / restatement policy and the same relevant evidence base.
**Return-version differences do not change this gate finding.**

### 3.12 `HG9-OD-12` — Result

| Candidate | `HG-9` |
| --------- | ------ |
| `NDXJPY` | **PASS** |
| `XNDXJPY` | **PASS** |
| `XNDXNNRJPY` | **PASS** |

**The PASS carries the explicit limitations and non-establishment statements recorded above.**

### 3.13 `HG9-OD-13` — What this decision does not establish

This decision does **NOT** establish: point-in-time equivalence; absence of historical restatements;
historical restatement frequency; historical restatement magnitude; harmlessness of revision risk;
complete revision metadata; complete event-log availability; `P1-9` completion; `HG-8` satisfaction;
`O-4` resolution; `HG-11` PASS; candidate qualification; or Primary Proxy selection.

### 3.14 `HG9-OD-14` — No Frozen Baseline amendment

This decision **interprets and applies** the existing `HG-9` criterion. It does not add, remove, or
weaken a hard gate; change a comparative criterion; change a stop condition; amend OD-01 … OD-14;
modify the Frozen Baseline; or modify the criteria freeze.

**Coexistence check performed, and no conflict found.** Recording this decision required no change
to any normative frozen text, so **`SC-18` is not triggered** and no conflict is returned to the
Owner.

---

## 4. Documentary basis

The finding rests on **primary, dated, publisher-issued** evidence already recorded at Stage C — the
Nasdaq recalculation policy, read directly — together with the Stage-D record that **no restatement
event log for the candidate span was located**, and the later recorded absence of revision metadata
on the publicly accessible route.

**No new external research was authorized or performed for this decision.**

---

## 5. Limitations carried with the PASS

These travel with the result and must not be dropped when it is cited:

1. **No restatement event log** for the candidate span has been located.
2. **No revision or version metadata** is exposed on the publicly accessible route.
3. **Point-in-time equivalence is NOT established.**
4. **The materiality threshold is not an upper bound** on restatement magnitude.
5. **Frequency and magnitude of any historical restatement are unknown.**
6. **The backward-restatement look-ahead channel is real and unquantified**, and carries the
   downstream obligation at `HG9-OD-10`.

---

## 6. Resulting governance state

| Item | State |
| ---- | ----- |
| `HG-9`, C-1 ×3 | **PASS**, with the §5 limitations |
| `HG-8`, C-1 ×3 | **NOT EVALUABLE**; `O-4` **OPEN** |
| `HG-11`, C-1 ×3 | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; non-eliminating; carried to `OJ-6` |
| Bounded `HG-6` / `HG-12` reapplication | Accepted in principle; **NOT preserved** by this decision — a separate pending preservation action |
| C-1 candidate classification | **QUALIFICATION INCOMPLETE**, because `HG-8` remains NOT EVALUABLE |
| C-2A | Untouched; `HG-9` remains NOT EVALUABLE |
| `P1-9` | **PARTIAL** |
| Primary Proxy | **NOT APPROVED**; **P1-2 OPEN**; `OJ-6` Owner-reserved |
| Phase 2 | **BLOCKED**; Stage H not begun |

---

## 7. Anti-circularity

- **`AC-1`** — the criteria remain frozen at `1e8bc85`. This decision interprets and applies an
  existing gate; it does not change what any criterion requires.
- **`AC-2`** — **no performance quantity was computed.** No observation value informed this
  decision, and none appears in it.
- **`AC-3`** — `ND-1 … ND-7` were not used.
- **`AC-4`** — applied identically to all three C-1 series.
- **`AC-6`** — point-in-time discipline **preserved rather than relaxed**: `HG9-OD-04` and
  `HG9-OD-05` keep the hazard explicit, and `HG9-OD-10` carries it downstream.
- **`AC-8`** — no scoring or weighting introduced; `CT-7` remains comparative.
- **`SC-18`** — considered and **not triggered**.

---

## 8. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched; §6, §7 and §14.6 are
  unaltered.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **No event log is claimed to exist.**
- **Point-in-time equivalence is NOT claimed.**
- **Revision risk is NOT declared negligible.**
- **The materiality threshold is NOT represented as an upper bound.**
- **`P1-9` remains PARTIAL.**
- **`HG-8` remains NOT EVALUABLE and `O-4` remains OPEN.**
- **`HG-11` remains bounded and non-eliminating.**
- **All C-1 candidates remain QUALIFICATION INCOMPLETE.**
- **The bounded `HG-6` / `HG-12` reapplication result was NOT preserved by this decision.**
- **No prior artifact was modified, and no history was rewritten.**
- **No Primary Proxy is approved. P1-2 remains OPEN.** `OJ-6` remains Owner-reserved.
- **No external access was performed in reaching this decision.**
- **Stage H has not begun. Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. `HG-9`: PASS for `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY`, carrying
explicit limitations. Point-in-time equivalence: NOT ESTABLISHED. Revision risk: NOT declared
negligible. `P1-9`: PARTIAL. `HG-8`: NOT EVALUABLE — `O-4` OPEN. `HG-11`: bounded, non-eliminating.
Candidates: QUALIFICATION INCOMPLETE. Primary Proxy: NOT APPROVED — P1-2 remains OPEN. Phase 2:
BLOCKED.**
