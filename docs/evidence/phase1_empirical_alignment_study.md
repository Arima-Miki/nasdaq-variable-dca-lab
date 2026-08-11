# Phase 1 Evidence Artifact — Empirical Alignment Study

**Nissay NASDAQ100 Index Fund NAV vs Nasdaq JPY candidate index series**

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Empirical Alignment Study** |
| Study date | **2026-08-11** |
| Fixed Empirical Alignment Study Cutoff | **2026-08-10** |
| Owner Review | **APPROVED** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |

> **What the approval means.** The Owner has approved **the research evidence recorded
> in this artifact** — the study's method, its derived statistics, and its stated
> limits.
>
> The Owner has **not** approved a Primary Proxy, has **not** identified the Nissay
> benchmark, and has **not** unblocked Phase 2. **P1-2 remains OPEN.** Nothing in this
> artifact may be cited as approval of a data source for the Baseline backtest.

This artifact is written to be self-contained. A future researcher with no access to
the session in which the study was run should be able to understand what was tested,
how, what was found, and what was deliberately left unresolved, from this file alone.

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it and
does not govern Baseline behavior. The decision history is
[`docs/decisions/phase0_baseline_decisions.md`](../decisions/phase0_baseline_decisions.md).
This artifact records Phase-1 **evidence** only.

---

## 2. Research question

> **How does the actual Nissay NASDAQ100 Index Fund NAV align in observation time with
> the Nasdaq JPY candidate series, and how large are the residual differences once
> timing is aligned?**

Candidate series tested:

| Symbol | Nasdaq return version |
| ------ | --------------------- |
| `NDXJPY` | Price Return, JPY |
| `XNDXJPY` | Gross Total Return, JPY |
| `XNDXNNRJPY` | Notional Net Total Return, JPY |

**The study was explicitly NOT intended to approve a Primary Proxy.** Its purpose was to
establish, from data rather than assumption, whether an apparent one-business-day
observation offset between the fund NAV and the Nasdaq JPY series is real, and to
measure what is left over once that offset is removed.

### Why this was tested

Earlier Phase-1 primary-source research (Owner-approved) established that:

1. The fund's stated benchmark is 「NASDAQ100指数（配当込み、円換算ベース）」.
2. Nissay states in its statutory 交付目論見書 that the yen conversion is performed
   **independently by the management company** (「委託会社が独自に円換算したもの」).
3. The Nissay benchmark is therefore **not established to be identical** to any
   Nasdaq-published JPY index.
4. Nissay does **not** disclose whether 「配当込み」 means Gross, Net or Notional Net
   total return, nor its benchmark FX provider, fixing time, rate type, holiday
   convention, rounding, or fallback rules.
5. The fund's NAV valuation rule (請求目論見書, 【資産の評価】) values foreign equities at
   「金融商品取引所における計算日に知りうる直近の日の最終相場」 — the most recent
   closing price knowable on the calculation date — and converts foreign-currency
   assets at 「国内における計算日の対顧客電信売買相場の仲値」 (a Japan TTM rate on the
   calculation date).

Point 5 makes a one-observation offset *plausible*. The purpose of this study was to
test it rather than assume it, because the Frozen Baseline's Strategy B and C triggers
fire on daily drawdown zones and are therefore sensitive to observation timing.

---

## 3. Data sources and study window

### Fund NAV — Nissay Asset Management

| Item | Value |
| ---- | ----- |
| Source | Official Nissay since-inception daily NAV series (issuer-published) |
| Fields used | `基準価額`, `税引前分配金再投資基準価額` |
| Study start | **2023-03-31** (fund inception; no earlier fund data can exist) |
| Study cutoff | **2026-08-10** |
| Observations in window | **822** |
| Duplicate dates | 0 |

### Candidate indexes — Nasdaq Global Index Watch (GIW)

| Item | Value |
| ---- | ----- |
| Source | Official Nasdaq GIW **live** end-of-day history |
| Series | `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY` |
| Observations in window (each) | **842** |

**Only live Nasdaq history was used.** No pre-launch back-tested Nasdaq values entered
this study; none were required, since all three series have been live since 2020-06,
well before fund inception. **No secondary source** (Yahoo Finance, data portals, or
similar) was used at any point.

### Data-integrity observation (important for any future retrieval)

> The Nasdaq GIW end-of-day response carried the index level in the **`Value`** field.
> The **`Close`** field was **null** in the retrieved response.
>
> `Value` was used throughout this study. A future consumer that keyed on `Close` would
> silently receive nulls rather than an error.

### Study cutoff discipline

The Empirical Alignment Study Cutoff of **2026-08-10** was chosen as the latest date
common to all four series at retrieval time, was **fixed before any statistic was
computed**, and was applied uniformly. It is **not** a moving "latest" endpoint.

**It is not the Baseline Dataset Cutoff.** P1-6 remains a separate, open Owner decision.

### Raw-data boundary

Raw datasets were held in a working location **structurally outside the repository
tree** and were never added to version control. This artifact records **derived
statistics, methodology, aggregate counts, and dates of regime changes only**. No raw
dataset rows, NAV levels, or index levels are reproduced here, and none are committed
to this repository.

---

## 4. Distribution check

The Nissay source publishes both a raw NAV and a pre-tax-distribution-reinvested NAV.
These were compared across the entire fixed study window before any analysis:

> **`基準価額` and `税引前分配金再投資基準価額` were identical on all 822 observations.**

Consequently:

- **`基準価額` was used** for the study.
- **No distribution adjustment was required over the observed window.**

**This finding is limited to the observed study window (2023-03-31 → 2026-08-10) and
must not be generalized.** It does not establish that the fund will never distribute,
nor that a future window will require no adjustment. Any future study must repeat this
check over its own window.

---

## 5. Calendar mismatch

The fund NAV is published on Japanese business days; the Nasdaq JPY indexes are
calculated on U.S. index calculation days. The raw mismatch was characterized **before**
any alignment was applied.

| Measure | Count |
| ------- | ----- |
| Dates present in both series under the same calendar label | **791** |
| Japan-only observation dates (fund NAV exists, no index observation) | **31** |
| U.S.-only observation dates (index observation, no fund NAV) | **51** |
| Longest consecutive Japan-only run | **1** observation |
| Longest consecutive U.S.-only run | **3** observations |
| Japan-only clusters / U.S.-only clusters | 31 / 41 |

The counts were identical for all three candidates, which share the same calculation
calendar.

Methodological commitments, held throughout:

- **No forward-fill was used.**
- **No interpolation was used.**
- **No observation was synthesized** for a date on which a series did not publish.
- **Pairing was based on ordered valid observations**, never on blindly adding 24 hours
  to a calendar label.

---

## 6. Empirical lag result

This is the **principal approved finding** of the study.

### Lag convention (declared before computation)

> For a fund observation on Japanese business day **D**, let **p(D)** be the position,
> within the candidate series' ordered list of observations, of the **last candidate
> observation dated on or before D**.
>
> **Lag k** pairs the fund's daily return at **D** with the candidate's daily return at
> candidate-observation index **p(D) + k**.

Mapping to the alignment conventions the study was asked to test:

| Lag | Convention | Meaning |
| --- | ---------- | ------- |
| `0` | **A0** | Same labelled calendar date |
| `−1` | **A1** | Fund NAV one Japanese business day later than the candidate observation |
| `+1` | **A2** | Fund NAV against the *next* candidate observation |

Lag detection used **daily returns**, not index levels. The lag set `{−2, −1, 0, +1, +2}`
was **pre-declared** and was not widened during the study.

### Result — all three candidates

**Preferred lag: `−1`, for all three candidates.**

`NDXJPY`, full window:

| Lag | N | Pearson | Spearman | MAE | RMSE | Mean diff | SD diff |
| --- | - | ------- | -------- | --- | ---- | --------- | ------- |
| −2 | 819 | −0.0256 | −0.0117 | 1.4964% | 2.0833% | −1.51 bp | 2.0845% |
| **−1** | **820** | **0.8731** | **0.8330** | **0.4494%** | **0.7345%** | **+0.10 bp** | **0.7349%** |
| 0 | 821 | 0.0307 | 0.0343 | 1.4583% | 2.0355% | +0.32 bp | 2.0367% |
| +1 | 820 | 0.0220 | −0.0019 | 1.4884% | 2.0453% | +1.33 bp | 2.0465% |
| +2 | 819 | −0.0505 | −0.0406 | 1.5083% | 2.1062% | +3.91 bp | 2.1072% |

`XNDXJPY` and `XNDXNNRJPY` produced the same table to four decimal places at every lag.
At the preferred lag:

| Candidate | N | Pearson | Spearman | MAE | RMSE | Mean diff | SD diff |
| --------- | - | ------- | -------- | --- | ---- | --------- | ------- |
| `NDXJPY` | 820 | 0.8731 | 0.8330 | 0.4494% | 0.7345% | +0.10 bp | 0.7349% |
| `XNDXJPY` | 820 | 0.8731 | 0.8330 | 0.4494% | 0.7345% | −0.19 bp | 0.7349% |
| `XNDXNNRJPY` | 820 | 0.8731 | 0.8331 | 0.4494% | 0.7345% | −0.10 bp | 0.7349% |

### Summary of the contrast

| | Lag −1 | All other tested lags |
| --- | --- | --- |
| Pearson correlation | ≈ **0.873** | approximately **−0.05 to +0.03** |
| RMSE of daily return difference | ≈ **0.7345%** | approximately **2.04% to 2.11%** |
| MAE of daily return difference | ≈ **0.4494%** | approximately 1.46% to 1.51% |

**Lag −1 was selected by multiple independent measures simultaneously** — Pearson,
Spearman, MAE, RMSE, the standard deviation of the return difference, and the near-zero
mean difference — **not by any single statistic.** At every other lag the two series are
effectively unrelated.

---

## 7. Lag robustness

Lag −1 remained the preferred alignment for **all three candidates** in **every** window
tested, under **both** an argmax-Pearson and an argmin-RMSE criterion:

| Candidate | Full window | First half | Second half | Large-move subset |
| --------- | ----------- | ---------- | ----------- | ----------------- |
| `NDXJPY` | **−1** | **−1** | **−1** | **−1** |
| `XNDXJPY` | **−1** | **−1** | **−1** | **−1** |
| `XNDXNNRJPY` | **−1** | **−1** | **−1** | **−1** |

Split point: the median fund observation, **2024-12-02**.

Detail at lag −1 (`NDXJPY`; the other two candidates agree to three decimal places):

| Window | N | Pearson | RMSE |
| ------ | - | ------- | ---- |
| Full | 820 | 0.8731 | 0.7345% |
| First half | 410 | 0.8640 | 0.6803% |
| Second half | 409 | 0.8791 | 0.7859% |
| Large-move subset | 110 | **0.9380** | 1.1585% |

### Large-move subset

**Definition: observations where the absolute daily *fund* return exceeded 2%.**

The 2% threshold was **pre-declared and not optimized**. Conditioning on the fund's own
return (rather than on either series) keeps subset membership independent of the lag
being tested, so N is identical across lags and the comparison is not circular.

| Measure | Value |
| ------- | ----- |
| N | **110** |
| Pearson at lag −1 | **≈ 0.938** |
| RMSE at lag −1 | **≈ 1.159%** |
| Pearson at lag 0 (for contrast) | ≈ 0.053 |

All three candidates gave the same figures to three decimal places.

### Interpretation of the large-move result

> **The timing relationship is at least as clear during large moves as it is over the
> full sample.** Large moves are the observations most relevant to drawdown-triggered
> strategies, so the alignment is most secure precisely where an alignment error would
> matter most.

**This is a statement about observation timing only.** It is **not** a claim about
strategy profitability, about the performance of Strategies A, B or C, or about the
merits of variable DCA. No such claim is made or supported by this study.

---

## 8. Timing interpretation

The empirical evidence **strongly supports a one-observation relationship** in which the
Nissay NAV for a given Japanese business day reflects **the most recent U.S. market
close available before that NAV calculation**, rather than the U.S. close carrying the
same calendar label.

This is **consistent with the previously reviewed Nissay primary documentation**, in
particular the 請求目論見書 valuation rule 「金融商品取引所における計算日に知りうる直近の
日の最終相場」. The documentary expectation and the measured data agree.

### Scope limits on this interpretation — read carefully

- This establishes an **observation-time relationship between two published data
  series**. It does **not** establish the full future execution mapping.
- It does **not** by itself resolve the application-cutoff leg, the order-to-NAV leg, or
  distributor-specific cutoff differences. Those remain part of P1-1.
- **OD-03 (signal observation timing) and OD-04 (execution price convention) are
  unchanged by this artifact.** No Frozen Baseline rule was modified, and none may be
  modified by an evidence artifact.

This is recorded as **Phase-1 evidence relevant to the future signal → order → NAV
mapping**, and nothing more.

---

## 9. Candidate fit comparison

Computed after applying the lag −1 alignment to index **levels**, with both series
normalized to 1.0 at the first aligned observation.

**Level-alignment rule.** The fund level on Japanese business day **D** is paired with
the candidate **level** at index **p(D) − 1**, where **p(D)** is the position of the last
candidate observation dated on or before **D**. This is the level-space counterpart of
the lag −1 return alignment defined in §6.

| Parameter | Value |
| --------- | ----- |
| Aligned observations | **821** |
| Aligned window | 2023-04-03 → 2026-08-10 |
| Window length | **3.35 years** (≈ 244.5 observations/year) |

**Tracking difference is reported as (fund − candidate). A positive value means the fund
out-returned the candidate.** No cost adjustment was applied to any candidate series,
and no fund expense was deducted from the NAV a second time (the NAV already bears fund
costs).

| Series | Cumulative return | Annualized return | Tracking difference | Tracking error | Correlation | MAE | RMSE | Max abs cumulative divergence |
| ------ | ----------------- | ----------------- | ------------------- | -------------- | ----------- | --- | ---- | ----------------------------- |
| **Fund NAV** | ≈ **171.63%** | ≈ **34.71%** | — | — | — | — | — | — |
| `NDXJPY` | ≈ 167.57% | ≈ 34.11% | ≈ **+0.60%/yr** | ≈ 9.53% | 0.9132 | 0.3863% | 0.6089% | 12.32 pp |
| `XNDXJPY` | ≈ 174.33% | ≈ 35.11% | ≈ **−0.40%/yr** | ≈ 9.53% | 0.9132 | 0.3862% | 0.6089% | 9.23 pp |
| `XNDXNNRJPY` | ≈ 172.24% | ≈ 34.80% | ≈ **−0.09%/yr** | ≈ 9.53% | 0.9132 | 0.3862% | 0.6089% | 7.67 pp |

Cumulative return gap (candidate − fund): `NDXJPY` ≈ −4.06 pp; `XNDXJPY` ≈ +2.70 pp;
`XNDXNNRJPY` ≈ +0.61 pp.

### Recorded conclusion, with its limit

> **`XNDXNNRJPY` had the closest empirical level fit over this specific live-product
> overlap window.**
>
> **This does NOT establish that `XNDXNNRJPY` is the Nissay benchmark, and it does NOT
> make it an approved Primary Proxy. P1-2 remains OPEN.**

Three reasons the level ranking must not be acted upon:

1. **The discriminating signal is small relative to the noise.** The annualized tracking
   error is ≈ 9.52%/yr, which over a 3.35-year window gives the annualized tracking
   difference a standard error of roughly **5.20%/yr**. The quantity separating
   `XNDXJPY` from `XNDXNNRJPY` is ≈ **0.308%/yr** — on the order of **6%** of that
   uncertainty.
2. **The full-window figure averages year-by-year gaps of opposite sign.** Annualized
   tracking difference measured per calendar year (candidate − fund) drifted from
   roughly −1.26%/yr in 2023 to roughly +1.09%/yr in 2026 for `XNDXNNRJPY`, with the
   same drift common to all three candidates. The full-window value is a cancellation,
   not a stable relationship.
3. **The window is short and single-regime.** See [§16](#16-limitations).

The one directional statement that is defensible: the fund out-returned the **Price
Return** series, which is the sign expected of a fund that receives dividends. That
corroborates dividend receipt — already known from the fund documents — and does **not**
discriminate between the two total-return variants.

### Note on the two reported correlation figures

Two correlation values appear in this artifact and a future reader should not treat them
as inconsistent:

- **0.8731** (§6) — daily returns computed on each series' own consecutive observations
  and paired by index position.
- **0.9132** (§9) — candidate returns computed **between the aligned candidate
  observations**, so that a fund return spanning a holiday is matched against the
  candidate return spanning the same observations.

The second construction is the more like-for-like of the two. A further restriction to
pairs whose return intervals span exactly one candidate observation (N = 748 of 821,
excluding 73 pairs affected by a Japanese or U.S. holiday) gives Pearson ≈ 0.9226 and
RMSE ≈ 0.5756%. All three constructions agree on lag −1; none changes any conclusion.

---

## 10. Candidate-series relationship (pipeline consistency check)

Annualized differences between the candidate series themselves over the aligned window:

| Relationship | Annualized |
| ------------ | ---------- |
| `XNDXJPY` − `NDXJPY` | ≈ **+1.001%/yr** |
| `XNDXNNRJPY` − `NDXJPY` | ≈ **+0.693%/yr** |
| `XNDXJPY` − `XNDXNNRJPY` | ≈ **+0.308%/yr** |
| **(`XNDXNNRJPY` − `NDXJPY`) / (`XNDXJPY` − `NDXJPY`)** | **≈ 0.692** |

Nasdaq's *Index Versions* documentation describes the Notional Net Total Return variant
as reinvesting approximately **70%** of cash dividends. The measured ratio of ≈ 0.692 is
consistent with that description.

Additionally, the daily return difference **between** `XNDXJPY` and `XNDXNNRJPY` had a
standard deviation of ≈ **0.00167%**, against a fund-vs-candidate daily residual of
≈ 0.6089%.

> **How to read this.** This is a **pipeline and data-consistency check** — it confirms
> that retrieval, date mapping and normalization behaved correctly, and that the three
> candidates differ from one another exactly as Nasdaq's own documentation states.
>
> **It is NOT identification of Nissay's undisclosed benchmark dividend convention.** It
> says nothing about what 「配当込み」 means in the Nissay benchmark.

---

## 11. Drawdown-zone agreement

This section matters because the Frozen Baseline evaluates **deterministic
drawdown-triggered allocation**: Strategies B and C fire on daily drawdown zones.

### Diagnostic zone boundaries

| Zone | Condition |
| ---- | --------- |
| High | `DD > −10%` |
| Normal | `−20% < DD ≤ −10%` |
| Large Drop | `DD ≤ −20%` |

### Reference-high definition used, and why it is a diagnostic only

The drawdown reference used here is the **running maximum of each aligned series, seeded
at the first aligned observation (2023-04-03)**.

> **This is NOT the Frozen Baseline Reference High.** [`docs/experiment_spec.md` §7](../experiment_spec.md#7-drawdown-reference-high)
> permits historical observations preceding the measured performance start to initialize
> the Daily Closing ATH as warm-up data. The fund simply **has no history before its
> inception**, so a symmetric seeding at the first aligned observation was the only
> defensible choice for a fund-vs-candidate comparison.
>
> **This section is a proxy-alignment diagnostic. It is not a backtest**, and it must not
> be cited as one.

### Results

| Candidate | Matched dates | Agreement | H↔N | N↔L | H↔L | Candidate in deeper zone | Candidate in shallower zone |
| --------- | ------------- | --------- | --- | --- | --- | ------------------------ | --------------------------- |
| `NDXJPY` | **821** | **99.51%** (817) | 3 | 1 | 0 | 3 | 1 |
| `XNDXJPY` | **821** | **99.39%** (816) | 4 | 1 | 0 | 1 | 4 |
| `XNDXNNRJPY` | **821** | **99.39%** (816) | 4 | 1 | 0 | 2 | 3 |

Supporting detail:

| | Fund | `NDXJPY` | `XNDXJPY` | `XNDXNNRJPY` |
| --- | --- | --- | --- | --- |
| Maximum drawdown in window | −27.74% | −27.08% | −26.92% | −26.96% |
| Days outside the High zone | **111** | 112 | 107 | 109 |
| Distinct entries into Normal zone | 11 | 10 | 10 | 10 |
| Distinct entries into Large-Drop zone | **4** | **4** | **4** | **4** |

**All four observed Large-Drop entries occurred on the same dates for the fund and for
all three candidates:**

- **2024-08-06**
- **2024-09-09**
- **2025-04-04**
- **2025-04-11**

Disagreements were few and isolated, with no consecutive runs. Two disagreement dates
(**2024-09-10** and **2026-08-03**) were common to all three candidates, which points to
a fund-side effect rather than a candidate-specific one.

A robustness check re-seeding the running maximum six months later (2023-10-02, 697
matched dates) gave agreement of 99.43% / 99.28% / 99.28% — essentially unchanged. The
result is not an artifact of the seeding date.

### Interpretation, with its limits

> **For the observed live-product overlap window, all three candidate series behaved
> almost identically as drawdown-zone signal generators.**

This must **not** be generalized:

- **99.4% agreement is not proof of future equivalence.** It is a measurement over one
  short, single-regime window.
- **Most observations were in the High zone.** Only **111 of 821** days fell outside it,
  and only **four** Large-Drop entries were observed. The headline agreement percentage
  is dominated by quiet High-zone days; the number of genuinely informative dates is
  small.
- The spread in agreement between candidates (99.51% vs 99.39%) amounts to **one date out
  of 821** and must not be read as a ranking.

---

## 12. Residual

After timing alignment, a **material fund-vs-candidate daily-return residual remains**.

| Measure | Approximate value |
| ------- | ----------------- |
| Daily return RMSE (like-for-like Stage-3 aligned comparison) | ≈ **0.609%** |
| Annualized tracking error | ≈ **9.52%** |

Possible contributors **may** include, in no implied order:

- FX observation convention differences
- Fund expenses
- Trading / rebalancing effects
- Futures basis
- Dividend timing
- Cash-flow timing
- Benchmark-construction differences
- Residual calendar effects

> **This study does NOT causally attribute the residual to any one factor.** Decomposition
> was explicitly out of scope.

One bounded, defensible observation is recorded:

> **The disclosed annual fund-expense magnitude is not sufficient, by itself, to explain
> the observed scale of the daily return residual.**

That statement is deliberately left unquantified. A numeric ratio between a slow,
deterministic annual fee accrual and a daily-return RMSE would compare quantities of
different kinds and could mislead; the Owner directed that no such ratio be recorded.

A partial, non-causal decomposition observation is also available: restricting the
comparison to pairs whose return intervals span exactly one candidate observation
reduced the daily RMSE from ≈ 0.7345% to ≈ 0.5756%, indicating that **some** of the
residual is attributable to unequal return spans across the two calendars — and that
this is a minority of it, not the bulk.

---

## 13. What the study establishes

Established / strongly supported by the evidence:

1. **A one-observation timing offset (lag −1) exists** between the Nasdaq candidate
   observations and the Nissay NAV observations under the tested mapping.
2. **The result is robust** across the full window, both split half-windows, and the
   large-move subset, under two independent selection criteria.
3. **All three candidates have essentially identical daily timing behavior** for the
   purpose studied.
4. **All three candidates show very high drawdown-zone agreement** with the actual fund
   over the observed live-product window, including identical Large-Drop entry dates.
5. **`XNDXNNRJPY` has the closest empirical level fit in this specific window**, but the
   evidence is **insufficient to identify it as the true benchmark** and insufficient to
   distinguish it from `XNDXJPY` on this sample.

---

## 14. What the study does NOT establish

The study does **not** establish any of the following:

- An **approved Primary Proxy** (P1-2 remains OPEN)
- Whether Nissay's 「配当込み」 is **Gross, Net, or Notional Net** total return
- Nissay's **benchmark FX provider**
- Nissay's **benchmark FX fixing time**
- The fund's **exact FX conversion convention**
- The **composition of the residual**
- **Strategy profitability**
- **Variable DCA superiority** over simple DCA, or any comparison among Strategies A, B
  and C
- The **Phase-2 Baseline start date**
- The **Phase-2 Dataset Cutoff**
- **Future equivalence** of the three candidate series

---

## 15. Phase-1 status mapping

Statuses as approved by the Owner. **No item was upgraded merely because this artifact
was recorded.** The open-items register in
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements)
remains the authoritative list of requirements.

| # | Requirement | Status | Rationale |
| - | ----------- | ------ | --------- |
| **P1-1** | Signal → order → execution date → applicable NAV mapping | **SUBSTANTIALLY ADVANCED** | The one-observation offset between a Nasdaq JPY index and the fund NAV is now empirically confirmed and robust. The order-to-NAV leg, application cutoff history, and distributor-specific cutoffs are not resolved by this study. |
| **P1-2** | Approved Primary Proxy | **OPEN** | Not approved. The three candidates are interchangeable for signal purposes over this window and indistinguishable for level purposes at this sample size. |
| **P1-3** | Proxy return composition / dividend treatment | **PARTIAL** | The fund out-returned Price Return and lagged both total-return variants, corroborating dividend receipt. Gross vs. notional-net remains UNKNOWN; the discriminating quantity is far inside the measurement noise. |
| **P1-4** | Cost / expense treatment without double-counting | **PARTIAL** | No cost was deducted twice and no candidate was cost-adjusted. New evidence: fund expenses alone cannot account for the scale of the daily residual, reinforcing the Frozen §14.5 prohibition on equating expense ratio with tracking difference. |
| **P1-5** | Exact Baseline start date | **OPEN** | Depends on P1-2. Newly sharpened: live-product validation can never begin before 2023-03-31. |
| **P1-6** | Fixed Baseline Dataset Cutoff | **OPEN** | A *study* cutoff was fixed and applied, demonstrating the mechanism is workable, but the Baseline Dataset Cutoff was not set and remains an Owner decision. |
| **P1-7** | Currency treatment | **SUBSTANTIALLY ADVANCED** | The magnitude of the currency/observation mismatch is measured for the first time (≈ 9.52%/yr tracking error). Currency treatment is confirmed as a first-order, not second-order, issue. The convention itself remains undisclosed. |
| **P1-8** | Licensing / redistribution | **PARTIAL** | Unchanged by this study. Local-only handling was demonstrated end to end, but redistribution remains restricted and the automated-capture question is unresolved. |
| **P1-9** | Revision / restatement behaviour | **PARTIAL** | No restatement testing was performed (single retrieval). One practical data-integrity finding recorded in §3 (`Value` vs null `Close`). |

---

## 16. Limitations

1. **Only ≈ 3.35 years of actual fund overlap** (821 aligned observations).
2. **Strongly rising market regime** throughout the window; a single regime is observed.
3. **Only 111 days outside the High drawdown zone** — the informative sample for
   zone-agreement purposes is much smaller than the 821 matched dates suggests.
4. **Only four Large-Drop entries** were observed.
5. **The drawdown reference high had to be seeded from fund inception** for this
   diagnostic, because no earlier fund history exists. This is not the Frozen Baseline
   Reference High.
6. **The residual remains undecomposed** (≈ 9.52%/yr tracking error left unexplained by
   design).
7. **Single retrieval; no historical restatement study** was performed on either source.
8. **Licensing and redistribution questions remain unresolved** for both Nasdaq and
   Nissay data (P1-8).
9. **Exploratory, not confirmatory.** The lag set and large-move threshold were
   pre-declared and not optimized, but this is a single pass over one sample with no
   out-of-sample confirmation.
10. **No statistical significance is claimed** for any proxy comparison; no p-value was
    used to select anything; no causal or predictive claim is made.
11. **Fund-side idiosyncrasies are unobserved** — subscription/redemption flows, futures
    positioning, and actual dividend receipt timing are not visible in NAV alone.

---

## 17. Next research step

Exactly one approved research direction is recorded:

> ### Phase-1 FX residual decomposition
>
> **Purpose:** determine how much of the post-alignment fund-vs-candidate residual can be
> explained by differences in **FX observation convention**.

Conditions attached to this direction:

- **This is a research direction only. It was not performed in this task, and it has not
  been started.**
- **No synthetic USD × USD/JPY series has been approved**, proposed for approval, or
  constructed. Nothing in this artifact authorizes building one.
- **The next study must first identify an authoritative FX data source with acceptable
  licensing and data-handling terms.** That licensing check must precede any analysis,
  in the same way the repository-safety check preceded this study.
- No Nissay FX fixing time, quoting institution, or conversion algorithm may be inferred
  or reconstructed without supporting primary evidence.

---

## Appendix — reproduction notes

A future researcher reproducing this study should note:

- The fund NAV source is the issuer's official since-inception daily series; it always
  returns data from inception to the present, with **no as-of parameter**. A study cutoff
  must therefore be **imposed and recorded by the researcher**, as was done here.
- The Nasdaq GIW end-of-day series carries the index level in `Value`; `Close` was null
  (§3).
- Nasdaq index observation timestamps were normalized to the **U.S. Eastern calendar
  date** of the index observation before any pairing.
- Both raw sources are subject to unresolved licensing constraints (P1-8). **Raw data
  must remain outside the repository** until redistribution rights are established.
- The alignment definitions in §6 and §9 are sufficient to reconstruct every derived
  statistic in this artifact from the two sources.

---

**End of Phase-1 Evidence Artifact. Owner Review: APPROVED. Primary Proxy: NOT APPROVED —
P1-2 remains OPEN.**
