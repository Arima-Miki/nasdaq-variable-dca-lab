# Phase 1 Primary Proxy Qualification — Stage F Closure Owner Decision

**Status:** APPROVED

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-12

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Closure of Stage F; resolution of `OJ-5`; disposition of the existing verbatim publisher quotations; ratification of Stage-F external storage; scope of the Broadridge delivery channel |
| Decision status | **APPROVED** |
| Supporting evidence | [`../evidence/phase1_primary_proxy_stage_f_licensing_reproducibility_evidence.md`](../evidence/phase1_primary_proxy_stage_f_licensing_reproducibility_evidence.md) |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at `1e8bc85` |
| Prior stage closures | [Stage C](phase1_primary_proxy_stage_c_closure_decision.md); [Stage D](phase1_primary_proxy_stage_d_closure_decision.md); [Stage E](phase1_primary_proxy_stage_e_closure_decision.md) |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion amended, added, renumbered, or re-weighted** |
| `OJ-5` | **RESOLVED** — bounded research-use disposition (§2.3) |
| `P1-8` | **PARTIAL** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage G | **NOT AUTHORIZED** |
| Stage H | **NOT AUTHORIZED** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It closes one stage of an authorized Phase-1 study and records
the determinations arising from its evidence.

> **It is NOT a modification of the Phase-0 Baseline.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and does not create,
  amend, or supersede any of them.
- The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this
  decision and that specification could be read as differing, **the specification governs Baseline
  behavior**.
- It does **not** amend the frozen qualification criteria. `HG-1 … HG-13`, `CT-1 … CT-9`,
  `ND-1 … ND-7`, `OJ-1 … OJ-6` and `SC-1 … SC-20` are unchanged.
- This decision contains **no Baseline results, no performance claims, no historical values, and no
  legal conclusions.**

---

## 2. Decisions

### 2.1 F-9 — Existing verbatim publisher quotations

**APPROVED — CARRIED FORWARD TO STAGE H.**

The Owner accepts the Stage-F finding that the currently located publisher terms do not provide
sufficient evidence for this project to affirmatively authorize public reproduction of the short
verbatim publisher quotations already present in committed Stage-C, Stage-D and Stage-E artifacts.

> **No existing repository artifact is modified at this time.**

Prohibited by this decision: deleting or rewriting prior evidence artifacts; rewriting Git history;
amending prior commits; moving prior tags; characterizing prior publication or retrieval as
unlawful; characterizing the quotations as legally prohibited; and determining whether any statutory
quotation or other legal exception applies.

The project makes only this bounded finding:

> **The available terms evidence is not treated as sufficient to affirmatively authorize public
> reproduction of those quotations under the project's fail-closed publication policy.**

The final repository and publication disposition belongs to **Stage H**, which shall explicitly
review whether the public artifact should retain the quotations, paraphrase them, reduce them to
non-quotational documentary characterizations, or otherwise apply the project's publication
boundary. **No legal conclusion is authorized.**

### 2.2 F-10 — Stage-F external evidence store

**RATIFIED.** The Stage-F persistent external research-material location is accepted, with its
retained terms documents, provenance index, and checksum structure, and with the reported checksum
result accepted.

The store remains **structurally outside the Git worktree** and is not committed. This ratification
is **Stage-F-specific** and does **not** establish a repository-wide storage architecture. It is not
to be relocated or modified without a later reason and Owner authorization. If an integrity defect
is discovered later: **STOP** — it is not to be silently repaired.

### 2.3 F-11 — `OJ-5` resolution

**`OJ-5` IS RESOLVED FOR THE CURRENT NASDAQ EVIDENCE STATE.**

> A candidate whose legitimate local-research-use permission is **UNCLEAR** but is **NOT positively
> restricted** may continue through qualification under a **BOUNDED RESEARCH-USE** disposition.

The common Nasdaq leg for `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` and C-2A may therefore **proceed to
Stage G for gate application**.

**What this disposition is not.** It is **not** a finding that Nasdaq has granted permission; not a
legal interpretation; not a redistribution authorization; not a publication authorization; not a
repository-inclusion authorization. It does **not** resolve `P1-8`, does **not** establish
automated-retrieval permission, does **not** authorize entitlement-gated access, and does **not**
authorize retrieval of historical index values.

**What it means, and only this:** the currently located evidence does not establish a positive
restriction on legitimate local research use, and the frozen §5.5 framework explicitly distinguishes
UNCLEAR from RESTRICTED. Accordingly, **UNCLEAR alone shall not mechanically eliminate a candidate
at `HG-11`**. The uncertainty is carried forward explicitly.

> **The bounded qualification must NOT be silently converted into a PASS.**

### 2.4 F-12 — Durable Stage-F closure record

**APPROVED.** The minimum durable package is the Stage-F Evidence Artifact and this Owner Decision.
Both are **additive**.

Publisher wording is **paraphrased rather than reproduced**, per F-9. No publisher source file, raw
publisher text beyond the minimum necessary, Terms-of-Use text, raw historical value, transformed
series, derived performance statistic, external-store checksum, credential, or personal information
enters the repository. No earlier Stage-C/D/E artifact was modified; the Frozen Baseline, the
criteria freeze, and README are untouched.

### 2.5 F-13 — Broadridge delivery channel

**OUT OF SCOPE** for the current Stage-F qualification.

Broadridge is **not** added as a publisher merely because it serves as a delivery channel for
Invesco statutory documents. The authoritative publisher relevant to the candidate remains
**Invesco**. The existence of the delivery channel is recorded as a provenance/access caveat only.

No Broadridge terms were investigated, the publisher matrix was not expanded, no permission was
inferred from Broadridge, and Broadridge is not treated as a candidate dependency. **If later
evidence establishes that reproducibility or legitimate local research use materially depends on
Broadridge rather than merely on delivery through it, the matter returns to the Owner.**

---

## 3. Stage-F closure determination

**Stage F is accepted as COMPLETE within the authorized documentary boundary.**

The Stage-F findings are **evidence results**. They must not be reinterpreted to preserve or
eliminate any candidate.

### 3.1 C-1 — `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY`

| Item | State |
| ---- | ----- |
| Nasdaq local research use | **UNCLEAR** |
| `OJ-5` | **RESOLVED** by bounded research-use disposition |
| `HG-11` | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED** |
| `HG-11` failure | **None established** |
| Reproducibility | Documentary path reproducible; **data path not** — the value series is entitlement-gated |

### 3.2 C-2A

| Leg | State |
| --- | ----- |
| Nasdaq | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED** |
| Invesco | **PERMITTED** for local research use, as evidenced in Stage F |
| USD/JPY provider | **UNIDENTIFIED BY DESIGN** |
| FX leg `HG-11` | **NOT YET EVALUABLE** |
| Route-level `HG-11` | **PARTIAL**, unless the frozen Stage-G application requires a more specific state |
| `HG-11` failure | **None established** |
| Reproducibility | **Not reproducible end-to-end by anyone**, because one required input is unidentified by design |

### 3.3 Cross-cutting state

| Item | State |
| ---- | ----- |
| Nissay | Evidence / publication axis only; **no candidate `HG-11` consequence** |
| `N-4` | **OPEN / FAIL-CLOSED FOR PUBLICATION** — handoff to Stage H / `P1-8` |
| `P1-8` | **PARTIAL** — nothing cleared for redistribution or for committing raw values |
| Redistribution / publication | **Not authorized for any source** on the evidence located |
| Composition rule | Permissions are **not averaged**; a jointly derived result is no more publishable than its least-clear contributing source |
| Stop conditions | **None triggered** — `SC-12` and `SC-13` in particular were not triggered |
| Candidate elimination | **None.** Stage G owns application of the frozen hard gates |
| Primary Proxy | **NOT APPROVED** |

---

## 4. What this decision does NOT approve

- It does **not** approve a Primary Proxy — P1-2 remains **OPEN**.
- It does **not** pass any hard gate; a bounded qualification is **not** a PASS.
- It does **not** eliminate any candidate.
- It does **not** establish that any publisher has granted permission for anything.
- It does **not** authorize redistribution, publication, repository inclusion, automated retrieval,
  entitlement-gated access, or retrieval of historical index values.
- It does **not** resolve `P1-8`, `O-3`, `HG-4` for C-2A, `HG-8`, `OJ-1`, `OJ-4`, `N-2` continuity,
  `N-3`, or `N-4`.
- It does **not** draw any legal conclusion, and does **not** decide whether any statutory exception
  applies to any act.
- It does **not** determine what this project will publish — that is Stage H.
- It does **not** amend OD-11, OD-12, any Owner Decision, or any frozen criterion.
- It does **not** authorize Stage G or Stage H.
- It does **not** unblock Phase 2.

---

## 5. Anti-circularity confirmation

- **No performance quantity was computed.** Stage F performed **no calculation of any kind**.
- **`ND-1 … ND-7` were not used**, and **no candidate performance was used to interpret any
  licensing term**.
- No publisher or candidate was ranked by permissiveness; the matrices carry labels, never scores
  (`AC-8`).
- `AC-1 … AC-8` were maintained; the three C-1 series share one publisher and received one identical
  assessment (`AC-4`).

---

## 6. Publication and external-material boundary

**No historical value, return, or derived statistic is recorded in this repository.** Publisher
wording is **paraphrased, not reproduced**; no Terms-of-Use text is committed.

No publisher document, provenance index, checksum file, extracted text, scratch tooling, or `F-02`
content enters Git. All source material is retained **structurally outside** the repository.

Redistribution terms remain **unestablished** for every source used at Stages C, D, E and F. The
fail-closed publication policy applies and **nothing is cleared for republication**. The binding
per-source publication determination is **Stage H's**.

---

## 7. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **No prior evidence artifact or decision was rewritten, no commit amended, no tag moved, and no
  Git history altered.**
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked, selected, or eliminated. No hard gate was applied.**
- **No legal conclusion was drawn.**
- **No account, login, personal information, payment, entitlement request, publisher contact, or
  click-through acceptance was used, and no access control was bypassed.**
- **No raw dataset, publisher document, or external provenance material is committed to this
  repository.**
- **Stage G has not begun and is NOT AUTHORIZED. Stage H has not begun and is NOT AUTHORIZED.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Stage F: CLOSED. `OJ-5`: RESOLVED — bounded research-use
disposition. C-1 `HG-11`: BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED. C-2A
`HG-11`: PARTIAL. `N-4`: OPEN / FAIL-CLOSED. `P1-8`: PARTIAL. Primary Proxy: NOT APPROVED — P1-2
remains OPEN. Phase 2: BLOCKED.**
