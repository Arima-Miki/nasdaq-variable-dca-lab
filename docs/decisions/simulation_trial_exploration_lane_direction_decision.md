# Simulation Trial — Research Direction Pivot: Exploration vs. Validation

**Status:** **APPROVED BY OWNER DECISION, 2026-08-15 — RESEARCH DIRECTION PIVOT.**

**Date:** 2026-08-15

**Owner approval:** 2026-08-15

---

## Owner Decision: Separate Exploration from Validation

The Owner establishes two distinct research lanes for immediate and future work:

### Lane 1: Exploration (Immediate)

**Scope:** Exploratory B-vs-D simulation using existing available project data.

**Purpose:** Understand Strategy B and Strategy D behavior, compare trigger timing, capital deployment, and terminal outcomes.

**Data:** Use only market data already available to the project (may overlap prior research windows D-H0, D-H1, D-H2).

**Strategy freeze:** Keep Strategy B and Strategy D fixed (do not modify to optimize exploratory results).

**Classification:** All exploratory findings labeled `EXPLORATORY — NOT INDEPENDENT VALIDATION EVIDENCE`.

**Use:** Exploratory results inform mechanism understanding and future hypotheses only. May NOT be used to claim independent validation, robustness, qualification, or Strategy D adoption.

### Lane 2: Validation (Deferred)

**H3 independent-window selection:** Remains frozen, deferred, and blocked under currently authorized data.

**H3 protocol:** Unchanged (DH3-R3, DH3-R5, DH3-R6, tier hierarchy immutable).

**H3 status:** UNSELECTED. Available for future independent validation when new Owner authorization provides eligible data.

**No H3 modifications:** Do not weaken DH3-R5, do not select H3, do not acquire external market data for H3 in this work phase.

**External H3 data search:** Discontinued. Availability study findings (BEFORE-side impossible, AFTER-side incomplete until 2027-12-18) recorded in draft research artifact only.

---

## Scope Boundaries

### Exploration Lane — What IS Permitted

- ✓ Reuse D-H0, D-H1, D-H2 data for new exploratory simulations
- ✓ Compare Strategy B and Strategy D behavior on existing data
- ✓ Analyze trigger timing, capital consumption, terminal outcomes
- ✓ Generate hypotheses for future research
- ✓ Identify regime-dependent behavior patterns

### Exploration Lane — What IS NOT Permitted

- ✗ Claim independent validation from overlapping-window results
- ✗ Modify Strategy B or Strategy D to improve exploratory metrics
- ✗ Design Strategy E in this task
- ✗ Use exploratory results to justify qualification or adoption
- ✗ Weaken any frozen validation criterion

### H3 Validation Lane — Deferred

- ✗ No H3 selection
- ✗ No external market data retrieval
- ✗ No H3 protocol modification
- ✗ No continued H3 availability research
- ✗ Future task only, when new Owner authorization makes H3 eligible

---

## Qualification State (Unchanged)

- ✓ O-4 Primary Proxy remains: PARTIAL
- ✓ Phase 2 remains: BLOCKED
- ✓ H3 status remains: UNSELECTED
- ✓ No qualification implications from exploratory research

---

## Prior Artifacts and Work

### H3 Availability Study Draft

An external-data availability study (docs/research/simulation_trial_strategy_d_dh3_external_data_availability_study.md) was prepared as a draft to explore whether external Nasdaq-100 data could satisfy the frozen H3 protocol.

**Findings (summary):**
- BEFORE-side: Structurally impossible (Nasdaq-100 launched 1985-01-31; boundary is 1980-02-02)
- AFTER-side: Not yet possible (data required through 2027-12-18; currently available through 2026-07-10)

**Status:** DRAFT only, not committed, not authoritative.

**Disposition:** Discarded (not committed to repository). Findings available for reference if H3 feasibility is revisited in late 2027.

---

## Strategy Freeze Verification

**Confirmed unchanged:**
- ✓ Strategy D hypothesis (commit 5a3f54a)
- ✓ Strategy D semantics (commit 62c5c42)
- ✓ Strategy B (unchanged since prior approval)
- ✓ sim/ directory (no strategy modifications)
- ✓ No simulation reruns executed

---

## Next Task Specification

### Immediate Task (Approved)

> **RUN EXPLORATORY B-vs-D SIMULATIONS USING EXISTING AVAILABLE DATA**

**Scope:** Simulate both Strategy B and Strategy D on D-H0, D-H1, and/or D-H2 windows using existing held data. Compare behavior, outcomes, and mechanisms.

**Classification:** All results labeled EXPLORATORY (not independent validation).

**Execution:** Separate task; not started in this preservation task.

**No methodology pre-specification:** Execution details (window selection, metric definitions, output format) decided pragmatically during simulation task.

---

## Preservation Integrity

This decision artifact preserves:
- ✓ Separation of exploration and validation research lanes
- ✓ H3 deferral and freeze
- ✓ Existing frozen protocols unchanged
- ✓ Qualification state unchanged
- ✓ Strategy B/D fixed initially
- ✓ Minimum governance boundary around exploratory work

---

**Status: APPROVED BY OWNER DECISION, 2026-08-15.**

**Next authorized task: RUN EXPLORATORY B-vs-D SIMULATIONS USING EXISTING AVAILABLE DATA.**

**Do not begin exploratory simulations in this task.**

---

**END OF DECISION ARTIFACT**
