# B-vs-D Mechanism Analysis Methodology

**Status:** APPROVED BY OWNER DECISION, 2026-08-15 — METHODOLOGY ONLY.

**Date drafted:** 2026-08-15

**Owner approval date:** 2026-08-15

**Approval scope:** This approval freezes the B-vs-D comparison methodology before result analysis. It approves BD-M1 through BD-M18 as reviewed. This approval does not compute or authorize reinterpretation of B-vs-D results; does not execute or modify Strategy B; does not execute or modify Strategy D; does not design Strategy E; does not change qualification state; does not authorize Phase 2.

**Authority basis:** Post-D-H2 Consolidation Checkpoint (commit 064bcc9) · Strategy D hypothesis (5a3f54a) · Strategy D semantics (62c5c42) · D-H1 mechanical result (8a76769) · D-H2 mechanical result (023a401) · Mode-P terminal valuation decision (f0f60fa) · Baseline v2 (effective 2026-08-13)

---

## MANDATORY INITIAL STATEMENT

**This methodology design is PURELY METHODOLOGICAL.**

**This design does NOT:**
- Execute any strategy
- Compute any B-vs-D result
- Rerun H1 or H2
- Modify Strategy B
- Modify Strategy D
- Design Strategy E
- Change qualification state
- Authorize Phase 2
- Claim any superiority or inferiority

**This design does:**
- Formally define four research variables before any analysis
- Establish comparison semantics and boundaries
- Identify required preserved fields from H1/H2 evidence
- Determine whether strategy reruns are necessary
- Create a decision matrix governing future B-vs-D execution

---

## A. RESEARCH QUESTION — FORMALIZED

**Proposed wording:**

> Given identical funding schedules and the same frozen market input window, how do fixed Strategy B and fixed Strategy D trade off in terms of:
> (1) market participation rates,
> (2) cash preservation,  
> (3) acquired exposure units, and
> (4) final economic value?

**Authority basis:** Consolidation Checkpoint §8 (four variables identified); Post-result-hypothesis semantics (§18.4.5 / §18.4.7)

**Interpretation boundary:** This is a MECHANISM ANALYSIS QUESTION, not a superiority question. It asks: what different behavioral or economic trade-offs do these two fixed strategies exhibit? It does not ask: which is better?

**Status:** FROZEN BEFORE ANALYSIS BEGINS — no modification after H1/H2 results are computed.

---

## B. MARKET PARTICIPATION — FORMAL DEFINITION

**Definition adopted: MP-DEPLOY (Capital Deployment Ratio)**

$$MP_{deploy} = \frac{\text{cash deployed (committed)}}{\text{total cash granted (all years combined)}}$$

### B1. Numerator: Cash Deployed (Committed)

**Definition:** The sum of all cash amounts corresponding to allocation commitments actually accepted (post-capping, post-budget-validation) across the entire window.

**Source field:** From preserved mechanical results: sum of `allocated_cash_amount_jpy` for all rows with `allocation_status = "COMMITTED"` (or equivalent mechanical indicator across runs).

**Interpretation:** 
- Counts only cash that was formally reserved/committed, not merely requested
- Respects budget capping; if a strategy requests ¥10k but only ¥5k is available, counts ¥5k
- Includes all calendar months and budget years within the window
- Does not include executed vs. pending distinction; counting happens at commitment

**Temporal scope:** All observations within the frozen window boundary

### B2. Denominator: Total Cash Granted

**Definition:** The sum of all annual grants over the full analysis window, calculated as:

$$\text{cash granted} = \text{number of complete years in window} \times 120000 + \text{prorated first/last partial year funding}$$

**Authority basis:** Baseline v2 §11.1–11.3 (annual grant, carry-forward, zero-yield cash)

**Invariant:** Identical for Strategy B and Strategy D within the same window (Invariant 3)

### B3. Why MP-DEPLOY vs. Alternatives

| Alternative | Rejected? | Reason |
|---|---|---|
| MP-ALLOC (allocation event participation: committed events / opportunities available) | YES | "Opportunity available" requires defining what signals *could* have fired but were suppressed — implicitly model-dependent. MP-DEPLOY is more direct. |
| MP-TIME (time-in-market: observations with non-zero exposure / total observations) | NO — secondary descriptor | Adds interpretability: "how many days did the strategy hold exposure?" Retained as optional secondary. |
| MP-BINARY (whether any exposure occurred) | NO | Too coarse for understanding participation patterns over windows with different market regimes. |

**Secondary descriptor retained:** MP-TIME — percentage of observations with non-zero cumulative exposure held. Useful for understanding whether deployment was concentrated vs. distributed.

### B4. Example Calculation

**D-H1 window (1985-01-31 → 1987-07-26):**
- Window span: ~2.5 years; 3 complete years of grant within span = 3 × 120,000 = 360,000 JPY (plus prorated, if any)
- D-H1 confirmed grant: ¥360,000 (preserved in D-H1 mechanical result)
- D-H1 Strategy D deployed: ¥360,000 (confirmed in preserved mechanical result)
- **MP-DEPLOY(D, H1) = 360,000 / 360,000 = 1.0 (100%)**

**D-H1 Strategy B (preserved in economic comparison, not computed here):**
- B deployed: ¥340,000 (preserved in D-H1 economic comparison table)
- **MP-DEPLOY(B, H1) = 340,000 / 360,000 = 0.944... (~94.4%)**

**Status:** Examples illustrative only. Derived metrics have NOT yet been computed in this task.

### B5. Pathological Cases and Handling

**Case 1: Window contains zero observation days**
- Not possible (both H1 and H2 have 627+ observations)
- **Handling:** N/A

**Case 2: No grant was given (funding = zero)**
- Would make denominator = 0
- **Handling:** FAIL CLOSED — do not attempt comparison if funding_granted_jpy = 0 for either strategy

**Case 3: Strategy requests zero in every month (natural zero-allocation path)**
- Deployed = 0; MP-DEPLOY = 0 / (granted) = 0
- This is NOT an error; it is a valid outcome (D-H2 demonstrates this)
- **Handling:** Report as 0% with explicit note: "zero allocations in this window"

---

## C. CASH PRESERVATION — FORMAL DEFINITION

**Definition adopted: CP-RESIDUAL (Terminal Undeployed-Cash Ratio)**

$$CP_{residual} = \frac{\text{terminal unconverted cash}}{\text{total cash granted}}$$

### C1. Numerator: Terminal Unconverted Cash

**Definition:** The total cash amount that was never converted into acquired exposure by the window-end observation.

**Explicit sub-components (disclosed separately):**
1. **Available cash:** cash not yet reserved or committed (may be zero)
2. **Reserved-but-unexecuted cash:** cash that was committed as an allocation but execution never occurred within the window (distinct category per Mode-P decision MP-EV-D2)

**Source field:** From preserved mechanical/economic results: `cash_available_jpy + cash_reserved_unexecuted_jpy` = total unconverted cash at terminal state.

**Authority basis:** Mode-P decision MP-EV-D2 (reserved-but-unexecuted must be separately disclosed); Baseline v2 §11.3 (zero-yield cash assumption)

**Critical distinction:** 
- Do NOT conflate "cash reserved but unexecuted" with "allocation failure"
- Reserved cash is a VALID state per Baseline v2 §12.3 (execution may occur in a later month/year)
- At window END, unrealized reservations count as unconverted cash, not as executed exposure

### C2. Denominator: Total Cash Granted

**Identical to MP-DEPLOY denominator.**

$$CP_{residual} = \frac{\text{available} + \text{reserved-but-unexecuted}}{\text{cash\_granted}}$$

### C3. Relationship to MP-DEPLOY

**By construction:** MP-DEPLOY + CP-RESIDUAL = 1.0 (within rounding)

Proof: 
- Cash granted = Cash deployed (committed) + Cash never deployed
- Cash never deployed = Available + Reserved-but-unexecuted
- Therefore: (Deployed) / (Granted) + (Available + Reserved) / (Granted) = 1.0

This identity provides an automatic consistency check.

### C4. Why CP-RESIDUAL vs. Alternatives

| Alternative | Rejected? | Reason |
|---|---|---|
| CP-NEVER (capital never converted into ANY exposure) | NO — alternative framing | Same as CP-RESIDUAL (if never converted by window end, it's unconverted). Retained as equivalent descriptor. |
| CP-TIME-WEIGHTED (time-weighted availability) | NO — secondary descriptor | Useful for understanding cash availability *through time*, not just at window end. Retained as optional. |

### C5. Pathological Cases

**Case 1: Reserved-but-unexecuted cash, if future execution is possible**
- If window ends with outstanding reservations, they count as unconverted under this methodology
- This is NOT a bug; it reflects the true state at window-end
- **Handling:** Report separately per MP-EV-D2; note: "¥X reserved, awaiting execution after window-end"

**Case 2: Strategy never deploys anything**
- Unconverted cash = 100% of granted
- CP-RESIDUAL = 1.0
- **Handling:** Report with explicit note: "zero deployment in this window"

---

## D. ACQUIRED EXPOSURE UNITS — DEFINITION

**Definition adopted: Direct mechanical field from preserved results**

$$AEU = \text{exposure\_units\_held at terminal observation}$$

### D1. Source and Scope

**Source field:** From preserved mechanical/economic results: `exposure_units_held` at terminal state of the window (final observation date).

**Authority basis:** Baseline v2 §2.3 (1 unit = ¥10,000 notional); §13.1–§13.2 (exposure metrics); preserved D-H1/D-H2 mechanical checkpoints

**Example values (preserved, not computed here):**
- D-H1 Strategy D: 14,378.59091... units (from D-H1 economic result table §3)
- D-H1 Strategy B: 13,579.96260... units (from D-H1 economic result table §3)
- D-H2 Strategy D: 0 units (from D-H2 mechanical result §3)

### D2. Comparability Across B and D

**Within-window direct comparison:** YES. Both strategies operate under identical:
- Funding schedule (¥120,000/year, granted at start of calendar year)
- Unit definition (1 unit = ¥10,000)
- Execution mechanics (Baseline v2 §9, §12)
- Window boundaries and observation dates

**Therefore:** Difference in `exposure_units_held` is directly attributable to:
1. How much cash each strategy deployed (MP-DEPLOY difference)
2. At what prices/dates each strategy executed (execution timing effect)

### D3. Terminal Holdings vs. Gross Acquisitions

**What this field captures:** Only terminal holdings, not the FULL acquisition history.

**Potential information loss:** If both strategies acquired exposure but one then sold or reversed, only holdings would show the difference.

**Assessment:** Under Baseline v2, there is **no sell, liquidation, or reversal mechanism**. All exposure acquired remains held through window-end. Therefore, terminal holdings = gross acquisition.

**No additional derived metric needed** unless a future window has liquidation capability.

### D4. Mechanical Verification

**Consistency check (preserved evidence):** Compare D-H1 numbers against evidence:
- D acquired 14,378.59... units ✓
- B acquired 13,579.96... units ✓
- D − B = +798.63... units (D acquired more)

**Status:** Direct mechanical quantities; no recalculation necessary for B-vs-D.

---

## E. FINAL ECONOMIC VALUE — DEFINITION

**Definition adopted: MODE-P COMBINED TERMINAL ECONOMIC VALUE (authorized)**

$$FEV = \text{Exposure Market Value} + \text{Unconverted Cash}$$

$$FEV = (\text{units\_held} \times \text{terminal\_price}) + (\text{cash\_available} + \text{cash\_reserved})$$

### E1. Authority and Status

**Authorized by:** Mode-P Terminal Valuation Decision (f0f60fa), decisions MP-EV-D1 through MP-EV-D4

**Label requirement:** MUST be labeled in every report as:
> **MODE-P TERMINAL ECONOMIC VALUE — NOT BASELINE TTEV — SIMULATION-TRIAL ONLY**

**NOT:** This is NOT Baseline TTEV. Baseline TTEV requires Phase-2 execution under different governance. This is a simulation-trial-only provisional calculation.

### E2. Component Definitions

**Exposure Market Value:**
$$EMV = \text{exposure\_units\_held} \times \text{terminal\_valuation\_price}$$

- **Terminal valuation price:** The close of the final available observation in the window (MP-EV-D1)
- **D-H1:** Price on 1987-07-24 = 27.3328140... JPY per unit
- **D-H2:** Price on 1990-01-18 = TBD from preserved results

**Unconverted Cash:**
$$UC = \text{cash\_available} + \text{cash\_reserved\_unexecuted}$$

Per MP-EV-D2, must be disclosed as TWO separate sub-components in any analysis.

### E3. Comparison Within Window

**Funding-Relative Simple Return (secondary descriptor):**

$$FRSR = \frac{FEV - \text{cumulative\_grant}}{FEV}$$

Example (D-H1, all strategies granted identical ¥360,000):
- D: FEV = ¥393,007.35 → FRSR = (393,007.35 − 360,000) / 360,000 = 0.09168... (≈9.17%)
- B: FEV = ¥391,178.59 → FRSR = (391,178.59 − 360,000) / 360,000 = 0.08660... (≈8.66%)

**Interpretation:** Return percentage relative to total capital granted. Simple, non-annualized, single-path.

**Status:** Examples illustrative only. Values NOT computed in this task.

### E4. Explicitly Prohibited Metrics

**MUST NOT introduce (without separate Owner authorization):**
- CAGR (Compound Annual Growth Rate)
- XIRR (Internal Rate of Return)
- Sharpe Ratio
- Volatility measures
- Drawdown statistics
- Statistical significance testing
- Confidence intervals
- Time-weighted returns

**Reason:** These require methodology decisions (M-1, M-2, M-8, etc.) that remain OPEN and cannot be decided here.

### E5. Temporal Information Preserved Separately

**Not embedded in FEV (which is a terminal snapshot):**
- When acquisitions occurred (implied in MP-TIME secondary)
- Price path effects (D-H1 vs D-H2 show different outcomes due to market regime)
- Sequence dependency (whether deployment was front-loaded vs. distributed)

**Handling:** Preserved via MP-TIME and deployment timing analysis (§G below).

---

## F. FOUR-VARIABLE CAUSAL/MECHANICAL MODEL

**Proposed decomposition:**

```
GRANT (¥360,000 identical)
  ↓
DECISION RULE (Strategy B vs. Strategy D)
  ↓
DEPLOYMENT BEHAVIOR (how much cash gets committed)
  ├─→ MP-DEPLOY (deployment ratio)
  ├─→ CP-RESIDUAL (cash preserved)
  └─→ MP-TIME (concentration of deployment over time)
  ↓
EXECUTION TIMING & PRICES (at what dates/prices committed cash becomes exposure)
  ├─→ Market regime at execution dates
  ├─→ Relative to decision dates (Signal evaluation vs. execution lag)
  └─→ Terminal price path effect
  ↓
ACQUIRED EXPOSURE UNITS (AEU)
  ├─→ Determined by: (deployed cash / execution price on each execution date)
  └─→ Terminal AEU = sum of all unit acquisitions
  ↓
TERMINAL MARKET VALUE (EMV)
  ├─→ Determined by: (AEU × terminal price at window-end)
  └─→ Path-independent given AEU (terminal price is fixed at window-end)
  ↓
FINAL ECONOMIC VALUE (FEV)
  ├─→ = EMV + unconverted cash
  └─→ Reflects both deployment and timing effects combined
```

### F1. Mechanical Identities vs. Strategy Effects

**Pure mechanical identities (no choice involved):**
- EMV = AEU × terminal_price (fixed once AEU is determined)
- MP-DEPLOY + CP-RESIDUAL = 1.0 (accounting identity)
- FEV = EMV + UC (definition)

**Strategy-dependent relationships:**
- How much cash is deployed (B may deploy differently than D)
- When it is deployed (different rules → different execution dates)
- Therefore, AEU (which units were acquired, and at what prices)
- Therefore, final FEV

### F2. Strategy-Driven Choice Points

**Strategy B rule determines:**
1. On which observation dates to signal (daily drawdown trigger)
2. How much cash to request (1.0 or 2.0 units depending on zone)
3. Monthly capacity constraint (at most 1 commitment/month)
4. No month-end fallback

**Strategy D rule determines:**
1. On which observation dates to signal (same drawdown zones)
2. **Different deployment logic:** Normal first, then conditional escalation
3. **Different monthly capacity:** up to 2 allocations per month (given conditions)
4. No month-end fallback

**Both subject to:**
- Available funding at commitment time (budget capping, §12.4)
- Same annual grant schedule
- Same execution mechanics

### F3. Causal Direction

**NOT a causal claim:**
This model is purely **mechanical**. It describes what quantities influence what other quantities, but does NOT claim causation in the scientific sense (e.g., "deployment causes exposure"). Rather, it is a decomposition showing:

- Grant → Deployment behavior (strategy rule applied to market conditions)
- Deployment → AEU (via execution mechanics and prices)
- AEU → FEV (via terminal price)

---

## G. DEPLOYMENT EFFECT vs. TIMING EFFECT — DECOMPOSITION

**Core question:** How much of the B-vs-D difference in FEV comes from:
1. Different amounts deployed (deployment effect)?
2. Different execution dates/prices (timing effect)?

### G1. Proposed Decomposition Method

**Step 1: Quantify deployment difference**
$$\Delta_{deploy} = \text{deployed}_D - \text{deployed}_B$$

Example (D-H1, preserved): ¥360,000 − ¥340,000 = +¥20,000 (D deployed ¥20k more)

**Step 2: Isolate timing effect**

Hypothetical: If B had deployed D's exact cash amount at D's exact dates, how many units would B have acquired?

**Calculation:**
- Use B's deployment dates (when B committed allocations)
- Use D's deployment dates (when D committed allocations)
- Use the actual execution prices from the preserved mechanical result
- Calculate the counterfactual unit acquisitions

**Question:** Can this be computed from preserved evidence WITHOUT rerunning B?

**Answer:** YES, the decomposition can be derived from preserved evidence IF:
- Preserved D-H1 economic result shows B deployed ¥340k and acquired 13,579.96 units
- Preserved D-H1 economic result shows D deployed ¥360k and acquired 14,378.59 units
- Preserved D-H1 event log shows the dates and prices of each allocation

**Decomposition:**
- B deployed less (¥20k difference) → purely a deployment effect
- B executed at different dates → purely a timing effect
- The B-vs-D unit difference = (difference due to ¥20k more deployment) + (difference due to timing/prices)

### G2. Exact Decomposition Formula

Given:
- $C_B$ = cash deployed by B
- $C_D$ = cash deployed by D  
- $A_B$ = units acquired by B at B's execution dates/prices
- $A_D$ = units acquired by D at D's execution dates/prices

**Hypothetical scenarios:**

1. **Scenario A: B deployed D's cash, at D's dates/prices**
   - Units: $A_{B|C_D, P_D}$ (B's cash, D's execution path)
   - This isolates the effect of "how much more cash"

2. **Scenario B: D deployed B's cash, at D's dates/prices**
   - Units: $A_{D|C_B, P_D}$ (D's cash, D's execution path)
   - Shows timing/price contribution

**Decomposition:**
$$\Delta A = A_D - A_B = \underbrace{(A_{B|C_D, P_D} - A_B)}_{\text{deployment effect}} + \underbrace{(A_D - A_{B|C_D, P_D})}_{\text{timing/price effect}}$$

### G3. Can This Be Computed Without Rerunning?

**Analysis:**

The deployment-vs-timing decomposition can be derived from preserved evidence IF event logs show each allocation's execution date, execution price, and unit quantity. No strategy rerun is required IF preserved mechanical evidence is sufficient.

**Timing/price effect:** Knowing D acquired more units than the hypothetical counterfactual, the difference is purely timing/price.

**Conclusion:** The decomposition CAN be computed from preserved evidence without rerunning Strategy B IF:
1. Event logs show each allocation's execution date and execution price
2. Event logs show each allocation's unit quantity
3. A weighted average execution price can be calculated for each strategy

**Status:** Actual computation of these values is DEFERRED to the future execution task. This methodology defines the approach only.

### G4. Interaction Terms and Ambiguities

**Potential interaction:** If B and D deploy at different times, the market may be at different prices. So "deployment amount" and "timing" are not independent.

**Example:** D deploys ¥20k more on 1987-05-15 (at ¥25/unit); B would have deployed it on 1987-03-10 (at ¥30/unit). Same ¥20k → fewer units at higher price.

**Handling:** Report this as a **cross-effect**, not as a pure "timing" vs. "deployment" split:
- Deployment difference: +¥20k
- Timing difference: D's execution dates vs. B's execution dates
- **Cross-effect:** The combination matters

**Clarity:** Avoid claiming clean orthogonal decomposition. Instead, state:
- "D deployed ¥20k more cash"
- "D executed at dates/prices that resulted in X units per ¥10k; B resulted in Y units per ¥10k"
- "Difference in unit acquisition: composed of deployment amount + timing/price interaction"

---

## H. ZERO-ALLOCATION CASE HANDLING

**D-H2 demonstrates:** Strategy D can naturally produce zero allocations (triggers never fire).

### H1. Zero-Allocation Is Not an Error

**Explicit statement:** A zero-allocation result is NOT:
- A failure of the strategy logic
- An indication of weakness
- An indication of strength
- A reason to exclude the window
- A missing data problem

**It IS:** A valid behavioral outcome when market conditions don't satisfy trigger conditions.

### H2. How to Handle Zero-Allocation Across All Four Variables

| Variable | Treatment |
|---|---|
| **MP-DEPLOY** | 0 / granted = 0.0% (100% undeployed). Report with note: "zero allocations." |
| **CP-RESIDUAL** | 1.0 (100% cash preserved). Natural consequence of zero deployment. |
| **MP-TIME** | 0.0% (zero observations with non-zero exposure). No holding period. |
| **AEU** | 0 units. Mechanical fact. |
| **EMV** | 0 × terminal_price = ¥0. Mechanically determined. |
| **FEV** | ¥0 (exposure) + ¥granted (cash) = ¥granted. All capital remains as cash. |
| **FRSR** | (granted − granted) / granted = 0%. No gain, no loss; break-even. |

### H3. B-vs-D Comparison When D Has Zero-Allocation

**Scenario: B deployed something; D deployed nothing in same window**

Valid factual statements:
- "B deployed X% of granted; D deployed 0%"
- "D retained 100% as cash; B retained Y% as cash"
- "B acquired N units; D acquired 0 units"
- "B's terminal value was ¥M; D's terminal value was ¥granted" (assuming zero gain on cash)

**Invalid interpretations:**
- ❌ "D's strategy failed" (zero allocation is consistent with zero triggers)
- ❌ "D is inferior" (comparison requires identical market regimes; D-H2's no-drawdown regime is not inferior, it's different)
- ❌ "D's rule is broken" (the rule is WORKING; it's not firing because conditions don't trigger)

### H4. Window-Level Comparison Semantics

**For D-H2 specifically (D-H2 had zero allocation):**
- Compare B-vs-D within H2 directly: factual differences in deployment, units, cash retained
- BUT do NOT claim "robustness" or "superiority" from H2 alone
- Note: H2 represents a "no-drawdown regime"; H1 represents a "drawdown-active regime"
- The two windows show different MARKET CONDITIONS, not different strategy quality

---

## I. FUNDING COMPARABILITY — INTEGRITY GATE

**Before any B-vs-D comparison is made, the following MUST be true:**

### I1. Mandatory Conditions (FAIL CLOSED)

| Condition | Check | Action if violated |
|---|---|---|
| **Identical window** | H1: 1985-01-31 → 1987-07-26; H2: 1987-07-27 → 1990-01-18 | Both B and D must use the SAME window. FAIL if windows differ. |
| **Identical funding schedule** | Both strategies granted annually on same calendar dates | FAIL if funding timing differs. |
| **Identical annual_units** | Both strategies granted 12.0 units per calendar year (Invariant 3) | FAIL if annual grants differ. |
| **Identical unit_value_jpy** | 1 unit = ¥10,000 (Baseline v2 §2.3) | FAIL if unit definition differs. |
| **Identical terminal observation** | Both strategies evaluated at same final date and price | FAIL if terminal observation differs. |
| **Mechanically valid runs** | Both strategies completed without invariant violations | FAIL if either run has unresolved invariant failures. |
| **Same data provenance** | Both strategies use the same input file (e.g., D-H1 for both B-D on H1) | FAIL if input data differs. |

### I2. Verification Procedure

Before computing B-vs-D results:

1. **Extract from preserved mechanical results:**
   - Strategy B: window start date, window end date, grant total, terminal_price_on_final_date
   - Strategy D: window start date, window end date, grant total, terminal_price_on_final_date

2. **Verify exact equality:**
   ```
   if (B.window_start != D.window_start) FAIL
   if (B.window_end != D.window_end) FAIL
   if (B.cash_granted != D.cash_granted) FAIL
   if (B.terminal_price != D.terminal_price) FAIL
   if (B.input_file_sha256 != D.input_file_sha256) FAIL
   ```

3. **If any check fails, STOP and report:**
   - "Funding comparability gate FAILED"
   - Do NOT attempt to normalize or adjust
   - Report the specific field that failed

### I3. Expected State for H1 and H2

**D-H1 B-vs-D comparison (when authorized):**
- Input: NDXJPY 1985-01-31 → 1987-07-26 (D-H1 bounded-release decision `b722fb2`)
- Funding: ¥360,000 total (¥120k × 3 years)
- Terminal: 1987-07-24 close
- Both B and D MUST use identical dataset

**D-H2 B-vs-D comparison (when authorized):**
- Input: NDXJPY 1987-07-27 → 1990-01-18 (D-H2 canonical clean CSV, SHA `d8089b9...`) per provenance remediation
- Funding: ¥360,000 total (¥120k × 3 years)
- Terminal: 1990-01-18 close (dataset final observation)
- Both B and D MUST use identical dataset

---

## J. CROSS-WINDOW COMPARISON SEMANTICS

**D-H1 and D-H2 represent TWO DIFFERENT MARKET REGIMES.**

### J1. Within-Window Comparison (Primary)

**D-H1 comparison:** Compare B-vs-D WITHIN the 1985-01-31 → 1987-07-26 window.
- Both strategies operate under the SAME market conditions
- Differences are attributable to RULE, not to market regime
- Example finding: "On H1, D deployed ¥20k more than B" is valid

**D-H2 comparison:** Compare B-vs-D WITHIN the 1987-07-27 → 1990-01-18 window.
- Both strategies operate under the SAME (but different) market conditions
- Example finding: "On H2, D deployed ¥0, while B deployed ¥X" is valid

### J2. Cross-Window Observation (Secondary, with strict constraints)

**Question:** How does the B-vs-D relationship CHANGE between H1 and H2?

**Valid observations (ONLY if stated correctly):**
- "D-H1 showed D deployed more; D-H2 showed D deployed nothing"
- "D's allocation mechanism depends on drawdown zone triggers; H1 had triggers, H2 did not"
- "The market regimes differed: H1 experienced drawdowns; H2 did not"

**Invalid claims (PROHIBITED):**
- ❌ "D is robust across windows" (two windows don't establish robustness)
- ❌ "D generalizes" (two windows don't establish generalization)
- ❌ "D is more consistent than B" (consistency requires multiple independent, identical-regime windows)
- ❌ "The results are statistically significant" (mode-P, single-path, no statistical testing authorized)

### J3. Aggregation Across Windows

**Question:** May H1 and H2 be combined into a single "average" or "aggregate" score?

**Answer:** NO without separate Owner authorization.

**Reason:** 
- H1 and H2 had different market conditions (drawdown-active vs. drawdown-absent)
- Combining them implies equal weighting to two structurally different regimes
- Doing so without explicit approval would hide the regime dependency

**If aggregation is desired later:**
- Requires a separate methodology decision
- Must specify: how are H1 and H2 weighted?
- Must state explicitly: "aggregation hides regime-dependency"
- Requires Owner approval before computing

### J4. Cross-Window Pattern Observation

**Permitted (narrowly):**
"Strategy D's deployment behavior differs between H1 and H2 because the triggering conditions differed (H1 had drawdowns; H2 did not). This is consistent with D's design."

**This is NOT:** Evidence of robustness, optimality, or generalization. It is a mechanism observation.

---

## K. PERMITTED FACTUAL STATEMENTS — VOCABULARY FREEZE

**These statements are PERMITTED for B-vs-D results (factual, mechanical):**

1. **Deployment comparisons:**
   - "D deployed ¥X more / less granted capital than B"
   - "D deployed Y% of granted; B deployed Z% of granted"
   - "The deployment difference was ¥W"

2. **Cash preservation comparisons:**
   - "D retained ¥A more unconverted cash than B"
   - "D retained P% of granted as cash; B retained Q% as cash"
   - "D's reserved-but-unexecuted cash was ¥R; B's was ¥S"

3. **Acquisition comparisons:**
   - "D acquired N more / fewer exposure units than B"
   - "D acquired M units; B acquired K units"
   - "The unit-acquisition difference was L units"

4. **Economic-value comparisons:**
   - "D's combined terminal value (MODE-P ONLY) was ¥X; B's was ¥Y"
   - "The terminal-value difference was ¥Z (favoring D / B)"
   - "D's funding-relative return (PROVISIONAL) was P%; B's was Q%"

5. **Temporal comparisons:**
   - "D deployed more evenly over the window; B deployed more front-loaded" (if true)
   - "D's first allocation occurred on date D1; B's on date B1"
   - "D held exposure for T% of observations; B held exposure for U% of observations"

6. **Directional language (ONLY if factually accurate):**
   - "D's market participation (MP-DEPLOY) was higher / lower than B"
   - "D's cash preservation (CP-RESIDUAL) was higher / lower than B"
   - "D's acquired units were more / fewer than B"

---

## L. PROHIBITED STATEMENTS — HARD BOUNDARY

**These claims are ABSOLUTELY PROHIBITED regardless of numerical results:**

- ❌ "D is better than B" / "D is superior"
- ❌ "D is worse than B" / "D is inferior"  
- ❌ "D should replace B"
- ❌ "D should be adopted as Baseline"
- ❌ "D is optimal"
- ❌ "D is more robust"
- ❌ "D generalizes to other markets / windows"
- ❌ "D is statistically significant"
- ❌ "D's result is definitive"
- ❌ "The analysis proves D..."
- ❌ Treating Favorable result on H1 as adoption-ready (§18.4.7 anti-contamination)
- ❌ Retroactively describing D-H0 as "independent validation" (it's hypothesis-generating)
- ❌ Using D-H1 favorable result to justify Phase 2 advancement without D-H2 disclosure
- ❌ "D is robust because it performed differently in H1 vs H2" (different market regime, not robustness)

**Why:** Section 18.4.3 (Mode-P structural bar on strategy superiority claims); §18.4.7 (anti-contamination); this methodology is NOT A QUALIFICATION DECISION.

---

## M. STRATEGY-E FIREWALL — EXPLICIT BOUNDARY

**This methodology analyzes B and D ONLY.**

### M1. Strategy E — Not Designed Here

Strategy E (or any new strategy) is EXPLICITLY OUT OF SCOPE.

**Example prohibited synthesis:**
"D participates better in drawdown periods but retains more cash in rising markets. Strategy E should combine D's drawdown triggers with B's cash-deployment aggressiveness."

**Why prohibited:**
- D-H2 was not run to study "rising market" behavior; it was a separate validation window
- Reverse-engineering a rule from observing where B vs D succeeded is hindsight contamination
- Any such rule is a NEW hypothesis requiring its own registration, semantics, and anti-contamination discipline

### M2. How Strategy E Could Be Authorized Later

1. **Separate hypothesis registration** (new AR-xx entry or equivalent)
2. **Explicit semantic freeze** before any evidence is examined
3. **Separate validation window** or cross-validation
4. **Separate Owner Decision** authorizing its investigation
5. **Full anti-contamination protocol** (not derived from B-vs-D results)

**Status:** This methodology DOES NOT authorize any of the above.

---

## N. MINIMUM REQUIRED FUTURE COMPUTATION

**If this methodology is approved, the future B-vs-D execution task will derive comparative metrics from already-preserved fields.**

### N1. Strategy B Evidence Status

**Current state:** Verify whether Strategy B mechanical runs on D-H1 and D-H2 inputs already exist and are preserved.

**If preserved:** Use the existing runs (no rerun required).

**If NOT preserved:** Run Strategy B once on D-H1 input and once on D-H2 input using the frozen Baseline v2 §4.2 rule.

### N2. Required Source Fields

**From preserved mechanical/economic results (B and D):**

1. **MP-DEPLOY(B, H1)** and **MP-DEPLOY(D, H1)**
   - Fields needed: sum of allocation amounts, total grant
   - Source: terminal_state.json and manifest metadata
   - Computation: simple division

2. **CP-RESIDUAL(B, H1)** and **CP-RESIDUAL(D, H1)**
   - Fields needed: cash_available_jpy, cash_reserved_unexecuted_jpy, total grant
   - Source: terminal_state.json
   - Computation: simple division

3. **MP-TIME(B, H1)** and **MP-TIME(D, H1)** (secondary)
   - Fields needed: observations with exposure_held > 0, total observations
   - Source: event_log.json, cumulative tracking
   - Computation: percentage

4. **AEU(B, H1)** and **AEU(D, H1)**
   - Fields needed: exposure_units_held at terminal state
   - Source: terminal_state.json
   - Computation: direct read

5. **EMV(B, H1)** and **EMV(D, H1)**
   - Fields needed: exposure_units_held, terminal_price
   - Source: terminal_state.json, dataset final close
   - Computation: multiplication

6. **FEV(B, H1)** and **FEV(D, H1)**
   - Fields needed: EMV, cash_available_jpy, cash_reserved_unexecuted_jpy
   - Source: terminal_state.json
   - Computation: addition

7. **FRSR(B, H1)** and **FRSR(D, H1)** (secondary)
   - Fields needed: FEV, cumulative grant
   - Source: derived from above
   - Computation: simple percentage

**Same fields required for D-H2.**

### N3. Critical Note: Derived Metrics NOT Yet Computed

**This methodology defines WHAT to compute and HOW to compute it.**

**This methodology does NOT compute those metrics.**

**Actual B-vs-D comparative metrics will be derived from preserved evidence in the future execution task, using fields and formulas specified here.**

**Status:** No strategy rerun is required IF preserved mechanical evidence (terminal_state.json, event_log.json, manifest) from both B and D runs is available on identical windows. If preserved evidence is insufficient, one run of Strategy B (per window) is the only execution needed.

---

## O. DECISION MATRIX — GOVERNANCE CHECKPOINTS

| # | Decision | Recommended Disposition | Alternative | Rationale | Implementation Cost | Owner Approval Required |
|---|---|---|---|---|---|---|
| **BD-M1** | **Research Question** | "Given identical funding and the same frozen market input, how do fixed Strategy B and fixed Strategy D trade off market participation, cash preservation, acquired exposure units, and final economic value?" | Alternative wording or scope change | Frozen wording prevents scope creep. Disallows reinterpretation after analysis. | Verbal/text-only | YES — already included in this design |
| **BD-M2** | **Market Participation Definition** | MP-DEPLOY (capital deployment ratio: deployed / granted) | MP-ALLOC, MP-TIME, MP-BINARY | MP-DEPLOY is most direct; MP-TIME retained as secondary | Direct calculation from existing fields | YES (already decided above) |
| **BD-M3** | **Market Participation Numerator** | Sum of allocation amounts committed (post-capping) across all months | Alternative: use requested amounts | Committed amounts respect budget constraints; more meaningful | Simple aggregation |  |
| **BD-M4** | **Market Participation Denominator** | Total cash granted (annual × years + prorated first/last) | Alternative: use end-of-period available units | Cash granted is invariant per funding schedule; prevents gaming | Simple calculation | YES (Invariant 3 enforces identical grants) |
| **BD-M5** | **Cash Preservation Definition** | CP-RESIDUAL (terminal unconverted cash / total granted) | CP-NEVER, CP-TIME-WEIGHTED | Direct, terminal-focused; secondary measures available | Simple division | YES (already decided above) |
| **BD-M6** | **Cash Preservation Numerator** | Sum of available + reserved-but-unexecuted at terminal state | Alternative: available only | Separate disclosure (MP-EV-D2); avoids underestimating preservation | Direct read from terminal_state | YES (Mode-P decision) |
| **BD-M7** | **Acquired Exposure Units** | Direct terminal_state.exposure_units_held field | Alternative: recalculate from transactions | No ambiguity; directly comparable; no data loss (no liquidation mechanism) | Direct read | YES (mechanical, no recomputation) |
| **BD-M8** | **Economic Endpoint** | MODE-P COMBINED TERMINAL ECONOMIC VALUE (labeled) | Alternative: use alternative metrics | Authorized by f0f60fa; mandatory label distinguishes from Baseline TTEV | Direct read + simple addition | YES (already authorized) |
| **BD-M9** | **Economic Value Components** | Exposure market value (units × terminal price) + unconverted cash (available + reserved) | Alternative: include other adjustments | Terminal price authorized (MP-EV-D1); reserved-cash treatment authorized (MP-EV-D2) | Simple multiplication and addition | YES (Mode-P decision) |
| **BD-M10** | **Zero-Allocation Handling** | Report as valid outcome; do not exclude; do not claim error/strength; disclose triggers didn't fire | Alternative: exclude window, or assume failure | D-H2 demonstrates zero-allocation is natural for Strategy D; symmetry requires same treatment for B | Narrative disclosure only | YES (required by anti-contamination) |
| **BD-M11** | **Funding Comparability Gate** | FAIL CLOSED if window, funding, unit definitions, or terminal price differ | Alternative: normalize/adjust | Any adjustment introduces methodological choice; FAIL CLOSED prevents hidden assumptions | Automated verification check | YES (required for integrity) |
| **BD-M12** | **Deployment vs. Timing Decomposition** | Separate "cash deployed" from "execution dates/prices"; note interaction effects; don't claim orthogonal split | Alternative: claim clean orthogonal decomposition | Acknowledges that timing and deployment amounts interact via prices; more honest | Disclosure in analysis | YES (prevents false precision) |
| **BD-M13** | **Within-Window Comparison** | B-vs-D compared only within same window (H1 with H1, H2 with H2) | Alternative: cross-window averages | Same market regime assumption required for mechanical attribution | Organizational (run separately) | YES (prevents regime conflation) |
| **BD-M14** | **Cross-Window Observation** | Document HOW market regimes differed (H1 = drawdown-active, H2 = drawdown-absent); note rule responses naturally differ | Alternative: claim robustness, generalization | Two windows with different conditions don't establish robustness; they establish regime sensitivity | Narrative (market analysis) | YES (prevents false claims) |
| **BD-M15** | **Claim Vocabulary** | Use only permitted factual comparisons (deployment, cash, units, terminal value); prohibit superiority/inferiority | Alternative: allow normative language | §18.4.3 Mode-P structural bar; anti-contamination required | Compliance checklist | YES (non-negotiable) |
| **BD-M16** | **Strategy-E Firewall** | Explicitly prohibit synthesis of new rule from B-vs-D observations; require separate hypothesis registration if Strategy E is later proposed | Alternative: allow evolutionary design from observations | Prevents contamination; maintains clear hypothesis → evidence ordering | Governance only (no computation) | YES (anti-contamination critical) |
| **BD-M17** | **Strategy B Evidence Status** | Use preserved Strategy B run IF available on identical window/input; if not preserved, run once only per window | Alternative: always rerun for safety | Single rerun acceptable if needed; multiple reruns risk data contamination | Single execution on H1 + H2 if needed | YES (if not already available) |
| **BD-M18** | **Documentation & Approval** | This methodology frozen BEFORE analyzing H1/H2 results; results reported separately; methodology NEVER edited retroactively after results seen | Alternative: draft methodology after seeing results | Pre-result methodology freeze is the anti-contamination control | Process discipline only | YES (mandatory) |

---

## P. UNRESOLVED QUESTIONS

The following remain open and do NOT block methodology approval:

1. **Exact field names in preserved evidence:** terminal_state.json column names may vary; exact mapping TBD during execution task
2. **Partial-year prorating logic:** First/last year funding calculations (Invariant 14) require fine detail; formula in §I.2 is conceptual
3. **Weighted average execution price calculation (for decomposition):** Exact weighting scheme (by allocation amount? by observation count?) TBD during execution
4. **Cross-month execution timing:** If H1 or H2 has executions crossing calendar months, attributed to which month? Resolved by Baseline v2 §12.2; exact implementation TBD

**Status:** None of these block methodology approval. All are resolvable during execution.

---

## Q. SCOPE AND EXPLICIT NON-AUTHORIZATION

**This artifact:**
- ✓ Freezes research question and variable definitions
- ✓ Establishes comparison semantics and boundaries
- ✓ Identifies required fields from preserved evidence
- ✓ Creates decision matrix
- ✓ Establishes claim vocabulary

**This artifact does NOT:**
- ❌ Execute any strategy
- ❌ Compute any B-vs-D result
- ❌ Rerun H1 or H2
- ❌ Modify Strategy B or D
- ❌ Design Strategy E
- ❌ Authorize Phase 2
- ❌ Change qualification state
- ❌ Claim any superiority, inferiority, or robustness
- ❌ Approve any future Phase-2 progression

---

## R. NEXT TASK (REQUIRES SEPARATE OWNER AUTHORIZATION)

**If this methodology is approved by Owner Decision:**

**Next task to be SEPARATELY AUTHORIZED (not begun here):**

**"B-vs-D Mechanism Analysis Execution"**

Scope:
1. Verify Strategy B mechanical run on D-H1 exists and is preserved (or run once if needed)
2. Verify Strategy D mechanical run on D-H1 is preserved (already exists)
3. Extract all required fields per §N above
4. Derive all defined variables (§B–§E) from preserved fields
5. Prepare factual comparison report using only permitted vocabulary (§K–§L)
6. Report cross-window observation (§J) with explicit regime-dependency note
7. Do NOT rank B vs D; do NOT claim superiority; do NOT advance any claim to adoption

---

## S. ARTIFACT STATUS

**File:** `docs/decisions/simulation_trial_strategy_bd_mechanism_analysis_methodology.md`

**Status:** APPROVED BY OWNER DECISION, 2026-08-15 — METHODOLOGY ONLY.

**Approval scope:**
- Freezes B-vs-D comparison methodology before result analysis ✓
- Approves BD-M1 through BD-M18 as reviewed ✓
- Does not compute or authorize reinterpretation of B-vs-D results ✓
- Does not execute or modify Strategy B ✓
- Does not execute or modify Strategy D ✓
- Does not design Strategy E ✓
- Does not change qualification state ✓
- Does not authorize Phase 2 ✓

**No strategy modified:** B and D remain frozen exactly as per consolidation checkpoint
**No result computed:** All B-vs-D analysis deferred to separate execution task
**No Strategy E designed:** Firewall explicit and enforced
**Qualification state unchanged:** O-4, P1-x, M-x, HG-8, Primary Proxy, Phase 2 all unchanged

**Next task (separate authorization required):** EXECUTE THE APPROVED B-vs-D MECHANISM ANALYSIS USING PRESERVED D-H1 AND D-H2 EVIDENCE, WITHOUT RERUNNING STRATEGIES UNLESS REQUIRED BY AN EVIDENCE-INTEGRITY FAILURE.

---

**End of Approved Methodology. Preservation complete 2026-08-15.**
