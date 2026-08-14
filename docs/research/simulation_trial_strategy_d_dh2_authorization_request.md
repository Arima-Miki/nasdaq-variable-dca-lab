# Simulation Trial — Strategy D Stage D-H2 Independent-Validation Authorization **REQUEST**

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.** This approval authorizes execution of the
already-frozen deterministic dataset-selection rule for Stage D-H2 candidate selection and freeze only.
No D-H2 dataset has yet been selected. No candidate price value has been inspected. No retrieval,
execution, or economic computation has occurred. Strategy D remains unmodified.
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Produced by:** Post-D-H1 Owner Review (analysis-only task; this artifact is the "shortest defensible
next step" output of that review, offered per its own instruction to draft a useful artifact only after
completing the analysis, and to leave it uncommitted).
**Controlling Baseline:** v2 (effective 2026-08-13) — unchanged by this request
**Controlling D-H1 chain (all unmodified, all reused by reference):**
hypothesis `5a3f54a` · semantics `62c5c42` · Mode-E E5 `f16a815` · D-H0 `486b994` ·
D-H1 dataset-selection policy `f8332a5` · D-H1 deterministic selection rule `f025bbf` ·
D-H1 bounded-release decision `b722fb2` · D-H1 mechanical-result checkpoint `8a76769` ·
D-H1 economic-comparison methodology `f0f60fa` · D-H1 economic-comparison result `2fb87c3`
(tag `simulation-trial-strategy-d-dh1-economic-result-20260814`)

---

## 1. What this request is for

The preserved D-H1 result (`2fb87c3`) is one independently-selected window. It explicitly does not, and
cannot, establish robustness, generalization, statistical validation, or adoption readiness for Strategy
D. The repository's own governance chain (`f8332a5` §8A, and the mechanical-result checkpoint `8a76769`
§7) anticipated exactly this choice point: whether to pursue **another** independent-validation window
("D-H2") before any Strategy-D modification, Strategy E work, or adoption discussion.

This request proposes running the **already-approved, zero-discretion D-H1 machinery a second time**,
against a second, still-unseen window — nothing new is designed here. It bundles the same sequence of
gated steps the D-H1 chain already used, each still separately checkpointed, so the Owner can approve the
whole reusable pipeline once rather than re-approving seven near-identical documents.

## 2. Precondition — verified, not asserted

**Strategy D's rule and semantics (`5a3f54a`/`62c5c42`) remain completely unmodified since D-H1.** This
is the load-bearing precondition for D-H2 being valid independent evidence about the *same* hypothesis,
per the versioning discipline already fixed in `f8332a5` §15/`DH1-R14`: any substantive Strategy-D
change made *after* inspecting a result creates a new, distinctly-versioned hypothesis that D-H1 (or
D-H2) can never retroactively validate. **This precondition must be re-verified true at execution time,
not assumed from this document's drafting date.**

## 3. What is reused mechanically, unchanged

- **Dataset-selection policy** (`f8332a5`) — unchanged. All eligibility categories, contamination
  boundary, one-shot discipline, replacement policy, and instrument-option ranking (§16A) apply as
  written.
- **Deterministic selection rule** (`f025bbf`) — unchanged, zero residual discretion. Its `ALREADY_SEEN`
  test (§3 of `f025bbf`, category-C/D exclusion) already, without any amendment, excludes **both**
  previously-touched spans: the D-H0 span (`2018-01-02→2020-06-26`) via the existing `OVERLAPS_DH0`
  test, and the D-H1 span (`1985-01-31→1987-07-26`) via `ALREADY_SEEN`, since that span now has computed
  economic statistics on record. **No new rejection code or rule text is required** to keep D-H2 clear
  of both prior windows.
- **Economic-comparison methodology template** (`f0f60fa`) — the metric set (§10 fields A–L), the
  factual-vs-superiority claim boundary (§12), the funding-comparability guarantee (§7), the reserved-
  cash treatment (§9, `DH1-EV-D2`-equivalent), and the execution ordering (§14) all transfer unchanged.
  Only the **terminal-valuation literal** (`DH1-EV-D1`'s dataset-specific final price) requires a fresh,
  narrow, dataset-specific decision — exactly as `f0f60fa` §8 already states about its own relationship
  to `00b2b4a`.
- **Mechanical engine path** — `SUPPORTED_STRATEGIES = ("A", "B", "C", "D")` already extended; no code
  change required.

## 4. What genuinely requires a new, separate Owner Decision

1. **Execution of the deterministic selection rule against the now-updated eligibility universe** (D-H0
   and D-H1 spans both excluded) — mechanical, zero discretion, but is itself an act requiring
   authorization, exactly as `f025bbf`'s own execution required separate authorization from its design.
2. **A new bounded-release decision** for whatever window the rule selects — mirrors `b722fb2` exactly;
   cannot be pre-drafted here because the window is not yet known.
3. **A new, minimal terminal-valuation decision** (`DH2-EV-D1`-equivalent) instantiating the `f0f60fa`
   template's one dataset-specific literal (final observation price) — mirrors the `00b2b4a`→`f0f60fa`
   relationship exactly.
4. **Re-verification of the precondition in §2** at the time D-H2 is actually executed, not merely at
   the time this request is drafted.

No other genuinely new governance artifact is anticipated. This is the entire marginal cost.

## 5. Proposed execution ordering (mirrors `f8332a5` §13 / `f0f60fa` §14 exactly)

1. Execute the D-H1 deterministic selection rule (`f025bbf`) against the current eligibility universe.
   Record the selection trace. **No price value inspected.**
2. Draft and obtain the fresh bounded-release decision for the selected window.
3. Run Strategy D alone, mechanical-only, on the frozen input; preserve as a checkpoint (mirrors
   `8a76769`) before A/B/C are even considered.
4. Run Strategies A, B, C, mechanical-only, in that order; preserve.
5. Draft and obtain the fresh terminal-valuation decision; compute the D-H2 economic comparison strictly
   from the four preserved mechanical states.
6. Preserve the factual result, restating the full §18.4.7 disclosure chain (now three prior Simulation
   Trial results on Strategy-D-adjacent windows, extended a fourth time) and the unchanged evidentiary
   ceiling: **even a favorable D-H2 result does not authorize adoption, Phase 2, or Baseline
   modification.**

## 6. What this request explicitly does NOT do

Does not select a dataset, instrument, or window. Does not inspect any price value. Does not execute
Strategy D, A, B, or C. Does not compute any economic value. Does not modify Strategy D's rule or
semantics. Does not modify the Frozen Baseline, `experiment_spec_v2.md`, or the criteria freeze. Does not
authorize Strategy E or any new hypothesis. Does not change any `P1-x`/`M-x`/`O-4`/`HG-8`/Primary-Proxy/
Stage-G/Stage-H/Phase-2 state. Does not, even if every subsequent step succeeds, authorize adoption,
optimization, Baseline-candidate status, or any claim beyond the same factual-difference / one-more-
window-mechanism-observation boundary `f0f60fa`/`2fb87c3` already established for D-H1.

## 7. STOP conditions (inherited from `f8332a5`/`f025bbf` unchanged)

If the deterministic rule finds no eligible candidate across all four tiers: `D-H2 BLOCKED — NO ELIGIBLE
INPUT`, return to Owner Review — do not weaken any criterion to force a result. If Strategy D has been
modified in any way since `62c5c42`: **STOP** — this request is void as drafted; any validation run must
instead follow the "new versioned hypothesis" path (`f8332a5` §15), not this document.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14. This approval authorizes execution
of the frozen deterministic dataset-selection rule (`f025bbf`) for D-H2 candidate selection and freeze
only. No dataset has been selected. No price value has been inspected. The next distinct task is
execution of that rule against the updated eligibility universe (both D-H0 and D-H1 spans excluded by
existing rule text). Strategy D, the D-H1 chain, and the Frozen Baseline remain unchanged.**
