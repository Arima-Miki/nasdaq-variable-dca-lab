# Phase 1 Evidence Artifact — Japan-side TTM Source Qualification

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Japan-side TTM Source Qualification** |
| Research date | **2026-08-11** (all source access dates 2026-08-11) |
| Owner Review | **APPROVED** |
| Qualification recommendation | **APPROVED BY OWNER, with limitations** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Nissay FX provider | **NOT IDENTIFIED** |
| Phase 2 | **BLOCKED** |

> **What the approval means.** The Owner has approved **the research evidence recorded in this
> artifact**, and has separately issued a **narrow qualification decision** on the MUFG/MURC
> TTM series, recorded in
> [`docs/decisions/phase1_ttm_qualification_decision.md`](../decisions/phase1_ttm_qualification_decision.md)
> and restated in §13 below.
>
> The Owner has **not** identified Nissay's FX provider, has **not** approved a Primary Proxy,
> has **not** approved a Baseline FX convention, and has **not** unblocked Phase 2.

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and does
not govern Baseline behavior. The preceding broad source survey is
[`phase1_fx_source_research.md`](phase1_fx_source_research.md). The observation-time alignment
evidence is [`phase1_empirical_alignment_study.md`](phase1_empirical_alignment_study.md).

**Provenance note.** This artifact was reconstructed from a Research Working Record rescued
from the research session of 2026-08-11. The working record was a manual copy of terminal
output; its table formatting was degraded in transit and has been repaired here. Semantic
content is preserved.

---

## 2. Research question

> **Can a reproducible Japanese-bank USD/JPY TTM series serve as a defensible candidate
> approximation of Nissay's Japan-side FX conversion concept for Phase-1 research?**

The Nissay 請求目論見書 valuation rule cited in the approved alignment artifact converts
foreign-currency assets at 「国内における計算日の対顧客電信売買相場の仲値」. The matching public
concept is a Japanese bank's **公表仲値 / TTM**.

### 2.1 Central distinction — binding throughout this artifact

A Japanese bank TTM series may be **structurally similar** to the conversion concept described
by Nissay. That does **NOT** establish that:

- Nissay uses that bank;
- Nissay uses that exact published TTM;
- Nissay uses the same fixing time;
- Nissay uses the same re-fixing rule;
- the candidate reproduces Nissay's actual FX conversion.

**The candidate is an approximation for research and sensitivity analysis only.** This
distinction is not weakened anywhere in this artifact.

---

## 3. Executive summary of findings

| Question | Finding |
| -------- | ------- |
| Does a reproducible Japanese-bank historical USD/JPY TTM series exist? | **Yes.** MUFG Bank's 対顧客外国為替相場 is archived by MURC as per-year Excel files containing an explicit daily USD/JPY TTM column, back to 1990, at stable URL patterns, plus per-date HTML pages. The 2023–2026 files were parsed directly and the schema, values, and annotations confirmed. |
| Is MUFG/MURC the strongest candidate? | **Yes**, by a wide margin over the alternatives examined. Mizuho remains inaccessible; SMBC offers only monthly PDFs and answered no question the primary target could not. |
| Is the rate definition sufficiently documented? | **Yes.** MURC states TTM = (TTS + TTB) / 2 in two independent places, and the identity was verified numerically against the archive data. |
| Is fixing timing sufficiently documented? | **No — partially.** MURC's *publication* timing is documented. The bank's *determination* moment is not documented by any primary or near-primary source reached. **PRIMARY TIMING EVIDENCE NOT FOUND.** |
| Are local research rights sufficiently clear? | **No.** MUFG's own site terms explicitly prohibit unauthorised use, reproduction, and modification. MURC's FX site publishes **no** terms-of-use or copyright page — only a data disclaimer. This is the weakest dimension of the candidate. |
| Is automated retrieval sufficiently clear? | **Partially.** MURC's `robots.txt` does not disallow the `/fx` paths. That is a genuine machine-readable signal, but **robots.txt is not a licence**, and MURC states no automated-access policy. |
| Is point-in-time historical reproducibility established? | **Established, and nuanced.** The archive's default is the **final** rate, stated in-record. The yearly Excel files **additionally preserve the initial rate** for suspension days as a labelled reference record. Point-in-time reconstruction is possible **for the annotated events only**, for the initial/final pair only, and **with no timestamps**. |

---

## 4. MUFG/MURC source chain

| Fact | Evidence | Source class | Confidence |
| ---- | -------- | ------------ | ---------- |
| MUFG Bank originates the rate; it is the 対顧客外国為替相場 | MURC daily page footer 「三菱UFJ銀行の最終公表相場による (Final official quotation by MUFG Bank, Ltd., Tokyo)」; page header 「三菱UFJ銀行公表の対顧客外国為替相場 / MUFG Bank, Ltd. Exchange Quotations」 | NEAR-PRIMARY | HIGH |
| MUFG publishes TTS/TTB on its own site, **current day only** | MUFG `spot_rate.csv` header 「外国為替相場一覧表（ＳＰＯＴ ＲＡＴＥ）」 with 「最終更新日時：2026/08/10 10:26」, columns T.T.S. / ACC. / CASH S. / T.T.B. / A/S / D/P・D/A / CASH B.; MURC FAQ A1 「※銀行のホームページ「外国為替相場」でご覧いただけます。ただし、当日限りの掲載となります。」 | PRIMARY (CSV) + NEAR-PRIMARY (FAQ) | HIGH |
| **MUFG's own site publishes no TTM column** | Direct parse of `spot_rate.csv`: USD row = TTS 158.98 / TTB 156.98; no TTM field present | PRIMARY | HIGH |
| **MUFG maintains no public historical archive; MURC is the archive path** | MURC FAQ A1 (当日限り) + MURC 【1990年以降の為替相場】; no MUFG historical page located | NEAR-PRIMARY | HIGH |
| MURC publishes the historical archive and exposes TTM | MURC FAQ menu: 「1990年以降の為替相場 … 公表相場が年ごとにご覧になれます。公表仲値（TTM）はここからご覧ください。」 | NEAR-PRIMARY | HIGH |
| MURC **transcribes** rather than originates | MURC disclaimer: 「銀行発表の最終公表相場から転記して掲載しており、可能な限り正確性を期しておりますが、データ引用元との整合性や信頼性を完全に保証するものではありません。あくまで参考値としてご参照ください。」 | NEAR-PRIMARY | HIGH |
| Source-bank chain is documented, with no break inside the study window | MURC: 1990/01–1996/03 旧東京銀行 → 1996/04–2005/12 旧東京三菱銀行 → 2006/01–2018/03 三菱東京UFJ銀行 → 2018/04 以降 三菱UFJ銀行 | NEAR-PRIMARY | HIGH |
| Cross-check: MURC values equal MUFG's published values | MUFG CSV 2026-08-10 USD 158.98 / 156.98 = MURC 本日の為替相場 2026-08-10 USD 158.98 / 156.98 | PRIMARY vs NEAR-PRIMARY | HIGH (single-date check) |

### 4.1 The chain

```
MUFG Bank  ──(publishes TTS/TTB, current day only, no TTM column)──►  bk.mufg.jp
     │
     └──(MURC transcribes 最終公表相場; computes/exposes TTM = (TTS + TTB) / 2)──►
              murc-kawasesouba.jp  ──►  daily HTML pages + per-year XLS archive
```

**MURC is NEAR-PRIMARY evidence for historical TTM, not direct MUFG primary evidence.**

### 4.2 Uncertainties in the chain

1. **A transcription layer sits between the bank and every historical value.** MURC disclaims
   full consistency with the source. One date was cross-checked and matched exactly; that is one
   date, not a validation.
2. **TTM is a derived quantity in this chain.** MUFG's own published artefact carries TTS and
   TTB; the TTM in the archive is the documented midpoint. Arithmetically trivial, but worth
   stating: **the archive's TTM is not independently published by the bank on the pages read.**
3. **MURC's own business calendar can delay publication:**
   「銀行の営業日であっても、当社が休業日にあたる場合は掲載しません…当社の翌営業日以降に掲載します。」
   This affects availability timing, not the value.
4. MURC states it may change or discontinue sources without notice **for some of its other
   datasets** (現地参考為替相場 / 世界の為替相場). That caveat was **not** found attached to
   【1990年以降の為替相場】.

---

## 5. Rate-definition findings

| Concept | Definition | Source | Evidence class | Status |
| ------- | ---------- | ------ | -------------- | ------ |
| **公表仲値 (TTM)** | 「公表仲値（TTM）は、TTSとTTBの中間の相場であり、**（TTS＋TTB）/2**で算出されます」 | MURC 本日の為替相場 page; MURC FAQ Q4 note (p.3) | NEAR-PRIMARY | **DOCUMENTED** — verified numerically (e.g. 2024-08-06: 145.98, 143.98 → 144.98) |
| **TTS** | Telegraphic Transfer Selling — column `T.T.S.` in MUFG's own rate table | MUFG `spot_rate.csv`; MUFG 外国為替相場一覧表 | PRIMARY (column exists) | **NAMED**, not defined by MUFG on the pages read |
| **TTB** | Telegraphic Transfer Buying — column `T.T.B.`; for some currencies flagged 「TTBは参考相場 (TTB is for reference only)」 | MUFG `spot_rate.csv`; MURC daily page footnote \*2 | PRIMARY / NEAR-PRIMARY | **NAMED**; the 参考相場 flag does **not** apply to USD |
| **対顧客外国為替相場** | 「三菱UFJ銀行公表の対顧客外国為替相場 / MUFG Bank, Ltd. Exchange Quotations」 — the bank's customer-facing quotation set | MURC page heading; FAQ Q1 | NEAR-PRIMARY | **NAMED**, matching the Nissay prospectus concept 「対顧客電信売買相場」 |
| **最終公表相場** | 「三菱UFJ銀行の最終公表相場による (Final official quotation by MUFG Bank, Ltd., Tokyo)」 — the archive stores the day's **final** quotation | MURC daily archive page footer (every dated page) | NEAR-PRIMARY | **DOCUMENTED IN-RECORD** |
| **公示相場 / 1次公示相場** | Terminology used inside the Excel archive for the published rate and the **first** published rate | MURC yearly XLS shared-string table | NEAR-PRIMARY | **DOCUMENTED** — note the website uses 公表相場, the workbook uses 公示相場 |
| **Quote direction** | **JPY per 1 USD** (USD row values ≈ 145–159) | MUFG CSV + MURC archive | PRIMARY | **ESTABLISHED** |

> **Direct documentation of TTM = (TTS + TTB) / 2 by the publisher:** **Yes, by MURC** (twice),
> and verified arithmetically across the archive. **Not by MUFG Bank** on any page reached —
> MUFG publishes the components, not the identity.
>
> **The TTM identity is therefore NEAR-PRIMARY, not PRIMARY.**

---

## 6. Historical-data assessment

| Property | Finding | Evidence | Status |
| -------- | ------- | -------- | ------ |
| Start date | **1990** (per-year files from `murc_1990.xls`) | MURC year selector; FAQ A7 confirms nothing before 1989 | ESTABLISHED |
| Latest date — **yearly XLS** | **2026-07-31** | Direct parse of `murc_2026.xls` | ESTABLISHED |
| Latest date — **dated HTML pages** | **2026-08-07** available; **2026-08-10 not yet in the archive** | Direct fetch: dated page for 2026-08-07 works; 2026-08-10 falls back (see §7) | ESTABLISHED |
| Update cadence explains the lag | 「このデータは**月1回**、銀行の**月末営業日の15時以降**、当日中に当該月のデータを更新します」 | MURC FAQ A6 (p.4) | ESTABLISHED |
| Daily USD/JPY TTM available | **Yes** — explicit TTM column in the yearly XLS | Direct BIFF parse | ESTABLISHED |
| Format | **Legacy `.xls` (BIFF8 / CFB)**, `application/vnd.ms-excel`, ~290–392 KB per year; dated pages are **Shift_JIS HTML** | `file` output; HTTP `Content-Type`; page `charset=Shift_JIS` | ESTABLISHED |
| File interval | **One file per calendar year**; one row per calendar day (non-business days blank) | Direct parse | ESTABLISHED |
| Do dated pages show TTM? | **No** — dated HTML pages show **TTS and TTB only**; TTM must be derived or taken from the XLS | Direct parse of three dated pages | ESTABLISHED |
| URL stability | Stable, predictable patterns: per-year `murc_YYYY.xls` under `/fx/xls/`; per-date pages under `/fx/past/` keyed by `YYMMDD` | Direct retrieval, 4 years + 4 dates | ESTABLISHED (observed, not guaranteed) |
| Study-window coverage | **816 distinct in-window dates with USD TTM** through 2026-07-31 (2023: 187, 2024: 246, 2025: 243, 2026: 141) | Direct parse across 4 files | ESTABLISHED |
| Full window 2023-03-31 → 2026-08-10 | **Not from the XLS alone.** Requires XLS (→ 2026-07-31) **plus** dated pages for 2026-08-03 … 08-07, **plus** an unresolved route for 2026-08-10 | Direct verification | **GAP — resolvable, but must be declared** |
| Archive state semantics | **Final published rate**, stated in-record; initial rate additionally retained as an annotated reference record on suspension days | MURC footer + XLS annotations | **ESTABLISHED — DOCUMENTED** |

**Count observation, offered as suggestive only.** 816 in-window observations plus 6 Japanese
business days in 2026-08-03 … 08-10 = **822**, which equals the 822 fund NAV observations
recorded in the approved alignment artifact for the same window. This is a **count-level
coincidence**; the fund NAV date list was not available and **no date-by-date match was
performed**. It must not be cited as established calendar equivalence.

**No raw historical dataset from this source is committed to this repository.** The values
quoted in this artifact are targeted evidence citations.

---

## 7. Critical retrieval hazard — data-integrity requirement discovered in Phase 1

> **Requesting a date not present in the dated archive may return HTTP 200 with the site
> index / current-rate page rather than a 404.**
>
> Two dates were tested that are not (yet) in the dated archive. Both returned **HTTP 200**
> carrying the **site index page**, which displays the **current** rate. Neither returned 404,
> and neither signalled absence in any way. A naive retriever keying on the USD row would
> **silently record today's rate under the requested historical date**.
>
> **A future retriever MUST validate that the returned page actually identifies the requested
> historical date** before accepting any value from it.

Discriminators observed during the study — recorded as evidence of *how* the failure presents,
**not** as a prescribed production implementation:

- Response size differed markedly between a dated page (~14.5 KB) and the index page (~18.2 KB).
- A genuine dated page carries a 「YYYY年M月D日の為替相場」 title; the index fallback does not.

**No production implementation is prescribed here.** The requirement is recorded as a
data-integrity constraint that any future Phase-1 retrieval design must satisfy.

This is the **same class of failure** as the `Value` / null-`Close` finding already recorded in
[`phase1_empirical_alignment_study.md`](phase1_empirical_alignment_study.md) §3: a source that
returns a plausible wrong value instead of an error.

---

## 8. Fixing-time assessment

The three tiers are kept strictly separate and are **not** merged.

### 8.1 ESTABLISHED (PRIMARY / NEAR-PRIMARY)

| Fact | Wording | Source | Class |
| ---- | ------- | ------ | ----- |
| MURC posts the day's rate after 11:00 JST on bank business days | 「（当ホームページでは）銀行営業日の**午前11時過ぎ**に掲載します。」 | MURC FAQ A1 (p.2) | NEAR-PRIMARY |
| The MURC table is changed after 11:00 | 「相場は**11時過ぎ**に変更します （Table will be updated around 11：00）」 | MURC daily page footer | NEAR-PRIMARY |
| MUFG's own page carries the rate for that day only | 「ただし、**当日限り**の掲載となります。」 | MURC FAQ A1 | NEAR-PRIMARY |
| MUFG's rate table bore a 10:26 JST update stamp on one observed date | 「最終更新日時：**2026/08/10 10:26**」 | MUFG `spot_rate.csv` | **PRIMARY** — but a *single* observation, and an **update stamp, not a determination time** |
| Publication time differs from determination time | 「銀行が**再発表した時刻**と、当社が変更後の相場を掲載する**時間帯にタイムラグ**があります。」 | MURC FAQ A2 (p.3) | NEAR-PRIMARY |

### 8.2 CONVENTIONAL / SECONDARY — preserved separately, **not** promoted

| Claim | Wording | Source | Class |
| ----- | ------- | ------ | ----- |
| The published rate is computed from the interbank rate just before 10:00 each morning and announced to customers | 「公表相場は毎朝**午前10時前**の銀行間相場をベースに算出され、顧客に発表されます。」 | 公益財団法人 国際通貨研究所 (IIMA) | SECONDARY-institutional |
| It normally applies unchanged all day | 「公表相場はそのまま変わることなく、原則として当日の取引に終日使用されます。」 | IIMA | SECONDARY-institutional |
| TTM references the ~09:55 JST interbank rate, published ~10:00 | Various | 野村證券, SMBC日興証券, iFinance, OANDA glossaries | SECONDARY |

### 8.3 UNKNOWN

- **The exact moment MUFG determines the initial TTM.** No MUFG-issued statement located.
- Whether MUFG's determination differs from the general market convention.
- Whether the 10:26 JST stamp observed once is typical, early, or late.
- The timezone handling of that stamp (assumed JST; not stated on the file).

> ### PRIMARY TIMING EVIDENCE NOT FOUND
>
> **No MUFG Bank primary source establishes the TTM determination time.**
>
> The commonly cited **approximately 09:55 JST** convention rests on institutional and glossary
> sources only. It **must not** be described as an established MUFG determination time. It may
> be carried **only** as conventional, secondary-source-based, or as an explicit assumption for
> sensitivity analysis.

### 8.4 Timezone discipline

JST observes **no** daylight saving. The United Kingdom and the United States both do, on
transition dates that are **not always identical**. Any statement relating a JST fixing moment
to a London or New York observation therefore has a **date-dependent offset** and must be
computed with **calendar-aware timezone conversion per observation date**. **No fixed-hour
relationship is asserted in this artifact.**

---

## 9. Re-fixing semantics (第2次公表相場 / 公示相場停止)

### 9.1 Supported by evidence

| Element | Evidence | Source | Class / confidence |
| ------- | -------- | ------ | ------------------ |
| The bank may **suspend** a published rate and **re-announce** it | 「外国為替市場に**大きな変動**が生じた場合は、銀行は、発表した公表相場を**一旦停止**し、**あらためて公表相場を発表**する場合があります。」 | MURC FAQ A2 | NEAR-PRIMARY, HIGH |
| MURC then changes the displayed rate and ultimately shows the day's **final** rate | 「この場合、掲載していた相場を**変更**し、**最終的には当該日の最終の相場を掲載**します。」 | MURC FAQ A2 | NEAR-PRIMARY, HIGH |
| There is a **lag** between the bank's re-announcement and MURC's update | 「銀行が再発表した時刻と、当社が変更後の相場を掲載する時間帯にタイムラグがあります。」 | MURC FAQ A2 | NEAR-PRIMARY, HIGH |
| Terminology in use | Website: **公表相場停止**, **第2次公表相場**. Workbook: **公示相場停止**, **1次公示相場**. | MURC site notices; XLS strings | NEAR-PRIMARY, HIGH |
| Suspension days are **flagged in the data file** | 「【8月7日公示相場停止あり】」 (2024 file); 「【1月18日公示相場停止あり】」 (2023 file) | MURC XLS string table | NEAR-PRIMARY, HIGH |
| The **initial** rate is retained as a labelled reference record | 「(下記、数値は**参考記録**として**1次公示相場発表分**を掲載します)」 | MURC XLS string table (2023 and 2024 files) | NEAR-PRIMARY, HIGH |
| The re-fixing affects the **whole published quotation set**, not TTM alone | Both 2024-08-07 rows carry full currency sets (USD, EUR, CAD, …) with different values | Direct parse | NEAR-PRIMARY, HIGH |
| Frequency is **low** | Annotation scan of the four study-window year files: 2023 → 1 (Jan 18, **outside the study window**), 2024 → 1 (Aug 7), 2025 → **0**, 2026 (to Jul 31) → **0** | Direct scan | NEAR-PRIMARY, HIGH |

### 9.2 Explicitly identified as unsupported folklore

> **The commonly cited "about ¥1 movement" trigger threshold is NOT documented by any primary
> or near-primary source located in this study.**
>
> MURC states only 「大きな変動」 (large movement). IIMA states only 「大きな相場変動」. Neither
> gives a number. The ¥1 figure appears **only** in secondary glossaries.
>
> **It must not be used as a modelling assumption.**

### 9.3 Also unresolved

- Whether **more than two** publications can occur on one day. The terminology 「1次公示」 /
  「第2次」 implies a sequence but sets no bound; both observed events show exactly two.
- Whether the bank publishes its own suspension notice (none located on MUFG's site).
- How users are informed in real time — the only mechanisms observed are a MURC site notice and
  the in-file annotation, **both after the fact**.
- Whether the trigger is evaluated on the interbank rate, on TTM, or per currency.

---

## 10. 2024-08-07 case study

> **Motivation only, no causal claim.** 2024-08-07 falls immediately after 2024-08-06, one of
> the four Large-Drop zone entry dates recorded in
> [`phase1_empirical_alignment_study.md`](phase1_empirical_alignment_study.md) §11.
> **No relationship between the two is claimed, tested, or implied.** No return, performance, or
> portfolio analysis was performed.

### 10.1 Evidence

| Item | Finding | Source | Class |
| ---- | ------- | ------ | ----- |
| Site notice (index) | 【お知らせ】 stating that on 8月7日(水) 「相場の変動により公表相場が停止され、第2次公表相場が発表されました」 | MURC 外国為替相場情報 index | NEAR-PRIMARY |
| Site notice (archive) | 「『1990年以降の為替相場』掲載の 2024年8月7日付の為替相場は、**第2次公表相場**を掲載しております。」 | MURC 1990年以降の為替相場 | NEAR-PRIMARY |
| In-file annotation | 「【8月7日公示相場停止あり】」 | `murc_2024.xls` string table | NEAR-PRIMARY |
| In-file reference-record label | 「(下記、数値は参考記録として1次公示相場発表分を掲載します)」 | `murc_2024.xls` string table | NEAR-PRIMARY |
| Dated HTML page | 2024年8月7日: USD TTS 148.04 / TTB 146.04 (implied TTM 147.04) | MURC dated page for 2024-08-07 | NEAR-PRIMARY |
| XLS main sequence | 2024-08-07: TTS 148.04 / TTB 146.04 / **TTM 147.04** | Direct parse | NEAR-PRIMARY |
| XLS separate annotated block | 2024-08-07: TTS 145.80 / TTB 143.80 / **TTM 144.80** | Direct parse | NEAR-PRIMARY |
| Adjacent days (no duplicates) | 2024-08-06: 145.98 / 143.98 / 144.98 · 2024-08-08: 147.20 / 145.20 / 146.20 | Direct parse | NEAR-PRIMARY |

### 10.2 Event semantics

MUFG suspended its initially published quotation for 2024-08-07 and issued a replacement. **The
archive holds both:**

| Publication | TTS | TTB | **TTM** | Location in archive |
| ----------- | --- | --- | ------- | ------------------- |
| **Initial / first (1次公示)** | ≈ 145.80 | ≈ 143.80 | **≈ 144.80** | Separate annotated reference block |
| **Final / second (第2次公表相場)** | ≈ 148.04 | ≈ 146.04 | **≈ 147.04** | Main date sequence; also the value served by the dated HTML page |

**Difference on TTM: ≈ ¥2.24, ≈ 1.55 %.** That is not a rounding artefact; it is the size of a
real intraday move captured on opposite sides of the re-fixing.

**Assignment basis, stated so it can be checked.** The main-sequence value matches the dated
page; MURC states the archive shows the 最終公表相場; and MURC's site notice states the
displayed 2024-08-07 rate **is** the 第2次公表相場. The reference-record label identifies the
separate block as 1次公示. **No in-file cell label attaching "1次" to that specific row was
found** — the association rests on the block-level annotation plus the three converging
statements above. Confidence **HIGH**, but this is inference from labelled structure, not a
per-row tag.

### 10.3 Archive behaviour

- The **dated HTML page carries no marker** that the day was a suspension day. It is
  structurally identical to 2024-08-06 and 2024-08-08. The only in-record signal is the generic
  footer 「最終公表相場による」.
- The **XLS does carry a marker** — both a date-specific annotation and the reference block.
- **Consequence: the HTML route loses the event; the XLS route preserves it.** A study using
  only the dated pages would silently take the second rate with no indication that a first rate
  existed.

### 10.4 Point-in-time implications

This case demonstrates a **point-in-time reproducibility issue** and, simultaneously, the
archive's **partial remedy**:

- "What does the archive show today for 2024-08-07?" → **≈ 147.04**
- "What rate was available earlier that Japanese morning?" → **≈ 144.80**, per the reference
  record

The distinction is recoverable **only because MURC chose to retain the first rate** — a
courtesy, not a guarantee, and one whose scope beyond flagged days is unestablished.

### 10.5 Unresolved details

- **No timestamps.** Neither the time of the initial publication nor of the re-publication was
  found recorded anywhere.
- No record of when MURC updated its display (the FAQ states there is a lag but does not
  quantify it).
- Whether the 1次公示 block is retained indefinitely or eventually dropped.
- Whether 2023-01-18 — the other flagged event, **outside the study window**, which begins
  2023-03-31 — has the same dual-row structure. The annotation strings are present in
  `murc_2023.xls`, but that date's rows were not extracted.
- Whether any suspension occurred on a date **not** annotated.

---

## 11. Point-in-time reproducibility assessment

The three purposes are assessed **separately** and are **not** equivalent.

### Retrospective final-rate research — **SUITABLE**

For studies asking "what was the day's final customer conversion rate," the archive is directly
fit for purpose: documented definition, verified arithmetic, machine-readable, stable URL
patterns, per-day granularity, explicit 最終公表相場 semantics. The single in-window suspension
is flagged.

### Point-in-time historical research — **CONDITIONALLY SUITABLE**

Suitable **only if** the study explicitly handles the suspension mechanism. Within the study
window this is tractable: **one date (2024-08-07)**, flagged in-file, with both rates
recoverable. The caveats are:

- The default archive state is the **final** rate, not the point-in-time rate.
- **No timestamps exist**, so a rule depending on *when during the day* a rate became available
  cannot be evaluated.
- Detection of suspensions depends on MURC's annotations; **annotation exhaustiveness is
  unverified**.
- The dated-HTML route loses the distinction entirely.

### Full reproducibility — **PARTIAL**

| Question | Finding |
| -------- | ------- |
| Corrections / re-fixings | Documented mechanism; two events flagged across the 2023–2026 files |
| Are files replaced? | **Yes** — yearly files are rewritten monthly (FAQ A6); `murc_2024.xls` carried a Last-Saved stamp of 2024-12-30 |
| Revision notices | Site notices exist for suspension days; **no general change log** |
| Archive versioning | **None found** |
| Prior versions available | **No** |
| Immutability | **Not established** — the monthly rewrite is explicit |
| Checksums / dated snapshots | **None provided** |
| Publisher's own advice | 「必要な場合は、定期的にお客さまで保存することをお薦めします」 — MURC recommends users save data themselves (stated for its other datasets) |

**Direct P1-9 consequence.** Because the publisher provides no versioning, immutability
guarantee, or checksums, **any study relying on this source must fix its own dated snapshot and
record it**, exactly as the approved alignment study imposed and recorded its own cutoff. The
publisher will not do this for the researcher.

---

## 12. Licensing

Assessed **separately** for MUFG and MURC. **Their terms do not explicitly apply jointly**, and
no statement linking them was found.

### 12.1 MUFG Bank (bk.mufg.jp)

Governing text, 本サイトのご利用にあたって:

> 「本サイトに掲載されたすべての内容(情報、商標、デザインなど)の著作権は、当行または本サイトの
> 運営に関わる協力会社に帰属するものです。**したがって、無断で使用、複製、改変することを禁じます。**」

*Copyright in all site content belongs to the bank or its cooperating companies; unauthorised
use, reproduction, and modification are prohibited.* **No 私的利用 or 引用 exception is
stated. No automated-access statement appears.** Page disclaimer:
「掲載されているレートは最終更新日時時点でのものであり、あくまで目安としてご利用ください。」

| Use | Classification |
| --- | -------------- |
| Human viewing | **PERMITTED** |
| Manual download | **UNCLEAR** — the CSV is offered for download, but 無断使用 is prohibited and no exception is stated |
| Local research analysis | **UNCLEAR** — 「無断で使用…を禁じます」 is broad; no legal conclusion is drawn |
| Automated retrieval | **UNCLEAR** — no policy either way |
| Repeated automated retrieval | **UNCLEAR** |
| Raw-data redistribution | **RESTRICTED** — 無断複製 explicitly prohibited |
| Public Git repository raw data | **RESTRICTED** |
| Publication of derived statistics | **UNCLEAR** |

### 12.2 MURC (murc-kawasesouba.jp)

**No terms-of-use page, copyright policy, or site policy exists on this site.** Every link on
the index page was enumerated (no terms link present) and candidate URLs were probed
(`/fx/menseki.php`, `/fx/riyou.php` → 404; `murc.jp/policy/`, `murc.jp/sitepolicy/` → 404;
`/fx/faq/` → 403 directory listing). The only governing texts are the on-page disclaimer and
the FAQ.

Disclaimer:
「銀行発表の最終公表相場から転記して掲載しており…データ引用元との整合性や信頼性を完全に保証する
ものではありません。あくまで参考値としてご参照ください。また情報の利用により生じたいかなる損害に
ついても、一切の責任を負いかねますので、ご了承ください。」

`robots.txt`: `User-agent: *` with `Disallow: /inc, /include, /web_manager, /ec, /ec_elp,
/elp-mufg, /murc, /GLOBAL_Angle, /elp_mufg` — **`/fx`, `/fx/past`, and `/fx/xls` are not
disallowed.**

| Use | Classification |
| --- | -------------- |
| Human viewing | **PERMITTED** |
| Manual download | **PERMITTED** — files are published for download and the FAQ documents the download workflow (A6) |
| Local research analysis | **UNCLEAR** — no grant and no prohibition located; only a "reference value" disclaimer |
| Automated retrieval | **UNCLEAR, with a positive `robots.txt` signal** — the relevant paths are not disallowed, but **robots.txt is not a licence** |
| Repeated automated retrieval | **UNCLEAR** — no rate-limit or frequency policy stated |
| Raw-data redistribution | **UNCLEAR** — no permission located; **absence of a prohibition is not permission** |
| Public Git repository raw data | **UNCLEAR — treat as RESTRICTED in practice**, since the underlying MUFG content is explicitly protected |
| Publication of derived statistics | **UNCLEAR** |

### 12.3 Mizuho Bank — ACCESS UNRESOLVED

> ### ACCESS UNRESOLVED

All attempts were normal public web access with a standard browser user-agent. **No anti-bot
control was bypassed and no alternative access route was pursued.**

| URL | Result |
| --- | ------ |
| `/market/historical/index.html` | HTTP 403 |
| `/market/historical/backnumber_a/index.html` | HTTP 403 |
| `/market/quote.html` | HTTP 403 |
| `/market/csv/quote.csv` | HTTP 403 |
| `/robots.txt` | **HTTP 403** — Akamai "Access Denied", reference `18.f530d417.1786415682.26f47784` |

**Consequence for qualification:** because `robots.txt` itself is inaccessible, the
automated-access policy **cannot even be read**, let alone complied with. Mizuho therefore
cannot be qualified — **not because its data is unsuitable, but because its terms are
unreadable.** Secondary reports of CSV coverage from 2002-04-01 remain **unverified and are not
relied upon**. All licensing categories: **UNCLEAR (unread)**.

This did not block completion of the MUFG assessment.

### 12.4 Data-handling conclusion

**No legal conclusion is drawn.** It is neither asserted nor denied that local analysis is
lawful under either site's terms; this artifact records what the located texts do and do not
say. **Raw MUFG/MURC values must not be committed to this public repository.**

---

## 13. Qualification result — Owner-approved, narrow

The Owner has issued the following decision. It is recorded in full in
[`docs/decisions/phase1_ttm_qualification_decision.md`](../decisions/phase1_ttm_qualification_decision.md);
the substance is restated here so this artifact remains self-contained.

### 13.1 Decision

**Status: APPROVED.**

MUFG/MURC historical USD/JPY TTM is **qualified for use as a candidate Japan-side FX
approximation** in:

- local Phase-1 research;
- FX residual decomposition research;
- sensitivity analysis.

The qualification exists because the source is **structurally similar** to the conversion
concept described in the Nissay prospectus: 「国内における計算日の対顧客電信売買相場の仲値」.

### 13.2 The qualification is deliberately narrow — explicit non-claims

It does **NOT** establish that:

- Nissay uses MUFG;
- Nissay uses MURC;
- MUFG/MURC is Nissay's actual FX provider;
- the MUFG/MURC TTM reproduces Nissay's actual FX conversion;
- Nissay uses the same fixing time;
- approximately 09:55 JST is an established MUFG fixing time;
- the commonly cited approximately ¥1 re-fixing threshold is valid;
- the archived final TTM was necessarily the point-in-time value available at every historical
  decision moment;
- raw MUFG/MURC data may be redistributed;
- raw MUFG/MURC data may be committed to this public repository;
- a Baseline FX convention has been approved;
- a Primary Proxy has been approved.

**P1-2 remains OPEN. Phase 2 remains BLOCKED.**

### 13.3 Required 2024-08-07 sensitivity condition

Any future Phase-1 study using MUFG/MURC TTM **must explicitly handle 2024-08-07**.

| Publication | TTM |
| ----------- | --- |
| Initial / first publication | ≈ **144.80** JPY/USD |
| Final / second publication | ≈ **147.04** JPY/USD |
| Difference | ≈ **¥2.24** — approximately **1.55 %** |

**The future study must not silently choose one.** The choice must be **stated, justified, and
where relevant tested under both readings.**

### 13.4 Timing boundary

Approximately 09:55 JST may be described **only** as conventional, secondary-source based, or as
an assumption for sensitivity analysis. **It must NOT be described as an established MUFG
determination time.**

### 13.5 Re-fixing boundary

**Do NOT model a quantitative approximately ¥1 re-fixing threshold.** No primary or near-primary
evidence established such a threshold.

### 13.6 Licensing / data-handling boundary

**MUFG/MURC raw values must remain outside the public repository.** The qualification authorizes
a **research input, not redistribution**. Derived statistics may be proposed for repository
evidence, but their publication remains subject to the evidence and licensing boundaries already
recorded.

---

## 14. Candidate comparison

| Candidate | Structural relevance | Timing evidence | History | Terms clarity | Revision clarity | Overall research suitability |
| --------- | -------------------- | --------------- | ------- | ------------- | ---------------- | ---------------------------- |
| **MUFG/MURC TTM** | **Highest** — 対顧客 TTM, the same concept class as 「対顧客電信売買相場の仲値」 | **Partial** — publication documented; **determination time UNKNOWN** | **Strongest** — daily 1990→; 816 in-window observations to 2026-07-31 plus dated pages | **Weakest** — MUFG restrictive, MURC silent | **Best of the three** — mechanism documented, events flagged in-file, initial rate retained | **Qualified candidate, with limitations** |
| **Mizuho TTM** | High (same concept class) | Unknown | Unverified (reported 2002→) | **Unreadable** | Unknown | **Not assessable — ACCESS UNRESOLVED** |
| **BOJ 17:00 spot** (non-TTM fallback / reference) | **Lower** — Tokyo interbank spot mid, **not** a 対顧客 TTM; different concept and different time of day | **Strongest** — 17:00 JST, defined as the offer/bid midpoint | Strong — `FM08'FXERD04`, 1998→, 820 in-window observations to 2026-08-06 | **Clearest** — reproduction permitted with attribution (stated exceptions) | Weaker for this purpose — 「訂正が入る可能性がある」 with no event flags | **Useful cross-check / robustness reference, not a TTM substitute** |

**Reading of this table.** The two viable candidates are **complementary rather than
competing**: MUFG/MURC is strongest on structural relevance and revision transparency; BOJ is
strongest on licensing clarity and timing documentation. How a future study combines them is
**study design, out of scope for this artifact.**

---

## 15. P1 impact

Statuses as approved. **No item was upgraded merely because this artifact was recorded.**

| # | Requirement | Status | Basis |
| - | ----------- | ------ | ----- |
| **P1-7** | Currency treatment | **SUBSTANTIALLY ADVANCED** (unchanged tier, materially strengthened) | The Japan-side leg now has an identified, machine-readable, definitionally documented candidate matching the Nissay concept class, with quantified window coverage. It does **not** reach RESOLVED: Nissay's provider and fixing time remain undisclosed, MUFG's determination time is undocumented, and the candidate remains an approximation of a concept. |
| **P1-8** | Licensing / redistribution | **PARTIAL** (unchanged) | Sharpened in both directions: MUFG's terms were read and are **explicitly restrictive** on reproduction; MURC has **no terms page at all**; MURC's `robots.txt` gives a positive but non-dispositive automated-access signal; Mizuho's terms are unreadable. **Nothing is cleared for redistribution or for committing raw values.** |
| **P1-9** | Revision / restatement behaviour | **PARTIAL** (substantially strengthened within PARTIAL) | First concrete, quantified restatement evidence in the project: a documented suspend-and-re-announce mechanism; **exactly one in-window event (2024-08-07)** with both rates recoverable and a ≈ ¥2.24 TTM spread; zero flagged events in 2025 and 2026-to-July; no publisher versioning, immutability, or checksums; and a newly identified silent-fallback retrieval hazard. Stays PARTIAL because **no timestamps exist**, annotation exhaustiveness is unverified, and no restatement testing was performed on the fund NAV or the Nasdaq series. |
| **P1-2** | Approved Primary Proxy | **OPEN — unchanged** | Nothing in this study bears on Primary Proxy selection. |

---

## 16. Limitations

1. **MURC is a transcription layer.** Only one date was cross-checked against MUFG's own
   publication.
2. **The TTM identity is NEAR-PRIMARY**, documented by MURC and not by MUFG on the pages read.
3. **The determination time is unknown**; only the publication side is documented.
4. **No timestamps** attach to either publication on a suspension day.
5. **Annotation exhaustiveness is unverified** — suspensions are detected only via MURC's flags.
6. **The yearly XLS does not reach the 2026-08-10 study cutoff**; the tail requires dated pages,
   and 2026-08-10 was not yet available by that route at access time.
7. **Terms are the weakest dimension**: MUFG restrictive, MURC silent, Mizuho unreadable.
8. **Mizuho and SMBC were not qualified**, for access and format reasons respectively.
9. **No Japanese bank has been identified as Nissay's FX provider**, and none is implied.

---

## 17. Confirmations

- **No Japanese bank was identified as Nissay's FX provider.**
- **The qualification is an approximation of a concept, not a reconstruction of Nissay's
  conversion.**
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No Baseline FX convention was approved. The Frozen Baseline is unchanged.**
- **No FX residual decomposition was performed.** No returns were compared and no performance
  analysis was carried out.
- **No synthetic index was constructed.**
- **No raw TTM dataset is committed to this repository.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Evidence Artifact. Owner Review: APPROVED.
Qualification: APPROVED BY OWNER, narrow and bounded — see
[`docs/decisions/phase1_ttm_qualification_decision.md`](../decisions/phase1_ttm_qualification_decision.md).
Primary Proxy: NOT APPROVED — P1-2 remains OPEN.**
