# Phase 1 Evidence Artifact — `O-4` Candidate-Applicability Held-Evidence Bounded Reapplication

**Status:** **DRAFT — Owner Review pending.** Application only; no new evidence

**Scope:** Phase 1 — Data Foundation

**Reapplication date:** 2026-08-13

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact — bounded reapplication (DRAFT)** |
| Subject | Application of the committed candidate-applicability interpretation to **already-held, already-authorized evidence**, for `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` |
| Controlling interpretation | [`../decisions/phase1_primary_proxy_o4_candidate_applicability_interpretation_decision.md`](../decisions/phase1_primary_proxy_o4_candidate_applicability_interpretation_decision.md) — commit `fa2fd091…`, `AP-OD-01 … AP-OD-08` — **unchanged** |
| Rule applied | **AUTHORITATIVE PUBLISHER-SIDE DOCUMENTARY LINKAGE**, four conjunctive conditions, fail-closed, `AP-OD-04` traceability applied strictly, lowest-class rule applied |
| Evidence boundary | **HELD EVIDENCE ONLY.** No retrieval, no browsing, no URL test, no publisher contact |
| **Result** | **APPLICABILITY NOT ESTABLISHED FROM HELD EVIDENCE — all three candidates** |
| `O-4` | **OPEN** — **`O4-PARTIAL` ×3 unchanged.** No reconciliation performed |
| `HG-8` | **NOT EVALUABLE ×3** — not evaluated, not reapplied |
| `O4-M03` | Residual gap **characterized only**. **Not designed, not authorized, not executed** |
| Span | `OD-P15-06` floor → **`K1` = 2026-08-13** — unchanged |
| `P1-5` / `P1-6` / `H-1` | **OPEN (P-A, date NOT YET DERIVED)** / **OPEN** / **NOT ESTABLISHED** |
| Baseline / criteria freeze | **UNCHANGED** — `1e8bc85`; `AC-4` unchanged |
| Primary Proxy | **NOT APPROVED — P1-2 OPEN** · Stage G **OPEN** · Stage H **NOT BEGUN** · Phase 2 **BLOCKED** |

> **This is a held-evidence result.** It is **NOT** a statement that the required documentary evidence
> does not exist externally.

---

## 2. Evidence boundary used

Only material held and authorized **before** this task:

| Source | Items relied on |
| ------ | --------------- |
| Stage-C store | `D-01` NDX Index Methodology · `D-02` Calculation Manual – Equities & Commodities (20 May 2026) · `D-03` NDX Index Versions register · `D-04` Nasdaq Index Methodology Guide (31 Jul 2026) |
| Stage-D store | `E-04` / `E-05` / `E-06` — Index Overview pages for the three candidates, retained 2026-08-11 |
| `O-4` store | `O4-D01` NDX Methodology Change Log · `O4-D03` versions register (byte-identical to `D-03`) · `O4-D04` methodology (byte-identical to `D-01`) |
| Repository | The committed interpretation and the parent `O-4` authorization and Execution Plan |

**Nothing was retrieved. No store was modified. No secondary material was used.**

Local text extraction was performed on already-held PDFs for reading purposes only; no extracted
publisher text is reproduced here beyond the minimum documentary propositions required, consistent
with the Stage-F publication boundary.

---

## 3. The two authorities the chain must reach

`O-4` concerns the methodology chain. Held evidence shows it rests on **two distinct authorities**,
and applicability must be established for **both**:

| Authority | Document | Governs |
| --------- | -------- | ------- |
| **Construction** | `D-01` methodology, and its change record `O4-D01` | Eligibility, constituent selection, weighting, maintenance, calendar |
| **Calculation** | `D-02` Calculation Manual | Return version, dividend and withholding treatment, Index Currency, FX convention |

A candidate whose chain closes on one authority but not the other is **not established**.

---

## 4. Candidate documentary chain — `NDXJPY`

### 4.1 Construction authority

| # | Edge | Evidence ID | Publisher | Documentary proposition relied upon (paraphrased) | Class | Explicit? | Inference required? | Classification |
| - | ---- | ----------- | --------- | ------------------------------------------------- | ----- | --------- | ------------------- | -------------- |
| 1 | Candidate → its methodology document | `E-04` | Nasdaq | The publisher's own `NDXJPY` index page presents, under a "Related Links" heading, a link whose anchor text names it as **the `NDXJPY` methodology**, pointing to the NDX index-methodology document | PRIMARY | **Yes** | **No** | **DOCUMENTARY STATEMENT** |
| 2 | That document → self-identified authority | `D-01` / `O4-D04` | Nasdaq | The document identifies itself in its own heading as the **Nasdaq-100 Index NDX Index Methodology** | PRIMARY | **Yes** | **No** | **DOCUMENTARY STATEMENT** |
| 3 | Change record → same authority | `O4-D01` | Nasdaq | The change log identifies itself in its own heading as the **Nasdaq-100 Index NDX Methodology Change Log** | PRIMARY | **Yes** | **No** | **DOCUMENTARY STATEMENT** |

> **Construction-authority chain CLOSES for `NDXJPY`.** Three explicit publisher statements, no
> inference edge. Corroborated by a second independent observation of the same page at a different
> date, and by `D-03`, which lists `NDXJPY` as a version of NDX.

### 4.2 Calculation authority

| # | Edge | Evidence ID | Documentary proposition (paraphrased) | Class | Explicit? | Inference? | Classification |
| - | ---- | ----------- | -------------------------------------- | ----- | --------- | ---------- | -------------- |
| A | Candidate identified with a return version | `D-03` | The register lists `NDXJPY` by official name and symbol, with return version **price return**, currency **JPY**, base value date and base value, as a **version of NDX** | PRIMARY | **Yes** | **No** | **DOCUMENTARY STATEMENT** |
| B | Manual's scope over a class | `D-02` §1.2 | The Manual **shall apply to all Nasdaq Equity Indexes**, and covers price return, gross total return and net total return among the computed version types | PRIMARY | **Yes** | **No** | **DOCUMENTARY STATEMENT** |
| C | **Candidate ∈ that class** | — | *No held publisher document states that the JPY versions are **Nasdaq Equity Indexes**, or otherwise states that the Calculation Manual governs them* | — | **No** | **Yes** | **NOT ESTABLISHED** |

**Edge C examined and rejected as establishable from held evidence.** `D-03` establishes the
candidate is a Nasdaq **Index** and an NDX **version**; it does not state it is an **Equity** Index.
`D-04` contains **no** occurrence of "version" and **no** occurrence of "Equity Index", so it supplies
no general rule. The only occurrence of "Equity" on the retained overview pages is **site navigation
chrome**, not a per-index asset-class field — treating it as a class assertion about the candidate
would be **ANALYST INFERENCE** under `AP-OD-05`.

> **Calculation-authority chain DOES NOT CLOSE for `NDXJPY`.**

---

## 5. Candidate documentary chain — `XNDXJPY`

### 5.1 Construction authority

| # | Edge | Evidence ID | Documentary proposition (paraphrased) | Class | Explicit? | Inference? | Classification |
| - | ---- | ----------- | -------------------------------------- | ----- | --------- | ---------- | -------------- |
| 1 | Candidate → its methodology document | `E-05` | **The publisher's own `XNDXJPY` index page presents no methodology link and no versions link.** No document is named as this candidate's methodology | PRIMARY (negative) | — | — | **NOT ESTABLISHED** |
| 1′ | Alternative: general version-governance rule | `D-04` | *No held document states that a version of an index is governed by the parent index's methodology.* `D-04` contains **zero** occurrences of "version" | — | **No** | **Yes** | **NOT ESTABLISHED** |
| 2 | Candidate → version of NDX | `D-03` | The register lists `XNDXJPY` by name and symbol, return version **gross total return**, currency **JPY**, as a **version of NDX** | PRIMARY | **Yes** | **No** | **DOCUMENTARY STATEMENT** |

Edge 2 establishes *version membership*. It does **not** establish that the construction methodology
or its change record **governs** that version — that step is available only by inference.

> **Construction-authority chain DOES NOT CLOSE for `XNDXJPY`.**

### 5.2 Calculation authority

Edges A and B as at §4.2 — `D-03` records return version **gross total return**; `D-02` §1.2 and §2.3
cover that version type. **Edge C fails identically.**

> **Calculation-authority chain DOES NOT CLOSE for `XNDXJPY`.**

---

## 6. Candidate documentary chain — `XNDXNNRJPY`

### 6.1 Construction authority

Identical in structure to §5.1, on this candidate's own evidence: `E-06` presents **no methodology
link and no versions link**; `D-04` supplies no version-governance rule; `D-03` establishes version
membership only.

> **Construction-authority chain DOES NOT CLOSE for `XNDXNNRJPY`.**

### 6.2 Calculation authority

Edge A is **stronger here than for the other two**, and is recorded because it is genuine: `D-03`
describes this candidate's calculation method — reinvestment of 70% of cash dividends with a
deduction based on an indicative 30% tax rate — and `D-02` defines **Notional Net Total Return** in
substantively the same terms. Both are explicit publisher statements, and the correspondence is
documentary.

> **However, a correspondence of description is not a statement of scope.** `AP-OD-03` condition 2
> requires a publisher document to establish the Manual's scope **over a class the candidate is
> stated to belong to**. **Edge C fails identically.**

> **Calculation-authority chain DOES NOT CLOSE for `XNDXNNRJPY`.**

---

## 7. `AP-OD-03` condition check

| Condition | `NDXJPY` | `XNDXJPY` | `XNDXNNRJPY` |
| --------- | -------- | --------- | ------------ |
| **1.** Publisher document identifies the candidate and establishes its relationship to a parent index / family / version / return class / currency class | **SATISFIED** — `D-03`; and `E-04` names its methodology directly | **PARTIAL** — `D-03` version membership only | **PARTIAL** — `D-03` version membership only |
| **2.** Publisher document explicitly establishes the scope of the controlling methodology / calculation document over that class | **PARTIAL** — construction authority satisfied via `E-04`+`D-01`; **calculation authority NOT satisfied** | **NOT SATISFIED** for either authority | **NOT SATISFIED** for either authority |
| **3.** Linkage direct and mechanically traceable, without naming similarity, publisher identity alone, market convention, or analyst inference | **NOT SATISFIED** — edge C requires inference | **NOT SATISFIED** — edges 1 and C require inference | **NOT SATISFIED** — edges 1 and C require inference |
| **4.** No conflicting primary publisher evidence identified | **SATISFIED** | **SATISFIED** | **SATISFIED** |

**All four conditions are conjunctive and fail-closed (`AP-OD-03`). Condition 3 fails for every
candidate.**

---

## 8. Candidate-level results

| Candidate | Result |
| --------- | ------ |
| `NDXJPY` | **APPLICABILITY NOT ESTABLISHED FROM HELD EVIDENCE** |
| `XNDXJPY` | **APPLICABILITY NOT ESTABLISHED FROM HELD EVIDENCE** |
| `XNDXNNRJPY` | **APPLICABILITY NOT ESTABLISHED FROM HELD EVIDENCE** |

**No intermediate or favourable result was created.** The permitted vocabulary has two values and the
conservative one applies wherever any required edge is NOT ESTABLISHED or requires ANALYST INFERENCE.

> **Recorded so the difference is not lost:** `NDXJPY` came materially closer than the other two. Its
> **construction-authority chain closes** on three explicit publisher statements. It fails only on the
> calculation-authority class-membership edge, which fails for all three. `XNDXJPY` and
> `XNDXNNRJPY` fail on **two** independent edges. **This difference is reported, not collapsed**, and
> **no candidate inherits another's finding.**

---

## 9. Conflicts

**None.** No held primary publisher evidence conflicts on any edge examined. Condition 4 is satisfied
for all three candidates. No conflict is returned to Owner Review.

---

## 10. Residual gaps

### 10.1 Common missing edge — all three candidates

> **`GAP-A` — class membership for the calculation authority.** No held publisher document states
> that the JPY versions are **Nasdaq Equity Indexes**, or otherwise states that the Calculation
> Manual governs them. `D-02` states its scope over a class; no held document places the candidates
> in that class.

**What would close it:** a publisher statement that the Manual (or its return-version provisions)
governs these indexes or a class they are stated to belong to; or a publisher statement classifying
the JPY versions as Nasdaq Equity Indexes.

### 10.2 Candidate-specific missing edge — `XNDXJPY` and `XNDXNNRJPY` only

> **`GAP-B` — construction-authority governance.** No held publisher document names a governing
> methodology for these two candidates, and no held document states the general rule that a version
> is governed by its parent index's methodology.

**What would close it:** a publisher statement naming the governing methodology for each candidate —
the analogue of what `E-04` provides for `NDXJPY` — or a publisher statement of the general
version-governance rule, which would close it for both at once and would also strengthen `NDXJPY`.

**`NDXJPY` does not carry `GAP-B`.**

---

## 11. `O4-M03` necessity finding

Case **(C)** under the authorization: **applicability is established for none of the three.**

> **A residual candidate-applicability research gap IS demonstrated by this reapplication**, and it is
> **precisely characterized**: `GAP-A` for all three; `GAP-B` for `XNDXJPY` and `XNDXNNRJPY`.

**Only the residual gap is characterized here. `O4-M03` is not designed, not authorized, and not
executed. No `M03-*` state is decided.**

---

## 12. What this reapplication does NOT establish or change

- **`O4-PARTIAL` ×3 is unchanged.** No reconciliation was performed; `M01` and `M02` were not
  reassessed.
- **`HG-8` was not evaluated or reapplied** and remains **NOT EVALUABLE ×3**. Candidate applicability
  is an `O-4` documentary finding only and is **not** normalized into PASS or FAIL.
- **No statement that the required documentary evidence does not exist externally.** This is a
  held-evidence result about the search boundary applied, not about the world.
- **`H-1`** — not established, not inferred. Methodology governance says nothing about live status.
- **`P1-5`** — no date derived. **`P1-6`** — not selected. **`K1`** — unchanged.
- **`OJ-1`, `OJ-6`** — not exercised. **No Primary Proxy selected.**
- **C-2A** — outside this task; untouched.
- **No candidate was ranked, scored, or preferred.** No performance quantity was computed;
  `ND-1 … ND-7` were not used.

---

## 13. Anti-circularity

- **`AC-1`** — the interpretation was committed **before** this application; semantics were not
  fitted to a result already seen.
- **`AC-2`** — no performance quantity computed. **`AC-3`** — no `ND-n` material used.
- **`AC-4`** — the three candidates were carried **identically and separately**; the same edges were
  tested for each; the asymmetric outcome reflects an asymmetric evidence base, **not** differential
  effort, and no candidate inherits another's finding.
- **`AC-6`** — point-in-time discipline untouched.
- **`AC-8`** — no scoring, weighting, or ranking.
- **`SC-18`** — not triggered; no frozen text required change. **`SC-19`** — no prior finding
  narrowed, withdrawn, or downgraded; the executed `O-4` record stands exactly as preserved.
- **Direction of the result:** this reapplication **did not** advance any candidate toward
  qualification. The strict reading of `AP-OD-04` was applied even where the bridging step would have
  been intuitively obvious — the `NDXJPY` calculation edge in particular.

---

## 14. Preserved governance state

`O-4` **OPEN**, **`O4-PARTIAL` ×3** · `HG-8` **NOT EVALUABLE ×3**, not reapplied · `HG-6` / `HG-9` /
`HG-12` **PASS ×3** with recorded limitations and conditions · `HG-11` **BOUNDED QUALIFICATION —
UNCLEAR, NOT POSITIVELY RESTRICTED**, not PASS, non-eliminating, carried to `OJ-6` · `H-1` **NOT
ESTABLISHED** · `P1-9` **PARTIAL** · `K1` **2026-08-13** · `P1-5` **OPEN**, **P-A**, date **NOT YET
DERIVED** · `P1-6` **OPEN** · C-1 ×3 **QUALIFICATION INCOMPLETE** · C-2A **unchanged** · `OJ-1` **NOT
REACHED — DEFERRED** · `OJ-6` **unexercised** · **no Primary Proxy approved**, `P1-2` **OPEN** ·
Frozen Baseline and criteria freeze **unchanged**, `AC-4` unchanged · Stage G **OPEN** · Stage H
**NOT BEGUN** · Phase 2 **BLOCKED**.

---

**End of DRAFT Evidence Artifact. Held evidence only. Result: **APPLICABILITY NOT ESTABLISHED FROM
HELD EVIDENCE** for `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`. `NDXJPY`'s construction-authority chain
closes on three explicit publisher statements; its calculation-authority chain does not.
`XNDXJPY` and `XNDXNNRJPY` fail on two independent edges. Residual gaps: **`GAP-A`** (all three),
**`GAP-B`** (two). No conflict. `O4-M03`: residual gap **characterized only** — not designed, not
authorized, not executed. **`O4-PARTIAL` ×3 unchanged. `HG-8` NOT EVALUABLE ×3, not reapplied.**
`K1` = 2026-08-13. `P1-5` **OPEN**; `P1-6` **OPEN**. Primary Proxy: **NOT APPROVED — P1-2 OPEN**.
Phase 2: **BLOCKED**.**
