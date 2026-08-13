# Simulation Trial — Mode E (Engine Validation) Owner Authorization

**Status:** **APPROVED — Mode E AUTHORIZED.** Not yet executed: no implementation, no dataset, no run

**Governing Baseline: v2** — effective 2026-08-13

**Scope:** Simulation Trial lane, Mode E only

**Decision date:** **2026-08-13** — the date of explicit Owner approval

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Owner Authorization — Simulation Trial Mode E** |
| Decision status | **APPROVED — Mode E AUTHORIZED, not yet executed** |
| Owner dispositions | `ME-OD-01` … `ME-OD-12` |
| Governing Baseline | **v2**, [`../experiment_spec_v2.md`](../experiment_spec_v2.md) §18.3, §18.4 — activated 2026-08-13 |
| Resolves | **`OD-REQ-4`** — on approval |
| Execution plan | [`../research/simulation_trial_mode_e_execution_plan.md`](../research/simulation_trial_mode_e_execution_plan.md) — **APPROVED** |
| Mode P | **NOT AUTHORIZED** — and expressly not authorized by this decision |
| Phase 2 | **BLOCKED — unchanged** |
| Qualification lane | **UNCHANGED** — and not a prerequisite; see §7 |
| Success criterion | **FIRST SUCCESSFUL END-TO-END SYNTHETIC SIMULATION** — defined at §6 |

### Artifact role

This is the **separate Owner Decision** that Baseline v2 §18.3 and §18.4.1 require before any
Simulation Trial code may be written. **v2 created the possibility; this creates the permission —
for Mode E only.**

---

## 2. Compatibility finding

`ME-OD-01`. **Mode E is compatible with controlling authority.** Verified from the repository:

| Check | Finding |
| ----- | ------- |
| Baseline v2 effective and controlling | ✅ effective **2026-08-13** |
| v2 §18.3 permits Simulation Trial code before the Phase-1 gates clear | ✅ subject to four conditions, all satisfied by this authorization |
| v2 §18.4.1 requires a separate Owner Decision per mode | ✅ **this is that decision, for Mode E** |
| `AC-7` — `P1-2` before **Phase-2 code** | ✅ **not engaged.** Mode-E code is not Phase-2 code (v2 §18.3); Phase 2 stays BLOCKED |
| Formal-result gate (v2 §18.3.2 equivalent) | ✅ **untouched.** Mode E produces no formal output |
| Criteria freeze `1e8bc85` | ✅ unchanged |

> **No normative conflict. No Baseline change is required.**

---

## 3. Authorized scope

`ME-OD-02`. **Authorized, and limited to what the first synthetic run requires:**

- simulator implementation;
- implementation of the **frozen Baseline strategy rules** (Strategies A, B, C) as the execution
  target;
- **synthetic** data generation and deterministic scenario fixtures;
- **synthetic-only** data loaders;
- execution manifests;
- run logs and event logs;
- assertions and invariant checks;
- **engine-level state summaries** — unit counts, cash and budget balances, reservation and
  execution events;
- tests required to establish mechanical correctness.

---

## 4. Prohibited scope

`ME-OD-03`. **Absolutely prohibited under Mode E:**

- **real historical market data** of any kind — index, NAV, FX, or otherwise;
- **provisional economic claims** or any economic conclusion;
- **Mode P** work, or anything that would in substance constitute it;
- **evaluation metrics governed by §19.2** — no TTEV, XIRR, CAGR, total return, annualised return,
  tracking statistics, or any performance measure. v2 §18.3 requires §19.2 items to be fixed
  *before the metrics they govern are reported*, and **`M-1 … M-8` are not fixed**;
- representing synthetic data as market evidence;
- Phase-2 work; changing any qualification state; modifying Baseline v1, Baseline v2, the criteria
  freeze, README, or any preserved artifact.

`ME-OD-04`. **Mode E reports engine state, never performance.** This is the operative line that keeps
Mode E non-economic, and it is not to be softened.

---

## 5. Unresolved methodology semantics — handled, not researched

`ME-OD-05`. Where a mechanic is unresolved, it is classified **A** (blocks execution) or **B**
(representable by an explicit synthetic fixture without deciding the underlying question). **Every
item below is B. None blocks the first run, and none is turned into a research project.**

| Item | Status | Treatment |
| ---- | ------ | --------- |
| **`M-7`** — numeric tolerance/rounding at exactly `-10.0%` / `-20.0%` | Unresolved | **B.** §4.0's *semantics* are fixed and MUST be implemented: `DD = -10.0%` → Normal zone; `DD = -20.0%` → Large-drop zone. Comparison is performed in **exact decimal arithmetic**, so the fixed semantics hold without adopting any tolerance policy. **This is an implementation-precision choice, not a Baseline change, and `M-7` remains OPEN** |
| **`M-4`** — execution-failure retry / cancellation / reservation-release | Unresolved | **B.** **No execution-failure scenario is included.** All fixtures execute successfully |
| **`M-6`** — zero-unit-acceptance semantics and reason codes | Unresolved | **B.** The engine records *"no Purchase Request generated"*; it does **not** model a zero-unit acceptance or assign reason codes |
| **`M-1`, `M-2`, `M-3`, `M-5`, `M-8`** — metric formulas, rolling windows, boundary-state init, TTEV pending-allocation treatment, statistics | Unresolved | **B.** **Out of scope.** No metric is computed and no rolling window is run |
| **`P1-1`** — signal → order → execution date → NAV mapping | Open Phase-1 item | **B.** The **execution valuation rule is a declared fixture parameter** of each synthetic scenario. It is a synthetic fixture choice, **not** a Baseline execution-price determination. **`P1-1`, `OD-04` untouched** |
| **`P1-5`** — Baseline start date | OPEN | **B.** A synthetic run's start is simply its fixture's first observation. **This derives no `P1-5` date.** OD-14 first-year funding is implemented and applies at the fixture's declared performance start |

> **No unresolved economic question is decided by Mode E.**

---

## 6. Success criterion

`ME-OD-06`. **FIRST SUCCESSFUL END-TO-END SYNTHETIC SIMULATION** means **all** of:

1. a **committed synthetic fixture** and a **manifest** are the sole inputs;
2. the engine runs **end to end** over that fixture without error, for at least one scenario and at
   least one Baseline strategy;
3. it emits a **complete ordered event log** — observation, ATH update, drawdown, zone, signal,
   purchase request, budget validation, commitment/reservation, execution — plus a **terminal state**
   (units held, cash, budget remaining, carry-forward);
4. **every implemented invariant asserts true**;
5. the **run manifest** is written and complete per v2 §18.4.9, including the status
   `NON-FORMAL — SIMULATION TRIAL` and `baseline_version: v2`;
6. a **replay with identical code, config and input reproduces byte-identical engine output**;
7. output is **correctly classified** per §8 and stored **outside `docs/`**.

> **It does not require the full scenario suite, all three strategies, or any metric.** Those follow.

---

## 7. Qualification lane is not a prerequisite

`ME-OD-07`. **Mode E does NOT wait on the Qualification lane.** Per v2 §18.4.3, Mode-E output can
never establish any qualification item, so no qualification item gates it.

> **The following are expressly NOT Mode-E prerequisites**, and none is a reason to stop:
> `O-4` OPEN · `HG-8` NOT EVALUABLE · `P1-2` OPEN · `P1-5` / `P1-6` OPEN · `H-1` NOT ESTABLISHED ·
> `GAP-A` / `GAP-B` · historical data unavailable · candidate qualification incomplete.

The Qualification lane continues **independently and unchanged**.

---

## 8. Result classification

`ME-OD-08`. Every Mode-E output carries, in its manifest and in every summary:

> **`ENGINE VALIDATION RESULT — SYNTHETIC — NON-ECONOMIC — NON-BASELINE — NON-PROMOTABLE`**

plus the v2 §18.4.9 status **`NON-FORMAL — SIMULATION TRIAL`**.

**Mode-E output MUST NOT be cited as** investment performance · expected return · historical
performance · a Baseline result · qualification evidence · evidence of strategy superiority · support
for any live-investment decision.

---

## 9. Promotion barrier

`ME-OD-09`. Baseline v2 §18.4.4 is carried unchanged:

> **An old experimental run is NEVER promoted. It is re-run, or it is not formal.**

Nothing produced under Mode E becomes formal merely because the same engine is later used elsewhere.
**No Mode-E output file may be copied, moved, renamed, or relabelled into a formal result.** Future
formal use requires a new authorized run under the applicable lane, satisfying all seven v2 §18.4.4
conditions.

---

## 10. Anti-contamination

`ME-OD-10`. Structural, not procedural:

| Content | Location |
| ------- | -------- |
| Simulator source, fixtures, tests | **In Git**, under a dedicated top-level `sim/` tree — never under `docs/` |
| Mode-E run outputs, logs, manifests | **Outside the Git worktree**, in a dedicated external store, following the established Stage-C/D/E/F pattern with `PROVENANCE.md` and `SHA256SUMS` |

> **No Mode-E output path may be under `docs/`**, which is reserved for formal governance and
> evidence artifacts. **No Mode-E output enters Git** without a separate Owner Decision.

Source lives in Git because v2 §18.4.9 requires a simulator version/commit in every manifest.

---

## 11. STOP conditions — deliberately narrow

`ME-OD-11`. **STOP for Owner Review only if:**

1. repository authority conflicts with Mode-E execution;
2. a required strategy semantic cannot be implemented without an Owner decision — i.e. a **category-A**
   item is found;
3. implementing the first synthetic run would alter frozen qualification criteria;
4. Mode-E isolation cannot be maintained;
5. the proposed work would in substance constitute **Mode P** or **Phase 2**.

> **Do NOT stop merely because** `O-4` is open, `HG-8` is NOT EVALUABLE, `P1-2` / `P1-5` / `P1-6` are
> open, historical data is unavailable, or qualification is incomplete. **None is a Mode-E
> prerequisite under Baseline v2.**

---

## 12. Preserved state

`ME-OD-12`. Unchanged by this authorization:

**Mode P — NOT AUTHORIZED**, framework placeholder only. **Phase 2 — BLOCKED.** Baseline v1 and v2,
the criteria freeze, `AC-7`, `SC-18` (ENGAGED), `OD-REQ-2` — all unchanged.

**Qualification lane:** `O4-PARTIAL` ×3 · `GAP-A` ×3 · `GAP-B` ×2 · `HG-8` **NOT EVALUABLE** ×3 ·
`HG-6` / `HG-9` / `HG-12` **PASS** ×3 · `HG-11` bounded, non-eliminating · `H-1` **NOT ESTABLISHED** ·
`P1-9` **PARTIAL** · `P1-2` **OPEN** · `P1-5` **OPEN** (**P-A**, date **NOT YET DERIVED**) · `P1-6`
**OPEN** · `K1` = 2026-08-13 · C-1 ×3 **QUALIFICATION INCOMPLETE** · C-2A unchanged · `OJ-1` **NOT
REACHED — DEFERRED** · `OJ-6` unexercised · **no Primary Proxy approved** · Stage G **OPEN** ·
Stage H **NOT BEGUN**. `M01` / `M02` drafts untracked and unmodified; `M03` not designed, not
authorized, not executed.

---

## 13. Authorization boundary

> **Drafting authorized nothing. Owner approval and preservation did.**

Mode E becomes authorized **only** on explicit Owner approval of **both** this decision and its
execution plan, followed by preservation. Until then **no simulator code, no fixture, no dataset and
no run may exist**.

**This decision does not authorize Mode P, Phase 2, or any use of real historical data.**

---

**End of Owner Authorization — Simulation Trial Mode E. `ME-OD-01` … `ME-OD-12`. Governing
Baseline **v2**. Scope: synthetic Engine Validation only. All unresolved semantics are **category B**
and none blocks the first run. Success = **FIRST SUCCESSFUL END-TO-END SYNTHETIC SIMULATION** (§6).
Output: **ENGINE VALIDATION RESULT — SYNTHETIC — NON-ECONOMIC — NON-BASELINE — NON-PROMOTABLE**.
**Mode P: NOT AUTHORIZED. Phase 2: BLOCKED. Qualification lane: UNCHANGED and not a prerequisite.**
**Mode E: AUTHORIZED 2026-08-13 — NOT YET EXECUTED.**
