# Phase 1 Primary Proxy Qualification — `SC-6` Scope and Post-Base-Date Segment Owner Decision

**Status:** APPROVED — scope interpretation recorded

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Scope of the §6.4 mandatory segment classification and of `SC-6`, as applied to the C-1 post-base-date segment; and the consequence for `HG-12` capability evaluation |
| Decision status | **APPROVED** |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Related Owner Decisions | **D-6** (Stage-D pre-base-date classification) — **unchanged**; **G-OD-10** (Stage-G `HG-12` pinning standard) — **unchanged**; [`phase1_primary_proxy_hg6_capability_interpretation_decision.md`](phase1_primary_proxy_hg6_capability_interpretation_decision.md) — **unchanged** |
| Controlling Frozen Baseline authority | [`../experiment_spec.md`](../experiment_spec.md) §6 (look-ahead prohibition), §14.6 / OD-12 (Baseline period and dataset cutoff) |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| Adopted `HG-12` interpretation | **I-1** — `HG-12` requires candidate-series retrieval/pinning capability only |
| Stage-G execution result | **NOT MODIFIED.** `HG-12` remains recorded NOT EVALUABLE |
| Stage-G reapplication | **NOT AUTHORIZED** by this decision |
| `H-1` | **NOT ESTABLISHED** — unchanged |
| `OJ-1` | **NOT REACHED — DEFERRED**; not exercised |
| `HG-9` | **UNRESOLVED** — pending separate Owner review |
| `O-4`, `P1-5`, `P1-6` | **OPEN** — unchanged |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision** interpreting the **scope** of provisions already frozen in the
study design. It is a semantic clarification, not evidence, not a gate result, and not a stage
result.

> **It is NOT a modification of the Phase-0 Baseline, and NOT a modification of the frozen
> qualification criteria.**

The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this decision
and that specification could be read as differing, **the specification governs Baseline behavior**.
`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and
`1e8bc85` remains the criteria-freeze boundary.

This decision contains **no evidence, no gate result, no candidate classification, no Baseline
result, no performance claim, and no historical value.**

---

## 2. Why this interpretation became necessary

The frozen study design states the segment-classification rule in two places, at two scopes:

- **§6.4**, whose third class — NON-LIVE, UNCHARACTERIZED — is defined as *values exist but status
  cannot be established*, with the consequence that `SC-6` applies and the segment may not be used;
- **§13**, whose stop-condition register scopes the same condition to *pre-launch history exists but
  its status cannot be determined*.

Read in isolation, §6.4's phrasing would sweep in **any** segment whose LIVE status has not been
affirmatively established — including segments that are not pre-launch and are not asserted to be
non-live. Read with §13, it does not.

The question became operative because a bounded, Owner-authorized capability investigation
established that publisher-direct observations for the C-1 post-base-date segment demonstrably exist
and are retrievable. Before that, the point was moot. It is now the single semantic question
standing between accepted capability evidence and a future `HG-12` evaluation.

**The two provisions are reconciled below without either being rewritten.**

---

## 3. Decisions

### 3.1 `SC6-OD-01` — `SC-6` is a scoped exclusion rule

`SC-6` applies to history whose relevant status places it within the **pre-launch / non-live /
uncharacterized-history problem** governed by the Frozen Baseline.

> **`SC-6` must NOT be expanded into a universal rule that every observation segment whose LIVE
> status has not been affirmatively established is automatically excluded.**

### 3.2 `SC6-OD-02` — §6.4 must be read together with §13

The §6.4 class definition — *values exist but status cannot be established* — **must not be read in
isolation from the stop-condition register**. Where §13 scopes `SC-6` to *pre-launch history exists
but its status cannot be determined*, **that scope remains operative**.

> **Therefore: absence of affirmative LIVE evidence alone does not automatically classify every
> post-base-date observation as NON-LIVE, UNCHARACTERIZED.**

### 3.3 `SC6-OD-03` — D-6 remains untouched

The Stage-D Owner Decision concerning the **pre-base-date** segment remains **fully controlling**.
That segment remains **NON-LIVE, UNCHARACTERIZED** with **`SC-6` triggered**.

> **Nothing in this decision reopens, weakens, or modifies D-6.**

### 3.4 `SC6-OD-04` — Post-base-date C-1 segment

For `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`, the post-base-date segment is **NOT automatically
`SC-6`-excluded** merely because `H-1` = NOT ESTABLISHED.

The correct bounded state is:

| Element | State |
| ------- | ----- |
| Position | **Post-base-date** |
| Publisher-direct observations | **Demonstrably exist and are retrievable** |
| `H-1` LIVE status | **NOT ESTABLISHED** |
| `SC-6` exclusion | **NOT ESTABLISHED** for that segment |

> **This decision does NOT affirmatively declare the segment LIVE. It does NOT declare
> historical-span admissibility established.**

### 3.5 `SC6-OD-05` — Negative versus positive proposition

The distinction is **mandatory** and must be preserved in every downstream artifact:

> **"not established as LIVE" does NOT mean "established as NON-LIVE."**
>
> **"`SC-6` exclusion not established" does NOT mean "full historical admissibility established."**

**Do not collapse these states.**

### 3.6 `SC6-OD-06` — `HG-12` consequence

For **`HG-12` capability evaluation only**, a publisher-direct post-base-date observation may
support retrieval and pinning capability where all of the following hold:

1. the candidate identity is established;
2. the observation route is authorized;
3. the segment is not already `SC-6`-excluded;
4. reproducible retrieval is demonstrated;
5. pinning is demonstrated.

**Affirmative `H-1` LIVE establishment is not additionally required by `HG-12`.**

> **This does NOT automatically set `HG-12` = PASS. A later authorized Stage-G reapplication must
> apply the gate.**

### 3.7 `SC6-OD-07` — `H-1` remains unresolved

**`H-1` remains NOT ESTABLISHED.** This decision does not establish the earliest live observation
date, live-history continuity, complete historical admissibility, or intended-span live coverage.

`H-1` continues to feed the appropriate later Owner judgments and comparative criteria.

### 3.8 `SC6-OD-08` — `OJ-1` remains unexercised

**`OJ-1` is not exercised by this decision.**

The decision does **not** authorize use of the already-excluded pre-base-date segment for measured
performance, for warm-up, or for any other qualification purpose.

### 3.9 `SC6-OD-09` — `CT-2` remains comparative

`CT-2` remains a **comparative criterion**. It must **not** be used to strengthen `HG-12` or to
create an additional hard-gate requirement. Its eventual evaluation may still depend on `H-1` and on
intended-span selection.

### 3.10 `SC6-OD-10` — `HG-9` remains separate

The **absence of revision/version metadata** on the demonstrated access route does not alter this
decision. That question remains assigned to **`HG-9`**, which is **not resolved here**.

### 3.11 `SC6-OD-11` — No Frozen Baseline amendment

This decision is an **interpretation of existing scope**. It does not add, remove, or weaken a hard
gate; change a comparative criterion; change a stop condition; change OD-01 … OD-14; change the
Reference-High construction; or set `P1-5` or `P1-6`.

**Coexistence check performed, and no conflict found.** §6.4 and §13 are both provisions of the
frozen study design, not of the Frozen Baseline; this decision reconciles their scopes **without
rewriting either**. Neither the Frozen Baseline nor the criteria-freeze artifact required any
normative change in order to record it, so **`SC-18` is not triggered** and no conflict is returned
to the Owner.

---

## 4. Adopted `HG-12` interpretation

The Owner adopts **I-1**:

> **`HG-12` requires candidate-series retrieval/pinning capability only. `SC-6` exclusion still
> applies, but affirmative `H-1` LIVE establishment is not a prerequisite unless the demonstrated
> segment is actually excluded.**

Accepted alongside it, and recorded here so the reasoning is not lost:

- `H-1` is an **evidence / handoff state, not an additional hard gate**;
- `CT-2` **must not be imported** into `HG-12`;
- `OJ-1` **need not be exercised** merely to evaluate retrieval and pinning capability;
- revision/version uncertainty **remains reserved to `HG-9`**;
- `P1-5` and `P1-6` are **not prerequisites** to `HG-12` capability evaluation;
- the existing Stage-G result **remains unchanged** until a separately authorized reapplication.

---

## 5. What this decision does NOT do

- It does **not** declare the post-base-date segment **LIVE**.
- It does **not** declare historical-span admissibility established.
- It does **not** set `HG-12` = PASS, or change `HG-12`'s recorded NOT EVALUABLE state.
- It does **not** authorize a Stage-G reapplication.
- It does **not** reopen, weaken, or modify **D-6**, and does **not** un-exclude the pre-base-date
  segment.
- It does **not** establish `H-1`, exercise `OJ-1`, or resolve `HG-9`.
- It does **not** resolve `O-4`, `O-3`, `N-2` continuity, `N-3`, `N-4`, or `P1-8`.
- It does **not** set `P1-5` or `P1-6`.
- It does **not** approve a Primary Proxy or exercise `OJ-6`.
- It does **not** authorize Stage H or unblock Phase 2.

---

## 6. Anti-circularity

- **`AC-1`** — the criteria remain frozen at `1e8bc85`. This decision reconciles the scope of two
  existing provisions; it does not change what any criterion requires, and it is recorded **before**
  any reapplication so that semantics are not fitted to a result already seen.
- **`AC-2`** — no performance quantity was computed. No observation value informed this decision,
  and none appears in it.
- **`AC-3`** — `ND-1 … ND-7` were not used.
- **`AC-4`** — the interpretation applies identically to all three C-1 series.
- **`AC-6`** — point-in-time discipline preserved: `SC6-OD-10` keeps the revision hazard live and
  assigned to `HG-9`.
- **`AC-8`** — no scoring or weighting introduced.
- **`SC-18`** — considered and **not triggered**; see `SC6-OD-11`.

---

## 7. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched; §6, §7, §14.6 and the
  Reference-High construction are unaltered.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary; §6.4 and §13 are reconciled, not rewritten.
- **D-6 remains fully controlling.** The pre-base-date segment remains NON-LIVE, UNCHARACTERIZED
  with `SC-6` triggered.
- **The post-base-date segment is not declared LIVE and is not declared fully admissible.**
- **`H-1` remains NOT ESTABLISHED. `OJ-1` remains unexercised. `HG-9` remains unresolved.**
- **`HG-12` is not changed**; the existing Stage-G result stands, and **Stage G was not re-run**.
- **`G-OD-10` and the `HG-6` capability interpretation are unchanged.**
- **No prior artifact was modified, and no history was rewritten.**
- **No Primary Proxy is approved. P1-2 remains OPEN.** `OJ-6` remains Owner-reserved.
- **No external access was performed in reaching this decision.**
- **Stage H has not begun. Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. `SC-6`: scoped exclusion rule, read with §13. Post-base-date C-1
segment: `SC-6` exclusion NOT ESTABLISHED — and NOT declared LIVE. D-6: untouched. `HG-12`
interpretation: **I-1**, capability only. `H-1`: NOT ESTABLISHED. `OJ-1`: unexercised. `HG-9`:
unresolved. Stage-G result: not modified. Stage-G reapplication: NOT AUTHORIZED. Primary Proxy: NOT
APPROVED — P1-2 remains OPEN. Phase 2: BLOCKED.**
