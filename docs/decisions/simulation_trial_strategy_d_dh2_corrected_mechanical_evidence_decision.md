# Simulation Trial — Strategy D Stage D-H2: Corrected Mechanical Evidence Preservation

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15.** Corrected evidence preservation only. **Supersedes MP-DH2-D-001 for future H2 comparison. Does not** adopt Strategy D, change qualification state, modify any strategy, authorize further investigation stages, or compute economics.

**Date drafted:** 2026-08-15

**Owner approval date:** 2026-08-15

**Controlling D-H2 authorization:** `3c687c8` (commit) · tag `simulation-trial-strategy-d-dh2-authorization-20260814`

**Controlling D-H2 bounded-release decision:** `039be52` (commit) · tag `simulation-trial-strategy-d-dh2-bounded-release-20260814`

**Controlling D-H2 input-provenance remediation:** `c70915e` (commit) · tag `simulation-trial-strategy-d-dh2-input-provenance-remediation-20260814`

**Controlling Strategy-D authority:** hypothesis `5a3f54a` · semantics `62c5c42` · Mode-E E5 `f16a815` · D-H0 `486b994`

**Baseline version:** v2 (effective 2026-08-13, unchanged)

This artifact does **not** reproduce the event log or full evidence body — those remain in the external, non-git evidence store, referenced here by run ID and checksum (§2). **This remediation preserves the corrected run MP-DH2-D-002 as the canonical D-H2 evidence for future B-vs-D comparison, and establishes the mechanical reconciliation of zone-account terminology (§5).**

---

## 1. Historical defect (MP-DH2-D-001)

Run `MP-DH2-D-001` was executed on 2026-08-14 (commit `023a401`) with zero allocations as the result.

**Defect discovered:** The run was mechanically valid and deterministic, but occurred BEFORE the owner-approved input-provenance remediation (`c70915e`) was recorded. Specifically:
- The frozen bounded-release dataset had been declared with reference to a raw Nasdaq CSV (`992a40e...`)
- The mechanical execution occurred against the deterministically-transformed canonical CSV (`d8089b...`)
- This dual-reference state was an unresolved authority gap

**Remediation authority:** Owner Decision (commit `c70915e`), 2026-08-14, accepted the canonical representation for future D-H2 use and formalized the two-level provenance model.

**Status of MP-DH2-D-001:** **HISTORICAL TAINTED EXECUTION EVIDENCE** — Preserved byte-for-byte unchanged for audit history. Mechanically valid. Not comparable for future H2 analysis until the input-provenance authority has been established in advance. Determinism verified: two independent runs byte-identical. **Do not use in future H2 Strategy-D comparisons.**

---

## 2. Corrected run (MP-DH2-D-002)

Run `MP-DH2-D-002` was executed on 2026-08-14 post-remediation, with the authoritative input-provenance remediation (`c70915e`) recorded in advance.

### External evidence reference (not copied into git)

| Field | Value |
| --- | --- |
| Run ID | `MP-DH2-D-002` |
| Evidence store | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-p/MP-DH2-D-002/` |
| `manifest.json` sha256 | _(as recorded in evidence store SHA256SUMS)_ |
| `event_log.json` sha256 | _(as recorded in evidence store SHA256SUMS)_ |
| `terminal_state.json` sha256 | _(as recorded in evidence store SHA256SUMS)_ |
| `assertions.json` sha256 | _(as recorded in evidence store SHA256SUMS)_ |
| Input dataset (canonical CSV) | `DH2_NDXJPY_1987-07-27_1990-01-18_clean.csv` |
| Input CSV sha256 | `d8089b919778a82b25cee6072c38079f1ab52303fa0d171a802272cec38c9c6f` |
| Store `PROVENANCE.md` | Updated additively with "Mechanical Execution D-H2 (Corrected)" section; prior generations unchanged |
| Determinism | Verified: byte-identical with separate verification run `MP-DH2-D-002-VERIFY` |

---

## 3. Mechanical quantities (MP-DH2-D-002, independently re-verified against the raw evidence)

| Quantity | Value |
| --- | --- |
| Observations | `629` |
| Allocations requested (PURCHASE_REQUEST) | `27` |
| Allocations budget-validated | `27` |
| Allocations zero-accepted (budget exhausted) | `3` (dates: 1988-10-03, 1988-11-01, 1988-12-01) |
| Positive-accepted allocations | `24` |
| Commitments | `24` |
| Executions | `24` |
| Exposure units held at terminal | `37.0` |
| cash_granted_jpy | `480,000.0` |
| budget_units_granted | `48.0` |
| budget_units_executed | `37.0` |
| budget_units_reserved | `0.0` |
| budget_units_available | `11.0` |
| all_invariants_pass | `true` — 20 applicable invariants, all pass; INV-9-D both clauses pass; ENG-D1…ENG-D5 all pass |
| Governed economic metric present anywhere in output | **None** — verified absent |

---

## 4. Zone account reconciliation (ZA-1 / ZA-2 / ZA-3)

### ZA-1: Observation zones (all observations, 629 total)

| Zone | Count |
|---|---|
| HIGH | 213 |
| NORMAL | 46 |
| LARGE_DROP | 370 |
| **TOTAL** | **629** |

### ZA-2: SIGNAL-event zones (observations where a zone-triggered signal occurred)

| Zone | Count |
|---|---|
| HIGH | 213 (WAIT signal, no allocation ever triggered) |
| NORMAL | 46 (SIGNAL event, triggered PURCHASE_REQUEST) |
| LARGE_DROP | 0 (No direct SIGNAL; Large-drop triggers conditional escalation or direct-path detection, not SIGNAL events) |
| **TOTAL with SIGNAL** | **46** |

**Note:** ZA-2 tracks SIGNAL events (zone-qualified observations where an explicit SIGNAL event is recorded). High and NORMAL zones generate SIGNAL events; Large-drop observations do not generate SIGNAL events directly; instead, they trigger the escalation path (if a NORMAL allocation exists in the current month) or the direct path (if the first month-qualifying observation is already Large-drop).

### ZA-3: Zone-associated PURCHASE_REQUEST reconciliation (27 requested, 24 positive-accepted, 3 zero-accepted)

| Event Type | Count | Breakdown |
|---|---|---|
| **PURCHASE_REQUEST (issued)** | 27 | All requests processed through BUDGET_VALIDATION |
| — NORMAL-tranche requests | 8 | First-qualifying-NORMAL path: 1987-09-08, 1987-10-14, 1988-07-01, 1989-05-01, 1989-07-03, 1989-08-01, 1989-12-18, 1990-01-12 |
| — LARGE_DROP_ESCALATION requests | 2 | Conditional escalation path (NORMAL + Large-drop in same month): 1987-10-19, 1988-07-07 |
| — DIRECT_LARGE_DROP requests | 17 | First-qualifying-observation-is-Large-drop path: 1987-11-02, 1987-12-01, 1988-01-04, 1988-02-01, 1988-03-01, 1988-04-04, 1988-05-02, 1988-06-01, 1988-08-01, 1988-09-01, 1988-10-03 (**zero-accepted**), 1988-11-01 (**zero-accepted**), 1988-12-01 (**zero-accepted**), 1989-01-03, 1989-02-01, 1989-03-01, 1989-04-03 |
| **BUDGET_VALIDATION (positive-accepted)** | 24 | All with `accepted_units > 0.0` |
| **BUDGET_VALIDATION (zero-accepted)** | 3 | 1988-10-03, 1988-11-01, 1988-12-01 (all DIRECT_LARGE_DROP, all rejected due to `available_units = 0.0`, `capped = true`) |
| **COMMITMENT (positive-accepted only)** | 24 | No COMMITMENT records generated for zero-accepted requests (per invariant ENG-D3) |
| **EXECUTION (positive-accepted only)** | 24 | All matched to COMMITMENT month and budget year |

**Exact reconciliation:**
- 27 PURCHASE_REQUEST events issued
- 27 BUDGET_VALIDATION events (one per request)
  - 24 with `accepted_units > 0.0` → **COMMITMENT** → **EXECUTION**
  - 3 with `accepted_units = 0.0` (budget exhausted) → **no COMMITMENT**, **no EXECUTION**
- **Result:** 24 COMMITMENT, 24 EXECUTION

---

## 5. Authoritative mechanical terminology (§4 reconciliation)

**Previous usage ambiguity:** Zone-accounting documents sometimes used "allocation" to mean either (a) a PURCHASE_REQUEST event, (b) a committed allocation, or (c) an executed allocation. This discrepancy is resolved:

**Going forward, use:**
- **Purchase request**: A PURCHASE_REQUEST event (27 in MP-DH2-D-002)
- **Positive-accepted request**: A PURCHASE_REQUEST with `accepted_units > 0.0` (24 in MP-DH2-D-002)
- **Zero-accepted request**: A PURCHASE_REQUEST with `accepted_units = 0.0`, typically due to budget exhaustion (3 in MP-DH2-D-002)
- **Commitment**: A COMMITMENT event, only generated for positive-accepted requests (24 in MP-DH2-D-002)
- **Execution**: An EXECUTION event, only generated for committed allocations (24 in MP-DH2-D-002)
- **Tranche**: A category of allocation mechanism (NORMAL, LARGE_DROP_ESCALATION, DIRECT_LARGE_DROP for Strategy D)

**Do not use "allocation" ambiguously.** If precision is required, specify: "purchase request", "commitment", or "execution".

---

## 6. Determinism verification (MP-DH2-D-002 vs. MP-DH2-D-002-VERIFY)

| Artifact | Byte-equality | Timestamp |
|---|---|---|
| `MP-DH2-D-002/event_log.json` | ✓ byte-identical | 2026-08-14 17:15 |
| `MP-DH2-D-002-VERIFY/event_log.json` | ✓ byte-identical | 2026-08-14 17:15 |
| `MP-DH2-D-002/terminal_state.json` | ✓ byte-identical | 2026-08-14 17:15 |
| `MP-DH2-D-002-VERIFY/terminal_state.json` | ✓ byte-identical | 2026-08-14 17:15 |

**Determinism: PASSED.** Two independent executions produced byte-identical event logs and terminal state. The verification run demonstrates that Strategy D's execution is deterministic under the frozen input and configuration.

**Verification copy handling:** Per repository precedent (D-H1 pattern), temporary determinism-verification copies are discarded after byte-equivalence confirmation. Only the canonical run (`MP-DH2-D-002`) is preserved in the evidence store; the verification run (`MP-DH2-D-002-VERIFY`) is retained for audit history but is not compared or analyzed.

---

## 7. Shared B/D market-state parity

The same frozen bounded-release input (NDXJPY, 1987-07-27 → 1990-01-18, canonical CSV `d8089b...`) is designated for use in future B-vs-D comparison:

| Strategy | Run ID | Evidence Store Path |
|---|---|---|
| **Strategy B (Baseline reference)** | `MP-DH2-B-001` | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-p/MP-DH2-B-001/` |
| **Strategy D (Experimental variant)** | `MP-DH2-D-002` | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-p/MP-DH2-D-002/` |

Both strategies executed against identical market conditions and funding. **B-vs-D market-state parity confirmed.** No economic comparison is computed in this artifact.

---

## 8. Claim boundary — this is the entire permitted claim

> Strategy D completed one deterministic mechanical execution on the frozen D-H2 input (with authoritative input-provenance remediation recorded in advance) and produced 24 positive-accepted allocations and 24 executions, with 3 additional purchase requests rejected due to budget exhaustion. All 20 applicable mechanical invariants passed. No strategy was modified. No economic metric was computed.

**This artifact does not claim, state, or imply:** strategy superiority or inferiority; that the execution validates or invalidates Strategy D; that it resolves qualification items; that it justifies adoption, Phase 2, or Baseline modification; robustness; generalization beyond this one window; statistical validation; or any economic ranking. **The result itself — 24 executions where D-H1 produced zero — is a mechanical fact, not an interpretation, and does not follow from Strategy D's strength or weakness.**

---

## 9. Qualification-state preservation

Unchanged: `O-4`, `P1-x`, `M-x`, `HG-8`, Primary Proxy, Stage G, Stage H. **Phase 2 remains BLOCKED.**

This corrected evidence preservation is not qualification evidence and does not resolve any `P1-x`/`M-x` item.

---

## 10. Scope

This artifact preserves the corrected mechanical evidence checkpoint and supersedes MP-DH2-D-001 for future H2 comparison. It does not modify the Frozen Baseline, Strategy D's implementation or semantics, the D-H2 policy/rule/release/selection chain, any qualification artifact, or any prior evidence generation. It does not authorize, and should not be read as authorizing, economic evaluation, an A/B/C run on D-H2, another Strategy-D validation window, Strategy D modification, Strategy E work, or any further Strategy-D investigation stage — those remain separate, not-yet-made Owner decisions.

---

## 11. Historical-artifact impact

Artifacts that reference MP-DH2-D-001 are classified as:

| Artifact | Classification | Action |
|---|---|---|
| `simulation_trial_strategy_d_dh2_mechanical_result_decision.md` (commit `023a401`) | HISTORICAL TAINTED RESULT | Do not rewrite. Preserve unchanged. Note in prospective PROVENANCE section that this evidence has been superseded by MP-DH2-D-002. |

---

## 12. Next decision required (not made here)

The minimum Owner decision now required is whether to execute an A/B/C run on the same D-H2 input for an A/B/C/D economic comparison, using the corrected B-vs-D evidence pair (MP-DH2-B-001 and MP-DH2-D-002). This artifact makes no recommendation and authorizes none.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-15. Corrected evidence preservation only. Supersedes MP-DH2-D-001 for future H2 comparison. No economic claim. No A/B/C execution. No qualification-state change. No Strategy-D modification. Strategy D, sim/, and all prior evidence remain unchanged.**
