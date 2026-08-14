# Simulation Trial — Strategy D Stage D-H1: A/B/C/D Economic Comparison Result (Preservation Checkpoint)

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** Preserves the factual, one-window economic
comparison result only. **Does not** authorize adoption, optimization, another validation window,
Strategy E, qualification-lane promotion, Baseline modification, Phase 2 work, or any new economic
metric (§7).
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling D-H1 chain:** dataset-selection policy `f8332a543f7bab4c8b5f42974813ccd70be9137f` ·
deterministic selection rule `f025bbf0dd5df9a4b037936822b1ced4e263948c` · bounded-release decision
`b722fb27ada370cf1adf22f6a8e5a99331a9a705` · mechanical-result checkpoint
`8a76769493cd690800011e518495a34b2a3c3e8b` · economic-comparison methodology
`f0f60fa1312c3c51a2d87b4c522911c340e160ef` (`DH1-EV-D1`…`D12`) — **none modified by this artifact.**
**Strategy-D authority:** hypothesis `5a3f54ab11a1de8204cae659ad2732867e7d1274` · semantics
`62c5c429ce6aa4742c6327a9c39687421fd94325` — **unchanged.**

This artifact does not reproduce the full event logs or manifests — those remain in the external,
non-git evidence store, referenced here by run ID and checksum (§2).

---

## 1. What is preserved

The factual result of the D-H1 A/B/C/D economic comparison, computed exclusively from four
already-preserved mechanical states (no strategy was rerun to produce or verify this artifact),
independently reproduced in this task and confirmed to match the existing evidence exactly.

## 2. External evidence reference (not copied into git)

| Field | Value |
| --- | --- |
| Source mechanical runs | `MP-DH1-A-001`, `MP-DH1-B-001`, `MP-DH1-C-001`, `MP-DH1-D-001` |
| Economic-evaluation runs | `MP-DH1-EV-A-001`, `MP-DH1-EV-B-001`, `MP-DH1-EV-C-001`, `MP-DH1-EV-D-001`, `MP-DH1-EV-COMPARISON-001` |
| Evidence store | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-p/` |
| Dataset (shared by all four) | `NDXJPY`, `1985-01-31 → 1987-07-26`, sha256 `4b4d076e6c1c22be88dab25a1506b5a625e8fd9a8082c6befb7fb09898584439` |
| Terminal observation | `1987-07-24` (dataset's actual final observation), price `27.3328140048553`, verified from bytes |
| Funding (all four, identical) | `cash_granted_jpy = 360000.0`, `budget_units_granted = 36.0` |

Independently re-derived in this task from the preserved `manifest.json`/`terminal_state.json` files
and confirmed to match the already-computed `MP-DH1-EV-*` results field-for-field.

## 3. Exact A/B/C/D economic quantities

| Strategy | Deployed (¥) | Available (¥) | Reserved-unexecuted (¥) | Total unconverted (¥) | Exposure units | Exposure market value (¥) | Combined terminal value (¥) | Funding-relative simple return | Deployment ratio | Residual-cash ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 300,000.0 | 50,000.0 | 10,000.0 | 60,000.0 | 12,044.11058059430824814605895501985754781 | 329,199.4343532940069072016190878156927051 | 389,199.4343532940069072016190878156927051 | 0.08110953987026113029778227524393247973639 | 0.8333... | 0.1667... |
| B | 340,000.0 | 20,000.0 | 0.0 | 20,000.0 | 13,579.96260912789783898345429247934322941 | 371,178.5921881823263000353876314558529579 | 391,178.5921881823263000353876314558529579 | 0.08660720052272868416676496564293292488306 | 0.9444... | 0.0556... |
| C | 340,000.0 | 20,000.0 | 0.0 | 20,000.0 | 13,496.40902566995074277225481955138019927 | 368,894.8376320871037836911971847835672553 | 388,894.8376320871037836911971847835672553 | 0.08026343786690862162136443662439879793139 | 0.9444... | 0.0556... |
| D | 360,000.0 | 0.0 | 0.0 | 0.0 | 14,378.59091311845180901645899398584995914 | 393,007.3510801691757242744156895599689186 | 393,007.3510801691757242744156895599689186 | 0.09168708633380326590076226580433324699611 | 1.0000 | 0.0000 |

Labeled throughout as **`MODE-P TERMINAL ECONOMIC VALUE — NOT BASELINE TTEV — SIMULATION-TRIAL ONLY`**,
exactly per `DH1-EV-D1`/`MP-EV-D3`'s precedent labeling requirement.

**Deployment-amount vs. allocation-timing, distinguished using only already-permitted fields (no new
metric introduced):**

- **B vs. C isolates the timing effect cleanly**: both deployed *identical* cash (`¥340,000`), yet B
  acquired `83.5536...` more exposure units and ended with a `¥2,283.75` higher combined terminal
  value than C. Since deployed cash is identical, this entire difference is attributable to *when*
  each strategy executed its purchases (different observation dates, different execution prices),
  not to how much was deployed.
- **A vs. D, and B vs. D, combine both effects**: D deployed `¥60,000` more than A and `¥20,000` more
  than B, so their exposure/terminal-value differences reflect *both* the larger deployed amount and
  whatever timing differences exist. This artifact does not further decompose those combined effects,
  since doing so would require a new derived metric (e.g., an average-acquisition-price field) outside
  the approved allow-list — deferred, not computed.

## 4. Factual ordering on this D-H1 window

By combined terminal value: **`D > B > A > C`**
By funding-relative simple return: **`D > B > A > C`** (identical ordering, since the denominator —
`cash_granted_jpy` — is identical across all four)

**This is a factual ordering on this one independently-selected D-H1 window only.** It is not a
superiority claim, not evidence of robustness, not evidence of generalization, not statistical
validation, and not an adoption decision (§7).

## 5. B vs. D comparison (the registered Strategy-D mechanism question)

**Question**: did Strategy D deploy more of the available funding than Strategy B, in the direction
predicted by the registered Strategy-D hypothesis (addressing Strategy B's undeployed-cash behavior)?

**Answer: YES.**

| Quantity | B | D | D − B |
| --- | --- | --- | --- |
| Cash deployed | ¥340,000.0 | ¥360,000.0 | **+¥20,000.0** |
| Total unconverted cash retained | ¥20,000.0 | ¥0.0 | **−¥20,000.0** |
| Exposure units acquired | 13,579.9626... | 14,378.5909... | **+798.6283...** |
| Combined terminal value | ¥391,178.5922 | ¥393,007.3511 | **+¥1,828.7589** |
| Funding-relative simple return | 0.08660720... | 0.09168709... | **+0.508 percentage points** |

## 6. Strategy-D hypothesis observation — narrowest permissible statement

> On this one independently-selected D-H1 window, Strategy D's deployment behavior differed from
> Strategy B's in the direction predicted by the registered Strategy-D hypothesis, by the factual
> amounts stated in §5. This is a one-window mechanism observation, not evidence of economic
> superiority, robustness, generalization, or suitability for adoption.

This statement is not strengthened anywhere in this artifact.

## 7. Evidentiary ceiling — prohibited interpretations

This artifact does **not** state, and must not be read to imply: that Strategy D is superior to A, B,
or C; that Strategy D "solved" Strategy B's cash-drag behavior in general; that Strategy D should
replace B; that Strategy D is optimal, more efficient, or more robust; that this result generalizes
beyond this one window; that Strategy D is statistically validated; or that Strategy D should be
adopted. No `CAGR`, `XIRR`, annualized/time-weighted return, Sharpe ratio, volatility, portfolio-value
maximum drawdown, tracking error, risk-adjusted return, statistical significance, or confidence
interval appears anywhere in the evidence this artifact references.

## 8. §18.4.7 anti-contamination — preserved, not weakened

- Strategy D was proposed post-result, from earlier Mode-P observations on the original 2018-2020
  window (specifically, Strategy B's undeployed-cash behavior).
- D-H1 was independently selected under the frozen dataset-selection policy and deterministic rule,
  before any D-H1 result of any kind existed.
- The D-H1 A/B/C/D economic result is now known.
- Any future artifact deciding `O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`, Stage G, Stage H, or Primary
  Proxy selection MUST state that this result was known and affirm it was not used normatively.
- `NDXJPY` qualification state is **not** changed by this result — it remains one of the three active
  `C-1` candidates, `QUALIFICATION INCOMPLETE`.

## 9. Strategy-D status after this checkpoint

Strategy D remains exactly: **`OWNER-GENERATED POST-RESULT ALTERNATIVE HYPOTHESIS`**. This preserved
one-window result does **not** change that status to adopted, validated, Baseline, formal, production,
qualification evidence, or approved for Phase 2. The Strategy-D rule and semantic decision
(`5a3f54a`/`62c5c42`) are unmodified.

## 10. Qualification-state preservation

Unchanged: `O-4`, `P1-x`, `M-x`, `HG-8`, Primary Proxy, Stage G, Stage H. Phase 2 remains BLOCKED.

## 11. Scope

This artifact preserves a factual checkpoint only. It does not modify the Frozen Baseline, Strategy
D's implementation or semantics, the D-H1 policy/rule/release/checkpoint/methodology chain, or any
qualification artifact. It does not authorize Strategy D adoption or optimization, another D-H1/D-H2
validation window, Strategy E or any new strategy, qualification-lane promotion, Phase 2 work, or any
new economic metric.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. Factual one-window checkpoint only.
No new computation performed beyond independent verification of already-produced values. No
superiority, robustness, generalization, or adoption claim. `f8332a5`, `f025bbf`, `b722fb2`, `8a76769`,
`f0f60fa`, `5a3f54a`, `62c5c42`, and every preserved Strategy-D and Mode-P evidence generation are
unchanged.**
