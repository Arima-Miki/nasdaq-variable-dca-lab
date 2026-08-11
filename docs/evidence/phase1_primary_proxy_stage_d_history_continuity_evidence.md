# Phase 1 Evidence Artifact — Primary Proxy Qualification, Stage D: History, Continuity, and Pre-Launch Qualification

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Primary Proxy Candidate Qualification — Stage D** |
| Research date | **2026-08-11** (all source access dates 2026-08-11) |
| Authorising decisions | Study design [`phase1_primary_proxy_qualification_study_decision.md`](../decisions/phase1_primary_proxy_qualification_study_decision.md) (criteria frozen at `1e8bc85`); Stage-D Owner Decisions **D-1 … D-5** |
| Closure decision | [`phase1_primary_proxy_stage_d_closure_decision.md`](../decisions/phase1_primary_proxy_stage_d_closure_decision.md) (**D-6 … D-12**) |
| Owner Review | **PENDING — prepared for Owner Review** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Publication classification | **PUBLIC QUALITATIVE EVIDENCE** — dates, observation counts, segment classifications and documentary findings only |
| Historical values | **NONE PUBLISHED.** No observation value, and no incidentally returned value, appears in this artifact |
| Source material | Retained **outside** the repository. No publisher file, date-spine file, provenance index, or checksum file enters Git |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| `OJ-1` | **NOT REACHED — DEFERRED** (see [§8](#8-oj-1-disposition)) |
| Phase 2 | **BLOCKED** |

> **What this artifact is.** The record of what Stage D *researched and found* about candidate
> history, continuity, and pre-launch status. It classifies segments and records access limits. It
> qualifies no candidate, passes or fails no gate, approves no Primary Proxy, selects no start date
> or cutoff, and decides no admissibility question.

> **On repository entry at Stage D.** The frozen study design records `Repository entry: Nothing`
> for Stages A–G. This artifact exists because the Owner **explicitly directed** a durable Stage-D
> closure record. That is an Owner-authorized deviation, recorded rather than made silently. It does
> **not** amend the frozen study design, and Stage H's obligations are unchanged. The same deviation
> was recorded at Stage C.

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and does not
govern Baseline behavior. The frozen criteria — `HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`,
`OJ-1 … OJ-6`, `SC-1 … SC-20`, handoffs `H-1 … H-8` and rules `R-1 … R-4` — are fixed by the study
design and are **used, never amended, here**. Stage-C findings are recorded in
[`phase1_primary_proxy_stage_c_methodology_evidence.md`](phase1_primary_proxy_stage_c_methodology_evidence.md)
and remain authoritative for their own stage; this artifact is **additive** and does not rewrite
them.

This artifact is written to be self-contained. A future researcher with no access to the research
session should be able to establish what was investigated, what was found, what could not be
established, and why, from this file alone.

---

## 2. Research objective

Stage D asks one question per candidate, and deliberately only this one:

> **What history exists, what is its status, is it continuous, and can its boundaries be
> established from primary publisher evidence?**

The governing rule throughout, from the frozen study design §6.1:

> **"Available history" MUST NOT be interpreted as "admissible history."**

Stage D establishes documentary and structural facts. **It does not decide admissibility.**

### 2.1 Owner Decisions governing this execution

| # | Effect on Stage D |
| - | ----------------- |
| **D-1** | C-2A proceeds without first resolving `O-3`; the QQQ component is investigated only so far as facts can be established without choosing a NAV basis; the FX leg is **UNRESOLVED-BY-DESIGN**, and its absence is **not** a qualification failure |
| **D-2** | Methodology version/change-history retrieval authorized strictly for `HG-8` continuity work; not a reopening of Stage C |
| **D-3** | Evidence for `HG-6`, `HG-7`, `HG-9`, `HG-12` may be gathered where it arises naturally; **no gate is evaluated at Stage D** |
| **D-4** | The §6.6 OD-12 evidentiary standard is drafted here and put to the Owner; **never declared satisfied** |
| **D-5** | Incidental value return does not itself trigger `SC-16`; retrieval is not analysis; `SC-16` triggers only if a determination would require **analysing** values |

---

## 3. Candidate scope as executed

Carried **symmetrically** at every step, per `AC-4` and study design §4.1.

| Route | Scope at Stage D |
| ----- | ---------------- |
| C-1 `NDXJPY` | Full Stage-D investigation |
| C-1 `XNDXJPY` | Full Stage-D investigation |
| C-1 `XNDXNNRJPY` | Full Stage-D investigation |
| C-2A | QQQ component only, bounded by **D-1** |
| C-2B | Does not advance — dropped at Stage-C closure |
| C-3 | Out of scope by the frozen study design |

No candidate was dropped, narrowed, or deprioritised for difficulty of evidence.

---

## 4. Source inventory

New at Stage D. Evidence classes follow the established tiering (PRIMARY / NEAR-PRIMARY /
SECONDARY / UNREAD).

| # | Source | Publisher | What it establishes | Class | Locator |
| - | ------ | --------- | ------------------- | ----- | ------- |
| **E-1 … E-3** | Per-index historical data files, one per JPY series | Nasdaq | The date spine of the pre-base-date segment; the publisher's generic characterization statement | PRIMARY | `indexes.nasdaqomx.com/docs/AdditionalData_<symbol>.csv` |
| **E-4 … E-6** | Index Overview pages, one per JPY series | Nasdaq | Index currency, base value, component count; the same characterization statement; **the absence of any launch-date field** | PRIMARY | `indexes.nasdaqomx.com/Index/Overview/<symbol>` |
| **E-7** | Nasdaq-100 Index Consultation — February 2026 | Nasdaq | Proposed methodology changes and their implementation sequencing | PRIMARY (proposal stage) | `indexes.nasdaqomx.com/docs/NDX_Consultation-February_2026.pdf` |
| **E-8** | Site disclaimer page | Nasdaq | **Negative finding** — does not carry the historical-status language | PRIMARY | `indexes.nasdaqomx.com/Home/Disclaimer` |
| **E-9** | Index dates register | Nasdaq | **Negative finding** — carries no launch dates for the JPY series | PRIMARY | `indexes.nasdaqomx.com/Home/IndexDates` |
| **E-10** | `robots.txt` | Nasdaq | A readable automated-access policy that does not disallow the paths used | PRIMARY | `indexes.nasdaqomx.com/robots.txt` |
| **S-1 … S-3** | Date spines, **dates only** | derived | Observation dates, counts, gap structure | DERIVED | derived from E-1 … E-3; retained outside the repository |

Carried forward from Stage C and relied upon here: the NDX version register (base value dates), the
Recalculation Policy, the NDX Index Methodology, and the QQQ prospectus and SAI.

---

## 5. C-1 — what was established

### 5.1 Base Value Date

All three JPY series share a published **Base Value Date of 2020-06-29**, with a published base
value, from the Nasdaq version register (PRIMARY).

> **A Base Value Date is not a launch date.** Nothing in this artifact treats it as evidence of
> launch, of live status, or of back-tested status. That inference is expressly not drawn.

### 5.2 The publicly available historical segment

| Series | Earliest available observation | Latest available observation | Observations |
| ------ | ------------------------------ | ---------------------------- | ------------ |
| `NDXJPY` | **1985-01-31** | **2020-06-26** | 8,926 |
| `XNDXJPY` | **1999-03-04** | **2020-06-26** | 5,366 |
| `XNDXNNRJPY` | **2007-07-09** | **2020-06-26** | 3,268 |

Three structural facts, each established from dates alone:

1. The publicly available file for each series **ends before the Base Value Date**. The publicly
   available material therefore covers **only** the pre-base-date period.
2. The three earliest dates **differ per series** and are not a common family start.
3. The three spines are **exactly identical over their overlapping ranges** — zero dates missing,
   zero extra. The C-1 family shares one calendar.

### 5.3 Calendar and gap structure

- All spines are **weekday-only**; no weekend observations appear.
- Missing weekdays run **8–10 per year**, consistent with the governing methodology's rule that the
  Index is calculated Monday through Friday except when US markets are closed.
- Every year with an elevated count corresponds to a known additional US market closure. The two
  longest gaps in the longest spine are a **7-day gap in September 2001** and a **5-day gap spanning
  the 2006/2007 year end**; **2012** and **2018** also show one elevated year each.

> **No unexplained discontinuity was found. `SC-8` is NOT triggered.**

### 5.4 The live segment

The live segment (from the Base Value Date onward) is **not publicly retrievable**. Nasdaq's
publicly accessible material offers only the pre-base-date file; live history is delivered through
entitlement-gated channels — a web interface requiring login, an SFTP delivery service, and a
commercial real-time feed.

`robots.txt` is readable and does **not** disallow any path used, so the barrier is **entitlement,
not automated-access policy**.

> **`SC-14` is NOT triggered.**

---

## 6. Pre-launch characterization evidence

The only characterization located is a **generic, site-wide** statement appearing identically on the
data files and the overview pages. Its evidentiary core:

> "Nasdaq provides either actual historical index values or back-tested histories for certain
> indexes. All back-tested index values for periods prior to the launch date of an index are merely
> indicative, and they are provided "AS IS" for informational and educational purposes only."

The remainder disclaims accuracy, timeliness, completeness and fitness for purpose for index values
"either historical or back-tested," disclaims investment advice, and notes that past performance is
not indicative of future results.

**What this establishes.** That back-tested histories exist in Nasdaq's catalogue; that they cover
periods prior to an index's launch date; and how Nasdaq qualifies them.

**What it does not establish.** It does **not** state which of the two categories applies to the
pre-base-date segment of these three series. It names no series and no segment. Nasdaq's dedicated
disclaimer page carries no such language, and its index-dates register publishes no launch dates for
these series.

Consequently the **launch date of each JPY series is unestablished**, and with it the boundary
between live and non-live history.

### 6.1 Status of the prior "live since 2020-06" statement

The study design §6.3 records that this statement appears in an approved artifact **without a cited
primary source**, and requires it to be re-established from primary publisher material and treated
as unconfirmed until then.

> **It was NOT re-established.** What is established is the Base Value Date. The available data
> ending immediately before that date is *consistent* with the prior statement, but consistency is
> not confirmation, and per **D-6** structural consistency must not be used to infer status. The
> statement remains **unconfirmed**.

---

## 7. Segment maps

Per the mandatory three-way classification in the frozen study design §6.4, and per Owner Decision
**D-6**.

### 7.1 C-1 — identical structure for all three series

| Segment | Range | Class |
| ------- | ----- | ----- |
| Pre-base-date | earliest available (per §5.2) → **2020-06-26** | **NON-LIVE, UNCHARACTERIZED** |
| Base-date onward | **2020-06-29** → present | **NOT ESTABLISHED.** Presumed live, but presumption is not evidence; spine **ACCESS-LIMITED** |

> **`SC-6` is TRIGGERED** for the pre-base-date segments of `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY`.
>
> Under §6.4 those segments **may not be used** — for measured performance, for Reference-High
> warm-up, or for candidate qualification requiring admissible history. §6.4 states this is "not a
> licence to use it cautiously."
>
> **This is a segment-level exclusion on evidentiary grounds. It is NOT a finding that the
> publisher's historical values are wrong, or that its methodology is invalid.**

The classification rests on the absence of segment-specific publisher evidence. Per **D-6**, status
was **not** inferred from availability, from the file boundary, from the Base Value Date, or from
structural consistency with the prior repository statement. If future authoritative primary evidence
characterizes these segments specifically, the classification may be revisited through explicit
Owner Review **without rewriting this finding**.

### 7.2 C-2A

**No segment map can be produced.** Documentary boundaries are established (§9), but no observation
spine was retrieved, and the FX leg is UNRESOLVED-BY-DESIGN. Route-level continuity is therefore
**not declarable**. Per **D-1**, this is **not** recorded as a qualification failure.

---

## 8. `OJ-1` disposition

> **`OJ-1` — NOT REACHED. DEFERRED — no qualified NON-LIVE CHARACTERIZED segment is presently
> available for Owner admissibility judgment.**

`SC-6` excludes the affected C-1 segments **before** `OJ-1` is reached, so the three §6.5 questions —
non-live history for measured performance, for Reference-High warm-up only, or for neither — are
**not put to the Owner at this time** and none is chosen.

If later primary evidence moves a segment from NON-LIVE, UNCHARACTERIZED to NON-LIVE, CHARACTERIZED,
that segment returns to the Owner for `OJ-1`. **No admissibility decision is silently inherited.**

---

## 9. C-2A — QQQ component findings

Established from primary Invesco evidence:

| Fact | Value | Source |
| ---- | ----- | ------ |
| Trust formation | Formed as NASDAQ-100 Trust, Series 1 and **organized as a New York trust on 1999-03-04** | SAI, PRIMARY |
| Indenture amendment | Initial Trust Indenture **amended 2007-03-21** by the current adviser | SAI, PRIMARY |
| Reclassification (**N-2**) | UIT prior to market close **2025-12-19**; owners approved indenture amendments that day, implemented **after market close 2025-12-19**, changing the 1940-Act classification to an **open-end management investment company** | SAI, PRIMARY |
| Publisher-described continuity | Same investment objective and **substantially similar investment policies, but differing expenses**, when operating as a UIT; returns prior to the Reclassification reflect operation as a UIT | Prospectus, PRIMARY |
| Governance | The Board is **newly constituted** following the Reclassification | SAI, PRIMARY |
| NAV calculation calendar | NAV struck each day the NYSE is open, normally at 16:00 ET | Prospectus / SAI, PRIMARY |

**N-2 assessment.** The break is **dated, documented, and accompanied by a publisher continuity
description** — `HG-8`-compatible in kind. Per the Stage-D authorization, the **embedded-expense**,
**return-composition**, and **OD-11** implications are **NOT resolved here** and are handed to
Stage E.

**`O-3` remains OPEN.** No Stage-D determination required choosing between financial-reporting NAV
and shareholder-transaction NAV, and none was made. No Stage-D fact was found to diverge by NAV
basis, so **D-1**'s "record the divergence and stop that determination" path was not reached.

**FX leg: UNRESOLVED-BY-DESIGN.** No USD/JPY source or convention was selected, constructed,
inferred, or approved, and no synthetic JPY series was constructed.

---

## 10. Methodology-change findings

### 10.1 N-3 — the change effective 2026-05-01

| Element | Status |
| ------- | ------ |
| Effective date | **2026-05-01** — established from primary **fund-issuer** evidence (a prospectus supplement dated 2026-04-30) |
| Publisher-side documentation | The February 2026 Nasdaq consultation (**E-7**) — a **proposal**, covering market-capitalisation treatment for eligibility, a fast-entry rule for large new listings, and moving ad-hoc share-count and float adjustments into scheduled rebalances. It states changes would be implemented after the March 2026 quarterly rebalance and **does not state the 2026-05-01 date** |
| Affected scope | The Nasdaq-100 Index and related indexes — therefore **all three C-1 series and the QQQ underlying index** |
| Publisher final decision document | **NOT LOCATED** after bounded search |

**Assessment.** The change is **dated**, so `SC-4` is not triggered; a methodology chain exists, so
`SC-3` is not triggered. But the chain is assembled from an index-publisher *proposal* plus a
*fund-issuer* confirmation rather than from a single publisher decision document.

> **This is carried forward as an OPEN provenance gap.** No closure is manufactured, and no
> before-versus-after performance comparison was made or is possible under this study's rules.

### 10.2 Methodology version history

Owner Decision **D-2** authorized retrieval of methodology version and change-history documents.
**None was located** — no superseded methodology version and no publisher change log was found at
any accessible location. Stage-C item `O-4` therefore **remains open despite the authorization**.

The current methodology document carries a file creation date immediately preceding the stated
2026-05-01 effective date, which is *consistent* with publication for that change. Recorded as
consistency only — not as proof — since that document carries no in-body effective date (`O-5`).

---

## 11. H-1 … H-8 handoff facts

| | `NDXJPY` | `XNDXJPY` | `XNDXNNRJPY` | C-2A (QQQ component) |
| --- | --- | --- | --- | --- |
| **H-1** earliest LIVE observation | **NOT ESTABLISHED** | **NOT ESTABLISHED** | **NOT ESTABLISHED** | **NOT ESTABLISHED** as a series; Trust organized 1999-03-04 |
| **H-2** earliest available observation | 1985-01-31 | 1999-03-04 | 2007-07-09 | Not retrieved (D-1 scope) |
| **H-3** segment map | §7.1 | §7.1 | §7.1 | Not producible — §7.2 |
| **H-4** dated methodology changes | N-3; no version history (§10.2) | same | same | 2007-03-21 amendment; 2025-12-19 reclassification |
| **H-5** gaps / calendar | §5.3 | §5.3 | §5.3 | Documentary calendar rule only (§9) |
| **H-6** warm-up availability | §12 | §12 | §12 | Not established |
| **H-7** revision / restatement | Policy established at Stage C; **no restatement event log located** for the span | same | same | Not established |
| **H-8** integrity hazards | §13 | §13 | §13 | §13 |

**No start-date rule was selected.** `R-1 … R-4` remain candidate rules only; `AC-5` holds — the
start date is derived from a rule the Owner selects, never chosen by this study. **P1-5 remains
OPEN.**

---

## 12. Warm-up finding

Warm-up observations for the C-1 family exist **only within the pre-base-date segment**. Because
`SC-6` excludes that segment, the three §6.5 admissibility questions are **not independent** for
C-1: with the segment excluded, **no warm-up data is available at all**, and a Reference High would
have to be seeded from within the measured period itself.

The study design §6.5 hazard is recorded as **concrete rather than theoretical**: the excluded
segment spans multiple market cycles, so were it back-tested and later admitted even for warm-up
only, a hindsight-influenced peak could seed a Reference High **that never actually stood**,
affecting every subsequent drawdown zone — a look-ahead concern under spec §6 even in warm-up-only
use.

**Surfaced, not decided.**

---

## 13. Evidence gathered for `HG-6`, `HG-7`, `HG-9`, `HG-12`

Gathered under **D-3**. **No gate is evaluated here**; final evaluation remains Stage G.

| Gate | Evidence recorded |
| ---- | ----------------- |
| `HG-6` | The evidenced spine supports a daily-close Reference High. The §6.5 warm-up hazard above is the material open risk |
| `HG-7` | Drawdown zones are derivable from a single series on the evidenced spine; no additional input is required |
| `HG-9` | Restatement policy established at Stage C — EOD values may be restated, subject to a stated materiality threshold and reserved discretion. **No restatement event log for the candidate span was located** |
| `HG-12` | The pre-base-date file is a static, re-downloadable artifact and is checksummed in the external record, so that segment is pinnable. The live segment's pinnability is **unestablished**, being access-limited |

---

## 14. Incidental-value handling

Recorded per `S.2`'s minimisation rule and Owner Decision **D-5**.

- The per-index data files could not supply date-spine metadata without also returning observation
  values in an adjacent column. **The value column was not analysed.** Every derived artifact
  contains **dates only**.
- One value was *observed* in the course of identifying a segment boundary. It was **not relied
  upon** — the boundary was established from **dates alone**. It is recorded here as an incidental
  observation and is **not reproduced**, consistent with the publication boundary.
- The overview pages display current-day index values as ordinary page furniture. Not recorded, not
  used.
- **`SC-16` is NOT triggered.** No determination required analysing values. Retrieval is not
  analysis.

---

## 15. Anti-circularity verification

- **Zero value-derived computation.** No returns, cumulative or annualized returns, correlations,
  regressions, tracking error, RMSE, MAE, volatility, drawdowns, drawdown zones, level-similarity
  measures, performance comparisons, or strategy outcomes.
- All arithmetic performed was on **dates**: counts, differences, weekday classification, and set
  comparison. §7.1 of the study design fixes this line exactly — counting observations is
  permitted; computing anything from their values is not.
- **`ND-1 … ND-7` were not used.**
- `AC-1 … AC-8` maintained. In particular `AC-4`: the three C-1 series were carried identically at
  every step, and no candidate was preferred on history length.
- **No as-of date was required, so no Primary Proxy Qualification Research Cutoff was declared.**
  Nothing here bears on **P1-6**.

---

## 16. Publication and external-material boundary

- **No historical value is published here** — not from the spine, not incidental.
- **No publisher data file, date-spine file, provenance index, or checksum file enters Git.** All
  source material is retained **structurally outside** the repository, not in an ignored repository
  directory.
- Publisher text is quoted only where the clause is itself the evidence — the characterization
  statement in §6, on which the `SC-6` determination turns.
- **Redistribution terms remain unassessed** for every source used. Licensing is Stage-F work
  (`HG-11`), so fail-closed treatment applies and nothing is cleared for republication.
- Provenance sufficient for independent re-retrieval — publisher, item, locator, evidence class,
  and caveats — is recorded in §4 and in the external provenance index.

---

## 17. What this artifact establishes

1. The C-1 family's publicly available history covers **only the pre-base-date period**, with
   per-series start dates of 1985-01-31, 1999-03-04 and 2007-07-09, ending 2020-06-26.
2. That segment is **structurally clean**: weekday-only, with a gap structure fully explicable
   against the published calculation rule, and an identical calendar across all three series.
3. Nasdaq's characterization of pre-launch history is **generic and does not name these segments**,
   and **no launch date is published** for any of the three series.
4. Those segments are therefore **NON-LIVE, UNCHARACTERIZED**, and **`SC-6` is triggered**.
5. The live segment is **access-limited**, not unprovenanced; `SC-14` and `SC-5` are not triggered.
6. QQQ's structural break is **dated, documented, and continuity-described**.
7. The 2026-05-01 methodology change is **dated**, with an **open publisher-side provenance gap**.

## 18. What this artifact does NOT establish

1. That any candidate passes or fails `HG-8`, or any other gate. **No gate was evaluated.**
2. The **launch date** or first live observation of any C-1 series.
3. That the pre-base-date segment is back-tested — only that its status is **unestablished**.
4. That the pre-base-date segment is wrong, unreliable, or methodologically invalid. It is
   **excluded on evidentiary grounds**, not impugned.
5. That the post-base-date segment is live — it is **presumed** live, and presumption is not
   evidence.
6. Any admissibility conclusion. `OJ-1` was **not reached**.
7. That any candidate satisfies the OD-12 evidentiary standard.
8. Any comparison, ranking, or preference between candidates.

---

## 19. Phase-1 requirement impact

No item is upgraded merely because this artifact exists.
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements)
remains the authoritative register.

| # | Requirement | Status | Basis |
| - | ----------- | ------ | ----- |
| **P1-2** | Approved Primary Proxy | **OPEN** | No candidate qualified, ranked, or approved |
| **P1-5** | Baseline start date | **OPEN** | Facts handed over; **no date and no rule selected**. Materially constrained by `SC-6` |
| **P1-6** | Baseline Dataset Cutoff | **OPEN** | No cutoff, and no research cutoff, was declared |
| **P1-9** | Revision / restatement behaviour | **PARTIAL — unchanged** | Policy known from Stage C; **no event log located** for the candidate span |
| **P1-4** | Cost / expense treatment | **Unchanged** | N-2's differing-expense finding is a Stage-E handoff, not resolved here |
| **P1-8** | Licensing / redistribution | **Unchanged** | Not Stage-D work; all sources remain unassessed |

---

## 20. Handoffs

| To | Item |
| -- | ---- |
| **Stage E** | N-2's embedded-expense and return-composition implications, including OD-11 treatment across the reclassification |
| **Stage E** | `O-3` — C-2A's observation basis, still unpinned |
| **Separate Owner authorization** | The C-2A FX leg, UNRESOLVED-BY-DESIGN |
| **Stage F** | Licensing assessment for every source used at Stages C and D |
| **Stage G** | `HG-8` evidence; evidence gathered for `HG-6`, `HG-7`, `HG-9`, `HG-12`; the `SC-6` determination and its consequences |
| **Later gate evaluation** | The N-3 publisher-side provenance gap (§10.1) and the absent methodology version history (`O-4`) |
| **Owner** | Any segment that later becomes NON-LIVE, CHARACTERIZED returns for `OJ-1` |

---

## 21. Limitations

- Stage D is a **documentary and structural** stage. Every finding is about dates, counts, calendars,
  and what publishers state — never about how any series behaves.
- The live spine was **not obtained**, so no statement about its length, continuity, or gap
  structure is made.
- Entitlement-gated channels were **not** used; no account was created and no personal information
  was provided.
- The `SC-6` determination rests on the **absence** of segment-specific publisher evidence in the
  material located. It is a statement about the evidence obtained, not a claim that no such
  statement exists anywhere.
- The N-3 finding depends on a fund-issuer document for its effective date.

---

## 22. Confirmations

- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked, scored, weighted, or selected.** No criterion was amended, added, or
  renumbered; the criteria-freeze boundary at `1e8bc85` stands.
- **No gate was passed or failed.** Final gate evaluation remains Stage G.
- **No performance quantity was computed at any stage.** `ND-1 … ND-7` were not used.
- **No Baseline start date, no Baseline Dataset Cutoff, and no research cutoff were chosen.**
- **`OJ-1` was not reached.** No admissibility decision was made or inherited.
- **The OD-12 evidentiary standard is recorded as a standard; no candidate is claimed to satisfy
  it.**
- **No FX source or convention was selected.**
- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **No historical value, raw dataset, publisher file, or external provenance material is committed
  to this repository.**
- **Stage E has not begun.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Evidence Artifact. Owner Review: PENDING. `SC-6` triggered for the C-1
pre-base-date segments. `OJ-1`: NOT REACHED — DEFERRED. Primary Proxy: NOT APPROVED — P1-2 remains
OPEN. Phase 2: BLOCKED.**
