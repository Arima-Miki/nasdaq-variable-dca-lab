# Phase 1 Primary Proxy Qualification — `O-4` Candidate-Applicability Documentary-Linkage Interpretation

**Status:** **APPROVED — interpretation recorded.** Records semantics only

**Scope:** Phase 1 — Data Foundation

**Decision date:** **2026-08-13** — the date of explicit Owner approval

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision — evidentiary interpretation** |
| Decision status | **APPROVED** |
| Subject | The controlling meaning of the `O-4` candidate-applicability proof standard — the requirement that applicability be established *"from scope statements"* |
| Owner dispositions | `AP-OD-01` … `AP-OD-08` |
| Adopted rule | **AUTHORITATIVE PUBLISHER-SIDE DOCUMENTARY LINKAGE** |
| Interpreted provisions | Parent `O-4` Execution Plan §10.1, §17.1 condition 4, §5, §9.7, §14 — [`../research/phase1_primary_proxy_o4_methodology_chain_execution_plan.md`](../research/phase1_primary_proxy_o4_methodology_chain_execution_plan.md), commit `7988d06c…` — **unchanged; no wording deleted or rewritten** |
| Parent authorization | [`…o4_bounded_research_authorization_decision.md`](phase1_primary_proxy_o4_bounded_research_authorization_decision.md) — commit `b0aaab99…` — **unchanged** |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` — **unchanged** |
| Baseline status | **Phase 0 Frozen — unchanged** |
| Criteria-freeze status | **UNCHANGED — no criterion added, removed, weakened, widened, renumbered, or re-weighted** |
| `AC-4` | **UNCHANGED** |
| `O4-M03` | **Option C accepted in principle**; **not designed, not executed, not decided** |
| Current `O-4` result | **`O4-PARTIAL` ×3** — unchanged |
| `HG-8` | **NOT EVALUABLE ×3** — semantics unchanged; not reapplied |
| Span | `OD-P15-06` floor → **`K1` = 2026-08-13** — unchanged |
| Primary Proxy | **NOT APPROVED — P1-2 OPEN** · Stage G **OPEN** · Stage H **NOT BEGUN** · Phase 2 **BLOCKED** |

### Artifact role and precedence

A **Phase-1 Owner Decision interpreting an existing documentary proof standard.** It is not evidence,
not a research result, not a gate result, and not a stage result.

> **It is NOT a modification of the Phase-0 Baseline, NOT a modification of the frozen qualification
> criteria, and NOT the creation of any new criterion, hard gate, comparative criterion, or stop
> condition.**

`HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6`, `SC-1 … SC-20` and `AC-1 … AC-8` are
unchanged; `1e8bc85` remains the criteria-freeze boundary. Where this decision and any higher
authority could be read as differing, **the higher authority governs**.

This decision contains **no Baseline result, no performance claim, no historical value, no research
finding, and no candidate-specific applicability determination.**

---

## 2. Why the interpretation is needed

The executed `O-4` research recorded candidate applicability as **hypothesised** for the index
construction methodology and its change record, because neither document names the JPY versions,
while recording it as **established** for the version register and the calculation manual, which do
carry statements reaching the candidates.

The parent Execution Plan requires applicability to be established *"from scope statements"* and,
at §10.1, *"from the document's **own** scope statement. Never from family membership, naming
similarity, or publisher identity."*

Read as requiring a **single-document literal scope sentence**, that standard would treat a chain of
explicit publisher statements as insufficient. Read functionally, it would not. **The question is
semantic and cannot be resolved by any amount of new evidence**, which is why it is settled here,
before any follow-on research runs.

---

## 3. The three-way distinction — mandatory

`AP-OD-01`. Every applicability finding must be classified as exactly one of the following, and the
classification must be recorded:

| # | Class | Definition | May support applicability? |
| - | ----- | ---------- | -------------------------- |
| **1** | **DOCUMENTARY STATEMENT** | An authoritative publisher document states, in its own text, that it governs — or that a named methodology or calculation document governs — the candidate, a class the candidate belongs to, or the candidate's version relationship | **YES** |
| **2** | **DOCUMENTARY LINKAGE** | Two or more authoritative publisher documents, each making an explicit statement, which together compose a direct and mechanically traceable chain from candidate to controlling document — every edge documentary and explicit | **YES**, under `AP-OD-02` |
| **3** | **ANALYST INFERENCE** | Any step supplied by the researcher rather than by publisher text — similarity, plausibility, convention, expectation, or reasoning that a publisher "must have meant" | **NO — never** |

> **Only classes 1 and 2 may support candidate applicability. Class 3 may not, in any degree, for any
> candidate, at any interval.**

A finding that mixes classes takes the **lowest** class present. One class-3 edge makes the whole
chain class 3.

---

## 4. The adopted rule

`AP-OD-02`. **AUTHORITATIVE PUBLISHER-SIDE DOCUMENTARY LINKAGE.**

> Candidate applicability does **NOT** require every methodology document, change log, or calculation
> document individually to name every candidate.

Applicability **may** be established through an explicit, publisher-side documentary linkage where
**all four** of the following hold:

1. **an authoritative publisher document identifies the candidate** and explicitly establishes its
   relationship to a parent index, index family, version, return version, currency version, or other
   governance relationship relevant to the methodology; **AND**
2. **an authoritative publisher document explicitly establishes the scope** of the controlling
   methodology or calculation document over that parent index, family, version class, or governance
   class; **AND**
3. **the linkage between those documentary statements is direct and mechanically traceable**, without
   relying on naming similarity, publisher identity alone, market convention, or analyst inference;
   **AND**
4. **no conflicting primary publisher evidence has been identified.**

`AP-OD-03`. **Conjunctive and fail-closed.** All four conditions must hold. If any is unsatisfied,
applicability is **NOT established** by linkage, and the residue is recorded as a gap. Partial
satisfaction establishes nothing.

### 4.1 What the rule permits — shape only

A candidate-specific applicability finding **may** be supported by several publisher-issued documents
read together. Conceptually:

```
candidate
  → publisher-defined version relationship        (documentary statement)
  → publisher-defined parent index / governed class (documentary statement)
  → publisher-defined methodology or calculation scope (documentary statement)
```

Applicability may be established **where every edge in that chain is documentary and explicit**.

> **This example establishes applicability for NO actual candidate.** It states the permitted *shape*
> of an argument. **This artifact records semantics only** and makes no candidate-specific
> determination for `NDXJPY`, `XNDXJPY`, or `XNDXNNRJPY`.

### 4.2 Traceability requirement

`AP-OD-04`. A linkage is **mechanically traceable** only if each edge can be cited to a specific
authoritative publisher document and the statement within it, such that an independent reader could
reproduce the chain from those citations alone, without supplying any reasoning of their own.

**Every edge must be recorded individually**, with its document, its class under `AP-OD-01`, and its
candidate specificity. A linkage asserted as a whole, without its edges enumerated, is **not
established**.

---

## 5. What remains prohibited

`AP-OD-05`. The following are **insufficient**, singly or in combination, and remain so:

- shared **publisher identity** alone;
- **naming similarity**;
- **ticker similarity**;
- **analyst inference**;
- assumed **index-family membership**;
- **market convention**;
- **economic similarity**;
- **methodology similarity**;
- any **undocumented assumption that a JPY version inherits NDX rules**;
- a **secondary source** asserting applicability without return to publisher-side evidence.

> **No inference rule may be created from publisher identity.** That a single publisher issues two
> documents establishes nothing about the scope of either.

> **`AC-4` is not weakened.** Symmetric candidate handling is unchanged: this rule applies identically
> to all three C-1 candidates, and applicability must be established **per candidate**. A linkage
> established for one candidate establishes nothing for another.

---

## 6. Meaning of *"from scope statements"*

`AP-OD-06`. The existing phrase is interpreted **functionally**, not as requiring a single-document
literal scope sentence.

> It means that applicability must be established from **explicit publisher-side documentary
> statements of scope and governance**. Those statements **may reside in more than one authoritative
> publisher document**, provided the linkage is **direct, explicit, reproducible and
> candidate-specific**.

**This interpretation does not delete or rewrite the existing wording.** The Execution Plan's text
stands unamended, including its prohibitions at §10.1, which are preserved in full at §5 above.

### 6.1 Coexistence check — performed, no conflict found

| Provision | Status |
| --------- | ------ |
| Execution Plan §10.1, §17.1 c.4, §5, §9.7, §14 | **Unchanged.** Interpreted, not amended |
| The §10.1 word *"own"* | The point of tension, and the reason this decision exists. Resolved **functionally**: the guard §10.1 actually imposes is against *family membership, naming similarity and publisher identity* — **all three preserved verbatim** — not against a chain of explicit publisher statements |
| Execution Plan's amendability | The plan records at §1.1 that it is **"deliberately not part of any freeze and must remain amendable by Owner Review without touching frozen text."** Interpreting it therefore requires no frozen change |
| `AC-4` (frozen) | **Unchanged.** It governs symmetric candidate handling, not the documentary proof standard |
| Frozen Baseline; `1e8bc85` | **Unchanged.** Neither contains the interpreted phrase |
| `SC-18` | **Considered and NOT triggered.** No normative frozen text required change |

> **The tension is recorded rather than papered over:** a strict single-document reading of *"own"*
> was available, and the Owner has adopted the functional reading. The prohibitions that gave §10.1
> its force are carried through unchanged.

---

## 7. Relationship to `O4-M03`

`AP-OD-07`. Recorded:

- **Option C is accepted in principle** — `O4-M03` Candidate Applicability will be used **if a
  residual research question remains necessary** after this interpretation is applied.
- **`M03` remains a distinct scope-axis question**, orthogonal to `M01` (temporal coverage of the
  change record) and `M02` (temporal version chain of the calculation document).
- **No external `M03` research is authorized.** None is designed, executed, or decided here.
- **Before any `M03` research is designed or executed**, the already-held authorized evidence must be
  **reapplied under this interpretation**.
- **If that reapplication fully establishes candidate applicability**, `M03` may be resolved
  **without new external research**.
- **If a residual gap remains**, an explicit `M03` design may then address **only that residual gap**.

> **The reapplication is NOT performed in this task, and no `M03-*` state is decided.**

---

## 8. Anti-result-seeking

`AP-OD-08`. **This interpretation is fixed before any `M01`, `M02` or `M03` follow-on research is
executed.** It therefore fixes the evidentiary rule **before** follow-on results are observed —
the `AC-1` posture applied throughout this study.

> **It must not later be widened or narrowed merely because the resulting evidence proves favourable
> or unfavourable.** Any later need to change it **returns to Owner Review** under `SC-18`.

**Named rules preserved:** `AC-1` — rule fixed before evidence. `AC-2` — no performance quantity
computed. `AC-3` — `ND-1 … ND-7` not used. **`AC-4` — unchanged; symmetric handling preserved and
per-candidate establishment required.** `AC-5` — no `P1-5` date derived. `AC-6` — point-in-time
discipline untouched. `AC-8` — no scoring. **Invariant 17** — no Baseline parameter set. **`SC-17`** —
no proxy selected on performance. **`SC-18`** — not triggered; see §6.1. **`SC-19`** — no prior
finding narrowed, withdrawn or downgraded; the executed `O-4` record stands exactly as preserved.

**A note on direction, recorded for audit:** this interpretation could make applicability *easier* to
establish than a strict single-document reading would. That is why it is fixed **now**, before any
follow-on evidence exists, and why `AP-OD-03` makes the rule conjunctive and fail-closed,
`AP-OD-04` requires every edge to be enumerated, and `AP-OD-01` forbids any analyst-inference edge.
**The rule is permissive about *where* statements may reside and strict about *what counts as* a
statement.**

---

## 9. What this decision does NOT do

- It does **not** determine applicability for `NDXJPY`, `XNDXJPY` or `XNDXNNRJPY`.
- It does **not** reapply the held evidence under the new interpretation.
- It does **not** design, authorize, execute, or decide **`O4-M03`**.
- It does **not** change **`O4-PARTIAL` ×3**.
- It does **not** evaluate or reapply **`HG-8`**, and does not change `HG-8` semantics.
- It does **not** alter the `O-4` threshold at Execution Plan §17.1.
- It does **not** derive **`P1-5`**, select **`P1-6`**, or change **`K1`**.
- It does **not** exercise `OJ-1` or `OJ-6`, approve a Primary Proxy, or resolve `P1-2`.
- It does **not** modify the `M01`/`M02` follow-on drafts, any existing artifact, or any evidence
  store.
- It does **not** begin Stage H or unblock Phase 2.

---

## 10. Preserved governance state

| Item | State |
| ---- | ----- |
| **Frozen Phase-0 Baseline** | **UNCHANGED** — OD-01 … OD-14 untouched |
| **Criteria freeze** | **UNCHANGED** — `1e8bc85`; **`AC-4` unchanged** |
| `K1` | **2026-08-13** — unchanged, immutable |
| `P1-5` | **OPEN** — principle **P-A** selected; date **NOT YET DERIVED** |
| `P1-6` | **OPEN** |
| `H-1` | **NOT ESTABLISHED** |
| `O-4` | **OPEN** — **`O4-PARTIAL` ×3 unchanged** |
| `O4-M03` | Option C accepted in principle; **not designed, authorized, executed or decided** |
| `HG-8`, C-1 ×3 | **NOT EVALUABLE** — semantics unchanged; **not reapplied** |
| `HG-6` / `HG-9` / `HG-12`, C-1 ×3 | **PASS**, with recorded limitations and conditions |
| `HG-11`, C-1 ×3 | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; not PASS; non-eliminating; carried to `OJ-6` |
| `P1-9` | **PARTIAL** |
| C-1 classification | **QUALIFICATION INCOMPLETE** ×3 |
| C-2A | **UNCHANGED** |
| `OJ-1` | **NOT REACHED — DEFERRED** · `OJ-6` **unexercised** |
| `P1-2` | **OPEN** — **no Primary Proxy approved** |
| Stage G | **OPEN** · Stage H **NOT BEGUN** · Phase 2 **BLOCKED** |

---

## 11. Confirmations

- **Frozen Phase-0 Baseline unchanged. Criteria freeze unchanged. `AC-4` unchanged.**
- **No new hard gate, comparative criterion, or stop condition. No stop condition changed.**
- **The `O-4` threshold and `HG-8` semantics are unchanged.**
- **The parent `O-4` authorization and Execution Plan are unchanged** — interpreted, with **no wording
  deleted or rewritten**.
- **Coexistence check performed; no conflict found; `SC-18` not triggered.**
- **`O4-PARTIAL` ×3 preserved. `HG-8` NOT EVALUABLE ×3, not reapplied. `H-1` NOT ESTABLISHED.**
- **`K1` = 2026-08-13 unchanged. `P1-5` OPEN (P-A, date NOT YET DERIVED). `P1-6` OPEN.**
- **No candidate-specific applicability determination is made.**
- **No external access was performed**, no document retrieved, no evidence store created or modified,
  no empirical quantity computed, and `ND-1 … ND-7` were not used.
- **Neither `M01`/`M02` follow-on draft was modified.**

---

**End of Phase-1 Owner Decision. `AP-OD-01` … `AP-OD-08`. Rule: **AUTHORITATIVE PUBLISHER-SIDE
DOCUMENTARY LINKAGE** — four conjunctive conditions, fail-closed, every edge enumerated. Three-way
classification mandatory: **documentary statement** and **documentary linkage** may support
applicability; **analyst inference** never may. *"From scope statements"* read **functionally**, with
§10.1's prohibitions preserved verbatim and no wording rewritten. `AC-4` unchanged. `O4-M03`:
accepted in principle, **not designed, authorized, executed or decided**; reapplication of held
evidence deferred. `O4-PARTIAL` ×3 unchanged. `HG-8`: **NOT EVALUABLE** ×3, semantics unchanged, not
reapplied. `K1` = 2026-08-13. `P1-5` **OPEN**; `P1-6` **OPEN**. Primary Proxy: **NOT APPROVED — P1-2
OPEN**. Phase 2: **BLOCKED**.**
