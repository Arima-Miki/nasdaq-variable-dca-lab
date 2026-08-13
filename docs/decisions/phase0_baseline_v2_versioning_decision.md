# Phase 0 — Baseline v2 Versioning Owner Decision

**Status:** **APPROVED — Baseline v2 preserved. Baseline v2 is NOT YET EFFECTIVE.**

**Scope:** Phase 0 — Baseline change control

**Decision date:** **2026-08-13** — the date of explicit Owner approval. **This is NOT the Baseline-v2 effective date.**

**Effective date of Baseline v2:** **NOT YET SET — Owner action required (§7)**

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-0 Owner Decision — Baseline versioning** |
| Decision status | **APPROVED — preservation only; NOT activation** |
| Subject | Creation of an explicitly versioned successor Baseline separating experimental-tooling permission from formal-result permission |
| Owner dispositions | `BV2-OD-01` … `BV2-OD-12` |
| Successor artifact | [`../experiment_spec_v2.md`](../experiment_spec_v2.md) — **APPROVED AND PRESERVED, NOT YET EFFECTIVE** |
| Predecessor | [`../experiment_spec.md`](../experiment_spec.md) — Baseline v1, blob `3a18862b…`, tag `phase0-baseline-v1` — **UNCHANGED, NOT AMENDED** |
| Route adopted | **R2-B** — versioned successor creating the Simulation Trial **framework**, authorizing **neither** mode. **R1 (reinterpretation of v1 §18.3) expressly NOT adopted** |
| Instrument form | **FULL RESTATEMENT** — `OD-REQ-3` adopted. v2 is complete and standalone once activated |
| Sole changed provision | **v1 §18.3** — restated at v2 §18.3 |
| Sole addition | **v2 §18.4** — Simulation Trial lane |
| Change surface | **VERIFIED MECHANICALLY** — see §3.1 |
| Lane naming | **Simulation Trial**; **Mode E** Engine Validation; **Mode P** Provisional Economic Simulation — `OD-REQ-5` adopted |
| `SC-18` | **ENGAGED — recorded openly.** See §6 |
| Criteria freeze `1e8bc85` | **NOT MODIFIED.** `AC-7` treatment at §5; cross-reference rule `OD-REQ-2` adopted at §5.2 |
| Phase 2 | **BLOCKED — unchanged** |
| Qualification state | **UNCHANGED** in every respect — §8 |
| Authorization created | **NONE.** No mode, no code, no simulation |

### Artifact role and precedence

This decision records **reasoning and the versioning act**. The normative successor text is
`experiment_spec_v2.md`. This follows the existing separation of concerns: `experiment_spec.md` is
normative, `phase0_baseline_decisions.md` explains reasoning only.

> **Baseline v1 is not amended, not rewritten, and not invalidated.** It remains the immutable
> controlling authority for all work performed under it.

---

## 2. Authority permitting successor versioning

`BV2-OD-01`. The repository provides an **explicit** route. Three provisions, read together:

| Source | Text relied upon |
| ------ | ---------------- |
| `phase0_baseline_decisions.md`, *Change control after the Freeze* | *"Subsequent changes to thresholds, sizing, cash assumptions, escalation behavior, annual budget, Reference High definition, **or any other Baseline rule** are not Baseline changes unless the research governance explicitly creates a **new Baseline version**."* |
| v1 §18.2 | *"Any later change … MUST be either a **new, explicitly versioned Baseline created under research governance**, or sensitivity analysis reported separately. It MUST NOT be applied as a silent edit to this Frozen Baseline."* |
| v1 §18.3 | *"Neither this Freeze nor **any later revision** may be applied by anyone other than the Owner."* |

**Three findings:**

1. **The route exists.** Versioning is the repository's own prescribed mechanism, not an invention.
2. **It reaches §18.3.** The change-control clause generalises to *"any other Baseline rule"*; §18.3's
   code prohibition is a Baseline rule. The enumerated list is illustrative of what *requires*
   versioning, not exhaustive of what *may be* versioned.
3. **The Owner is the actor.** v1 §18.3 reserves any later revision to the Owner alone.

> **No conflict with immutable authority was found**, because v1 is not being altered. A successor
> version is precisely what v1 contemplates.

---

## 3. What changes, and what does not

`BV2-OD-02`. **The changed normative surface is one provision.**

| v1 provision | Disposition |
| ------------ | ----------- |
| **§18.3** | **CHANGED** — restated at v2 §18.3, separating formal-study code from Simulation Trial code |
| **§18.4** | **ADDED** — the Simulation Trial lane, authorizing nothing by itself |
| **§§0–17, §18.1, §18.2, §19, §20** | **UNCHANGED** — restated verbatim; see §3.1 |
| **OD-01 … OD-14** | **UNCHANGED** |

`BV2-OD-03`. **No provision is silently carried forward.** v2's Version provenance section states the
approved change surface explicitly, and §3.1 below verifies mechanically that nothing outside it
differs.

### 3.1 Change surface — mechanically verified

`OD-REQ-3` adopts **FULL RESTATEMENT**, and requires that *"any accidental difference outside the
approved change surface is a defect and must STOP preservation."*

**v2 was therefore built mechanically from v1, not transcribed by hand**, and the result was verified
by direct comparison:

| Check | Result |
| ----- | ------ |
| v1 lines 11–1066 (title block through §18.2) present in v2 **verbatim, contiguous** | ✅ |
| v1 lines 1089–end (§19, §20) present in v2 **verbatim, contiguous** | ✅ |
| v1 restated-scope lines **absent** from v2 | **0** |
| Differing hunks | **exactly three**: the version-identity header; §18.3; the §18.4 insertion |
| §18.3 lines changed | only the three code bullets (now `formal`), plus the added *formal execution* definition and the Simulation Trial clause. Every other §18.3 line **KEPT verbatim** |

> **No difference exists outside the approved change surface.** The version-identity header is version
> metadata, not a normative provision, and is declared as such in v2's Version provenance section.

`BV2-OD-04`. **The minimal-change principle is honoured.** Nothing unrelated is redesigned: no
threshold, sizing parameter, budget, cash assumption, escalation behaviour, Reference-High
definition, qualification criterion, hard gate, comparative criterion, stop condition,
anti-circularity rule, publication control, or evidence standard changes.

---

## 4. The substantive change

`BV2-OD-05`. v1 §18.3 coupled two distinct permissions:

- **(A)** permission to develop and execute **experimental simulation tooling**;
- **(B)** permission to produce **formal Baseline / Phase-2 results**.

v2 separates them. **(B) is preserved without relaxation** — v2 §18.3 carries v1's prohibition
forward in full, scoped by an explicit definition of *"formal"*. **(A) becomes available**, but only
under a **separate Owner authorization**, and only for output that is **structurally barred from ever
becoming formal evidence** (v2 §18.4.3).

> **v2 creates a possibility, never a permission.** It authorizes no mode, no code, and no run.

---

## 5. `AC-7` and the criteria freeze — critical

`BV2-OD-06`. **The criteria-freeze artifact is NOT modified. `1e8bc85` remains the criteria-freeze
boundary.**

`AC-7` reads:

> *"**Sequencing gate** — P1-2 is approved before any Phase-2 code exists; §18.3 already forbids
> backtest code, methodology code, and data loaders."*

**It has two clauses, and they must be separated:**

| Clause | Nature | Effect of v2 |
| ------ | ------ | ------------ |
| **1.** *"P1-2 is approved before any **Phase-2 code** exists"* | `AC-7`'s **own operative rule** | **UNCHANGED and fully binding.** Simulation Trial code is expressly **not** Phase-2 code (v2 §18.3), and **Phase 2 remains BLOCKED**. The rule is not engaged, not weakened, and not reinterpreted |
| **2.** *"§18.3 already forbids backtest code, methodology code, and data loaders"* | A **descriptive cross-reference** to v1 §18.3, not an independent prohibition | Remains **accurate about v1 §18.3**, which is unchanged. It does not describe v2 §18.3 |

`BV2-OD-07`. **`AC-7` is not papered over.** The honest position is stated: clause 2 is a citation, and
citations are version-relative. **Under v2, clause 2 must be read as describing Baseline v1 §18.3;
the corresponding v2 provision is §18.3.** Clause 1 continues to bind unchanged.

> **This does not change what `AC-7` requires.** No criterion is added, removed, weakened, widened,
> renumbered, or re-weighted, and `1e8bc85` is untouched.

`BV2-OD-08`. **A successor criteria-freeze artifact is NOT required**, and creating one is
**expressly not recommended**: it would disturb the `1e8bc85` boundary that every downstream artifact
cites, for no normative gain, since `AC-7`'s operative rule is unaffected.

### 5.2 `OD-REQ-2` — criteria cross-reference rule, ADOPTED

For work created **after** Baseline v2 becomes effective, a frozen criterion referring generically to
**"the Baseline"** is read against the **Governing Baseline version explicitly declared for that
work**.

**Four constraints, all binding:**

1. a criterion or artifact that **explicitly identifies** Baseline v1, `experiment_spec.md`,
   `phase0-baseline-v1`, or a specific v1 provision **remains bound to v1** for that reference;
2. **historical artifacts are never retrospectively reinterpreted** under v2;
3. **no qualification criterion changes** merely because the governing Baseline version changes;
4. **no `HG`, `CT`, `AC`, `SC`, `OJ`, `ND` or other frozen criterion is amended** by this rule.

> **The purpose is version resolution only. It creates no substantive qualification change.**

#### 5.2.1 Coexistence check — demonstrated, not asserted

**No conflict with frozen normative text was found, and the reason is structural:**

Because `OD-REQ-3` requires **full restatement**, and §3.1 verifies mechanically that the change
surface is confined to §18.3 and §18.4, **every provision a qualification criterion could reference
is textually identical in v1 and v2**. Resolving a generic reference to v2 therefore returns **the
same text** it would return under v1.

> **Version resolution cannot alter any criterion's meaning, because there is no textual difference
> for it to reach.** The only provisions that differ — §18.3 and §18.4 — are not referenced
> generically by any frozen criterion; **`AC-7` cites §18.3 explicitly**, so constraint 1 binds that
> citation to v1.

**`SC-18` is not *additionally* triggered by this rule**, because no criterion changes. `SC-18`'s
engagement arises solely from the §18.3 change, and is recorded at §6.

---

## 6. `SC-18` treatment — recorded openly

`BV2-OD-09`. **`SC-18` IS ENGAGED.** It is **not** recorded as "not triggered".

`SC-18` reads: *"Any frozen criterion would need to change after evidence is seen."* The substance of
the hazard is present: **a frozen normative rule is being changed, and qualification evidence has
already been seen** — the executed `O-4` research, `O4-PARTIAL` ×3, `GAP-A`, `GAP-B`.

**The required process, and how it is satisfied:**

| Step | Status |
| ---- | ------ |
| The condition is detected and **not worked around** | ✅ Detected in the compatibility analysis; `R1` reinterpretation was **offered and the Owner declined it** |
| The matter **returns to Owner Review** | ✅ It did; the Owner directed **R2** |
| The change is made by the **Owner alone** | ✅ v1 §18.3 reserves revision to the Owner; this decision is an Owner Decision |
| The change is made by **explicit versioning**, not silent edit | ✅ v1 §18.2's prescribed route |
| The change is **recorded with predecessor, rationale, scope, and effective boundary** | ✅ v2 its Version provenance section and §7 here |

> **`SC-18`'s remedy is Owner Review, and Owner Review is what occurred.** The versioned successor
> route is the mechanism the Baseline itself provides for exactly this situation.

### 6.1 The hazard, stated plainly rather than buried

**A frozen rule is being changed after evidence was seen. That is the precise shape of the risk
`SC-18` exists to catch.** Four facts bear on it, and they are recorded so a later reader can judge
for themselves:

1. **The changed rule is a sequencing/permission rule** — not a qualification criterion, hard gate,
   threshold, sizing parameter, budget, evidence standard, or stop condition.
2. **It cannot make any candidate more likely to qualify.** v2 §18.4.3 bars Simulation Trial output
   from establishing `P1-2`, `P1-5`, `P1-6`, `O-4`, `HG-8`, Primary Proxy approval, or any formal
   result. The change is **qualification-neutral by construction**.
3. **The motivation is the project objective**, recorded before any simulation exists — not any
   observed result. **No simulation has ever been run in this repository**, so no result could have
   motivated it.
4. **The evidence that has been seen is unfavourable**, not favourable: `O4-PARTIAL` ×3, applicability
   not established ×3. The change is not being made to rescue a result.

> **Recorded against interest:** none of the above eliminates the hazard. It is mitigated, disclosed,
> and left visible for audit.

---

## 7. Activation

`BV2-OD-10`. **Drafting is not approval. Approval is not activation. Commit is not activation.**

Baseline v2 becomes controlling **only** when all three occur, in order: **(1)** explicit Owner
approval; **(2)** preservation — commit, push, annotated tag `phase0-baseline-v2`; **(3)** an
**explicit Owner statement of the effective date**, recorded in this decision.

**Until all three are complete, Baseline v1 remains the sole controlling Baseline and its §18.3
applies in full.**

This follows the repository's established **S-A** precedent, under which a decision date records the
explicit Owner-approval date and commit/tag merely **preserve** an act already taken. **The effective
date is a separate Owner statement** and is not inferred from any commit, tag, or draft date.

---

## 8. Qualification-lane preservation

`BV2-OD-11`. **Nothing in the Qualification lane changes.** Preserved exactly:

`O4-PARTIAL` ×3 · `GAP-A` ×3 · `GAP-B` ×2 · `HG-8` **NOT EVALUABLE** ×3 · `HG-6` / `HG-9` / `HG-12`
**PASS** ×3 with recorded limitations · `HG-11` **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY
RESTRICTED**, not PASS, non-eliminating, carried to `OJ-6` · `H-1` **NOT ESTABLISHED** · `P1-9`
**PARTIAL** · `P1-2` **OPEN** · `P1-5` **OPEN**, principle **P-A**, date **NOT YET DERIVED** · `P1-6`
**OPEN** · `K1` = **2026-08-13** · C-1 ×3 **QUALIFICATION INCOMPLETE** · C-2A **unchanged** · `OJ-1`
**NOT REACHED — DEFERRED** · `OJ-6` **unexercised** · **no Primary Proxy approved** · Stage G
**OPEN** · Stage H **NOT BEGUN** · **Phase 2 BLOCKED**.

**The `M01`/`M02` follow-on drafts remain untracked and unmodified. `M03` remains not designed, not
authorized, not executed.** Qualification research continues **independently** of this version and is
neither paused nor reprioritized by it.

---

## 9. `AR-01`

`BV2-OD-12`. **`AR-01` remains RECORDED — NOT ADOPTED**, and **NOT EXECUTABLE AS STATED**. It is
**not** made part of any Baseline, and is **not** authorized by the existence of the Simulation Trial
lane.

A later Owner authorization **could** test `AR-01` as an experimental rule variant under v2 §18.4.5,
provided its open executable semantics are first resolved, and provided every run and output is
labelled **`EXPERIMENTAL VARIANT — NOT BASELINE`**. **Testing it neither adopts it nor changes the
frozen Baseline rule.** **No such test is authorized here.**

---

## 10. What this decision does NOT do

- It does **not** activate Baseline v2, or set its effective date.
- It does **not** authorize Mode E, Mode P, any code, any dataset, or any run.
- It does **not** modify Baseline v1, the criteria-freeze artifact, or any existing artifact.
- It does **not** change `P1-2`, `P1-5`, `P1-6`, `P1-9`, `O-4`, `HG-8`, `H-1`, or any candidate state.
- It does **not** unblock Phase 2 or begin Stage H.
- It does **not** adopt `AR-01`, or authorize `M03`, `M01`, or `M02` work.
- It does **not** decide the criteria cross-reference question at `OD-REQ-2`.

---

## 11. Further Owner decisions required — identified, not taken

| # | Decision | Why it is required |
| - | -------- | ------------------ |
| **`OD-REQ-1`** | **Effective date of Baseline v2** | §7 requires an explicit Owner statement; it is not inferable from commit or tag |
| ~~`OD-REQ-2`~~ | **RESOLVED — adopted at §5.2**, with four binding constraints and a demonstrated coexistence check | — |
| ~~`OD-REQ-3`~~ | **RESOLVED — FULL RESTATEMENT adopted.** v2 is complete and standalone; change surface verified at §3.1 | — |
| **`OD-REQ-4`** | **Mode-E authorization** — a separate Owner Decision authorizing Engine Validation, with its own execution plan | v2 §18.3 and §18.4.1 require it; **not** created by this decision |
| ~~`OD-REQ-5`~~ | **RESOLVED — adopted.** **Simulation Trial**; **Mode E** Engine Validation; **Mode P** Provisional Economic Simulation. Names implying Phase-2 entry are prohibited | — |

**`OD-REQ-1` and `OD-REQ-4` remain OPEN and are not decided here.** `OD-REQ-2`, `OD-REQ-3` and
`OD-REQ-5` were decided by the Owner and are recorded above as resolved.

---

## 12. Confirmations

- **Baseline v1 is unchanged, unamended, and not invalidated.** Work performed under it remains valid
  as a historical governance record.
- **The criteria-freeze artifact is unchanged.** `1e8bc85` remains the boundary; **`AC-7`'s operative
  rule is unchanged and fully binding**.
- **`SC-18` is recorded as ENGAGED**, with the process satisfied through Owner Review and explicit
  versioning.
- **Exactly one normative provision changes** — v1 §18.3 — plus one addition, v2 §18.4.
- **The formal-result gate is not relaxed.** Phase 2 remains **BLOCKED**.
- **No authorization of any kind is created.** No mode, no code, no dataset, no simulation.
- **All qualification state is unchanged**, and the Qualification lane continues independently.
- **No external access was performed**, no code was written, no dataset created, no simulation run,
  and no empirical quantity computed.

---

**End of Phase-0 Owner Decision. `BV2-OD-01` … `BV2-OD-12`. Route **R2-B** adopted; **R1
declined**. Authority: v1 §18.2, §18.3 and the *Change control after the Freeze* clause reaching
*"any other Baseline rule"*. Sole change: **v1 §18.3**, restated at v2 §18.3; sole addition: **v2
§18.4**. **`AC-7` clause 1 unchanged and binding; clause 2 is a version-relative citation** — criteria
freeze **not modified**. **`SC-18`: ENGAGED**, disclosed, process satisfied. **Baseline v2: NOT
APPROVED, NOT EFFECTIVE.** No authorization created. Qualification state **unchanged**. Phase 2:
**BLOCKED**.**
