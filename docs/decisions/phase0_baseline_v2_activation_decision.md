# Phase 0 — Baseline v2 Activation Owner Decision

**Status:** **APPROVED** — records the Owner activation of Baseline v2

**Scope:** Phase 0 — Baseline change control

**Decision date:** **2026-08-13** — the date of the explicit Owner activation

> **BASELINE v2 EFFECTIVE DATE: 2026-08-13**

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-0 Owner Decision — Baseline activation** |
| Decision status | **APPROVED** |
| Subject | The explicit Owner activation required by `OD-REQ-1`, fixing the Baseline-v2 effective date |
| Owner dispositions | `BA-OD-01` … `BA-OD-08` |
| **Baseline v2 effective date** | **2026-08-13** |
| Baseline v2 status after activation | **EFFECTIVE — the CONTROLLING Baseline for new work** |
| Baseline v1 status after activation | **PRESERVED and IMMUTABLE — historical predecessor** |
| Activated artifact | [`../experiment_spec_v2.md`](../experiment_spec_v2.md) — blob `50da4d16…`, preserved at commit `0de33f108d665e112a9c3ecec3b65ca9de0b422e`, tag `phase0-baseline-v2` |
| Governing versioning decision | [`phase0_baseline_v2_versioning_decision.md`](phase0_baseline_v2_versioning_decision.md) — blob `d8b3ab3e…` — **unchanged** |
| Predecessor | [`../experiment_spec.md`](../experiment_spec.md) — Baseline v1, blob `3a18862b…`, tag `phase0-baseline-v1` — **unchanged** |
| `OD-REQ-1` | **RESOLVED by this decision** |
| `OD-REQ-4` | **OPEN** — Mode E **NOT AUTHORIZED** |
| Mode E / Mode P | **NOT AUTHORIZED** / **NOT AUTHORIZED** |
| Criteria freeze `1e8bc85` | **UNCHANGED**; `AC-7` **unchanged** |
| `SC-18` | **ENGAGED — unchanged**, with its recorded mitigations |
| `OD-REQ-2` | **Controlling** for Baseline-version resolution |
| Qualification state | **UNCHANGED** in every respect |
| Phase 2 | **BLOCKED — unchanged** |

### Artifact role

This is the **separate explicit Owner activation** that `BV2-OD-10` (versioning decision §7) requires
as the third and final activation condition. It is **additive**: it modifies no existing artifact.

---

## 2. Activation

`BA-OD-01`. **Baseline v2 is ACTIVATED.**

> **Effective date: 2026-08-13** — the date of this explicit Owner activation.

`BA-OD-02`. **All three activation conditions of `BV2-OD-10` are now satisfied**, in order:

| # | Condition | Satisfied by |
| - | --------- | ------------ |
| **1** | Explicit Owner approval | Owner approval of the Baseline-v2 package, recorded at `phase0_baseline_v2_versioning_decision.md` decision date **2026-08-13** |
| **2** | Preservation — commit, push, annotated tag | Commit **`0de33f108d665e112a9c3ecec3b65ca9de0b422e`**, pushed to `main`, tag **`phase0-baseline-v2`** peeling to that commit, verified local and remote |
| **3** | **Explicit Owner statement of the effective date** | **This decision** |

---

## 3. Resulting Baseline state

`BA-OD-03`.

| Version | Status from 2026-08-13 |
| ------- | ---------------------- |
| **Baseline v2** | **EFFECTIVE. The CONTROLLING Baseline for new work.** |
| **Baseline v1** | **PRESERVED and IMMUTABLE.** The historical predecessor. It remains controlling for all work governed by it |

`BA-OD-04`. **Historical artifacts remain governed by the Baseline version applicable to them.**

> **No historical artifact is reinterpreted retrospectively.** Any artifact that does not declare a
> governing Baseline version was created under **v1** and is read under **v1**.

`BA-OD-05`. **`OD-REQ-2` remains controlling** for Baseline-version resolution, with its four
constraints intact: explicit v1 references remain bound to v1; historical artifacts are never
retrospectively reinterpreted; no qualification criterion changes because the governing version
changes; and no frozen criterion is amended by the rule.

---

## 4. What activation does NOT do

`BA-OD-06`. **This activation authorizes no work.**

> **Mode E remains NOT AUTHORIZED. `OD-REQ-4` remains OPEN.**
>
> **Mode P remains NOT AUTHORIZED** and remains a framework placeholder only.

Not authorized, and not performed: simulator code; methodology code; data loaders; synthetic dataset
creation; any Simulation Trial execution in either mode; Phase 2; any change to qualification state;
any modification of the criteria freeze; any modification of Baseline v1; any retrospective
reinterpretation of historical artifacts.

**Activating the Baseline that makes a Simulation Trial possible is not authorizing a Simulation
Trial.** Under v2 §18.3 and §18.4.1, each mode requires its own separate Owner Decision and execution
plan.

---

## 5. Unchanged governance

`BA-OD-07`.

- **Criteria freeze `1e8bc85` — UNCHANGED.** No criterion added, removed, weakened, widened,
  renumbered, or re-weighted.
- **`AC-7` — UNCHANGED.** Its operative rule — `P1-2` approved before any Phase-2 code exists —
  remains fully binding, and **Phase 2 remains BLOCKED**.
- **`SC-18` — ENGAGED, unchanged**, with its recorded mitigations: explicit Owner action; explicit
  successor version; a narrow, mechanically verified change surface; a preserved predecessor; no
  retrospective application; formal / non-formal separation; and anti-contamination rules.
  **Mitigation is not elimination**, and that statement stands.
- **Baseline v1 — unchanged, unamended, immutable.**
- **The Baseline-v2 preserved text and its versioning decision — unchanged.** This decision amends
  neither.

---

## 6. Qualification lane — unchanged

`BA-OD-08`. Activation changes **nothing** in the Qualification lane:

`O4-PARTIAL` ×3 · `GAP-A` ×3 · `GAP-B` ×2 · `HG-8` **NOT EVALUABLE** ×3 · `HG-6` / `HG-9` / `HG-12`
**PASS** ×3 with recorded limitations · `HG-11` **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY
RESTRICTED**, not PASS, non-eliminating, carried to `OJ-6` · `H-1` **NOT ESTABLISHED** · `P1-9`
**PARTIAL** · `P1-2` **OPEN** · `P1-5` **OPEN**, principle **P-A**, date **NOT YET DERIVED** · `P1-6`
**OPEN** · `K1` = **2026-08-13** · C-1 ×3 **QUALIFICATION INCOMPLETE** · C-2A **unchanged** · `OJ-1`
**NOT REACHED — DEFERRED** · `OJ-6` **unexercised** · **no Primary Proxy approved** · Stage G
**OPEN** · Stage H **NOT BEGUN** · **Phase 2 BLOCKED**.

The `M01` / `M02` follow-on drafts remain **untracked and unmodified**; `M03` remains **not designed,
not authorized, not executed**. Qualification research continues **independently**.

> **Note on `K1`.** The `O-4` Research Cutoff `K1` and the Baseline-v2 effective date share the value
> **2026-08-13**. **The coincidence carries no normative meaning.** They are unrelated instruments:
> `K1` bounds methodology research under the parent `O-4` authorization; the effective date activates
> a Baseline version. Neither derives from, constrains, or implies the other.

---

## 7. Two stale markers in preserved artifacts — disclosed, not repaired

Recorded openly, because this repository has never modified a tracked artifact after preservation —
**every tracked artifact has exactly one commit**, and that additive-only discipline is preserved here.

| Artifact | Stale text | Correct reading |
| -------- | ---------- | --------------- |
| `experiment_spec_v2.md` header | *"Effective date: NOT YET SET"* and *"NOT YET EFFECTIVE. NOT CONTROLLING."* | Superseded by this decision. **v2 is EFFECTIVE from 2026-08-13 and is the controlling Baseline for new work** |
| `phase0_baseline_v2_versioning_decision.md` §7 | *"an explicit Owner statement of the effective date, **recorded in this decision**"* | The Owner statement exists and is preserved — **in this activation artifact**, not inside the versioning decision |

**Neither is repaired**, because repairing either would modify a preserved artifact and break the
additive-only pattern. **This decision is the controlling record of the effective date**, and precedent
already exists for a preserved artifact carrying a status marker later superseded additively.

> **If the Owner prefers the markers corrected in place, that is a separate Owner decision** — it
> would be the first in-place modification of a preserved artifact in this repository, and should be
> taken deliberately rather than as a side effect.

---

## 8. Confirmations

- **Baseline v2 is EFFECTIVE from 2026-08-13** and is the controlling Baseline for new work.
- **Baseline v1 is preserved, immutable, and unchanged**, and remains controlling for work governed
  by it. **`3a18862b…` verified byte-identical to the `phase0-baseline-v1` blob.**
- **`phase0-baseline-v2` peels to `0de33f108d665e112a9c3ecec3b65ca9de0b422e`**, verified locally and
  on the live remote.
- **The preserved Baseline-v2 text and versioning decision are unchanged** — `50da4d16…` and
  `d8b3ab3e…`, both matching their blobs at the tag.
- **The criteria freeze is unchanged** (`4c8b3849…` = `1e8bc85`); **`AC-7` unchanged**; **`SC-18`
  ENGAGED with its mitigations**; **`OD-REQ-2` controlling**.
- **No historical artifact is reinterpreted retrospectively.**
- **`OD-REQ-1` is RESOLVED. `OD-REQ-4` remains OPEN. Mode E and Mode P remain NOT AUTHORIZED.**
- **No simulator code, methodology code, data loader, dataset, or simulation exists**, and none is
  authorized.
- **No qualification state changed.** **Phase 2 remains BLOCKED.**
- **No external access was performed** in reaching this decision.

---

**End of Phase-0 Owner Decision. `BA-OD-01` … `BA-OD-08`. **Baseline v2 ACTIVATED — effective
2026-08-13**, and is the controlling Baseline for new work. Baseline v1: **preserved, immutable,
historical predecessor**. Historical artifacts governed by their applicable version; **no
retrospective reinterpretation**. `OD-REQ-1`: **RESOLVED**. `OD-REQ-4`: **OPEN**. **Mode E: NOT
AUTHORIZED. Mode P: NOT AUTHORIZED.** Criteria freeze, `AC-7`: **unchanged**. `SC-18`: **ENGAGED**.
`OD-REQ-2`: **controlling**. Qualification lane: **unchanged**. Phase 2: **BLOCKED**.**
