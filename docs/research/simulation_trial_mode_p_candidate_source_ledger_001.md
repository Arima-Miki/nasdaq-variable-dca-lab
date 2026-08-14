# Mode P — Candidate Source Cost Ledger — Edition 001

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** Edition 001 is closed on preservation.
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Governing policy:** Mode P Dataset Source Selection and Human-in-the-Loop Policy (approved 2026-08-14)
**Edition rule:** additive. This edition is **never edited** after preservation; a later round
produces edition 002, which supersedes but does not modify it.

**Evaluated in this edition: one candidate (FRED).** All others are listed as **NOT YET EVALUATED** —
identity only. No terms were read and no data retrieved for them, because that work is not
authorized. Listing a name is neither an endorsement nor a Primary Proxy nomination
(§18.4.3, §18.4.7).

---

## C-001 — FRED `NASDAQ100`

| Field | Value |
| --- | --- |
| Source authority | Federal Reserve Bank of St. Louis (FRED), redistributing Nasdaq, Inc. index data |
| Dataset identity | Series `NASDAQ100`, title **"NASDAQ-100"**; Release: *Nasdaq Daily Index Data* |
| Coverage **(verified)** | **1986-01-02 → 2026-08-12** — covers the authorized 2018-01-01→2022-12-31 span with wide margin |
| Frequency **(verified)** | **Daily, Close** |
| Units / denomination **(verified)** | **Index, Not Seasonally Adjusted** — USD index points |
| Return composition | **Price index.** Not total return, not dividend-adjusted, not fund NAV (`P1-3`, `P1-1` remain open) |
| Data-quality concerns | None observed. Publisher-direct via a central bank redistributor; strong series identity |
| Provenance quality | **High** — stable series ID, documented title, source, release, units, frequency |
| Copyright status **(verified)** | **"Copyrighted: Pre-Approval Required"**; *Copyright © 2016, NASDAQ OMX Group, Inc.* |

### Axis assessment

| Axis | Verdict | Evidence |
| --- | --- | --- |
| **A** AI autonomous retrieval | **NO** | Prohibited Use bars *"data mining, mirroring, robots, scraping, or similar data-gathering or extraction methods except as expressly allowed by the terms of use applicable to the FRED API."* API route requires a key → account creation |
| **B** Human manual retrieval | **YES (apparent)** | FRED FAQ expressly contemplates *"Download data into Excel for homework assignments"* for personal, non-commercial use |
| **C** Local retention | **YES** | Pre-approval tag permits *"non-commercial educational or personal use"* without permission |
| **D** Local software processing | **AMBIGUOUS** | See blocking clause below |
| **E** Simulator input | **AMBIGUOUS** | Same clause. **This is the actual blocker** |
| **F** Retain derived outputs | Likely yes if **E** permitted; untested |
| **G** AI inspection of outputs | Probably out of scope — outputs are derived artifacts, not FRED Content; untested |
| **H** AI-training restriction | **YES, explicit** | Satisfiable by *declining that use*; the Owner requires no AI training |

### Blocking clause — verbatim

> *"Use the FRED® Services or FRED® Content in connection with the development or training of any
> software program or system or machine learning, including, but not limited to, large language
> models, deep learning, generative artificial intelligence, or any other program or process commonly
> known as artificial intelligence."*

**Broad reading:** using the data to develop/validate the Mode-P simulator is prohibited **regardless
of who downloads it**. **Narrow reading:** the enumeration is wholly AI/ML, so *"software program or
system"* is coloured by that context and ordinary local simulation is unaffected. Both readings are
available on the text; the ambiguity is **recorded, not resolved**.

### Costs and disposition

| Field | Value |
| --- | --- |
| Authentication / account | None for manual download; **required** for API (the only lawful automated route) |
| Monetary cost | None |
| Recurring human effort | One manual download per snapshot — **low**; `MP-D2` requires only one |
| Engineering effort | Minimal — a two-column CSV loader |
| Reproducibility cost | **None once captured**; determinism is a property of engine + frozen snapshot |
| Unresolved ambiguity | Axes **D/E** — the *use*-side clause above |
| **Class** | **C** — acquirable, downstream use materially unresolved |
| **Status** | **CONDITIONAL** |
| Reason not selected | The `D`/`E` ambiguity is unresolved, and permission must not be invented |
| Workaround | Written clarification request to FRED (`stlsFRED@stls.frb.org`); FRED cannot grant permission for Nasdaq, so a definitive answer may require **Nasdaq pre-approval** |
| Workaround cost | Owner effort low; **latency unknown**; outcome uncertain |
| Residual risk after workaround | If Nasdaq approval is needed, latency may be substantial; a refusal makes this **HARD REJECT** |
| **Fallback rank** | **2** — best provenance found so far, gated on one answerable question |

> **`MP-S-08` restated:** the earlier fail-closed outcome stands exactly as recorded. It is **not**
> claimed that autonomous retrieval was permitted. **Human-in-the-loop acquisition does not cure this
> candidate**, because the blocking clause restricts *use*, not acquisition.

---

## C-005 — Nasdaq `NDXJPY`, **already held** in the Stage-D evidence store

Found during this task by inspecting preserved evidence, **not** by external access. It changes the
cost picture materially and is therefore assessed in full.

| Field | Value |
| --- | --- |
| Source authority | **Nasdaq, Inc., publisher-direct** — `indexes.nasdaqomx.com/docs/AdditionalData_NDXJPY.csv` |
| Local status | **Already retrieved 2026-08-11**, hashed in `SHA256SUMS`, provenance-indexed as Stage-D item `E-01`; `robots.txt` captured as `E-10` and recorded as not disallowing the paths used |
| Denomination | **JPY** — NASDAQ-100 expressed in Japanese yen |
| Frequency | Daily |
| Coverage **(verified, dates only)** | **1985-01-31 → 2020-06-26**, 8,926 rows |
| Coverage in the authorized span | **PARTIAL — 626 observations, 2018-01-02 → 2020-06-26 only.** The authorized 2018-01-01→2022-12-31 window **cannot be served**; the file ends mid-2020 |
| Return composition | Price index (JPY). `XNDXJPY` / `XNDXNNRJPY` variants also held; composition not verified |
| Known caveat | Carries Nasdaq's back-tested-history disclaimer: pre-launch values are *"merely indicative… AS IS for informational and educational purposes only"* |

### Why this candidate is attractive

- **Zero acquisition cost and zero acquisition risk** — the file is already lawfully here.
- **JPY-denominated**, which *dissolves* the USD-index-point / JPY-budget dimensional mismatch
  disclosed in the acquisition request. `exposure_units_acquired` would become dimensionally coherent.
- **Publisher-direct** provenance, better than any redistributor.
- A **shorter** viable span (2018-01-02 → 2020-06-26: three calendar years, ~30 month boundaries, two
  internal year boundaries) still spans the late-2018 drawdown, the early-2020 crash and the recovery
  to new highs — satisfying the coverage requirement while being *shorter*, which `MP-P-D1` prefers.

### Why it is NOT selected here — two blockers, neither mine to clear

> **1. Owner Decision D-5 minimisation rule.** The Stage-D provenance records that these values were
> *"incidentally returned; **NOT analysed**. Only the Date column was used,"* with a dedicated
> incidental-value-return record. Feeding those values to a simulator **converts incidentally-returned
> data into analysed data** — precisely what D-5 forbade. This requires an explicit Owner release
> from D-5; it **must not** be assumed.
>
> **2. Anti-contamination appearance (§18.4.7).** This is *Primary Proxy candidate* evidence. Running
> Mode P on a candidate's own series creates strong appearance risk, and once results exist, §18.4.7's
> disclosure duty attaches to every later `O-4` / `P1-2` decision **about that very candidate**. That
> is a heavier, more entangling burden than `MP-D4` contemplated for a neutral third-party series.

Also unassessed: local **use** terms (axes D/E) — the Stage-D provenance assessed only redistribution,
and marked even that **UNASSESSED**, with fail-closed treatment "for local audit and re-verification
only." Simulation is neither audit nor re-verification.

| Field | Value |
| --- | --- |
| Monetary cost | None |
| Recurring human effort | **None** — already held |
| Engineering effort | Minimal — two-column CSV, JPY native |
| Unresolved items | D-5 release; §18.4.7 entanglement; axes D/E terms; span shortfall |
| **Class** | **C** |
| **Status** | **CONDITIONAL** |
| Workaround | Owner release from D-5 **plus** acceptance of the §18.4.7 entanglement **plus** a span reduced to 2018-01-02 → 2020-06-26 |
| Residual risk | Qualification-lane entanglement is **not** removable by any technical step |
| **Fallback rank** | **1 on cost, 3 on governance cleanliness** |

---

## Not yet evaluated

Identity only — no terms read, no data retrieved, no ranking implied.

| ID | Candidate | Note |
| --- | --- | --- |
| C-002 | Stooq | Previously named fallback; **explicitly not auto-selected** by Owner instruction. Terms unread |
| C-003 | Nasdaq, Inc. publisher-direct index history | The upstream rights holder; may resolve the copyright question at its root |
| C-004 | General market-data aggregators with published API terms | Category, not a selection; some publish terms expressly permitting programmatic access and private retention |

**Deliberately noted, not proposed:** the intended fund's own published NAV history. It sits close to
`P1-1`/`P1-2` territory, and while §18.4.3 bars Mode P from establishing either, using it
provisionally would invite exactly the confusion the Simulation Trial exists to prevent. It should
not be considered without a specific Owner Decision.

---

## Current ranking

- **BEST PRACTICAL CANDIDATE:** *none confirmed.* Both evaluated candidates are **CONDITIONAL**, each
  gated on a single Owner-answerable question — and they are gated on **different** questions, so
  neither is a substitute for the other.
- **LOWEST-COST FALLBACK:** **C-005 (Stage-D `NDXJPY`)** — zero acquisition cost, already held,
  JPY-native, but requiring a D-5 release and accepting §18.4.7 entanglement, on a shorter span.
- **HIGHEST-QUALITY FALLBACK:** **C-001 (FRED `NASDAQ100`)** — cleanest governance separation from the
  qualification lane and full span coverage, gated on the `D`/`E` use-clause ambiguity.
- **NO ACCEPTABLE CANDIDATE:** **NOT ASSERTED, and not close.** Two candidates are CONDITIONAL, not
  HARD REJECT; under `MP-S-06` that conclusion would require HARD REJECT on every candidate.

**The two blockers are of different kinds, and that matters.** C-001's is a question of *fact about
external terms* the Owner can ask a third party. C-005's is a question of *internal governance* the
Owner can decide unilaterally, today, without waiting for anyone. If reaching a first simulation
quickly is the priority, C-005's blocker is the one that can be cleared fastest — at the price of
qualification-lane entanglement that no technical measure can undo.
