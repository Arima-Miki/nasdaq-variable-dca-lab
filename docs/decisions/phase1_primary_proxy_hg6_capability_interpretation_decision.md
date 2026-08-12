# Phase 1 Primary Proxy Qualification — `HG-6` Capability Interpretation Owner Decision

**Status:** APPROVED — narrow interpretation recorded

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Narrow semantic interpretation of hard gate `HG-6` — its capability nature, its relationship to warm-up data and to `SC-6`, and its separation from `HG-9` and `HG-12` |
| Decision status | **APPROVED** |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Stage-G authorization semantics | [`phase1_primary_proxy_stage_g_authorization_decision.md`](phase1_primary_proxy_stage_g_authorization_decision.md) — **unchanged by this decision** |
| Controlling Frozen Baseline authority | [`../experiment_spec.md`](../experiment_spec.md) §6 (look-ahead prohibition), §7 (Drawdown Reference High), §14.6 (Baseline period and dataset cutoff) |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| Stage-G execution result | **NOT MODIFIED.** `HG-6` remains recorded NOT EVALUABLE in the existing Stage-G result |
| Stage-G reapplication | **NOT AUTHORIZED** by this decision |
| `HG-9` | **UNRESOLVED — pending separate Owner review** |
| `HG-12` | **NOT EVALUABLE** for the C-1 candidates — unchanged |
| `O-4`, `P1-5`, `P1-6` | **OPEN** — unchanged |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision** interpreting an existing frozen hard gate. It is a semantic
clarification, not evidence, not a gate result, and not a stage result.

> **It is NOT a modification of the Phase-0 Baseline, and NOT a modification of the frozen
> qualification criteria.**

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and
`1e8bc85` remains the criteria-freeze boundary.

This decision contains **no evidence, no gate result, no candidate classification, no Baseline
result, no performance claim, and no historical value.**

---

## 2. Decision scope

**In scope:** the meaning of the frozen `HG-6` requirement — specifically whether it is a capability
finding about the §7 Reference-High construction or a requirement that the project already hold an
admissible historical observation dataset; and how it relates to warm-up data, to `SC-6`, to `HG-9`,
and to `HG-12`.

**Out of scope, and expressly untouched:** the Stage-G matrix; any candidate classification;
re-running Stage G; `HG-9`; `HG-12`; external retrieval; observation retrieval; account creation;
entitlement access; third-party data-provider research; Owner-supplied-data ingestion; `O-4`
research; `P1-5`; `P1-6`; `OJ-6`; Stage H; Phase 2.

---

## 3. Controlling Frozen Baseline authority

`HG-6` is stated in the frozen criteria as: **Reference High constructible without look-ahead, from
observations available at each simulated date**, resting on Frozen Baseline §6 and §7.

The §7 construction it points to defines the Reference High as the highest daily closing value
observable up to and including the current decision date, computed as the maximum of daily closes
available through *t*. §7 further requires that the Reference High and the current market value use
the same price series and the same observation basis; that intraday highs not be used; that future
observations not be used; that the construction be free of look-ahead bias; and that the Reference
High never decrease within a run.

§7 additionally provides that historical observations preceding the measured performance start
**MAY** be used to initialize the Reference High, as warm-up data excluded from measured
performance.

---

## 4. Why this interpretation became necessary

Stage G recorded `HG-6` = **NOT EVALUABLE** for all three C-1 candidates. The recorded reason was
that the only available observations fall in the pre-base-date segment, which `SC-6` excludes, so
the Reference-High and warm-up construct was not established from admissible evidence.

Subsequent analysis identified that this result rests on an unresolved semantic question, and that
the question matters well beyond `HG-6`:

1. **`HG-6` and `HG-12` had been returning the same result for different reasons.** Their identical
   NOT EVALUABLE status masked two different requirements — one about a construction, one about
   project-side access — which meant any observation-access decision was being sized against an
   unclear target.
2. **Warm-up is permissive under §7, not mandatory.** Whether the absence of admissible warm-up data
   defeats `HG-6` therefore turns on how the gate is read.
3. **`HG-6` shares grammatical form with the other capability gates** — `HG-7`'s "applicable
   deterministically" and `HG-12`'s self-description as "a capability finding only".

The interpretation is recorded now, in advance of any reapplication, so that the semantics are fixed
before evidence is re-examined rather than after — consistent with `AC-1`.

---

## 5. Decisions

### 5.1 `HG6-OD-01` — Capability nature of `HG-6`

`HG-6` is a **capability finding** concerning whether the Frozen Baseline §7 Reference-High
construction can be applied without look-ahead.

> **`HG-6` does NOT require the project to already possess an admissible historical observation
> dataset.**

The gate asks whether the Reference High is **constructible** without look-ahead — not whether the
final Baseline dataset has already been acquired.

### 5.2 `HG6-OD-02` — Reference High construction

The controlling Frozen Baseline construction remains: the Reference High at *t* is the maximum of
the same candidate's daily closes available through *t*.

**This interpretation does not modify that construction.**

Because the construction uses only observations available through *t*, the running-maximum operation
itself does not require future observations.

> **This interpretation does not authorize use of any observation that would otherwise violate §6.**

### 5.3 `HG6-OD-03` — Warm-up data

Frozen Baseline §7 provides that historical observations preceding the measured performance start
**MAY** be used to initialize the Reference High. **Pre-start warm-up history is therefore
permissive, not mandatory.**

> **Absence of admissible pre-start warm-up history does NOT by itself cause `HG-6` to be NOT
> EVALUABLE or FAIL.**

Where no admissible warm-up history is used, the Reference High may initialize from observations
within the measured period, according to the frozen construction.

> **This decision does NOT admit the `SC-6`-excluded pre-base-date segment. `SC-6` remains fully
> effective.**

### 5.4 `HG6-OD-04` — `SC-6` relationship

`SC-6` remains a **segment-level evidentiary exclusion**. It continues to exclude the affected
pre-base-date observations from measured performance, from Reference-High warm-up, and from any
qualification use requiring admissible history.

However, exclusion of **optional** warm-up observations does not by itself make the §7 Reference-High
construction incapable of operating without look-ahead.

> **Therefore: `SC-6` alone is not a basis for `HG-6` = NOT EVALUABLE or `HG-6` = FAIL.**

**Owner Decision D-6 is preserved unchanged.**

### 5.5 `HG6-OD-05` — Point-in-time / revision boundary

This interpretation does **not** resolve the separate question of whether a currently retrievable
historical observation is identical to the observation that was available at simulated date *t*.

The Frozen Baseline identifies retroactively revised series as a potential look-ahead hazard. **That
issue is not duplicated inside the structural Reference-High construction test.** It remains subject
to the appropriate revision / point-in-time gate, including `HG-9` and the pending `HG-9` Owner
review.

> **This decision must NOT be read as: declaring revision history harmless; declaring `HG-9` PASS;
> authorizing use of as-restated observations; or declaring point-in-time equivalence established.**

**`HG-9` remains unresolved for Owner review.**

### 5.6 `HG6-OD-06` — `HG-12` separation

`HG-6` and `HG-12` are **distinct gates with distinct evidentiary requirements**:

| Gate | Concerns |
| ---- | -------- |
| **`HG-6`** | Construction capability and look-ahead semantics |
| **`HG-12`** | Project-side access, reproducible retrieval, pinning, and cutoff capability |

**Nothing in this decision changes `G-OD-10`.** `HG-12` remains **NOT EVALUABLE** for the C-1
candidates under the current authorized evidence and access state.

> **A structural `HG-6` finding must NOT be used to infer `HG-12` satisfaction.**

### 5.7 `HG6-OD-07` — C-1 applicability

For `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`, the existing committed evidence **may be re-evaluated
under this interpretation at a later, explicitly authorized Stage-G reapplication**.

> **This decision itself does NOT change `HG-6` = NOT EVALUABLE in the existing Stage-G execution
> result.**

It supplies the controlling interpretation for the **next authorized application**. The previous
finding is **not** silently rewritten, and remains valid as the result of the application actually
performed under the semantics then in force.

### 5.8 `HG6-OD-08` — No criterion change

This Owner Decision is an **interpretation of the existing frozen `HG-6` requirement**. It does
**not**: add a hard gate; remove a hard gate; weaken a hard gate; alter §6; alter §7; alter the
Reference-High formula; alter any stop condition; alter any comparative criterion; amend OD-01
through OD-14; or amend the Frozen Baseline.

**No such change was required in order to record this interpretation.**

---

## 6. Dependency finding preserved

Recorded without resolving the later steps:

```
HG-6 Owner interpretation  →  later Stage-G reapplication of HG-6
```

- **`HG-12` still requires an observation-access resolution path.** It is not advanced by this
  decision.
- **`P1-5` and `P1-6` are NOT prerequisites** to resolving `HG-6` or `HG-12` capability. `HG-12`'s
  own frozen text records that it is a capability finding only and does not set `P1-6`.
- **`P1-5` and `P1-6` remain relevant** before final dataset retrieval, and **materially scope**
  later `O-4` continuity research.
- **`O-4` remains OPEN**, and no `O-4` research is authorized or performed.

---

## 7. Anti-circularity

- **`AC-1` — criteria frozen before evidence.** This interpretation clarifies the meaning of an
  existing gate; it does not change what the gate requires, and it is recorded **before** any
  reapplication so that semantics are not fitted to a result already seen.
- **`AC-2` — zero performance computation.** No performance quantity was computed. No observation
  was retrieved, examined, or used.
- **`AC-3` — `ND-1 … ND-7` quarantine.** No `ND-n` material informed this interpretation.
- **`AC-4` — symmetric candidate handling.** The interpretation applies identically to all three
  C-1 series, and to any candidate to which `HG-6` is applied.
- **`AC-6` — point-in-time discipline.** Expressly preserved rather than relaxed: `HG6-OD-05`
  keeps the revision hazard live and assigns it to `HG-9`.
- **`AC-8` — no scoring, no weights.** None introduced.
- **`SC-18` was considered and not triggered:** recording this interpretation required no frozen
  criterion to change.

---

## 8. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched. §6, §7 and the
  Reference-High formula are unaltered.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **`SC-6` is unchanged and fully effective. D-6 is preserved unchanged.**
- **`G-OD-10` is unchanged. `HG-12` remains NOT EVALUABLE** for the C-1 candidates.
- **`HG-9` remains unresolved**, pending separate Owner review.
- **The existing Stage-G execution result is not modified**, and no candidate classification is
  changed. All four candidates remain **QUALIFICATION INCOMPLETE**.
- **Stage-G reapplication is NOT authorized** by this decision.
- **`O-4`, `P1-5` and `P1-6` remain OPEN.**
- **No Primary Proxy is approved. P1-2 remains OPEN.** `OJ-6` remains Owner-reserved.
- **No external access was performed, no observation retrieved, and no calculation made.**
- **Stage H has not begun. Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. `HG-6`: interpreted as a capability finding — pre-start warm-up
history is permissive, and `SC-6` alone is not a basis for NOT EVALUABLE or FAIL. `HG-9`:
unresolved. `HG-12`: NOT EVALUABLE, unchanged. Stage-G result: not modified. Stage-G reapplication:
NOT AUTHORIZED. Primary Proxy: NOT APPROVED — P1-2 remains OPEN. Phase 2: BLOCKED.**
