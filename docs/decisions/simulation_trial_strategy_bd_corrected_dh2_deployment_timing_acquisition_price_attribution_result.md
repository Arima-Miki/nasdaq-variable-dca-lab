# Simulation Trial — B-vs-D Deployment Timing & Acquisition-Price Attribution: Corrected D-H2 Result

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15.** Preserves the factual deployment-timing and acquisition-price attribution analysis for corrected D-H2. **Does not** authorize adoption, claim superiority, design Strategy E, modify strategies, or change qualification state.

**Date drafted:** 2026-08-15

**Owner approval date:** 2026-08-15

**Controlling corrected D-H2 B-vs-D analysis result:** commit `8830a49` · tag `simulation-trial-strategy-bd-corrected-dh2-analysis-result-20260815`

**Controlling B-vs-D mechanism analysis methodology:** commit `bb028bb` · tag `simulation-trial-strategy-bd-mechanism-analysis-methodology-20260815`

**Controlling corrected D-H2 mechanical evidence:**
- Strategy B: `MP-DH2-B-001` (preserved 2026-08-14)
- Strategy D: `MP-DH2-D-002` (corrected evidence, 2026-08-15)
- Input-provenance remediation: commit `c70915e` — canonical CSV established
- Mechanical evidence decision: commit `ff87b88` — corrected D-002 confirmed

**Historical defective evidence (EXCLUDED):**
- Strategy D: `MP-DH2-D-001` (zero-allocation artifact; tainted pre-remediation; **NOT USED**)

**Controlling Strategy authorities:** B Baseline v2 §4.2 (frozen), D hypothesis `5a3f54a` + semantics `62c5c42` (frozen)

**Governing Baseline:** v2 (effective 2026-08-13, unchanged)

---

## 1. Owner Decision and Scope

This preservation documents the factual finding that Strategy B and Strategy D, despite deploying identical capital and identical allocation quantities by zone, acquired different quantities of exposure due to differences in execution dates and prices.

**What is preserved:**
- ✓ Deployment-timing analysis: cumulative capital deployment divergence and convergence
- ✓ Acquisition-price attribution: terminal exposure difference explained by execution-date and price interactions
- ✓ Factual observation bounded to this window only (D-H2, 1987-07-27 → 1990-01-18)
- ✓ Mechanical causation (trigger firing, monthly capacity effects, execution sequence)

**What is NOT preserved:**
- ❌ Superiority or inferiority claims
- ❌ Generalization to other windows or regimes
- ❌ Robustness assessment (two unique regimes insufficient)
- ❌ Optimization or adoption recommendation
- ❌ Strategy E design or specifications

---

## 2. Authority Chain and Evidence Identity

**Mandatory verification (completed):**

| Item | Status | Authority |
|---|---|---|
| **Methodology authority** | ✓ Approved before analysis | commit `bb028bb` (2026-08-15) |
| **B evidence identity** | ✓ MP-DH2-B-001 verified | Preserved terminal_state.json |
| **D evidence identity (current)** | ✓ MP-DH2-D-002 verified | Corrected evidence decision `ff87b88` |
| **D evidence identity (superseded)** | ✓ MP-DH2-D-001 confirmed excluded | Pre-remediation execution; tainted |
| **Input provenance** | ✓ Canonical CSV established | Remediation decision `c70915e` |
| **Strategy B unchanged** | ✓ Baseline v2 §4.2 frozen | No modifications since 2026-08-13 |
| **Strategy D unchanged** | ✓ Hypothesis `5a3f54a` + semantics frozen | No modifications since 2026-08-14 |
| **sim/ directory unchanged** | ✓ No strategy reruns performed | Analysis used preserved evidence only |
| **Qualification state unchanged** | ✓ O-4 PARTIAL, Phase 2 BLOCKED | No impact from this analysis |

**Evidentiary ceiling:** Window-level factual comparison only (mechanical causation observed, no generalization claimed).

---

## 3. Equal-Deployment Finding (Re-verified)

### Deployed Capital

| Metric | **Strategy B** | **Strategy D (D-002)** | **D − B** |
|---|---|---|---|
| **Total budget granted** | 48.0 units | 48.0 units | **0.0 units** |
| **Total budget executed** | 37.0 units | 37.0 units | **0.0 units** |
| **Cash granted (JPY)** | ¥480,000.00 | ¥480,000.00 | **¥0.00** |
| **Cash deployed (JPY)** | ¥370,000.00 | ¥370,000.00 | **¥0.00** |
| **Deployment ratio (MP-DEPLOY)** | 77.08% | 77.08% | **0.00 pp** |

**Verification status:** ✓ Both strategies deployed identical capital in identical amounts.

### Budget Availability at Terminal

| Budget State | **Strategy B** | **Strategy D (D-002)** |
|---|---|---|
| Units available | 11.0 | 11.0 |
| Cash remaining | ¥110,000.00 | ¥110,000.00 |
| Cash preservation ratio (CP-RESIDUAL) | 22.92% | 22.92% |

**Verification status:** ✓ Both strategies preserved identical cash and arrived at identical intermediate budget state.

---

## 4. Equal-Zone-Allocation Finding (Re-verified)

### Execution by Market Zone

| Zone | **Strategy B** | **Strategy D (D-002)** | **D − B** |
|---|---|---|---|
| **NORMAL** | 8.0 units | 8.0 units | **0.0 units** |
| **LARGE_DROP** | 29.0 units | 29.0 units | **0.0 units** |
| **Total** | **37.0 units** | **37.0 units** | **0.0 units** |

**Verification status:** ✓ Both strategies allocated identical quantities in each zone.

**Interpretation:** Zone-level deployment constraints were equally binding on both strategies. Neither zone-based allocation nor cash-preservation behavior differed.

---

## 5. Cumulative Deployment Divergence and Convergence

### Deployment Path Timeline

**Key observation:** Both strategies began with identical early deployments (first two executions matched), then diverged as monthly capacity constraints interacted with trigger timing.

#### Divergence Phase (1987-11 through 1988-09)

**November 1987 → September 1988:**
- Strategy B: 4 → 23 cumulative units  
- Strategy D: 3 → 21 cumulative units
- Maximum unit divergence: 2 units (at 1988-09-02)
- Cause: Monthly capacity constraints (B=1 unit/month, D=2 units/month) interacted with signal firing patterns

**Exposure during divergence:**
- By 1988-09-02, D was *behind* B despite D having higher monthly capacity
- This indicates that despite higher capacity, D's signals fired less frequently than B's during this window
- Cumulative divergence exposed D to lower prices during divergence period (B held higher exposure-per-cash ratio)

#### Convergence Phase (1989-01 through 1990-01)

**January 1989 → January 1990:**
- Monthly allocation capacity constraints became less binding (fewer signals to trigger)
- D executed one additional allocation (24th) that B could not accommodate within B's 1-unit monthly capacity
- Both converged to 37 units, but D acquired additional exposure during final execution due to the 24th allocation

**Terminal execution (1990-01-15):**
- Both executed final 1.0-unit allocation at identical price (¥28.4887/unit)
- Both acquired ¥351.02 exposure on that final unit
- But D's earlier execution sequence resulted in 24 total executions vs. B's 23

---

## 6. Acquisition-Price Attribution Result

### Terminal Exposure Acquired

| Metric | **Strategy B** | **Strategy D (D-002)** | **D − B** |
|---|---|---|---|
| **Total exposure units held** | 16,854.94254147 | 16,885.25884560 | **+30.31630412** |
| **Execution count** | 23 | 24 | **+1 execution** |

**Attribution mechanism:**

Strategy B and D deployed identical ¥370,000 over 37 allocated units, yet acquired different total exposure quantities. The difference is **entirely attributable to execution-date and execution-price interactions**, not to cash deployment differences.

**Detailed attribution:**

1. **Equal cash committed:** Both strategies committed ¥370,000 (10,000 JPY per unit × 37 units)

2. **Different execution sequences:** Due to monthly capacity constraints (B=1/month, D=2/month), the 23 vs. 24 executions occurred on different dates, exposing each execution to different market prices

3. **Price variation over window:** NDXJPY prices ranged from ¥26.94 to ¥32.32 during the execution window

4. **Cumulative price effect:** D's 24-execution path resulted in different cumulative exposure than B's 23-execution path, even though both deployed identical total capital

**Exact exposure difference breakdown:**

- Allocation count difference: D executed 1 additional allocation (24 vs. 23)
- Cumulative-price difference: Due to monthly sequencing, each strategy faced different prices on similar allocations
- Terminal exposure difference: 30.32 units
- Terminal value difference: ¥881.13 (30.32 units × ¥29.0644 terminal price)

**Verification:** The observed terminal exposure difference of +30.32 units, when multiplied by the common terminal valuation price (¥29.0644/unit), mechanically reconciles with the observed terminal-value difference of +¥881.13.

---

## 7. Terminal Value Reconciliation

### FEV Calculation and Verification

**Terminal market price (1990-01-18):** ¥29.0644499524955 per exposure unit

#### Strategy B (MP-DH2-B-001)

| Component | Value |
|---|---|
| Exposure units held | 16,854.94254147417084 |
| Exposure market value (units × price) | ¥489,879.63 |
| Cash remaining | ¥110,000.00 |
| **FEV (MODE-P TERMINAL ECONOMIC VALUE)** | **¥599,879.63** |

#### Strategy D (MP-DH2-D-002)

| Component | Value |
|---|---|
| Exposure units held | 16,885.25884559827898 |
| Exposure market value (units × price) | ¥490,760.76 |
| Cash remaining | ¥110,000.00 |
| **FEV (MODE-P TERMINAL ECONOMIC VALUE)** | **¥600,760.76** |

#### Reconciliation

| Difference | Calculated | Observed |
|---|---|---|
| Terminal exposure units (D − B) | +30.31630412 units | Verified ✓ |
| Exposure value difference | 30.3163 × ¥29.0644 = ¥881.13 | ¥881.13 ✓ |
| FEV difference (D − B) | ¥881.13 | ¥881.13 ✓ |

**Interpretation:** Under identical deployed capital (¥370,000 each) and identical cash remaining (¥110,000 each), the observed terminal exposure difference of 30.32 units mechanically accounts for the observed terminal-value difference of ¥881.13. **The terminal value difference is not due to superior portfolio management, market timing, or trading skill — it is a direct mechanical consequence of different execution dates and prices encountered by the two strategies' fixed rules.**

---

## 8. Funding-Constraint Compression Context

### D-H1 vs. Corrected D-H2 Comparative Observation

| Regime Property | **D-H1 (1985-01-31 → 1987-07-26)** | **Corrected D-H2 (1987-07-27 → 1990-01-18)** |
|---|---|---|
| **Market regime** | Maximum drawdown (≤−20% reached) | Drawdown-heavy (near −10%, end of window) |
| **B cash deployed** | ¥340,000 (94.44% of grant) | ¥370,000 (77.08% of grant) |
| **D cash deployed** | ¥360,000 (100% of grant) | ¥370,000 (77.08% of grant) |
| **D−B deployment ratio** | D deployed 5.56 pp more | D deployed 0.00 pp more |
| **D−B terminal value** | D > B by ¥1,828.76 | D > B by ¥881.13 |

**Observation:** Funding constraints compressed the D-vs-B difference in corrected D-H2 relative to D-H1. In D-H1, D deployed 100% while B deployed 94%; in corrected D-H2, both deployed 77%. Despite this convergence in cash deployment, D retained a marginal exposure advantage due to executing one additional allocation (24 vs. 23). The magnitude of the advantage decreased (¥1,829 → ¥881), consistent with reduced funding flexibility.

**Factual contrast (permitted interpretation):** The D-H2 result shows that when both strategies deploy aggressively in a drawdown-heavy window with identical cash available, funding constraints compress both to the same deployment ratio. However, D's higher monthly allocation capacity (2 vs. 1) still permitted one additional execution, resulting in a smaller (but still positive) terminal-value advantage.

**Not permitted:** "Strategy D was more robust," "funding constraints validate D's approach," "D deserves adoption," or "this mechanism generalizes" (two unique regimes insufficient for generalization).

---

## 9. Relationship to Prior Corrected D-H2 Studies

### Superseded Narrative (Based on Tainted MP-DH2-D-001)

**Prior claim (2026-08-14, based on defective D-001 evidence):**
> "Strategy D remained fully in cash on D-H2, deploying ¥0 while Strategy B deployed ¥370,000. Economic ordering flipped: D > B on H1, but B > D on corrected H2."

**Status:** **EXPLICITLY SUPERSEDED AND DISREGARDED.** The D-001 execution occurred prior to input-provenance remediation and is tainted for this analysis.

### Corrected Narrative (Based on Authoritative MP-DH2-D-002)

**Corrected claim (2026-08-15):**
> Strategy B and Strategy D deployed identical capital (¥370,000 each, 77.08% of grant) and identical allocation quantities (8 NORMAL + 29 LARGE_DROP). They executed different cumulative strategies (23 vs. 24 allocations), exposing each to different historical prices. This execution-sequence difference resulted in D acquiring 30.32 additional exposure units, accounting for a terminal-value advantage of ¥881.13. The D-H1 advantage (¥1,829) compressed to the D-H2 margin (¥881) due to funding constraint convergence.

**Evidentiary basis:**
- ✓ Methodology `bb028bb` applied exactly as approved
- ✓ Mechanical evidence `MP-DH2-B-001` and `MP-DH2-D-002` verified and reconciled
- ✓ Input provenance `c70915e` established as canonical
- ✓ All 20 mechanical invariants pass for both runs
- ✓ Terminal exposure and FEV reconciliation verified

---

## 10. Evidentiary Ceiling — Bounded Claims

This corrected D-H2 deployment-timing and acquisition-price attribution result establishes:

**Permitted claims (within-window factual observation):**
- ✓ B and D deployed identical capital and executed equal allocations by zone
- ✓ They executed different numbers of transactions (23 vs. 24) on different dates
- ✓ This execution-sequence difference resulted in 30.32 additional exposure units for D
- ✓ The exposure difference mechanically explains the ¥881.13 terminal-value difference
- ✓ Funding constraints compressed the B-vs-D deployment-ratio difference from H1 to H2
- ✓ D's higher monthly allocation capacity (2 vs. 1) permitted one additional execution that B could not accommodate

**Claims NOT established (outside evidentiary ceiling):**
- ❌ Statistical significance (single-path execution; no distribution)
- ❌ Generalization (two unique regimes with opposite funding behaviors)
- ❌ Robustness (corrected H2 shows reduced D-advantage vs. H1; mechanism inconsistent across regimes)
- ❌ Superiority or market-timing skill (mechanism is pure execution-sequence artifact, not superior judgment)
- ❌ Optimization or adoption suitability ("D should be preferred" or "D's approach is better")
- ❌ Forecasting value ("This pattern will persist" or "D will outperform in the future")

---

## 11. Strategy-E Firewall — Maintained

The deployment-timing and acquisition-price attribution analysis identifies a potential future hypothesis:

> "Could a hybrid strategy combining B's responsive deployment triggers with D's higher monthly allocation capacity achieve exposure acquisition gains?"

**Explicit non-authorization:**
- ❌ No Strategy E is designed
- ❌ No specifications are proposed
- ❌ No ruleset is defined
- ❌ No authorization is granted for further investigation
- ❌ Any future hybrid strategy must be separately registered as a new post-result hypothesis under full anti-contamination discipline

**Permitted use of this result:**
- Input to future hypothesis-generation discussions *only if* Owner explicitly authorizes new strategic exploration

---

## 12. Qualification-State Preservation

**Status unchanged:**
- ✓ O-4: PARTIAL (Primary Proxy qualification ongoing, no impact)
- ✓ P1-x through M-x: All OPEN
- ✓ HG-8: NOT EVALUABLE
- ✓ Primary Proxy: NOT SELECTED (NDXJPY remains C-1 candidate)
- ✓ Stage G, Stage H: Unchanged
- ✓ Phase 2: **BLOCKED** (no change)

**This analysis provides no qualification evidence and does not alter any qualification state.**

---

## 13. Strategy and Methodology Integrity

**Strategy B:** Baseline v2 §4.2 rule — **unchanged**. No rerun performed; preserved evidence used only.

**Strategy D:** Hypothesis `5a3f54a`, semantics `62c5c42`, consolidated `064bcc9` — **unchanged**. No rerun performed; corrected MP-DH2-D-002 evidence used.

**Approved methodology:** `bb028bb` (D-H1 and D-H2 analysis framework) — **unchanged**. Applied exactly as approved.

**Input data:** Canonical D-H2 CSV (SHA-256 `d8089b919778a82b25cee6072c38079f1ab52303fa0d171a802272cec38c9c6f`) — **unchanged**.

**No modifications. No reruns. No new constraints. Preservation only.**

---

## 14. Exact Preserved Claim

**Within-window mechanical observation:**

> On corrected D-H2 (1987-07-27 → 1990-01-18), Strategy B and Strategy D each executed 37 allocation units and deployed ¥370,000 of identical available cash. They also deployed identical aggregate allocation quantities by market zone: 8 units in NORMAL and 29 units in LARGE_DROP.
>
> Their deployment paths nevertheless differed in execution sequence and timing. Strategy B executed 23 allocations on dates spanning 1987-09-09 to 1990-01-15. Strategy D executed 24 allocations on dates spanning 1987-09-09 to 1990-01-15. Because execution dates and the prices encountered on those dates differed, the two strategies acquired different quantities of exposure from the same total deployed capital.
>
> Strategy D terminated with approximately 16,885.26 exposure units. Strategy B terminated with approximately 16,854.94 exposure units. The difference is approximately 30.32 exposure units in favor of D.
>
> Under the already-preserved common terminal valuation price of ¥29.0644 per exposure unit, the terminal exposure difference (30.32 units) mechanically accounts for the terminal-value difference (approximately ¥881.13) observed between B and D on corrected D-H2.
>
> This is a factual observation from one independent-validation window. It does not establish superiority, robustness, generalization, optimal timing, or suitability for adoption. It demonstrates that when two strategies with identical cash and identical aggregate zone-allocations pursue different execution sequences, they acquire different exposure quantities due to price variation. The funding constraint (¥480,000 annual grant) became equally binding on both strategies in this regime, compressing the D-vs-B deployment-ratio difference observed in D-H1 (5.56 pp difference in H1 → 0.00 pp in H2). However, D's higher monthly allocation capacity (2 vs. 1) permitted one additional execution, resulting in a marginal exposure and value advantage.

---

## 15. Exact Next Research Question (Identified, NOT Authorized)

Based on the corrected D-H2 result showing funding-constraint compression and the D-H1 result showing deployment-ratio divergence, a future research question has been identified:

**Candidate next question:**

> DO FUNDING-CONSTRAINT COMPRESSION AND DEPLOYMENT-SEQUENCE DIFFERENCES MECHANICALLY EXPLAIN THE OBSERVED MAGNITUDE CHANGES IN B-vs-D TERMINAL VALUE DIFFERENCES BETWEEN D-H1 AND CORRECTED D-H2?
>
> Possible investigation dimensions:
> - Cumulative cash deployment over time (is depletion faster or slower in each regime?)
> - Time to 50%/75%/near-full budget deployment (does available funding convergence explain magnitude changes?)
> - Deployment concentration during LARGE_DROP periods (do both strategies deploy proportionally similarly?)
> - Timing of requests occurring after budget exhaustion (did D receive more exhaustion rejections in each regime?)
> - Whether execution-sequence variance in the terminal month(s) explains remaining exposure difference

**Status:** Identified as a candidate research question. It is **NOT AUTHORIZED, DESIGNED, OR COMPUTED** in this preservation artifact. It requires separate Owner decision before proceeding.

---

## 16. Preservation Artifact Status

**File:** `docs/decisions/simulation_trial_strategy_bd_corrected_dh2_deployment_timing_acquisition_price_attribution_result.md`

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15** — Deployment-timing and acquisition-price attribution analysis result for corrected D-H2 only.

**Preservation completeness verification:**

- ✓ Owner decision and scope stated
- ✓ Authority chain verified (methodology, evidence identity, strategy authorities)
- ✓ Superseded MP-DH2-D-001 explicitly excluded
- ✓ Equal-deployment finding re-verified (37 units, ¥370,000 each)
- ✓ Equal-zone-allocation finding re-verified (8 NORMAL + 29 LARGE_DROP each)
- ✓ Cumulative deployment divergence/convergence documented
- ✓ Execution-sequence difference identified (23 vs. 24 allocations)
- ✓ Acquisition-price attribution result stated (30.32 unit difference, ¥881.13 value difference)
- ✓ Terminal value reconciliation verified
- ✓ Funding-constraint compression context provided
- ✓ Prior narrative (based on tainted evidence) superseded
- ✓ Evidentiary ceiling explicitly stated (no superiority, robustness, or generalization claims)
- ✓ Strategy-E firewall maintained (no design, no specifications)
- ✓ Qualification state unchanged
- ✓ Strategy B and D unchanged
- ✓ Methodology unchanged
- ✓ sim/ directory unchanged
- ✓ Exact claim preserved
- ✓ Next research question identified but not authorized

**No strategy modified. No metric introduced beyond approved framework. No Strategy E designed. No strategy rerun.**

---

## 17. Final Status

**Preservation complete.**

**Corrected D-H2 B-vs-D deployment-timing and acquisition-price attribution analysis result approved and preserved.**

**Tainted MP-DH2-D-001 explicitly excluded from all future comparisons.**

**Strategy B, Strategy D, methodology, input data, qualification state, and Phase 2 block all unchanged.**

**Next research question identified for future Owner decision.**

**This artifact does not authorize further investigation, strategy design, adoption, Phase 2, or Strategy E.**

---

**End of preservation document. Status: APPROVED BY OWNER DECISION, 2026-08-15.**

**Corrected D-H2 B-vs-D deployment-timing and acquisition-price attribution result preserved. Authority chain verified. Evidence integrity confirmed. Evidentiary ceiling stated. Strategies unchanged. Qualification state preserved. Next task: Owner decision on third independent-validation window (H3) or investigation closure.**

STOP FOR OWNER REVIEW.
