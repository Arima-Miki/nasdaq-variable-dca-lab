# Simulation Trial — Strategy D: Post-D-H2 Consolidation Checkpoint

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15.** Consolidation checkpoint only. Preserves Strategy D as the fixed reference for subsequent comparative research. **Does not** adopt Strategy D, promote it to Baseline, authorize Phase 2, modify any strategy, or define metrics for future B-vs-D research.

**Date drafted:** 2026-08-14

**Owner approval date:** 2026-08-15

**Controlling Strategy-D authority:** Hypothesis `5a3f54ab11a1de8204cae659ad2732867e7d1274` · Semantics `62c5c429ce6aa4742c6327a9c39687421fd94325` (SD-1…SD-10 resolved) · Mode-E E5 `f16a815d4fc64706247e5ac63e8449857dd58643`

**Controlling D-H0/H1/H2 evidence:** D-H0 Mode-P observations (motivation source) · D-H1 mechanical checkpoint `8a76769493cd690800011e518495a34b2a3c3e8b` · D-H1 economic result `2fb87c3198997dc70ec9365f1f3a7f0b8bd5e036` · D-H2 mechanical checkpoint `023a40157a8c671c34bbb260628c1d07fff4c10f` · D-H2 economic evaluation completed 2026-08-14

**Governing Baseline:** v2 (unchanged by this artifact)

---

## 1. What is preserved

Strategy D as currently defined, fixed, and ready for reference in subsequent comparative research. This artifact records the chronology of Strategy D's observation and consolidation; it does not modify, optimize, or promote Strategy D.

---

## 2. Strategy D's fixed identity

### Registered hypothesis (5a3f54a)

Strategy D is an owner-generated post-result alternative hypothesis to Strategy B, proposed after inspection of the preserved 2018-2020 Mode-P economic comparison (`MP-EV`/`MP-EV2`, commits `00b2b4a`/`e475717`). It was motivated by Strategy B's observed accumulation of undeployed funding.

**Mechanism:** Drawdown-conditional, order-dependent, two-stage allocation rule:
- First qualifying Normal-zone observation in a month: request 1.0 unit
- Conditional escalation: if drawdown deteriorates to Large-drop zone **after** Normal acceptance, request 1.0 additional unit (new, independent allocation)
- Direct-to-Large-drop path: if month's first qualifying event is already Large-drop, request 2.0 units (single allocation)
- No month-end fallback
- Monthly capacity ceiling: 2.0 units (rule limit, not a funding grant)
- Same annual funding capacity as A/B/C (Invariant 3)

### Resolved semantics (62c5c42 — SD-1 through SD-6)

| Open Item | Resolution | Authority |
|---|---|---|
| **SD-1** | Direct-to-Large-drop behavior | Symmetric: 2.0 units in single allocation | §2 |
| **SD-2** | Repeated Normal signals | After first Normal-triggered allocation, no additional allocation same month | §4 |
| **SD-3** | Accounting for escalation top-up | New, independent allocation; draws from shared monthly capacity | §3 |
| **SD-5** | Zero-unit acceptance | No allocation, no commitment, no reservation; capacity not consumed | §5 |
| **SD-6** | Month-end fallback | None exists (unlike Strategy C); pure drawdown trigger only | §7 |

Remaining open items (SD-4, SD-7, SD-8, SD-10) are non-blocking and derive from existing authority or edge-case interactions already covered by preserved semantics.

### Implementation status

- **NOT adopted** (remains Simulation Trial experimental variant, §18.4.5)
- **NOT Baseline** (Baseline v2 is frozen; Strategy D is alternative)
- **NOT in production**
- **Implementation-ready** (all blocking semantics resolved)
- **Never pre-registered** (post-result hypothesis; §18.4.7 anti-contamination binding)

---

## 3. Chronology — binding, permanent record

### Stage D-H0: 2018-01-02 → 2020-06-26 (hypothesis-generating window)

- Strategies A, B, C executed mechanically (MP-H1/MP-H2, commit `da85b66`)
- Economic comparison computed under Mode-P terminal-valuation authority (`MP-EV`/`MP-EV2`, commits `00b2b4a`/`e475717`)
- **Result: Strategy B retained materially more undeployed cash than A/C over this specific window**
- **This result motivated Strategy D's hypothesis** (§7 below)
- D-H0 is **hypothesis-generating data**, not independent evidence; cannot be cited as validation

### Stage D-H1: 1985-01-31 → 1987-07-26 (first independent validation)

- Input deterministically selected (policy `f8332a543f7bab4c8b5f42974813ccd70be9137f`, rule `f025bbf0dd5df9a4b037936822b1ced4e263948c`) before D execution
- Bounded released (`b722fb27ada370cf1adf22f6a8e5a99331a9a705`)
- Strategy D executed deterministically (MP-DH1-D-001, checkpoint `8a76769493cd690800011e518495a34b2a3c3e8b`)
- **Mechanical result:** 26 allocations; ¥360,000 deployed; 14,378.59 exposure units acquired
- All invariants passed; determinism verified (two independent runs)
- **Economic result (authorized economic methodology `f0f60fa`):** Combined terminal value ¥393,007.35; rank **1st** (D > B > A > C)

### Stage D-H2: 1987-07-27 → 1990-01-18 (second independent validation)

- Input deterministically selected (same selection rule) before D execution
- Bounded released (`039be52d29e3e25b9c8264c3d2a0e59ac012b666`)
- Input provenance remediation (`c70915e141ea53996dffb4ea9c809eefde25bd3d`) applied
- Strategy D executed deterministically (MP-DH2-D-001, checkpoint `023a40157a8c671c34bbb260628c1d07fff4c10f`)
- **Mechanical result:** 0 allocations; ¥0 deployed; 0 exposure units acquired (natural zero-allocation path — drawdown thresholds never reached)
- All invariants passed; determinism verified (two independent runs)
- **Economic result (same authorized methodology `f0f60fa`):** Combined terminal value ¥480,000.00; rank **4th** (B > C > A > D)

**Chronological binding:** This sequence — D-H0 observation, D hypothesis, D-H1 execution, D-H2 execution — is permanent. No retroactive reordering or relabelling as pre-registered.

---

## 4. Factual H1 vs H2 contrast — what it demonstrates

### Market environment difference

| Window | Max drawdown reached | Normal zone observations | Large-drop zone observations | Market condition class |
|---|---|---|---|---|
| **D-H1** | Yes (≤ −20%) | Yes | Yes | **Drawdown-active** |
| **D-H2** | No (max dd > −10%) | No | No | **Drawdown-absent** |

### Strategy D's response

Strategy D is a conditional, drawdown-triggered rule with no mechanism to force deployment when markets remain stable:

| Aspect | D-H1 | D-H2 | Interpretation |
|---|---|---|---|
| **Trigger fire** | Yes (zones occur) | No (zones don't occur) | **Working as designed** |
| **Allocations** | 26 committed | 0 committed | **Conditional execution** |
| **Cash deployed** | ¥360,000 | ¥0 | **No fallback; no forced deployment** |
| **Terminal value** | ¥393,007 | ¥480,000 | **Outcome depends on market regime** |
| **Rank vs B** | **First** (D > B) | **Last** (D < B) | **Opposite economic directions** |

### What this demonstrates

1. **Strategy D is not market-adaptive.** It does not increase deployment in rising markets to compensate for cash accumulation. It waits for drawdown zones only.

2. **Strategy D is purely reactive to defined zones.** When triggers fire, deployment happens (D-H1). When triggers don't fire, no deployment happens (D-H2). Both outcomes are mechanical, neither is an error.

3. **The two windows show Strategy D's response to two different market regimes:**
   - High-drawdown regime (D-H1): mechanism fires, staged deployment occurs
   - No-drawdown regime (D-H2): mechanism doesn't fire, remains in cash

4. **Strategy D's design question is explicitly about allocation staging and timing** (Normal-first → then escalate conditionally), **not about adapting to all market conditions.** The staged approach works when conditions deteriorate; no deployment occurs when deterioration never happens.

---

## 5. Evidentiary ceiling — what is NOT claimed

This consolidation checkpoint does **not** state, imply, or authorize:

- Strategy D is superior to A, B, or C
- Strategy D is inferior to A, B, or C
- Strategy D's mechanism is robust
- Strategy D's behavior generalizes beyond these windows
- Strategy D is statistically validated
- Strategy D should replace Strategy B
- Strategy D is optimal, more efficient, or preferable
- Strategy D should be adopted as Baseline
- Strategy D should advance to Phase 2
- The D-H1 favorable result establishes anything other than a factual outcome on one window
- The D-H2 unfavorable result indicates malfunction or weakness — only that triggers didn't fire

---

## 6. Strategy-D freeze statement

> Strategy D, as currently defined by its registered hypothesis (5a3f54a), resolved semantics (62c5c42), and preserved implementation, is hereby frozen as the reference Strategy-D version for subsequent comparative research.
>
> This is a **research-version freeze only**. It establishes a stable, unambiguous point of reference.
>
> This freeze is **NOT**:
> - adoption;
> - Baseline promotion;
> - production approval;
> - qualification-state promotion;
> - Phase-2 authorization;
> - any change to existing governance or classification.

---

## 7. Anti-contamination chronology and boundary — binding, non-negotiable

**Chronological sequence (permanent):**

1. Strategies A, B, C existed and were observed (Mode-P 2018-2020, MP-H1/H2/EV)
2. Strategy D was hypothesized based on observed B behavior
3. D-H0 remains the hypothesis-generating / motivation window (cannot be cited as independent evidence)
4. D-H1 was independently selected and executed
5. D-H2 was independently selected and executed
6. Strategy D is now consolidated (this checkpoint)
7. Future B-vs-D mechanism research may be authorized (separate task, separate decision)
8. Only after B-vs-D research, if authorized separately, any new Strategy-E hypothesis

**Non-negotiable prohibitions:**

- ❌ Do **NOT** use D-H1/D-H2 results to silently modify Strategy D's rule
- ❌ Do **NOT** rerun D with modified semantics and claim the original result still applies
- ❌ Do **NOT** combine properties of B and D into an undocumented hybrid — any such rule is a new versioned hypothesis (e.g., Strategy E), not a mutation of D
- ❌ Do **NOT** promote D's D-H1 favorable result as adoption-ready without simultaneously disclosing D-H2's opposite result
- ❌ Do **NOT** cite D-H0 as independent validation
- ❌ Do **NOT** alter Strategy D as a consequence of this consolidation

**Permitted chain:**

- ✓ Observe that D-H1 and D-H2 produced different outcomes
- ✓ Analyze why (market conditions differed; triggers occurred vs. didn't occur)
- ✓ Note that D's mechanism is purely conditional on drawdown zones
- ✓ Study the trade-offs between B's continuous deployment and D's conditional deployment
- ✓ Propose a new Strategy-E hypothesis that might address both window types
- ✓ Register Strategy-E explicitly as a SEPARATE rule, not D modification
- ✓ Subject Strategy-E to the same anti-contamination discipline

**Future qualification artifacts:** Any future artifact addressing O-4, P1-x, Primary Proxy, Stage G, Stage H, or Phase 2 **MUST restate** that D-H0 was hypothesis-generating, D-H1 and D-H2 were independent validation windows, both windows' results were known at artifact-draft time, and no hidden hindsight contamination occurred.

---

## 8. Future research variables — concept identified, formal definition deferred

The following four variables are identified as candidates for the future B-vs-D Mechanism Analysis. Their **concepts** are understood from existing mechanical and economic data. Their **formal definitions** for comparative research purposes are **NOT defined here** and are **DEFERRED** to the future B-vs-D Mechanism Analysis methodology task.

| Variable | Data Source | Concept | Formal Definition Status |
|---|---|---|---|
| **Acquired exposure units** | Preserved mechanical states (terminal_state.json, `exposure_units_held`) | Total index units acquired by each strategy at window end | **EXISTING** (direct mechanical output; no derivation needed) |
| **Final economic value** | Authorized economic-evaluation methodology (f0f60fa, results from 2fb87c3 and 2026-08-14 eval) | Combined terminal value (exposure market value + unconverted cash) | **EXISTING** (computed under pre-authorized methodology; available per economic-evaluation boundaries) |
| **Market participation rate** | Proposed derivation from `exposure_units_held > 0` across observations | Fraction of window in which strategy held active exposure | **CONCEPT IDENTIFIED** — FORMAL DEFINITION DEFERRED to B-vs-D methodology task |
| **Cash preservation rate** | Proposed derivation from `residual_cash_ratio` or `total_unconverted_cash_jpy / cash_granted_jpy` | Fraction of grant remaining unconverted at window end | **CONCEPT IDENTIFIED** — FORMAL DEFINITION DEFERRED to B-vs-D methodology task |

**Do not compute, define, or finalize metrics for the deferred variables in this artifact or any derivative of it.** Their formal definitions, including exact numerator/denominator specifications, temporal interpretation, comparison semantics, and use in conclusions, belong to the future B-vs-D methodology task, which will freeze those definitions before any analysis begins.

---

## 9. Qualification state — completely unchanged

**No change to any of the following:**

- **O-4:** Proxy evaluation — PARTIAL (three released C-1 candidates; unchanged)
- **P1-1…P1-7:** Terminal valuation, cost model, FX, return composition — all OPEN (unchanged)
- **M-1…M-8:** Economic metrics, time-weighting, risk adjustment, statistical significance — all OPEN (unchanged)
- **HG-8:** Hedge-ratio estimation — NOT EVALUABLE (unchanged)
- **Primary Proxy:** NOT SELECTED (unchanged)
- **Stage G:** OPEN (unchanged)
- **Stage H:** NOT BEGUN (unchanged)
- **Phase 2:** **BLOCKED** (unchanged)

**Strategy D within qualification framework:**

- Strategy D remains **OWNER-GENERATED POST-RESULT ALTERNATIVE HYPOTHESIS, NON-BASELINE, NON-ADOPTED**
- D-H1 and D-H2 results are **NOT** qualification evidence and **CANNOT** be promoted into qualification lanes
- No change to qualification criteria or evidence requirements
- No future D-based decision (adoption, Phase 2 advancement, etc.) is authorized by this consolidation

---

## 10. Scope of this consolidation

This artifact:

- ✓ Preserves Strategy D's identity and semantics exactly as frozen
- ✓ Records the chronology of D-H0/H1/H2 observation and consolidation
- ✓ Documents the H1 vs H2 factual contrast mechanically
- ✓ Identifies four research variables for future B-vs-D work (concepts only, not formal definitions)
- ✓ Establishes the freeze checkpoint statement
- ✓ Reaffirms anti-contamination boundaries
- ✓ Confirms qualification-state preservation

This artifact does **not**:

- ❌ Modify Strategy D's rule or implementation
- ❌ Design or propose Strategy E
- ❌ Formally define B-vs-D research metrics
- ❌ Begin B-vs-D mechanism analysis
- ❌ Change any qualification state
- ❌ Authorize Phase 2 or any adoption decision
- ❌ Claim robustness, superiority, generalization, or statistical validation
- ❌ Promote D-H0 as independent evidence
- ❌ Make any economic claim beyond acknowledging pre-authorized results

---

## 11. Next task — identified but NOT begun

**Next task to be designed (not authorized or begun by this checkpoint):**

**"B-vs-D Mechanism Analysis Methodology Design"**

Scope:
- Define, formally and with pre-result frozen definitions, the four research variables:
  - market participation rate (formal definition with numerator, denominator, temporal semantics)
  - cash preservation rate (formal definition with numerator, denominator, temporal semantics)
  - acquired exposure units (verification of existing mechanical quantity; clarify scope of comparison)
  - final economic value (clarify which economic-evaluation boundaries apply; specify which results are permissible for comparison)
- Specify permitted comparison forms (pairwise differences, ratios, temporal patterns, etc.)
- Establish claims ceiling for B-vs-D comparison results
- Pre-freeze all analysis procedures before any comparison result is computed

**This task is NOT authorized by this consolidation checkpoint.** It requires a separate, future Owner Decision.

---

## 12. Scope

This artifact preserves Strategy D as the fixed research-version reference only. It does not modify any existing decision, Baseline, strategy implementation, qualification state, or evidence. It does not authorize any future task, only identifies it and defers it to a separate, future decision.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-15. Consolidation checkpoint only. Strategy D fixed as reference for future comparative research. No adoption, no Phase 2 authorization, no strategy modification, no metric definition, no qualification change. 5a3f54a, 62c5c42, 8a76769, 023a401, f0f60fa, 2fb87c3, and all preserved D-H0/H1/H2 evidence remain unchanged.**
