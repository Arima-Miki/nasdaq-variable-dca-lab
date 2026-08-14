# Simulation Trial — Mode P: Bounded Release of Stage-D `NDXJPY` for the First Provisional Historical Simulation

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.**
`MP-NDX-D1` **APPROVE WITH CONDITIONS** · `MP-NDX-D2` **ACCEPT** · `MP-NDX-D3` **APPROVE**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13)
**Controlling Mode-P authority:** Decision Boundary `91378fe` · Execution Plan `535de39` ·
Source-Selection Policy `f6c79ce` · DATA-READY implementation `1dd51a8`
**Criteria freeze:** `1e8bc85` — **unchanged by this artifact**

**One artifact, not two.** The `D-5`/`S.2` release and the §18.4.7 acceptance concern **one dataset,
for one bounded purpose, decided at one moment**. Repository precedent bundles related Owner
Decisions in a single artifact (`BV2-OD-01…12`, `ME-OD-01…12`, `AP-OD-01…08`). Splitting them would
allow the release to be preserved without its contamination acceptance, which is exactly the pairing
that must not come apart.

---

## 1. Correction to a preserved artifact — recorded, not silently fixed

Candidate ledger edition 001 (`f6c79ce`) states that Owner Decision **`D-5`** *"forbade"* analysing
the incidentally-returned values. **That characterisation is wrong.** `D-5` reads:

> *"Incidental value return does not itself trigger `SC-16`; retrieval is not analysis; `SC-16`
> triggers only if a determination would require **analysing** values."*

`D-5` is **permissive** — it clarifies that mere retrieval does not trip a stop condition. The actual
restriction lies elsewhere (§2 below). Ledger 001 is preserved and **must not be edited**; under the
edition rule this correction carries forward into edition 002. The practical conclusion of ledger 001
— that Owner release is required before these values may be used — **survives the correction**, but
for a different and more precise reason.

---

## 2. Exact state of the restriction

Three provisions bear on the held material. Only the second restricts it.

| Provision | Verbatim effect | Bearing |
| --- | --- | --- |
| **`D-5`** (Stage-D) | *"retrieval is not analysis; `SC-16` triggers only if a determination would require analysing values"* | **Permissive.** Not a prohibition |
| **`S.2` minimisation rule** (criteria freeze `1e8bc85`) | *"If a source cannot provide date-spine metadata without also technically returning values, **retain the minimum material necessary and do not analyse the values.**"* | **THE OPERATIVE RESTRICTION** |
| Stage-D `PROVENANCE.md` | *"retained for local audit and re-verification only"* | Self-imposed retention scope, narrower than simulation |

`S.2` also states that its authorization *"does NOT include empirical value analysis"* and must not be
used to analyse *"index levels for performance comparison … drawdowns … strategy outcomes … or any
information used to rank candidates by historical performance."*

**What `S.2` is.** It is the **qualification study's external-research authorization**. Its
prohibitions define the limits of *that* authorization, and its trailing clause — *"or any
information used to rank candidates by historical performance"* — shows the target: preventing the
qualification study from ranking candidates empirically. It does not purport to govern the Simulation
Trial lane, which Baseline v2 §18.4 authorizes separately.

**Why Owner release is nevertheless required.** The material was **retained** under an undertaking
not to analyse it. A Mode-P run computes drawdowns and strategy outcomes from exactly those values.
Repurposing material held under a non-analysis undertaking, without an explicit release, would be
precisely the kind of quiet reinterpretation this repository's discipline exists to prevent —
whatever the lane. **The release must be express.**

### Stop conditions checked and NOT triggered

| Condition | Assessment |
| --- | --- |
| **`SC-16`** — *"Date-spine metadata cannot be obtained without retrieving and analysing values"* | **Not triggered.** `SC-16` governs whether a **study determination** requires value analysis. Mode P makes no qualification determination — §18.4.3 bars its output from establishing `P1-2`, `P1-5`, `P1-6`, `O-4` or `HG-8`. `D-5` says so directly |
| **`SC-18`** — *"Any frozen criterion would need to change after evidence is seen"* | **Not engaged.** No frozen criterion changes. `HG-1…13`, `CT-1…9`, `ND-1…7`, `OJ-1…6`, `SC-1…20`, `AC-1…8`, `R-1…4`, `H-1…8` are untouched, `S.2` is unchanged **for every qualification purpose**, and nothing is altered to accommodate observed evidence — **no Mode-P result exists** |
| **`AC-1`** — criteria frozen before evidence | Untouched; this artifact changes no criterion |
| **`P1-8`** / redistribution | Unaffected. Nothing is published, redistributed, or committed |
| `S.2` external-storage rule — material *"structurally outside the repository"* | **Satisfied and preserved**: the Mode-P input stays in the external store; the repository holds no raw data |

**No independent repository provision prohibits this bounded use.**

---

## 3. §18.4.7 — a disclosure obligation, not a prohibition

§18.4.7 prohibits **uses of Simulation Trial output**; it does not prohibit running. It bars using
output to *"select a candidate because it performs better; derive or redefine P1-5; select P1-6
opportunistically; reinterpret O-4; weaken HG-8; alter any evidence hierarchy; alter any
search-exhaustion rule; exclude an unfavourable candidate;"* or change strategy thresholds outside a
governed hypothesis process. Its **disclosure rule** then requires:

> *"Where a qualification decision is taken after any Simulation Trial result exists, the deciding
> artifact MUST state that such results were known and affirm that they were not used normatively."*

**The entanglement here is maximal, and the Owner should decide it knowingly.** `NDXJPY` is **one of
the three active `C-1` candidates** (`NDXJPY`, `XNDXJPY`, `XNDXNNRJPY`), all currently
**QUALIFICATION INCOMPLETE**. Running Mode P on a live candidate's own series means:

**What every future qualification artifact must disclose.** Any artifact deciding `O-4`, `P1-2`,
`P1-5`, `P1-6`, `HG-8`, Stage G, Stage H, or Primary Proxy selection — for **any** candidate, not
only `NDXJPY` — must state that Mode-P results on `NDXJPY` were known and affirm they were not used
normatively.

**What must remain logically separated.** Mechanical engine behaviour on `NDXJPY` values is
**not** evidence about `NDXJPY`'s suitability, continuity, return composition, licensing, or
qualification. The qualification lane must continue to reach its conclusions from `HG`/`CT`/`ND`/`OJ`
evidence alone.

**What cannot be inferred from the Mode-P result — ever.** That `NDXJPY` is suitable or unsuitable as
a proxy; that it should be preferred to `XNDXJPY` or `XNDXNNRJPY`; anything about `O-4`, `HG-8`,
`P1-2`, `P1-5`, `P1-6` or `H-1`; that its data quality is adequate for formal work; or that any
strategy is superior.

**Ongoing cost.** A permanent, recurring disclosure sentence in every future qualification artifact,
and a standing obligation to keep the reasoning separate. It is **real and irreversible** — the
knowledge cannot be un-known (§18.4.7: *"Blinding is neither claimed nor practical"*). It does not
prohibit anything the project intends to do.

---

## 4. Limitation classification

Per the four required categories, not collapsed.

### HARD BLOCKER
**None found.**

### CONDITIONAL / ACCEPTABLE WITH DISCLOSURE
- The `S.2` non-analysis undertaking — cured **only** by the express release below.
- §18.4.7 entanglement with a live `C-1` candidate — cured by acceptance and permanent disclosure.
- Stage-D retention scope *"local audit and re-verification only"* — widened, narrowly, by this release.

### NON-BLOCKING IMPERFECTION
- **Span ends 2020-06-26.** The previously contemplated 2018→2022 window is **impossible**; the
  usable window is **2018-01-02 → 2020-06-26** — 626 observations, 3 calendar years, 30 distinct
  months. That still spans the late-2018 drawdown, the early-2020 crash and the recovery, so all
  three zones and Strategy C's fallback remain reachable. **Shorter is preferred** under `MP-P-D1`.
- Single price series; no cross-source corroboration. Irrelevant to mechanical validation.
- The **drawdown-rich span bias** already recorded: B and C are structurally more active than A, so
  this span is **permanently barred from performance comparison**. Harmless because `MP-D3` forbids
  performance reporting.

### FORMAL-ONLY ISSUE
- **Return composition** (`P1-3`) — `NDXJPY` is *declared* a JPY price index by naming convention;
  **not verified** in this task.
- **Back-tested vs actual history.** The file carries Nasdaq's disclaimer that pre-launch values are
  *"merely indicative,"* and Stage-D item `E-09` records that **no launch-date register exists for
  the JPY series** — so whether the 2018–2020 segment is actual or back-tested is **NOT ESTABLISHED**.
  Material for `HG`/`SC-6` and formal work; **not** a blocker for a disclosed provisional run.
- `P1-1`, `P1-4`, `P1-7`, `P1-8`, `P1-9`, `M-1…M-8` — all unchanged and unaffected.

---

## 5. Owner Decision Sheet

> ### `MP-NDX-D1` — Release decision
> **Question.** May the already-held Stage-D `NDXJPY` dataset be released from its `S.2`
> non-analysis undertaking and Stage-D retention scope, for **one** bounded Mode-P provisional
> historical simulation?
>
> **Disposition: APPROVE WITH CONDITIONS `[APPROVED — OWNER DECISION 2026-08-14]`** (§6).
>
> **Controlling reason.** No repository provision prohibits it. `D-5` is permissive; `SC-16` governs
> study determinations and Mode P makes none (§18.4.3); `SC-18` is not engaged because no frozen
> criterion changes; §18.4.7 imposes disclosure, not prohibition; §18.3 expressly permits Simulation
> Trial execution *"before those gates are cleared."* The only genuine obstacle is the `S.2`
> undertaking under which the bytes were retained — an **Owner-imposed** restriction the Owner may
> expressly and narrowly release. **Owner release is therefore sufficient.**
>
> **Unresolved even if approved:** `P1-2`, `P1-3`, `P1-9`, `O-4`, `HG-8`, `H-1`, all `M-x`. No
> candidate is qualified; no Primary Proxy exists.

> ### `MP-NDX-D2` — §18.4.7 anti-contamination acceptance
> **Question.** Accept the resulting disclosure duty and separation requirements?
>
> **Disposition: ACCEPT `[ACCEPTED — OWNER DECISION 2026-08-14]`.** The Owner has expressly
> accepted that Mode-P results, once observed, cannot be unseen.
>
> **Exact ongoing cost.** Every future artifact deciding `O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`,
> Stage G, Stage H or Primary Proxy selection — for **any** candidate — must state that Mode-P
> results on `NDXJPY` were known and affirm they were not used normatively. §18.4.7 is **not
> weakened** by this acceptance.

> ### `MP-NDX-D3` — Dataset classification
> **Question.** May it be labelled `dataset_class: provisional`, and what further labels are required?
>
> **Disposition: APPROVE `[APPROVED — OWNER DECISION 2026-08-14]`** — `dataset_class: "provisional"`
> per §18.4.9, **plus** these mandatory
> labels in the manifest and every output:
>
> - `PROVISIONAL · NOT QUALIFIED · NON-FORMAL · NON-PROMOTABLE · SIMULATION-TRIAL ONLY`
> - `SOURCE: STAGE-D QUALIFICATION EVIDENCE, RELEASED FOR SIMULATION USE ONLY`
> - `NDXJPY IS AN ACTIVE C-1 QUALIFICATION CANDIDATE — THIS RUN IS NOT EVIDENCE ABOUT IT`
> - `NOT A PRIMARY PROXY SELECTION — P1-2 REMAINS OPEN`
> - `SPAN CARRIES NO P1-5 / P1-6 SIGNIFICANCE`
> - `BACK-TESTED VS ACTUAL HISTORY NOT ESTABLISHED FOR THIS SEGMENT`
> - `RETURN COMPOSITION DECLARED, NOT VERIFIED — P1-3 OPEN`

No further Owner decisions are required.

---

## 6. Minimum bounded release, if approved

`NDXJPY` **only** — `XNDXJPY` and `XNDXNNRJPY` are **not** released. The already-held Stage-D
snapshot **only**, byte-identical, **checksum-verified before use** against the Stage-D `SHA256SUMS`
(`E-01` = `316dd1a882002d28430a60a966a31601e3224b2bc84346c906f64715b38d52b0`, verified OK on
2026-08-14). Span **2018-01-02 → 2020-06-26** only.

**Prohibited:** replacement or enrichment; span extension; a second source; source blending; any
qualification-state change; any formal metric; TTEV or any governed economic metric; result
promotion; Phase-2 use; and any inference that `NDXJPY` is the Primary Proxy.

**Traceability.** The Mode-P dataset record must cite Stage-D item `E-01`, its original retrieval
date **2026-08-11**, and its Stage-D SHA-256, so the released material remains traceable to its
original provenance. **The Stage-D evidence store is read-only to this work and MUST NOT be
modified**; the Mode-P store is separate. Raw data remains **structurally outside** the repository,
as `S.2` requires.

---

## 7. State preservation

Unchanged by this artifact: `O4-PARTIAL ×3` · `GAP-A ×3` · `GAP-B ×2` · `HG-8 NOT EVALUABLE ×3` ·
`P1-2 OPEN` · `P1-5 OPEN` (P-A selected, **date not derived**) · `P1-6 OPEN` · `H-1 NOT ESTABLISHED` ·
`P1-9 PARTIAL` · `C-1 ×3 QUALIFICATION INCOMPLETE` · **no Primary Proxy** · Stage G **OPEN** ·
Stage H **NOT BEGUN** · Phase 2 **BLOCKED** · `M-1 … M-8` unresolved · Mode P **NON-FORMAL and
NON-PROMOTABLE**. The Frozen Baseline and the criteria freeze `1e8bc85` are **not altered**.

---

## 8. Resulting readiness

If `MP-NDX-D1`–`D3` are approved, the repository becomes **HISTORICAL-INPUT-READY MODE P: YES** —
a DATA-READY simulator (`1dd51a8`) plus one released, checksum-verified provisional historical input.

The shortest next instruction is then **execution**, not research: authorize the first bounded Mode-P
historical simulation — extract the 2018-01-02 → 2020-06-26 `NDXJPY` window into the Mode-P store,
run Strategies A, B and C against that one dataset, verify determinism and replay, report only
`MP-D3` quantities, and **STOP**.
