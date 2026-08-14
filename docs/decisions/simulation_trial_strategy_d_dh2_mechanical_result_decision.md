# Simulation Trial — Strategy D Stage D-H2: Mechanical-Result Preservation Checkpoint

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** Preserves the mechanical-execution checkpoint
only. **Does not** claim economic superiority, adoption, statistical validation, robustness, or
qualification evidence (§4).
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling D-H2 authorization:** `3c687c80e2ec51f63e3fd2c9a98af0f320578baf` (commit
`3c687c8`) · tag `simulation-trial-strategy-d-dh2-authorization-20260814`
**Controlling D-H2 bounded-release decision:** `039be52d29e3e25b9c8264c3d2a0e59ac012b666` (commit
`039be52`) · tag `simulation-trial-strategy-d-dh2-bounded-release-20260814`
**Controlling D-H2 deterministic selection rule:** `f025bbf0dd5df9a4b037936822b1ced4e263948c`
**Controlling Strategy-D authority:** hypothesis `5a3f54a` · semantics `62c5c42` · Mode-E E5
`f16a815` · D-H0 `486b994`

This artifact does **not** reproduce the event log or full evidence body — those remain in
the external, non-git evidence store, referenced here by run ID and checksum (§2).

---

## 1. What is preserved

The completed mechanical-execution checkpoint for run `MP-DH2-D-001`: Strategy D's preserved,
unmodified implementation and semantics, executed exactly once against the deterministically-selected,
bounded-released D-H2 input (`NDXJPY`, `1987-07-27 → 1990-01-18`), without any economic metric being
computed, and without Strategies A, B, or C being run.

## 2. External evidence reference (not copied into git)

| Field | Value |
| --- | --- |
| Run ID | `MP-DH2-D-001` |
| Evidence store | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-p/MP-DH2-D-001/` |
| `manifest.json` sha256 | `166040f625192837d201288bc37a2bc60a0bc6f63eeec517afe6e30a8ca33be5` |
| `event_log.json` sha256 | `45a7a7502e6cc51ad115090202ac5988676152a8aff4f954385533a1044d892a` |
| `terminal_state.json` sha256 | `2332c299718646e078854e871d2d67127b813429ae8bc105f606226d56821c06` |
| Input dataset CSV | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh2-selection/dataset/DH2_NDXJPY_1987-07-27_1990-01-18_clean.csv` |
| Input CSV sha256 | `992a40e39b5ec0c037ad2b547e3e78c911c01943cbf68596a67f653827fe654c` |
| Store `PROVENANCE.md` | Updated additively with "Mechanical Execution D-H2" section; prior generations (`D-H0`, `D-H1`, `DH1-D1`) unmodified |
| Determinism | Verified: two independent executions produced byte-identical `event_log.json`/`terminal_state.json` |

## 3. Mechanical quantities (independently re-verified against the raw evidence)

| Quantity | Value |
| --- | --- |
| Observations | `629` |
| Allocations committed | `0` |
| Suppressions | `0` |
| Zero-cap events | `0` |
| Positive-partial-cap events | `0` |
| Commitments | `0` |
| Reservations outstanding | `0` |
| Executions | `0` |
| Exposure units held | `0` |
| cash_granted_jpy | `480,000.0` |
| budget_units_granted | `48.0` |
| all_invariants_pass | `true` — 20 applicable invariants, all pass; INV-9-D both clauses pass; ENG-D1…ENG-D5 all pass |
| Governed economic metric present anywhere in output | **None** — verified absent |

## 4. Claim boundary — this is the entire permitted claim

> Strategy D completed one deterministic mechanical execution on the frozen D-H2 input without
> mechanical or invariant failure. The natural execution path produced zero allocations.

**This artifact does not claim, state, or imply**: economic success or failure; superiority or
inferiority to Strategy A, B, or C; that the zero-allocation result indicates weakness, strength, or
anything other than what occurred (no Normal-zone or Large-drop-zone triggers in this window); that
Strategy D should be modified; robustness; generalization beyond this one window; statistical
validation; or adoption. None of these follow from the mechanical result above, and none are asserted here.

## 5. Qualification-state preservation

Unchanged: `O-4`, `P1-x`, `M-x`, `HG-8`, Primary Proxy, Stage G, Stage H. **Phase 2 remains BLOCKED.**
This checkpoint is not qualification evidence and does not resolve any `P1-x`/`M-x` item.

## 6. Scope

This artifact preserves a checkpoint reference only. It does not modify the Frozen Baseline, Strategy
D's implementation or semantics, the D-H2 policy/rule/release/selection chain, any qualification
artifact, or any prior evidence generation. It does not authorize, and should not be read as
authorizing, economic evaluation, an A/B/C run on D-H2, another Strategy-D validation window, Strategy
D modification, Strategy E work, or any further Strategy-D investigation stage — those remain separate,
not-yet-made Owner decisions (§7).

## 7. Next decision required (not made here)

The minimum Owner decision now required is which of the following becomes the next research question:
(1) whether to execute A/B/C mechanically on the same D-H2 input for an A/B/C/D economic comparison;
(2) another independent-validation stage for Strategy D; (3) stopping Strategy-D investigation at this
mechanical checkpoint; or (4) beginning Strategy E research. This artifact makes no recommendation
among them and authorizes none.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. Mechanical-result checkpoint only.
No economic claim. No A/B/C execution. No qualification-state change. No Strategy-D modification.
`f025bbf`, `3c687c8`, `039be52`, and every preserved Strategy-D and Mode-P evidence generation are
unchanged.**
