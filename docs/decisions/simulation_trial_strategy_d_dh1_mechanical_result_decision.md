# Simulation Trial — Strategy D Stage D-H1: Mechanical-Result Preservation Checkpoint

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** Preserves the mechanical-execution checkpoint
only. **Does not** claim economic superiority, adoption, statistical validation, robustness, or
qualification evidence (§4).
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling D-H1 policy:** `f8332a543f7bab4c8b5f42974813ccd70be9137f`
**Controlling D-H1 deterministic selection rule:** `f025bbf0dd5df9a4b037936822b1ced4e263948c`
**Controlling D-H1 bounded-release decision:** `b722fb27ada370cf1adf22f6a8e5a99331a9a705`
**Strategy-D implementation/semantic authority:** hypothesis `5a3f54ab11a1de8204cae659ad2732867e7d1274` ·
semantics `62c5c429ce6aa4742c6327a9c39687421fd94325` · Mode-E E5 `f16a815d4fc64706247e5ac63e8449857dd58643` ·
D-H0 mechanical validation `486b9940b032f89c66398ed70a73ae5c1f674644`

This artifact does **not** reproduce the event log, manifest, or full evidence body — those remain in
the external, non-git evidence store, referenced here by run ID and checksum (§2).

---

## 1. What is preserved

The completed mechanical-execution checkpoint for run `MP-DH1-D-001`: Strategy D's preserved,
unmodified implementation and semantics, executed exactly once against the deterministically-selected,
bounded-released D-H1 input (`NDXJPY`, `1985-01-31 → 1987-07-26`), without any economic metric being
computed, and without Strategies A, B, or C being run.

## 2. External evidence reference (not copied into git)

| Field | Value |
| --- | --- |
| Run ID | `MP-DH1-D-001` |
| Evidence store | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-p/MP-DH1-D-001/` |
| `manifest.json` sha256 | `6f1ad7c21d9df526c80bb4fc826d01e227c2fe79e0cfe0a8f833ebb01fdd2651` |
| `event_log.json` sha256 | `972b36b786a4dfa60f7bbd17fc4360ac4e28fcb6e77d72f11bcf70856adf6e85` |
| `terminal_state.json` sha256 | `fe7881a51d395b795e353119adc2342d6fc1680acb04795c46d2eba372f3a584` |
| `assertions.json` sha256 | `7ed9e568d9ebcf3cf229a43243d59c591cb3811bd18ab63f54c8a0b555da94e7` |
| Input dataset CSV | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh1-selection/dataset/DH1_NDXJPY_1985-01-31_1987-07-26.csv` |
| Input CSV sha256 | `4b4d076e6c1c22be88dab25a1506b5a625e8fd9a8082c6befb7fb09898584439` |
| Store `PROVENANCE.md` | Updated additively with a "Generation DH1" section; prior generations (`MP-H1`, `MP-H2`, `MP-EV`, `MP-EV2`, `MP-DH0`, `MP-DH0P`) unmodified |
| Determinism | Verified: two independent executions produced byte-identical `event_log.json`/`terminal_state.json`/`assertions.json` (apart from the `run_id` string) |

## 3. Mechanical quantities (independently re-verified against the raw evidence before this preservation)

| Quantity | Value |
| --- | --- |
| Observations | `627` |
| Allocations | `26` (`12 NORMAL`, `4 LARGE_DROP_ESCALATION`, `10 DIRECT_LARGE_DROP`) |
| Suppressions | `547` (`175 STRATEGY_D_REPEATED_NORMAL_NO_ADDITIONAL_ALLOCATION`, `372 STRATEGY_D_MONTHLY_CAPACITY_EXHAUSTED`) |
| Zero-cap events | `7` (`NO_ALLOCATION`, reason `ZERO_UNITS_AVAILABLE`) |
| Positive-partial-cap events | `0` |
| Month-crossing executions | `0` |
| Year-crossing executions | `0` |
| Exact `-10.00%` / `-20.00%` boundary observations | `0` / `0` |
| `all_invariants_pass` | `true` — 20 applicable invariants, including `INV-9-D` (both clauses) and `ENG-D1`…`ENG-D5`, all pass; Baseline `INV-9` correctly not applicable (no A/B/C touched) |
| Governed economic metric present anywhere in output | **None** — token-scanned (`TTEV`, `XIRR`, `CAGR`, Sharpe); every match confined to the manifest's own declared `outputs_excluded` prohibition string, never a computed value |

## 4. Claim boundary — this is the entire permitted claim

> Strategy D completed one deterministic mechanical execution on the frozen D-H1 input without
> mechanical or invariant failure.

Natural-path coverage observed (test-coverage reporting only — frequency implies no performance
judgment): Normal-only, Normal→Large-drop escalation, direct Large-drop, repeated-Normal suppression,
and repeated-capacity suppression all occurred naturally; zero-cap occurred naturally; positive-partial
cap, month-crossing execution, year-crossing execution, and exact `-10%`/`-20%` boundary observations
did not occur in this window.

**This artifact does not claim, state, or imply**: economic success or failure; superiority or
inferiority to Strategy A, B, or C; optimization; robustness; generalization beyond this one window;
statistical validation; or adoption. None of these follow from the mechanical result above, and none
are asserted here.

## 5. Qualification-state preservation

Unchanged: `O-4`, `P1-x`, `M-x`, `HG-8`, Primary Proxy, Stage G, Stage H. **Phase 2 remains BLOCKED.**
This checkpoint is not qualification evidence and does not resolve any `P1-x`/`M-x` item.

## 6. Scope

This artifact preserves a checkpoint reference only. It does not modify the Frozen Baseline, Strategy
D's implementation or semantics, the D-H1 policy, rule, or bounded-release decision, any qualification
artifact, or any prior evidence generation. It does not authorize, and should not be read as
authorizing, economic evaluation, an A/B/C/D comparison, or any further Strategy-D investigation stage
— those remain separate, not-yet-made Owner decisions (§7).

## 7. Next decision required (not made here)

The minimum Owner decision now required is which of the following becomes the next research question:
(1) economic evaluation of Strategy D on this D-H1 result; (2) an A/B/C/D comparison on D-H1; (3)
another independent-validation stage; or (4) stopping Strategy-D investigation at this mechanical
checkpoint. This artifact makes no recommendation among them and authorizes none.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. Mechanical-result checkpoint only.
No economic claim. No A/B/C/D comparison. No qualification-state change. `f8332a5`, `f025bbf`,
`b722fb2`, and every preserved Strategy-D and Mode-P evidence generation are unchanged.**
