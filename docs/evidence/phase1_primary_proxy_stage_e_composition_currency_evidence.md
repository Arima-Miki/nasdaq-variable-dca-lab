# Phase 1 Evidence Artifact — Primary Proxy Qualification, Stage E: Return Composition and Currency Treatment

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Primary Proxy Candidate Qualification — Stage E** |
| Research date | **2026-08-12** (new source access dates 2026-08-12; retained Stage-C/D sources accessed 2026-08-11) |
| Authorising decisions | Study design [`phase1_primary_proxy_qualification_study_decision.md`](../decisions/phase1_primary_proxy_qualification_study_decision.md) (criteria frozen at `1e8bc85`); Stage-E Owner Decisions **E-1 … E-7** |
| Closure decision | [`phase1_primary_proxy_stage_e_closure_decision.md`](../decisions/phase1_primary_proxy_stage_e_closure_decision.md) (**E-8 … E-12**) |
| Owner Review | **PENDING — prepared for Owner Review** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Publication classification | **PUBLIC QUALITATIVE EVIDENCE** — documentary findings, classifications, dates, and publisher-stated fee parameters only |
| Historical values | **NONE PUBLISHED.** No observation value, no return, and no incidentally returned NAV or net-asset value appears in this artifact |
| Source material | Retained **outside** the repository. No publisher file, provenance index, checksum file, extracted text, or decrypted copy enters Git |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| `OJ-3` | **NOT REACHED** by Owner disposition (see [§15](#15-the-82-classification-and-its-owner-disposition)) |
| `OJ-4` | **NOT RESOLVED** |
| Phase 2 | **BLOCKED** |

> **What this artifact is.** The record of what Stage E *researched and found* about each
> candidate's return composition, currency treatment, and embedded components. It documents
> semantics. It qualifies no candidate, passes or fails no gate, approves no Primary Proxy,
> selects no return version, selects no FX source or convention, and constructs no series.

> **On repository entry at Stage E.** The frozen study design records `Repository entry: Nothing`
> for Stages A–G, and records `Owner gate: No (reported at G)` for Stage E specifically. This
> artifact exists because the Owner **explicitly directed** an execution-level review checkpoint
> (Owner Decision E-4) and a durable closure record (Owner Decision E-10). That is an
> Owner-authorized deviation, recorded rather than made silently. It does **not** amend the frozen
> study design. The same deviation was recorded at Stages C and D.

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and does not
govern Baseline behavior. The frozen criteria — `HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`,
`OJ-1 … OJ-6`, `SC-1 … SC-20`, handoffs `H-1 … H-8` and rules `R-1 … R-4` — are fixed by the study
design and are **used, never amended, here**. Stage-C findings
([`phase1_primary_proxy_stage_c_methodology_evidence.md`](phase1_primary_proxy_stage_c_methodology_evidence.md))
and Stage-D findings
([`phase1_primary_proxy_stage_d_history_continuity_evidence.md`](phase1_primary_proxy_stage_d_history_continuity_evidence.md))
remain authoritative for their own stages. This artifact is **additive** and rewrites neither, even
where Stage E adds precision to a Stage-C statement.

This artifact is written to be self-contained. A future researcher with no access to the research
session should be able to establish what was investigated, what was found, what could not be
established, and why, from this file alone.

---

## 2. Research objective

Stage E asks one question per candidate:

> **What, according to its own publisher, does this candidate's return series contain — which
> return version, which dividend and withholding treatment, which embedded expenses, and which
> currency treatment — and is each of those determinate from primary evidence?**

The governing distinction throughout, from frozen study design §8.1:

> **Q-A — "What is the *candidate's own* return composition, per its publisher?"** is the
> qualification question, and is establishable.
> **Q-B — "What does Nissay's 「配当込み」 mean?"** is a separate, bounded question about a
> non-candidate.

### 2.1 Owner Decisions governing this execution

| # | Subject | Effect on execution |
| - | ------- | ------------------- |
| **E-1** | C-2A `HG-4` treatment | `HG-4` recorded **NOT YET EVALUABLE** for the external FX leg; the "currency treatment indeterminate → `HG-4` fails" rule does **not** apply where the governance design itself prohibits Stage E from selecting the convention |
| **E-2** | `O-3` evidence | Primary evidence bearing on `O-3` may be recorded if encountered; no NAV basis may be chosen; `HG-2` and `HG-5` may not be declared satisfied |
| **E-3** | C-2A FX-source qualification | Characterize the obligation only; no per-source qualification, no comparison, no selection |
| **E-4** | Stage-E Owner Review checkpoint | Added at execution level; does **not** amend the frozen "Owner gate: No (reported at G)" |
| **E-5** | Arithmetic on published parameters | Permitted solely as a documentary consistency check; `AC-2` remains fully binding |
| **E-6** | Published fee and expense parameters | Recordable as documentary evidence where needed for `HG-10` / OD-11 |
| **E-7** | Reuse of previously examined Nissay evidence | Prior approved-stage documents count toward the §8.3 declared classes; new retrieval only where a class was not yet adequately examined |

---

## 3. Candidate scope as executed

| Route | Stage-E treatment |
| ----- | ----------------- |
| **C-1** `NDXJPY` | Executed in full |
| **C-1** `XNDXJPY` | Executed in full |
| **C-1** `XNDXNNRJPY` | Executed in full |
| **C-2A** | Executed in full, subject to E-1 and E-3 |
| **C-2B** | Does not advance (Stage-C closure P-1) |
| **C-3** | Out of scope by the frozen study design |

`SC-6` remains a **segment-level** exclusion from Stage D and does not remove any C-1 series from
documentary Stage-E qualification: return composition and currency treatment are properties of the
series, not of a segment. The three C-1 series were carried **identically and distinctly**
throughout, per `AC-4` and §4.1.

---

## 4. Source inventory

All documents are **PRIMARY** and were read locally. Source files are retained outside the
repository; identifiers below are the durable citation handles.

### 4.1 Retained from Stages C and D, re-read at Stage E

| ID | Document | Publisher | Date / version |
| -- | -------- | --------- | -------------- |
| `D-01` | NASDAQ-100 Index® NDX® — Index Methodology | Nasdaq, Inc. | © 2026 |
| `D-02` | Calculation Manual – Equities & Commodities | Nasdaq | 20 May 2026 |
| `D-03` | NDX Index Versions | Nasdaq, Inc. | © 2026 |
| `D-04` | Nasdaq Index Methodology Guide | Nasdaq | 31 Jul 2026 |
| `D-06` | Annual Financial Statements — Invesco QQQ Trust℠, Series 1 | Invesco | period ended 30 Sep 2025 |
| `D-07` | Invesco QQQ performance page | Invesco | accessed 2026-08-11 |
| `D-08` | Invesco QQQ Trust, Series 1 — Prospectus (statutory) | Invesco | 22 Dec 2025 |
| `D-09` | Invesco QQQ Trust, Series 1 — Statement of Additional Information | Invesco | 22 Dec 2025 |
| `D-10` | Invesco QQQ — Summary Prospectus | Invesco | 22 Dec 2025 |
| `E-07` | Nasdaq-100 Index® Consultation — February 2026 | Nasdaq | Feb 2026 |

### 4.2 New at Stage E

| ID | Document | Publisher | Date / version | Purpose |
| -- | -------- | --------- | -------------- | ------- |
| `F-01` | Nasdaq Indexes: Withholding Tax Rates | Nasdaq, Inc. | May 2026 | resolves `O-2` |
| `F-02` | Change in Withholding Tax Rates (notice) | Nasdaq, Inc. | 30 Oct 2025 | **not relied upon** — see [§20.2](#202-n-4--a-confidentiality-marking-on-f-02) |
| `F-03` | 交付運用報告書 — ＜購入・換金手数料なし＞ニッセイＮＡＳＤＡＱ１００インデックスファンド | ニッセイアセットマネジメント | 2nd fiscal period, ended 2024-09-20 | S.3 periodic disclosure |
| `F-04` | Fund report index page | ニッセイアセットマネジメント | accessed 2026-08-12 | navigation only; no document locators served |
| `F-05` | ファンドの特色 (fund outline page) | ニッセイアセットマネジメント | accessed 2026-08-12 | S.3 benchmark-describing material |
| `F-06` | 投資信託説明書（交付目論見書） | ニッセイアセットマネジメント | 使用開始日 2025.12.20 | S.3 statutory disclosure |

Evidence tier for every characterization recorded in this artifact is **PRIMARY**. No
characterization rests on a secondary source, so `SC-7` was not triggered.

---

## 5. C-1 — return composition (`HG-3`)

The Index Versions register (`D-03`) assigns each candidate a named **Return Version**, and the
Calculation Manual (`D-02`) defines what that version means mechanically. Both were read; they
agree, and the Manual is the more precise of the two.

| | `NDXJPY` | `XNDXJPY` | `XNDXNNRJPY` |
| --- | -------- | --------- | ------------ |
| Return version | **PRICE RETURN** | **GROSS TOTAL RETURN** | **NOTIONAL NET TOTAL RETURN** |
| Ordinary dividends | Excluded | Reinvested | Reinvested, net of notional withholding |
| **Special dividends** | **Reflected** | Reinvested | Reinvested |
| Reinvestment timing | not applicable | **ex-date** | ex-date (inherits the NTR method) |
| Withholding | none | none (gross) | **flat notional 30%** |
| Currency | JPY | JPY | JPY |
| Fund-level management expense embedded | **none** | **none** | **none** |

Governing publisher statements:

> **Price Return** — "The Price Return Index is calculated without regard to ordinary dividends;
> however, it does reflect special dividends." (`D-02` §2.3.1.1)

> **Gross Total Return** — "The Gross Total Return (GTR) Index Value reinvests cash dividends."
> (`D-02` §2.3.2); "Reinvests cash dividends on the ex-date." (`D-03`)

> **Notional Net Total Return** — "The Notional Net Total Return (NNTR) Index value reinvests cash
> dividends based on a tax withholding rate of 30%." (`D-02` §2.3.3.2); "Designed to reflect a net
> total return index reinvesting 70% of cash dividends, and factors in a deduction based on an
> indicative 30% tax rate." (`D-03`)

Two points of precision that Stage E adds, **additively**, to the Stage-C record:

1. The register's word "*ordinarily*" in "Ordinarily calculated without regard to cash dividends"
   is explained by the Manual: ordinary dividends are excluded, **special dividends are reflected**.
   A distinct *True Price Return* variant excludes both; `NDXJPY` is **not** that variant.
2. `XNDXNNRJPY`'s withholding basis is a **flat notional rate stated in the Manual**, not a
   per-security rate. This is what resolves `O-2` (§6).

> **`HG-3` evidence for all three C-1 candidates: COMPLETE and DETERMINATE.** No gate is passed or
> failed here; gate evaluation remains Stage G.

The three series are **not interchangeable** and are **not collapsed**. No return version is
selected by this artifact.

---

## 6. C-1 — withholding and open item `O-2`

`O-2` was the never-retrieved Nasdaq document referenced by the Calculation Manual as the source of
withholding tax rates. It was retrieved at Stage E as `F-01`.

`F-01` (May 2026) states that Nasdaq uses withholding tax rates "in the calculation of **Net Total
Return** indexes"; that the rates used are those applicable to non-resident investors who do not
benefit from double taxation treaties; and that they are used in the calculation of net total
return indexes "unless otherwise specified in an individual index methodology". Its Appendix A is a
table of rates by **country of incorporation**. The strings *notional* and *NNTR* appear **zero**
times in `F-01`.

Therefore:

| Candidate | Depends on `F-01` Appendix A? | Withholding basis |
| --------- | ----------------------------- | ----------------- |
| `NDXJPY` | No | none — no dividend is reinvested |
| `XNDXJPY` | No | none — gross reinvestment |
| `XNDXNNRJPY` | **No** | flat notional **30%**, stated directly in `D-02` §2.3.3.2 |

> **`O-2` = RESOLVED.** The document exists, was retrieved, and was read. Its rates govern **NTR**
> indexes. **No current C-1 candidate is an NTR index**, so no candidate depends on Appendix A for
> its withholding assumption.

**Recorded but expressly not used as evidence.** Appendix A lists a rate for the United States of
America that coincides numerically with `XNDXNNRJPY`'s notional 30%. `XNDXNNRJPY`'s 30% is taken
from the Calculation Manual's own statement of the NNTR method. **The numerical coincidence is not
the evidentiary basis**, and no inference is drawn from it.

No withholding precision is inferred beyond publisher evidence. No stop condition was triggered.

---

## 7. C-1 — currency treatment (`HG-4`)

`HG-4`'s **embedded** branch applies. All three required elements are documented.

| Element | Publisher evidence |
| ------- | ------------------ |
| **Rate source** | "Foreign exchange rate is provided by the WM Company" (`D-02`); the accompanying footnote identifies the WM/Reuters Spot Rates provided by The World Markets Company plc in conjunction with Thomson Reuters |
| **Observation time** | "in the calculation of the EOD Index Value is the closing spot rate at **16:00:00 UK time**, unless otherwise noted in the Index Methodology"; intraday spot rates apply to real-time calculation (`D-02`) |
| **Alignment** | the spot rate is subscripted to the **current index calculation day** `t` and paired with the EOD price for day `t`; the Start-of-Day value uses day `t−1`'s rate (`D-02`) |

Two structural facts recorded alongside them:

- Conversion is applied **per Index Security**, converting each security's quote currency into the
  Index Currency. A JPY series is **not** produced by converting a USD index level.
- **Override check.** `D-01`, the governing NDX Index Methodology, contains **zero** occurrences of
  *currency*, *exchange rate*, *WM*, or *JPY*. The "unless otherwise noted in the Index
  Methodology" escape is therefore **not** triggered. This is a documented absence and is
  consistent with the Stage-C finding.

### 7.1 The observation-time asymmetry

`D-01` records that the index value is disseminated to 17:16:00 ET and that the closing value may
change until 17:15:00 ET due to corrections to constituent Last Sale Prices, while the FX leg is a
**16:00:00 UK** closing spot. Both observation times are published by the publisher.

> This is recorded as a **documented characteristic of the embedded construction**, not as an
> evidence failure and not as a performance judgment. `HG-4` requires that the rate source,
> observation time, and alignment be documented; they are.

> **`HG-4` evidence for all three C-1 candidates: COMPLETE (embedded branch).**

---

## 8. C-1 — embedded components (`HG-10`)

The embedded components of a C-1 series are its **dividend treatment** and, for `XNDXNNRJPY`, its
**notional withholding deduction**. Nothing else is embedded.

- **No fund-level management expense is embedded in any C-1 candidate.** An index carries no
  management fee, and none of `D-01` … `D-04` discloses one.
- **Embedded FX is not an expense.** It is a component of the index calculation and is recorded as
  such.
- **`XNDXNNRJPY`'s notional withholding deduction is a return-composition component, not a fund
  management fee**, and must not be treated as one.

> **`HG-10` evidence for all three C-1 candidates: COMPLETE.**

---

## 9. C-2A — return composition (`HG-3`)

| Item | Publisher evidence (`D-06`, `D-08`, `D-09`) |
| ---- | ------------------------------------------- |
| NAV computation | calculated and disseminated daily on each day the NYSE is open; normally calculated as of the regularly scheduled close of the NYSE (normally 4:00 p.m., Eastern time); NAV = (assets − liabilities) ÷ shares outstanding, rounded to the nearest cent |
| NAV total return | "an initial investment made at the net asset value at the beginning of the period, **reinvestment of all dividends and distributions at net asset value** during the period, and redemption at net asset value on the last day of the period" |
| Distribution behaviour | the Trust **distributes**; the Financial Highlights carry a distributions-to-shareholders line |
| Reinvestment mechanism | "Dividend Reinvestment Service. **No reinvestment service is provided by the Trust.**" Broker-dealers may make the DTC book-entry service available (`D-09`) |

> **Critical distinction, recorded deliberately.** The reinvestment convention is **part of the
> return calculation**. It is **not** evidence that the Fund operationally reinvests shareholder
> distributions. Reinvestment is therefore an **assumption applied in a return construction** for
> C-2A, whereas for `XNDXJPY` and `XNDXNNRJPY` reinvestment occurs **inside the index** at the
> ex-date.

> **`HG-3` evidence for C-2A: COMPLETE and DETERMINATE.** The reinvestment convention is stated
> identically regardless of which NAV basis is meant, so `HG-3` does not depend on `O-3`.

---

## 10. C-2A — open item `O-3`

Encountered while establishing `HG-3`, and recorded under Owner Decision E-2. The publisher states:

> "Net asset value total return includes adjustments in accordance with accounting principles
> generally accepted in the United States of America and as such, **the net asset value for
> financial reporting purposes and the returns based upon those net asset values may differ from
> the net asset value and returns for shareholder transactions.**" (`D-06`, `D-08`)

This authoritatively establishes that:

1. a **financial-reporting NAV** exists;
2. a **shareholder-transaction NAV** exists;
3. the two **may differ**;
4. returns calculated from the two bases **may differ**.

It does **not** establish which basis governs any published QQQ NAV-return series relevant to
C-2A.

**A related documented absence.** The issuer's own performance page (`D-07`) defines **only** its
market-return basis — the midpoint of the bid/ask spread at 4 p.m. ET — and publishes **no**
definition of its NAV-return basis. This absence is recorded as evidence. **Absence is not
resolution**, and no basis is inferred from the silence.

> **`O-3` = CHARACTERIZED, NOT RESOLVED — remains OPEN.**

No NAV basis was chosen. `HG-2` is **not** declared satisfied. `HG-5` is **not** declared
satisfied. Stage B was not reopened. No prior Stage-C finding was modified.

---

## 11. C-2A — embedded expenses (`HG-10`) and item `N-2`

The published QQQ return record spans **two embedded-cost regimes**.

| Period | Structure | Stated ratio |
| ------ | --------- | ------------ |
| **UIT era**, through market close **2025-12-19** | Under the Trust Agreement the Trust is responsible for the Trustee's fee (including fees for extraordinary expenses and other services), transfer agency service fees, governmental fees, taxes and charges payable by the Trustee with respect to Shares, expenses of protective action, indemnification, expenses of contacting beneficial owners including proxy fees, brokerage commissions and other transactional charges, and other out-of-pocket expenses. Operating-expense lines reported: Licensing, Professional, Marketing, Trustee, Proxy, Other. | **0.20%** ratio of expenses to average net assets, in each of the five fiscal years reported through the year ended 30 Sep 2025 |
| **Open-end era**, Investment Advisory Agreement effective **2025-12-20** | Annual **unitary** management fee of **0.18%** of average daily net assets. Out of the unitary fee the Adviser pays substantially all Fund expenses, **except** distribution fees (if any), acquired fund fees and expenses (if any), brokerage expenses, taxes, interest, litigation expenses, and other extraordinary expenses including proxy expenses. Interest expense is excluded from the Fund expenses borne by the Adviser. | **0.18%** Total Annual Fund Operating Expenses (Management Fees 0.18%, Other Expenses None), footnoted as "restated to reflect current fees" |

The publisher further states that prior to 20 December 2025 the Fund "did not have a contractual
agreement with an investment adviser to provide investment advisory services" and "did not pay
advisory fees to the Adviser" (`D-08`).

### 11.1 Two findings that qualify every ratio above

1. **NAV-embedded transaction costs are excluded from the reported expense ratio.** The publisher
   states that transaction costs are included in the calculation of the Trust's NAV and accordingly
   **reduce the Trust's total returns**, while not being considered operating expenses and not
   being reflected in the ratios of expenses reported in the Financial Highlights (`D-06`).
2. **A fee waiver is embedded in published performance.** The Adviser has agreed to waive the
   Advisory Fee in an amount equal to the lesser of (i) 100% of the net advisory fees attributable
   to the Fund's Affiliated Investments or (ii) the Advisory Fee available to be waived; the waiver
   does not apply to cash collateral received for securities lending; it is in place **through at
   least 31 August 2027**, with no guarantee of extension. The prospectus states that the Fund's
   performance reflects fee waivers, absent which performance would have been lower (`D-08`,
   `D-09`).

> Together these establish, from the publisher's own documents, that **the embedded cost of the
> C-2A route is not summarised by any single stated ratio**, in either regime.

### 11.2 `N-2` status

The publisher states that the Fund had the same investment objective and substantially similar
investment policies, **but differing expenses**, when operating as a UIT, and that returns prior to
the Reclassification reflect the Fund's operation as a UIT (`D-08`).

> **`N-2`: expense facts ESTABLISHED. Continuity consequence UNRESOLVED.**

No tracking difference was inferred; no stated expense ratio was equated with tracking difference;
no expense-adjusted series was created; no cost model was built; `HG-8` was **not** decided; no
before/after performance was evaluated.

> **`HG-10` evidence for C-2A: COMPLETE, recorded per period.**

---

## 12. C-2A — FX obligation and `HG-4` status

Recorded under Owner Decisions E-1 and E-3.

> **C-2A FX leg = UNRESOLVED-BY-DESIGN.**
> **`HG-4` = NOT YET EVALUABLE for the external FX leg.**

This is a **governance deferral**, not a gate pass and not a qualification failure. The frozen
Stage-E rule "currency treatment indeterminate → `HG-4` fails" does **not** apply where the
indeterminacy exists because the governance design itself prohibits Stage E from selecting the
convention.

A future C-2A construction would require, at minimum:

1. an authoritative USD/JPY rate source;
2. a documented observation time;
3. documented alignment to the relevant observation date;
4. source qualification;
5. licensing / use-right review where applicable;
6. **separate Owner authorization before construction.**

**Recorded structural asymmetry.** C-1's embedded FX is observed at 16:00:00 UK, whereas C-2A's USD
NAV is struck at the NYSE close (normally 4:00 p.m. ET). A C-2A JPY construction would therefore be
**choosing a different observation convention**, not inheriting C-1's.

No FX provider, rate, fixing time, or alignment convention was selected; no per-source
qualification was performed; no FX sources were compared; no prior FX research was used to make a
selection; no JPY series was constructed. Existing Phase-1 FX evidence is referenced **only** to
record that the question has previously been researched and remains unresolved.

---

## 13. `N-3` — Stage-E relevance

Narrow finding, from already-authorized evidence (`E-07`) only:

> **The available consultation evidence does not document a return-composition, dividend,
> withholding, or currency-treatment change.**

The proposals concern market-capitalization calculation for eligibility, fast entry, share-count
and float adjustment timing, and folding ad-hoc changes into scheduled quarterly rebalances — that
is, **constituent selection and weighting**. The terms *dividend*, *total return*, *currency* and
*withholding* each appear **zero** times in the document.

That zero result was **verified rather than assumed**: the extraction covers all six pages with the
appendix intact, and positive controls in the same text return non-zero counts for terms known to
be present. The document's appendix of related indexes enumerates structural derivatives and does
**not** enumerate currency variants.

**Limitation, recorded explicitly.** `E-07` is the **consultation document**, not the final
publisher-side decision document. Owner Decision D-11 recorded the absence of that final document
as an open provenance gap, and Stage E was not authorized to reopen it.

> **This finding is about the *proposals*. It must not be generalized into a claim about the final
> adopted change. The `N-3` / D-11 publisher-side provenance gap remains OPEN.**

---

## 14. The bounded S.3 Nissay investigation and Q-B

Executed exactly per frozen study design §8.3, with prior approved-stage documents counted toward
the declared classes under Owner Decision E-7.

| §8.3 declared class | Material examined | Status |
| ------------------- | ----------------- | ------ |
| Nissay-issued **statutory disclosure** | 交付目論見書 (`F-06`, 使用開始日 2025.12.20); 請求目論見書 (examined in a prior Owner-approved Phase-1 stage, reused under E-7) | **EXAMINED** |
| Nissay-issued **periodic disclosure** | 交付運用報告書, 2nd fiscal period ended 2024-09-20 (`F-03`), including its dedicated 「指数に関して」 section | **EXAMINED** |
| Nissay-issued **material describing the benchmark** | ファンドの特色 (`F-05`); the benchmark passages of `F-03` and `F-06` | **EXAMINED** |
| The **benchmark publisher's own definition of a return version explicitly named by Nissay** | — | **INAPPLICABLE — class never reached.** Nissay names no Nasdaq return version, no index symbol, and no gross / net / notional-net designation |

What Nissay does state, consistently across all three document classes:

> 「NASDAQ100指数（配当込み、円換算ベース）」とは、「NASDAQ100指数（配当込み）」をもとに、
> **委託会社が独自に円換算したもの**です。

The dedicated 「指数に関して」 section of the periodic report contains only the benchmark name, the
Nasdaq disclaimer, and that sentence. The licence recital confirms that what Nasdaq licenses is the
Nasdaq-100 Index® itself, while the **yen conversion is the management company's own**.

### 14.1 Q-B result

> **Q-B = UNDISCLOSED / NOT ESTABLISHED.**

Nissay does not disclose whether 「配当込み」 denotes gross, net, or notional-net total return, nor
its benchmark FX provider, fixing time, rate type, holiday convention, rounding, or fallback rules.

The absence was verified, not assumed: the Japanese terms for *gross* and *net* appear **zero**
times in the examined material, and the character coverage of the mapping actually used to read
those documents was confirmed against positive controls present in the same documents.

### 14.2 The investigation stopped at the declared boundary

The investigation **STOPPED** once the declared classes were examined. It was **not** extended to
third-party interpretation, correspondence with Nissay, empirical fit, inference from product
naming, relative plausibility, investor tax assumptions, or any undeclared evidence class.
**`SC-20` was not triggered.**

---

## 15. The §8.2 classification and its Owner disposition

The frozen design requires an unresolved Q-B to be classified as exactly one of: prevents
qualification / non-discriminating among candidates / requires Owner judgment.

**Decision history is preserved here deliberately, per Owner Decision E-10.**

| Step | Record |
| ---- | ------ |
| **1. Stage-E evidence result** | Q-B is **UNDISCLOSED / NOT ESTABLISHED** (§14.1). This is the factual finding and it is unchanged by anything below |
| **2. Stage-E provisional interpretation** | The Stage-E execution report classified the unresolved Q-B as *requires Owner judgment*, and reported **"`OJ-3` REACHED — NOT MADE"**, on the reasoning that the choice among three qualified return versions could not be made from evidence. The report simultaneously recorded the competing reading — that if the Primary Proxy need not correspond to Nissay's benchmark, Q-B is non-discriminating — and referred the question to the Owner rather than resolving it |
| **3. Owner disposition (E-8)** | The Owner determined that **Q-B is NON-DISCRIMINATING** among the Primary Proxy candidates, because the Primary Proxy is a research proxy for the Frozen Baseline and its role is not to reconstruct, reverse-engineer, or guess an undisclosed Nissay internal benchmark convention. Nissay's undisclosed meaning therefore establishes no principled basis for selecting among `NDXJPY`, `XNDXJPY` and `XNDXNNRJPY` |
| **4. Authoritative governance state** | **Q-B NON-DISCRIMINATING — `OJ-3` NOT REACHED.** This supersedes step 2 as the governance disposition |

The Owner disposition is a **governance disposition of the ambiguity**. It does **not** modify the
factual finding that Q-B is UNDISCLOSED / NOT ESTABLISHED. It does **not** select a C-1 return
version. It does **not** establish that the three return versions are equally suitable.

> Any eventual Primary Proxy return-version decision must arise from the frozen qualification
> framework and the Primary Proxy's role as a Baseline research proxy — **not** from an attempt to
> guess Nissay's undisclosed convention.

**Binding inference prohibitions.** Nissay's undisclosed convention must not be inferred from
empirical closeness, fund performance, tracking difference, product naming, `ND-4`, relative
plausibility, or investor tax assumptions.

---

## 16. §9 route-obligation comparison

Qualitative and ordinal, per §9.1 and `AC-8`. No scores, no weights, no ranking, no performance.

| Obligation | C-1 (each of the three) | C-2A |
| ---------- | ----------------------- | ---- |
| Return version | **publisher-governed** | **publisher-governed** |
| Reinvestment mechanism | **publisher-governed** — inside the index, ex-date | **researcher-applied** — the Trust provides no reinvestment service |
| Withholding | **publisher-governed** — none, or flat notional 30% | not applicable at fund level |
| Embedded fund expense | **none** | **present, two regimes**, plus a time-limited waiver and NAV-embedded transaction costs excluded from the ratio |
| Observation basis | index EOD value | **UNRESOLVED — `O-3`** |
| FX | **embedded**, fully specified by the publisher | **constitutive** — source, time and alignment must be researcher-selected; none selected |
| Source qualification required | Nasdaq only | Nasdaq + Invesco + **an unselected FX provider** |
| Additional construction steps | **none** — the series is published as such | **a level-space synthetic JPY construction**, requiring separate Owner authorization |
| Reproducibility | one publisher, one documented chain | multiple publishers, one undocumented choice, one unauthorized construction |
| Unresolved obligations entering Stage F | `HG-8`; Stage-D `SC-6` segment exclusion; `H-1` NOT ESTABLISHED | `O-3`; the entire FX leg; `HG-4`; `HG-8`; `N-2` continuity |

> **Ordinal finding.** C-2A presently carries **more researcher-selected assumptions and more
> unresolved construction obligations** than C-1.

This is an **obligation and reproducibility finding only**. It is **not** a performance ranking,
**not** a candidate score, **not** a Primary Proxy selection, **not** proof that C-1 is more
accurate, and **not** proof that C-2A is unsuitable.

### 16.1 `CT-3` and `CT-4` inputs

**`CT-3` — additional assumptions each construction forces:**

| Candidate | Researcher-selected assumptions required |
| --------- | ---------------------------------------- |
| `NDXJPY` | none |
| `XNDXJPY` | none |
| `XNDXNNRJPY` | none — the notional 30% is publisher-stated, not researcher-chosen |
| `C-2A` | NAV basis (`O-3`); FX source; FX observation time; FX alignment; reinvestment convention; treatment across the 2025-12-19 expense-regime change |

**`CT-4` — evidence tier of governing methodology:** **PRIMARY** for every candidate.

These are recorded as **inputs to Stage G**. No comparative criterion is applied or scored here.

---

## 17. `OJ-4` evidence

Recorded as required by §9.4, and **not resolved**:

> Promoting C-2 to Primary Proxy would consume the independent cross-validation role currently
> assigned to C-2 under the three-layer concept (§14.2 of the Frozen Baseline), and would leave
> that concept without an independent cross-check.

Stage-E evidence sharpens the point: C-2A's value as a cross-check rests on its being a
**different kind of source** — a fund NAV rather than an index. Using it as the Primary Proxy
would forfeit exactly that independence, while simultaneously importing the FX obligation, the
`O-3` ambiguity, and a two-regime embedded-cost structure that C-1 does not carry.

> **`OJ-4` remains for later Owner judgment at the appropriate gate. It is NOT resolved here.**

---

## 18. OD-11 documentation result

The Phase-1 documentation duty delegated by OD-11 / Frozen Baseline §14.5 — that Phase 1 must
document which return components and expenses are already embedded in a proxy series — is
**DISCHARGED for the Stage-E candidates**, per candidate and, for C-2A, per period (§5, §8, §11).

Stage-E evidence independently supports why OD-11's prohibitions are well-founded: NAV-embedded
transaction costs reduce total returns while being excluded from the reported expense ratio, and a
time-limited waiver of undisclosed magnitude is embedded in published performance.

Preserved prohibitions, all observed at Stage E:

- costs already embedded in a series **must not** be deducted again;
- a stated expense ratio **must not** be equated with, or used to infer, tracking difference;
- **no** adjustment or cost model may be invented.

> **OD-11 is unchanged.** Stage E did **not** amend it, did **not** evaluate it, and did **not**
> complete the future `P1-4` cost-model work that §14.5 delegates to Phase 1.

---

## 19. Calculation boundary and documentary arithmetic

> **Stage E remained documentary. No historical observation-value analysis occurred.**

The only arithmetic performed was one **documentary consistency check** under Owner Decision E-5:
the Index Versions register describes `XNDXNNRJPY` as reinvesting 70% of cash dividends with a
deduction based on an indicative 30% rate, while the Calculation Manual describes the NNTR method
as reinvesting based on a 30% withholding rate. **70 + 30 = 100** — the two publisher statements
are internally consistent descriptions of the same construction.

> Recorded **only** as a documentary consistency check on publisher-stated parameters. It is
> **not** empirical analysis, generated no candidate return, created no series, and was not used as
> a discriminator. **`AC-2` remains fully binding.**

---

## 20. Evidence-integrity caveats

Recorded because they bear on **evidence confidence**, not as repository architecture.

### 20.1 Extraction hazards encountered and handled

Stage E read publisher documents locally. Four distinct hazards were encountered, each of which
would otherwise have produced a **false absence** — a null result indistinguishable from a genuine
documentary gap:

| Hazard | Handling |
| ------ | -------- |
| Font-program streams decoding into plausible-looking noise | excluded from the text under examination (an `SC-15` hazard) |
| Kerning-split text, where a phrase is broken across text-showing operations | searched space-insensitively rather than literally |
| **Encrypted documents** — two Nissay PDFs use the PDF standard security handler | decrypted locally, with the empty user password **verified against the document's own `/U` entry before any content was read**, so that a null could not be an unopened file |
| **CID-keyed fonts without a usable ToUnicode mapping** | the character codes for the phrases actually being searched were derived from a document whose mapping was known, and the shared code space was **confirmed by positive match before** that mapping was relied upon |

Before any new Stage-E claim was made, the extraction was **validated against three findings already
established at Stage C** — the NNTR 70% / 30% wording, the WM 16:00:00 UK convention, and the QQQ
reclassification passage — all three of which reproduced.

> **Every zero-hit result reported in this artifact is paired with a positive control from the same
> document.** Fluent extraction output and zero-hit extraction were not trusted without an
> integrity check, per the Stage-C research-integrity finding.

This is a **research discipline**. The temporary extraction tooling is not committed, and its
implementation details are deliberately **not** recorded as a repository architecture requirement.

### 20.2 `N-4` — a confidentiality marking on `F-02`

`F-02` carries an internal-use / limited-distribution marking, notwithstanding that it was served
from a public URL.

Fail-closed treatment was applied and is recorded:

- `F-02` was **not relied upon** for any Stage-E qualification finding;
- its substantive content is **not reproduced** in this or any repository artifact;
- **public accessibility is not evidence of redistribution permission**;
- **no inference** is made that the marking is ineffective or irrelevant.

> **`N-4` = OPEN / FAIL-CLOSED FOR PUBLICATION**, routed to Stage F for `HG-11` / `P1-8`
> determination.

This is **not** a finding that retrieval was unlawful, and no such claim is made.

---

## 21. Anti-circularity verification

- **`AC-2` holds absolutely.** No performance quantity was computed at any point in Stage E. The
  only arithmetic was on publisher-stated methodology parameters (§19).
- **`AC-3`.** `ND-1 … ND-7` were not used in reaching any part of this artifact. **`ND-4` was
  specifically not used** to infer anything about Nissay's convention.
- **`AC-4`.** The three C-1 series were carried identically and distinctly through every step, and
  C-2A received the same investigation depth. The C-1 / C-2A obligation asymmetry recorded in §16
  is a **finding about obligations**, not a symmetry breach.
- **`AC-8`.** No scoring, no weighting, no ranking. The §9 comparison is ordinal and reasoned.
- **No return version was selected by empirical closeness.** No candidate is described as "the
  benchmark", "benchmark-equivalent", or "best fit".
- **Incidental values** encountered in the source documents — fund NAV levels, annual return
  figures, net-asset totals, distribution amounts — were **not** used in any determination and are
  **not** reproduced in this artifact.

---

## 22. Publication and external-material boundary

**No historical value appears in this artifact.** No observation value, no return, no NAV level, no
net-asset total, no distribution amount, and no incidentally returned value.

The publisher-stated **fee and expense parameters** in §11 are recorded under Owner Decision E-6 as
documentary facts required to discharge `HG-10` / OD-11. They are not performance values.

Nothing else enters Git. Specifically excluded: publisher PDFs and HTML; the external provenance
index and checksum file; raw extracted text; decrypted copies of any document; scratch extraction
tooling; `ND-1 … ND-7` material; and any `F-02` content.

All source material is retained **structurally outside** the repository. Redistribution terms
remain **unassessed** for every source used at Stages C, D and E; licensing is Stage-F work, so
fail-closed treatment applies and nothing is cleared for republication. `P1-8` is unchanged by
Stage E.

---

## 23. What this artifact establishes

1. **`HG-3` documentary evidence is complete and determinate for all four candidates**, with the
   three C-1 return versions carried distinctly.
2. **`HG-4` documentary evidence is complete for all three C-1 candidates** on the embedded branch.
3. **`HG-10` documentary evidence is complete for all four candidates**, recorded per period for
   C-2A.
4. **`O-2` is RESOLVED**, and no current C-1 candidate depends on the withholding-rates document.
5. **`O-3` is CHARACTERIZED** by authoritative publisher evidence, and **remains OPEN**.
6. **Q-B is UNDISCLOSED / NOT ESTABLISHED**, established across the complete bounded set of
   declared evidence classes.
7. **The C-2A route carries more researcher-selected assumptions and unresolved obligations than
   C-1**, as an obligation and reproducibility matter.
8. **`N-2`'s expense facts are established** on both sides of the 2025-12-19 reclassification.
9. **The OD-11 Phase-1 documentation duty is discharged** for the Stage-E candidates.

---

## 24. What this artifact does NOT establish

- It does **not** approve a Primary Proxy — **P1-2 remains OPEN**.
- It does **not** pass or fail any hard gate for any candidate. Gate evaluation remains Stage G.
- It does **not** select a C-1 return version, and does **not** establish that the three return
  versions are equally suitable.
- It does **not** resolve `O-3`, and does **not** choose a NAV basis.
- It does **not** declare `HG-2` or `HG-5` satisfied.
- It does **not** select an FX source, rate, fixing time, alignment convention, or Baseline FX
  convention, and does **not** authorize any C-2 synthetic JPY construction.
- It does **not** resolve `HG-8`, `OJ-1`, `OJ-3`, or `OJ-4`.
- It does **not** close the `N-3` publisher-side provenance gap.
- It does **not** determine any licensing or redistribution question — that is Stage F.
- It does **not** amend the Frozen Phase-0 Baseline, any Owner Decision OD-01 … OD-14 including
  OD-11, or any frozen qualification criterion.
- It does **not** authorize Stage F or Stage G, and does **not** unblock Phase 2.

---

## 25. Phase-1 requirement impact

| Requirement | Effect of Stage E |
| ----------- | ----------------- |
| **P1-2** — Primary Proxy approval | **OPEN.** Unchanged |
| **P1-3** — proxy return composition | **SUBSTANTIALLY ADVANCED.** Q-A is now established and determinate for all four candidates from primary evidence. The Nissay-side Q-B is bounded, exhausted, and dispositioned as non-discriminating |
| **P1-4** — cost and expense treatment | **INFORMED, NOT SATISFIED.** Embedded components are documented; no cost model was built |
| **P1-5**, **P1-6** — start date, dataset cutoff | **OPEN.** Untouched |
| **P1-7** — QQQ route | Composition and expense semantics established; `O-3` and the FX leg remain open |
| **P1-8** — licensing | **UNCHANGED.** Stage-F work; `N-4` added to its scope |

---

## 26. Handoffs

**To Stage F.** Publishers whose terms must be assessed: Nasdaq, Inc.; Invesco; ニッセイアセット
マネジメント; and any USD/JPY FX provider later proposed for a C-2A construction. `N-4` carries a
specific confidentiality question for `HG-11` / `P1-8`.

**To Stage G.** `HG-3` evidence (all four candidates); `HG-4` evidence (complete for C-1;
deferred-by-governance for C-2A); `HG-10` evidence (per period for C-2A); the §8.2 classification
and its Owner disposition; the §9 route-obligation comparison; `OJ-4` evidence; `CT-3` and `CT-4`
inputs.

**Carried unresolved.** `O-3`; the C-2A FX leg; `HG-4` for C-2A; `HG-8`; `HG-5` and `HG-13`
(unassigned to any stage); Stage-D `SC-6` and `H-1`; `OJ-1`; `OJ-4`; `N-2` continuity; `N-3`
provenance; `N-4`.

---

## 27. Limitations

1. **Stage E is documentary.** Nothing here is validated against data, and nothing here should be
   read as evidence about how any candidate behaves.
2. **`N-3`'s finding is about the consultation document only**, not about the final adopted change,
   which remains unavailable in the evidence record.
3. **The S.3 investigation is bounded by design.** Its null result is a statement about the
   declared evidence classes, not a claim that no answer exists anywhere.
4. **`O-3` is characterized but unresolved**, and the issuer's silence on its NAV-return basis is
   recorded as an absence, not as an answer.
5. **Licensing is unassessed** for every source used, so no source is cleared for republication.
6. **Stage-D limitations are unchanged.** `SC-6` still excludes the C-1 pre-base-date segments and
   `H-1` remains NOT ESTABLISHED; Stage E does not revisit them.

---

## 28. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched, **including OD-11 and
  OD-12**.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary; no criterion was amended, added, renumbered, or re-weighted.
- **No prior evidence artifact was rewritten.** Stage-C and Stage-D findings stand; this artifact is
  additive, and the decision history at §15 is preserved rather than erased.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked, scored, or selected. No gate was evaluated.**
- **No C-1 return version was selected.**
- **No FX source or convention was selected, and no JPY series was constructed.**
- **No raw dataset, publisher document, external provenance material, extracted text, or decrypted
  copy is committed to this repository.**
- **Stage F has not begun and is NOT AUTHORIZED. Stage G has not begun.**
- **Phase 2 remains BLOCKED.**
