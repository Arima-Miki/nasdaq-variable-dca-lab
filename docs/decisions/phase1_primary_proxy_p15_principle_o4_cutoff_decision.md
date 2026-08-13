# Phase 1 Primary Proxy Qualification — `P1-5` Principle and `O-4` Research Cutoff Owner Decision

**Status:** APPROVED — `P1-5` principle selected; `O-4` Research Cutoff rule selected

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-13

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Selection of the `P1-5` start-date **principle**, and selection of the **`O-4` Research Cutoff rule**; the required interpretation of each; and the D-10 treatment |
| Decision status | **APPROVED** |
| Owner dispositions recorded | `OD-P15-07` … `OD-P15-12` |
| Adopted `P1-5` principle | **P-A — EARLIEST ADMISSIBLE OBSERVATION** |
| Adopted `O-4` Research Cutoff rule | **K1 — the date on which the bounded `O-4` research authorization is recorded** |
| `O-4` Research Cutoff **value** | **NOT YET FIXED** — see §8. **It is not this artifact's decision date** |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Controlling Frozen Baseline authority | [`../experiment_spec.md`](../experiment_spec.md) §6, §7, **§14.6 / OD-12**, §17 Invariant 17, §19.1 |
| Immediate controlling decision | [`…p15_p16_o4_sequencing_decision.md`](phase1_primary_proxy_p15_p16_o4_sequencing_decision.md) — `OD-P15-01 … 06`, Interpretation B, §7.3 conditions, §8 floor — **unchanged** |
| Related Owner Decisions | **D-6**, **D-8**, **D-9**, **D-10**; Stage-G authorization semantics; [`…hg6_capability_interpretation_decision.md`](phase1_primary_proxy_hg6_capability_interpretation_decision.md); [`…sc6_post_base_segment_interpretation_decision.md`](phase1_primary_proxy_sc6_post_base_segment_interpretation_decision.md); [`…hg9_revision_restatement_decision.md`](phase1_primary_proxy_hg9_revision_restatement_decision.md); [`…stage_g_bounded_reapplication_decision.md`](phase1_primary_proxy_stage_g_bounded_reapplication_decision.md) — **all unchanged** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| `P1-5` | **OPEN** — principle **now selected**; **date NOT YET DERIVED** |
| `P1-6` | **OPEN** — no Baseline Dataset Cutoff selected |
| `O-4` | **OPEN** — no research performed; **bounded `O-4` research NOT YET AUTHORIZED** |
| `HG-8` | **NOT EVALUABLE** ×3 — not reapplied |
| `OJ-1` | **NOT REACHED — DEFERRED**; not exercised |
| `D-10` | **Unchanged.** Not converted into a hard gate; unresolved conditions remain visible |
| Candidate classification | **QUALIFICATION INCOMPLETE** ×3 — unchanged |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage G | **OPEN** — not a Stage-G artifact, not a Stage-G closure |
| Stage H | **NOT BEGUN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It exercises two decisions the Owner had expressly reserved: a
`P1-5` **principle** and an **`O-4` Research Cutoff rule**. It is not evidence, not a gate result,
and not a stage result. **No external research was authorized or performed.**

> **It is NOT a modification of the Phase-0 Baseline, and NOT a modification of the frozen
> qualification criteria.**

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and
`1e8bc85` remains the criteria-freeze boundary.

This decision contains **no Baseline result, no performance claim, no historical value, no derived
`P1-5` date, and no fixed cutoff value.**

---

## 2. Problem statement

`HG-8` is the sole remaining qualification-blocking **gate** for the three C-1 candidates, with root
cause `O-4` — no methodology version history or publisher change log has been located.

`HG-8` is span-relative. The committed sequencing decision established the two instruments that bound
that span for research purposes: **`OD-P15-06`** fixed the methodology-research **floor** at the
published Base Value Date while D-6 / `SC-6` control and `OJ-1` is unexercised, and **`OD-P15-05`**
permitted a separate **`O-4` Research Cutoff** as the **ceiling**, under five conditions and expressly
distinct from `P1-6`.

Two Owner acts remained outstanding: selection of a `P1-5` **principle** — reserved to the Owner by
frozen study design §14 and §10.2, and required by `AC-1` discipline to be recorded **before** `O-4`
runs — and selection of the cutoff **rule**. This decision records both.

**It does not authorize `O-4` research.** See §13.

---

## 3. Authority hierarchy

Applied in this order, highest first:

| Rank | Authority | Bearing here |
| ---- | --------- | ------------ |
| 1 | **Frozen Phase-0 Baseline** | §14.6 / OD-12 create `P1-5` and its substantive requirements; §6 and §7 bound look-ahead and the Reference High; Invariant 17 |
| 2 | **OD-01 … OD-14** | OD-12: longest defensible continuous history; start justified by data availability and methodology, **not** by performance inspection |
| 3 | **Frozen qualification criteria** — `1e8bc85` | `HG-8`; §6.4; §10.2; §14 Owner-only decisions; `AC-1`, `AC-4`, `AC-5`; `SC-17`, `SC-18`, `SC-19`; `OJ-1` |
| 4 | **`OD-P15-01 … 06`** | Rule/date split; `R-2` circularity; candidate-neutrality; **Interpretation B**; cutoff conditions; research floor |
| 5 | **Other committed Owner Decisions** | **D-6**, **D-8**, **D-9**, **D-10**; `G-OD-08`; `HG6-OD-03/04`; `SC6-OD-03/04/05/08`; `HG9-OD-07/09/10/13` |
| 6 | **Committed Phase-1 evidence** | Stage-D segment maps, `H-1 … H-8`, warm-up finding; Stage-G bounded reapplication |
| 7 | **This decision** | Principle and cutoff-rule selection only |

Where this decision could be read as differing from any higher rank, **the higher rank governs.**

---

## 4. Decisions

### 4.1 `OD-P15-07` — `P1-5` principle adopted

**ADOPTED: P-A — "EARLIEST ADMISSIBLE OBSERVATION".**

> **The Baseline start-date principle is the first observation of the earliest segment that is not
> excluded under D-6 / `SC-6`.**

This selects **the principle only.**

- **No `P1-5` date is derived or selected by this decision.**
- The eventual date must be derived **mechanically** from this principle against the
  **Phase-1-approved Primary Proxy** and the evidence applicable at that time.
- **`P1-5` remains OPEN.** Selection of the principle is **not** completion of `P1-5`.

**Basis.** Permitted by **Interpretation B** (`OD-P15-04`): a principle outside `R-1 … R-4` creates no
new criterion where it already satisfies OD-12 / §14.6. P-A satisfies all three limbs — it takes the
**longest** history available subject to admissibility, it is **justified by data availability and
methodology** (the admissibility rules committed at D-6 / `SC-6`), and it is **wholly independent of
strategy performance**, of which none exists.

### 4.2 `OD-P15-08` — Required interpretation of P-A

**P-A means "not excluded under D-6 / `SC-6`." Nothing more.**

> It **MUST NOT** be interpreted as establishing any of the following:
>
> 1. **`H-1` LIVE status**;
> 2. **full historical admissibility**;
> 3. **point-in-time equivalence**;
> 4. **satisfaction of D-10 in full**;
> 5. **full-span retrievability**;
> 6. **absence of revision / restatement risk**;
> 7. **`P1-6`**;
> 8. **`P1-2`**, or approval of a Primary Proxy.

`SC6-OD-05`'s mandatory distinction is preserved verbatim in force:

> **"not established as LIVE" does NOT mean "established as NON-LIVE."**
>
> **"`SC-6` exclusion not established" does NOT mean "full historical admissibility established."**

**The limitations already recorded under `H-1`, D-10, `HG-9`, `P1-9` and related committed artifacts
remain visible and controlling where applicable.** In particular: `H-1` remains **NOT ESTABLISHED**;
`HG9-OD-10`'s backward-restatement obligation remains live; `HG-12`'s PASS remains a capability
finding at minimal scale, with full-span retrievability unestablished and reserved to `P1-6`.

### 4.3 `OD-P15-09` — `AC-5` preservation

**The start date is derived from a rule, never chosen as a discretionary date.**

The derivation, when it occurs, must be **mechanical**: identify the earliest segment not excluded
under D-6 / `SC-6` for the approved Primary Proxy, then take its first observation. No discretion may
enter at the point of derivation.

> **`AC-5` is preserved and reinforced.** Its named failure mode — *choosing the start date after
> seeing strategy performance* — is structurally unavailable under P-A: the principle's inputs are
> segment classifications and an observation date, and **no performance quantity exists or may be
> computed** (§7.1 structural guarantee; `AC-2`).

If the derivation ever appears to require a judgment call, that is a signal to return to Owner
Review, not to exercise discretion.

### 4.4 `OD-P15-10` — `O-4` Research Cutoff rule adopted

**ADOPTED: K1 — "THE DATE ON WHICH THE BOUNDED `O-4` RESEARCH AUTHORIZATION IS RECORDED".**

The `O-4` methodology-research window therefore has:

| Bound | Value | Source |
| ----- | ----- | ------ |
| **Floor** | The already-established **Base Value Date** methodology-research scoping floor | `OD-P15-06` — unchanged, and narrow |
| **Ceiling** | The date on which the **bounded `O-4` research authorization** is recorded | **K1**, adopted here; **value not yet fixed** — §8 |

**This cutoff bounds `O-4` methodology research only.**

> **It is NOT `P1-6`. It is NOT the Baseline Dataset Cutoff. It MUST NOT be silently reused as
> `P1-6`.**

**The five `OD-P15-05` / §7.3 conditions are satisfied or provided for:**

| # | Condition | Status |
| - | --------- | ------ |
| 1 | Named distinctly from the Baseline Dataset Cutoff | ✅ **"`O-4` Research Cutoff"** — a distinct name used throughout |
| 2 | Expressly does not resolve or modify `P1-6` | ✅ Stated here and at §10 |
| 3 | Fixed and recorded **before `O-4` evidence is compiled** | ✅ **By construction** — K1's value is the authorization date, which necessarily precedes any evidence compiled under that authorization |
| 4 | Justified by **research reproducibility and bounded scope**, never candidate qualification outcome | ✅ §5.2 |
| 5 | Coincidence carries no normative meaning | ✅ Provided for at §8.3 |

### 4.5 `OD-P15-11` — D-10 treatment

**D-10 is NOT converted into a new hard gate and NOT into an additional Stage-G qualification
blocker.**

- D-10 remains the **previously adopted study-level evidentiary standard** — the §6.6 interpretation
  of OD-12's "defensible continuous history".
- **`HG-8` remains the sole remaining qualification-blocking gate** for the C-1 candidates. D-10 does
  not change that, and adds no gate.
- **This decision does NOT declare the post-base-date C-1 segment to satisfy D-10.** Stage D's
  position stands unchanged: the standard is established; **no candidate is claimed to satisfy it.**
- **D-10's unresolved conditions remain visible for later Owner review, including `OJ-6` / `P1-2`
  where applicable.** They are neither discharged, waived, nor downgraded by the adoption of P-A.

> **Recorded so it is not lost: P-A reads OD-12's "defensible" as "not excluded". D-10 sets a higher
> bar for the same phrase. The Owner has adopted P-A as the `P1-5` principle while leaving D-10
> intact and its residual conditions live.** These coexist because they operate at different points —
> P-A determines where measurement would begin; D-10 informs `OJ-6` / `P1-2` on whether the resulting
> history is defensible enough to approve.

### 4.6 `OD-P15-12` — Anti-circularity fixing

**P-A and K1 are fixed BEFORE any `O-4` research is performed.**

> **No `O-4` finding may be used to alter:**
>
> - the adopted **`P1-5` principle**;
> - the **`O-4` Research Cutoff** or its adopted rule;
> - the **research floor**;
> - **any frozen criterion**.

**No performance quantity was used in this decision, and none may be.** `ND-1 … ND-7` were not used.

If `O-4`'s findings appear to warrant changing any of the four items above, that is a matter for
explicit Owner Review under `SC-18` — **not** an adjustment to be made inside the research.

---

## 5. The adopted principle — statement and derivation semantics

### 5.1 Statement

> **P-A — EARLIEST ADMISSIBLE OBSERVATION.** The Baseline start-date principle is the first
> observation of the earliest segment that is not excluded under D-6 / `SC-6`.

### 5.2 Why this principle, on governance grounds

Recorded because `OD-P15-05` condition 4 and OD-12 both require the basis to be stated, and because
§11.5 of the sequencing decision requires the **actual** basis to be visible:

1. **Immunity to the span-shrinking hazard.** P-A's inputs are segment classifications committed at
   Stage D and one observation date. **It cannot move in response to how difficult `O-4` proves.**
   This is the direct answer to the hazard named at `…sequencing_decision.md` §11.5.
2. **Zero circularity.** It has **no dependence on `O-4`'s outcome** — unlike `R-2`, whose required
   input is `O-4`'s output (`OD-P15-02`).
3. **Reproducibility.** Derivable from committed artifacts plus a single observation date.
4. **It maximises length subject to admissibility**, which is the structure of OD-12's "longest
   defensible continuous history".

**No candidate qualification outcome informed this selection**, and no comparison among candidates
was performed.

### 5.3 Candidate-neutrality — `OD-P15-03` satisfied

P-A refers to **admissibility rules**, not to any candidate, family, return version, or date. Applied
to any candidate it yields that candidate's own admissible start.

> **It does not prejudge C-2A**, which remains an **UNCONSTRUCTED ROUTE**, QUALIFICATION INCOMPLETE,
> and **unchanged in every respect** by this decision.

**Neutral in form is not the same as neutral in effect**: on the current record several principles are
blocked for C-1 for reasons peculiar to C-1's evidence. That asymmetry arises from the evidence, not
from the principle. **`AC-4` is satisfied** — nothing narrows toward a favourite.

### 5.4 What still stands between P-A and a date

Recorded as a fact, without authorizing its resolution:

- **`P1-2`** must be approved — §14.6 binds the history to the *approved* Primary Proxy.
- **The first observation date of the earliest non-excluded segment is NOT ESTABLISHED** for any C-1
  series, because the post-base-date spine was never obtained (ACCESS-LIMITED at Stage D). The floor
  is presently established at **segment level, not observation level**.
- Establishing it is an **ordinary retrieval question** on the route whose capability `HG-12` now
  records as PASS — **not** entitlement-gated work under D-9. **No such retrieval is authorized by
  this decision.**

---

## 6. Required non-inferences

Restated as a checklist because these must survive every downstream citation of P-A:

| Proposition | Status |
| ----------- | ------ |
| `H-1` LIVE status | **NOT ESTABLISHED** — unchanged |
| Full historical admissibility | **NOT ESTABLISHED** |
| Point-in-time equivalence | **NOT ESTABLISHED** — `HG9-OD-13` |
| D-10 satisfied in full | **NOT DECLARED** — `OD-P15-11` |
| Full-span retrievability | **NOT ESTABLISHED** — a `P1-6` matter |
| Absence of revision / restatement risk | **NOT ESTABLISHED** — `HG9-OD-10` obligation live |
| `P1-6` | **OPEN** |
| `P1-2` / Primary Proxy approval | **NOT APPROVED — OPEN** |
| The post-base-date segment is LIVE | **NOT DECLARED** — `SC6-OD-04` |
| The pre-base-date segment is admissible | **NO** — D-6 / `SC-6` unchanged and controlling |

---

## 7. The `O-4` research window

### 7.1 Structure

```
floor  = published Base Value Date scoping floor        (OD-P15-06, unchanged, narrow)
ceiling = date the bounded O-4 research authorization is recorded   (K1, value not yet fixed)
```

The window bounds **methodology-chain research only**. Within it, the coverage standard recorded at
`…sequencing_decision.md` §7.2 applies unchanged and is **enumerative, not incidental**: a search
returning only already-known changes cannot distinguish *no change occurred* from *no change was
found*.

The proposition `HG-8` requires, recorded at §7.1 of that decision, is likewise unchanged, together
with `G-OD-08` (authoritative issuer evidence may establish a change and its date; the `N-3`
publisher-side gap alone does not fail `HG-8`).

### 7.2 The floor is not widened

**`OD-P15-06` is used exactly as recorded, in its narrow sense only.** The Base Value Date serves as a
methodology-research scoping floor **because** the pre-base-date segment is excluded from measured
performance, warm-up, and other qualification use under D-6 and §6.4.

> **It establishes no first live observation, no first actual observation, no launch date, no `H-1`,
> no admissibility, and no warm-up availability.** **D-8** and **`SC6-OD-03`** are unchanged, and the
> conflict checks recorded against them stand.

### 7.3 Residual coverage limitation, recorded not resolved

If the eventual `P1-6` falls **later** than the `O-4` Research Cutoff, methodology changes effective
between the two would lie inside the `HG-8` span but outside the researched window. This is inherent
to bounding research before the Baseline pin exists. **It is surfaced here so it is not discovered
later**, and would require a supplementary check at `P1-6` time. It is not resolved by this decision.

---

## 8. K1 date-assignment boundary — unambiguous

This section exists so that K1 cannot accidentally acquire the wrong value.

### 8.1 The rule is adopted; the value is not yet fixed

> **The `O-4` Research Cutoff value is the date on which the LATER BOUNDED `O-4` RESEARCH
> AUTHORIZATION is recorded.**
>
> **It is NOT the date on which this principle / cutoff decision artifact is drafted, reviewed,
> committed, or tagged.**

### 8.2 Explicitly

- **This artifact's decision date is NOT the `O-4` Research Cutoff.** No date appearing in this
  artifact is the cutoff value.
- **The cutoff value does not exist yet.** It comes into existence only when a bounded `O-4` research
  authorization is recorded.
- **The two authorizations are distinct**, unless **explicitly combined by a later Owner decision**.
  If a later Owner decision does combine them, that decision must say so expressly; **the combination
  must never be inferred** from proximity in time, from adjacent commits, or from a shared tag date.

### 8.3 Coincidence rule — condition 5

If the eventual cutoff value **coincides** with an existing study cutoff, with the date of this
artifact, or with the eventual `P1-6`:

> **The artifact recording it MUST state that the coincidence carries no normative meaning.**

This mirrors frozen study design §11's treatment of research cutoffs and `OD-P15-05` condition 5.

---

## 9. `P1-5` state after this decision

> **`P1-5` remains OPEN.**

| Component | State |
| --------- | ----- |
| **Principle / rule** | **SELECTED — P-A, "earliest admissible observation"** |
| **Derived date** | **NOT YET DERIVED**, and not derivable before `P1-2` |

**Selection of the principle must not be represented as completion of `P1-5`**, and `P1-5` must not
be shown as resolved, closed, or satisfied in any downstream artifact.

---

## 10. `P1-6` separation

- **`P1-6` remains OPEN.** No Baseline Dataset Cutoff is selected.
- **The `O-4` Research Cutoff is not `P1-6` and must not silently become it.** The prohibition applies
  equally to the FX Residual Decomposition Research Cutoff, the Empirical Alignment Study cutoff, any
  retrieval timestamp, and any publication date.
- `P1-6`'s function remains the **reproducibility pin** required by §14.6 / OD-12.
- **`HG-12` PASS does not set `P1-6`** — its own frozen text records it as a capability finding only.
- Under `HG9-OD-07`, `P1-6` addresses the **forward**-restatement channel and does **not** eliminate
  the **backward**-restatement channel; `HG9-OD-10`'s downstream obligation stands and is not
  designed here.

---

## 11. `OJ-1` preservation

> **`OJ-1` is NOT exercised. It remains NOT REACHED — DEFERRED.**

- P-A operates **on top of** the currently controlling D-6 / `SC-6` exclusion, used exactly as
  recorded. It does not un-exclude, weaken, or reopen anything.
- **This is not a permanent waiver.** If `OJ-1` is later exercised, the earliest non-excluded segment
  could change, and with it **both** the P-A derivation **and** the `O-4` research floor. Any such
  consequence **must be evaluated separately**, and would require re-scoping `O-4`.
- The three §6.5 admissibility questions — non-live history for measured performance, for
  Reference-High warm-up only, or for neither — remain open and undecided.
- `SC6-OD-08` is unchanged.

---

## 12. Anti-circularity and criteria-freeze analysis

### 12.1 What this decision is, and is not

| Category | Present? | Assessment |
| -------- | -------- | ---------- |
| Interpreting already-frozen semantics | Yes | `OD-P15-08`'s reading of P-A; legitimate |
| **Selecting a previously reserved Owner principle** | **Yes** | The core act. Reserved to the Owner by frozen study design §14 and §10.2, and left open since the criteria freeze. Legitimate |
| Creating a new criterion after evidence was observed | **No** | Permitted by **Interpretation B**; P-A satisfies OD-12 / §14.6 without altering any `HG` / `CT` / `ND` / `OJ` / `SC` / `AC` item. `R-1 … R-4` are not edited, withdrawn, or extended. `R-5` is not invented |
| Bounding research for reproducibility | Yes | K1 and the §7.1 window; legitimate |
| **Shrinking a qualification span because evidence is difficult to recover** | **No** | **P-A is the option structurally incapable of this** — see §12.2 |

### 12.2 Why this is not criterion engineering

1. **P-A cannot move in response to `O-4`.** Its inputs are segment classifications committed at
   Stage D and one observation date. Unlike `R-2`, it has **no dependence whatever on the methodology
   history that `O-4` is meant to recover**. The span it implies is the **widest** admissible under
   D-6 / `SC-6`, not the narrowest — it therefore **increases** the `HG-8` burden relative to `R-2`.
2. **The floor derives from a ruling that was adverse when made.** D-6 was decided on independent
   evidentiary grounds and destroyed *all* C-1 warm-up availability, making the §6.5 hazard concrete.
   A ruling that worsened the candidate's position cannot be recast as engineering in its favour.
3. **Both selections are fixed before the evidence is gathered** — `OD-P15-12`, in the same `AC-1`
   posture as the `HG-6`, `SC-6`, `HG-9` and sequencing interpretations.
4. **No performance quantity has ever been computed in this study**, so `SC-17`'s prohibition has
   nothing to bite on and no tuning surface exists.

### 12.3 Named-rule evaluation

| Rule | Assessment |
| ---- | ---------- |
| **`AC-1`** — criteria frozen before evidence | **Not violated.** `1e8bc85` intact; no criterion changed; both selections recorded **before** `O-4` runs |
| **`AC-2`** — zero performance computation | **Preserved.** None computed; none used |
| **`AC-3`** — `ND-n` quarantine | **Preserved.** `ND-1 … ND-7` not used |
| **`AC-4`** — symmetric candidate handling | **Preserved.** P-A is candidate-neutral; no candidate-specific span, date, or rule |
| **`AC-5`** — derived from a rule, never chosen | **Preserved and reinforced** — `OD-P15-09`. No date is derived here |
| **`AC-6`** — point-in-time discipline | **Preserved.** `OD-P15-08` keeps point-in-time equivalence expressly unestablished |
| **`AC-8`** — no scoring, no weights | **Preserved.** None introduced |
| **Invariant 17** | **Not triggered.** No Baseline parameter is set: no date, no cutoff value. It becomes live when `P1-5`'s date and `P1-6` are fixed |
| **`SC-17`** | **NOT triggered.** No proxy selected on strategy performance; no `ND-n` proposed as a discriminator |
| **`SC-18`** | **NOT triggered.** See §12.4 |
| **`SC-19`** | **NOT triggered.** No prior finding narrowed, withdrawn, or downgraded. D-6, D-8, D-9, D-10, `HG6-OD-*`, `SC6-OD-*`, `HG9-OD-*`, `G-OD-*`, `OD-P15-01 … 06` and the bounded-reapplication result are preserved in full |

### 12.4 `SC-18` disposition

**Considered and NOT triggered.**

Recording both selections required **no change to any normative frozen text** — not the Frozen
Baseline, not OD-01 … OD-14, not `HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6`,
`SC-1 … SC-20`, `AC-1 … AC-8`, and not `R-1 … R-4`, which are neither edited nor extended. **P-A is
admitted by Interpretation B, already committed**, and satisfies OD-12 / §14.6 on its own terms.
**Coexistence check performed at each disposition, and no conflict found.**

`SC-18` **would** fire if an `O-4` finding were later used to alter the principle, the cutoff, the
floor, or any frozen criterion — which `OD-P15-12` prohibits and routes to Owner Review instead.

---

## 13. Authorization boundary

> **This decision authorizes preservation of the Owner Decision only. It does NOT authorize bounded
> `O-4` research.**

Not authorized by this decision, and not performed: `O-4` research; methodology-history retrieval;
historical-observation retrieval; establishing the first post-base observation date; any series
construction; any empirical calculation; `HG-8` reapplication; any Stage-G reapplication; `OJ-1`;
`OJ-6`; Primary Proxy selection; deriving `P1-5`'s date; selecting `P1-6`; Stage H; Phase 2.

**A separate Owner authorization is required to begin bounded `O-4` research**, and the date on which
that authorization is recorded becomes the `O-4` Research Cutoff value under §8.

---

## 14. Resulting governance state

| Item | State |
| ---- | ----- |
| **Frozen Phase-0 Baseline** | **UNCHANGED.** OD-01 … OD-14 untouched |
| **Criteria freeze** | **UNCHANGED.** `1e8bc85` remains the boundary |
| `P1-5` | **OPEN** — **principle SELECTED (P-A); date NOT YET DERIVED** |
| `P1-6` | **OPEN** — no Baseline Dataset Cutoff selected |
| `O-4` | **OPEN** — no research begun; **bounded research NOT YET AUTHORIZED** |
| `O-4` Research Cutoff | **Rule adopted (K1); value NOT YET FIXED** |
| `O-4` research floor | Base Value Date scoping floor — **`OD-P15-06` unchanged** |
| `HG-8`, C-1 ×3 | **NOT EVALUABLE** — not reapplied |
| `HG-6`, C-1 ×3 | **PASS** — unchanged |
| `HG-9`, C-1 ×3 | **PASS**, carrying its recorded limitations — unchanged |
| `HG-12`, C-1 ×3 | **PASS**, carrying its recorded conditions — unchanged |
| `HG-11`, C-1 ×3 | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; not PASS; non-eliminating; carried to `OJ-6` |
| `H-1` | **NOT ESTABLISHED** |
| **D-6, D-8, D-9, D-10** | **UNCHANGED** |
| `P1-9` | **PARTIAL** |
| `OJ-1` | **NOT REACHED — DEFERRED**; not exercised |
| `OJ-2`, `OJ-4`, `OJ-6` | Unexercised |
| C-1 classification | **QUALIFICATION INCOMPLETE** ×3. None DISQUALIFIED; none a QUALIFIED SURVIVOR |
| C-2A | **UNCHANGED** |
| Primary Proxy | **NOT APPROVED — P1-2 remains OPEN** |
| Stage G | **OPEN** |
| Stage H | **NOT BEGUN** |
| Phase 2 | **BLOCKED** |

---

## 15. What this decision does NOT establish

- **A `P1-5` date** — not derived, not selected.
- **`P1-5` completion** — it remains OPEN.
- **`P1-6`** — not selected.
- **An `O-4` Research Cutoff value** — the rule is adopted; the value does not yet exist.
- **`O-4` resolution** — not researched, not authorized.
- **`HG-8`** — not applied, not reapplied, not satisfied.
- **`H-1`**, first live observation, first actual observation, launch date — none established.
- **D-10 satisfaction** — not declared; residual conditions remain live.
- **Full historical-span admissibility**, **point-in-time equivalence**, **full-span retrievability**
  — none established.
- **Warm-up availability** — not established; presently empty for C-1.
- **`OJ-1`** — not exercised; the excluded segment remains excluded.
- **Candidate qualification, ranking, or Primary Proxy selection** — none.
- **`OJ-6`** — not exercised.
- **Stage-G closure** — not effected.

---

## 16. Next authorized decision boundary

The next step is **an Owner authorization, not research.**

A **bounded `O-4` research authorization** may now be prepared. It would carry:

- the **floor** from `OD-P15-06`;
- the **ceiling** = its own recording date, per K1 and §8;
- the **§7.1 proposition** and the **§7.2 enumerative coverage standard**;
- the `G-OD-08` documentary standard;
- an explicit statement that the cutoff is **not** `P1-6`.

The sequence thereafter, subject to separate authorization at each step:

```
bounded O-4 research authorization  (fixes the O-4 Research Cutoff value)
  → bounded O-4 research
  → HG-8 application (explicit Stage-G reapplication authorization required)
  → Stage-G survivor classification (G-OD-14 three-outcome reporting)
  → comparative criteria, ONLY among qualified survivors
  → OJ-6  →  P1-2
  → P1-5 date derived mechanically from P-A  →  P1-6 fixed
  → final historical retrieval, pinned to P1-6
```

**Zero qualified survivors remains a valid, reportable outcome**, and would itself be materially
useful evidence.

---

## 17. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 untouched; §6, §7, §14.6, Invariant 17
  and the Reference-High construction unaltered.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary. `R-1 … R-4` are neither edited, withdrawn, nor extended; **`R-5` is not invented.**
- **`SC-17`, `SC-18` and `SC-19` considered and NOT triggered.**
- **`OD-P15-01 … 06` are unchanged and controlling**, and this decision is taken under them.
- **D-6, D-8, D-9 and D-10 are unchanged.** **D-10 is not converted into a hard gate**, and the
  post-base-date C-1 segment is **not** declared to satisfy it.
- **`HG-8` remains the sole remaining qualification-blocking gate** for the C-1 candidates.
- **The `HG-6` capability interpretation, the `SC-6` post-base-date interpretation, the `HG-9`
  decision, the Stage-G authorization semantics, the bounded Stage-G reapplication, and the
  sequencing decision are all unchanged.** No prior artifact was modified and no history was
  rewritten.
- **`HG-6` PASS ×3, `HG-9` PASS ×3, `HG-12` PASS ×3 preserved exactly**, each carrying its recorded
  limitations or conditions. **`HG-11` preserved exactly** as BOUNDED QUALIFICATION — UNCLEAR, NOT
  POSITIVELY RESTRICTED: not PASS, non-eliminating, carried to `OJ-6`.
- **`P1-5` remains OPEN** — principle selected, **date not derived**.
- **`P1-6` remains OPEN**, and the `O-4` Research Cutoff must never silently become it.
- **`O-4` remains OPEN. No `O-4` research was performed, and none is authorized by this decision.**
- **`OJ-1` remains NOT REACHED — DEFERRED and was not exercised.**
- **`H-1` remains NOT ESTABLISHED. `P1-9` remains PARTIAL.**
- **All three C-1 candidates remain QUALIFICATION INCOMPLETE.** None DISQUALIFIED; none a QUALIFIED
  SURVIVOR.
- **C-2A is unchanged**, and was neither resolved nor constructed.
- **No Primary Proxy is approved. P1-2 remains OPEN.** `OJ-6` remains Owner-reserved.
- **No external access was performed**, no document retrieved, no observation retrieved, no external
  store inspected for new substantive evidence, no series constructed, and no empirical calculation
  performed.
- **No performance quantity was computed.** `ND-1 … ND-7` were not used.
- **No historical value appears in this artifact.**
- **Stage G remains OPEN. Stage H has not begun. Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. `OD-P15-07` … `OD-P15-12` recorded. `P1-5` principle: **P-A —
EARLIEST ADMISSIBLE OBSERVATION**, meaning "not excluded under D-6 / `SC-6`" and nothing more.
`P1-5`: **OPEN** — date NOT YET DERIVED. `O-4` Research Cutoff rule: **K1** — the date the bounded
`O-4` research authorization is recorded; **value NOT YET FIXED, and NOT this artifact's date**.
Floor: `OD-P15-06`, unchanged. D-10: unchanged, not a gate, residual conditions live. `HG-8`: **NOT
EVALUABLE** ×3 — still the sole remaining qualification-blocking gate. `OJ-1`: **NOT REACHED —
DEFERRED**, unexercised. `P1-6`: **OPEN**. Bounded `O-4` research: **NOT YET AUTHORIZED**.
Candidates: **QUALIFICATION INCOMPLETE**. Stage G: **OPEN**. Primary Proxy: **NOT APPROVED — P1-2
remains OPEN**. Phase 2: **BLOCKED**.**
