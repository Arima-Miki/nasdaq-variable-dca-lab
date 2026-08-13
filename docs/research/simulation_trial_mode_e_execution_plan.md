# Simulation Trial — Mode E (Engine Validation) Execution Plan

**Status:** **APPROVED.** Execution not yet performed: no code, no fixture, no run

**Governing Baseline: v2** — effective 2026-08-13

**Plan drafted:** 2026-08-13

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Simulation Trial Execution Plan — Mode E** |
| Plan status | **APPROVED — execution not yet performed** |
| Controlling authorization | [`../decisions/simulation_trial_mode_e_authorization_decision.md`](../decisions/simulation_trial_mode_e_authorization_decision.md) — **APPROVED; Mode E AUTHORIZED** |
| Governing Baseline | **v2** §18.3, §18.4 — [`../experiment_spec_v2.md`](../experiment_spec_v2.md) |
| Objective | Reach the **FIRST SUCCESSFUL END-TO-END SYNTHETIC SIMULATION** safely and quickly |
| Mode P / Phase 2 | **NOT AUTHORIZED** / **BLOCKED** |

> **This plan governs HOW Mode E runs. It never extends WHAT is authorized.** Where it and the
> authorization differ, **the authorization governs**; where the authorization and Baseline v2 differ,
> **v2 governs**.

---

## 2. Minimum engine mechanics

Taken from controlling Baseline v2. **Nothing here is invented; every item cites its provision.**

| # | Mechanic | Rule (v2) |
| - | -------- | --------- |
| 1 | **Reference High / ATH** | `reference_high(t) = max(daily closes available through t)`; never decreases within a run; intraday highs never used — §7, §4.0, OD-02 |
| 2 | **Drawdown** | `DD(t) = (close(t) − reference_high(t)) / reference_high(t)`; new ATH ⇒ `DD = 0%` — §4.0 |
| 3 | **Zone classification** | High `DD > −10%`; Normal `−20% < DD ≤ −10%`; Large-drop `DD ≤ −20%`. **`−10.0%` → Normal; `−20.0%` → Large-drop.** Mutually exclusive, jointly exhaustive — §4.0 |
| 4 | **Signal timing** | Per day, in order: observe confirmed close → add to available history → update ATH → compute DD → evaluate rule → emit Signal → execute separately. **A Signal from a day's close MUST NOT execute at that same close** — §8, OD-03 |
| 5 | **Strategy A** | Fixed DCA: 1.0-unit decision on the **final trading day of each calendar month**; no drawdown decision — §4.1, §4.4, OD-01 |
| 6 | **Strategy B** | Every trading day: High → WAIT / 0 units; Normal → **1.0-unit** trigger; Large-drop → **2.0-unit** trigger; no month-end fallback — §4.2, §4.4, OD-09 |
| 7 | **Strategy C** | As B, plus **0.5-unit month-end fallback** when no trigger committed that month — §4.3, §4.4, OD-05 |
| 8 | **Monthly exclusivity** | **Max 1 committed allocation per calendar month** per strategy; later same-month Signals create no Purchase Request; suppression observable with an explicit reason; a delayed execution attributed to a prior month does not consume the new month's limit — §10, §12.5, OD-06 |
| 9 | **Annual budget** | **12.0 units (JPY 120,000)** at the start of each calendar year, **available at once**, not monthly; unused units carry forward and never expire; **no carry-forward cap**; future-year units never borrowed; A, B, C funded identically — §11.1, OD-10 |
| 10 | **First partial year** | If performance start falls after 1 January, the starting calendar year receives the **full 12.0 units at the simulation performance start, without proration** — §11.1, OD-14, Invariant 18 |
| 11 | **Budget validation and capping** | `requested > available` ⇒ `accepted = available`; only accepted units reserved; future-year budget never back-fills a capped request — §12.4 |
| 12 | **Commitment / reservation** | On acceptance: reserve immediately; remove from available immediately; attribute to the **calendar month and budget year of acceptance** — §12.1, §12.2, OD-13 |
| 13 | **Execution timing** | May occur later; a later execution never changes the original month or budget year; **never deducts reserved units twice** — §12.3 |
| 14 | **Cash** | Unused satellite cash remains economic value; **Baseline cash return 0%** — §11.2, §11.3, OD-07 |
| 15 | **Position accumulation** | Reserved amount converts to NASDAQ exposure at the applicable valuation — §3, §9 |

### 2.1 Invariants to assert

From §17, those reachable in Mode E: **1** no future information influences a decision · **2** a
close used to generate a Signal is never the retrospective execution price for it · **3** identical
annual funding across A, B, C · **4** exactly 12.0 new units per calendar year · **5** future-year
units never borrowed · **6** unused units carry forward without expiration · **7** unused cash
remains economic value · **8** cash return 0% · **9** at most one committed allocation per calendar
month · **10** commitment reserves budget immediately · **11** execution never deducts twice · **12**
execution delay never changes month or budget year · **13** Strategy B never purchases in the High
zone · **14** Strategy C uses 0.5 units only as month-end fallback · **15** no same-month escalation ·
**18** first partial year funded at 12.0 units without proration.

Plus engine invariants: ATH never decreases; reserved + available + executed reconciles; no negative
balances.

> **Invariants 16 and 17 are reporting/governance rules, not engine assertions.**

---

## 3. Synthetic scenario suite

**Smallest suite that exposes implementation error.** Deliberately simple and **hand-verifiable** —
expected outputs derived by hand and recorded in the fixture **before** the engine runs.

| # | Scenario | Exposes |
| - | -------- | ------- |
| **S1** | Monotonically rising prices | ATH tracking; `DD` stays 0; B never buys (Invariant 13); A buys monthly; C uses fallback |
| **S2** | Shallow drawdown, never below −10% | Zone boundary on the High side; no B/C trigger |
| **S3** | First crossing into Normal zone | 1.0-unit trigger; commitment; reservation |
| **S4** | Crossing into Large-drop zone | 2.0-unit trigger |
| **S5** | Recovery to prior high, then a new ATH | ATH monotonicity; `DD` returns to 0 |
| **S6** | Repeated drawdowns across several months, budget remaining | Monthly exclusivity; one allocation per month; carry-forward |
| **S7** | Budget exhaustion mid-run | Capping (§12.4); `accepted = available`; no future-year borrowing |
| **S8** | Zero remaining units when a trigger fires | Zero-availability handling without deciding `M-6` reason codes |
| **S9** | `DD` exactly `−10.0%` and exactly `−20.0%` | **Fixed boundary semantics only** — `−10.0%` → Normal, `−20.0%` → Large-drop. Exact-decimal comparison. **Does not decide `M-7`** |
| **S10** | One tick either side of each threshold | Strict-inequality correctness |
| **S11** | Performance start after 1 January | OD-14: full 12.0 units, no proration (Invariant 18) |

**No historical observation is used.** Values are small round synthetic numbers chosen for hand
verification, **not** resembling any real series.

---

## 4. Determinism requirements

Fixed synthetic inputs, committed and hashed · deterministic event ordering per §8 · explicit
configuration, no hidden defaults · no wall-clock, RNG, locale, or filesystem-order dependence (any
generator seeded and the seed recorded) · run manifest per §5 · simulator commit recorded · input
hash recorded · fixed output location · assertion results recorded.

> **Replay rule:** identical code + config + input ⇒ **byte-identical engine output**. Verified by
> running twice and comparing checksums.

---

## 5. Run manifest

Per Baseline v2 §18.4.9, mandatory — **a run without a manifest is void**:

run ID · **execution mode `E`** · simulator version/commit · strategy-rule identifier (A / B / C) ·
**Baseline rule** vs `EXPERIMENTAL VARIANT — NOT BASELINE` · dataset ID · **dataset class:
`synthetic`** · parameters (thresholds, sizing, annual budget, execution valuation rule) · date range ·
assumptions · engine-state outputs produced · **`NON-FORMAL — SIMULATION TRIAL`** · prohibited uses ·
known limitations · **`baseline_version: v2`** · plus the §7 classification banner.

---

## 6. Repository and output structure

**Proposed; nothing is created by this plan.**

```
sim/                                   ← IN GIT (simulator source only)
    engine/                            deterministic engine
    fixtures/                          synthetic scenarios + hand-derived expectations
    tests/                             invariant and unit tests

~/research-materials/nasdaq-variable-dca-lab/simulation-trial-mode-e/   ← OUTSIDE GIT
    PROVENANCE.md
    SHA256SUMS
    <run-id>/  manifest.json · event log · terminal state · assertion results
```

> **No Mode-E output path may be under `docs/`.** Outputs stay outside the worktree; **no Mode-E
> output enters Git** without a separate Owner Decision. Source is in Git because §18.4.9 requires a
> simulator commit in every manifest.

---

## 7. Result classification

Every manifest and every summary carries:

> **`ENGINE VALIDATION RESULT — SYNTHETIC — NON-ECONOMIC — NON-BASELINE — NON-PROMOTABLE`**
> **`NON-FORMAL — SIMULATION TRIAL`**

**Never cited as** investment performance · expected return · historical performance · Baseline
result · qualification evidence · strategy superiority · support for a live-investment decision.

**No evaluation metric is computed** — no TTEV, XIRR, CAGR, total or annualised return, or drawdown
statistic as performance. **Engine state only.**

---

## 8. Execution sequence — first run as early as safely possible

**The proposed `E0 … E7` is compressed**: a walking skeleton reaches the first end-to-end run at
**step E1**, not step E5. Building the full suite before the first run would defer the only step that
proves the approach works.

| Phase | Work | Exit condition |
| ----- | ---- | -------------- |
| **E0** | Repository/authority verification — no code. Confirm v2 effective, Mode E authorized, qualification state unchanged | Boundary confirmed; any conflict → **STOP** |
| **E1** | **Walking skeleton → FIRST END-TO-END RUN.** Fixture **S3** only (simplest scenario exercising a trigger), one strategy (**B**), minimal engine covering mechanics 1–4, 6, 8, 9, 11, 12, plus manifest and event log | **FIRST SUCCESSFUL END-TO-END SYNTHETIC SIMULATION** per authorization §6 |
| **E2** | Invariants and unit tests for the mechanics implemented so far | All assertions pass |
| **E3** | Remaining scenarios **S1, S2, S4–S11**; Strategies **A** and **C**; mechanics 5, 7, 10, 13–15 | Suite passes against hand-derived expectations |
| **E4** | Determinism and replay verification | Byte-identical replay |
| **E5** | Package outputs to the external store; checksums and provenance | Store verifies |
| **E6** | Report and **STOP for Owner Review** | Report returned |

> **E1 is the milestone.** If E1 cannot be reached without a category-A decision, **STOP** rather
> than build around it.

---

## 9. STOP conditions

Narrow, per authorization `ME-OD-11`: repository-authority conflict · a **category-A** unresolved
semantic · the first run would alter frozen qualification criteria · isolation cannot be maintained ·
the work would in substance be **Mode P** or **Phase 2**.

> **Not STOP conditions:** `O-4` open · `HG-8` NOT EVALUABLE · `P1-2`, `P1-5`, `P1-6` open ·
> `H-1` NOT ESTABLISHED · historical data unavailable · qualification incomplete.

Also stop if: a real historical observation would be needed; an evaluation metric would be reported;
or an output would be written under `docs/`.

---

## 10. Execution-report contract

On completion the executing session returns and **STOPS**: phases executed · **first-run evidence**
(manifest, event log excerpt, terminal state) · scenarios run and hand-verification results ·
invariant results · determinism/replay verification · store integrity · classification confirmation ·
confirmation that **no metric, no historical data, and no economic claim** appears · qualification
state unchanged · Mode P and Phase 2 unchanged · files changed · `git status` · explicit STOP.

> **The executing session must not commit results without separate Owner approval**, and must not
> promote any output.

---

## 11. Preserved state

**Mode P NOT AUTHORIZED · Phase 2 BLOCKED · Baseline v1 and v2 unchanged · criteria freeze unchanged ·
`AC-7` unchanged · `SC-18` ENGAGED.**

Qualification lane unchanged and **not a prerequisite**: `O4-PARTIAL` ×3 · `GAP-A` ×3 · `GAP-B` ×2 ·
`HG-8` **NOT EVALUABLE** ×3 · `HG-6`/`HG-9`/`HG-12` **PASS** ×3 · `HG-11` bounded · `H-1` **NOT
ESTABLISHED** · `P1-9` **PARTIAL** · `P1-2` **OPEN** · `P1-5` **OPEN** (**P-A**, date **NOT YET
DERIVED**) · `P1-6` **OPEN** · `K1` 2026-08-13 · C-1 ×3 **QUALIFICATION INCOMPLETE** · C-2A unchanged ·
`OJ-1` **NOT REACHED — DEFERRED** · `OJ-6` unexercised · **no Primary Proxy** · Stage G **OPEN** ·
Stage H **NOT BEGUN**.

---

## 12. Approval boundary

> **Drafting did not make this plan executable. Owner approval and preservation did.**

No simulator code, fixture, dataset, or run may exist until the Owner explicitly approves **both**
this plan and its authorization decision, and both are preserved.

**Nothing was implemented, generated, or executed in drafting this plan.**

---

**End of Execution Plan — Simulation Trial Mode E. Governing Baseline **v2**. Mechanics 1–15
and Invariants 1–15, 18 taken from v2 with citations. Scenario suite **S1–S11**, hand-verifiable,
synthetic only. **First end-to-end run at phase E1**, not deferred behind a framework. Output:
**ENGINE VALIDATION RESULT — SYNTHETIC — NON-ECONOMIC — NON-BASELINE — NON-PROMOTABLE**; engine state
only, **no evaluation metric**. **Mode P: NOT AUTHORIZED. Phase 2: BLOCKED. Qualification lane:
UNCHANGED and not a prerequisite.** **APPROVED — execution not yet performed.**
