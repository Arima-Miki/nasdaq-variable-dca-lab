# Simulation Trial — Strategy D Stage D-H1 Deterministic Selection Rule (Design)

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14 — DETERMINISTIC SELECTION RULE ONLY.**
**Owner approval date:** 2026-08-14

**Approval of this rule DOES NOT:**
- execute the rule;
- select a dataset;
- select an instrument;
- select a window;
- authorize price-value inspection;
- authorize Strategy D execution;
- authorize economic evaluation.

This artifact designs a function; approval fixes that function's definition. It does not authorize
evaluating that function against the actual candidate universe. **RULE DESIGN ONLY. NOT EXECUTED. NO
DATASET SELECTED. NO WINDOW SELECTED. NO PRICE VALUES INSPECTED.** The freeze-before-reveal boundary
(§13) remains intact; execution under this rule is a separate, not-yet-authorized future task.
**Date drafted:** 2026-08-14
**Governing policy (controlling for D-H1 selection):** `docs/decisions/
simulation_trial_strategy_d_dh1_dataset_selection_policy.md`, commit `f8332a543f7bab4c8b5f42974813ccd70be9137f`,
tag `simulation-trial-strategy-d-dh1-dataset-selection-policy-20260814` — **not modified by this artifact.**
**Governing Strategy-D chain:** hypothesis `5a3f54a` · semantics `62c5c42` · Mode-E E5 `f16a815` ·
D-H0 mechanical validation `486b994`

---

## 0. Purpose and scope

The approved policy (`f8332a5`) fixes **what counts as unseen, what mechanisms are legitimate, and
how the four instrument/source options rank.** It does not yet specify a **mechanical procedure** that
takes those rules as input and produces exactly one candidate as output, with no execution-time
judgment call left over. This artifact designs that procedure. It is deliberately abstract about the
*result* — every rule below is stated as a function of metadata that has not been evaluated here, so
that reading this artifact does not itself constitute selection.

**Metadata used in designing this rule** (dates, row counts, retrieval dates — never price values) is
drawn from repository documentation already established prior to this task:

| Candidate | First observation | Last observation | Observation count |
| --- | --- | --- | --- |
| `NDXJPY` (Stage-D `E-01`) | `1985-01-31` | `2020-06-26` | `8,926` |
| `XNDXJPY` (Stage-D `E-02`) | `1999-03-04` | `2020-06-26` | `5,366` |
| `XNDXNNRJPY` (Stage-D `E-03`) | `2007-07-09` | `2020-06-26` | `3,268` |

Released D-H0 span (`73d6f51`): `2018-01-02` → `2020-06-26` (`626` observations). These are the only
facts this design relies on; none require reading a single price value.

---

## 1. Achievability of zero material discretion

**ZERO MATERIAL EXECUTION-TIME DISCRETION: ACHIEVED**, across all four options and the full cross-tier
traversal. The three numeric parameters previously open are Owner-approved and formalized with zero
residual interpretation:

1. window-length duration (`DH1-R3`) = `906` calendar days, computed by exact date subtraction (§5.1);
2. temporal-distance backstop (`DH1-R5`) = `1825`-day ordinal-difference floor, never "5 years" (§5.2);
3. continuity/discontinuity threshold (`DH1-R6`) = `90%` of a weekday-count denominator (§7).

**The one previously-flagged residual — Option D's within-category candidate ordering — is now closed**
(§10.1–§10.3): a five-level lexicographic hierarchy, terminating in a strictly discriminating lexical
identifier comparison that always produces a unique winner, together with a complete traversal algorithm
resolving exactly how `MP-S-07`'s own two clauses — the first-Class-A/B-candidate stopping rule and the
three-candidate-per-round investigation cap taken "in the declared order" — compose once a within-
category ordering exists. (Re-verified directly against the governing policy text: `MP-S-07`, §8, is the
single rule containing both the stopping condition and the three-candidate cap and search-order list;
`MP-S-08`, §9, is the separate FRED fail-closed precedent and is not a source of general search-budget
or ordering rules. An earlier draft of this section mislabeled part of this as an "`MP-S-07`/`MP-S-08`
interaction" — corrected here, recorded openly, not silently fixed.) This closure is scoped narrowly to
D-H1's Option D and does not modify the underlying Mode-P source-selection policy (§10.3).

---

## 2. Policy-tier traversal (`DH1-R1`)

```
evaluate(Option A)
  if ALL eligibility tests pass (§3):  SELECT A.  STOP.
  else: record rejection code(s); evaluate(Option B)

evaluate(Option B)
  if the higher-ranked of {XNDXJPY, XNDXNNRJPY} (§7 ordering) passes ALL eligibility tests:
      SELECT it.  STOP.
  elif the lower-ranked one passes:      SELECT it.  STOP.
  else: record rejection code(s); evaluate(Option C)

evaluate(Option C)
  if the deterministic chronological-holdout construction (§8) can be fully satisfied
  (complete requested span obtainable, no partial window): SELECT C.  STOP.
  else: record rejection code(s); evaluate(Option D)

evaluate(Option D)
  apply the bounded, inherited MP-S-07 search (§8) to a pre-fixed, metadata-only
  eligible universe, at most three candidates.
  if one passes: SELECT it.  STOP.
  else: D-H1 BLOCKED — NO ELIGIBLE INPUT (§13). Return to Owner Review.
```

**No tier is ever skipped without an objective, predeclared rejection code recorded first** (mirrors
`f8332a5` §16A's fallback rule and §10's replacement policy exactly — this is not a new principle,
only its mechanical expression). Cost never overrides methodology silently: Option B can only be
reached by A's objective failure, never by B simply appearing cheaper while A remains eligible.

---

## 3. Option-A eligibility (`DH1-R2`) — mechanical, metadata-only

**`DATA EXISTS` tests** (structural, already-established facts, not new inspection):

| Test | Rejection code on failure |
| --- | --- |
| `BYTE_AVAILABILITY` — the Stage-D `E-01` file exists at its recorded path; its SHA-256 matches `primary-proxy-stage-d/SHA256SUMS` | `CHECKSUM_UNSTABLE` |
| `PROVENANCE_INTEGRITY` — the `PROVENANCE.md` record correctly attributes `E-01`, retrieval date, and the `S.2` caveat | `PROVENANCE_INVALID` |
| `SCHEMA_COMPATIBILITY` — file structure satisfies the unmodified `csv_loader.py` contract (already demonstrated by the D-H0 extraction) | `SCHEMA_INCOMPATIBLE` |

**`DATA IS ELIGIBLE FOR D-H1` tests** (the anti-hindsight-specific layer):

| Test | Rejection code on failure |
| --- | --- |
| `OVERLAPS_DH0` — the candidate window (§4) does not intersect `[2018-01-02, 2020-06-26]` | `OVERLAPS_DH0` |
| `ALREADY_SEEN` — no repository artifact references, summarizes, or computes any price/value/statistic for the candidate region | `ALREADY_SEEN` |
| `SPAN_INSUFFICIENT` — the eligible non-overlapping region's calendar span meets or exceeds the window-length rule (§5) | `SPAN_INSUFFICIENT` |
| `RETENTION_NOT_PERMITTED` — the same eight-axis / `S.2` analysis that already cleared `NDXJPY` for Mode-P use (`73d6f51`) extends without new obstruction to the candidate span; a **new, separate bounded-release decision is still required before use** — this test only confirms nothing *new* blocks it | `RETENTION_NOT_PERMITTED` |

**Note, not a conclusion:** applying these tests to the actual `1985-01-31`→`2017`-portion of `E-01`
is **execution**, out of scope here. This artifact designs the tests, not their result.

---

## 4. Non-overlap and prior-release scope (feeds `OVERLAPS_DH0`)

Non-overlap is checked against the **exact released span** `2018-01-02`→`2020-06-26` (`73d6f51`) —
calendar-date comparison only. D-H0's engine used no warm-up data before `2018-01-02` (ATH state was
initialized from the first observation of the released span itself), so no pre-release portion of
`E-01` carries any indirect exposure through the engine's own state — the eligible non-overlapping
region for Option A is the entirety of `E-01` outside `[2018-01-02, 2020-06-26]`, i.e. approximately
`1985-01-31`→`2017`'s last trading day (~33 years, ~8,300 observations, by row-count arithmetic — not
inspected further here).

---

## 5. Window length (`DH1-R3`) and temporal-distance rule (`DH1-R5`) — **APPROVED, formalized**

### 5.1 Window length — `DH1-R3`

**Formula:** `window_duration_days = (D-H0_end_date − D-H0_start_date).days`, using ordinary calendar-
date subtraction (the same `datetime.date` semantics already used natively throughout `engine.py`).
`D-H0_start_date = 2018-01-02` and `D-H0_end_date = 2020-06-26` are already-published, already-fixed
boundary dates from the preserved D-H0 release (`73d6f51`) — not re-derived, not re-inspected, not
price-dependent.

**Computed value:** `window_duration_days = 906`. This is pure calendar arithmetic on two dates already
public since `73d6f51`; verified independently (`date(2020,6,26) − date(2018,1,2) == 906 days`).

**Exactly what is reused, and what is not** (per Owner clarification): **only** this integer, `906`.
Not the dates themselves, not the months, not any market event, not any inspection of D-H0's price
behavior. `906` is a pre-existing structural experiment parameter, reused by arithmetic identity alone.

**No repository-authority conflict found** — the rule is not mechanically undefined or inconsistent
(both boundary dates are exact and unambiguous; date subtraction is a total, deterministic operation).
`36` months is therefore **not substituted**; no STOP condition is triggered.

A candidate window's own end date is then `candidate_start_date + timedelta(days=906)`, where
`candidate_start_date` is resolved by §6.

### 5.2 Temporal-distance backstop — `DH1-R5`

**Two layers, unchanged in structure, now fully formalized:**

1. **Constructive layer (primary):** combined with §6's "earliest eligible window," distance from D-H0
   is maximized by construction — no threshold evaluation is needed for this layer to hold.
2. **Backstop layer (defensive redundancy) — formalized without ambiguity:**

   ```
   D-H0_start_date.toordinal() − candidate_window_end_date.toordinal()  >=  1825
   ```

   **The normative term is exactly `1825` calendar days — not "5 calendar years."** `5 × 365` is shown
   only to derive `1825`; it is never itself the operative rule, because five *anniversary* years can
   themselves span one or two leap days depending on placement, making "5 years" an ambiguous quantity
   in days. `1825` is described informally elsewhere as "roughly five years" for human readability only
   — every executable instance of this rule tests `>= 1825`, never a year-count. **Why ordinal-day
   arithmetic, not "add 5 years to a date":** the
   latter (`date(year−5, month, day)`) has a genuine edge case at `month=2, day=29` when `year−5` is
   not a leap year, which would silently require an interpretive fallback — exactly the kind of hidden
   discretion the Owner asked to eliminate. Pure ordinal-day subtraction has no such edge case: it is a
   total function over any two valid dates, with one unique answer always.

   **Why `365`, not `365.25`:** this project already treats "calendar year" as a **flat, non-leap-
   prorated unit** for policy/threshold purposes elsewhere in the frozen Baseline (§11.1: *"12.0 units
   at the beginning of each calendar year"*, never prorated for leap years) — `1825` follows that same
   existing convention rather than introducing a new one.

   **Confirmed non-binding under §6:** the earliest-window positioning (§6) places the candidate
   window's end date at `1985-01-31 + 906` days ≈ `1987` — roughly `30` calendar years before
   `2018-01-02`, vastly exceeding the `1825`-day floor. The backstop is satisfied automatically under
   the primary positioning rule and activates only as a check against a **future** revision of §6, or
   against an unexpected eligibility exclusion that shrinks the earliest-available eligible region —
   exactly the purpose the Owner specified, never an economic-sufficiency test.

---

## 6. Window-position rule (`DH1-R4`)

**Recommended: the earliest eligible window** — start at the eligible region's first available
observation (`1985-01-31` for `E-01`), running forward for the fixed duration (§5).

**Why not the alternatives:**
- *Latest eligible window* (immediately before `2018-01-02`) would **undermine Option A's own stated
  purpose** — it reintroduces essentially the same temporal-adjacency concern the policy sought to
  reduce for Option A, just facing backward instead of forward.
- *Midpoint-derived* adds an arbitrary "midpoint of what, weighted how" definition without a clear
  benefit over the extreme, zero-parameter "earliest" rule.
- *Deterministic hash/seed-derived* remains available as a fallback only if the Owner wants defense
  against a hypothetical "why earliest and not some other point" critique — but it requires defining
  an unmanipulable seed source, adding its own design surface for no clear gain here, since "earliest"
  already has zero free parameters and a one-sentence justification.

**Recommended: earliest eligible window, unconditionally** — the simplest mechanism giving one unique
answer with the fewest researcher degrees of freedom, exactly as the Owner asked to prefer.

---

## 7. Continuity / gap rule (`DH1-R6`) — **APPROVED, formalized**

The existing, unmodified `csv_loader.py` contract **already** performs no gap-filling, no
interpolation, no reordering, and requires only strictly increasing dates — ordinary non-trading-day
gaps (weekends, holidays) are already tolerated by construction, since the file simply omits those
dates and the engine processes whatever observations exist in order. **No new gap-handling
infrastructure is needed.**

**Implementability check, resolved without a STOP.** A `~252`-trading-days/year approximation (the
figure in the prior draft) is not itself deterministic without a market-holiday calendar — and the
repository deliberately has **no** such calendar (`engine.py`'s own `is_final_observation_of_month`
explicitly avoids importing a real-market trading-calendar dependency, by design, for exactly this
reason). Building one now would be the "complex new market-calendar subsystem" the Owner ruled out.

**Formalized denominator — weekday count only, zero external data, zero holiday enumeration:**

```
expected_trading_days(start, end) = count of dates d in [start, end]
                                     such that d.weekday() in {Mon, Tue, Wed, Thu, Fri}
```

This is a **pure calendar-arithmetic function** of the two boundary dates — no lookup table, no
jurisdiction-specific holiday list, no new "capability" beyond ordinary date iteration already native
to the existing codebase's date handling. It answers "how many weekdays fall in this window," not "how
many trading days," and is therefore unambiguous and total.

**Why this satisfies the Owner's "normal weekends/holidays must not count as missing" requirement:**
weekends are excluded from the denominator entirely (never counted as "expected" at all — not merely
tolerated). Holidays remain formally counted as expected weekdays, but a typical year has roughly `252`
trading days against roughly `260`–`261` weekdays — i.e. holiday absences are normally **within**
`3`–`4%` of the weekday count, comfortably inside a `90%` floor. Ordinary holiday gaps are therefore
absorbed by the threshold's slack, never individually enumerated or special-cased.

**Formalized rule:**

```
observed_count(candidate) / expected_trading_days(candidate_start, candidate_end)  >=  0.90
```

If this ratio falls below `0.90`: `SCHEMA_INCOMPATIBLE`. This is an anomalous-discontinuity /
data-integrity test only — never a market-quality or performance filter, and it cannot be satisfied or
failed by any property of the observed price *values*, only by the observed *count* of rows.

---

## 8. Option-B ordering (`DH1-R7`)

Hierarchy, applied only if Option A is objectively rejected:

1. **Construct comparability**, assessed from naming-convention and provenance metadata only (never
   price content): Nasdaq's `X`-prefix convention is consistent with a total-return variant, and `NNR`
   with a *net* total-return variant (dividends reinvested net of withholding tax) — meaning
   `XNDXNNRJPY` carries **one additional layer of divergence** from `NDXJPY`'s price-return construct
   beyond what `XNDXJPY` carries. **This inference is recorded as naming-convention-based, not a
   confirmed repository fact**, and should be verified against each file's own provenance record
   (still metadata, not values) before being relied upon at execution time. On this basis, `XNDXJPY`
   ranks above `XNDXNNRJPY`.
2. **Provenance completeness** — whichever has the more complete Stage-D provenance record (both
   retrieved the same day; expected to tie).
3. **Span sufficiency** — whichever has more available non-overlapping, eligible observations
   (`XNDXJPY`: `1999-03-04`→`2020-06-26`, `5,366` obs.; `XNDXNNRJPY`: `2007-07-09`→`2020-06-26`,
   `3,268` obs. — both metadata facts already on record).
4. **Final tie-breaker** — deterministic lexical ordering of the ticker string (`"XNDXJPY"` <
   `"XNDXNNRJPY"`), guaranteeing a unique answer even if every substantive discriminator above ties.

---

## 9. Option-C rule (`DH1-R8`)

```
start = first observation the source returns strictly after 2020-06-26
end   = start + (window-length duration, §5)
```

- The **first eligible observation after D-H0** is the start — not a specific calendar date chosen in
  advance, since the exact post-`2020-06-26` publishing calendar is not knowable without retrieval.
- **Duration is inherited from §5** — the same fixed value used for Option A, for cross-tier structural
  comparability.
- If the source cannot supply the **complete** requested span (discontinued series, insufficient
  history since acquisition), the result is `SPAN_INSUFFICIENT` or `SOURCE_UNAVAILABLE` — fall through
  to Option D.
- **Partial windows are forbidden outright** — not an acceptable substitute, consistent with the
  already-approved one-shot, no-manufacturing discipline (`f8332a5` §9).

---

## 10. Option-D bounded rule (`DH1-R9`) — **fully closed, zero remaining discretion**

Inherits `MP-S-01`…`MP-S-08` **without modification** for everything except the one gap identified in
prior review; that gap is now closed by §10.1–§10.3 below, scoped **narrowly to D-H1's Option D only**
— `MP-S-07` itself (the specific rule whose within-category ordering was left open) is not amended, and
nothing here binds any other Mode-P use of that policy.

### 10.1 Within-category total ordering

If an `MP-S-07` search category (of the three declared in §8: (1) sources whose published terms
expressly permit programmatic access and private retention; (2) publisher-direct index data;
(3) general market-data aggregators) contains more than one otherwise-eligible candidate, order them by
the following **lexicographic hierarchy** — each level either strictly discriminates or ties and passes
through to the next, so the algorithm is total and deterministic regardless of how cleanly any
individual level resolves:

1. **Classification rank (§4)** — the candidate's existing class from the policy's unmodified
   candidate-classification table (`A` before `B`; `C` and `D` are excluded from "otherwise eligible"
   by §4 itself and never reach this ordering at all). *Correction, recorded openly: an earlier draft
   of this line cited this classification as "`MP-S-04`" — re-checked directly against the governing
   policy text, §4's classification table carries no numbered `MP-S-0x` marker of its own (`MP-S-04` is
   actually §5's separate ledger rule, on the cost of making a rejected candidate usable). The citation
   is corrected to §4; the substance of the criterion (class `A` ranks before class `B`) is unchanged.*
   This reads an **already-computed** classification, not a new judgment.
2. **Provenance completeness** — count of the `MP-S-05`/`MP-S-06` cost-ledger's already-defined
   required fields (candidate/source identity, dataset identity, source authority, coverage,
   frequency/granularity, return composition, denomination, data-quality concerns, axes `A`–`H` with
   verdict and evidence, redistribution restriction, authentication/account requirement, monetary
   cost, recurring human effort, engineering effort, reproducibility cost, provenance quality,
   unresolved legal/terms ambiguity) that are populated and non-null for the candidate. Higher count
   ranks first. This reuses the **existing, already-approved** ledger schema verbatim — no new field
   is invented.
3. **Construct comparability to the D-H1 research object** — a candidate's own **published, pre-
   existing** series-type description (e.g. "price return index," "total return index," "ETF/fund")
   is compared against `NDXJPY`'s declared price-index construct on a fixed three-level scale: exact
   declared-type match (highest) > a documented named variant of the same underlying index (middle) >
   any other instrument category (lowest). This is a documentation-classification exercise of the
   **same kind `MP-S-03`'s eight-axis assessment already performs routinely** (reading published terms
   and categorizing them) — not new methodology, and never price-value inspection. **If a candidate's
   declared type cannot be classified from its own published metadata, it is not assigned a level at
   this criterion and the comparison ties, cascading to the next criterion** — ambiguity here never
   blocks termination, it only skips a non-discriminating level.
4. **Lower acquisition/operational cost** — the `monetary_cost` field from the same cost-ledger
   (criterion 2's schema); lower value ranks first. Ties (equal recorded cost) cascade to the next
   criterion.
5. **Stable lexical identifier ordering** — standard string comparison (Unicode codepoint order) of
   the candidate's ticker/instrument identifier string. **This level always strictly discriminates**
   between any two distinct candidates (two candidates sharing the identical identifier string are, by
   definition, the same candidate) — it is the guaranteed terminal tie-breaker for the whole hierarchy.

**No level of this hierarchy may be, or ever becomes, a function of price values, historical returns,
drawdown behavior, trigger counts, volatility, or known market events.** Every level is computed from
metadata already required to exist by `MP-S-03`/`MP-S-05`/`MP-S-06`, or from the candidate's own bare
identifier string.

### 10.2 Complete traversal algorithm — resolves `MP-S-07`'s own internal application precisely

```
budget = 3                                  # MP-S-07's total investigation cap, across ALL categories
for category in [1, 2, 3]:                  # MP-S-07's fixed declared category order
    universe = eligible_universe(category)  # fixed BEFORE any investigation; metadata-only
    ranked   = total_order(universe, §10.1) # deterministic; possibly a single candidate, or empty
    for candidate in ranked:                # evaluate strictly in ranked order — this IS
                                             # the unambiguous meaning of "first candidate"
        if budget == 0:
            STOP.  D-H1 BLOCKED — NO ELIGIBLE INPUT.  Return to Owner Review.  (MP-S-07 cap reached)
        budget -= 1
        result = evaluate(candidate)        # MP-S-03/04 axes + §7's "minimum acceptable dataset
                                             # properties" + this artifact's closed rejection codes
        if result == PASS and candidate.class in {A, B}:
            SELECT candidate.  STOP.        # MP-S-07's stop-at-first-success, now unambiguous
        else:
            record the objective rejection code; continue to the NEXT-ranked candidate
            in the SAME category (§10.1's ordering), still against the same shared budget
    # category exhausted (every ranked candidate evaluated, or budget hit 0) -> next category
# all three categories exhausted without success, within budget:
D-H1 BLOCKED — NO ELIGIBLE INPUT.  Return to Owner Review.
```

**Resolves `MP-S-07`'s own internal application exactly:** §8's text states the cap as "at most three
candidates, in the declared order" immediately followed by the three-category search-order list, but
does not itself say what happens if a single category's universe contains more than one otherwise-
eligible candidate — that composition question, not a cross-rule conflict with a separate `MP-S-08`, is
what §10.1's ordering and this algorithm resolve. The three-candidate cap is a **shared budget across
the whole round**, not three-per-category — if a category's universe contains more than one otherwise-
eligible candidate, evaluating a second one from that category consumes budget that would otherwise
have gone to a later category. "First candidate" always means *the top-ranked, not-yet-evaluated
candidate in the current category under §10.1's total order* — never an informal or discretionary
notion. "Next candidate after objective rejection" always means the next entry in that same ranked
list. "Next category after category exhaustion" is triggered only when the ranked list for the current
category is fully consumed (or the shared budget reaches zero, which stops the whole traversal outright
rather than merely advancing).

### 10.3 Scope discipline

This closes `DH1-R9`'s gap **only for D-H1's Option D**. `MP-S-07` itself, and its application to any
other Mode-P dataset-acquisition task, is **not** amended — this artifact is not authority to modify
`docs/decisions/simulation_trial_mode_p_dataset_source_selection_policy.md`, and does not do so.

No new instrument is named, searched for, or selected by this design.

---

## 11. Tie-breaker hierarchy (`DH1-R10`)

1. Preserved policy tier (A > B > C > D) — the primary axis; always decisive first.
2. Construct comparability (metadata/naming-convention-based).
3. Provenance completeness.
4. Lower operational cost.
5. **Stable lexical identifier ordering** — the terminal tie-breaker, guaranteed to produce a unique
   answer in every case, since string comparison never ties on distinct identifiers.

No price, path, or outcome information appears in any tier of this hierarchy.

## 12. Rejection-code vocabulary (`DH1-R11`)

Closed list, every entry independently grounded in already-established repository authority:

`PROVENANCE_INVALID` · `CHECKSUM_UNSTABLE` · `ALREADY_SEEN` · `OVERLAPS_DH0` · `SPAN_INSUFFICIENT` ·
`SCHEMA_INCOMPATIBLE` · `RETENTION_NOT_PERMITTED` · `SOURCE_UNAVAILABLE`.

**Permanently excluded, no exception:** `TOO_FEW_TRIGGERS` · `BORING_PERIOD` · `BAD_RETURN` ·
`GOOD_RETURN` · `INCONCLUSIVE_RESULT`, or any code phrased in terms of expected Strategy-D behavior.
No additional code is introduced beyond the closed list — every rejection condition designed in §3–§10
already maps onto one of the eight.

## 13. Freeze-before-reveal procedure (`DH1-R12`)

The Owner's proposed nine-step shape is **sufficient** and is adopted directly:

1. load the preserved selection-rule version (this artifact, once approved and tagged);
2. inspect metadata/provenance only (dates, checksums, row counts — never values);
3. resolve eligible tier (§2);
4. resolve unique instrument (§2, §8);
5. resolve unique window mechanically (§5–§6, or §9 for Option C);
6. record the selection trace (§14);
7. freeze source identity + exact dates + bytes + SHA-256;
8. write provenance and the full replacement-attempt history;
9. **only then** permit price values to be exposed to the Strategy-D execution process.

**One clarification, not a change:** steps 2–5 read only **metadata** (dates, counts, checksums) —
this is a lesser form of exposure than reading price values, and is necessary to resolve the window at
all. Price **values** remain unexposed until step 9, matching the already-approved lightweight
order-of-operations blinding (`f8332a5` §12) — no elaborate multi-worker blinding is added, since it
would be ceremony without material value in this solo-operator project.

## 14. Selection-trace schema (`DH1-R13`)

Schema only — no real trace is created by this artifact:

```
{
  "selection_rule_commit": "<this artifact's commit, once preserved>",
  "selection_rule_tag": "<this artifact's tag, once preserved>",
  "policy_commit": "f8332a543f7bab4c8b5f42974813ccd70be9137f",
  "policy_tag": "simulation-trial-strategy-d-dh1-dataset-selection-policy-20260814",
  "tiers_considered": [
    {"tier": "A", "result": "PASS|FAIL", "rejection_codes": ["..."]},
    {"tier": "B", "candidate": "XNDXJPY|XNDXNNRJPY", "result": "...", "rejection_codes": ["..."]},
    {"tier": "C", "result": "...", "rejection_codes": ["..."]},
    {"tier": "D", "candidates_considered": ["..."], "result": "...", "rejection_codes": ["..."]}
  ],
  "tie_breaker_decisions": ["..."],
  "selected_instrument_identifier": "...",
  "selected_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
  "snapshot_sha256": "...",
  "run_date": "YYYY-MM-DD",
  "price_values_not_inspected_before_freeze": true
}
```

`run_date` follows the project's existing deterministic-run-date convention (a declared parameter, not
wall-clock), consistent with every prior Mode-E/Mode-P manifest.

## 15. Rule-versioning consequence (`DH1-R14`)

**Adopted, directly supported by repository authority:** this is the same versioning discipline
`f8332a5` §15 already fixes for Strategy D itself — *"any substantive Strategy-D semantic modification
made after inspecting a result creates a new, distinctly versioned post-result hypothesis"* — extended
here from *the strategy* to *the selection rule that produces its input*, a natural and already-
authorized extension rather than a new principle.

- **Substantive change before rule execution:** requires a new preserved rule version (e.g., a
  `_v2` artifact); the prior version's provenance is retained unedited.
- **Substantive change after a candidate has been selected/revealed under the rule:** invalidates that
  candidate as independent evidence produced under a frozen-before-selection rule. Validating anything
  under the changed rule requires a fresh candidate selection under the new version, not a re-reading
  of the old candidate.

## 16. All-tiers-failed behavior (`DH1-R15`)

If Options A, B, C, and D **all** fail objective eligibility (including Option D's three-candidate
cap): the result is **`D-H1 BLOCKED — NO ELIGIBLE INPUT`**, returned to Owner Review. **No criterion is
weakened to force a result** — this mirrors `MP-S-06`'s existing discipline that
`NO ACCEPTABLE CANDIDATE` requires every candidate to be a genuine hard rejection, never a shortcut.
The Owner's cost-sensitive fallback principle is already fully expressed by the A→B→C→D traversal;
exhausting it is not a failure of the policy, it is the policy working as designed.

---

## 17. `DH1-R1`…`DH1-R15` decision matrix

| ID | Question | Recommended disposition | Alternatives considered | Discretion remaining after approval | Operational cost | Owner approval required? |
| --- | --- | --- | --- | --- | --- | --- |
| **`DH1-R1`** | Policy-tier traversal | A→B→C→D, objective-failure-gated (§2) | Parallel evaluation of all tiers at once | None | Low | **Yes** |
| **`DH1-R2`** | Option-A eligibility | Seven metadata-only tests (§3) | Fewer/more tests | None once tests are fixed | Low | **Yes** |
| **`DH1-R3`** | Exact window length | **APPROVED: `906` calendar days** = `(2020-06-26 − 2018-01-02).days`, exact date subtraction (§5.1) | `24`-month floor; `36` months | None — resolved to an exact integer | Low | **Approved 2026-08-14** |
| **`DH1-R4`** | Window-position rule | Earliest eligible window (§6) | Latest; midpoint; seed-derived | None | Low | **Yes** |
| **`DH1-R5`** | Temporal-distance rule | **APPROVED: `1825`-day ordinal-difference floor** (`5 × 365`, §5.2), constructive layer via §6 as primary | Month/day "+5 years"; gap threshold only | None — resolved to an exact integer, no leap-day edge case | Low | **Approved 2026-08-14** |
| **`DH1-R6`** | Continuity/gap rule | **APPROVED: `90%` of a weekday-count denominator** (§7) — no market-calendar subsystem | `~252`-trading-day approximation (rejected — required an undefined holiday calendar) | None — resolved to a pure date-arithmetic formula | Low | **Approved 2026-08-14** |
| **`DH1-R7`** | Option-B ordering | Construct comparability → provenance → span → lexical (§8) | Span-first; provenance-first | None | Low | **Yes** |
| **`DH1-R8`** | Option-C rule | Next observation after D-H0 + inherited duration; no partial windows (§9) | Fixed calendar start date | None | Medium (new retrieval) | **Yes** |
| **`DH1-R9`** | Option-D bounded rule, incl. within-category ordering | **APPROVED: `MP-S-01`…`MP-S-08` inherited unmodified + a 5-level lexicographic within-category ordering (§4 classification rank → provenance completeness → construct comparability → cost → lexical) and a complete traversal algorithm resolving `MP-S-07`'s own budget/order composition (§10.1–§10.3)** | A new, D-H1-specific acquisition process; leaving within-category order unspecified | **None** — the lexical level always strictly discriminates, guaranteeing a unique winner | Medium–High | **Approved 2026-08-14** |
| **`DH1-R10`** | Tie-breaker hierarchy | Tier → comparability → provenance → cost → lexical (§11) | A different ordering | None | Low | **Yes** |
| **`DH1-R11`** | Rejection-code vocabulary | Closed 8-code list (§12) | A broader/narrower list | None | Low | **Yes** |
| **`DH1-R12`** | Freeze-before-reveal procedure | Owner's 9-step shape, adopted directly (§13) | Full multi-worker blinding | None | Low | **Yes** |
| **`DH1-R13`** | Selection-trace schema | Fields listed in §14 | A smaller/larger schema | None | Low | **Yes** |
| **`DH1-R14`** | Rule-versioning consequence | New version required for pre-execution changes; post-selection changes invalidate the candidate (§15) | Allow minor changes without reversioning | None | Low | **Yes** |
| **`DH1-R15`** | All-tiers-failed behavior | `D-H1 BLOCKED — NO ELIGIBLE INPUT`, return to Owner Review (§16) | Weaken a criterion to force a result | None | Low | **Yes** |

**Target state assessment, final: ZERO MATERIAL EXECUTION-TIME DISCRETION: ACHIEVED.** `DH1-R3`,
`DH1-R5`, `DH1-R6`, and `DH1-R9` are all now Owner-approved and formalized with exact values or
complete algorithms. Every one of `DH1-R1`…`DH1-R15` reaches zero remaining discretion.

---

## 18. Cost/value analysis

| Safeguard | Classification |
| --- | --- |
| Metadata-only eligibility tests (§3, §7) | HIGH VALUE / LOW COST |
| Earliest-window positioning (§6) | HIGH VALUE / LOW COST |
| Constructive + backstop temporal-distance rule (§5) | HIGH VALUE / LOW COST |
| Existing loader's native gap tolerance (§7) | HIGH VALUE / LOW COST — no new infrastructure |
| Closed rejection-code vocabulary (§12) | HIGH VALUE / LOW COST |
| Lightweight freeze-before-reveal, no multi-worker blinding (§13) | HIGH VALUE / LOW COST |
| Selection-trace schema (§14) | HIGH VALUE / LOW COST |
| Rule-versioning discipline (§15) | HIGH VALUE / LOW COST |
| Seed/hash-derived window positioning as an alternative to "earliest" | LOW VALUE / MEDIUM COST — not adopted; earliest is simpler with no loss of rigor |
| Full multi-worker blinding | LOW VALUE / HIGH COST — not proposed, consistent with the already-approved policy |
| A market-calendar infrastructure for gap handling | LOW VALUE / HIGH COST — not needed; the existing loader contract already suffices |

Every recommended element is HIGH VALUE / LOW COST. No new infrastructure is proposed beyond what the
existing engine, loader, and inherited source-selection policy already provide — consistent with this
being a solo-operator project where ceremonial complexity is explicitly to be avoided.

---

## 19. What this artifact does not do

Does not execute any rule; does not select Option A, B, C, or D; does not select `NDXJPY`, `XNDXJPY`,
`XNDXNNRJPY`, or any external instrument; does not choose an exact date; does not read or report any
price value; does not modify `f8332a5`, Baseline v2, or any prior Strategy-D artifact; does not change
any qualification-lane state.

---

**End of document. Status: APPROVED BY OWNER DECISION, 2026-08-14 — DETERMINISTIC SELECTION RULE ONLY.
Rule design only. Not executed. No dataset, window, or price value was selected or inspected in
preparing or approving this artifact. Approval of the rule does not execute it, select a dataset,
instrument, or window, or authorize price-value inspection, Strategy D execution, or economic
evaluation. `f8332a5` and every preserved Strategy-D artifact are unchanged.**
