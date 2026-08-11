# Phase 1 Evidence Artifact — Primary Proxy Qualification, Stages A–C: Publisher Methodology and Provenance

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Primary Proxy Candidate Qualification — Stages A, B, C (incl. the C-2B targeted remediation)** |
| Research dates | **2026-08-11** (all source access dates 2026-08-11) |
| Authorising decision | [`phase1_primary_proxy_qualification_study_decision.md`](../decisions/phase1_primary_proxy_qualification_study_decision.md) — criteria frozen at commit `1e8bc85` |
| Closure decision | [`phase1_primary_proxy_stage_c_closure_decision.md`](../decisions/phase1_primary_proxy_stage_c_closure_decision.md) |
| Owner Review | **PENDING — prepared for Owner Review** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Publication classification | **PUBLIC QUALITATIVE EVIDENCE** — paraphrase plus precise document identity; short quotations only where a clause is itself the finding |
| Source documents | **Retained outside the repository. No publisher PDF, and no raw series of any kind, enters Git** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Candidate selection | **None. No candidate was ranked, preferred, or selected** |
| Performance computation | **None, at any stage** |
| Phase 2 | **BLOCKED** |

> **What this artifact is.** A record of what was *researched and found* in Stages A–C of the
> Primary Proxy Candidate Qualification Study. It establishes publisher methodology and
> provenance for the candidate routes. It qualifies no candidate, approves no Primary Proxy,
> selects no Baseline Start Date or Dataset Cutoff, and unblocks nothing.
>
> The Owner Decisions arising from these findings — including the disposition of C-2B — are
> recorded separately in
> [`phase1_primary_proxy_stage_c_closure_decision.md`](../decisions/phase1_primary_proxy_stage_c_closure_decision.md).

> **On repository entry at Stage C.** The frozen study design records `Repository entry:
> Nothing` for Stages A–G, with artifact recording deferred to Stage H. This artifact exists
> because the Owner **explicitly directed** a durable Stage-C closure record. That is an
> Owner-authorized deviation from the staged plan, recorded here rather than made silently. It
> does **not** amend the frozen study design, and Stage H's obligations are unchanged.

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and does not
govern Baseline behavior. The study's frozen criteria — hard gates `HG-1 … HG-13`, comparative
criteria `CT-1 … CT-9`, non-discriminating information `ND-1 … ND-7`, Owner judgments
`OJ-1 … OJ-6`, and stop conditions `SC-1 … SC-20` — are fixed by
[`phase1_primary_proxy_qualification_study_decision.md`](../decisions/phase1_primary_proxy_qualification_study_decision.md)
and are **used, never amended, here**. Earlier Phase-1 evidence relied upon for context is
[`phase1_fx_source_research.md`](phase1_fx_source_research.md).

This artifact is written to be self-contained. A future researcher with no access to the research
session should be able to establish what was asked, which documents were read, what each was found
to establish, what could not be established, and what was deliberately not published, from this
file alone.

---

## 2. Research objective

Stages A–C address one question, and deliberately only this one:

> **For each candidate route, does authoritative publisher methodology documentation exist, is it
> readable, and does it determine the series' identity and return composition?**

This is a **documentary** question. It is not a question about which candidate fits any observed
series better. That distinction is structural: the empirical route to P1-2 was already exhausted by
prior approved evidence, and the qualification framework therefore rests on methodology,
historical availability, return composition, licensing, and reproducibility — never on performance.

### 2.1 Explicit non-objectives

No candidate was ranked. No Primary Proxy was approved. No Baseline Start Date or Dataset Cutoff
was chosen. No FX source or convention was selected. No admissibility decision was made about
pre-launch or non-live history. No date-spine metadata was retrieved. Stage D was not begun.

---

## 3. Stages executed

| Stage | Scope as executed | Outcome |
| ----- | ----------------- | ------- |
| **A — Normative requirement extraction** | Repository-only. Converted the Frozen Baseline into a clause-cited register of binding requirements on the Primary Proxy | **COMPLETE — ACCEPTED.** Four criteria observations were raised and resolved by Owner interpretation, **not** by amending any criterion |
| **B — Candidate set fixing and identifier disambiguation** | Repository plus publisher identifier/definition documents | **BLOCKED then RESOLVED.** `SC-2` triggered on C-2; resolved by Owner interpretation into the bounded family C-2A / C-2B |
| **C — Publisher methodology and provenance discovery** | Publisher methodology documents for every candidate and component | **PARTIAL.** Established for C-1 and substantially for C-2A; `SC-1` triggered for C-2B |
| **C-remediation — C-2B primary-evidence recovery** | Bounded primary-source search for QQQ market-price return methodology | **EXHAUSTED.** Controlling primary documents retrieved and read; the methodology is **absent from them** |

Two disciplines applied throughout, and they constrain how these findings may be read:

- **Zero performance computation.** Not a policy of restraint but a structural guarantee: no
  return, correlation, tracking error, drawdown, or strategy quantity was computed at any point, so
  no finding here can have been shaped by candidate performance.
- **Verification against the actual document.** Every conclusion drawn from a PDF rests on local
  extraction with an identity check against the document's own cover text. See [§10](#10-research-integrity-findings).

---

## 4. Candidate scope as executed

| Route | Definition | Stage-C outcome |
| ----- | ---------- | --------------- |
| **C-1** `NDXJPY` | Nasdaq-100 Index JPY, price return | Methodology **ESTABLISHED** |
| **C-1** `XNDXJPY` | Nasdaq-100 Total Return JPY, gross total return | Methodology **ESTABLISHED** |
| **C-1** `XNDXNNRJPY` | Nasdaq-100 Notional Net Return JPY | Methodology **ESTABLISHED** |
| **C-2A** | QQQ **NAV-based** return construction combined with an externally specified USD/JPY conversion | **SUBSTANTIALLY ESTABLISHED** — open items in [§11](#11-open-items-carried-out-of-stage-c) |
| **C-2B** | QQQ **market-price-based** return construction combined with an externally specified USD/JPY conversion | **NOT ESTABLISHED** — `SC-1` triggered; see [§8](#8-c-2b--market-price-return-construction) |
| **C-3** | Nissay fund NAV, actual operating period | Out of scope by the frozen design; no work performed |

**Why C-2 became a two-member family.** The frozen candidate description "QQQ total-return series"
maps to at least three materially different constructions that are not interchangeable. Rather than
silently pick one, `SC-2` was triggered and the Owner bounded the family to **C-2A** and **C-2B**,
explicitly excluding third-party vendor adjusted-close series as a scope-control measure — *not* as
a judgment that such data is methodologically invalid. No vendor source was approached.

**The FX component was deliberately not approached.** C-2 requires component-wise identity under
`HG-2`. The USD/JPY component remains unidentified by design: selecting an FX source or convention
is outside Stage C's authorization.

---

## 5. Source inventory

Evidence classes follow the tiering established in
[`phase1_fx_source_research.md`](phase1_fx_source_research.md) §4: PRIMARY / NEAR-PRIMARY /
SECONDARY / UNREAD.

| # | Document | Publisher | Date / version | Class | What it establishes | Locator |
| - | -------- | --------- | -------------- | ----- | ------------------- | ------- |
| **D-1** | NASDAQ-100 Index® NDX® — Index Methodology | Nasdaq, Inc. | © 2026; no in-body effective date located | PRIMARY | Construction, eligibility, weighting, calculation days; delegation of calculation, recalculation, and data sources | `indexes.nasdaq.com/docs/Methodology_NDX.pdf` |
| **D-2** | Calculation Manual – Equities & Commodities | Nasdaq | **20 May 2026** (in-body) | PRIMARY | Return types, Index Currency, and the **EOD FX convention**; scope statement covering all Nasdaq Equity Indexes | `indexes.nasdaqomx.com/docs/Calculation_Manual_Equities_and_Commodities.pdf` |
| **D-3** | NDX Index Versions | Nasdaq, Inc. | © 2026 | PRIMARY | The register of NDX versions: official names, symbols, return versions, currency, base dates and base values | `indexes.nasdaqomx.com/docs/Index_Versions_NDX.pdf` |
| **D-4** | Nasdaq Index Methodology Guide | Nasdaq | **31 Jul 2026** (in-body) | PRIMARY | Definitions incl. Index Currency; data-source hierarchy; dissemination | `indexes.nasdaqomx.com/docs/Nasdaq_Index_Methodology_Guide.pdf` |
| **D-5** | Recalculation Policy | Nasdaq | **20 May 2026** (in-body) | PRIMARY | Restatement and recalculation of index values — an `HG-9` / P1-9 input | `indexes.nasdaqomx.com/docs/Recalculation Policy.pdf` |
| **D-6** | Invesco Annual Financial Statements and Other Information — Invesco QQQ Trust℠, Series 1 | Invesco | Period ended **30 Sep 2025** | PRIMARY | Trust legal identity and structure as of that date; **NAV total return definition**; distribution treatment | `invesco.com/content/dam/invesco/hk/en/pdf/annual-report/Invesco_QQQ_AnnualReport.pdf` |
| **D-7** | Invesco QQQ product and performance pages | Invesco | Accessed 2026-08-11 | PRIMARY (issuer-published) | Product identity; the **two published return bases**; the market-return basis statement | `invesco.com/qqq-etf/en/performance.html` |
| **D-8** | Invesco QQQ Trust, Series 1 — **Prospectus** (statutory, with supplements) | Invesco | **22 Dec 2025** | PRIMARY | Reclassification; Financial Highlights and the NAV total-return footnote; NAV computation and timing; valuation of portfolio securities | Invesco product page → issuer prospectus-delivery service, CUSIP `46090E103` |
| **D-9** | Invesco QQQ Trust, Series 1 — **Statement of Additional Information** | Invesco | **22 Dec 2025** | PRIMARY | 1940-Act classification change; dividend-reinvestment service statement; NAV calculation and order cut-off | as D-8, `doctype=sai` |
| **D-10** | Invesco QQQ Trust, Series 1 — **Summary Prospectus** | Invesco | **22 Dec 2025** | PRIMARY | Bid-ask spread disclosure; pointer to published NAV / market price / premium-discount data | as D-8, `doctype=spro` |
| **D-11** | Invesco QQQ Trust, Series 1 — **Semi-Annual Shareholder Report** | Invesco | **31 Mar 2026** | PRIMARY | Costs, key statistics, holdings. **Contains no performance table** | as D-8, `doctype=semi` |
| **D-12** | Invesco QQQ Trust, Series 1 — proxy statement / shareholder letter (structure modernization) | Invesco | **18 Aug 2025** | PRIMARY | Provenance of the proposed UIT → ETF conversion and its stated purpose | `invesco.com/us-rest/contentdetail?contentId=2b5fc069-cbd3-409c-967a-5b73419e6840` |
| **D-13** | Invesco QQQ Trust℠, Series 1 — Product Key Facts Statement (Hong Kong) | Invesco Capital Management LLC | **April 2026** | PRIMARY (non-US disclosure) | Index characterization; the fund's **published performance computation basis** | `invesco.com/content/dam/invesco/hk/en/pdf/kfs/Invesco_QQQ_KFS_EN.pdf` |

**Identified but NOT retrieved.** The Nasdaq dividend-classification / withholding-tax-rates
document referenced by D-1 and D-3 — carried forward as `O-2`.

**Retrieval path refused.** SEC EDGAR returned HTTP 403 ("Your Request Originates from an
Undeclared Automated Tool") on every attempted path. SEC's automated-access policy requires a
declared contact identity. **No personal identifier was transmitted to SEC or any other external
service, and no contact address was invented.** The path was therefore not used, and the limitation
is recorded rather than worked around. D-8 … D-11 were obtained instead through the **issuer's own**
prospectus-delivery link, reached from Invesco's QQQ product page.

---

## 6. C-1 — Nasdaq JPY index family

### 6.1 The methodology chain is reconstructable

D-1 does not stand alone; it delegates explicitly, and the chain is stated in its own text:

```
D-1  NDX Index Methodology   →  construction, eligibility, weighting, calculation days
      ├── delegates Calculation Types and mathematics        →  D-2  Calculation Manual
      ├── delegates Recalculation and Restatement Policy     →  D-5  Recalculation Policy
      └── delegates Data Sources and definitions             →  D-4  Methodology Guide
D-3  NDX Index Versions      →  the register of published versions
```

This satisfies `HG-1` in kind for C-1: publisher-issued, identifiable by title and version, and
actually extractable.

### 6.2 Return composition is determinate per series

Each JPY version carries its own publisher-stated return treatment in D-3, and the three are **not
interchangeable**:

| Series | Official name | Return version | Publisher's dividend treatment |
| ------ | ------------- | -------------- | ------------------------------ |
| `NDXJPY` | Nasdaq-100 Index JPY | Price return | Ordinarily calculated **without regard to** cash dividends on Index Securities |
| `XNDXJPY` | Nasdaq-100 Total Return JPY | Gross total return | **Reinvests cash dividends on the ex-date** |
| `XNDXNNRJPY` | Nasdaq-100 Notional Net Return JPY | Notional net total return | Reflects reinvestment of 70 % of cash dividends, with a deduction based on an **indicative** 30 % tax rate |

All three carry a JPY base date of **29 June 2020** with a base value of 1000. What that base date
means for *available history* is **not** determined here — see [§12](#12-what-stage-c-deliberately-did-not-determine).

`HG-3` is therefore satisfiable **per series** for C-1. The qualifier "indicative" on the
`XNDXNNRJPY` tax rate is recorded as a precision limit, and the underlying withholding-tax document
remains unread (`O-2`).

### 6.3 The FX convention is documented, and no currency-version override was located

D-2 states that the foreign exchange rate is provided by the WM Company and, in the EOD index
calculation, is the closing spot rate at **16:00:00 UK time**, *"unless otherwise noted in the Index
Methodology"* — and D-2 states that the Manual applies to all Nasdaq Equity Indexes.

The escape clause was then tested directly. **D-1 contains zero occurrences of "currency", "foreign
exchange", "WM", or "JPY". D-4 contains zero occurrences of "foreign exchange" or "WM Company".**

> **Finding: no currency-version override to the WM 16:00:00 UK convention was located in the
> governing NDX Index Methodology or in the Nasdaq Index Methodology Guide.**

This resolves a long-standing repository unknown, previously recorded as "not exhaustively checked"
in [`phase1_fx_source_research.md`](phase1_fx_source_research.md) §8. Stated precisely: this is a
**documented absence in the two documents the escape clause points to** — not proof that no override
exists anywhere in Nasdaq's document set. It was reached solely from newly read Nasdaq documents; no
prior FX-decomposition finding was used.

`HG-4` is therefore satisfiable for C-1: FX is embedded, with a documented rate source, observation
time, and a stated alignment to the index calculation.

### 6.4 Restatement behaviour — first primary evidence

D-5 establishes that Nasdaq reserves the right to recalculate, restate, and republish index levels,
and states that intraday values are never recalculated while **EOD values will generally not be
recalculated for pricing errors below a 10 basis point materiality threshold**, with discretionary
exceptions including period-end dates and the day preceding a scheduled rebalance.

This is the project's first primary evidence that **Nasdaq index values can be restated**. It is a
direct `HG-9` / P1-9 input. No restatement testing was performed, so P1-9 does not advance beyond
PARTIAL on this evidence.

### 6.5 Calculation days

D-1 states the Index is calculated Monday through Friday except on days when the US markets are
closed. Recorded as documentary context only. **No date spine was retrieved**, consistent with
Stage-C boundaries, and this does not resolve the candidate-calendar question.

---

## 7. C-2A — QQQ NAV-based return construction

D-6 and D-8 state the same definition. Paraphrased, with the operative clause quoted because the
clause *is* the finding: NAV total return is computed from an initial investment at the NAV at the
start of the period, with *"reinvestment of all dividends and distributions at net asset value"*
during the period, and redemption at NAV on the final day.

**C-2A's reinvestment semantics are therefore established from primary evidence.** `HG-3` is
satisfiable for this component.

Both documents immediately qualify it: NAV total return includes adjustments under US GAAP, and as
such the NAV *for financial reporting purposes* and the returns based upon it **may differ from the
NAV and returns for shareholder transactions**.

Two distinct NAVs therefore exist, and returns computed on them may differ. Under the Owner's `HG-5`
scope interpretation these are **different observation bases**, so "C-2A" does not yet denote a
single observation basis: which NAV a construction uses must be specified before `HG-2` and `HG-5`
can be applied. This is `O-3`, and it is **OPEN**. The remediation confirmed that D-8 restates the
same caveat without resolving it.

Corroborating the NAV basis as Invesco's published performance basis — recorded as context, not
relied upon as a substitute for US regulatory evidence — D-13 states the fund's performance
computation basis as calendar-year-end, **NAV-to-NAV, with dividend reinvested**.

---

## 8. C-2B — market-price return construction

### 8.1 What is established

D-7 states the basis on which market returns are computed: *"Market returns are based on the
midpoint of the bid/ask spread at 4 p.m. ET and do not represent the returns an investor would
receive if shares were traded at other times."*

That sentence fixes an **observation basis** — bid/ask midpoint, 16:00 ET. It does not state a
return formula, a period convention, or any treatment of distributions.

### 8.2 What could not be established

After the controlling primary documents were retrieved and read in full, none of the following is
established by any primary source located:

1. the **calculation definition** of the market-price return series;
2. whether **distributions are included**;
3. if included, the **reinvestment assumption**;
4. the **price and timing** used for any such reinvestment;
5. whether Invesco publishes sufficient methodology to make the construction **reproducible**.

This is a **documented absence, not an unexhausted search**:

- D-8's Financial Highlights present **only** a net asset value total return. There is **no
  market-price total-return line item**.
- D-9 contains **no performance-calculation section** of any kind.
- D-10 discloses the bid-ask spread as an investor cost and points to published NAV, market price,
  premium/discount and spread data — without defining a market-price return.
- D-11 contains **no performance table**.
- Every "closing price", "last trade price", and "16:00 ET" reference located in D-8 and D-9
  concerns **valuation of the Fund's portfolio securities for NAV computation**, or the NAV
  calculation time and order cut-off — none concerns the return construction of QQQ shares.

### 8.3 What was refused

`HG-3` was **not** satisfied by substitution. Specifically, the C-2A reinvestment convention was
**not** carried across to C-2B, and no reinvestment semantics were inferred from NAV methodology,
industry convention, third-party adjusted-close methodology, empirical return behaviour, or any
similarity between the two bases.

One adjacent primary statement is recorded without inference: D-9 states that **no reinvestment
service is provided by the Trust**, while broker-dealers may make a DTC book-entry dividend
reinvestment service available. This is a fact about a **shareholder service**, not about
return-reporting methodology. Its only bearing here is that no fund-level reinvestment mechanism
exists, so any market-price total-return series would rest on an **assumed** convention that the
publisher has not published — which makes the gap structural rather than incidental.

### 8.4 Stop condition

> **`SC-1` is TRIGGERED for C-2B** — authoritative methodology cannot be identified.
>
> **`HG-2` and `HG-3` cannot be established for C-2B from primary evidence**, and could only be
> "satisfied" by importing researcher-selected conventions and presenting them as the publisher's.

This is a **qualification failure under this study's frozen evidence requirements**. It is
explicitly **not** a finding that market-price-based return construction is methodologically invalid
in general, nor a statement about the quality of QQQ as an instrument.

The disposition of C-2B is an Owner Decision, recorded in
[`phase1_primary_proxy_stage_c_closure_decision.md`](../decisions/phase1_primary_proxy_stage_c_closure_decision.md).

---

## 9. QQQ legal structure — J-2, with temporal provenance

The prior finding and the current finding are **both correct, for different dates**. The earlier
finding is not rewritten.

| Period | Structure | Evidence |
| ------ | --------- | -------- |
| **Before the reclassification** | Invesco QQQ Trust℠, Series 1 was a **unit investment trust** organized under New York law and registered under the 1940 Act | D-6, period ended 30 Sep 2025 — **correct for the dated evidence from which it was derived** |
| **After the reclassification** | QQQ operates as an **open-end management investment company** | D-8 and D-9, dated 22 Dec 2025 |

D-8 states that effective **after market close on 19 December 2025** the Fund was reclassified as an
open-end management investment company, and that prior to the Reclassification it operated as a
UIT. D-9 confirms the change of classification under the 1940 Act. D-12 records the provenance of
the proposal, whose stated purpose was to modernize the structure and reduce the overall expense
ratio.

> **The prior J-2 finding is SUPERSEDED as to current structure, not corrected as to its own date.**

---

## 10. Research-integrity findings

Recorded narrowly, because they bear on how much confidence any documentary finding deserves.

1. **Fluent but unrelated extraction output.** One document-fetch summarization returned fluent
   prose that had nothing to do with the requested fund document. Local extraction of the same file
   subsequently established that **the underlying primary PDF was itself valid and intact** — the
   fault lay in the summarization step, not in the source. The output was discarded and never
   entered the evidence.
2. **False-negative extraction.** A later extraction of primary regulatory PDFs initially returned
   **zero keyword hits across every search term**, because those documents mix plainly encoded text
   with subset-font and CMap-based encodings. The null result was implausible on its face — a
   prospectus containing no occurrence of "performance" is not credible — and was detected on that
   basis, corrected, and re-run. All findings in this artifact come from the corrected extraction.
   The correction was also applied retroactively to the previously read annual report, confirming
   that the earlier C-2B null result was genuine and not an extraction artifact.

> **The durable lesson: critical documentary evidence must be verified against the actual document.
> Fluent extraction output and zero-hit extraction are both untrustworthy without an integrity
> check — identity verification against the document's own cover text, and a plausibility check on
> the result.**

This is a **verification discipline**, not a tooling requirement. The implementation details of the
temporary extraction tooling used in this session are deliberately **not** recorded as a repository
architecture requirement, and no repository code was created.

---

## 11. Open items carried out of Stage C

Identifiers `O-1 … O-7` are **Stage-C-scoped** and are distinct from every frozen namespace.

| # | Item | Serves | Status |
| - | ---- | ------ | ------ |
| **O-1** | C-2B return definition and reinvestment semantics not established | `HG-2`, `HG-3` | **CLOSED BY DISPOSITION** — remediation exhausted; resolved by Owner Decision on C-2B, **not** by establishing the evidence |
| **O-2** | Nasdaq dividend-classification / withholding-tax-rates document referenced but not retrieved; the notional-net 30 % rate is *indicative* | `HG-3` precision | **OPEN** — routed to its later applicable stage |
| **O-3** | Two NAVs for the trust (financial-reporting vs shareholder-transaction); C-2A's observation basis not yet pinned | `HG-2`, `HG-5` | **OPEN — explicitly not resolved** |
| **O-4** | No methodology-version history obtained for D-1 / D-2; only current versions. Prior versions and change dates unestablished | `HG-8`, Stage D | **OPEN** — routed forward |
| **O-5** | D-1 carries no in-body effective date; only a copyright year and a PDF creation date | Document dating precision | **OPEN (low)** |
| **O-6** | Neither C-2 route has an established reproducible **daily** return construction published by Invesco — Invesco publishes period returns, not a daily series | `HG-2`, `HG-12` | **OPEN** |
| **O-7** | Trustee identity remains SECONDARY | Completeness | **OPEN (low)** |

### 11.1 New items routed to the later continuity stage

Both arose from primary evidence during the remediation. **Neither is investigated or adjudicated
here.**

| # | Item | Why it matters | Routing |
| - | ---- | -------------- | ------- |
| **N-2** | The 19 Dec 2025 reclassification is a **publisher-documented structural break** in QQQ's own history. Primary evidence states the Fund had the same investment objective and substantially similar investment policies **but differing expenses** when operating as a UIT | Historical continuity; comparability across the break; embedded-expense treatment; OD-11 | **Routed to the stage responsible for `HG-8` / historical continuity** |
| **N-3** | Nasdaq-100 Index methodology changes **effective 1 May 2026**, recorded in a prospectus supplement dated 30 Apr 2026 | Methodology-break documentation across the intended span | **Routed to the same later stage** |

---

## 12. What Stage C deliberately did not determine

Stated explicitly, because each is a live invitation to over-read the findings above:

- **Available history is not admissible history.** The JPY base date of 29 June 2020 recorded in
  D-3 is a **base-value date**, and this artifact draws **no** conclusion from it about when live
  publication began, whether pre-launch or back-tested history exists, or whether any segment is
  admissible. Admissibility under §6 and OD-12 is `OJ-1`, an Owner judgment, and it remains
  **UNDECIDED**.
- **No segment map exists.** Live / non-live characterized / non-live uncharacterized classification
  is Stage-D work and was not performed.
- **No licensing or redistribution assessment was performed.** `HG-11` and P1-8 are Stage-F work.
  No publisher's terms were read, so **every source above is UNCLEAR as to redistribution** and none
  is cleared for republication.
- **No FX source or convention was selected** for the C-2 route.
- **No candidate calendar was adopted.**

---

## 13. Phase-1 requirement impact

No item is upgraded merely because this artifact exists.
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements)
remains the authoritative register.

| # | Requirement | Status | Basis |
| - | ----------- | ------ | ----- |
| **P1-2** | Approved Primary Proxy | **OPEN** | No candidate was qualified, ranked, or approved. Stage C establishes documentary inputs only |
| **P1-3** | Proxy return composition | **ADVANCED — not resolved** | Determinate per series for C-1 and for C-2A from primary evidence; **not** established for C-2B. The Nissay-side question is separately bounded and untouched here |
| **P1-7** | Currency treatment | **ADVANCED** | The Nasdaq-side convention is pinned and the override question is now answered as a documented absence in the governing documents. The C-2 route's FX component remains unidentified by design |
| **P1-8** | Licensing / redistribution | **UNCHANGED** | No terms were read at Stage C. Nothing is cleared for redistribution |
| **P1-9** | Revision / restatement behaviour | **ADVANCED — remains PARTIAL** | First primary evidence that Nasdaq EOD values can be restated, with a 10 bps materiality threshold and reserved discretion. No restatement testing performed |
| **P1-4** | Cost / expense treatment | **UNCHANGED in quantity** | `HG-10` is satisfiable in kind for both routes; no expense ratio or tracking-difference quantity was retrieved, computed, or cited |

---

## 14. Publication boundary

- **No publisher document is reproduced in this repository.** All retrieved PDFs and pages are
  retained outside it. Redistribution terms for Nasdaq and Invesco material have **not** been
  assessed, so fail-closed treatment applies.
- **Quotation is minimal and evidentiary.** Short clauses are quoted only where the clause is
  itself the finding — a return-composition definition, an FX convention, a basis statement, a
  reclassification statement. Everything else is paraphrased with precise document identity, so a
  third party can retrieve the same document and verify.
- **No raw series, of any kind, appears here** — no index values, no NAVs, no prices, no FX rates,
  no date spines.
- **No performance values appear here.** Published period returns for QQQ were visible in D-8 while
  locating the methodology footnote in the same section. They were **not** recorded, compared, or
  used, and they play no part in any finding.
- **No `ND-1 … ND-7` material was used or restated.**
- **No personal information and no credentials appear here**, and none was transmitted during the
  research.

---

## 15. External working material boundary

Source documents live **structurally outside** the repository, never in an ignored repository
directory. This artifact carries sufficient provenance — publisher, exact document title, date or
version, and locator — for any future researcher to retrieve each source independently. That
provenance, not the retained binary, is what makes the finding auditable.

The retained working copies were held in a **session-scoped** location, which is not durable
storage. A persistent external location is proposed for Owner decision in the closure decision
artifact, [§7](../decisions/phase1_primary_proxy_stage_c_closure_decision.md#7-external-research-material-retention--owner-decision-required).
**No file was moved
in the task that produced this artifact.**

---

## 16. What this artifact establishes

1. C-1's methodology chain is **reconstructable from primary Nasdaq documents**, and return
   composition is determinate **per series**.
2. Nasdaq's EOD FX convention is documented, and **no currency-version override was located** in the
   two governing documents the escape clause points to.
3. Nasdaq **can restate** EOD index values, subject to a stated 10 bps materiality threshold.
4. C-2A's reinvestment semantics are established from primary evidence, **subject to an unresolved
   two-NAV ambiguity**.
5. C-2B's return construction, distribution inclusion, and reinvestment semantics are **not
   established**, and the controlling primary documents have been read and do not contain them.
6. QQQ's legal structure **changed on 19 December 2025**, with both the prior and current states
   correctly dated.

## 17. What this artifact does NOT establish

1. That any candidate is qualified. **No candidate passed a full gate assessment** — Stages D
   through G were not performed.
2. That any candidate is preferable to another. **No comparison of any kind was made.**
3. That any history is admissible, or that any segment is live.
4. That any source may be redistributed, or that derived results may be published.
5. That C-2A is usable as a single observation basis — `O-3` is open.
6. That market-price return construction is invalid in general. **C-2B failed *this study's*
   evidence requirements.**

---

## 18. Limitations

- Stage C is a **documentary** stage. Every finding is a statement about what publishers document,
  not about how any series behaves.
- Nasdaq methodology **version history was not obtained** (`O-4`); only current versions were read.
  Statements about "the governing document" are statements about the current version.
- The documented absence of an FX override is bounded to D-1 and D-4. It is not a claim about
  Nasdaq's entire document set.
- One referenced Nasdaq document was never retrieved (`O-2`), leaving the notional-net tax
  treatment at its publisher-stated "indicative" precision.
- SEC EDGAR was unavailable throughout under the applicable privacy boundary. Findings drawn from
  issuer-published copies of regulatory documents are primary, but no filing was read from the
  regulator's own repository.

---

## 19. Confirmations

- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked, scored, weighted, or selected.** No qualification criterion was
  amended, added, renumbered, or re-weighted; the criteria-freeze boundary at commit `1e8bc85`
  stands.
- **No performance quantity was computed at any stage.** No returns, correlations, tracking error,
  RMSE, MAE, drawdowns, or strategy outcomes.
- **`ND-1 … ND-7` were not used.**
- **No Baseline Start Date and no Dataset Cutoff were chosen.** No admissibility decision was made
  about pre-launch or non-live history.
- **No FX source or convention was selected.**
- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **No raw dataset and no publisher document is committed to this repository.**
- **Stage D has not begun.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Evidence Artifact. Owner Review: PENDING. Primary Proxy: NOT APPROVED — P1-2
remains OPEN. Phase 2: BLOCKED.**
