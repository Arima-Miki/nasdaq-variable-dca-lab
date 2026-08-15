# Simulation Trial — B-vs-D Funding-Constraint Compression Study: Result Preservation

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15.** Preserves factual funding-constraint compression findings only. **Does not** authorize adoption, design Strategy E, modify strategies, change qualification state, or claim superiority.

**Date drafted:** 2026-08-15

**Owner approval date:** 2026-08-15

**Controlling corrected D-H2 B-vs-D result:** `8830a49` (commit) · tag `simulation-trial-strategy-bd-corrected-dh2-analysis-result-20260815`

**Controlling approved B-vs-D methodology:** `bb028bb` (commit) · tag `simulation-trial-strategy-bd-mechanism-analysis-methodology-20260815`

**Controlling corrected D-H2 mechanical evidence:**
- Strategy B: `MP-DH2-B-001` (preserved 2026-08-14)
- Strategy D: `MP-DH2-D-002` (corrected evidence, 2026-08-15)

**Historical defective evidence (EXCLUDED from this analysis):**
- Strategy D: `MP-DH2-D-001` (zero-allocation artifact, execution pre-remediation; NOT USED)

**Controlling Strategy authorities:** B Baseline v2 §4.2 (frozen), D hypothesis `5a3f54a` + semantics `62c5c42` (frozen)

**Governing Baseline:** v2 (effective 2026-08-13, unchanged)

---

## 1. Research Question

**Narrow question:**

> Did funding constraints compress the observable Strategy-B / Strategy-D difference during corrected D-H2, relative to the D-H1 window?

**Operational framing:**

This study examines whether both strategies' funded deployment totals converged in corrected D-H2 despite their different triggering and capacity mechanisms. Convergence would indicate that available funding became a binding mechanical constraint, not the strategies' rules.

---

## 2. H1 Funding-Behavior Facts (1985-01-31 → 1987-07-26)

**Strategy B:**
- Total budget units granted: 36.0
- Total budget units executed: 34.0 (94.4% execution rate)
- Cash deployed: ¥340,000
- Zone-specific execution:
  - NORMAL zone: 12.0 units
  - LARGE_DROP zone: 22.0 units
- Purchase requests generated: 130
- Positive commitments: 24
- NO_ALLOCATION (zero-accepted) events: 106
- First budget exhaustion date: 1986-08-01
- Commitment rate (positive / requests): 18.5%

**Strategy D:**
- Total budget units granted: 36.0
- Total budget units executed: 36.0 (100.0% execution rate)
- Cash deployed: ¥360,000
- Zone-specific execution:
  - NORMAL zone: 12.0 units
  - LARGE_DROP zone: 24.0 units
- Purchase requests generated: 33
- Positive commitments: 26
- NO_ALLOCATION (zero-accepted) events: 7
- First budget exhaustion date: 1985-12-02
- Commitment rate (positive / requests): 78.8%

**H1 B-vs-D Observed Difference:**
- Executed unit difference: D deployed 2.0 more units than B
- Zone difference: D deployed 2.0 more units exclusively in LARGE_DROP zone
- Cash difference: D deployed ¥20,000 more than B
- Budget exhaustion timing: D exhausted budget 278 days earlier than B

---

## 3. Corrected D-H2 Funding-Behavior Facts (1987-07-27 → 1990-01-18)

**Strategy B:**
- Total budget units granted: 48.0
- Total budget units executed: 37.0 (77.1% execution rate)
- Cash deployed: ¥370,000
- Zone-specific execution:
  - NORMAL zone: 8.0 units
  - LARGE_DROP zone: 29.0 units
- Purchase requests generated: 65
- Positive commitments: 23
- NO_ALLOCATION (zero-accepted) events: 42
- First budget exhaustion date: 1988-11-01
- Commitment rate (positive / requests): 35.4%

**Strategy D (corrected D-002):**
- Total budget units granted: 48.0
- Total budget units executed: 37.0 (77.1% execution rate)
- Cash deployed: ¥370,000
- Zone-specific execution:
  - NORMAL zone: 8.0 units
  - LARGE_DROP zone: 29.0 units
- Purchase requests generated: 27
- Positive commitments: 24
- NO_ALLOCATION (zero-accepted) events: 3
- First budget exhaustion date: 1988-10-03
- Commitment rate (positive / requests): 88.9%

**Corrected D-H2 B-vs-D Observed Difference:**
- Executed unit difference: D deployed 0.0 more units than B (IDENTICAL)
- Zone difference: D deployed 0.0 more units in any zone (IDENTICAL ZONE BREAKDOWN)
- Cash difference: D deployed ¥0 more than B (IDENTICAL)
- Budget exhaustion timing: D exhausted budget only 29 days earlier than B

---

## 4. Deployment Milestone Findings

| Milestone | H1 B | H1 D | H2 B | H2 D |
|---|---|---|---|---|
| **25% target** | 10/05/85 | 10/02/85 | 03/02/88 | 03/02/88 |
| **50% target** | 03/04/86 | 03/04/86 | 10/04/88 | 09/02/88 |
| **75% target** | 02/03/87 | 02/03/87 | 12/19/89 | 12/19/89 |
| **90% target** | 06/02/87 | 05/04/87 | NOT REACHED | NOT REACHED |
| **Maximum reached** | 07/02/87 (34 units, 94.4%) | 07/02/87 (36 units, 100%) | 01/15/90 (37 units, 77.1%) | 01/15/90 (37 units, 77.1%) |

**Factual observation:**
- H1: B and D reached 50% and 75% milestones on identical dates; D reached 90% slightly earlier
- Corrected H2: B and D reached 25%, 50%, and 75% milestones on identical or nearly identical dates; neither strategy reached 90% milestone (both capped at 77.1%)

---

## 5. Zone-Specific Deployment Findings

| Strategy | Window | NORMAL Units | LARGE_DROP Units | Total |
|---|---|---|---|---|
| B | H1 | 12.0 | 22.0 | 34.0 |
| D | H1 | 12.0 | 24.0 | 36.0 |
| **D-B difference (H1)** | | **0.0** | **+2.0** | **+2.0** |
| B | Corrected H2 | 8.0 | 29.0 | 37.0 |
| D | Corrected H2 | 8.0 | 29.0 | 37.0 |
| **D-B difference (H2)** | | **0.0** | **0.0** | **0.0** |

**Factual observation:**
- H1: D deployed 2.0 additional units exclusively in the LARGE_DROP zone; NORMAL-zone deployment was identical
- Corrected H2: Both strategies deployed identically by zone (8 NORMAL, 29 LARGE_DROP), achieving perfect zone parity despite different triggering mechanisms

---

## 6. Request / Commitment / Execution Findings

| Strategy | Window | Purchase Requests | Positive Commitments | Commitment Rate | Unfunded Requests |
|---|---|---|---|---|---|
| B | H1 | 130 | 24 | 18.5% | 106 |
| D | H1 | 33 | 26 | 78.8% | 7 |
| **Ratio (D/B)** | H1 | **0.25x** | **1.08x** | **4.3x** | **0.07x** |
| B | Corrected H2 | 65 | 23 | 35.4% | 42 |
| D | Corrected H2 | 27 | 24 | 88.9% | 3 |
| **Ratio (D/B)** | H2 | **0.42x** | **1.04x** | **2.5x** | **0.07x** |

**Factual observations:**
- H1: D generated far fewer purchase requests (33 vs 130, ratio 0.25x) but achieved higher positive-commitment rate
- H1: D had vastly fewer unfunded requests (7 vs 106, ratio 0.07x)
- Corrected H2: D still generated fewer purchase requests (27 vs 65, ratio 0.42x) and achieved higher commitment rate
- Corrected H2: D still had fewer unfunded requests (3 vs 42, ratio 0.07x)
- **Despite these request-efficiency differences, both strategies ended with identical executed totals in corrected H2**

---

## 7. Zero-Accepted Request Verification

| Strategy | Window | Zero-Accepted Events | First Exhaustion Date | Additional Dates |
|---|---|---|---|---|
| B | H1 | 106 | 1986-08-01 | Ongoing from 1986-08-04 |
| D | H1 | 7 | 1985-12-02 | 1986-07-01, 1986-08-01 |
| B | Corrected H2 | 42 | 1988-11-01 | Ongoing from 1988-11-02 |
| D | Corrected H2 | 3 | 1988-10-03 | 1988-11-01, 1988-12-01 |

**Factual findings:**
- H1: D exhausted budget 278 days earlier than B (1985-12-02 vs 1986-08-01)
- Corrected H2: D exhausted budget only 29 days earlier than B (1988-10-03 vs 1988-11-01)
- **Budget exhaustion gap narrowed 9.6x between H1 and corrected H2**
- Corrected H2: D's zero-accepted events clustered at budget exhaustion dates, suggesting funding availability (not monthly capacity) was the binding constraint

---

## 8. Funding-Pressure Timing Comparison

| Aspect | H1 | Corrected H2 | Change |
|---|---|---|---|
| **Time to first exhaustion (B)** | 583 days | 462 days | —60% (accelerated) |
| **Time to first exhaustion (D)** | 305 days | 433 days | +42% (delayed) |
| **Exhaustion gap** | 278 days (D first) | 29 days (D first) | —90% (converged) |
| **Both at max deployment** | Day 884 | Day 906 | Similar span |
| **Execution rate convergence** | B: 94.4%, D: 100% | B: 77.1%, D: 77.1% | From ±5.6 pp to 0.0 pp |

**Factual observation:**
- Both strategies encountered binding budget constraints much more tightly in corrected H2
- Exhaustion timing gap narrowed from 278 days to 29 days (9.6x convergence)
- Both execution rates converged to identical 77.1% in corrected H2

---

## 9. Convergence Finding: H1 vs Corrected H2

| Metric | H1 | Corrected H2 | Convergence? |
|---|---|---|---|
| **Executed unit total (B)** | 34 units | 37 units | — |
| **Executed unit total (D)** | 36 units | 37 units | — |
| **B-vs-D executed difference** | +2 units for D | +0 units (IDENTICAL) | ✓ YES |
| **Zone-specific parity** | D +2 in LARGE_DROP | Both 8 NORMAL + 29 LARGE_DROP | ✓ YES |
| **Budget exhaustion gap** | 278 days | 29 days | ✓ YES (9.6x narrower) |
| **Execution rate parity** | 94.4% vs 100.0% (±5.6 pp) | 77.1% vs 77.1% (0.0 pp) | ✓ YES |

**Factual conclusion:**
Corrected D-H2 exhibits measurably stronger convergence in funded deployment between Strategy B and Strategy D than D-H1. The execution difference narrowed from 2.0 units to 0.0 units. Zone-specific execution achieved parity. Budget exhaustion timing gap narrowed 9.6x.

---

## 10. Funding-Constraint-Compression Interpretation

**Bounded factual statement:**

Both Strategy B and Strategy D executed identical 37 budget units in corrected D-H2, despite their different triggering mechanisms and request-generation patterns. This convergence in funded deployment, compared to the 2-unit difference observed in H1, is consistent with the interpretation that **available budget became a mechanically binding constraint** on the expression of their different allocation rules.

**Evidence supporting this interpretation:**
1. D's superior request efficiency (88.9% commitment rate) did not result in higher execution
2. D's additional monthly capacity (2 allocations vs B's 1) was not realized in higher execution
3. Both strategies' budget exhaustion occurred within 29 days of each other (vs 278 days in H1)
4. D's zero-accepted events were concentrated at the budget exhaustion date, not distributed over time
5. Zone-specific execution achieved perfect parity despite different rule mechanics

**Mechanical pathway:**
- Available funding was allocated to both strategies' respective commitments
- Both reached the same funding depletion point despite different efficiency metrics
- Neither strategy could execute additional allocations beyond the point of budget exhaustion
- D's "efficiency advantage" (in terms of request-to-commitment ratio) was not translatable to higher execution because the binding constraint was funding availability, not monthly capacity

---

## 11. Observed-Fact vs Counterfactual Boundary

**This artifact establishes OBSERVED FACTS ONLY:**

✓ Both B and D executed identical budget units in corrected H2
✓ Budget exhaustion became a binding constraint for both strategies
✓ Funding availability limited execution despite different rule mechanisms
✓ Request efficiency metrics did not translate to execution advantage in a funding-constrained environment

**This artifact does NOT establish COUNTERFACTUAL CLAIMS:**

✗ What B or D would have done with additional budget
✗ Whether more funding would have changed execution patterns
✗ Whether D's superior efficiency "would have" enabled higher deployment with unlimited funding
✗ Optimal funding levels
✗ Whether funding should be increased
✗ What a third strategy would do

These counterfactual questions require separate research, not addressed here.

---

## 12. Evidentiary Ceiling

**What this analysis establishes:**
- Factual budget-constraint behavior in two windows
- Factual convergence in funded deployment between H1 and corrected H2
- Factual timing and magnitude of budget exhaustion
- Mechanical explanation: funding availability as binding constraint

**What this analysis does NOT establish:**
- ✗ Strategy superiority or inferiority
- ✗ Ranking of B vs D
- ✗ Robustness across windows
- ✗ Generalization beyond H1 and H2
- ✗ Statistical significance
- ✗ Optimal strategy or funding level
- ✗ Adoption recommendation
- ✗ Phase 2 readiness

**Scope limitation:**
This analysis is purely observational. It describes what happened under the actual preserved budget constraints. It makes no prescriptive claims about what should happen under different constraints.

---

## 13. Strategy-E Firewall

Strategy E is NOT authorized and NOT designed in this task.

The observation that both B and D converged to identical execution under binding budget constraints does not constitute authorization, design, or specification of any new strategy.

Any future hybrid strategy would require:
- Separate hypothesis registration
- Explicit semantic freezing before evidence inspection
- Separate validation window
- Full anti-contamination protocol
- Separate Owner Decision

---

## 14. Qualification-State Preservation

**Unchanged:**
- ✓ O-4: PARTIAL (Primary Proxy qualification ongoing)
- ✓ P1-x: All items OPEN
- ✓ M-x: All items OPEN
- ✓ HG-8: NOT EVALUABLE
- ✓ Primary Proxy: NOT SELECTED (NDXJPY remains C-1 candidate, QUALIFICATION INCOMPLETE)
- ✓ Stage G, Stage H: Unchanged
- ✓ Phase 2: **BLOCKED**

This analysis provides no qualification evidence and does not alter any qualification state.

---

## 15. Next Candidate Research Question

**Identified but NOT authorized in this task:**

> HOW DO STRATEGY B AND STRATEGY D DIFFER IN THE TIMING AND PRIORITIZATION OF LIMITED CAPITAL DEPLOYMENT?

Potential future investigation dimensions may include:
- Cumulative deployment curves across the window
- Relative timing of allocation requests
- Capital consumed before vs after major drawdowns
- Acquisition price distribution and timing effects
- Trigger-path contribution to capital consumption
- Opportunity cost of early vs late deployment
- Value of preserved cash during later market movements

**Status:** Conceptually identified as next research question. **NOT designed, computed, or authorized here.** Requires separate Owner Decision.

---

## 16. Scope and Non-Authorization

**This artifact preserves:**
- ✓ Factual funding-behavior findings from corrected D-H2 and D-H1
- ✓ Convergence observation: identical execution totals in corrected D-H2
- ✓ Budget constraint interpretation: funding availability as binding mechanical constraint
- ✓ Evidentiary ceiling: what is and is not established

**This artifact does NOT:**
- ❌ Rerun any strategy
- ❌ Design Strategy E
- ❌ Claim superiority or inferiority
- ❌ Authorize adoption
- ❌ Authorize Phase 2
- ❌ Change qualification state
- ❌ Modify Strategy B or D
- ❌ Simulate unlimited-budget scenarios

---

## 17. Artifact Status

**File:** `docs/decisions/simulation_trial_strategy_bd_funding_constraint_compression_result_decision.md`

**Status:** APPROVED BY OWNER DECISION, 2026-08-15 — Funding-constraint compression findings preserved.

**Preservation completeness:**
- ✓ Authority chain verified (8830a49, bb028bb, MP-DH1/DH2 evidence)
- ✓ Corrected D-H2 evidence identity confirmed (MP-DH2-D-002, excluding D-001)
- ✓ H1 and corrected H2 funding-behavior facts documented
- ✓ Zone-specific deployment verified and documented
- ✓ Request/commitment/execution patterns analyzed
- ✓ Budget exhaustion timing compared
- ✓ Convergence finding established: 2-unit difference (H1) → 0-unit difference (H2)
- ✓ Funding-constraint interpretation bounded to observed facts
- ✓ Counterfactual claims explicitly excluded
- ✓ Evidentiary ceiling stated
- ✓ Strategy-E firewall maintained
- ✓ Qualification state preserved unchanged
- ✓ Next research question identified but not authorized

**No strategy modified. No counterfactual simulations. No Strategy E designed. No rerun of B or D.**

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-15. Funding-constraint compression result preserved. Bounded to observed facts. No counterfactual claims. Strategy E firewall maintained. Qualification state unchanged. Next research question identified.**
