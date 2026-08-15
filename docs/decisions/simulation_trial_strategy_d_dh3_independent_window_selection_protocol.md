# Simulation Trial — Strategy D Stage D-H3 Independent-Window Selection Protocol (Design)

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15 — SELECTION PROTOCOL ONLY.**

**Date drafted:** 2026-08-15

**Owner approval date:** 2026-08-15

**Approval scope:** This approval fixes the H3 independent-window selection protocol. It approves reuse of the frozen f025bbf deterministic selection framework, with one H3-specific addendum (DH3-R5: temporal moat around the consumed research region). This approval does not select H3, choose an instrument, identify dates, execute any strategy, compute economic results, or change qualification state.

**CRITICAL BOUNDARY STATEMENT:**

This artifact **designs a protocol only**. It does **NOT**:
- ✗ Select H3
- ✗ Reveal a candidate window
- ✗ Inspect any candidate market values
- ✗ Retrieve new market data
- ✗ Execute Strategy D
- ✗ Execute Strategy B
- ✗ Rerun H1/H2
- ✗ Modify Strategy D
- ✗ Modify Strategy B
- ✗ Design Strategy E
- ✗ Choose a market regime
- ✗ Compute economic results
- ✗ Change qualification state

**Controlling authority chain:**

| Authority | Commit | Tag |
|---|---|---|
| Strategy D hypothesis | `5a3f54a` | — |
| Strategy D semantics | `62c5c42` | — |
| D-H1 dataset-selection policy | `f8332a5` | `simulation-trial-strategy-d-dh1-dataset-selection-policy-20260814` |
| D-H1 deterministic selection rule | `f025bbf` | `simulation-trial-strategy-d-dh1-deterministic-selection-rule-20260814` |
| D-H1 bounded release | `039be52` | `simulation-trial-strategy-d-dh1-bounded-release-20260814` |
| D-H1 result | — | prior preserved |
| D-H2 bounded release | `039be52` | `simulation-trial-strategy-d-dh2-bounded-release-20260814` |
| D-H2 corrected evidence | `ff87b88` | `simulation-trial-strategy-d-dh2-corrected-mechanical-evidence-20260815` |
| D-H2 analysis result | `8830a49` | `simulation-trial-strategy-bd-corrected-dh2-analysis-result-20260815` |
| D-H2 B-vs-D result | `e48ece4` | `simulation-trial-strategy-bd-funding-constraint-compression-result-20260815` |
| D-H2 timing/price attribution | `aa41ab8` | `simulation-trial-strategy-bd-corrected-dh2-timing-price-attribution-result-20260815` |
| B-vs-D methodology | `bb028bb` | `simulation-trial-strategy-bd-mechanism-analysis-methodology-20260815` |

**Baseline:** v2 (effective 2026-08-13, unchanged)

---

## 1. Purpose, Known-Results Disclosure, and Anti-Hindsight Boundary

### 1.1 Purpose of H3

H3 is the **third genuinely independent validation window** for the already-frozen Strategy D.

**H3 is NOT:**
- ❌ An optimization window
- ❌ A regime-search window
- ❌ A stress-test or favorable-regime selection
- ❌ A window chosen because H1/H2 produced an interesting result
- ❌ Strategy-E research
- ❌ A qualification-lane promotion
- ❌ An adoption test

**H3 is:**
- ✓ An additional mechanical observation of Strategy D on a third independently-selected market window
- ✓ A continuation of the already-frozen validation discipline
- ✓ Governed by the same frozen hypothesis and semantics as H1/H2
- ✓ Subject to the same anti-hindsight requirements as H1

### 1.2 Known-Results Disclosure (Mandatory Anti-Contamination Evidence)

**CRITICAL:** This protocol is being finalized AFTER H1/H2 results are already known to the research team.

Before H3 window selection occurs, the research team already knows:

**From D-H1:**
- D-H1 execution result (allocation count, cash deployed, terminal exposure, FEV)

**From D-H2 (corrected):**
- D-H2 corrected execution result (allocation count, cash deployed, terminal exposure, FEV)
- D-H2 B-vs-D mechanism analysis (deployment timing, acquisition-price attribution)
- Funding-constraint compression findings

**These known results MUST NOT influence the H3 selection function.**

The selection protocol must be mechanically applied without reference to:
- ❌ D-H1 or D-H2 allocation counts or drawdown behavior
- ❌ H1 or H2 cash-deployment patterns
- ❌ Trigger-firing frequency, magnitude, or regime sensitivity in H1/H2
- ❌ Whether H2 contained extensive LARGE_DROP observations
- ❌ Any known difference between B and D in any regime
- ❌ Whether funding constraints compressed in H2
- ❌ Acquisition-price or timing-attribution findings from H2
- ❌ Any expectation about H3's regime, volatility, performance, or market character
- ❌ Any preference for a candidate window that might confirm, contradict, strengthen, or weaken prior findings

**Honest disclosure:** Because DH3-R5 (the temporal moat rule) is being formalized after H1/H2 results were known, the protocol explicitly states this chronology in §3.2 below. However, DH3-R5 is restricted to a structural generalization of the pre-existing temporal-distance principle necessitated by multiple consumed windows. It uses only the framework and the prior-window dates, not any outcome knowledge.

**Selection will be evaluated for this contamination risk explicitly. Any selection rule modification made after learning H1/H2 results requires explicit disclosure and Owner approval, which this section provides.**

---

## 2. Reuse of Existing Frozen D-H1 Selection Framework (f025bbf)

**Owner Decision OD-H3-1: APPROVED**

The H3 protocol reuses the existing deterministic selection framework from commit `f025bbf` (D-H1 deterministic selection rule) to the maximum extent semantically possible.

### 2.1 Preserved Components (Reused Unchanged from f025bbf)

All existing frozen rules remain authoritative:

1. ✓ **Window-length rule (906 calendar days)** — Derived from D-H0 duration, outcome-independent
2. ✓ **Window-position rule (Earliest eligible)** — Zero-parameter rule, no regime choice
3. ✓ **Policy-tier traversal (A → B → C → D, objective-failure-gated)** — Proven framework
4. ✓ **Metadata-only eligibility tests** — Structural checks, market-independent
5. ✓ **Continuity/gap rule (90% weekday-count)** — Calendar arithmetic, outcome-independent
6. ✓ **Freeze-before-reveal procedure** — Nine-step, lightweight blinding
7. ✓ **Rejection-code vocabulary** — Closed list, all grounded in existing authority
8. ✓ **Option-B ordering** — Construct → provenance → span → lexical
9. ✓ **Option-C rule** — Next post-release + inherited duration, no partial windows
10. ✓ **Option-D rule** — MP-S-01…MP-S-08 with within-category ordering
11. ✓ **Tie-breaker hierarchy** — Tier → comparability → provenance → cost → lexical
12. ✓ **All-tiers-failed behavior** — Fail-closed, return to Owner Review

### 2.2 H3-Specific Addendum: DH3-R5 Temporal Moat (NEW)

**Owner Decision OD-H3-2: APPROVED**

One H3-specific extension is added to the existing f025bbf framework, explicitly disclosed as post-H1/H2 knowledge:

**H3-SPECIFIC ADDENDUM — Temporal Moat Around Consumed Research Region**

Because H3 now has multiple previously-consumed Strategy-D research windows (D-H0, D-H1, D-H2) that were not present when f025bbf was frozen, the temporal-distance principle must be generalized to protect the entire consumed research region from temporal-adjacency contamination.

This addendum extends the pre-existing temporal-distance principle (which originally protected distance from D-H0) to protect distance from the entire consumed region (D-H0 → D-H1 → D-H2).

**Exact formalization: see §3.2 below.**

This addendum is disclosed as an Owner-approved extension formalized after H1/H2 results became known, but it uses only the framework and prior-window dates, not outcome knowledge.

---

## 3. Existing Exclusion Set and Multi-Window Temporal Distance

### 3.1 Prior Windows (D-H0, D-H1, D-H2) — Exact Dates

| Window | Start | End | Source |
|---|---|---|---|
| **D-H0** | 2018-01-02 | 2020-06-26 | Released, hypothesis-generation |
| **D-H1** | 1985-01-31 | 1987-07-26 | First independent validation |
| **D-H2** | 1987-07-27 | 1990-01-18 | Second independent validation |

**Exclusion rule for H3:**

H3 must select a window with:
1. ✓ No overlap with D-H0 (`[2018-01-02, 2020-06-26]`)
2. ✓ No overlap with D-H1 (`[1985-01-31, 1987-07-26]`)
3. ✓ No overlap with D-H2 (`[1987-07-27, 1990-01-18]`)
4. ✓ Temporal-distance backstop applied against the most-recent prior window (D-H2)

### 3.2 Temporal-Moat Rule Formalization (DH3-R5 — H3-SPECIFIC ADDENDUM)

**Owner Decision OD-H3-2: APPROVED**

**Consumed Research Region (from repository authority):**

| Window | Start | End |
|---|---|---|
| D-H0 | 2018-01-02 | 2020-06-26 |
| D-H1 | 1985-01-31 | 1987-07-26 |
| D-H2 | 1987-07-27 | 1990-01-18 |

**Earliest boundary of consumed region:** 1985-01-31 (D-H1 start)
**Latest boundary of consumed region:** 2020-06-26 (D-H0 end)

**Temporal-Moat Rule (DH3-R5):**

An H3 candidate window must satisfy:

```
BEFORE consumed region:
  consumed_region_start.toordinal() − candidate_window_end.toordinal()  >=  1825

OR

AFTER consumed region:
  candidate_window_start.toordinal() − consumed_region_end.toordinal()  >=  1825
```

**Interpretation:**

An H3 candidate is temporally eligible if it lies at least 1,825 calendar days (approximately five years) on either side of the consumed research region `[1985-01-31, 2020-06-26]`.

**Two sides (OR logic):**
1. **BEFORE:** Candidate window ends ≥1,825 days before 1985-01-31 (placing it in early 1980 or earlier)
2. **AFTER:** Candidate window starts ≥1,825 days after 2020-06-26 (placing it in late 2025 or later)

**This creates a five-year temporal moat on each side of the consumed research region.**

**Rationale:**
- The pre-existing f025bbf temporal-distance principle (1,825 days) remains the operative constant
- The addendum generalizes that principle from protection against D-H0 to protection against the entire D-H0/D-H1/D-H2 cluster
- H3 is genuinely separated in time from all prior windows, maximizing regime independence
- No outcome knowledge enters the rule (only dates and framework)

**Disclosure:** DH3-R5 is formalized as an Owner-approved H3-specific addendum after H1/H2 results are known. However, the rule uses only the framework (the 1,825-day constant) and the prior-window dates, not any outcome knowledge. The logic is structural: protecting a multi-window research region requires generalizing the prior single-window temporal-distance rule.

---

## 4. Candidate Universe and Dataset Independence

### 4.1 Candidate Universe Definition (Metadata-Only Formation)

The eligible candidate universe for H3 is formed before any candidate value is viewed, using metadata only (dates, row counts, checksums).

**Tier A (highest priority):**
- **Instrument:** NDXJPY (original Nasdaq-100 price-return index)
- **Region:** Non-overlapping portions outside the consumed research region `[1985-01-31, 2020-06-26]`
- **Eligibility checks:** Metadata only (dates, row counts, checksums; never price values)
- **Availability determination:** At future selection execution, inspect permitted metadata to identify eligible non-overlapping spans mechanically

**Tier B:**
- **Instruments:** XNDXJPY or XNDXNNRJPY, as authorized by existing policy `f8332a5` and `f025bbf`
- **Region:** Non-overlapping portions outside consumed research region
- **Eligibility checks:** Metadata only
- **Authority boundary:** Tier B authority must be verified against existing frozen policy; do not expand without explicit authority

**Tier C:**
- **Rule:** Deterministic chronological holdout (next observation after any prior window, + fixed 906-day duration)
- **Eligibility:** Deterministic forward-positioning rule; requires authorization for any new external data retrieval if existing held snapshot does not extend far enough
- **Authority boundary:** Data acquisition must not exceed existing frozen authority; fail closed if new retrieval authority is required

**Tier D:**
- **Rule:** MP-S-07 bounded search (at most three candidates investigated)
- **Eligibility:** Inherited from existing Mode-P policy `f8332a5`, `f025bbf`
- **Universe:** Pre-formed metadata-only universe before any investigation

### 4.2 Dataset Independence Requirements

**H3 must exclude:**
1. ✓ Any observation overlapping D-H0 (`[2018-01-02, 2020-06-26]`)
2. ✓ Any observation overlapping D-H1 (`[1985-01-31, 1987-07-26]`)
3. ✓ Any observation overlapping D-H2 (`[1987-07-27, 1990-01-18]`)
4. ✓ Any observations from D-H0 data that were previously analyzed (retained after D-H0 analysis, not inspected further, but their statistics are known)
5. ✓ Any price values or summary statistics already computed from a candidate window
6. ✓ Any candidate whose price path was inspected or examined for any purpose by anyone before selection

**H3 may use:**
- ✓ Already-held NDXJPY data (Stage-D `E-01`), non-overlapping with prior windows, never before inspected for this purpose
- ✓ Qualification-research data (XNDXJPY, XNDXNNRJPY), retained under `S.2` non-analysis undertaking, with a new bounded-release decision
- ✓ Future-published data (option C) after D-H0's held snapshot ends
- ✓ General market knowledge (major events, known recessions/crashes), without outcome-specific inspection of the candidate

---

## 5. Instrument Preference and Tier Hierarchy

### 5.1 Instrument Preference Remains Unchanged

The tier-A preference for NDXJPY (the original Nasdaq-100 price-return index) is preserved:

**Why reuse:**
- Strategy D was designed against NDXJPY's drawdown semantics
- Tier-A (direct-access, low-cost) eligibility is maximal for NDXJPY
- Construct comparability is highest for NDXJPY
- No outcome-based reason exists to prefer a different instrument (H1/H2 results do not inform instrument choice)

**Tier ordering (unchanged):**
1. **Tier A:** NDXJPY, non-overlapping with D-H0/H1/H2
2. **Tier B:** XNDXJPY or XNDXNNRJPY, ordered by D-H1's existing rule
3. **Tier C:** Chronological holdout, next D-H0-derived duration window
4. **Tier D:** MP-S-07 bounded search, at most three candidates

---

## 6. Window Length (DH3-R3)

**Recommendation: UNCHANGED from D-H1**

```
DH3-R3 = 906 calendar days
```

**Rationale:**
- The 906-day duration is derived from D-H0's declared span (`2018-01-02` → `2020-06-26`), not from the market window selected
- It is independent of any outcome knowledge from H1/H2
- Reusing it preserves cross-stage structural comparability
- It was approved as a pure calendar-arithmetic fact in D-H1 (commit `f025bbf`)

**No alternative is considered.** The window length is frozen.

---

## 7. Window-Position Rule (DH3-R4)

**Recommendation: UNCHANGED from D-H1**

```
DH3-R4: Earliest eligible window
```

Apply to whichever tier-selected candidate achieves eligibility:

1. If Tier A (NDXJPY) qualifies: select its earliest eligible non-overlapping region
2. If Tier A fails and Tier B qualifies: select the earliest eligible region of the tier-B candidate
3. If Tier C applies: start at the first observation after D-H0, run for 906 days
4. If Tier D: apply to the top-ranked tier-D candidate (per `f025bbf`'s within-category ordering)

**Rationale:** The "earliest eligible window" rule has zero free parameters, no outcome-dependence, and was approved for D-H1. Reusing it ensures consistency and eliminates additional discretion.

**Not adopted:** Latest-eligible window, midpoint-derived, seed-derived (all alternatives considered in D-H1, rejected for their additional complexity and freedom).

---

## 8. Continuity / Gap Rule (DH3-R6)

**Recommendation: UNCHANGED from D-H1**

```
DH3-R6: 
  observed_count(candidate) / expected_trading_days(candidate_start, candidate_end)  >=  0.90
  where expected_trading_days = count of weekdays in [start, end]
```

**Rationale:** This is a data-integrity / structural-anomaly test only, never a market-quality filter. It is uninfluenced by price behavior and applicable to any window.

**Calculation method:** Pure calendar-date arithmetic, no market-calendar dependency, no outcome-dependence.

---

## 9. Temporal-Distance Rule (DH3-R5) — MODIFIED FOR MULTI-WINDOW EXCLUSION

**New rule for H3 (supersedes D-H1's single-window formulation):**

```
H3-candidate must satisfy ONE of:

  (1) BACKWARD DISTANCE:
      D-H2_end.toordinal() − candidate_window_end.toordinal()  >=  1825
      
      (places H3 entirely before D-H1)
      
  (2) FORWARD DISTANCE:
      candidate_window_start.toordinal() − D-H0_end.toordinal()  >=  1825
      
      (places H3 well after D-H0)
```

**Interpretation:**

An H3 candidate must be either:
- **At least 1,825 days (5 years) before D-H2's end (1990-01-18)**, ensuring it sits in the pre-1985 era, well before all three prior windows, **OR**
- **At least 1,825 days (5 years) after D-H0's end (2020-06-26)**, ensuring it is contemporary or future data, disconnected from the hypothesis-generation D-H0 window

This creates a "temporal moat" around the cluster of H0/H1/H2 observations (1985–2020), ensuring H3 is genuinely distant in time.

**Fail-closed behavior:** If no eligible candidate satisfies DH3-R5, H3 is blocked and the protocol returns to Owner Review.

---

## 10. Freeze-Before-Reveal Procedure (DH3-R12)

**Recommendation: UNCHANGED from D-H1**

Exact sequence from `f025bbf` §13:

1. Load the preserved H3-protocol version (this artifact, once approved)
2. Inspect metadata/provenance only (dates, checksums, row counts — never price values)
3. Resolve eligible tier using deterministic rules (§2, §5, §7–§9)
4. Resolve unique instrument (NDXJPY, XNDXJPY, XNDXNNRJPY, or bounded search result)
5. Resolve unique window mechanically (earliest eligible, satisfying DH3-R3, DH3-R5, DH3-R6)
6. Record the selection trace (§11)
7. Freeze source identity + exact dates + bytes + SHA-256
8. Write provenance and replacement-attempt history
9. **Only then** permit price values to be exposed to the Strategy-D execution process

**Lightweight blinding:** Steps 2–5 read metadata only (dates, checksums). Price values remain unexposed until step 9, matching the already-approved lightweight order-of-operations blinding from `f8332a5` §12.

---

## 11. Selection-Trace Schema (DH3-R13)

**Recommendation: UNCHANGED from D-H1, with addendum for multi-window context**

### 11.1 Base Schema (from f025bbf §14)

```json
{
  "selection_rule_commit": "<this artifact's commit, once preserved>",
  "selection_rule_tag": "<this artifact's tag, once preserved>",
  "policy_commit": "f8332a543f7bab4c8b5f42974813ccd70be9137f",
  "policy_tag": "simulation-trial-strategy-d-dh1-dataset-selection-policy-20260814",
  "prior_windows_excluded": {
    "D-H0": {"start": "2018-01-02", "end": "2020-06-26"},
    "D-H1": {"start": "1985-01-31", "end": "1987-07-26"},
    "D-H2": {"start": "1987-07-27", "end": "1990-01-18"}
  },
  "tiers_considered": [
    {"tier": "A", "candidate": "NDXJPY", "result": "PASS|FAIL", "rejection_codes": ["..."]},
    {"tier": "B", "candidates": ["XNDXJPY", "XNDXNNRJPY"], "result": "...", "rejection_codes": ["..."]},
    {"tier": "C", "result": "...", "rejection_codes": ["..."]},
    {"tier": "D", "candidates_considered": ["..."], "result": "...", "rejection_codes": ["..."]}
  ],
  "temporal_distance_rule": "DH3-R5: (D-H2_end.ordinal - candidate_end.ordinal >= 1825) OR (candidate_start.ordinal - D-H0_end.ordinal >= 1825)",
  "selected_instrument_identifier": "...",
  "selected_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
  "window_duration_days": 906,
  "continuity_ratio": 0.XX,
  "snapshot_sha256": "...",
  "run_date": "YYYY-MM-DD",
  "known_results_at_selection_time": {
    "D-H1_result_known": true,
    "D-H2_result_known": true,
    "B_vs_D_comparison_known": true,
    "funding_compression_finding_known": true,
    "timing_attribution_finding_known": true,
    "selection_rule_applied_mechanically_without_outcome_reference": true
  },
  "price_values_not_inspected_before_freeze": true
}
```

### 11.2 Addendum Fields for H3 (NEW)

The following fields are added to document that H3 selection occurred with knowledge of prior results:

```json
{
  "validation_stage": "D-H3",
  "prior_results_known": true,
  "prior_windows_count": 3,
  "candidate_universe_formed_before_price_inspection": true,
  "known_results_excluded_from_selection_function": true,
  "selection_contamination_risk_assessment": "PASSED — deterministic rule applied mechanically to pre-formed metadata-only universe",
  "known_results_disclosure": {
    "D-H1_result": "Window 1985-01-31 → 1987-07-26 executed; allocation count, cash deployment, exposure acquired (specific values recorded separately)",
    "D-H2_result": "Window 1987-07-27 → 1990-01-18 executed; corrected analysis result with B-vs-D comparison, funding compression, timing/acquisition-price attribution (specific values recorded separately)",
    "statement": "These results did NOT enter the H3 selection function. H3 was selected mechanically from a metadata-only universe using a pre-frozen rule."
  }
}
```

---

## 12. Rejection-Code Vocabulary (DH3-R11)

**Recommendation: UNCHANGED from D-H1**

Closed list, every entry grounded in existing authority:

```
PROVENANCE_INVALID
CHECKSUM_UNSTABLE
ALREADY_SEEN
OVERLAPS_DH0
OVERLAPS_DH1
OVERLAPS_DH2
SPAN_INSUFFICIENT
SCHEMA_INCOMPATIBLE
RETENTION_NOT_PERMITTED
SOURCE_UNAVAILABLE
TEMPORAL_DISTANCE_INSUFFICIENT
```

**Additions for H3 only:**
- `OVERLAPS_DH1` — candidate overlaps with D-H1 window
- `OVERLAPS_DH2` — candidate overlaps with D-H2 window
- `TEMPORAL_DISTANCE_INSUFFICIENT` — DH3-R5 backstop not satisfied

**Permanently excluded:**
- ❌ `TOO_FEW_TRIGGERS`
- ❌ `BORING_PERIOD`
- ❌ `BAD_RETURN`
- ❌ `GOOD_RETURN`
- ❌ `INCONCLUSIVE_RESULT`
- ❌ Any criterion phrased in terms of Strategy-D expected behavior

---

## 13. All-Tiers-Failed Behavior (DH3-R15) — FAIL-CLOSED

**Recommendation: UNCHANGED from D-H1**

If Options A, B, C, and D **all** fail objective eligibility tests (including DH3-R5's temporal-distance backstop and Option D's three-candidate cap):

```
RESULT: D-H3 BLOCKED — NO ELIGIBLE INPUT
ACTION: Return to Owner Review
```

**Explicit prohibition:**
- ❌ No criterion is weakened to force a result
- ❌ No temporal-distance rule is shortened
- ❌ No window-length rule is violated
- ❌ No continuity threshold is reduced
- ❌ No new instrument is introduced without formal authority

The protocol's cost-sensitive fallback (A → B → C → D) expresses Owner's priorities. Exhausting it is not a failure of the policy; it is the policy working as designed.

---

## 14. Strategy-D Freeze Requirement

**Before H3 selection is eventually executed, Strategy D must remain identical to the version tested in H1/H2.**

Explicit preservation:

```
If Strategy D changes before H3 execution:
  H3 authorization becomes invalid for that modified strategy.

A changed D requires:
  1. New versioned hypothesis
  2. New semantic freeze
  3. New validation chain
  
Do NOT silently treat a modified D as the same Strategy D.
```

**Current state:** Strategy D (commit `5a3f54a`, semantics `62c5c42`) is unchanged since H1/H2.

---

## 15. B-vs-D Scope and Future Comparison Boundary

### 15.1 H3 Execution Precedent

H3's primary purpose is Strategy-D mechanical validation. The question of whether Strategy B should also be executed on H3 is separate.

**Recommended:** Execute H3 window selection and Strategy D independently, following the same staged precedent used by H1/H2:

1. **Phase 1:** H3 window selection (this protocol)
2. **Phase 2:** Strategy D execution on H3 (separate authorization)
3. **Phase 3 (future, conditional):** Strategy B comparison analysis (separate authorization, only if deemed valuable after H3-D result is known)

**This protocol does NOT authorize Strategy-B execution.** Any future H3 B-vs-D comparison requires separate Owner decision.

### 15.2 Future Boundary Clarification

The question of whether H1/H2/H3 results will inform a final cross-window B-vs-D synthesis (e.g., "across all three windows, how do the patterns look?") is outside this protocol's scope. That synthesis, if pursued, must occur only after all H3 results are preserved and would require additional Owner authorization for its own contamination-risk mitigation.

---

## 16. Economic Evaluation Boundary (DH3-R18)

**H3 window selection does NOT authorize:**
- ❌ Terminal valuation of Strategy D on H3
- ❌ FEV computation
- ❌ Return calculations (CAGR, XIRR)
- ❌ Risk metrics (Sharpe, volatility)
- ❌ B-vs-D economic comparison
- ❌ Statistical metrics or hypothesis tests
- ❌ Any conclusion about strategy performance

**Execution** of Strategy D on H3 and **valuation** are separate, later authorizations.

---

## 17. H3-Protocol Decision Matrix (DH3-P1 through DH3-P15)

| ID | Question | Recommended Disposition | Alternative(s) | Contamination Risk | Implementation Cost | Owner Approval Required? |
|---|---|---|---|---|---|---|
| **DH3-P1** | Reuse f025bbf or design new H3 algorithm? | REUSE with single modification (temporal-distance rule for multi-window exclusion) | Redesign from scratch | **HIGH** — new rule introduces new discretion surface | Low | **Yes, recommend reuse** |
| **DH3-P2** | Exclusion-set rule for H0/H1/H2 | Non-overlapping with all three windows + DH3-R5 temporal backstop | Exclude H0/H1 only; weaker temporal distance | **MEDIUM** — misses H2, less independent | Low | **Yes, require all three** |
| **DH3-P3** | Temporal-distance rule (DH3-R5) | **Approve: 1,825 days from D-H2_end OR 1,825 days after D-H0_end** | Fixed distance from mid-point; variable threshold | **MEDIUM** — OR condition allows forward-only window, which has less independence from D-H0 regime | Low | **Yes, approve as stated** |
| **DH3-P4** | Instrument preference hierarchy | NDXJPY > XNDXJPY > XNDXNNRJPY > bounded search | Randomize instrument selection; prefer cheaper alternative | **MEDIUM** — outcome-insensitive instrument choice differs; cheaper is legitimate but reusing prior hierarchy preserves construct consistency | Low | **Yes, maintain hierarchy** |
| **DH3-P5** | Window-length rule (DH3-R3) | **906 calendar days** (reuse D-H0 duration) | 24 months; 36 months; variable span | **NONE** — 906 is a pure calendar fact, outcome-independent | Low | **Approved (f025bbf)** |
| **DH3-P6** | Window-position rule (DH3-R4) | Earliest eligible window | Latest eligible; midpoint; seed-derived | **MEDIUM** — latest-eligible might favor a window approaching H0, affecting regime independence; earliest is simplest, zero-parameter | Low | **Yes, maintain earliest** |
| **DH3-P7** | Continuity rule (DH3-R6) | **0.90 weekday-count threshold** | ~252 trading days/year approx; variable | **NONE** — pure calendar arithmetic, outcome-independent | Low | **Approved (f025bbf)** |
| **DH3-P8** | Tier traversal (A → B → C → D) | Objective-failure-gated, reuse f025bbf §2 | Parallel evaluation; cost-first | **NONE** — reuses proven f025bbf framework | Low | **Approved (f025bbf)** |
| **DH3-P9** | Option-B ordering (if Tier B qualifies) | Construct > provenance > span > lexical, reuse f025bbf §8 | Provenance-first; span-first | **NONE** — reuses proven hierarchy | Low | **Approved (f025bbf)** |
| **DH3-P10** | Option-C rule (if Tier C qualifies) | Next observation after D-H0, + 906-day duration, no partial windows | Fixed calendar start date; allow partial window | **LOW** — Option C is a backup; next-observation-plus-duration is mechanical | Medium | **Approved (f025bbf)** |
| **DH3-P11** | Option-D bounded rule | Inherit MP-S-01…MP-S-08 + f025bbf's within-category ordering | Redesign tier-D selection | **NONE** — inherits frozen, already-proven framework | Medium | **Approved (f025bbf)** |
| **DH3-P12** | Freeze-before-reveal procedure | 9-step, metadata-only until step 9 (reuse f025bbf §13) | Full multi-worker blinding | **NONE** — lightweight blinding is approved; heavier is not needed | Low | **Approved (f025bbf)** |
| **DH3-P13** | Selection-trace schema | f025bbf's schema + addendum for multi-window context and known-results disclosure | Minimal trace; extensive trace | **NONE** — trace is documentation, not selection criterion | Low | **Yes, approve addendum** |
| **DH3-P14** | Rule-versioning consequence | New version required for pre-execution changes; post-selection changes invalidate the window (reuse f025bbf §15) | Allow minor changes | **MEDIUM** — strict versioning prevents silent rule drift; reuse maintains discipline | Low | **Approved (f025bbf)** |
| **DH3-P15** | All-tiers-failed behavior | `D-H3 BLOCKED — NO ELIGIBLE INPUT`, return to Owner Review | Weaken a criterion to force result | **HIGH** — weakening any criterion introduces outcome-dependence risk | Low | **Yes, maintain fail-closed** |

---

## 18. Unresolved Questions Requiring Owner Clarification

| Question | Impact | Status |
|---|---|---|
| **Q1:** Is the temporal-distance backstop (1,825 days from D-H2_end OR from D-H0_end) the correct dual-condition formulation, or should it require both conditions (AND)? | HIGH — an OR allows a forward-only window; an AND requires true historical distance | **Requires Owner Decision** |
| **Q2:** Does qualification-research data (XNDXJPY, XNDXNNRJPY, retained under S.2 undertaking) automatically qualify for a new bounded-release decision under Tier B, or does each require separate Owner authorization? | MEDIUM — affects Tier-B availability | **Requires Owner Decision** |
| **Q3:** If post-D-H0 published data exists (Option C), is it eligible even though it requires new external retrieval, or is the "already-held" principle a hard requirement? | LOW–MEDIUM — affects Tier-C availability | **Clarify existing policy (f8332a5 §5, DS-1)** |
| **Q4:** Should the H3 protocol artifact itself be tagged and treated as an approved rule-version, or remain a draft decision pending H3 window selection? | LOW — administrative | **Recommend: Tag upon Owner approval; H3 selection then executed under tagged protocol** |

---

## 19. What This Artifact Does

- ✓ Designs a deterministic H3 window-selection protocol
- ✓ Identifies one substantive modification to f025bbf (temporal-distance rule for multi-window exclusion)
- ✓ Reuses proven components from D-H1 (window length, positioning, tier traversal, freeze-before-reveal)
- ✓ Formalizes the multi-window exclusion set (D-H0, D-H1, D-H2)
- ✓ Documents known-results disclosure and anti-contamination requirements
- ✓ Defines selection-trace schema with multi-window context
- ✓ Identifies unresolved questions and escalation points

---

## 20. What This Artifact Does NOT Do

- ✗ Select H3
- ✗ Reveal a candidate window
- ✗ Inspect any candidate market values
- ✗ Retrieve new market data
- ✗ Execute Strategy D
- ✗ Execute Strategy B
- ✗ Rerun H1/H2
- ✗ Modify Strategy D, Strategy B, or Baseline
- ✗ Design Strategy E
- ✗ Choose a market regime
- ✗ Compute economic results
- ✗ Change qualification state

---

## 21. Verification of Current State

**Verified as of commit `aa41ab8`:**

- ✓ Strategy D (hypothesis `5a3f54a`, semantics `62c5c42`) unchanged since H1/H2
- ✓ sim/ directory unchanged, no strategy reruns
- ✓ Qualification state unchanged (O-4 PARTIAL, Phase 2 BLOCKED)
- ✓ D-H1 result (1985-01-31 → 1987-07-26) preserved
- ✓ D-H2 corrected result (1987-07-27 → 1990-01-18) preserved
- ✓ D-H2 B-vs-D results (funding compression, timing/acquisition-price attribution) preserved
- ✓ B-vs-D methodology (`bb028bb`) approved
- ✓ HEAD == origin/main

**Repository is the Single Source of Truth.**

---

## 22. Recommendation Summary

### For Owner Decision:

1. **Accept the D-H1-with-modification approach (DH3-P1):** Reuse f025bbf's proven framework with a single targeted change to the temporal-distance rule for multi-window exclusion, rather than designing a new algorithm.

2. **Approve DH3-R5 (temporal-distance rule):** Require H3 candidates to be either 1,825+ days before D-H2's end (backward) OR 1,825+ days after D-H0's end (forward), ensuring genuine temporal independence from all prior windows.

3. **Preserve fail-closed behavior (DH3-P15):** If no eligible candidate exists under the approved rules, block H3 and return to Owner Review rather than weakening any criterion.

4. **Clarify Q1, Q2, Q3:** Provide Owner guidance on the three unresolved questions (temporal-distance OR vs. AND, qualification-research eligibility, Option-C data-retrieval eligibility) before protocol execution.

5. **Approve selection-trace addendum (DH3-P13):** Add the multi-window exclusion context and known-results disclosure fields to the trace schema to document that H3 was selected with knowledge of H1/H2 results, using a mechanically applied rule.

### Next Steps:

**If Owner approves this protocol:**
1. Update artifact to "APPROVED BY OWNER DECISION" status
2. Commit and tag the approved protocol
3. **Do NOT select H3 in this task**
4. **Next task:** Execute the approved H3 selection protocol, freeze exactly one candidate window without inspecting price values, record selection trace, and stop for Owner review before Strategy D execution

**If Owner requires modifications:**
1. Return this draft for amendment
2. Document changes as a new protocol version (e.g., `_v2`)
3. Re-review after changes

---

---

## 23. Final Status and Preservation Declaration

**Status: APPROVED BY OWNER DECISION, 2026-08-15 — SELECTION PROTOCOL ONLY.**

**Approval Implementation:**

- ✓ **OD-H3-1 (Reuse f025bbf):** Existing frozen framework from commit `f025bbf` is preserved unchanged. All proven components (tier traversal, window length, positioning, continuity, freeze-before-reveal) are reused directly.

- ✓ **OD-H3-2 (Temporal-moat addendum):** DH3-R5 is formalized as an H3-specific extension to the pre-existing temporal-distance principle. It protects the entire consumed research region `[1985-01-31, 2020-06-26]` with a five-year moat on each side (OR logic). The addendum is explicitly disclosed as post-H1/H2 approved knowledge, but uses only the framework (1,825-day constant) and prior-window dates, not outcome knowledge.

- ✓ **OD-H3-3 (Remove Tier-A availability spans):** Concrete availability metadata (e.g., "approximately 1980-01-01 → 1985-01-30") have been removed. Tier-A eligibility is determined mechanically at future selection-execution time from authoritative metadata.

- ✓ **OD-H3-4 (Tier-B boundary):** Tier-B authority is limited to existing frozen policy. No new instrument permission is granted.

- ✓ **OD-H3-5 (Tier-C acquisition boundary):** Data acquisition is limited to existing frozen authority. Fail-closed if new retrieval is required.

- ✓ **OD-H3-6 (Preserve deterministic rules):** All existing frozen rules (906-day duration, earliest-eligible positioning, tier traversal, continuity, freeze-before-reveal) are preserved unchanged from f025bbf.

**Known-Results Disclosure:**

Before H3 selection execution, the research team already knows D-H1 and D-H2 results. This protocol explicitly discloses this chronology and ensures that no outcome knowledge enters the H3 selection function. The selection is a deterministic algorithm applied to metadata-only universe of previously-consumed windows.

**Confirmation Statements:**

- ✓ **H3 has NOT been selected.** No instrument chosen, no dates identified.
- ✓ **No candidate price values have been inspected.**
- ✓ **No new market data has been acquired.**
- ✓ **Strategy D has NOT been executed.**
- ✓ **Strategy B has NOT been executed.**
- ✓ **Strategy E has NOT been designed.**
- ✓ **Qualification state remains UNCHANGED.**
- ✓ **Strategy D remains frozen** (commit `5a3f54a`, semantics `62c5c42`).
- ✓ **sim/ directory remains unchanged**, no strategy reruns.

---

**END OF PROTOCOL DOCUMENT**

**Status: APPROVED BY OWNER DECISION, 2026-08-15.**

**Protocol is now preserved and frozen. The next task (H3 window selection execution) requires separate authorization and must follow this protocol exactly.**
