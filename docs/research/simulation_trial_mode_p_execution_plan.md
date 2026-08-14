# Simulation Trial — Mode P Execution Plan

**Status:** **APPROVED IN PRINCIPLE — OWNER DECISION 2026-08-14.**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13)
**Controlling Decision:** Mode P Decision Boundary, commit `91378fe`,
tag `simulation-trial-mode-p-decision-boundary-20260814`

**This plan does not authorize retrieval.** Baseline v2 §18.4.1 requires *"its own separate Owner
Decision **and execution plan**"*. Both now exist. **Step P1 nonetheless still requires its own
bounded acquisition authorization before any external data is touched**, and the Owner Decision of
2026-08-14 expressly directs a STOP at that gate.

---

## 0. Objective and anti-scope

**Objective:** the shortest honest path to the **FIRST BOUNDED REAL-DATA SIMULATION**.

**This is not a Mode-P roadmap.** It stops at the first successful run. It does not plan a second
run, a sensitivity study, a proxy comparison, a metric suite, or Phase 2.

**Anti-scope, absolute:**

- no economic conclusion, no performance claim, no strategy ranking;
- no metric governed by `M-1 … M-8` (`MP-D3`);
- no resolution of `M-7`, `P1-1`, `OD-04`, `P1-2`…`P1-9`, `O-4`, `M01`/`M02`/`M03`;
- no Primary Proxy selection or qualification-lane action;
- no Phase 2 work — Phase 2 remains **BLOCKED**;
- no promotion of any Mode-E or Mode-P output to formal status.

---

## 1. The one decision this plan cannot make for you

> ### `MP-P-D1` — Provisional data-source selection **`[RESOLVED — OWNER DECISION 2026-08-14]`**
>
> Repository authority **fixes the index and the intended product**: the Baseline is a NASDAQ-100
> strategy, and §9.1 names the intended *Nissay NASDAQ100 Index Fund*. Authority **does not fix** the
> provisional data **vendor**, **series type**, or **snapshot**.
>
> **Owner disposition.** The first Mode-P simulation uses **a provisional historical daily NASDAQ-100
> price series** suitable for exercising the existing Strategy A/B/C engine, selected on this
> priority order: (1) reproducible access; (2) sufficient historical span; (3) daily observations
> suitable for month/year boundary processing; (4) clear denomination and series semantics;
> (5) licence/retention terms compatible with private external storage; (6) minimal implementation
> complexity.
>
> **A source MUST NOT be selected or rejected on the basis of simulated Strategy A/B/C results**
> (§18.4.7 bars selecting *"a candidate because it performs better"*). The source, series and span
> MUST be recorded **before** any result is inspected.
>
> The dataset is **PROVISIONAL — NOT QUALIFIED — NON-FORMAL — NON-PROMOTABLE**. Its use does not
> resolve `P1-1` or `P1-2`, select a Primary Proxy, resolve `O-4` or `M01`/`M02`/`M03`, establish
> formal historical admissibility, or authorize Phase 2.

**Data shape.** The simplest available daily series providing observation date, closing level, series
metadata sufficient to identify it, and enough history for multiple month and year boundaries.
**OHLC is not required** — `MP-R-02` uses closes only. Dividend-adjusted, fund-NAV-equivalent, or
formally qualified data is **not** required to obtain the first run; those remain deferred formal
questions (`P1-3`, `P1-4`, `P1-1`).

**Span.** Bounded but meaningful: multiple calendar years, multiple drawdown regimes, month
boundaries, year boundaries, recoveries and new highs. **The span MUST NOT be maximised merely
because more data exists** — prefer the shortest span giving meaningful coverage of those engine
states, recorded before results are inspected.

> **Disclosed selection bias — binding limitation.** A span chosen for *drawdown-regime richness*
> selects conditions under which Strategies B and C are structurally more active than Strategy A,
> since B and C act only on drawdowns while A does not read drawdown at all. This is legitimate for
> **engine-state coverage**, which is the first run's sole purpose, and is harmless while `MP-D3`
> forbids performance reporting. It nonetheless **permanently bars this span from any later
> performance comparison**: a comparison over a deliberately drawdown-rich span would be a selected
> result, not evidence. Any future formal work MUST use a span derived from `P1-5`/`P1-6`, never this
> one.

---

## 2. Minimum sequence

### P0 — Verify controlling authority `[no external access]`

Confirm, mechanically: Baseline v2 blob `50da4d16…`; the Decision Boundary preserved at `91378fe`,
tag peeling correctly; Mode-E engine at `d5e7db8` with all four suites green; prior tags unmoved.
**Abort if any differs.**

### P1 — Obtain separate authorization for ONE bounded acquisition `[STOP — Owner gate]`

Requires `MP-P-D1` decided. The authorization must state exactly: one source, one series, one span,
one snapshot, retrieved once, stored **outside** the worktree, **never committed**.

> **No external access whatsoever occurs before this gate.** Drafting or approving *this plan* does
> not authorize acquisition.

### P2 — Acquire exactly one frozen snapshot

One retrieval into an external Mode-P data store. Record retrieval timestamp and SHA-256 at the
moment of capture. **The snapshot is immutable.** Re-retrieval later is a **new dataset and a new
run** — never a revision of this one (`P1-9`, §18.4.4).

### P3 — Dataset provenance and manifest

Create `PROVENANCE.md` and `SHA256SUMS` in a **Mode-P store separate from the Mode-E store**, plus a
§18.4.9-compliant run manifest recording: run ID; `execution_mode: "P"`; simulator commit;
strategy-rule identifier; **BASELINE RULE** (not an experimental variant); dataset ID;
`dataset_class: "provisional"`; parameters; date range; assumptions; outputs; the status
**`NON-FORMAL — SIMULATION TRIAL`**; prohibited uses; known limitations; `baseline_version: v2`.

> §18.4.9: *"A run without a manifest is void, and its output MUST NOT be used for any purpose."*

Declared assumptions MUST include, in the manifest and in every output: `MP-R-02` provisional
execution valuation and its distortion direction; **zero costs modelled** (`P1-4`); **no FX
conversion modelled** (`P1-7`); series type (`P1-3`); the span carrying **no** `P1-5`/`P1-6`
significance; **no execution failure modelled** (`M-4`); **no zero-unit-acceptance semantics**
(`M-6`).

### P4 — Minimum loader and driver

Reuse the **preserved Mode-E engine unchanged** in its mechanics. Add only:

1. a loader converting the frozen snapshot into the existing observation schedule shape;
2. a Mode-P driver — the Mode-E driver's evidence-safety gate, fail-closed overwrite protection,
   strategy-label integrity and fixture-hash integrity all carry over unchanged;
3. `MP-R-01` exact scaled comparison (`close ≤ 0.9×ATH`, `close ≤ 0.8×ATH`) replacing quotient
   comparison in classification;
4. Mode-P classification labels and the §18.4.3 prohibited-use list.

**No new strategy semantics.** All four preserved suites (E1–E4) MUST still pass afterwards; if
Strategy-A/B/C behaviour changes on the synthetic suite, **STOP** — the change is a defect, not an
improvement.

### P5 — Execute A, B and C against the same provisional dataset

One span, one snapshot, three strategies, `MP-R-01` classification, `MP-R-02` execution valuation.
Identical funding capacity across strategies (Invariant 3) is asserted as in E3.

### P6 — Report only `MP-D3`-approved quantities

Units acquired; cash deployed; cash remaining; allocation count; suppression count; the ordered event
log. **Prohibited:** terminal exposure valued at the final observation, any terminal portfolio
valuation, TTEV, XIRR, CAGR, return in any form, tracking statistics, and any combination whose
purpose is to reconstruct an `M-1 … M-8` metric. Mode E's no-metric guard is carried over unchanged
and extended to the Mode-P outputs.

### P7 — Verify determinism and evidence integrity

Apply the E4 regime: replay each run and require byte-identical outputs; verify manifest ↔ engine ↔
state strategy agreement; verify `dataset_sha256` equals the snapshot's hash; verify
`simulator_paths_match_commit`; reconcile `SHA256SUMS` and confirm Mode-E evidence is untouched.

### P8 — STOP

**STOP immediately after the first successful bounded real-data simulation and its verification.**
Report; do not interpret; do not tune; do not run a second configuration; do not begin Phase 2.

---

## 3. STOP conditions

Stop and return to Owner Review if: `MP-P-D1` is undecided at P1; acquisition would exceed one
source / one series / one span / one snapshot; licence terms would require committing raw data or
forbid private retention; a preserved E1–E4 regression fails; Strategy A/B/C synthetic behaviour
changes; replay is not byte-identical; a manifest cannot be completed under §18.4.9; the data would
require inventing a `P1-1` mapping; any output would reconstruct a governed metric; or any step would
require Mode-E evidence to be modified.

---

## 4. Success criteria

One bounded real-data simulation executes A, B and C over one provisional snapshot; every run carries
a complete §18.4.9 manifest and the `NON-FORMAL — SIMULATION TRIAL` classification; replay is
byte-identical; only `MP-D3`-permitted quantities are reported; E1–E4 regressions and Mode-E evidence
are untouched; and `M-7`, `P1-1`, `OD-04`, `M-1`, `M-5`, `M-8`, `P1-2`…`P1-9`, `O-4` and
`M01`/`M02`/`M03` all remain **exactly as unresolved as before the run**.

---

## 5. What a successful first run will and will not tell you

**Will:** whether the frozen mechanics behave coherently on real price paths — how often each strategy
commits, how monthly exclusivity and the annual budget interact over a real drawdown history, whether
Strategy C's fallback fires as designed, and where budget capping binds.

**Will not:** which strategy is better. That question requires TTEV, which requires `M-5`, which
`MP-D3` and §18.4.3 both put out of reach. Anyone reading the first run as a performance comparison
has misread it.
