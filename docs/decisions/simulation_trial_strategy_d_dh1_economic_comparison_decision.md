# Simulation Trial — Strategy D Stage D-H1: A/B/C/D Economic Comparison Methodology (Design)

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14 — METHODOLOGY ONLY.**
**Owner approval date:** 2026-08-14

**NO A/B/C EXECUTION YET. NO NEW D EXECUTION. NO ECONOMIC VALUE COMPUTED. NO TERMINAL PRICE
INSPECTED.** This artifact fixes the D-H1 A/B/C/D economic-comparison methodology; it does not perform
the comparison. Approval of this methodology does not authorize A/B/C execution, a Strategy-D rerun, or
any economic computation — each remains a separate, not-yet-made Owner decision.
**Date drafted:** 2026-08-14
**Governing D-H1 chain:** dataset-selection policy `f8332a543f7bab4c8b5f42974813ccd70be9137f` ·
deterministic selection rule `f025bbf0dd5df9a4b037936822b1ced4e263948c` · bounded-release decision
`b722fb27ada370cf1adf22f6a8e5a99331a9a705` · mechanical-result checkpoint
`8a76769493cd690800011e518495a34b2a3c3e8b` — **none modified by this artifact.**
**Governing precedent (methodology template, not literally inherited — see §8):** Mode-P
terminal-valuation decision `00b2b4ac6e982511d5e74394125ed870e7ff6275`
(`MP-EV-D1`…`MP-EV-D4`), implementation `sim/engine/run_mode_p_terminal.py`.
**Governing Baseline:** v2, §18.4.3, §18.4.5, §18.4.6, §18.4.7, §18.4.9; Baseline Invariant 3
(§17); §13.1 TTEV definition; §19.1 (`P1-x`), §19.2 (`M-x`).

---

## 1. What this artifact does and does not do

Designs the minimum methodology needed to answer: *on the same frozen D-H1 input, under the same
funding assumptions and predeclared economic metrics, how do Strategies A, B, C, and D differ?* It
freezes metric definitions, the terminal-valuation rule, the reserved-cash treatment, the permitted
claim boundary, and the execution ordering — **before** any A/B/C run exists on D-H1 and before any
D-H1 economic value is computed. It does not run any strategy, compute any economic value, or inspect
any terminal price.

---

## 2. Repository authority reviewed

Read in full for this task: `f8332a5`, `f025bbf`, `b722fb2`, `8a76769` (re-verified unchanged, §21);
the Mode-P terminal-valuation decision (`00b2b4a`) and its implementation
(`sim/engine/run_mode_p_terminal.py`, `ALLOWED_RESULT_FIELDS`, `BANNED_NAME_TOKENS`, the exact
`simple_funding_relative_return` formula, the `simulator_paths_match_commit` safety gate); Baseline
v2 §18.4.3 (formal-result prohibition, permanent), §18.4.5 (experimental variants), §18.4.6
(sensitivity boundary — **provisional economic sensitivity is Mode-P-only, requiring its own Owner
Decision** — the exact authority this artifact exercises), §18.4.7 (anti-contamination), §18.4.9
(manifest requirement); §13.1 (`TTEV` formula); §17 Baseline Invariant 3 (identical annual funding
capacity across strategies); §19.1/§19.2 (`P1-x`/`M-x` register).

**No item permitted for the earlier D-H0/2018–2020 Mode-P evaluation is assumed to carry over
automatically.** Each is re-derived below from repository authority as it applies to D-H1 specifically.

---

## 3. Is a D-H1 A/B/C/D economic comparison governable now?

**YES**, via a narrow Simulation-Trial-lane Owner Decision — the same class of authority already used
for `MP-EV-D1`…`MP-EV-D4` — without touching the Frozen Baseline, without resolving general `M-x`
methodology, without resolving Primary Proxy qualification, without changing `P1-x` general states,
without changing Strategy D, and without contaminating qualification work.

**Exact authority.** §18.4.6 states explicitly: *"Provisional economic sensitivity — proxy-choice, FX,
expense or alignment perturbation intended to estimate materiality — Mode P only, requiring its own
Owner Decision."* A D-H1 economic comparison is exactly this class of question. §18.4.5 permits
executing an `EXPERIMENTAL VARIANT — NOT BASELINE` (Strategy D, already so labelled) without adopting
it. §18.4.3's bar on **"strategy superiority"** is **permanent and structural** — no Owner Decision
within the Simulation Trial lane can lift it (restated verbatim from `00b2b4a` §3, `MP-EV-D3`'s closing
sentence); this artifact does not attempt to lift it, only to permit **factual** quantities and
**factual** differences, exactly as `MP-EV-D3` already did once. §18.4.7 supplies the anti-contamination
disclosure mechanism already used twice in this chain (`73d6f51`, `b722fb2`) and extended a third time
here (§16). **No blocking decision was found.**

---

## 4. Experimental chronology (load-bearing, permanent record)

1. Strategies A, B, and C existed and were run before Strategy D was proposed.
2. Strategy D was proposed only after observing the earlier A/B/C mechanical result, specifically
   Strategy B's undeployed-cash behavior (`00b2b4a` §5).
3. The D-H1 dataset-selection policy (`f8332a5`) was then frozen.
4. The D-H1 deterministic selection rule (`f025bbf`) was then frozen.
5. The D-H1 input was selected mechanically, without price-value inspection (`f025bbf` execution,
   §14 of the prior task's report).
6. The D-H1 input was separately bounded-released (`b722fb2`), distinct from the earlier `73d6f51`
   release.
7. Strategy D alone was run first on D-H1 (`MP-DH1-D-001`, checkpoint `8a76769`).
8. Strategy D's D-H1 mechanical result is now known.
9. **A, B, and C have NOT yet been run on D-H1.**
10. **No D-H1 economic evaluation has yet been performed.**

Strategy D is **post-result relative to the original D-H0 window** (point 2) — that characterization is
unchanged and is not softened here. It is **not** ex-ante in that sense. What **is** true, and is the
entire basis for calling the D-H1 mechanical result independent, is narrower: the D-H1 **input
selection procedure** (points 3–6) was frozen and executed **before** D-H1's own result existed (points
7–8), and this economic-comparison **methodology** is now being frozen **before** the D-H1 A/B/C/D
economic result exists (points 9–10). These are two distinct, narrower claims, and neither is
overstated as general ex-ante status for Strategy D itself.

---

## 5. Comparison input — exactly the already-frozen bytes

| Field | Value |
| --- | --- |
| Instrument | `NDXJPY` |
| Window | `1985-01-31 → 1987-07-26` |
| Extracted comparison CSV | `~/research-materials/nasdaq-variable-dca-lab/simulation-trial-strategy-d-dh1-selection/dataset/DH1_NDXJPY_1985-01-31_1987-07-26.csv` |
| Extracted CSV sha256 | `4b4d076e6c1c22be88dab25a1506b5a625e8fd9a8082c6befb7fb09898584439` |
| Stage-D parent checksum | `316dd1a882002d28430a60a966a31601e3224b2bc84346c906f64715b38d52b0` |

Strategies A, B, C, and D must all run against this **exact** file — same bytes, same observations,
same `MP-R-02` execution-price mapping (untouched, unre-examined — `00b2b4a` §2), same annual-funding
parameters (`annual_units: "12.0"`, `unit_value_jpy: "10000"`, identical to the D run). No alternate
window, no second dataset, no replacement, no new acquisition, no span extension, no blending, no
result-dependent adjustment of any kind.

---

## 6. Strategy definitions — unmodified

Strategies A, B, C remain exactly Baseline v2 §4.1/§4.2/§4.3 (`OD-01`/`OD-09`/`OD-05`). Strategy D
remains exactly the implementation validated at `f16a815`/`486b994` and already executed, unmodified,
in `MP-DH1-D-001`. **No strategy is altered for comparison symmetry, and Strategy D is not altered
because its D-H1 mechanical behavior is now known** — doing so would itself be the exact hindsight
modification `f8332a5` §15/`DH1-R14` (extended from the strategy to its input) already treats as
disqualifying. If a structural difference (e.g., D's two-tranche capacity model vs. A/B/C's single
trigger) makes a metric incomparable, that limitation is disclosed (§12), not resolved by changing a
strategy.

---

## 7. Funding comparability

**Funding (the grant) is guaranteed structurally identical across all four strategies, by
construction — this is a parameter/methodology fact, not an economic result, and requires no A/B/C
execution to establish.** Baseline Invariant 3 (§17): *"All Baseline strategies receive identical
annual external funding capacity."* Strategy D's semantic decision (`62c5c42`, resolving `SD-1`…
`SD-10`) draws from the **same** `annual_units`/`unit_value_jpy` funding pool as A/B/C — it changes only
*when and how much* is deployed within that pool, never the pool's size. Running A, B, C, and D against
the identical dataset with identical `annual_units`/`unit_value_jpy` parameters (§5) therefore already
guarantees identical `cash_granted_jpy` across all four, by the same mechanism `00b2b4a` §2 cites for
the 2018-2020 window (*"identical for Strategies A, B and C by Invariant 3"*) — extended here, on the
same structural basis, to include D.

**One methodological fact, already disclosed in preserved evidence, not new inspection**: the
preserved `MP-DH1-D-001` `assertions.json` already shows three `BUDGET_GRANT` events (1985, 1986,
1987), each `"prorated": false` — the engine's annual-grant mechanism does not prorate a partial first
calendar year (the D-H1 window starts `1985-01-31`, not `1985-01-01`). This is a **non-strategy-specific
engine behavior**, governed by the same grant mechanism for all four strategies, not by any Strategy
A/B/C/D trigger logic — citing it here is confirming a structural methodology fact already on the
public record from the preserved D run, not inspecting a new D-H1 outcome to select a favorable metric.

**Deployment** (`cash_deployed_jpy`, `cash_remaining_jpy`, reservation timing) **will differ by
strategy — that is the comparison's subject, not a confound**, provided funding itself is identical,
which it structurally is. The methodology below therefore explicitly separates:

- **FUNDING DIFFERENCE** — none expected, none permitted to exist unexamined; if any run's
  `cash_granted_jpy` differs from the others, this is an `EvidenceSafetyError`-class integrity failure
  (mirroring `run_mode_p_terminal.py`'s existing fail-closed cross-check), not a reportable comparison
  finding, and blocks the comparison pending Owner Review.
- **DEPLOYMENT DIFFERENCE** — the actual subject of the comparison, reported via the metrics in §10.

---

## 8. Terminal valuation

`MP-EV-D1`'s **rule** (*"value already-acquired exposure units at the close of the final available
observation in the released dataset"*) is a reusable **methodology template**. Its **decision text**
is not reusable as-is: it hardcodes the 2018-2020 dataset's identity, checksum, final date, and final
price (`2020-06-26`, close `1000`). Per §18.4.6, a new dataset requires its own Owner Decision — the
prior decision cannot simply be inherited by reference.

**Recommended `DH1-EV-D1`** (fresh, D-H1-specific, structurally identical rule):

> Terminal valuation price = close of the D-H1 dataset's final observation. The final observation's
> **date** is already known from preserved extraction metadata (`1987-07-24` — the last date row in
> the extracted CSV; a date is not a price and its citation here is not price-value inspection). The
> final observation's **price** is deliberately **not** stated in this artifact and must remain unknown
> until economic execution, verified programmatically from the preserved dataset file itself (mirroring
> `run_mode_p_terminal.py`'s `_verify_terminal_price()`, which reads the value from bytes rather than
> trusting a literal) rather than by a human reading the CSV.

This is **not** a `P1-1` determination; it does not alter `MP-R-02`; it does not alter qualification
state — identical scope discipline to `MP-EV-D1`.

---

## 9. Reserved-but-unexecuted treatment — predeclared before results

**Recommended `DH1-EV-D2`**: adopt `MP-EV-D2`'s accounting treatment verbatim, predeclared now,
**regardless of whether it turns out to be load-bearing for D-H1** (unlike the 2018-2020 window, it is
not yet known whether any strategy will hold a reservation at the D-H1 window's exact final
observation — that is an A/B/C/D execution-time fact, not inspected here). Reserved-but-unexecuted
allocations remain **cash**, never exposure, disclosed **separately**. A D-H1 terminal report must
include, at minimum: (1) cash available; (2) cash reserved but unexecuted; (3) total unconverted cash
(1+2); (4) acquired (executed) exposure units and their `DH1-EV-D1` valuation. **PROVISIONAL `M-5`
PRESENTATION — MODE P / D-H1 ONLY**; general `M-5` remains OPEN.

---

## 10. Minimum economic metric set — classified

| # | Field | Classification | Grounding |
| - | --- | --- | --- |
| A | `cash_granted_jpy` | **PERMITTED NOW** | Already an existing `MP-D3`-permitted mechanical Mode-P field (`run_mode_p.py` `PERMITTED_TERMINAL_FIELDS`); already reported in `MP-DH1-D-001` |
| B | `cash_deployed_jpy` | **PERMITTED NOW** | Same — already `MP-D3`-permitted mechanical field |
| C | `cash_remaining_jpy` | **PERMITTED NOW** | Same |
| D | `reserved_but_unexecuted_jpy` | **PERMITTED WITH NEW NARROW OWNER DECISION** | The underlying unit count (`budget_units_reserved_outstanding`) is already mechanically permitted; converting to JPY and fixing its accounting treatment (cash side, not exposure) is a methodology decision (§9, `DH1-EV-D2`) |
| E | `total_unconverted_cash_jpy` | **PERMITTED WITH NEW NARROW OWNER DECISION** | Sum of two categories under D; same decision |
| F | `exposure_units_held` | **PERMITTED NOW** | Already `MP-D3`-permitted mechanical field |
| G | `terminal_valuation_price` | **PERMITTED WITH NEW NARROW OWNER DECISION** | Exactly the load-bearing question `MP-EV-D1` resolved narrowly before; needs its own D-H1 version (§8, `DH1-EV-D1`); general `P1-1` untouched |
| H | `terminal_exposure_market_value` | **PERMITTED WITH NEW NARROW OWNER DECISION** | Depends on G |
| I | `combined_terminal_value` | **PERMITTED WITH NEW NARROW OWNER DECISION** | Sum of H + E; exactly `MP-EV-D3` item 5's *"combined terminal economic value / TTEV"* class, same mandatory label `MODE-P TERMINAL ECONOMIC VALUE — NOT BASELINE TTEV — SIMULATION-TRIAL ONLY` |
| J | funding-relative simple return | **PERMITTED WITH NEW NARROW OWNER DECISION** | Exact formula `(combined_terminal_value − cash_granted_jpy) / cash_granted_jpy`, identical to `MP-EV-D3` item 7; denominator (`A`) already unambiguous, so no new methodology question is opened |
| K | deployment ratio (`B / A`) | **PERMITTED WITH NEW NARROW OWNER DECISION** | New field beyond the literal `MP-EV-D3` list, but follows the **identical** reasoning already used for J: a ratio of two already-permitted fields with an already-fixed, unambiguous denominator. No new methodology question |
| L | residual-cash ratio (`E / A`) | **PERMITTED WITH NEW NARROW OWNER DECISION** | Same reasoning as K |

**None of A–L requires resolving general `M-x` or `P1-x`.** `D`, `E`, `G`, `H`, `I`, `J`, `K`, `L` each
require the same class of narrow, dataset-specific Owner Decision already exercised once (`00b2b4a`) —
not a new category of decision, just its D-H1 instance.

---

## 11. Sophisticated metrics — explicitly reviewed and deferred

| Metric | Disposition | Why |
| --- | --- | --- |
| `CAGR` | **PROHIBITED** | Explicitly barred, unchanged, by `MP-EV-D3`'s own list; requires no new resolution — restated, not reopened |
| `XIRR` / money-weighted return | **PROHIBITED** | Same; would additionally require `M-1`'s exact-formula resolution (§19.2), which remains OPEN and off the critical path |
| Annualized / time-weighted return | **PROHIBITED** | Same class as `CAGR` |
| Sharpe ratio | **PROHIBITED** | Requires a risk-free-rate/volatility methodology never defined; not clearly governed |
| Volatility | **PROHIBITED** | Not clearly governed; no existing formula authority |
| Maximum drawdown **of portfolio value** (distinct from the already-computed price-reference-high zone `dd`) | **PROHIBITED** | A new metric requiring its own numeric-tolerance methodology (`M-7`-adjacent) not currently authorized for this purpose |
| Tracking error | **PROHIBITED** | Explicitly barred by `MP-EV-D3`'s list |
| Risk-adjusted return | **PROHIBITED** | Composite of the above; same reasoning |
| Statistical significance / confidence intervals | **PROHIBITED** | `M-8` (§19.2) was found **not required** for exactly this reason in `00b2b4a` §2 (*"single-path, non-statistical, non-probabilistic observation"*) — adding these would newly require resolving `M-8`, contrary to the default-toward-deferral instruction |

None of these are added merely because they are common investment metrics. Each would either reopen an
explicitly OPEN `M-x` item or introduce a methodology question with no existing governing formula. The
first D-H1 A/B/C/D comparison stays as small and auditable as the first 2018-2020 one was.

---

## 12. Factual comparison vs. superiority claim — frozen before results

**Permitted factual statement forms** (mirroring `00b2b4a` §3 item 6 and §4 verbatim):

- "Strategy X deployed ¥N more/less than Strategy Y on this window."
- "Strategy X retained ¥N more/less unconverted cash than Strategy Y."
- "Strategy X ended with N more/less exposure units than Strategy Y."
- "Combined terminal value differed by ¥N between Strategy X and Strategy Y."
- "Funding-relative simple return differed by N percentage points between Strategy X and Strategy Y."

**Prohibited, unless separately and explicitly justified by a future, distinct Owner Decision**:
"Strategy D is better"; "Strategy D solves Strategy B's cash drag"; "Strategy D should replace B";
"Strategy D is more efficient"; "Strategy D is more robust"; "Strategy D generalizes better"; any
"optimal"/"superior"/"proven" characterization. **A numerical ordering is not automatically a
superiority claim** — reporting that X's terminal value exceeds Y's is a factual difference; asserting
that this makes X *better* is the prohibited step, and is a distinct, separately-gated inferential act
this artifact does not authorize.

---

## 13. Strategy-D hypothesis-test boundary

**HYPOTHESIS-MECHANISM OBSERVATION** (permitted): whether the specific mechanism Strategy D was
designed to change — Strategy B's undeployed-cash behavior — actually manifests differently for D on
this window. E.g., *"D deployed more cash than B on this window"* is a permitted factual statement
about **mechanism**, because it is exactly the deployment-timing difference D was built to produce.

**ECONOMIC SUPERIORITY** (prohibited): that this mechanism difference produced a **better investment
outcome**. A higher terminal value for D on this one window does not establish general superiority,
robustness, or that the mechanism is economically beneficial — §17 restates why.

**Strongest permissible claim, defined now, before any result exists:**

> On this one independently-selected D-H1 window, Strategy D's deployment behavior did or did not
> differ from Strategy B's in the direction its hypothesis predicted, by a stated factual amount. This
> is a mechanism observation on one window. It is not evidence of economic superiority, robustness, or
> generalization, and does not by itself justify adoption.

---

## 14. Recommended A/B/C execution ordering

Follow the already-established, already-precedented two-phase pattern exactly (mechanical run first,
economic layer second — the same sequence `MP-H1`/`MP-H2` then `MP-EV`/`MP-EV2` already used, and the
same sequence Strategy D itself just followed on D-H1):

1. Run Strategy A on the D-H1 input, mechanical-only (`run_mode_p.py`, unmodified) — preserve.
2. Run Strategy B, mechanical-only — preserve.
3. Run Strategy C, mechanical-only — preserve.
4. Verify determinism for each (two independent executions, byte-identical payloads — same discipline
   already applied to D in `MP-DH1-D-001`).
5. **Only then**, open the economic-evaluation step (a new, D-H1-scoped `run_mode_p_terminal.py`-style
   reporting layer) for all four preserved mechanical results together.

This is the minimum-new-architecture path: it reuses `run_mode_p.py` unmodified for steps 1–3 (exactly
as already done for D), and requires only a D-H1-scoped adaptation of the existing, already-vetted
`run_mode_p_terminal.py` pattern for step 5 (new `DATASET_SHA256`, new terminal-price verification
against the D-H1 file, new `ALLOWED_RESULT_FIELDS` extended per §10). No single combined run is
recommended — it would weaken the existing per-run evidence-safety gate (`run_id` reuse protection)
and offers no cost saving over the already-proven sequential pattern.

---

## 15. Reuse of the preserved D mechanical result

**Recommended: reuse `MP-DH1-D-001` — do not rerun Strategy D.** No technical necessity requires a
rerun. `run_mode_p_terminal.py`'s existing `load_source()` already gates on
`manifest["simulator_paths_match_commit"]` being `true` before building any economic report from a
source run — this is a pre-existing safety gate, not new design, and it must be satisfied (already
expected to hold: `sim/` was verified clean at `MP-DH1-D-001`'s execution time, and remains clean now,
§21) before the future economic-evaluation implementation consumes it. Economic evaluation should
compute strictly from `MP-DH1-D-001`'s preserved `terminal_state.json`, exactly as `MP-EV`/`MP-EV2`
already computed from `MP-H2-*-001`'s preserved states without re-running A/B/C.

---

## 16. Anti-contamination — extended, not duplicated

**Recommended `DH1-EV-D4`**, restating and extending the standing §18.4.7 obligation (already attached
by `b722fb2` and, before it, `73d6f51`), unchanged and unweakened:

- Strategy D was proposed post-result relative to the original D-H0 (2018-2020) A/B/C result.
- D-H1 was selected under the frozen, metadata-only deterministic rule (`f025bbf`), independently of
  D-H1's own outcome.
- D-H1's Strategy-D mechanical behavior is now known (`MP-DH1-D-001`).
- Economic metric definitions are being frozen **only now**, before any D-H1 A/B/C economic comparison
  exists.
- No D-H1 A/B/C economic comparison exists yet.

Any future artifact deciding `O-4`, `P1-2`, `P1-5`, `P1-6`, `HG-8`, Stage G, Stage H, or Primary Proxy
selection MUST state that the D-H1 mechanical result, and — once it exists — the D-H1 A/B/C/D economic
comparison, were known, and affirm they were not used normatively. This obligation is **not** weakened
by this artifact.

---

## 17. One-window evidentiary ceiling

D-H1 is **one** independently-selected window. Regardless of the eventual comparison result, it cannot
by itself establish robustness, generalization, statistical superiority, optimality, adoption, or
Baseline replacement — for any strategy, in either direction. A desire for further evidence (additional
windows, formal Phase-2 execution) is a **separate**, not-yet-made research-design decision; **no**
additional window is pre-authorized by this artifact.

---

## 18. `DH1-EV-D1`…`DH1-EV-D12` decision matrix

| ID | Question | Recommended disposition | Alternatives | Rationale | Risk | Cost | Further decision needed? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DH1-EV-D1` | Terminal valuation rule | Close of D-H1 dataset's final observation, verified from bytes, price unstated until execution (§8) | Average of last N observations; explicit fixed date chosen in advance | Mirrors `MP-EV-D1` exactly; simplest, zero free parameters | Low — same class already Owner-approved once | Low | **Yes — Owner approval of this artifact** |
| `DH1-EV-D2` | Reserved-but-unexecuted treatment | Four-field breakdown, cash-side, predeclared (§9) | Treat reservations as provisional exposure | Mirrors `MP-EV-D2` exactly; avoids overstating exposure | Low | Low | **Yes** |
| `DH1-EV-D3` | Funding-comparability guarantee | Identical `cash_granted_jpy` structurally guaranteed by Invariant 3 + shared parameters (§7); any divergence is a fail-closed integrity error, not a finding | Empirically verify post-hoc only | Establishes the funding/deployment distinction before results exist | Low | Low | No — follows directly from existing Invariant 3 |
| `DH1-EV-D4` | Permitted economic fields | §10 table (A–L), 8 of 12 requiring this decision | Broader or narrower set | Minimum sufficient to answer the research question (§10) | Low–Medium | Low | **Yes** |
| `DH1-EV-D5` | Funding-relative simple-return definition | `(combined_terminal_value − cash_granted_jpy) / cash_granted_jpy`, identical to `MP-EV-D3` item 7 | A different denominator | Denominator already fixed and unambiguous (`cash_granted_jpy`) | Low | Low | **Yes** (new field instance, same formula) |
| `DH1-EV-D6` | Deployment / residual-cash ratios | `cash_deployed_jpy / cash_granted_jpy`; `total_unconverted_cash_jpy / cash_granted_jpy` | Omit; defer to a later decision | Same reasoning class as `DH1-EV-D5`; no new methodology question | Low | Low | **Yes** |
| `DH1-EV-D7` | A/B/C/D factual-difference reporting | Absolute-difference statements only, computed from already-permitted fields (§12) | Also report relative/percentage differences | Matches `MP-EV-D3` item 6 exactly | Low | Low | **Yes** |
| `DH1-EV-D8` | Superiority/adoption claim prohibition | Structural, permanent, per §18.4.3 — restated, not newly created | N/A — not liftable within this lane | §18.4.3 cannot be lifted by any Simulation Trial Owner Decision | N/A | None | No — already fixed by Baseline |
| `DH1-EV-D9` | A/B/C execution procedure | Sequential mechanical runs, then economic layer (§14) | Single combined run | Reuses proven architecture; preserves per-run evidence-safety gate | Low | Low (reuses `run_mode_p.py` unmodified) | **Yes** (authorizes execution — separate future task) |
| `DH1-EV-D10` | Reuse of preserved D mechanical state | Reuse `MP-DH1-D-001`; verify `simulator_paths_match_commit` before consuming it | Rerun D | No technical need to rerun; avoids redundant evidence generation | Low | None (reuse) | No — mechanical, gated by an existing safety check |
| `DH1-EV-D11` | §18.4.7 disclosure | Extended per §16, unweakened | N/A | Consistent with `73d6f51`/`b722fb2` precedent | Low | Low | **Yes** (formal restatement) |
| `DH1-EV-D12` | One-window evidentiary ceiling | Predeclared per §17; no further window pre-authorized | Pre-authorize a second window now | Keeps this decision minimal; a second window is a distinct research-design question | Low | None | No — a non-decision (explicit non-authorization) |

---

## 19. Cost/value discipline

Every recommended control reuses an already-approved precedent (`MP-EV-D1`…`D4`, `run_mode_p_terminal.py`'s
allow-list/ban-list architecture, the existing sequential mechanical-then-economic run pattern) rather
than inventing new infrastructure. The only genuinely new artifacts required downstream are: (a) a
D-H1-scoped constant set (`DATASET_SHA256`, terminal-price verification path) in a copy or parameterized
variant of `run_mode_p_terminal.py`, and (b) three ordinary `run_mode_p.py` invocations for A/B/C — no
new engine logic, no new strategy code, no new market-data infrastructure. This satisfies the stated
goal: minimum controls sufficient to prevent hindsight metric selection, accidental Baseline mutation,
unfair funding comparison, economic-field leakage, and overclaiming a one-window result — nothing more.

---

## 20. Unresolved questions carried forward, not resolved here

Whether a second independent-validation window is ever pursued (§17); whether Strategy D is ever
formally adopted (requires Phase 2, `§18.4.4`, entirely separate); the general resolution of `P1-1`,
`M-1`, `M-5`, `M-8` (all remain OPEN in general, resolved only narrowly and provisionally for this
Mode-P/D-H1 use, exactly as `00b2b4a` left them for the 2018-2020 case).

---

## 21. Repository state re-verified for this design task

`HEAD == origin/main == 8a76769493cd690800011e518495a34b2a3c3e8b`. `f8332a5`, `f025bbf`, `b722fb2`
checksums unchanged. `sim/` byte-identical to `486b994` (its last modifying commit) — zero drift. No
strategy was executed, no economic value was computed, and no terminal price was inspected in preparing
this artifact.

---

## 22. Scope

This artifact designs a methodology only. It does not run Strategy A, B, C, or D; does not compute any
economic value; does not inspect the D-H1 window's terminal price; does not modify the Frozen Baseline,
Strategy D, the D-H1 policy/rule/release/checkpoint chain, or any preserved evidence generation; and
does not authorize A/B/C execution, D rerun, or economic computation — those remain separate,
not-yet-made Owner decisions.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14 — METHODOLOGY ONLY. No A/B/C
execution yet. No new D execution. No economic value computed. No terminal price inspected. Approval
fixes the methodology only; it does not authorize A/B/C execution, a Strategy-D rerun, or any economic
computation. `f8332a5`, `f025bbf`, `b722fb2`, `8a76769`, and every preserved Strategy-D and Mode-P
evidence generation are unchanged.**
