# Simulation Trial — Mode P Decision Boundary

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.**
**Date drafted:** 2026-08-13
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13)

**Mode P status:** **AUTHORIZED IN PRINCIPLE — EXECUTION STILL BLOCKED.** Baseline v2 §18.4.1
requires *"its own separate Owner Decision **and execution plan**"*. This artifact, as approved, is
that Owner Decision. **The execution plan does not yet exist**, so no Mode-P implementation,
dataset acquisition or run is authorized by this artifact.

**Amendment record.** `MP-D3` was found, during Owner Review preparation, to permit reporting
*"terminal exposure valued at the final observation"* alongside remaining cash — which is precisely
§13.1's `TTEV = market value of acquired NASDAQ exposure + remaining unused satellite cash`, and
which engages the open methodology item `M-5` whenever a span ends with a committed-but-unexecuted
allocation. The defect originated in this artifact's own drafting, was reported rather than silently
repaired, and was corrected by Owner Decision of 2026-08-14. `MP-D3` below is the amended text.
`MP-D1`, `MP-D2`, `MP-D4`, `MP-R-01` and `MP-R-02` are substantively unchanged from the reviewed
draft.

---

## 1. Purpose and strict scope

This artifact determines the **minimum set of Owner decisions required before Mode P can safely
consume real historical market data**. It is deliberately narrow.

It does **not**: design the Mode-P architecture; begin implementation; begin external data research;
retrieve, name, or evaluate any data source; or alter any qualification-lane state.

`[STATUS ALIGNMENT — 2026-08-14]` As approved, this artifact **is** the separate Owner Decision
§18.4.1 requires. It authorizes Mode P **in principle only**: §18.4.1 requires an execution plan as
well, that plan does not yet exist, and **no implementation, dataset acquisition or run is authorized
here**.

**The E4 closing recommendation is the hypothesis under test here, not an input to be trusted.** That
recommendation asserted that `M-7` and `P1-1`/`OD-04` are the two immediately load-bearing deferred
questions. §7 of this artifact concludes that **the hypothesis is wrong on both counts**, for a
structural reason that applies to the whole Phase-1 and §19.2 registers at once.

---

## 2. Repository authority reviewed

| Authority | Bearing |
| --------- | ------- |
| Baseline v2 §4.0 | Zone semantics; the `[METHODOLOGY]` note that is `M-7`'s site |
| Baseline v2 §6 | Look-ahead prohibition |
| Baseline v2 §7 | `reference_high(t) = max(daily closes available through t)` |
| Baseline v2 §9, §9.1 | Execution model; `OD-04` principle; the P1-1 mapping requirement |
| Baseline v2 §10, §12 | Monthly exclusivity; commitment / reservation / capping |
| Baseline v2 §16 | Sensitivity analysis belongs to Phase 4 |
| Baseline v2 §17 | Invariants 1–18, in particular Invariant 2 |
| Baseline v2 **§18.3** | Phase-2 gating; the express Simulation-Trial carve-out |
| Baseline v2 **§18.4.1–18.4.9** | Mode E / Mode P; formal-result prohibition; promotion barrier; sensitivity boundary; anti-contamination; manifest requirements |
| Baseline v2 §19.1 | `P1-1 … P1-9`, headed *"Blocking for Phase 2 implementation, not for Baseline Freeze"* |
| Baseline v2 §19.2 | `M-1 … M-8`, *"Methodology Requirements before implementation"* |
| Mode-E authorization decision + execution plan | Precedent for the shape of a mode authorization |
| Preserved Mode-E evidence store | Precedent for keeping data and outputs outside the worktree |

---

## 3. The structural finding that governs everything below

Two provisions of Baseline v2, read together, settle the blocking question for the entire Phase-1
and §19.2 registers:

**§18.3** — *"Simulation Trial code MAY be developed and executed **before those gates are
cleared**"*, where "those gates" are precisely the §19.1 and §19.2 items.

**§18.4.3** — Simulation Trial output may never *"resolve any hard gate, satisfy any Phase-1 item,
[or] fix any §19.2 methodology item."*

If any §19.1 or §19.2 item were a **precondition** of a Mode-P run, then Mode P could never execute:
the item could not be cleared by Simulation Trial work (§18.4.3), and Mode P is defined by §18.4.1 as
consuming *"provisional, **not-yet-qualified** historical data"* — data whose non-qualification is
its defining property. Mode P would be simultaneously permitted by §18.3 and unreachable in
practice.

> **MP-B-01.** No `P1-x` item and no `M-x` item is a precondition of a Mode-P run. The registers gate
> **Phase 2 implementation** and the **reporting of the metrics they govern** — not the existence of
> a non-formal Simulation Trial run. `M-7` and `P1-1` are therefore **NOT** blockers, and neither is
> anything else in those registers.

This does not make the two questions irrelevant. Each still requires an **implementation rule** so
the simulator is executable. The distinction is exact and load-bearing throughout: adopting a
declared, disclosed, non-normative implementation rule **is not** resolving the deferred question,
and §18.4.3 guarantees no Mode-P run can drift into resolving it.

---

## 4. `M-7` — boundary tolerance and classification

### 4.1 Why Mode E never needed a tolerance policy

`M-7` asks for *"numeric comparison tolerance and rounding at the `-10.0%` / `-20.0%` boundaries,
without altering the fixed boundary semantics"* (§19.2, §4.0). Mode E did not need it because it
used **exact Decimal arithmetic at precision 40** over small synthetic integers, so every comparison
was decided exactly. No tolerance was adopted, and `M-7` was recorded OPEN throughout.

### 4.2 Do real prices force a tolerance policy? No.

The question is often assumed to be numerical. It is not. Zone classification asks a **decidable
arithmetic question** about finite decimal quantities:

```
DD(t) = ( close - ath ) / ath          ath > 0
```

Comparing `DD` against `-10%` and `-20%` is **algebraically equivalent** to comparing the close
against exactly-scaled thresholds, with **no division at all**:

```
DD <= -0.10   <=>   close <= 0.9 * ath
DD <= -0.20   <=>   close <= 0.8 * ath
```

Real historical closes are finite decimals. `0.9 * ath` and `0.8 * ath` are therefore also finite
decimals, computed **exactly** by multiplication at adequate precision. Every zone decision is exact
for every possible real close. **No tolerance is required, and none should be invented.**

This separates the two things §19.2 warns about:

- **Numerical representation** — division produces a non-terminating quotient that must be rounded
  before comparison. This is an artefact of *how* the predicate is evaluated, not of the predicate.
  It is removed entirely by not dividing.
- **Genuine strategy semantics** — which zone owns the exact boundary. §4.0 **already fixes** this:
  `-10.0%` belongs to Normal, `-20.0%` belongs to Large-drop. Nothing is open here.

`M-7` remains genuinely open for anything that **must** report a rounded drawdown, and for metrics
governed by §19.2. It is not open for classification.

> **Implementation observation, disclosed rather than acted on.** The preserved engine computes
> `dd = (close - ath) / ath` at precision 40 and then compares. For real closes the true value is
> either exactly on a boundary or differs from it by vastly more than `1e-40`, so no realistic input
> can misclassify. The dependency is nonetheless removable, and the exact form is *more* faithful to
> §4.0 than quotient comparison. **No code change is made in this task** — none is authorized.

### 4.3 Minimum alternatives

| # | Rule | Assessment |
| - | ---- | ---------- |
| **T-1** | **Exact scaled comparison** — classify by `close <= 0.9*ath` / `close <= 0.8*ath`; never compare a rounded quotient | Exact for all real inputs; no tolerance; algebraically identical to §4.0; deterministic; trivial |
| T-2 | Keep quotient comparison at declared precision 40 | Works in practice; retains a needless precision dependency; must declare the precision as a run parameter |
| T-3 | Adopt an epsilon tolerance (e.g. `1e-12`) | **Rejected.** Invents a methodology answer §18.4.3 forbids Simulation Trial from fixing, and creates a band where the frozen boundary ownership silently changes |
| T-4 | Round `DD` to N decimals, then compare | **Rejected.** Materially alters §4.0 boundary semantics — a close at `-9.996%` would become Normal |

### 4.4 Adopted — **T-1**

> **MP-R-01 `[APPROVED — OWNER DECISION 2026-08-14]`.** Mode P classifies zones by **exact scaled comparison** against
> `0.9 × reference_high` and `0.8 × reference_high`, using exact Decimal arithmetic with no
> tolerance and no pre-comparison rounding. Any drawdown percentage that appears in output is a
> **rendering for human reading only** and is never an input to classification. **This adopts no
> tolerance policy and does not resolve `M-7`, which remains OPEN.**

---

## 5. `P1-1` / `OD-04` — signal-to-execution valuation

### 5.1 What remains unresolved

§9 approves the **principle**: signal and execution are distinct; a signal's own closing value MUST
NOT be its execution price; the Baseline must ultimately use the *earliest realistically obtainable
valuation / NAV* after the signal is observable. §9 then states the mapping is **not specified** and
adds a pointed prohibition:

> *"A same-day-close, next-open, or next-close convention MUST NOT be assumed merely because it is
> simple to implement."*

`P1-1` (§19.1, §9.1) requires the real mapping — order cutoff, application/order date, execution
date, NAV determination timing, JST/U.S. session relationship, both holiday calendars, historical
reproducibility — from authoritative product documentation.

### 5.2 The Mode-E assumption that cannot simply be carried over

Mode E declared the execution valuation as a **fixture parameter**: execution occurs at the *next
available observation's close*, with the manifest stating *"not a Baseline execution-price
determination; P1-1 and OD-04 untouched."*

That was honest in Mode E because the data was **invented** — no claim about any real fund could
attach to it. With real data the same rule becomes an **economically consequential approximation**:
it stands in for a real NAV mapping that may settle one or two business days later, across two
holiday calendars. Carrying it over silently would let an implementation convenience masquerade as a
fund-behaviour claim, which is exactly what §9 prohibits. It may be carried over **only** as an
explicitly declared, disclosed provisional placeholder.

### 5.3 Minimum mechanically implementable alternatives

| # | Rule | Look-ahead risk | Reproducibility | Data required | Complexity | Economic distortion | Frozen-strategy compatibility |
| - | ---- | --------------- | --------------- | ------------- | ---------- | ------------------- | ----------------------------- |
| **EV-1** | Same observation's close | **Violates Invariant 2 and §9** | high | closes | trivial | look-ahead | **Impermissible** |
| **EV-2** | **Next available observation's close** | none — strictly later | exact | closes only | trivial | Understates settlement lag; direction disclosable | Satisfies §9 principle and INV-2 |
| EV-3 | Next observation's **open** | none | exact | **OHLC**, not closes | low | Closer to an intraday order, but the fund transacts at NAV, not at open | Compatible; needs data the Baseline never defined |
| EV-4 | Close at **T+N**, N declared | none | exact | closes only | low | Tunable — and therefore a tuning surface, which §16 keeps in Phase 4 | Compatible but invites optimisation |
| EV-5 | Actual fund NAV under the real mapping | none | exact | **the P1-1 mapping + a fund NAV series** | high | none | **This is P1-1 itself — unavailable by definition** |

### 5.4 Adopted — **EV-2**

> **MP-R-02 `[APPROVED — OWNER DECISION 2026-08-14]`.** The first Mode-P run executes a committed allocation at the **close of
> the next available observation strictly after the signal observation**, declared in the manifest as
> a **PROVISIONAL EXECUTION VALUATION PLACEHOLDER — NOT A P1-1 DETERMINATION**, with its known
> direction of distortion (it ignores order cutoff and NAV settlement lag, so it executes *earlier*
> than the real fund would) recorded in every output. **`P1-1` and `OD-04` remain unresolved**, and
> §18.4.3 bars this run from establishing either.

`EV-2` is chosen as the **narrowest** rule, not the most realistic one. `EV-4` is deliberately
rejected despite being more flexible: a declared `N` is a parameter someone will eventually want to
vary, and varying it is provisional economic sensitivity, which §18.4.6 confines to a **separately
authorized** Mode-P decision.

---

## 6. Classification of every other unresolved item

Default is **DOES NOT BLOCK** unless repository authority demonstrates otherwise (§3, `MP-B-01`).

| Item | Classification | Basis / required disclosure |
| ---- | -------------- | --------------------------- |
| `P1-1` execution mapping | **DOES NOT BLOCK** | `MP-R-02` placeholder; §18.4.3 |
| `P1-2` Primary Proxy | **DOES NOT BLOCK** | Mode P is *defined* over not-yet-qualified data (§18.4.1); §18.4.3 bars establishing P1-2 |
| `P1-3` return composition | **DOES NOT BLOCK** | Must declare price-index vs total-return; materially affects magnitude, so disclosure is mandatory |
| `P1-4` cost / expense | **DOES NOT BLOCK** | Declare **zero costs modelled** as a stated approximation |
| `P1-5` start date | **DOES NOT BLOCK** | Declare an arbitrary provisional span; §18.4.3 **expressly** bars a Simulation Trial from deriving P1-5 |
| `P1-6` dataset cutoff | **DOES NOT BLOCK** | As `P1-5`; §18.4.3 and §18.4.7 both name it |
| `P1-7` currency | **DOES NOT BLOCK** | Declare the denomination and that **no FX conversion is modelled** |
| `P1-8` licensing / redistribution | **DOES NOT BLOCK the run; CONSTRAINS the storage** | Its text binds *"before any **raw data is committed**"*. Keeping data in the external store, as Mode E did, leaves it unengaged. **It blocks committing any raw data to the repository.** |
| `P1-9` revision / restatement | **DOES NOT BLOCK** | Use one **frozen snapshot**, hashed and dated; re-retrieval later is a new run, never a promotion |
| `M-1`, `M-2`, `M-3`, `M-5`, `M-8` | **DOES NOT BLOCK the run; CONSTRAINS reporting** | §18.3: methodology items are fixed *"before the metrics they govern are reported."* See `MP-D3` |
| `M-4` execution failure | **DOES NOT BLOCK** | Model no execution failure; declare it, as Mode E did |
| `M-6` zero-unit acceptance | **DOES NOT BLOCK** | Avoid by design, as Mode E did |
| `M-7` boundary tolerance | **DOES NOT BLOCK** | `MP-R-01` removes the need entirely |
| `O-4`, `M01`/`M02`/`M03` | **DOES NOT BLOCK** | Qualification-lane work; §18.4.8 keeps the lanes independent. **But see `MP-D4`** |
| Invariant 18 | **DOES NOT BLOCK** | Unreachable in the Simulation Trial; preserved as a limitation, not worked around |
| README debt | **DOES NOT BLOCK** | Deferred maintenance; must not gate simulation progress |

---

## 7. What actually blocks the first Mode-P run

Four decisions, none of which is `M-7` or `P1-1`.

> **MP-D1 — Mode-P authorization and execution plan. `[APPROVED — OWNER DECISION 2026-08-14]`** §18.4.1 is explicit: *"This specification
> authorizes NEITHER mode… Each requires its own separate Owner Decision and execution plan. A
> Mode-E authorization does not authorize Mode P."* This is a **formal precondition**, unavoidable
> and not satisfiable by any analysis in this artifact.

> **MP-D2 — Provisional dataset declaration. `[APPROVED — OWNER DECISION 2026-08-14]`** A run cannot exist without data. The Owner must fix:
> the dataset's identity and `dataset_class: provisional` (§18.4.9); a **single frozen snapshot**
> with retrieval date and SHA-256; the declared span; the return composition (`P1-3`) and
> denomination (`P1-7`); and that **raw data is not committed to the repository**, keeping `P1-8`
> unengaged and following the Mode-E external-store precedent.

> **MP-D3 — Reportable-output boundary. `[AMENDED AND APPROVED — OWNER DECISION 2026-08-14]`**
>
> This is the constraint the E4 recommendation missed entirely, and it bites harder than `M-7`. §18.3
> requires §19.2 methodology items to be *"fixed before the metrics they govern are reported"*, and
> §13.6 requires that *"All metric definitions MUST be fixed **before** results are inspected"*
> (Invariant 17), while §18.4.1 gives Mode P the purpose of *"behaviour comparison"* — which needs
> some comparable quantity.
>
> **The first bounded Mode-P run MUST NOT report or reconstruct TTEV or any other metric governed by
> `M-1 … M-8`.**
>
> **Permitted first-run outputs — definition-free engine quantities only:**
>
> - units acquired;
> - cash deployed;
> - cash remaining;
> - allocation count;
> - suppression count;
> - the ordered event log;
> - other existing Mode-E terminal-state fields **only** where they do not create, reconstruct,
>   approximate, or imply a governed metric.
>
> **Explicitly PROHIBITED:**
>
> - terminal exposure valued at the final observation;
> - TTEV;
> - XIRR;
> - CAGR;
> - return, in any form;
> - tracking statistics;
> - **any** terminal portfolio valuation;
> - **any combination** of reported quantities whose purpose is to reconstruct a metric governed by
>   `M-1 … M-8`.
>
> `M-1`, `M-5` and `M-8` **remain unresolved**. The first Mode-P run exists for **behavioural and
> mechanical observation, not performance evaluation.**
>
> Mode E's no-metric guard already enforces this and is carried over unchanged. Omitting terminal
> valuation costs little: because Invariant 3 gives A, B and C identical funding capacity, deployment
> timing and unit counts alone exhibit the behavioural difference Mode P exists to observe. Terminal
> valuation would add the single number most likely to be misread as performance.

> **MP-D4 — Anti-contamination acknowledgement. `[APPROVED — OWNER DECISION 2026-08-14]`** §18.4.7 bars Simulation Trial results from being
> used to select a candidate that performs better, to derive or redefine `P1-5`, to select `P1-6`
> opportunistically, to reinterpret `O-4`, or to weaken `HG-8`. Its **disclosure rule** then requires
> that *any* qualification decision taken after a Simulation Trial result exists must state that such
> results were known and affirm they were not used normatively. Because `O-4`, `M01`, `M02` and `M03`
> are **live and unfinished**, authorizing Mode P now attaches that disclosure duty to every
> subsequent qualification artifact. This is a real, permanent cost and it is the Owner's to accept
> deliberately — not a formality.

---

## 8. Exact remaining prerequisites after these decisions

Assuming `MP-D1`–`MP-D4` are decided and `MP-R-01`/`MP-R-02` adopted, what is left before a first run
is **engineering only**:

1. A Mode-P run driver reusing the preserved Mode-E engine, with `execution_mode: "P"` and
   `dataset_class: "provisional"` in the manifest (§18.4.9).
2. A provisional-data loader converting the frozen snapshot into the existing observation schedule
   shape — the engine's mechanics need no change.
3. Classification switched to exact scaled comparison per `MP-R-01`.
4. Mode-P output labelling extended with the §18.4.3 prohibited-use list and the
   `PROVISIONAL ECONOMIC SIMULATION` classification.
5. An external Mode-P evidence store, separate from the Mode-E store, with its own `PROVENANCE.md`
   and `SHA256SUMS`.

No new strategy semantics, no Baseline change, and no qualification-lane action is required.

---

## 9. Shortest path to the first bounded real-data simulation

| Step | Action | Gate |
| ---- | ------ | ---- |
| 1 | Owner reviews this artifact; decides `MP-D1`–`MP-D4`, `MP-R-01`, `MP-R-02` | Owner Decision |
| 2 | Preserve the resulting decision artifact | commit / push / tag |
| 3 | Owner authorizes a **bounded data-snapshot acquisition** — one source, one span, one snapshot, stored externally, uncommitted | separate authorization; **not** qualification research |
| 4 | Implement the Mode-P driver, loader and labelling (§8 above) | Mode-P execution plan |
| 5 | Execute the first bounded Mode-P run; verify determinism and replay as E4 established | evidence store |
| 6 | Report behaviour comparison in raw quantities only, labelled `NON-FORMAL — SIMULATION TRIAL` | §18.4.3 |

Step 3 is the only step requiring anything outside the repository, and it is deliberately isolated so
it cannot expand into qualification research. **Steps 1 and 2 are the entirety of the present
critical path.**

---

## 10. What this artifact does not do

It does not authorize any Mode-P implementation, dataset acquisition or run — §18.4.1 additionally
requires an execution plan, which does not yet exist; resolve `M-7`, `P1-1`, `OD-04`, or any other
`P1-x` / `M-x` item;
name, select, retrieve or evaluate a data source; alter any qualification-lane state, `O-4`,
`M01`/`M02`/`M03`, `HG-8`, or the criteria freeze; change the frozen strategy or any Baseline text;
authorize Phase 2, which remains **BLOCKED**; or modify any preserved artifact.

`SC-18` is **not engaged**: no normative frozen text requires modification for any recommendation
above.
