# Phase 1 Evidence Artifact — FX Data Source Availability and Licensing

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **FX Data Source Availability and Licensing** |
| Research date | **2026-08-11** (all source access dates 2026-08-11) |
| Owner Review | **APPROVED** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| FX source approval status | **No FX source approved by this study** |
| Phase 2 | **BLOCKED** |

> **What the approval means.** The Owner has approved **the research evidence recorded in
> this artifact** — the sources examined, what each was found to establish, the access and
> licensing findings, and the stated limits.
>
> The Owner has **not**, by approving this artifact, approved any FX source, any Primary
> Proxy, or any Baseline FX convention. A separate, narrowly scoped Owner Decision on the
> Japan-side TTM candidate is recorded in
> [`docs/decisions/phase1_ttm_qualification_decision.md`](../decisions/phase1_ttm_qualification_decision.md).

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and does
not govern Baseline behavior. The Phase-0 decision history is
[`docs/decisions/phase0_baseline_decisions.md`](../decisions/phase0_baseline_decisions.md).
This artifact records Phase-1 **evidence** only.

**Provenance note.** This artifact was reconstructed from a Research Working Record rescued
from the research session of 2026-08-11. The working record was a manual copy of terminal
output; its table formatting was degraded in transit and has been repaired here. Semantic
content is preserved. Where the working record's source URLs were truncated during manual
copying, the full URL has been restored **only** where it appears elsewhere within the same
working record; otherwise the source is cited by publisher, document title, and host.

---

## 2. Research objective

> **What authoritative or near-authoritative USD/JPY daily FX series can be used for local
> research, with sufficient historical coverage and sufficiently clear licensing and access
> terms, to support a future Phase-1 FX residual-decomposition study?**

The study was a **source survey and licensing assessment only**. It performed no
decomposition, constructed no synthetic series, and was explicitly not permitted to approve a
source.

Sources were investigated in a declared priority order: primary monetary and public
authorities first; then primary commercial benchmark providers; then institutional or
near-primary sources including Japanese-bank TTM publications; and finally secondary
aggregators, admitted for discovery and cross-checking only and never promoted to authority.

For each candidate the study separated **source authority**, **data definition**,
**timestamp / fixing convention**, **historical coverage**, **access method**, **licensing and
redistribution**, and **suitability for local analysis** — deliberately, so that a source
strong on one dimension could not be credited for another.

---

## 3. Principal findings

### 3.1 The Nasdaq-side FX convention is documented and pinned

Two Nasdaq documents were read directly and state the same convention:

- **Nasdaq Global Index Family Methodology**, §4.2 *Foreign Exchange Rate*, **page 14**:
  *"The Global Index Family uses the WM Company, Closing Spot Rates at 16:00:00 UK time in the
  calculation of the closing Index Values. SIX Financial Information Intraday Spot Rates are
  applied to the real time Index calculations during the trading day."*
- **Nasdaq Calculation Manual — Equities & Commodities, 20 May 2026**, definitions section:
  the FX rate *"is provided by the WM Company … and in the calculation of the EOD Index Value
  is the closing spot rate at 16:00:00 UK time, unless otherwise noted in the Index
  Methodology. Intraday spot rates are applied to the real time index calculations during the
  index calculation day."* The manual states it *"shall apply to all Nasdaq Equity Indexes."*

The Calculation Manual is the broader document and covers the NDX currency versions, so the
16:00 UK convention applies to `NDXJPY` / `XNDXJPY` / `XNDXNNRJPY` **unless a specific index
methodology overrides it**. No override was located, but not every NDX currency-version
methodology document was checked — recorded as a residual unknown (§8).

### 3.2 WMR is the structurally correct Nasdaq-side input and is not publicly obtainable

WMR FX Benchmarks are administered by **FTSE International Limited**, authorised as a
Benchmark Administrator and regulated in the UK by the FCA (reference number 796803). Daily
Closing rates are published at **4:00 pm London**, Monday–Friday. LSEG states benchmark data
*"is made available on LSEG Data & Analytics platforms, through direct data feeds and APIs and
is widely available through other third-party market data vendors and authorised
redistributors."*

- Historical availability is described as *"All rates are archived daily and are available
  direct from us and other vendors"*; **no commencement date appears on that page**. LSEG
  factsheet material reporting Closing Spot history since 1994 is **Secondary** and was not
  primary-verified.
- The current methodology document — *Methodology: WMR FX Benchmarks, Spot, Forward, NDF and
  Metal Rates*, **v30, January 2026** — was identified by title and version, but **its body
  text was not machine-extractable** in the research environment. The 5-minute fix window and
  volume-weighted-median construction are **Secondary-reported and not primary-verified here**.
- The evidence supports the conclusion that **historical WMR data require a licence**: no
  single price statement was found, but administration under UK BMR, delivery via "authorised
  redistributors", and the fact that the WMR Republication Policy is written entirely in terms
  of **"subscribers"** together support it.
- Obtaining 16:00 UK observations for local research without redistribution rights was **not
  established by any route found**. No licensed data was acquired.

**Consequence.** Direct comparison against Nasdaq's own FX input is **not realistically
possible** for this research repository without a commercial licence, and such a licence would
not confer redistribution rights. Any FX decomposition must proceed with a **publicly sourced
approximation** of the 16:00 UK observation and must state that it is an approximation.

**Incidental P1-9 finding.** The *Republication of the WMR FX Benchmark Rates Policy*, **v2.0,
December 2025**, establishes that WMR benchmark rates **can be restated after publication**: an
internal quality-control finding or a subscriber query triggers a **Price Challenge**
investigation, whose findings *"may necessitate the republication of the benchmark rate
challenged."* FTSE Russell notifies subscribers and retains republication records for a minimum
of five years. The policy also begins a sentence bounding the amendment window — *"Please note
that under no circumstances will a benchmark for one day be amended after the publication of
…"* — which the working record's extraction **truncated**; it is **not** completed by
inference here. Whether any restatement affected the study window, and whether Nasdaq
recalculates index values when one occurs, is **unknown and unexamined**.

### 3.3 BOJ provides authoritative Tokyo USD/JPY spot data with clear observation timing

Read directly from the BOJ Time-Series Data Search main table `fm08_d_1`, decoded from
Shift_JIS:

- Table: 為替相場（東京インターバンク相場）（日次）
- **`FM08'FXERD04`** — 東京市場 ドル・円 スポット **17時時点**; unit **￥／＄**; 収録開始期
  **1998-01-05**; 収録終了期 **2026-08-06**; 最終更新日 **2026-08-10**
- **`FM08'FXERD05`** — 東京市場 ドル・円 スポット **中心相場**; unit ￥／＄; 収録開始期
  **1999-01-01**; same end and update dates

Direction is **yen per USD**, the same direction the Nissay NAV conversion requires.

**Definition (Primary).** The BOJ 外国為替市況（日次）page states that the 9:00 and 17:00 spot
rates are 「オファーとビッドの中間値」 — the midpoint of offer and bid. The same page carries a
material caveat: 「本統計は、外国為替市場参加者からの情報を基に作成しており、**訂正が入る可能性
がある**旨ご留意ください」 — the statistic is compiled from market-participant information and
**may be subject to correction**. That is a direct P1-9 input.

**Coverage measured over the study window (2023-03-31 → 2026-08-10):**

| Measure | Value |
| ------- | ----- |
| Calendar rows in window | 1,226 |
| `FXERD04` numeric observations | **820** |
| `FXERD05` numeric observations | **820** |
| `NA` (non-business days) | 405 |
| `ND` | 0 |
| Last available observation | **2026-08-06** |
| 2026-08-07 / 2026-08-10 | **absent from this table** |

Spot-checks recorded against dates relevant to the approved alignment artifact (FXERD04 /
FXERD05): 2024-08-05 = 143.5 / 145.65; 2024-08-06 = 145.3 / 145.02; 2024-08-07 = 146.7 /
144.75; 2025-04-04 = 146.28 / 145.94.

Two findings recorded for the Owner:

1. **Coverage falls two business days short of the fixed Empirical Alignment Study Cutoff of
   2026-08-10.** The BOJ time-series site lags; the separate 70-business-day page carries the
   more recent values. Any study reusing the 2026-08-10 cutoff must either combine two BOJ
   pages or accept a shortened FX window, and **must record which it did**.
2. The 820 business-day count in this window coincides with the N = 820 return pairs at lag −1
   in the approved alignment artifact. This is **a count-level coincidence only**. The fund NAV
   date list was not available and **no date-by-date match was performed**. It must not be
   treated as established calendar equivalence.

**Terms.** The BOJ copyright page permits reproduction subject to the requirement
「出所を明記してください」, with three stated exceptions: 商用目的; content marked
「無断転載・複製を禁じます」; and photographs, illustrations, or image data. It also states
「当サイトの内容については、日本銀行に無断で改変を行うことはできません」 and disclaims
responsibility for users' actions. The Time-Series site's notice page carries equivalent
conditions and **refers to separate API usage terms** (`api_notice.pdf`), which could not be
extracted (§8).

**Recorded explicitly:** BOJ publishes an authoritative, clearly timestamped daily USD/JPY
series. **It is not a TTM**, and it is **not** the 「対顧客電信売買相場の仲値」 concept named in
the Nissay 請求目論見書. It must not be preferred merely because it is public and Japanese.

### 3.4 FRB H.10 provides a public-authority noon-New-York USD/JPY series

- **Definition (Primary):** *"noon buying rates in New York for cable transfers payable in the
  listed currencies"*; the rates *"have been certified by the Federal Reserve Bank of New York
  for customs purposes."*
- **Revision behaviour (Primary):** the release states that *"past releases are not revised."*
  This stands in contrast to the correction and restatement mechanisms documented for BOJ, WMR,
  and the Japanese-bank TTM sources.
- **Japan historical file:** *"Historical Rates for the Japanese Yen (Rates in Japanese yen per
  U.S. dollar)"*; daily; `ND` marks non-trading days; read through **31-JUL-26** at access
  time, on a weekly release cadence.
- **Terms:** **no explicit terms, copyright, or public-domain statement was located.** The
  Board's linking-policies page addresses only *third-party* content on linked sites —
  *"Permission to use copyrighted materials must be obtained from the original source and
  cannot be obtained from the Board."* Recorded as **UNCLEAR**, not assumed public domain.

**FRED (`DEXJPUS`) is a distributor, not the originator, and was inaccessible.** Four access
attempts failed: `WebFetch` on the series page, the trailing-slash series page, and the data
page each returned **HTTP 403**; `curl` with a browser user-agent over IPv4 failed to connect
twice. The series page, its Notes, its date range, its last-updated stamp, and any FRED terms
statement were therefore **not read**. Search metadata consistently reports DEXJPUS as
originating from the H.10 release with the Board of Governors as source — **Secondary, medium
confidence**. Since the upstream H.10 is directly readable, **there is no reason to route
through FRED**, and FRED does not remove upstream licensing constraints.

One operational note (**Secondary**): search results indicate the Board is retiring its Data
Download Program and directing users toward FRED. If that proceeds, FRED could become the
practical access path even though H.10 remains the originator. That is a future-access risk,
not a present one.

### 3.5 BOJ spot is not equivalent to the Nissay customer TTM concept

The Nissay 請求目論見書 valuation rule cited in the approved alignment artifact converts
foreign-currency assets at 「国内における計算日の対顧客電信売買相場の仲値」. The matching public
concept is a Japanese bank's **公表仲値 / TTM** — a customer-facing (対顧客) rate — **not** an
interbank spot observation. BOJ `FM08'FXERD04` is an interbank spot midpoint at 17:00 JST and
is therefore a **different rate concept observed at a different time of day**.

This distinction is the reason the study concluded that the Japan-side leg, not the index-side
leg, was the binding source-qualification question.

### 3.6 MUFG/MURC emerged as the strongest Japan-side TTM candidate

Read directly (**Near-primary**: the rate originates with MUFG Bank; the archive site is
operated by 三菱UFJリサーチ&コンサルティング (MURC), which transcribes it):

- **Definition (verbatim, live page as of 2026-08-10):**
  「なお、公表仲値（TTM）は、TTSとTTBの中間の相場であり、（TTS＋TTB）/2で算出されます。」
- **Scope:** 「三菱UFJ銀行公表の対顧客外国為替相場 / MUFG Bank, Ltd. Exchange Quotations」 —
  the 対顧客 rate, matching the Nissay concept class.
- **History:** 「1990年以降の為替相場 / Daily Exchange Quotations - since 1990 -」, daily, with
  per-year Excel files (`murc_1990.xls` … through 2026).
- **Documented source-bank chain:** 1990/01–1996/03 旧東京銀行 → 1996/04–2005/12 旧東京三菱銀行
  → 2006/01–2018/03 三菱東京UFJ銀行 → 2018/04 以降 三菱UFJ銀行. The entire 2023-03-31 →
  2026-08-10 window falls in the final, single-entity segment — **no source-bank discontinuity
  inside the study window**.
- **Publication timing:** the MURC index page states the table is updated around 11:00.

Two caveats were recorded verbatim:

1. **Transcription fidelity is expressly not guaranteed:**
   「当サイトにおける『1990年以降の為替相場』につきましては、銀行発表の最終公表相場から転記して
   掲載しており、可能な限り正確性を期しておりますが、データ引用元との整合性や信頼性を完全に保証
   するものではありません。あくまで参考値としてご参照ください。また情報の利用により生じたいかなる
   損害についても、一切の責任を負いかねますので、ご了承ください。」
2. **Re-fixing (第2次公表相場) is real and occurred inside the study window.** The site carries
   an 【お知らせ】 stating that on 8月7日(水) the published rate was suspended owing to market
   movement and a 第2次公表相場 was announced, and on the historical page:
   「『1990年以降の為替相場』掲載の 2024年8月7日付の為替相場は、第2次公表相場を掲載しております。」

**2024-08-07 is the day immediately after 2024-08-06**, one of the four Large-Drop zone entry
dates recorded in the approved alignment artifact §11. This adjacency is recorded as
**motivation for careful handling only. No causal relationship is claimed, tested, or implied.**
It is also a restatement behaviour relevant to P1-9: the archive shows the final rate, not the
first-published rate, so a naive historical download is **not** a point-in-time record.

This finding is the reason the study's single recommendation was a further, narrowly scoped
Japan-side TTM qualification — carried out subsequently and recorded in
[`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md), which
supersedes this section's necessarily preliminary treatment.

### 3.7 Mizuho remained access-unresolved

`https://www.mizuhobank.co.jp/market/historical/index.html` and
`/market/historical/backnumber_a/index.html` returned **HTTP 403**, and **`robots.txt` itself
returned 403** from an Akamai edge ("Access Denied", reference
`18.f530d417.1786415682.26f47784`). The page, the data definitions, the file formats, and any
terms were **not read**. Secondary search results describing 公示相場（仲値）CSV/text downloads
from 2002-04-01 are **unverified and are not relied upon**.

Because `robots.txt` itself was unreadable, **the automated-access policy could not be read**,
let alone complied with. No automated access was or should be attempted until this is resolved
through a permitted path.

### 3.8 SMBC was unsuitable for the intended machine-readable historical study

`www2.smbc.co.jp/market/backnumber/fixing/past.html` was reachable but encoding-garbled. What
was legible is a set of **monthly PDF files** (~127–130 KB each) covering roughly the last 12
months, described in search results as 公表相場仲値推移一覧. **PDF-only, monthly, shallow
archive** — unsuitable for a daily-alignment study without heavy extraction work. No terms
statement was legible.

### 3.9 Licensing and redistribution remain a material constraint

Across the entire survey, **exactly one source is clearly restricted** (WMR) and **exactly one
carries an explicit attribution-conditioned reproduction permission** (BOJ). Every other
candidate is **UNCLEAR** for redistribution rather than clearly permitted, and two could not be
read at all. **Nothing is cleared for redistribution, and nothing is cleared for committing raw
values to this public repository.** See the licensing matrix in §6.

---

## 4. Source inventory

| Source | Publisher | Tier | Series / rate | What it establishes | URL / locator |
| ------ | --------- | ---- | ------------- | ------------------- | ------------- |
| BOJ Foreign Exchange Rates (Daily) | Bank of Japan | 1 | 東京市場 ドル・円 スポット 17時時点 | Rate is the mid of offer and bid; 9:00 and 17:00 JST observations; last 70 business days; long history via stat-search | `boj.or.jp/en/statistics/market/forex/fxdaily/index.htm`; JP: `boj.or.jp/statistics/market/forex/fxdaily/index.htm` |
| BOJ Time-Series Data Search, table `fm08_d_1` | Bank of Japan | 1 | `FM08'FXERD04` (17時時点), `FM08'FXERD05` (中心相場) | Exact data codes, unit ￥／＄, coverage 1998-01-05 / 1999-01-01 → 2026-08-06, last updated 2026-08-10 | `stat-search.boj.or.jp/ssi/mtshtml/fm08_d_1.html` |
| BOJ 著作権・免責事項 | Bank of Japan | 1 | — | Reproduction permitted with attribution; 3 stated exceptions | `boj.or.jp/about/copyright.htm` |
| BOJ stat-search 利用上の留意点 | Bank of Japan | 1 | — | Equivalent conditions; refers to separate API terms | `stat-search.boj.or.jp/info/notice.html` |
| H.10 Foreign Exchange Rates — About | Federal Reserve Board | 1 | H.10 | "noon buying rates in New York for cable transfers"; certified by FRBNY; "past releases are not revised" | `federalreserve.gov/releases/h10/about.htm` |
| H.10 historical — Japan | Federal Reserve Board | 1 | JAPAN yen | "Rates in Japanese yen per U.S. dollar"; daily; `ND` for non-trading days; read through 31-JUL-26 | `federalreserve.gov/releases/h10/hist/dat00_ja.htm` |
| FRB website linking policies | Federal Reserve Board | 1 | — | No copyright / public-domain statement for Board content; third-party caveat only | `federalreserve.gov/website-linking-policies.htm` |
| FRED `DEXJPUS` | Federal Reserve Bank of St. Louis (distributor) | 1 (distributor) | `DEXJPUS` | Distributes H.10; **page inaccessible from the research environment** | `fred.stlouisfed.org/series/DEXJPUS` |
| Euro foreign exchange reference rates | European Central Bank | 1 | EUR-base reference rates | **No direct USD/JPY**; ~14:10–14:15 CET concertation, ~16:00 CET publication; "using the rates for transaction purposes is strongly discouraged" | `ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html` |
| BIS bilateral exchange rates | Bank for International Settlements | 1 (distributor) | `WS_XRU` | Daily USD rates, ~80 economies; ECB is primary source for recent daily data, complemented by the Fed | `data.bis.org` |
| Nasdaq Global Index Family Methodology | Nasdaq, Inc. | — (context) | §4.2, p.14 | "uses the WM Company, Closing Spot Rates at 16:00:00 UK time in the calculation of the closing Index Values" | `indexes.nasdaqomx.com/docs/NQGIFamilyMethodology.pdf` |
| Nasdaq Calculation Manual — Equities & Commodities, 20 May 2026 | Nasdaq, Inc. | — (context) | definitions section | FX "is provided by the WM Company … the closing spot rate at 16:00:00 UK time, unless otherwise noted"; applies to all Nasdaq Equity Indexes | `indexes.nasdaqomx.com`, Calculation Manual PDF |
| WMR FX Benchmarks | LSEG / FTSE Russell | 2 | Closing Spot 16:00 UK | Administered by FTSE International Limited; 4pm London daily; "available direct from us and other vendors"; subscriber model | `lseg.com/en/ftse-russell/benchmarks/wmr-fx-benchmarks` |
| WMR Republication of Benchmark Rates Policy v2.0, Dec 2025 | FTSE Russell | 2 | — | WMR rates can be republished (restated) after a Price Challenge; subscribers notified; records kept ≥5 years | `lseg.com`, WMR republication rates policy PDF |
| WMR FX Methodology v30, January 2026 | FTSE Russell | 2 | — | Current methodology version identified; body text not machine-extractable in the research environment | `lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/wmr-fx-methodology.pdf` |
| 外国為替相場情報 — 本日の為替相場 | MUFG Bank via MURC | 3 | 公表仲値 (TTM) | 「公表仲値（TTM）は、TTSとTTBの中間の相場であり、（TTS＋TTB）/2で算出されます」; page as of 2026-08-10 | `murc-kawasesouba.jp/fx/index.php` |
| 1990年以降の為替相場 | MUFG Bank via MURC | 3 | 対顧客外国為替相場, daily since 1990 | Per-year Excel `murc_YYYY.xls` 1990→2026; 第2次公表相場 events; transcription disclaimer; documented source-bank chain | `murc-kawasesouba.jp/fx/past_3month.php` |
| MURC 外国為替相場情報のご案内・よくあるご質問 | MURC | 3 | — | FAQ covering publication timing, re-fixing, data-file cadence | `murc-kawasesouba.jp/fx/faq/faq.pdf` |
| ヒストリカルデータ / 外国為替公示相場 | Mizuho Bank | 3 | 公示相場 仲値 (TTM), CSV | **Blocked (HTTP 403)**; secondary reports indicate CSV from 2002-04-01 (unverified) | `mizuhobank.co.jp/market/historical/index.html` |
| 外国為替情報 バックナンバー | 三井住友銀行 (SMBC) | 3 | 公表相場仲値推移一覧 | Monthly PDF archives; visible archive ≈12 months; not machine-readable | `www2.smbc.co.jp/market/backnumber/fixing/past.html` |

Sources consulted and found **inaccessible or non-existent** are recorded in §8.

---

## 5. Candidate comparison

| Candidate | Authority | Rate definition | Observation time | Coverage (2023-03-31 → 2026-08-10) | Access | Licensing | Study suitability |
| --------- | --------- | --------------- | ---------------- | ---------------------------------- | ------ | --------- | ----------------- |
| **BOJ `FM08'FXERD04`** | Primary (central bank) | Tokyo interbank spot, mid of offer/bid | 17:00 JST, documented | 820 obs; ends 2026-08-06 (2 business days short) | Public HTML table, Shift_JIS; API exists (separate terms) | Reproduction permitted with attribution; API terms unread | High for a Japan-side timing leg — **but not a TTM** |
| **BOJ `FM08'FXERD05`** | Primary | Tokyo 中心相場 (central rate) | Same table; **concept not defined on the page** | 820 obs, same end date | Same | Same | Medium — definition unresolved; **do not treat as interchangeable with `FXERD04`** |
| **FRB H.10 (Japan)** | Primary (central bank) | Noon buying rate, New York, cable transfers, certified by FRBNY | 12:00 New York time; offset from the 16:00 UK fix is **date-dependent** (§7) | Daily from 1971; historical file read through 2026-07-31 | Public HTML; weekly release | No terms statement located → UNCLEAR | Strongest for the index-side leg: closest freely available public series in observation time to Nasdaq's WM input; explicitly **not revised** |
| **FRED `DEXJPUS`** | Distributor of H.10 | Same as H.10 | Same | Same as H.10 | **Inaccessible from the research environment (403 / connection failure)** | Does not remove upstream terms | Redundant — use H.10 upstream instead |
| **ECB reference rates** | Primary | EUR-base reference rates | ~14:10–14:15 CET concertation; published ~16:00 CET | Full; **USD/JPY only as a derived cross** | CSV / XML / SDMX | "for information purposes only"; transaction use "strongly discouraged" | Low — cross-derivation adds a second convention; wrong time zone for both legs |
| **BIS `WS_XRU`** | Distributor | Mixed provenance | **Inherits ECB/Fed timing — not uniform** | Long | Portal / SDMX | BIS copyright; terms not read | Low — provenance mixing defeats the purpose of a timing study |
| **WMR Closing Spot 16:00 UK** | Primary benchmark administrator | Volume-weighted median over a fix window (Secondary-reported) | 16:00:00 UK, documented | 1994→ per LSEG material (Secondary) | **Subscription only** | **CLEARLY RESTRICTED** | Ideal but unobtainable — this is Nasdaq's actual input |
| **MUFG TTM (via MURC)** | Near-primary (bank rate, third-party transcription) | 対顧客 TTM = (TTS + TTB) / 2 | ~09:55 JST reference / ~10:00 publication — **convention, not primary-documented** | Daily since 1990 | Per-year `.xls`, public | UNCLEAR — disclaimer found; no grant or prohibition located | Highest structural relevance to the Nissay NAV concept; weakest on terms and on transcription fidelity |
| **Mizuho 公示相場** | Near-primary | 公示相場 仲値 (TTM) | Same convention | Reported from 2002-04-01 (unverified) | **403 blocked**; CSV reported | UNCLEAR / unread | Potentially strong; **cannot be assessed without access** |
| **SMBC 公表相場仲値** | Near-primary | 公表相場仲値 | Same convention | Monthly PDFs, shallow archive | PDF only | Unread | Low — format and archive depth unsuitable |
| **Yahoo / Stooq / Investing.com etc.** | Secondary | Undefined / vendor-composite | **Typically undocumented** | Long | Easy | Varies, often restrictive | **Discovery and cross-check only — must not be promoted** |

---

## 6. Licensing matrix

Labels reflect **what the evidence actually read supports** — not what is probable. Where a
terms statement could not be read, the label is **UNCLEAR**, including where a permissive
outcome seems likely.

| Source | Local viewing | Download | Local analysis | Automation | Raw redistribution | Derived statistics |
| ------ | ------------- | -------- | -------------- | ---------- | ------------------ | ------------------ |
| **BOJ (fxdaily / stat-search)** | PERMITTED | PERMITTED | PERMITTED | UNCLEAR (separate API terms unread) | UNCLEAR — permitted with attribution, but excludes 商用目的 and marked content | PERMITTED with attribution (same exceptions) |
| **FRB H.10 (incl. Japan historical file)** | PERMITTED | PERMITTED | UNCLEAR | UNCLEAR (no scraping statement either way) | UNCLEAR — no copyright or public-domain statement located | UNCLEAR |
| **FRED (`DEXJPUS`)** | UNCLEAR (inaccessible) | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR — does not remove upstream terms | UNCLEAR |
| **ECB reference rates** | PERMITTED | PERMITTED | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR — published "for information purposes only" |
| **BIS `WS_XRU`** | PERMITTED | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR (BIS copyright asserted) | UNCLEAR |
| **WMR (LSEG / FTSE Russell)** | **RESTRICTED** | **RESTRICTED** | **RESTRICTED** (subscription) | **RESTRICTED** | **RESTRICTED** | RESTRICTED / UNCLEAR — governed by licence terms not obtained |
| **MUFG TTM via MURC** | PERMITTED | PERMITTED (public `.xls`) | UNCLEAR | UNCLEAR | UNCLEAR — no grant and no prohibition located | UNCLEAR |
| **Mizuho 公示相場** | UNCLEAR (403) | UNCLEAR | UNCLEAR | UNCLEAR — **do not automate** (`robots.txt` itself returned 403) | UNCLEAR | UNCLEAR |
| **SMBC 公表相場仲値** | PERMITTED | PERMITTED (PDF) | UNCLEAR | UNCLEAR | UNCLEAR | UNCLEAR |
| **Tier-4 secondary sources** | Varies | Varies | UNCLEAR | Often RESTRICTED | Generally RESTRICTED | UNCLEAR |

> **No legal conclusion is drawn in this table.** In particular, it is **not** asserted that
> U.S. federal government data is public domain: the Federal Reserve Board's linking-policies
> page contains no such statement, and its only copyright language refers to third-party
> content on linked sites.

The MUFG and MURC rows above are **superseded in detail** by the separated, per-publisher
matrices in [`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md)
§9, which read MUFG's site terms directly and established that MURC publishes no terms page.

---

## 7. Timezone discipline and the structural hypothesis

### 7.1 Timezone discipline — binding on all future FX work

JST observes **no** daylight saving. The United Kingdom and the United States both do, on
transition dates that are **not always identical**. Therefore:

- **No fixed-hour relationship between a JST, London, or New York observation may be asserted.**
- Any relative-timing statement must be computed with **calendar-aware timezone conversion per
  observation date**, not with a constant offset.
- In particular, it must **not** be stated that FRB H.10's noon-New-York observation is always
  a fixed interval after the WMR 16:00 UK fix. The interval is date-dependent.

The approximate figures in §7.2 are retained because they motivated the research direction.
They are **illustrative and must be re-derived per date** before any analytical use.

### 7.2 Structural hypothesis — a hypothesis, not a finding

Combining only documented observation times, and treating every interval as **approximate and
date-dependent**:

- The WM fix at 16:00 London falls **before** the U.S. equity close it is paired with.
- The FRB noon New York observation falls **after** that WM fix and still before the U.S. close.
- A Japan TTM struck in the Japanese morning falls **after** the preceding U.S. close.
- The BOJ 17:00 JST observation falls later still on the same Japanese day.

On documented times alone, the Nasdaq and Nissay conversion points therefore sit on
**opposite sides of the U.S. close** and are separated by a substantial, date-dependent
interval.

> This is a **coherent structural reason why an FX-convention difference could contribute
> materially** to the ≈ 9.52 %/yr residual recorded in
> [`phase1_empirical_alignment_study.md`](phase1_empirical_alignment_study.md) §12.
>
> **It is the hypothesis the next approved study exists to test. It is not a result.**
> **FX has NOT been shown to be the dominant cause of the residual, and no such claim is made.**

The Japan-morning leg of this reasoning additionally rests on a fixing time that is
**Secondary-sourced** and on a convention **Nissay has not confirmed it uses**.

---

## 8. Remaining unknowns

### Access failures, recorded explicitly

1. **FRED** — all four attempts failed (403 via fetch tool; connection failure via curl). Series
   page, Notes, date range, and FRED terms **unread**.
2. **Mizuho Bank** — HTTP 403 on both the historical page and `robots.txt`. Data definitions,
   formats, coverage, and terms **unread**; automated-access permissibility **undeterminable**.
3. **BOJ `api_notice.pdf`** — could not be text-extracted. **BOJ API terms unknown**, so
   automated retrieval from BOJ is unassessed.
4. **WMR FX Methodology v30** — identity and version confirmed; **body text not extractable**.
   Fix-window length, USD/JPY quote convention, holiday rules, and history start date are **not
   primary-verified**.
5. **SMBC** — page encoding garbled; rate definition and terms **not legible**.
6. **MURC / MUFG terms** — no terms-of-use or copyright page located during this study (two
   candidate URLs returned 404). Only the on-page disclaimer was found. *(Subsequently resolved
   in part by the Japan-side TTM qualification study, which located and read MUFG's site terms.)*
7. **Federal Reserve Board terms** — two candidate terms URLs returned 404; no Board-content
   copyright or reuse statement located.

### Substantive unknowns

8. Nissay's **benchmark FX provider, fixing time, rate type, holiday convention, rounding, and
   fallback rules** — all still undisclosed (carried forward from the approved alignment
   artifact).
9. Whether any **NDX currency-version-specific methodology overrides** the WM 16:00 UK
   convention ("unless otherwise noted in the Index Methodology"). Not exhaustively checked.
10. Whether **WMR republications** occurred during 2023-03-31 → 2026-08-10, and whether Nasdaq
    recalculates index values when they do.
11. Whether **BOJ corrections** occurred in the window.
12. The **complete list of 第2次公表相場 dates** in the window — only 2024-08-07 was surfaced by
    a site notice during this study. *(Subsequently narrowed by the Japan-side TTM qualification
    study's in-file annotation scan.)*
13. A **primary statement** of the Japanese TTM fixing time and of the re-fixing trigger
    threshold.
14. Whether the **BOJ business-day calendar matches the Nissay NAV publication calendar date by
    date** — only a count-level coincidence was observed.
15. How to cover **2026-08-07 and 2026-08-10** for BOJ, and early-August 2026 for H.10, if the
    2026-08-10 cutoff is retained.
16. Whether **derived statistics** from any of these sources may be published in this public
    repository — UNCLEAR for every source except BOJ.

---

## 9. P1 impact

Statuses as approved. **No item was upgraded merely because this artifact was recorded.** The
open-items register in
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements)
remains the authoritative list of requirements.

| # | Requirement | Status | Basis |
| - | ----------- | ------ | ----- |
| **P1-7** | Currency treatment | **SUBSTANTIALLY ADVANCED** | The Nasdaq-side convention is pinned from primary Nasdaq documents: WM Company Closing Spot at 16:00:00 UK, EOD, applying to all Nasdaq Equity Indexes. Candidate public series with documented timestamps were identified and timed relative to it. The Nissay-side fixing time and provider remain undisclosed, so the pair is still only half-determined — the item does **not** advance to RESOLVED. |
| **P1-8** | Licensing / redistribution | **PARTIAL** | One source is clearly restricted (WMR). One is explicitly permissive with attribution (BOJ). The rest are UNCLEAR, and two could not be read at all. Nothing is cleared for redistribution or for committing raw values. |
| **P1-9** | Revision / restatement behaviour | **PARTIAL** | Three concrete restatement mechanisms were documented, none previously recorded: (a) BOJ 「訂正が入る可能性がある」; (b) WMR benchmark republication after a Price Challenge, with subscriber notification and 5-year records; (c) Japanese TTM 第2次公表相場, evidenced on 2024-08-07, with archives showing the final rate. Against these, FRB H.10 states "past releases are not revised." **No restatement testing was performed**, so the item stays PARTIAL. |
| **P1-3** | Proxy return composition | **PARTIAL** | Nasdaq's dividend formulas apply the **previous day's** WM 16:00 UK Closing Spot Rate to dividend market values — an FX-timing detail inside the total-return construction. Noted only; nothing approved. |
| **P1-2** | Approved Primary Proxy | **OPEN** | Untouched by this study by design. Nothing here bears on proxy selection, and the level-fit ranking in the approved alignment artifact remains inside its own measurement noise. |

---

## 10. Research transition

The broad source survey established that the **index-side leg was already in workable shape**:
Nasdaq's convention is pinned to WM 16:00 UK from primary documents, and FRB H.10 supplies a
Tier-1, explicitly non-revised public series observed on the same trading day.

It also established that the **Japan-side leg was the binding constraint**. BOJ is authoritative
and the most clearly licensed candidate, but **is not a TTM**; the only located TTM candidates
had unresolved terms, and one could not be read at all.

The study therefore recommended exactly one next step: **a further, narrowly scoped
source/licensing qualification of the Japan-side TTM leg**, with MUFG (via MURC) as the primary
target and Mizuho as the secondary target.

That study was subsequently performed and is recorded in
[`phase1_japan_side_ttm_qualification.md`](phase1_japan_side_ttm_qualification.md). Its
findings, and the resulting narrow Owner Decision recorded in
[`docs/decisions/phase1_ttm_qualification_decision.md`](../decisions/phase1_ttm_qualification_decision.md),
supersede this artifact's preliminary treatment of MUFG/MURC in §3.6 and §6.

---

## 11. Confirmations

- **No FX source was approved by this study.** All candidates are ranked assessments.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No Baseline FX convention was approved. The Frozen Baseline is unchanged.**
- **No FX residual decomposition was performed.** No synthetic USD × USD/JPY series was
  proposed or constructed.
- **No Nissay FX fixing time, provider, or conversion algorithm was inferred.**
- **No raw FX dataset is committed to this repository.** Individual rate values appearing in
  this artifact are targeted evidence citations, not a dataset.
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Evidence Artifact. Owner Review: APPROVED. No FX source approved.
Primary Proxy: NOT APPROVED — P1-2 remains OPEN.**
