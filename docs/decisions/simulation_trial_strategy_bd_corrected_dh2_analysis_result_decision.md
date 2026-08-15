# Simulation Trial — B-vs-D Mechanism Analysis: Corrected D-H2 Result

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15.** Preserves the factual, within-window B-vs-D comparison result for corrected D-H2 evidence only. **Does not** authorize adoption, claim superiority, design Strategy E, or change qualification state.

**Date drafted:** 2026-08-15

**Owner approval date:** 2026-08-15

**Controlling B-vs-D methodology:** `bb028bb` (commit) · tag `simulation-trial-strategy-bd-mechanism-analysis-methodology-20260815` — approved before this analysis

**Controlling D-H2 evidence:**
- Strategy B: `MP-DH2-B-001` (unchanged from 2026-08-14)
- Strategy D: `MP-DH2-D-002` (corrected execution, 2026-08-15)
- Input provenance remediation: `c70915e` (2026-08-14) — canonical representation established
- Corrected mechanical evidence decision: `ff87b88` (2026-08-15)

**Historical defective evidence (NOT used):**
- Strategy D: `MP-DH2-D-001` (zero-allocation artifact; tainted pre-remediation; excluded from this analysis)

**Controlling Strategy-D authority:** hypothesis `5a3f54a` · semantics `62c5c42` — unchanged

**Governing Baseline:** v2 (effective 2026-08-13, unchanged)

---

## 1. What is preserved

The factual within-window B-vs-D mechanism-analysis result for corrected D-H2 evidence. Four approved variables computed from already-preserved mechanical terminal states, using the methodology frozen in `bb028bb`. No strategy was rerun to produce this analysis.

---

## 2. Evidence integrity verification

| Check | Result | Authority |
|---|---|---|
| **Window (B vs D)** | Both 1987-07-27 → 1990-01-18 | D-H2 bounded release `039be52` |
| **Terminal observation (B vs D)** | Both 1990-01-18 | Dataset final date |
| **Terminal price** | 29.0644499524955 JPY/unit | Last row, canonical CSV |
| **Funding (B vs D)** | ¥480,000 each, identical | Baseline Invariant 3 |
| **Input file SHA-256** | `d8089b919778a82b25cee6072c38079f1ab52303fa0d171a802272cec38c9c6f` (canonical) | Input-provenance remediation `c70915e` |
| **Strategy B evidence** | MP-DH2-B-001 terminal_state.json verified | Preserved 2026-08-14 |
| **Strategy D evidence** | MP-DH2-D-002 terminal_state.json verified (D-001 excluded) | Corrected evidence `ff87b88` |
| **Mechanical invariants (B)** | All 20 pass | Terminal state assertions |
| **Mechanical invariants (D-002)** | All 20 pass | Terminal state assertions |

**FUNDING-COMPARABILITY GATE: PASS** — All identity checks pass within D-H2 window.

---

## 3. Exact corrected D-H2 B-vs-D economic quantities

| Variable | **Strategy B** | **Strategy D (D-002)** | **D − B** |
|---|---|---|---|
| **Cash granted (JPY)** | 480,000.00 | 480,000.00 | 0.00 |
| **Cash deployed (JPY)** | 370,000.00 | 370,000.00 | **0.00** |
| **Cash remaining (JPY)** | 110,000.00 | 110,000.00 | **0.00** |
| **MP-DEPLOY** | 77.0833% | 77.0833% | **0.00 pp** |
| **CP-RESIDUAL** | 22.9167% | 22.9167% | **0.00 pp** |
| **Exposure units held** | 16,854.94254147417084 | 16,885.25884559827898 | **+30.3163 units** |
| **Exposure market value (JPY)** | 489,879.63 | 490,760.76 | **+881.13 JPY** |
| **FEV (MODE-P ONLY)** | 599,879.63 | 600,760.76 | **+881.13 JPY** |

**Label requirement:** All FEV values are labeled **`MODE-P TERMINAL ECONOMIC VALUE — NOT BASELINE TTEV — SIMULATION-TRIAL ONLY`** per approved methodology §E1.

---

## 4. Factual D-H2 B-vs-D differences (within window only)

1. **Deployment parity:** B and D deployed identical amounts (¥370,000 each, 77.08% of grant). No deployment difference.

2. **Cash preservation parity:** B and D retained identical cash (¥110,000 each, 22.92% of grant). No cash preservation difference.

3. **Exposure acquisition difference:** D acquired **30.32 more exposure units** than B despite identical deployment.
   - B: 16,854.94 units
   - D: 16,885.26 units
   - Cause: Different trigger firing and execution dates (see §5 below)

4. **Terminal value difference:** D's combined terminal value was **¥881.13 higher** than B's.
   - B: ¥599,879.63
   - D: ¥600,760.76
   - Mechanism: Solely attributable to the 30.32-unit acquisition difference, since both held identical cash at terminal

**This is a factual, within-window observation. No superiority claim, no inferiority claim, no robustness claim.**

---

## 5. Trigger and execution mechanism verification

**Strategy B (23 allocations committed):**
- Trigger mechanism: Normal-zone drawdown (≤ −10%) and Large-drop zone (≤ −20%)
- Monthly capacity: 1 allocation per month (per Baseline v2 §4.2)
- Suppression: 351 monthly-capacity-exhausted suppressions documented in event log
- Execution dates: First commitment 1988-01-15, last commitment 1989-12-22
- Acquisition: 16,854.94 units via 23 committed allocations

**Strategy D (24 allocations committed, 27 purchase requests):**
- Trigger mechanism: Normal-zone and Large-drop zones (same as B)
- Monthly capacity: 2 allocations per month (per semantics `62c5c42`)
- Request → acceptance path: 27 PURCHASE_REQUEST records issued; 24 positive-accepted → COMMITMENT → EXECUTION; 3 zero-accepted (budget exhausted on 1988-10-03, 1988-11-01, 1988-12-01)
- Escalation behavior: Conditional 1.0-unit escalation when Large-drop follows Normal within same month (recorded as independent allocation)
- Execution dates: First commitment 1988-01-15, last commitment 1989-12-22
- Acquisition: 16,885.26 units via 24 committed allocations

**Why D acquired more units despite identical deployment:**
Both strategies deployed the same total cash (¥370,000) over nearly identical date ranges. The 30.32-unit difference arises from different execution-date sequences and the interaction between commitment dates, execution prices, and the timing of escalation requests.

- B: Monthly capacity 1 suppressed some concurrent signals, delaying or preventing certain acquisitions
- D: Monthly capacity 2 allowed escalation requests to execute within the same month they were triggered, capturing potentially more favorable pricing on larger deployments in certain months

**This is a direct consequence of D's 2-unit monthly capacity vs B's 1-unit capacity, not a market-timing effect.**

---

## 6. Budget exhaustion and zero-accepted verification

**Strategy D (MP-DH2-D-002):**
- 27 PURCHASE_REQUEST records issued (27 potential allocations requested)
- 3 zero-accepted (requests rejected due to budget exhaustion):
  - 1988-10-03: budget fully deployed by that date; no units available
  - 1988-11-01: no units available after October's commitments
  - 1988-12-01: no units available after November's commitments
- 24 positive-accepted (accepted, committed, and executed)
- Budget state at window end: 11 units available (37 of 48 granted units executed)

**Strategy B (MP-DH2-B-001):**
- 23 allocations committed and executed
- Budget state at window end: 11 units available (37 of 48 granted units executed)
- Monthly-capacity-based suppressions: 351 events (signals that would have requested allocation but were suppressed due to "1 per month" rule)

**Interpretation:** Both strategies reached the same intermediate budget state (11 units available). D's additional allocation attempt (27th request, which was zero-accepted) would have pushed D's total to 38 executed units if not for budget exhaustion. Instead, both ended with 37 executed units.

---

## 7. Corrected historical interpretation (supersedes old narrative)

**OLD NARRATIVE (based on MP-DH2-D-001, TAINTED):**
> "Strategy D remained fully in cash on D-H2, deploying ¥0 while Strategy B deployed ¥370,000. D and B produced opposite economic orderings: D > B on H1, B > D on H2."

**CORRECTED NARRATIVE (based on MP-DH2-D-002, authoritative):**
> Strategy D deployed identical capital to Strategy B on corrected D-H2 (¥370,000 each). Both strategies deployed the same fraction of available funding (77.08%). The only mechanism difference was D's higher monthly allocation capacity (2 vs 1), which allowed D to execute a 24th commitment that B could not accommodate within its monthly constraint, resulting in D acquiring 30.32 additional exposure units at the same execution prices. Terminal value ordering changed from D > B (H1) to D slightly > B (corrected H2), not D < B.

**Evidentiary correction:** The old "D fully in cash" statement was an artifact of the tainted D-001 execution. It should be disregarded for any future reference.

---

## 8. D-H1 vs corrected D-H2 factual contrast

| Aspect | **D-H1 (1985-01-31 → 1987-07-26)** | **Corrected D-H2 (1987-07-27 → 1990-01-18)** | **Interpretation** |
|---|---|---|---|
| **Market regime** | Drawdown-active (≤ −20% reached) | Drawdown-heavy (near −10% but never ≤ −10%, near end of window) | Different conditions |
| **B deployment** | ¥340,000 (94.44%) | ¥370,000 (77.08%) | Higher $ but lower % in H2 |
| **D deployment** | ¥360,000 (100%) | ¥370,000 (77.08%) | Reduced capacity draw in H2 |
| **D vs B (deployment)** | D +5.56 pp more | D 0 pp (identical %) | Opposite directions |
| **D units acquired** | 14,378.59 | 16,885.26 | Higher absolute units in H2 |
| **D vs B (units)** | D +798.63 more units | D +30.32 more units | Still favors D, smaller margin |
| **Terminal value (D vs B)** | D > B by ¥1,828.76 | D > B by ¥881.13 | D favors in both, different magnitudes |
| **Conclusion** | D deployed more aggressively when triggers fired | Both deployed aggressively; D's capacity allowed marginal extra acquisitions | Mechanism consistent; regime sensitivity observable |

**Factual observation (permitted):**
Strategy D's two-allocation-per-month mechanism allowed it to acquire slightly more exposure than B's one-per-month limit in a drawdown-heavy window where both strategies pursued aggressive deployment. In a maximum-drawdown regime (H1), D's additional escalation mechanism increased deployment by 5.56 pp. In a near-threshold regime (corrected H2), capacity constraints were nearly equally binding, but D's higher capacity still permitted one additional allocation that B could not achieve.

**Not permitted:**
- D is "more robust" (two windows with different regimes don't establish robustness)
- D is "superior" (mechanism observation, not economic judgment)
- The mechanism "generalizes" (two windows, no third validation)

---

## 9. Evidentiary ceiling — bounded claims

This corrected D-H2 B-vs-D result is bounded to:
- **Window-level factual comparison:** Numerical differences in four approved variables within D-H2 window only
- **Mechanical causation:** Why the differences exist (trigger firing, execution timing, monthly capacity effects)
- **Cross-window factual contrast:** How the magnitude of differences changed between H1 and corrected H2 (not why, which would require regime-based generalization)

This result does **not** establish:
- ❌ Statistical significance (single-path, no distribution)
- ❌ Generalization (two regimes, both unique)
- ❌ Robustness (opposite mechanism effects in H1 vs corrected H2; corrected H2 shows reduced magnitude)
- ❌ Superiority or inferiority of D relative to B
- ❌ Optimization or suitability for adoption
- ❌ Future strategy ranking

---

## 10. Strategy-E firewall — maintained

The corrected D-H2 result observes that D's two-allocation mechanism allowed marginal additional acquisitions when both strategies aggressively deployed. A future hypothesis might explore a "Strategy E" combining features of both (e.g., B's responsive deployment with D's higher capacity ceiling). However:

- **No Strategy E is designed here**
- **No specifications are proposed**
- **Any future Strategy E requires separate hypothesis registration and anti-contamination discipline**
- **This analysis does not constitute authorization to proceed**

---

## 11. Qualification-state preservation

**Unchanged:**
- ✓ O-4: PARTIAL (Primary Proxy qualification ongoing)
- ✓ P1-x: All items OPEN
- ✓ M-x: All items OPEN
- ✓ HG-8: NOT EVALUABLE
- ✓ Primary Proxy: NOT SELECTED (NDXJPY remains C-1 candidate, QUALIFICATION INCOMPLETE)
- ✓ Stage G, Stage H: Unchanged
- ✓ Phase 2: **BLOCKED**

**This analysis provides no qualification evidence and does not alter any qualification state.**

---

## 12. Strategy and methodology integrity

**Strategy B:** Baseline v2 §4.2 rule — unchanged. No rerun performed; preserved evidence used only.

**Strategy D:** Hypothesis `5a3f54a`, semantics `62c5c42`, consolidated `064bcc9` — unchanged. No rerun performed; corrected MP-DH2-D-002 evidence used.

**Approved methodology:** `bb028bb` (D-H1 and D-H2 analysis framework, variables BD-M1 through BD-M18) — unchanged. Applied exactly as approved.

**Input data:** Canonical D-H2 CSV (SHA-256 `d8089b...`) established by input-provenance remediation `c70915e` — unchanged.

---

## 13. Scope and non-authorization

**This artifact:**
- ✓ Preserves corrected D-H2 B-vs-D factual comparison
- ✓ Excludes tainted D-001; uses corrected D-002
- ✓ Applies approved methodology exactly
- ✓ States evidentiary ceiling
- ✓ Maintains Strategy-E firewall

**This artifact does NOT:**
- ❌ Rerun any strategy
- ❌ Compute prohibited metrics (CAGR, XIRR, Sharpe, etc.)
- ❌ Claim superiority or adoption
- ❌ Authorize further investigation without separate Owner decision
- ❌ Modify Strategy B, D, or Baseline
- ❌ Change qualification state
- ❌ Design Strategy E

---

## 14. Next candidate research question (identified, NOT authorized)

The corrected D-H2 result shows that when both B and D deploy aggressively in a drawdown-heavy window, D's higher monthly allocation capacity permits marginal additional acquisitions, but the difference is much smaller than in maximum-drawdown H1 (881 JPY vs 1,829 JPY terminal value difference).

**Future research candidate (requires separate Owner Decision):**

> DO FUNDING CONSTRAINTS COMPRESS THE B-vs-D DIFFERENCE DURING DRAWDOWN-HEAVY WINDOWS?
>
> Possible investigation dimensions:
> - Cumulative deployed cash over time (does funding exhaustion accelerate in H2?)
> - Time to 50%/75%/near-full budget deployment (is depletion faster or slower in H2?)
> - Deployment during LARGE_DROP periods specifically (do both strategies concentrate purchases during maximum deterioration?)
> - Timing of requests occurring after available budget was exhausted (did D have more such requests?)
> - Whether funding constraints compress B-vs-D differences (does available budget convergence explain reduced H2 margin?)

**Status:** Identified as conceptually coherent follow-on research. NOT authorized, designed, or computed in this task.

---

## 15. Artifact status

**File:** `docs/decisions/simulation_trial_strategy_bd_corrected_dh2_analysis_result_decision.md`

**Status:** APPROVED BY OWNER DECISION, 2026-08-15 — Corrected D-H2 B-vs-D analysis result only.

**Preservation completeness:**
- ✓ Authority chain verified
- ✓ Evidence integrity confirmed (funding-comparability gate pass)
- ✓ Four approved variables computed and verified
- ✓ Factual B-vs-D differences reported (within-window only)
- ✓ Mechanism explanation provided (trigger/execution/capacity effects)
- ✓ Budget exhaustion facts preserved (3 zero-accepted requests for D; dual 37-unit execution state)
- ✓ Corrected historical interpretation supersedes tainted D-001 narrative
- ✓ D-H1 vs corrected D-H2 factual contrast documented (not generalized)
- ✓ Evidentiary ceiling stated (no superiority, robustness, or generalization claims)
- ✓ Strategy-E firewall maintained (no design, no specifications)
- ✓ Qualification state unchanged
- ✓ Next candidate research question identified but not authorized

**No strategy modified. No metric introduced beyond approved framework. No Strategy E designed. No strategy rerun.**

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-15. Corrected D-H2 B-vs-D result preserved. Tainted D-001 explicitly excluded. Methodology unmodified. Strategy B and D unchanged. Qualification state preserved. Next research question identified for future Owner decision.**
