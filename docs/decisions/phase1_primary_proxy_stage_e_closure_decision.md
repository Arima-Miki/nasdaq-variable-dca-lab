# Phase 1 Primary Proxy Qualification — Stage E Closure Owner Decision

**Status:** APPROVED

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Closure of Stage E; disposition of Q-B and `OJ-3`; status of `O-3`; ratification of Stage-E external storage; routing of `N-4` |
| Decision status | **APPROVED** |
| Supporting evidence | [`../evidence/phase1_primary_proxy_stage_e_composition_currency_evidence.md`](../evidence/phase1_primary_proxy_stage_e_composition_currency_evidence.md) |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Prior stage closures | [`phase1_primary_proxy_stage_c_closure_decision.md`](phase1_primary_proxy_stage_c_closure_decision.md); [`phase1_primary_proxy_stage_d_closure_decision.md`](phase1_primary_proxy_stage_d_closure_decision.md) |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion amended, added, renumbered, or re-weighted** |
| OD-11 | **UNCHANGED.** This decision records that a Phase-1 *documentation duty* was discharged; it does not alter OD-11 |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage F | **NOT AUTHORIZED** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It closes one stage of an authorized Phase-1 study and
records the determinations arising from its evidence.

> **It is NOT a modification of the Phase-0 Baseline.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and it does not
  create, amend, or supersede any of them — **including OD-11 and OD-12**.
- The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this
  decision and that specification could be read as differing, **the specification governs Baseline
  behavior**.
- It does **not** amend the frozen qualification criteria. `HG-1 … HG-13`, `CT-1 … CT-9`,
  `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged, and `1e8bc85` remains the
  criteria-freeze boundary.
- This decision contains **no Baseline results, no performance claims, and no historical values.**

---

## 2. Decisions

### 2.1 E-8 — Q-B and `OJ-3` disposition

**APPROVED.**

The factual Stage-E finding stands: **Q-B = UNDISCLOSED / NOT ESTABLISHED.** The bounded §8.3
investigation is accepted as **complete**, and S.3 is not to be expanded beyond the already
authorized evidence classes.

> **The Owner determines that Q-B is NON-DISCRIMINATING among the Primary Proxy candidates for the
> present qualification study.**

**Reason.** The Primary Proxy is a research proxy for the Frozen Baseline. Its role is **not** to
reconstruct, reverse-engineer, or guess an undisclosed Nissay internal benchmark convention.
Nissay's undisclosed meaning of 「NASDAQ100指数（配当込み、円換算ベース）」 therefore establishes no
principled basis for selecting among `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`.

Accordingly:

> **`OJ-3` = NOT REACHED** for the current evidence state.

**Decision history is preserved, not erased.** The Stage-E execution report provisionally
classified the unresolved Q-B as *requires Owner judgment* and reported **"`OJ-3` REACHED — NOT
MADE"**, while simultaneously recording the competing reading and referring the question to the
Owner. That provisional statement is **superseded** by the Owner disposition:

> **"Q-B NON-DISCRIMINATING — `OJ-3` NOT REACHED."**

This is a **governance disposition of the ambiguity**. It does **not** modify the factual finding
that Q-B is UNDISCLOSED / NOT ESTABLISHED. It does **not** select a C-1 return version. It does
**not** establish that all three return versions are equally suitable.

Any eventual Primary Proxy return-version decision must arise from the frozen qualification
framework and the Primary Proxy's role as a Baseline research proxy.

**Binding inference prohibitions.** Nissay's undisclosed convention must **not** be inferred from:
empirical closeness; fund performance; tracking difference; product naming; `ND-4`; relative
plausibility; or investor tax assumptions.

### 2.2 E-9 — Stage-E external storage

**APPROVED.** The Stage-E persistent external research-material location is ratified, with its
existing primary documents, provenance index, and checksum structure accepted as Stage-E external
research material.

It remains **structurally outside the Git worktree** and is not committed. This approval is
**Stage-E-specific** and does **not** establish a universal repository-wide research-storage
architecture.

### 2.3 E-10 — Durable Stage-E closure artifact

**APPROVED.** The minimum durable package is a Stage-E Evidence Artifact and this Owner Decision.
Both are **additive**.

No prior Stage-C or Stage-D evidence or decision was rewritten merely because Stage E adds
precision. Temporal provenance is preserved throughout, and where a Stage-E provisional
interpretation was later resolved by Owner Review, the evidence artifact records **the original
evidence result, the Owner disposition, and the resulting authoritative governance state**.

### 2.4 E-11 — `N-4` confidentiality marking

**APPROVED.** `N-4` is carried forward to **Stage F / `HG-11`**.

Source `F-02` carries a confidentiality / distribution marking despite having been retrievable from
a public URL. The Stage-E fail-closed treatment is accepted:

- `F-02` was **not relied upon** for any Stage-E qualification finding;
- its content is **not to be reproduced** in repository evidence;
- **public accessibility is not evidence of redistribution permission**;
- **no inference** is to be made that the marking is ineffective or irrelevant.

> **`N-4` = OPEN / FAIL-CLOSED FOR PUBLICATION** until Stage F determines the applicable
> publication / licensing consequence under `HG-11` / `P1-8`.

**This is not a finding that retrieval was unlawful, and no such claim is made.**

### 2.5 E-12 — `O-3` status

**APPROVED.** `O-3` is recorded as:

> **CHARACTERIZED, NOT RESOLVED.**

Authoritative publisher evidence establishes that a financial-reporting NAV exists, that a
shareholder-transaction NAV exists, that the two may differ, and that returns calculated from the
two bases may differ. This **materially characterizes** the ambiguity.

The evidence does **not** establish which NAV basis governs the published QQQ NAV-return series
relevant to C-2A. Therefore **`O-3` remains OPEN**.

Neither basis may be chosen. `HG-2` may **not** be declared satisfied from this finding. `HG-5` may
**not** be declared satisfied from this finding. No C-2A series may be constructed. No basis may be
inferred from the issuer performance page's silence — **the documented absence of a published
NAV-return-basis definition is recordable as evidence, but absence is not resolution.**

---

## 3. Stage-E closure determination

**Stage E is accepted as COMPLETE within the authorized documentary boundary.**

The Stage-E findings are **evidence results**. They must not be reinterpreted to preserve or
eliminate any candidate.

### 3.1 C-1 — `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY`

| Item | State |
| ---- | ----- |
| `HG-3` documentary evidence | **COMPLETE** — three distinct return versions: **PRICE RETURN**, **GROSS TOTAL RETURN**, **NOTIONAL NET TOTAL RETURN**; ordinary-dividend, special-dividend, reinvestment and withholding distinctions documented |
| `HG-4` documentary evidence | **COMPLETE** — publisher-governed embedded FX: WM / Reuters spot, 16:00:00 UK closing spot for EOD calculation, current-index-day alignment, per-Index-Security conversion, no NDX-methodology override identified |
| `HG-10` documentary evidence | **COMPLETE** — **no fund-level management expense is embedded** in any index candidate |
| `O-2` | **RESOLVED** |
| Stage-D limitations | **UNCHANGED** — `SC-6` and `H-1` stand as recorded at Stage D |
| Return version | **NONE SELECTED** |

**Binding characterizations.** The observation-time asymmetry between the FX leg and the index
close is a **documented characteristic, not an evidence failure**, and must not be converted into a
performance judgment. Embedded FX must **not** be described as an expense. `XNDXNNRJPY`'s notional
withholding deduction is a **return-composition component, not a fund management fee**. The three
candidates must **not** be collapsed.

**On `O-2`.** The Nasdaq withholding-rates document governs **NTR** indexes. `XNDXNNRJPY` is
**NNTR**, and its flat notional 30% withholding basis is documented directly by the Calculation
Manual. No current C-1 candidate depends on Appendix A. **`XNDXNNRJPY`'s 30% must not be derived
from the United States entry in Appendix A — the numerical coincidence is not the evidentiary
basis.**

### 3.2 C-2A

| Item | State |
| ---- | ----- |
| `HG-3` documentary evidence | **COMPLETE** — NAV total return: beginning-period NAV, reinvestment of dividends and distributions at NAV, ending-period NAV |
| `HG-10` documentary evidence | **COMPLETE** — two-regime embedded-cost structure documented |
| `O-3` | **CHARACTERIZED, NOT RESOLVED — OPEN** |
| External FX leg | **UNRESOLVED-BY-DESIGN** |
| `HG-4` | **NOT YET EVALUABLE** for the external FX leg |
| JPY series | **NONE CONSTRUCTED** |

**Binding characterization.** The Trust itself provides **no dividend reinvestment service**. The
reinvestment convention is therefore **part of the return calculation**, and is **not** evidence
that the Fund operationally reinvests shareholder distributions.

**Preserved expense facts.** The UIT-era expense structure and its **0.20%** ratio; the
post-reclassification **0.18%** unitary management fee; **NAV-embedded transaction costs that are
excluded from the reported expense ratio**; the existence and stated duration of the documented fee
waiver; and the publisher statement that pre-reclassification returns reflect operation as a UIT
with differing expenses.

**Prohibited.** Inferring tracking difference; equating any stated expense ratio with tracking
difference; creating an expense-adjusted series; building a cost model; deciding `HG-8`.

**A future C-2A construction** would require, at minimum: an authoritative USD/JPY source; an
observation time; observation-date alignment; source qualification; licensing / use-right review
where applicable; and **separate Owner authorization**. No FX provider, rate, fixing time, or
alignment convention may be selected; prior FX research may **not** be reused to make a selection;
no JPY series may be constructed.

### 3.3 Cross-cutting state

| Item | State |
| ---- | ----- |
| Q-B | **UNDISCLOSED / NOT ESTABLISHED** |
| §8.2 Owner disposition | **Q-B NON-DISCRIMINATING** |
| `OJ-3` | **NOT REACHED** |
| `OJ-4` | **NOT RESOLVED** — the documented governance consequence stands: promoting C-2 to Primary Proxy would consume the independent cross-validation role currently assigned to C-2 under the three-layer concept |
| `N-2` | Expense facts **ESTABLISHED**; continuity consequence **UNRESOLVED** |
| `N-3` | Consultation evidence documents no return-composition, dividend, withholding, or currency-treatment change; the final publisher-side decision document remains unavailable, so the **provenance gap remains OPEN**. The consultation finding must **not** be generalized into a claim about the final adopted change |
| `N-4` | **OPEN / FAIL-CLOSED FOR PUBLICATION** — handoff to Stage F / `HG-11` |
| OD-11 | Phase-1 **documentation duty discharged** for the Stage-E candidates; OD-11 itself **unchanged**; future `P1-4` cost-model work **not** completed |
| `HG-8` | **No candidate passes or fails at Stage E.** Final gate evaluation remains Stage G |
| Primary Proxy | **NOT APPROVED** |

### 3.4 §9 route-obligation finding

**Preserved:** C-2A presently carries more researcher-selected assumptions and unresolved
construction obligations than C-1, together with the concrete assumption inventory supporting it.

This is an **obligation / reproducibility finding only**. It is **not** a performance ranking,
**not** a candidate score, **not** a Primary Proxy selection, **not** proof that C-1 is more
accurate, and **not** proof that C-2A is unsuitable.

### 3.5 Calculation boundary

Stage E remained **documentary**. No historical observation-value analysis occurred. The only
arithmetic was the publisher-parameter consistency check **70 + 30 = 100** for the NNTR
reinvestment / notional withholding description, recorded **only** as a documentary consistency
check and **not** as empirical analysis.

---

## 4. What this decision does NOT approve

- It does **not** approve a Primary Proxy — P1-2 remains **OPEN**.
- It does **not** pass or fail any hard gate for any candidate.
- It does **not** select a C-1 return version, and does **not** establish that the three return
  versions are equally suitable.
- It does **not** resolve `O-3`, and does **not** choose a NAV basis.
- It does **not** declare `HG-2`, `HG-5`, or `HG-8` satisfied.
- It does **not** select an FX source or convention, and does **not** authorize any C-2 synthetic
  JPY construction.
- It does **not** resolve `OJ-1`, `OJ-4`, `O-4`, `O-5`, `O-6`, or `O-7`.
- It does **not** close the `N-3` publisher-side provenance gap, and does **not** determine `N-4`.
- It does **not** decide any licensing or redistribution question.
- It does **not** amend OD-11, OD-12, any Owner Decision, or any frozen criterion.
- It does **not** authorize Stage F or Stage G.
- It does **not** unblock Phase 2.

---

## 5. Anti-circularity confirmation

- **No performance quantity was computed** at any point in Stage E. The only arithmetic was on
  publisher-stated methodology parameters.
- **`ND-1 … ND-7` were not used** in reaching any part of this decision, and **`ND-4` was
  specifically not used** to infer Nissay's convention.
- The Q-B disposition rests on the **role of the Primary Proxy under the frozen framework** — a
  governance ground. It was not informed by any candidate's historical behaviour, and no comparison
  between candidates was made.
- `AC-1 … AC-8` were maintained; the three C-1 series were carried identically throughout.
- No candidate is described as "the benchmark", "benchmark-equivalent", or "best fit".

---

## 6. Publication and external-material boundary

**No historical value — observation, incidental, NAV, net-asset, or distribution — is recorded in
this repository.** Publisher-stated fee and expense parameters are recorded as documentary facts
required to discharge `HG-10` / OD-11, and are not performance values.

No publisher document, provenance index, checksum file, extracted text, decrypted copy, scratch
extraction tooling, or `F-02` content enters Git. All source material is retained **structurally
outside** the repository; an ignored repository directory is not an acceptable substitute.

Redistribution terms remain **unassessed** for every source used at Stages C, D and E. Licensing is
Stage-F work, so fail-closed treatment applies and nothing is cleared for republication.

---

## 7. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched, **including OD-11 and
  OD-12**.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **No prior evidence artifact or decision was rewritten.** Stage-C and Stage-D findings stand;
  this closure is additive, and the Stage-E decision history is preserved.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked or selected. No gate was evaluated.**
- **No C-1 return version was selected.**
- **No FX source or convention was selected, and no C-2A JPY series was constructed.**
- **No raw dataset, publisher document, or external provenance material is committed to this
  repository.**
- **Stage F has not begun and is NOT AUTHORIZED. Stage G has not begun.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Stage E: CLOSED. Q-B: UNDISCLOSED / NOT ESTABLISHED —
NON-DISCRIMINATING. `OJ-3`: NOT REACHED. `O-3`: CHARACTERIZED, NOT RESOLVED — OPEN. C-2A `HG-4`:
NOT YET EVALUABLE. `N-4`: OPEN / FAIL-CLOSED. Primary Proxy: NOT APPROVED — P1-2 remains OPEN.
Phase 2: BLOCKED.**
