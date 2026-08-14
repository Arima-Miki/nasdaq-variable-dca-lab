# Simulation Trial — Strategy D Stage D-H2: Input Provenance Remediation Decision

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** Remedial acceptance of canonical execution representation following discovery of authorization-gap defect in original process.

**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling prior artifact:** D-H2 bounded-release decision `039be52` · tag `simulation-trial-strategy-d-dh2-bounded-release-20260814`
**Controlling prior evidence:** MP-DH2-D-001 preserved mechanical result, commit `023a40157a8c671c34bbb260628c1d07fff4c10f` · tag `simulation-trial-strategy-d-dh2-mechanical-result-20260814`

---

## 1. Defect Discovered Before A/B/C Execution

**Defect Classification:** DH2-INTEGRITY-C + DH2-INTEGRITY-B

Before executing Strategies A, B, C on the frozen D-H2 input, an integrity audit (conducted 2026-08-14) discovered:

### DH2-INTEGRITY-C — Execution-Authority Defect

The bounded-release decision (§8) froze:

**SOURCE REPRESENTATION (Raw Nasdaq-derived bytes):**
- File: `DH2_NDXJPY_1987-07-27_1990-01-18.csv`
- SHA-256: `992a40e39b5ec0c037ad2b547e3e78c911c01943cbf68596a67f653827fe654c`

However, the preserved Strategy-D execution (`MP-DH2-D-001`) actually consumed:

**CANONICAL EXECUTION REPRESENTATION (Simulator-compatible bytes):**
- File: `DH2_NDXJPY_1987-07-27_1990-01-18_clean.csv`
- SHA-256: `d8089b919778a82b25cee6072c38079f1ab52303fa0d171a802272cec38c9c6f`

**The defect:** A deterministic CSV schema-canonicalization step occurred between source freezing and Strategy-D execution **without that transformation being explicitly authorized and recorded as a separate execution representation by the release decision**.

This represents an authority gap: the bounded-release decision did not state that a preprocessing step would occur, and no separate authorization artifact approved the canonical representation before execution.

### DH2-INTEGRITY-B — Evidence/Provenance Defect

The preserved manifest for `MP-DH2-D-001` truthfully records the actual consumed file path (`input_file: "...DH2_NDXJPY_1987-07-27_1990-01-18_clean.csv"`) but fails to record the SHA-256 checksum of the consumed bytes. This creates evidentiary ambiguity.

---

## 2. Integrity Audit Finding

A complete structural comparison (2026-08-14) independently established:

| Property | Result |
|----------|--------|
| Observation count | 629 in both raw and canonical |
| Date sequence | Identical, sorted order preserved |
| All 629 numeric values | Bit-for-bit identical (digit-for-digit) |
| Row ordering | Preserved |
| Dropped observations | None |
| Added observations | None |
| Numeric transformation | None — values unchanged |
| Column transformation | `Date` → `date`, `NDXJPY` → `close` |
| Disclaimer row removal | Yes — non-data header dropped |
| No interpolation or rounding | Confirmed |
| Determinism | Transformation is deterministic and reproducible |

**Audit conclusion:** The canonical representation contains exactly the same 629 ordered observations and numeric values as the source representation. No data corruption, no value loss, no reordering occurred.

---

## 3. Root Cause: Schema Compatibility Requirement

The simulator's CSV loader contract (§18.4.9 / `sim/engine/csv_loader.py`) requires:

1. Header row with recognized column names: `date`/`close` or acceptable aliases
2. Data rows as date,value pairs with no extraneous header material

The raw Nasdaq source file contains:

1. A Nasdaq disclaimer row in the header position (non-data material)
2. Column names `Date` and `NDXJPY` (not in the loader's alias set)
3. Two trailing empty columns (disclaimer carrier artifacts)

**The mismatch:** The raw source representation is mechanically incompatible with the simulator's loader contract, despite containing all required observational data.

**The transformation:** The canonical representation removes the disclaimer row and applies standard column naming (`date`, `close`), producing a loader-compatible file that preserves every observation and value.

---

## 4. Historical Precedent: D-H1 Handled the Same Pattern

The D-H1 extraction and execution process (preserved in `simulation-trial-mode-p/PROVENANCE.md`, lines 233–237) explicitly documented a parallel canonicalization step:

> "Extraction procedure: Mechanical column/row extraction only... **the `Date` and `NDXJPY` columns retained verbatim... the two trailing empty quoted columns (disclaimer-carrier artifacts of the source format, identical and empty in every data row) dropped; header rewritten to `date,close` — both accepted column aliases in `sim/engine/csv_loader.py` — for loader ingestion. No value was altered, computed, interpolated, reordered, or filled.**"

**Critical difference:** D-H1 preprocessing was explicitly documented in the extraction PROVENANCE before the mechanical run occurred. D-H2 preprocessing was not.

---

## 5. Owner Remediation Decision

The Owner accepts the findings and approves the following remediation:

### A. Accept Canonical Representation as D-H2 Execution Standard

The canonical `_clean.csv` representation (SHA-256 `d8089b9...`) is henceforth the frozen, immutable execution representation for all D-H2 work.

**This acceptance:**
- Does NOT retroactively erase DH2-INTEGRITY-C or DH2-INTEGRITY-B
- DOES remedially authorize use of `_clean.csv` for the remainder of D-H2
- DOES establish prospective governance: all future D-H2 executions must use exactly this file

### B. Preserve MP-DH2-D-001 Without Rerun

Strategy D is NOT rerun. The existing `MP-DH2-D-001` evidence remains preserved as executed.

**Disposition:** Mechanically valid but originally recorded with an undisclosed authorization gap. The mechanical output (event log, terminal state, invariants) is correct because exact observation-level equivalence with the source has been independently verified.

### C. Two-Level Provenance Model for D-H2

Formally distinguish and record:

**LEVEL 1: SOURCE REPRESENTATION**
- Identity: `DH2_NDXJPY_1987-07-27_1990-01-18.csv`
- SHA-256: `992a40e39b5ec0c037ad2b547e3e78c911c01943cbf68596a67f653827fe654c`
- Relationship to Nasdaq: Direct extraction from Nasdaq `AdditionalData_NDXJPY.csv`
- Status: Frozen by bounded-release decision; source of truth for observation selection

**LEVEL 2: CANONICAL EXECUTION REPRESENTATION**
- Identity: `DH2_NDXJPY_1987-07-27_1990-01-18_clean.csv`
- SHA-256: `d8089b919778a82b25cee6072c38079f1ab52303fa0d171a802272cec38c9c6f`
- Transformation: Deterministic schema canonicalization (disclaimer removal + column renaming)
- Status: Frozen by this remediation decision; canonical input for all D-H2 executions
- Verification: Observation-level equivalence independently confirmed; no data loss

### D. Future D-H2 Execution Rule

**All subsequent D-H2 Strategy A/B/C executions MUST:**

1. Consume exactly: `DH2_NDXJPY_1987-07-27_1990-01-18_clean.csv`
2. Match exactly: SHA-256 `d8089b919778a82b25cee6072c38079f1ab52303fa0d171a802272cec38c9c6f`
3. Perform NO regeneration, recanonicalization, modification, or alternate parsing
4. Record the canonical input SHA-256 in every execution manifest
5. Reference this remediation decision in execution provenance

**Prohibited:**
- Using the raw file directly (loader incompatible)
- Regenerating `_clean.csv` (would create a new representation with different bytes)
- Creating alternate clean files
- Parsing the raw file with a loader workaround (breaks provenance chain)

---

## 6. Qualification-State Preservation

**Unchanged:**
- All `P1-x` open items remain OPEN
- All `M-x` open items remain OPEN
- `O-4` remains PARTIAL
- `HG-8` remains NOT EVALUABLE
- Primary Proxy: **NOT SELECTED**
- Stage G: OPEN
- Stage H: NOT BEGUN
- Phase 2: **BLOCKED**

**This remediation decision does not constitute qualification evidence, does not modify any qualification artifact, and does not alter the Frozen Baseline.**

---

## 7. Scope

This artifact resolves the D-H2 input authorization and provenance defect only.

It does NOT:
- Rerun Strategy D
- Execute Strategies A/B/C (separate authorization required)
- Compute or rank economic metrics
- Modify any strategy logic
- Change qualification-lane state
- Alter prior preserved artifacts (D-H0, D-H1, D-H2 bounded-release, D-H2 mechanical-result remain exactly as preserved)

---

## 8. Next Decision Required

The minimum Owner decision now required is whether to execute Strategies A/B/C mechanically on the now-frozen canonical D-H2 execution representation (SHA-256 `d8089b9...`), using the existing preserved MP-DH2-D-001 result without rerun, for the purpose of an A/B/C/D economic comparison that remains simulation-trial-only and non-promotional.

This artifact does not authorize that execution and makes no recommendation. It resolves the input-provenance defect only.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. Input provenance remediation only. Authorization gap disclosed and remedially accepted. Source and canonical representations formally distinguished. MP-DH2-D-001 preserved unchanged. No strategy execution. No qualification-state change. No data corruption. No prior artifact rewritten.**
