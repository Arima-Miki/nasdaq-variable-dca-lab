# Phase 1 Primary Proxy Qualification — Stage C Closure Owner Decision

**Status:** APPROVED

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-11

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Closure of Stage C of the Primary Proxy Candidate Qualification Study; disposition of route C-2B; supersession of the J-2 structure finding; continuity handoff |
| Decision status | **APPROVED** |
| Supporting evidence | [`../evidence/phase1_primary_proxy_stage_c_methodology_evidence.md`](../evidence/phase1_primary_proxy_stage_c_methodology_evidence.md) |
| Governing study design | [`phase1_primary_proxy_qualification_study_decision.md`](phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at commit `1e8bc85` |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Criteria-freeze status | **UNCHANGED — no criterion amended, added, renumbered, or re-weighted** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Stage D | **NOT AUTHORIZED** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It disposes of one candidate route and closes one stage of an
authorized Phase-1 study.

> **It is NOT a modification of the Phase-0 Baseline.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and it does not
  create, amend, or supersede any of them.
- The normative Baseline remains [`../experiment_spec.md`](../experiment_spec.md). Where this
  decision and that specification could be read as differing, **the specification governs Baseline
  behavior**.
- It does **not** amend the frozen qualification criteria. Hard gates `HG-1 … HG-13`, comparative
  criteria `CT-1 … CT-9`, non-discriminating information `ND-1 … ND-7`, Owner judgments
  `OJ-1 … OJ-6`, and stop conditions `SC-1 … SC-20` are unchanged, and commit `1e8bc85` remains the
  criteria-freeze boundary.
- This decision contains **no Baseline results and no performance claims.**

---

## 2. Decisions

### 2.1 P-1 — C-2B is dropped from the bounded C-2 route

**APPROVED.**

> **Route C-2B — the QQQ market-price-based return construction — is dropped from the bounded C-2
> qualification route.**

**Reason.** The targeted remediation exhausted the reasonably available authoritative primary
published evidence. Invesco establishes the market-price **observation basis** — the midpoint of the
bid/ask spread, at 16:00 ET — but does not publish sufficient methodology to establish:

- the market-price return construction;
- distribution inclusion;
- reinvestment semantics;
- reinvestment price and timing.

C-2B therefore cannot satisfy `HG-2` and `HG-3` without importing researcher-selected conventions
and presenting them as the publisher's.

**How this must be characterized.**

- This is a **qualification failure under this study's frozen evidence requirements.**
- It is **not** a performance-based selection. No performance quantity was computed at any stage,
  and no candidate was ranked.
- It is **not** a finding that market-price-based return construction is methodologically invalid in
  general, nor a judgment about QQQ as an instrument, nor a judgment about market-price return data
  from any other publisher.
- Recorded narrowly: **C-2B is not qualified for this study.**

**Consequence.** **C-2A remains the surviving implementation of the bounded C-2 route.** C-2A's
survival at this point means only that its methodology is substantially established — it is **not**
a qualification, and `O-3` remains open against it (§2.4).

**What this decision does not do.** It does not reopen `SC-2`, does not reintroduce the excluded
third-party vendor adjusted-close construction, and does not authorize any replacement route.

### 2.2 P-2 — Supersession of the J-2 structure finding

**APPROVED.**

The prior J-2 finding — that QQQ operated as a unit investment trust — was **correct for the dated
primary evidence from which it was derived**, and is **not** rewritten as though it had been wrong.

Temporal provenance is preserved:

| Period | Structure |
| ------ | --------- |
| **Before reclassification** | QQQ operated as a **unit investment trust** |
| **After reclassification** | QQQ operates as an **open-end management investment company** |

The reclassification took effect **after market close on 2025-12-19**, established from primary
evidence dated 2025-12-22.

> **The prior finding is SUPERSEDED as to current structure. It is not corrected as to its own
> date.**

### 2.3 P-3 — Routing to the later continuity stage

**APPROVED.** Both items are **routed forward, not resolved**, and must not be adjudicated before
the stage responsible for `HG-8` / historical continuity.

| # | Item routed | To be evaluated later for |
| - | ----------- | ------------------------- |
| **N-2** | The 2025-12-19 reclassification is a **publisher-documented structural break**. Primary evidence states the Fund had the same investment objective and substantially similar investment policies **but differing expenses** when operating as a UIT | historical continuity; comparability across the reclassification; embedded-expense treatment; OD-11 implications |
| **N-3** | The Nasdaq-100 methodology change **effective 2026-05-01** | methodology-break documentation across the intended span |

Neither item was investigated or adjudicated in the closure task, and neither may be treated as
resolved by having been recorded.

### 2.4 Stage C determination

**Stage C is CLOSED for the purpose of advancing the study.**

| Route | Status |
| ----- | ------ |
| **C-1** `NDXJPY` | Advances — methodology established |
| **C-1** `XNDXJPY` | Advances — methodology established |
| **C-1** `XNDXNNRJPY` | Advances — methodology established |
| **C-2A** | Advances — QQQ NAV-based constructed route |
| **C-2B** | **Does not advance** — dropped by §2.1 |
| **C-3** | Out of scope by the frozen study design |

Binding conditions on this closure:

- **`O-3` remains explicitly OPEN.** C-2A's observation basis — financial-reporting NAV versus
  shareholder-transaction NAV — is **not** pinned. It must **not** be treated as resolved, and must
  not be silently resolved by adopting whichever basis a later construction finds convenient.
- **Every remaining open issue retains its existing blocking / non-blocking semantics** under the
  frozen study design. Closure of the stage does not downgrade any open item.
- **`O-1` is closed by disposition, not by evidence.** The C-2B semantics were never established;
  the item is closed because the route was dropped.
- Advancing a route means only that it is **eligible for later qualification stages**. It is not a
  qualification, not an approval, and not a preference.

---

## 3. What this decision does NOT approve

The narrowness is deliberate. This decision does **not**:

- approve a **Primary Proxy** — P1-2 remains **OPEN**;
- qualify C-1 or C-2A against any hard gate;
- rank, score, weight, or prefer any candidate against any other;
- decide the **admissibility** of pre-launch or non-live history — `OJ-1` remains **UNDECIDED**, and
  "available history" must still not be read as "admissible history";
- choose a **Baseline Start Date** or a **Baseline Dataset Cutoff**;
- select an **FX source** or FX convention for the C-2 route;
- resolve `O-2`, `O-3`, `O-4`, `O-5`, `O-6`, or `O-7`;
- read any publisher's licensing terms or clear any source for redistribution;
- authorize **Stage D**;
- unblock **Phase 2**.

---

## 4. Anti-hindsight and anti-circularity confirmation

- **No performance quantity was computed** at any point in Stages A–C or the remediation.
- **`ND-1 … ND-7` were not used** in reaching any part of this decision.
- C-2B was dropped on **documentary grounds only**. Its removal was not informed by how any
  candidate performs, and no comparison between C-1 and C-2 was made.
- No qualification criterion was changed to accommodate a finding. Where Stage A raised criteria
  observations and Stage B raised an identifier ambiguity, both were resolved by **Owner
  interpretation** rather than by amending the frozen criteria.

---

## 5. Research-integrity finding

Recorded narrowly, as a durable verification discipline:

- one document-extraction step produced **fluent but unrelated content**, and local verification
  established that the **underlying primary PDF was itself valid**;
- a later extraction produced **false-negative** keyword results because of mixed and subset font
  encodings;
- both failures were **detected and corrected** using document-identity verification and
  plausibility checks, and neither entered the evidence.

> **Critical documentary evidence must be verified against the actual document. Fluent extraction
> output and zero-hit extraction must not be trusted without integrity checks.**

This is a research discipline. It is **not** a repository architecture requirement, and the
implementation details of the temporary extraction tooling are deliberately not recorded as one.

---

## 6. Privacy boundary applied during research

SEC EDGAR refused automated retrieval on every attempted path, and its policy requires a declared
contact identity.

**No personal email address, personal name, credential, private repository information, or other
personal identifier was transmitted to SEC or to any other external service, and no contact address
was invented.** The path was not used. The limitation is recorded rather than worked around, and
the required documents were obtained instead from the issuer's own published copies.

This boundary remains in force for all later stages.

---

## 7. External research-material retention — Owner decision required

The primary documents underpinning the Stage-C findings were retained in a **session-scoped**
working location, which is **not durable storage**. Their loss would not invalidate the recorded
findings — the evidence artifact carries publisher, document title, date/version, and locator for
each source, which is what makes a finding auditable — but it would make re-verification depend on
re-retrieval from the publisher.

**No file has been moved.** The repository has no documented persistent research-material location,
and `.gitignore` names only an in-repository `/temp/` directory, which does **not** satisfy the
study design's requirement that source material live *structurally outside* the repository. Moving
material into a newly created location would establish a convention this repository does not yet
have, so it is put to the Owner rather than decided:

> **Proposed:** a persistent location outside the repository, e.g. `~/research-materials/nasdaq-variable-dca-lab/primary-proxy-stage-c/`,
> holding the Nasdaq and Invesco primary documents named `D-1 … D-13` in the evidence artifact,
> with a plain-text provenance index recording publisher, title, date/version, locator, and
> retrieval date.

Binding regardless of the outcome: **publisher PDFs must not enter Git**, and an ignored directory
inside the repository is not an acceptable substitute for a location outside it.

---

## 8. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **The frozen qualification criteria are unchanged.** Commit `1e8bc85` remains the criteria-freeze
  boundary.
- **No prior evidence artifact was rewritten.** The J-2 supersession is recorded additively, with
  temporal provenance preserved.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked or selected.**
- **No raw dataset and no publisher document is committed to this repository.**
- **Stage D has not begun and is NOT AUTHORIZED.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Stage C: CLOSED. C-2B: DROPPED — not qualified for this study.
Primary Proxy: NOT APPROVED — P1-2 remains OPEN. Phase 2: BLOCKED.**
