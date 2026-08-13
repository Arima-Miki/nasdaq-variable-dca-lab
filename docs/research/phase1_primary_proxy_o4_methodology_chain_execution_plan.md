# Phase 1 Primary Proxy Qualification — `O-4` Methodology-Chain Research Execution Plan

**Status:** **DRAFT PLAN — NOT APPROVED FOR EXECUTION.** No external research may begin until the
Owner explicitly approves this plan

**Scope:** Phase 1 — Data Foundation

**Plan drafted:** 2026-08-13 — **this date is not `K1` and does not affect `K1`**

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Research Execution Plan** — procedural, not normative |
| Subject | How the already-authorized bounded `O-4` methodology-chain research will be executed |
| Plan status | **DRAFT — NOT APPROVED FOR EXECUTION** |
| Controlling authorization | [`../decisions/phase1_primary_proxy_o4_bounded_research_authorization_decision.md`](../decisions/phase1_primary_proxy_o4_bounded_research_authorization_decision.md) — commit `b0aaab99772bfe396e4383f3498de81002e68f33`, tag `phase1-primary-proxy-o4-research-authorization-20260813` |
| `O-4` | **OPEN** |
| `O-4` research | **AUTHORIZED BUT NOT YET EXECUTED** |
| **`O-4` Research Cutoff** | **`K1` = 2026-08-13 — IMMUTABLE** |
| `K1` semantics | **S-A** — explicit Owner-approval date |
| Research floor | The **`OD-P15-06` Base Value Date methodology-research scoping floor**, narrow semantics unchanged |
| Candidate scope | `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` — **distinct** |
| `P1-5` | **OPEN** — principle **P-A**; date **NOT YET DERIVED** |
| `P1-6` | **OPEN** |
| `HG-8` | **NOT EVALUABLE** ×3 — **not reapplied**, and not evaluated by this plan or its execution |
| `HG-6` / `HG-9` / `HG-12` | **PASS ×3** each, with their recorded limitations and conditions |
| `HG-11` | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; not PASS; non-eliminating; carried to `OJ-6` |
| `H-1` | **NOT ESTABLISHED** · `P1-9` **PARTIAL** |
| C-2A | **Unchanged and outside this plan** |
| `OJ-1` | **NOT REACHED — DEFERRED** · `OJ-6` **unexercised** |
| Primary Proxy | **NOT APPROVED — P1-2 remains OPEN** |
| Stage G | **OPEN** · Stage H **NOT BEGUN** · Phase 2 **BLOCKED** |
| External access during drafting | **NONE.** No browsing, no retrieval, no URL testing, no availability checking |

### 1.1 Artifact location — reasoning

This artifact is placed at `docs/research/`, a **new directory**, rather than in `docs/decisions/`
or `docs/evidence/`.

- It is **not evidence** — it contains no research finding.
- It is **not an Owner Decision** — placing it in `docs/decisions/` would imply decision-level
  normative force it should not carry. It is a *procedure* subordinate to the authorization.
- The repository's only existing research-protocol text — the staged process at frozen study design
  §12 — lives **inside** a decision artifact, as part of the criteria freeze. This plan is
  deliberately **not** part of any freeze and must remain amendable by Owner Review without touching
  frozen text.

**Alternative considered and rejected:** `docs/decisions/`, on the precedent above. Rejected because
the precedent is a *frozen* protocol embedded in a criteria artifact, which this is not.

### 1.2 Precedence

> **This plan governs HOW the authorized research is executed. It does not extend WHAT is
> authorized.**

Where this plan and the controlling authorization could be read as differing, **the authorization
governs**. Where the authorization and any higher authority in its §3 hierarchy could be read as
differing, **the higher authority governs**. This plan adds no permission, widens no boundary,
creates no criterion, and creates no gate.

---

## 2. Authority and precedence

Read and relied upon for this plan, in the order the authorization's §3 fixes:

| Rank | Authority | What this plan draws from it |
| ---- | --------- | ---------------------------- |
| 1 | **Frozen Phase-0 Baseline** | §6 look-ahead prohibition; §14.4; §14.6 / OD-12; Invariant 17 |
| 2 | **OD-01 … OD-14** | OD-12's standard and anti-cherry-picking rationale |
| 3 | **Criteria freeze `1e8bc85`** | `HG-8`'s wording; `AC-1 … AC-8`; `SC-1 … SC-20`; **S.2** and its minimisation rule; the PRIMARY / NEAR-PRIMARY / SECONDARY / UNREAD tiering |
| 4 | **`OD-P15-01 … 12`** | Rule/date split; Interpretation B; cutoff conditions; floor; **K1**; anti-circularity fixing |
| 5 | **Stage-D Owner Decisions** | **D-2**, **D-5**, **D-6**, **D-8**, **D-9**, **D-10** |
| 6 | **Stage-G authorization** | **`G-OD-08`**; `SC-3` / `SC-4` treatment |
| 7 | **Stage-F licensing record** | Redistribution **UNCLEAR**; fail-closed publication policy; the recorded access limitations |
| 8 | **The `O-4` authorization** | §§4–15 — question, scope, span, hierarchy, protocol, preservation, publication, result vocabulary, anti-circularity, stop conditions |
| 9 | **This plan** | Execution procedure only |

**Repository evidence read for planning purposes** (facts, not new research): Stage-C methodology
evidence (document inventory `D-1 … D-13`; candidate identities and return versions; `O-2`, `O-4`,
`O-5`); Stage-D history/continuity evidence (`E-7` consultation; `N-3`; §10.2 version-history
finding; segment maps; `H-1 … H-8`); Stage-F licensing evidence (`T-05`/`T-06` access-policy record;
recorded host access limitations).

> **No authority is taken from chat history.** Every input above is a committed repository artifact.

---

## 3. Research objective

### 3.1 The question, unchanged

> **Can the methodology chain required for `HG-8` be established with sufficient documentary
> continuity across the authorized bounded research span, for each C-1 candidate?**

### 3.2 The proposition to be tested

> For the intended span, the candidate's governing methodology chain is reconstructable: **every
> methodology change effective within that span is identified and dated from authoritative
> documentary evidence, or it is authoritatively established that no such change occurred within
> it.**

### 3.3 The eight determinations

Carried verbatim in force from the authorization `O4-OD-01`, and answered **per candidate**:
(1) methodology identity across the span; (2) whether changes occurred within it; (3) each change's
effective date; (4) whether versions can be ordered; (5) whether continuity between successive
versions can be established; (6) whether a documentary gap remains; (7) whether any gap is material
to the construction `HG-8` requires; (8) whether the evidence supports a **determinate** `HG-8`
application.

> **`HG-8` is not evaluated.** Determination 8 records whether an application would be *possible*.

### 3.4 Coverage standard

**Enumerative, not incidental.** A search returning only already-known changes cannot distinguish
*no change occurred* from *no change was found*. **Absence of evidence is not evidence of absence.**

---

## 4. Fixed research span

| Bound | Value | Source |
| ----- | ----- | ------ |
| **Floor** | The **published Base Value Date** methodology-research scoping floor | `OD-P15-06`. The literal date is established in the committed Stage-D record §5.1 and is **not restated or re-derived here** |
| **Ceiling** | **`K1` = 2026-08-13** | `OD-P15-10` + `O4-OD-04` (S-A) |

**Both boundaries are immutable for this bounded study.**

### 4.1 The floor establishes nothing else

> It does **NOT** establish: first live observation; first actual observation; `H-1`; the `P1-5`
> date; measured-performance admissibility; Reference-High warm-up availability; or full historical
> admissibility.

It is a research floor **only** because the pre-base-date segment is excluded from measured
performance, warm-up, and other qualification use under **D-6** and §6.4. **D-8** and `SC6-OD-03` are
unchanged.

### 4.2 The ceiling is not a data cutoff

> `K1` is **NOT** `P1-6`; **NOT** the Baseline Dataset Cutoff; **NOT** a historical-data cutoff; and
> **NOT** evidence that no methodology change occurs later.

### 4.3 No new date

**This plan derives no date.** `K1` is quoted from the authorization; the floor is referenced by
name. Execution likewise derives no date — it *discovers* effective dates from documents and records
them as findings.

---

## 5. Candidate scope

Three candidates, carried **distinctly and symmetrically** per `AC-4`. Identities are as established
at Stage C:

| Candidate | Official name (Stage-C record) | Return version |
| --------- | ------------------------------ | -------------- |
| `NDXJPY` | Nasdaq-100 Index JPY | Price return |
| `XNDXJPY` | Nasdaq-100 Total Return JPY | Gross total return |
| `XNDXNNRJPY` | Nasdaq-100 Notional Net Return JPY | Notional net total return |

> **Evidence for one return version does not automatically establish another.**

Shared evidence is permitted where genuinely common — but **candidate applicability must be
demonstrated from the document's own scope statement**, never inferred from family membership.
Return-version-specific elements (withholding convention, reinvestment convention, version-register
entry) must be established **per version**.

**C-2A is outside this plan entirely.** It is neither researched nor re-evaluated, and no C-2A
finding may be produced.

---

## 6. Execution phases

The authorization's protocol is procedural rather than phased; this plan renders it as a
deterministic sequence. **The proposed `R0 … R10` structure is adopted with two modifications**,
each explained:

- **`R2` and `R3` are kept separate** as proposed, because they have different evidence
  characteristics: `R2` re-examines material **already held** (no external access), while `R3`
  requires external discovery. Merging them would hide a boundary that matters for audit.
- **A new `R3a` — preservation checkpoint** is inserted, because §15's preservation-before-
  interpretation rule requires retention, checksumming and provenance to complete **before** any
  chain reasoning uses a document. Without an explicit checkpoint the rule is easy to violate
  silently mid-phase.

Nothing else is renamed, split, merged, or reordered.

| Phase | Objective | Allowed inputs | Expected outputs | Evidence class | Candidate scope | Completion condition | Stop / escalation | **External access?** |
|-------|-----------|----------------|------------------|----------------|-----------------|----------------------|-------------------|----------------------|
| **R0** — repository-authority extraction | Re-derive the binding boundary from committed artifacts alone | Repository only | Boundary restatement; the already-held document inventory; open items `O-2`, `O-4`, `O-5`, `N-3` | None produced | All three | Boundary restated and matched against the authorization | Any divergence from the authorization → **STOP** | **No** |
| **R1** — candidate identity and methodology-family map | Fix, from committed evidence, which documents are *claimed* to govern which candidate | Repository + already-retained Stage-C/D store | Per-candidate identity map; explicit list of applicability **assumptions to be tested** | Existing PRIMARY | Per candidate | Map complete, with every unverified applicability marked as hypothesis | Identity ambiguity → record, continue | **No** |
| **R2** — current / latest primary methodology identification | Establish version identity and in-body date of each **already-held** document | Already-retained store only | Version/date table for held documents; `O-5`-type date gaps named | Existing PRIMARY | Per candidate | Every held document has version identity recorded or a stated gap | — | **No** |
| **R3** — historical methodology-version discovery | Locate **superseded** versions of each document class | Publisher repositories, version register, document libraries, archives | Candidate prior versions; ACCESS-LIMITED inventory | Tier 1–2 | Per document class, then mapped per candidate | §12 exhaustion criteria met for each class | §12 states; `SC-15` | **YES** |
| **R3a** — preservation checkpoint | Retain, checksum and record provenance for everything retrieved in `R3` | Retrieved material | Store entries; `SHA256SUMS`; `PROVENANCE.md` rows | — | — | Every retrieved item preserved **before** it is interpreted | Checksum mismatch → **STOP** | No (local only) |
| **R4** — methodology-change / effective-date discovery | Locate publisher notices stating a change and its effective date | Publisher change/notice channels; archives | Dated change inventory; undated-change inventory | Tier 1–2 | Per candidate | §12 exhaustion met for the notice channel | `SC-4` if a change is known but undatable | **YES** |
| **R5** — version-chain reconstruction | Order versions and establish supersession | `R2`–`R4` outputs, preserved | Per-candidate version chain with intervals | Derived from Tier 1–3 | Per candidate | Chain assembled, or gap classified | Conflict → `CONFLICT`, §12 | No |
| **R6** — candidate-to-version applicability reconciliation | Establish, per version, which candidates it governs, **from its own scope statement** | Preserved documents | Applicability matrix | Derived | Per candidate | Every chain interval has applicability established or `GAP-5`/`GAP-6` | Ambiguity → gap, continue | No |
| **R7** — documentary-gap analysis | Classify every residual gap and assess materiality to `HG-8` | `R5`–`R6` outputs | Gap register with classes and materiality | Derived | Per candidate | Every gap classified | — | No |
| **R8** — bounded completeness / stopping evaluation | Record, per candidate and per suspected transition, which §12 state was reached | Search log | Exhaustion record | — | Per candidate | Every search line has a §12 state | Any `OWNER-ESCALATION` → **STOP** | No |
| **R9** — `O-4` result classification | Apply §17's decision procedure | `R7`–`R8` outputs | Per-candidate `O4-*` result | — | Per candidate | Each candidate classified | Any state requiring discretion → **STOP** | No |
| **R10** — evidence-package and artifact preparation | Prepare the external package and the *proposed* repository artifact | All prior outputs | Verified store; **draft** repository evidence artifact | — | All | Package verified; draft prepared | — | No |

> **External access occurs in `R3` and `R4` only.** Every other phase is repository-local or
> analysis of already-preserved material.

---

## 7. Source hierarchy — operational lookup order

The authorization's hierarchy, rendered as a lookup order. **Higher tiers are exhausted before lower
tiers are consulted for the same fact.**

| Order | Tier | Class | Role |
| ----- | ---- | ----- | ---- |
| 1 | **Tier 1** | Dated official methodology documents; official methodology-change notices | **Can establish** a change, its effective date, and version identity |
| 2 | **Tier 2** | Official publisher pages or archives establishing version identity, effective date, or continuity | **Can establish** version identity and supersession; can corroborate dates |
| 3 | **Tier 3** | Other primary publisher material capable of corroborating the chain (consultations, proposals, notices bearing on a change without dating it) | **Corroborates only.** Cannot alone date a change |
| — | **Issuer-side primary** | Authoritative issuer or other authoritative party — per **`G-OD-08`** | **Tier 1 for the fact it establishes**, recorded as issuer-side. **Does not close a publisher-side provenance gap** |
| 4 | **SECONDARY** | Everything else | **Pointer only** — see §7.2 |
| — | **Archived copies** | Third-party archive of publisher material | **Tier 2 at best**, with the caveat that fidelity to the publisher original could not be verified against the publisher. **Never promoted to Tier 1 by content** |

### 7.1 The primacy rule

> **Secondary sources must not silently substitute for missing primary methodology evidence.** A gap
> in Tier 1 evidence is recorded as a **gap**. `SC-7` applies: secondary material is never promoted.

### 7.2 Secondary evidence — bounded exactly as authorized

Consultable **only** where all five authorization conditions hold:

1. Tier 1–3 primary avenues for that specific fact are exhausted under §12;
2. used **only** to locate or identify primary material — as a **pointer**, never as the fact;
3. recorded and labelled **SECONDARY**, with the fact it points to remaining **UNESTABLISHED**;
4. **never** used to establish a methodology change, effective date, version ordering, or continuity;
5. its use disclosed in the evidence artifact, with the gap it failed to close stated.

> **A secondary-source lead must be returned to a primary publisher source before it can support
> `O-4`.** If the lead cannot be converted to primary material, the fact stays UNESTABLISHED and the
> gap stands. **A conclusion resting on secondary material alone is not a resolution of `O-4`.**

---

## 8. Candidate search plans

**Design only. No query below may be executed until the Owner approves this plan.**

### 8.1 What the repository establishes, versus what is hypothesis

| Established by committed repository evidence | Hypothesis — to be tested at execution, not assumed |
| -------------------------------------------- | --------------------------------------------------- |
| Publisher / authority: **Nasdaq, Inc.** | That a publisher **change log** or version archive exists at all |
| The five already-held Nasdaq documents and their locators (`D-1` … `D-5`) | That prior versions are reachable at predictable locator patterns |
| The February 2026 consultation (`E-7`) exists and is a **proposal** | That consultation **outcome** documents are published as a class |
| `N-3`: a change **effective 2026-05-01**, established from **fund-issuer** evidence; publisher final decision document **NOT LOCATED** | That any publisher-side document dating `N-3` exists |
| `O-5`: at least one held document carries **no in-body effective date** | That undated documents can be dated from a publisher listing |
| `O-2`: a withholding-tax-rates document is **referenced but not retrieved** | That it bears on `XNDXNNRJPY`'s methodology **chain** (as opposed to a parameter) |
| Stage-D §10.2: under **D-2** authorization, **no** superseded version and **no** publisher change log was located | That a different search route would reach one |
| The index hosts' `robots.txt` is **readable** and disallows no path used | That it permits any particular new path — **`robots.txt` is not a licence** |
| The Nasdaq **site-wide terms host was unreachable** — an access limitation, not an absence of terms | That it is reachable now |

> **Nothing in the right-hand column may be recorded as fact without evidence obtained under this
> plan.**

### 8.2 Document-class targets

Sought as **current and superseded** versions of each: the index methodology document; the
calculation manual governing return types and index currency; the index-version register; the
general index methodology guide; the recalculation policy; and any publisher notice dating a
transition between versions of any of these.

### 8.3 Distinguishing a methodology document from a non-methodology document

Applied **before** a document is admitted as Tier 1:

| Admit as methodology evidence | Exclude — record as non-methodology |
| ----------------------------- | ----------------------------------- |
| States construction, eligibility, weighting, calculation, or return-version rules **normatively** | Describes the index for **marketing** or explanatory purposes |
| Carries a version identifier, effective date, or supersession statement | Is a **product**, factsheet, or brochure page |
| Carries a scope statement naming the index or index family | Is a **performance** page or a values/data display |
| Is issued **by the publisher** as governing text | Is a **derivative** work — a licensee's or distributor's restatement |
| A **consultation outcome** stating what was adopted | A **consultation proposal** — Tier 3 corroboration only, as `E-7` already is |

**Tie-break rule:** if a document's normative status is unclear, it is recorded at the **lower**
tier, and the ambiguity is noted. Fail-closed.

### 8.4 Per-candidate search plans

Search terms are grouped as **index-level** (may yield shared evidence) and **candidate-specific**
(required to discharge applicability). A hit at index level **does not** discharge the per-candidate
determination unless the document's own scope statement covers that version.

#### Common index-level terms — run once, applied to all three only if scope permits

Proposed query forms, **not executed**:

```
Nasdaq-100 index methodology              [+ "version" | "effective" | "supersede" | "archive"]
NDX methodology  effective date
Nasdaq index methodology guide            [+ "version history" | "previous versions"]
Nasdaq calculation manual equities        [+ "version" | "revision history"]
Nasdaq recalculation policy               [+ "version"]
Nasdaq index alerts | index notices | methodology change notice
Nasdaq-100 consultation                   [+ "results" | "outcome" | "decision"]
Nasdaq index versions register            [+ "NDX"]
```

Fallback forms if the above return nothing: publisher document-library listing pages; publisher
notice/announcement index pages; the version register's own internal references; archived copies of
the above (Tier 2 at best).

#### `NDXJPY` — Nasdaq-100 Index JPY, price return

- **Publisher expected to control:** Nasdaq, Inc. *(established)*
- **Methodology family expected:** the NDX index methodology plus the calculation manual's
  price-return and Index-Currency provisions *(established that these documents exist; that they
  jointly govern this candidate across the whole span is a **hypothesis**)*
- **Candidate-specific terms:** `NDXJPY`; "Nasdaq-100 Index JPY"; price return + JPY currency
  conversion provisions
- **Applicability to establish:** that the price-return and JPY-currency provisions applied
  throughout the span, and that any change to either is dated

#### `XNDXJPY` — Nasdaq-100 Total Return JPY, gross total return

- **Publisher / family:** as above, plus the calculation manual's **gross total-return** and
  dividend-reinvestment provisions
- **Candidate-specific terms:** `XNDXJPY`; "Nasdaq-100 Total Return JPY"; gross total return;
  ex-date reinvestment
- **Applicability to establish:** that the gross-TR reinvestment convention applied throughout, and
  that any change to it is dated
- **Note:** the price-return chain does **not** establish the TR chain. `AC-4` requires the same
  search depth for each

#### `XNDXNNRJPY` — Nasdaq-100 Notional Net Return JPY, notional net total return

- **Publisher / family:** as above, plus the **notional net** provisions
- **Candidate-specific terms:** `XNDXNNRJPY`; "Nasdaq-100 Notional Net Return JPY"; notional net
  return; withholding / tax-rate provisions
- **Applicability to establish:** that the notional-net convention applied throughout, and that any
  change to it — including to the notional rate — is dated
- **`O-2` interaction:** the referenced withholding-tax-rates document remains **not retrieved**. If
  encountered incidentally it may be recorded, **but `O-2` is not in scope for resolution here**, and
  a change to a *rate parameter* must not be silently equated with a change to the *methodology
  chain*. Where the distinction is unclear → record as `GAP-6` and escalate if material

### 8.5 Access-route realism, from the committed record

Two recorded facts bear on route selection and must be carried into execution rather than
rediscovered as surprises:

1. The Nasdaq **site-wide terms host was unreachable** from the research environment across two HTTP
   versions and two clients. Recorded as an **access limitation, not an absence of terms**. If it is
   unreachable again, that is `ACCESS-LIMITED`, not a finding.
2. **SEC EDGAR returned HTTP 403** under its declared-automated-tool policy at Stage C, and the path
   was **not used** because no contact identity was invented. **That position is unchanged**: EDGAR
   remains outside the authorized routes for this study.

---

## 9. Evidence matrix design

Two tables, because document inventory and chain reconstruction have different keys — one row per
**document**, one row per **chain interval**. A single table would force either duplication or loss.

**Both are presented empty. No newly researched fact is entered here.**

### 9.1 Table A — document inventory (one row per document)

| Evidence ID | Candidate applicability | Methodology family / identity | Publisher | Document class | Document date | Effective date | Version | Supersedes | Superseded by | Primary / secondary | Evidence tier | Retrieved? | Retained externally? | Checksum recorded? | Provenance recorded? | Applicability established? | Notes / caveats |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | |

### 9.2 Table B — chain reconstruction (one row per candidate × interval)

| Candidate | Interval start | Interval end | Controlling document (Evidence ID) | Applicable from | Applicable through | Continuity predecessor established? | Continuity successor established? | Documentary gap? | Gap class | Gap material to `HG-8`? | Notes / caveats |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

### 9.3 Table C — search log (one row per search line)

Required so that §12 exhaustion is auditable rather than asserted.

| Candidate / target | Source class | Query or locator form | Executed? | Outcome | §12 state | Evidence IDs produced | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 9.4 Table D — missing / inaccessible inventory

| Item sought | Why sought | Evidence for its existence | Barrier | §12 state | Fact left UNESTABLISHED |
|---|---|---|---|---|---|
| | | | | | |

---

## 10. Methodology-chain reconstruction rules

Fixed **before** evidence is observed.

### 10.1 How each element is determined

| Element | Determination rule |
| ------- | ------------------ |
| **Version identity** | From the document's own version identifier, in-body date, or a publisher listing that names it. Never from filename, URL, or file timestamp alone |
| **Chronology** | From established effective dates. Where only document dates exist, ordering is **provisional** and marked as such |
| **Effective dates** | From Tier 1 statements, or from `G-OD-08` issuer-side primary evidence. **Never inferred** from publication, retrieval, or file-creation dates |
| **Supersession** | From an explicit publisher statement that one version replaces another, or from a publisher listing that orders them. Inferred supersession is recorded as **inferred**, not established |
| **Overlap** | Where two versions claim the same interval, record both and classify `GAP-8` / `CONFLICT`. Do not resolve by preference |
| **Gaps** | Any interval of the span with no established controlling document → `GAP-7` |
| **Candidate applicability** | From the document's **own scope statement**. Never from family membership, naming similarity, or publisher identity |
| **Return-version applicability** | Per version, from provisions that name the return version or its convention |
| **One version covering multiple candidates** | Permitted **only** where the scope statement covers them. Recorded once in Table A with multi-candidate applicability, and referenced from each candidate's Table B rows — no duplication of evidence |
| **Change affecting all vs. some candidates** | Determined from the changed provision's own scope. A change to a shared construction rule may affect all; a change to a reinvestment or withholding convention may affect only some. **Established, never assumed** |

### 10.2 Prohibited inferences — binding

> - **publication date ≠ effective date**
> - **retrieval date ≠ document date**
> - **the latest document does not describe the entire historical span**
> - **one candidate's continuity does not prove another candidate's continuity**
> - **absence of a located change notice does not prove absence of a methodology change**

Each is a recorded failure mode in this repository: the third and fifth are precisely why `O-4`
remains open after Stage-D's authorized search; the second is why `O-5` exists; the fourth is
`AC-4`.

### 10.3 The `N-3` in-span case, named in advance

The committed record establishes a methodology change **effective 2026-05-01** — inside the span —
whose **publisher-side final decision document was NOT LOCATED**, with a **proposal** (`E-7`) and a
**fund-issuer** confirmation standing in its place.

At execution this is a **specific target** under `R4`, and a specific classification case under §11:

- If a publisher-side dating document is located → the `N-3` provenance gap narrows. **`N-3` is not
  thereby closed as an open item**; that is an Owner act.
- If it is not located → the state is **unchanged**, recorded as `GAP-3`-adjacent or `GAP-2`
  depending on what was found. **Its continued absence must not be re-recorded as closure**, and the
  existing `G-OD-08` position stands: the change is **dated** from issuer-side primary evidence, so
  `SC-4` is not triggered.

---

## 11. Gap taxonomy

**Planning vocabulary only.** These classes are not governed by repository authority, create **no
hard gate**, and have no gate consequence. They exist to make `R7` auditable.

| Class | Meaning | Research continues? | Fallback search allowed | Secondary evidence? | Owner escalation? | Could it prevent `O4-ESTABLISHED`? |
|---|---|---|---|---|---|---|
| **GAP-0** | No documentary gap identified within the bounded chain | Yes — to completion | — | No | No | **No** |
| **GAP-1** | Document identity known, primary document retrievable | Yes — retrieve it | Locator variants; publisher listings | No | No | **No**, once retrieved |
| **GAP-2** | Identity / version known, primary document **inaccessible** | Yes | Archives (Tier 2); alternate publisher listing | **Pointer only**, §7.2 | Only if the barrier is an authorization boundary | **Yes**, if the interval it governs is otherwise uncovered |
| **GAP-3** | Transition known, exact **effective date** not established | Yes | Notice channels; issuer-side primary per `G-OD-08` | **Pointer only** | If undatable → **`SC-4`**, escalate | **Yes** |
| **GAP-4** | Successive documents located, **supersession not established** | Yes | Publisher listings; version register | **Pointer only** | No | **Yes**, if ordering is material |
| **GAP-5** | **Candidate applicability** ambiguous | Yes | Scope statements in adjacent versions | No | If unresolvable and material | **Yes**, for the affected candidate |
| **GAP-6** | **Return-version applicability** ambiguous | Yes | Return-version provisions; version register | No | If unresolvable and material | **Yes**, for the affected candidate |
| **GAP-7** | A portion of the span has **no identified controlling methodology** | Yes | Full re-run of §12 order for that interval | **Pointer only** | If it persists after exhaustion | **Yes — decisive** |
| **GAP-8** | Primary sources **conflict** | **Record both; do not resolve** | None — resolution by search is not permitted | No | **Always** | **Yes** |

> **No gap class may be downgraded because it is inconvenient.** A gap that persists after §12
> exhaustion is reported as a gap.

---

## 12. Search exhaustion and stopping rules

Fixed in advance so research cannot expand indefinitely once results are seen — and, equally, cannot
stop early once results look sufficient.

### 12.1 The lookup order, per candidate and per suspected transition

Executed in order; each step is recorded in Table C whether or not it yields anything:

1. **Already-held material** — the retained Stage-C/D store. No external access.
2. **Publisher document repositories** — current and any listed prior versions of each §8.2 class.
3. **Publisher index-version register** — version identity, symbols, return versions.
4. **Publisher document libraries / listings** — enumeration and supersession statements.
5. **Publisher change / notice channels** — notices, alerts, rule-change announcements, consultation
   **outcomes**.
6. **Issuer-side primary evidence** under `G-OD-08`, where a publisher-side document is absent.
7. **Archives** — Tier 2 at best, only to reach publisher-issued material not otherwise reachable.
8. **Secondary** — pointer only, under all five §7.2 conditions.

### 12.2 Exhaustion criterion

A search line is **exhausted** when steps 1–8 have been attempted in order for that specific target,
**or** an earlier step answered it, **or** a §12.3 state other than `SEARCH-COMPLETE` was reached.

> **Exhaustion is a statement about the search performed, not about what exists.**

### 12.3 The five terminal states

| State | Meaning | Consequence |
| ----- | ------- | ----------- |
| **`SEARCH-COMPLETE`** | The approved lookup sequence was executed sufficiently to classify the documentary state | Proceed to `R7` |
| **`ACCESS-LIMITED`** | Relevant material identified but not retrievable through authorized routes | Record with barrier named; `GAP-2`; **not** an absence |
| **`IDENTITY-UNRESOLVED`** | The controlling document or transition cannot be identified | `GAP-7` or `GAP-3`; record |
| **`CONFLICT`** | Primary publisher evidence is materially inconsistent | `GAP-8`; **record both**; escalate |
| **`OWNER-ESCALATION`** | Continuing would require widening the boundary, changing evidence rules, purchasing access, creating an account, using an unapproved source class, or a discretionary judgment that could affect qualification | **STOP.** Return to Owner |

> **Scope is never silently expanded in any of these cases.**

### 12.4 Anti-expansion and anti-contraction

- **Exhaustion criteria may not be changed after results are observed** (`AC-1`).
- Additional search **beyond** the approved order requires Owner approval — it is
  `OWNER-ESCALATION`.
- Stopping **before** the order is exhausted, because the result already looks adequate, is
  prohibited. **`AC-4` requires the same depth for all three candidates**, including any candidate
  whose chain looks inconvenient.

---

## 13. External evidence-store design

**Plan only. The store directory is NOT created by this planning task** — creating it would be a
preparatory act of execution, and the authorization's boundary is that execution begins only after
approval of this plan.

### 13.1 Proposed structure

```
~/research-materials/nasdaq-variable-dca-lab/primary-proxy-o4-methodology-chain/
    PROVENANCE.md
    SHA256SUMS
    O4-D01_<publisher>_<document-slug>_<yyyymmdd>.<ext>
    O4-D02_...
    ...
```

**Structurally outside the Git worktree** — not an ignored repository directory. Verified at
execution with `git rev-parse --is-inside-work-tree` returning "not a git repository".

### 13.2 Filename normalization

`O4-D<nn>_<publisher>_<document-slug>_<retrieval-date>.<ext>` — lower-case slug, hyphens within a
field, underscores between fields, no spaces, no publisher-supplied filename retained verbatim where
it contains spaces or characters requiring quoting.

### 13.3 Evidence IDs

- **`O4-D01 …`** — retained documents.
- **`O4-M01 …`** — items sought and **not** obtained (missing / inaccessible inventory).
- **`O4-X01 …`** — retrieval failures with a recorded barrier.

The `O4-` prefix is required by the authorization, to avoid the existing `D-n` collision between
Stage-C document IDs and Stage-D Owner Decision IDs.

### 13.4 Candidate applicability and shared documents

Applicability is recorded **in `PROVENANCE.md`, once per document**, as an explicit list of the
candidates the document's **own scope statement** covers — plus a separate field recording whether
that applicability is **established** or **hypothesised**.

> **Shared documents are stored once and referenced from each candidate's chain rows. Evidence is
> never duplicated**, because duplication would misrepresent one document as independent
> corroboration of itself.

### 13.5 Missing, inaccessible, and failed retrievals

Each recorded as its own entry with: what was sought; why; the evidence for its existence; the exact
barrier; the §12.3 state; and the fact left UNESTABLISHED. **Absence is recorded, never omitted.**

### 13.6 Documents that change during the research session

If a source is observed to differ between two retrievals within the session: **retain both**, record
both checksums, record the times, and classify as `CONFLICT` pending §12.3 treatment. **Do not
overwrite, and do not silently prefer either copy.**

### 13.7 Checksum verification

`SHA256SUMS` generated after every retention batch, verified with `sha256sum -c` at `R3a` and again
at `R10`. **A mismatch is a STOP condition.**

---

## 14. Provenance schema

Per-entry fields for `PROVENANCE.md`, fixed before research:

| Field | Notes |
| ----- | ----- |
| Evidence ID | `O4-D…` / `O4-M…` / `O4-X…` |
| Candidate applicability | List, plus **established / hypothesised** |
| Publisher / authority | |
| Title / document identity | As the document states it |
| Document class | Per §8.3 |
| Document date | As stated in the document |
| Effective date | **Only if established**; otherwise "not established" |
| Version | As stated |
| Source locator | The publisher path used |
| Retrieval date | |
| Local normalized filename | Per §13.2 |
| Byte size | |
| SHA-256 | |
| Evidence tier | Tier 1 / 2 / 3 |
| Primary / secondary | |
| Supersession relationship | Supersedes / superseded by; **established or inferred** |
| Extraction method | If text extraction was used |
| Retrieval caveat | |
| Accessibility caveat | |
| Integrity caveat | Including any redaction, disclosed |
| Research role | Which of the eight §3.3 determinations it bears on |

Plus store-level headers: retention date; the access-conditions statement; the storage-location
**ratification-pending** notice; and the missing inventory.

> **No value in this schema is populated by this planning task.**

---

## 15. Preservation-before-interpretation rule

**Adopted** for primary documents:

```
retrieve → preserve → checksum → provenance entry → inspect / extract → characterize
         → use in methodology-chain reasoning
```

Rationale: it prevents chain reasoning from resting on transient material that was never retained,
which would make the finding unreproducible. It is enforced structurally by the `R3a` checkpoint.

### 15.1 Defined exception — discovery surfaces

**Listing pages, search-result pages, and index/navigation pages** used only to *locate* a document
need not be retained in full, **provided that**:

1. nothing they show is used as substantive evidence — they establish **no** fact about the chain;
2. the locator they yielded is recorded in Table C;
3. if such a page is the **only** evidence for a fact — for example that a version exists, or that
   one document supersedes another — the exception **does not apply** and the page **must** be
   retained, checksummed and provenance-recorded like any primary document.

**The exception is for navigation only.** The moment a discovery surface becomes evidence, it is
evidence.

---

## 16. Publication boundary

The eventual repository artifact carries **only the minimum documentary characterization** needed to
support the `O-4` result.

### 16.1 Must NOT enter Git

Raw publisher documents; raw publisher webpages; raw historical values of any kind; source files;
checksums and `SHA256SUMS`; the provenance index; external local paths; credentials; cookies; session
data; token-bearing URLs; unnecessary source quotations; scratch extraction output.

### 16.2 MAY enter the eventual repository evidence artifact

Bounded **paraphrased** documentary findings; evidence IDs; methodology-version relationships;
effective-date characterizations where publication-safe; gap classifications; candidate
applicability; the per-candidate `O-4` result; limitations; and handoffs.

### 16.3 Existing controls preserved, not weakened

The **Stage-F publication boundary is unchanged**: redistribution terms remain **UNCLEAR**, the
**fail-closed publication policy applies**, and nothing is cleared for republication. Where a
publisher clause is itself the evidence, the minimum necessary quotation is permitted; otherwise
publisher wording is **characterised, not reproduced**.

---

## 17. `O-4` result decision procedure

The only approved states are **`O4-ESTABLISHED`**, **`O4-PARTIAL`**, **`O4-NOT-ESTABLISHED`**.
Applied **per candidate**. Conservative by construction.

### 17.1 `O4-ESTABLISHED` — all conditions required

> **Not satisfied merely because several methodology documents were found.**

1. A controlling methodology is established for **every interval** of the bounded span — no `GAP-7`.
2. **Every methodology change effective within the span is identified and dated** from Tier 1 or
   `G-OD-08` issuer-side primary evidence — **or** it is authoritatively established that no such
   change occurred.
3. The version sequence can be **ordered**, and supersession between successive versions is
   **established**, not merely inferred — no material `GAP-4`.
4. **Candidate applicability is established** for that candidate across every interval, from scope
   statements — no `GAP-5` / `GAP-6` for that candidate.
5. **No `GAP-8` conflict** bears on the chain.
6. §12 exhaustion reached `SEARCH-COMPLETE` for every search line bearing on that candidate.
7. No conclusion rests on secondary material.

### 17.2 `O4-PARTIAL`

Material documentary evidence exists, but one or more bounded gaps prevent a determinate `HG-8`
application. **The report must identify the exact gap or gaps** — by class, by interval, by
candidate, and by which of the eight §3.3 determinations each blocks.

### 17.3 `O4-NOT-ESTABLISHED`

The authorized search protocol **completed** without establishing the required continuity. The report
must state **which protocol was executed**, **which lookup steps were performed**, and **why the
chain was not established**.

> It does **not** mean no methodology change occurred; that no chain exists; or that the publisher
> issued no such documents. **It is a statement about the search performed, not about the world.**

### 17.4 Mandatory non-mappings

> **None of the three states maps to `HG-8` PASS or FAIL**, to candidate qualification or
> disqualification, to `P1-2`, or to Primary Proxy selection. **`HG-8` is not evaluated.**

`O4-PARTIAL` and `O4-NOT-ESTABLISHED` both leave **`O-4` OPEN**. Only `O4-ESTABLISHED` could support
a later Owner act on the open-items register — **an Owner act, not a research output**.

### 17.5 Tie-break

Where a candidate sits between two states, the **more conservative** state is recorded.

---

## 18. Candidate-level versus route-level reporting

**Reporting is candidate-level and primary; family-level findings are secondary and subordinate.**

```
For each of NDXJPY, XNDXJPY, XNDXNNRJPY — independently:
    chain table · gap register · §12 exhaustion record · O4-* result · limitations

Then, optionally:
    Shared methodology-family finding — documents whose scope statements
    were established to cover more than one candidate, with the
    applicability evidence for each
```

**Binding constraint:**

> **A family-level conclusion may never hide a candidate-specific gap.** If the three results differ,
> they are reported as differing. If a shared document's applicability is established for two
> candidates and hypothesised for the third, the third records a `GAP-5` — it does not inherit the
> conclusion.

Identical results across the three are reported as identical **only where they rest on an identical
established evidence base**, per the precedent already set for `HG-9` and the bounded Stage-G
reapplication.

---

## 19. Anti-circularity controls

### 19.1 The thirteen operational prohibitions

Execution must not: move the research floor; move `K1`; change **P-A**; derive `P1-5` opportunistically;
select `P1-6`; change the evidence hierarchy after seeing results; change search-exhaustion rules
after seeing results; drop or under-search a candidate because its chain is inconvenient; prefer a
methodology version because it improves performance; use empirical performance to establish
documentary continuity; convert **D-10** into a hard gate; treat methodology continuity as proof of
**`H-1`**; or silently widen `O-4` into historical-value research.

Each is a **STOP** condition, not an adjustment.

> **On `H-1`:** methodology continuity and live status are different propositions. Establishing that
> a documented methodology governed a period says nothing about whether values for that period were
> calculated and disseminated in real time. `SC6-OD-05`'s distinction remains mandatory.

> **On D-10:** it remains the study-level OD-12 evidentiary standard. `O-4` resolution would address
> **D-10 condition 3 only**; conditions 1, 5 and 6 would remain. `HG-8` remains the sole remaining
> qualification-blocking gate.

### 19.2 Named-rule operationalization

| Rule | How this plan enforces it |
| ---- | ------------------------- |
| **`AC-1`** | Span, hierarchy, protocol, exhaustion criteria, gap taxonomy and result procedure are **all fixed in this plan, before evidence**. Changing any of them mid-execution is `OWNER-ESCALATION` |
| **`AC-2`** | No phase computes any quantity. Any apparent need for arithmetic is a §20 STOP |
| **`AC-3`** | `ND-1 … ND-7` are not inputs to any phase |
| **`AC-4`** | §12.4 requires equal search depth for all three candidates; §18 forbids hiding a candidate gap behind a family conclusion |
| **`AC-5`** | No phase derives a date for `P1-5`. Effective dates discovered are **document facts**, not start dates |
| **`AC-6`** | Point-in-time discipline untouched; `HG9-OD-10` obligation survives |
| **`AC-8`** | No scoring, weighting, or ranking of candidates or of evidence |
| **Invariant 17** | No Baseline parameter is set by this research |
| **`SC-17`** | No step selects a proxy on strategy performance; no `ND-n` is a discriminator |
| **`SC-18`** | Any need to change a frozen criterion, the principle, the floor, or `K1` → **STOP** |
| **`SC-19`** | No prior finding may be narrowed, withdrawn, or downgraded. `N-3`, `O-2`, `O-5`, the `SC-6` determination, D-6 and D-8 are preserved as recorded |

---

## 20. Execution stop conditions

Execution **STOPS and returns to Owner Review** if proceeding would require:

1. changing the **Frozen Baseline**;
2. changing the **frozen qualification criteria**;
3. changing the **authorized research span**;
4. changing **`K1`**;
5. changing the **`P1-5` principle**;
6. selecting **`P1-6`**;
7. introducing a **new hard gate**;
8. exercising **`OJ-1` or `OJ-6`**;
9. **purchasing data**;
10. **creating an account**;
11. **requesting entitlement**;
12. **accepting publisher contractual terms** not already covered by the authorization;
13. using an **unapproved secondary-source class** as substantive evidence;
14. **historical-value retrieval**;
15. **empirical fit / performance analysis**;
16. resolving a **material primary-source conflict by discretion**;
17. **modifying an existing evidence or decision artifact**.

### 20.1 Additional stop conditions identified during this planning review

| # | Condition | Basis |
| - | --------- | ----- |
| 18 | A methodology change is known to have occurred but **cannot be dated** | **`SC-4`** |
| 19 | The methodology chain proves **not reconstructable** | **`SC-3`** |
| 20 | A **retrieval-integrity hazard** is detected — a source returning a plausible wrong result instead of an error | **`SC-15`** |
| 21 | **Automated retrieval** would be required where no readable access policy permits it | **`SC-14`** |
| 22 | A determination would require **analysing observation values** | **`SC-16`**, D-5 |
| 23 | **Arithmetic** appears necessary to answer a determination | S.2; the `G-OD-11` discipline |
| 24 | **Entitlement-gated evidence** appears necessary | **D-9**, with its return clause: exact evidence required, why, route, expected cost if known, licensing implications, non-commercial alternative |
| 25 | A **checksum mismatch** occurs, or a source changes between retrievals within the session | §13.6, §13.7 |
| 26 | A source requires **declaring a contact identity** to permit automated access | The Stage-C position: the path was not used and **no identity was invented** |
| 27 | Resolving `O-2`, `O-3`, `O-5`, `O-6`, `O-7`, or C-2A would be required to answer an `O-4` determination | Those items are **outside this authorization** |

> **A stop is a valid, reportable outcome.** It is not a failure, and it must not be worked around.

---

## 21. Future execution-report contract

After actual research, the execution task must return **A–V** and **STOP**:

| § | Required content |
| - | ---------------- |
| **A** | Research protocol **actually executed** — phase by phase, including any phase not reached |
| **B** | **External-access actions performed** — every retrieval, with route and outcome |
| **C** | Candidate-by-candidate **source inventory** (Table A) |
| **D** | **Retained / missing / inaccessible** inventory (Table D) |
| **E** | **Checksum / provenance verification** result |
| **F** | **Methodology-version chain per candidate** (Table B) |
| **G** | **Effective-date findings**, with the evidence class for each |
| **H** | **Transition / supersession findings**, marked established or inferred |
| **I** | **Documentary gaps**, by class, interval and candidate |
| **J** | **Search-exhaustion result** (Table C), with the §12.3 state for every line |
| **K** | **Candidate-level `O-4` result** — `O4-ESTABLISHED` / `O4-PARTIAL` / `O4-NOT-ESTABLISHED`, per candidate |
| **L** | **Limitations** |
| **M** | **Publication-boundary verification** |
| **N** | **External-store integrity** |
| **O** | **Frozen Baseline / criteria-freeze integrity** |
| **P** | **`P1-5` / `P1-6` preservation** — principle unchanged, date not derived, `P1-6` not selected |
| **Q** | **`HG-8` unchanged and NOT reapplied** |
| **R** | **`H-1` unchanged — NOT ESTABLISHED** |
| **S** | **`P1-6` supplementary-check obligation** restated |
| **T** | **Proposed repository artifacts, if any** — as drafts only |
| **U** | **git status** |
| **V** | **Explicit STOP for Owner Review** |

> **The execution task must NOT automatically commit its research findings.** Any repository artifact
> it produces is a **draft** pending separate Owner approval.

---

## 22. Preserved governance state

| Item | State |
| ---- | ----- |
| **Frozen Phase-0 Baseline** | **UNCHANGED** — OD-01 … OD-14 untouched |
| **Criteria freeze** | **UNCHANGED** — `1e8bc85` |
| `O-4` | **OPEN** — research **AUTHORIZED BUT NOT YET EXECUTED** |
| `O-4` Research Cutoff | **`K1` = 2026-08-13 — IMMUTABLE**, semantics **S-A** |
| Research floor | `OD-P15-06` Base Value Date scoping floor — **narrow semantics unchanged** |
| `P1-5` | **OPEN** — principle **P-A**; date **NOT YET DERIVED** |
| `P1-6` | **OPEN** |
| `HG-8`, C-1 ×3 | **NOT EVALUABLE** — **not reapplied** |
| `HG-6`, C-1 ×3 | **PASS** |
| `HG-9`, C-1 ×3 | **PASS**, with recorded limitations |
| `HG-12`, C-1 ×3 | **PASS**, with recorded conditions |
| `HG-11`, C-1 ×3 | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED**; not PASS; non-eliminating; carried to `OJ-6` |
| `H-1` | **NOT ESTABLISHED** |
| `P1-9` | **PARTIAL** |
| **D-6, D-8, D-9, D-10** | **UNCHANGED** |
| C-1 classification | **QUALIFICATION INCOMPLETE** ×3 |
| C-2A | **UNCHANGED** — outside this plan |
| `OJ-1` | **NOT REACHED — DEFERRED** · `OJ-6` **unexercised** |
| `P1-2` | **OPEN** — no Primary Proxy approved |
| Stage G | **OPEN** · Stage H **NOT BEGUN** · Phase 2 **BLOCKED** |

---

## 23. Owner approval boundary

> **THIS PLAN IS NOT EXECUTABLE MERELY BECAUSE IT HAS BEEN DRAFTED.**

The existing authorization permits bounded `O-4` research **in principle**. This planning boundary
controls **how** that authorized research is executed.

> **No external research may begin until the Owner has reviewed and explicitly approved this
> Execution Plan.**

### 23.1 `K1` is unaffected by this plan

> **`K1` remains 2026-08-13** regardless of when this plan is drafted, reviewed, committed, or
> executed.

This planning review is **not** a reinterpretation of `K1`, does not move it, and does not restart
it. `K1` was fixed by explicit Owner approval of the authorization under **S-A**, and only an
explicit Owner Decision under `SC-18` could change it.

### 23.2 What was NOT done in drafting this plan

**No external network access of any kind.** No browsing; no WebSearch or WebFetch; no `curl`, `wget`,
or browser automation; no publisher, search-engine, archive, or API access; no URL or endpoint
testing; no document-availability checking; no publisher contact; no login; no account; no entitlement
request; no purchase. **No `O-4` evidence was gathered**, **no external `O-4` store was created**, and
no repository artifact was modified.

---

**End of Research Execution Plan — DRAFT, NOT APPROVED FOR EXECUTION. Span: `OD-P15-06` floor →
`K1` = 2026-08-13, both immutable. Phases `R0 … R10` with an inserted `R3a` preservation checkpoint;
external access in `R3` and `R4` only. Result vocabulary `O4-ESTABLISHED` / `O4-PARTIAL` /
`O4-NOT-ESTABLISHED`, **none mapping to `HG-8`**. `HG-8`: **NOT EVALUABLE** ×3, not reapplied.
`O-4`: **OPEN**. `P1-5`: **OPEN**, principle **P-A**, date **NOT YET DERIVED**. `P1-6`: **OPEN**.
`H-1`: **NOT ESTABLISHED**. `OJ-1`: **NOT REACHED — DEFERRED**. Candidates: **QUALIFICATION
INCOMPLETE**. Stage G: **OPEN**. Primary Proxy: **NOT APPROVED — P1-2 remains OPEN**. Phase 2:
**BLOCKED**.**
