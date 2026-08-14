# Simulation Trial — Strategy D Stage D-H1 Independent-Validation Dataset Selection Policy

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14 — POLICY ONLY.** This approval fixes the
selection **policy**; it selects **no** dataset, instrument, window, or bytes. No dataset selected. No
data retrieved. No candidate price series inspected. No Strategy D or A/B/C execution occurred in
preparing or preserving this artifact.
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Governing Baseline:** v2 (effective 2026-08-13) — unchanged by this artifact
**Governing Strategy-D chain:** hypothesis `5a3f54a` · semantics `62c5c42` · Mode-E E5 `f16a815` ·
D-H0 mechanical validation `486b994`, tag `simulation-trial-strategy-d-dh0-20260814`
**Inherits, does not duplicate:** `docs/decisions/simulation_trial_mode_p_dataset_source_selection_policy.md`
(`MP-S-01`…`MP-S-08`) for acquisition mechanics; extends it with anti-hindsight requirements that
policy never needed to address.

---

## 0. Why this is a separate artifact, not an edit to the existing source-selection policy

The existing Mode-P source-selection policy (`MP-S-01`…`MP-S-08`) governs **how a provisional Mode-P
dataset is lawfully selected and acquired** — human-in-the-loop mechanics, the eight-axis rights
framework, candidate classification, cost-ledger schema, fallback ranking, and a search-exhaustion
stopping rule. Every one of those mechanics is fully applicable to Stage D-H1 and is **inherited
unchanged** (§1 below).

What it does **not** address, because it never needed to: **Strategy D is a post-result hypothesis.**
The original NDXJPY acquisition was trivially "unseen" by construction — no Mode-P run of any kind had
ever occurred before it. Stage D-H1 is different in kind: Strategy D exists *because* the Owner
inspected an earlier result, so the ordinary "no result exists yet, so nothing can be cherry-picked"
reasoning **does not transfer**. A dataset could still be selected in a way that is *effectively*
outcome-based — by favoring a window whose general character is already suspected to suit Strategy D
— without ever formally running Strategy D on candidates first. This artifact exists solely to close
that gap.

---

## 1. Inherited from the existing source-selection policy, unchanged

- `MP-S-01` — human-in-the-loop acquisition is repository-compliant; no automation is assumed or required.
- `MP-S-02` — a manual acquisition step is a cost, never a rejection ground.
- `MP-S-03` — the eight-axis rights framework (A–H), assessed per axis, never collapsed.
- `MP-S-04` — candidate classification A–D by downstream use, not by who downloads.
- `MP-S-05` — rejection-status vocabulary (SELECTED / CONDITIONAL / SOFT REJECT / HARD REJECT / NOT YET EVALUATED).
- `MP-S-06` — every seriously evaluated candidate recorded, including rejected ones; ledger editions are numbered and additive-only.
- `MP-S-07` — imperfection is a cost to measure, not an automatic stop; **NO ACCEPTABLE CANDIDATE**
  requires showing every candidate is HARD REJECT.
- `MP-S-08` — the search-exhaustion stopping rule: at most three candidates investigated per round, no
  data retrieved during investigation, return to Owner Review if all three fail.

None of this is restated in full below; it applies to Stage D-H1 exactly as written for Mode P
generally.

## 2. What is genuinely new for Stage D-H1

Everything below is **additional to**, not a replacement for, §1 — because Strategy D's post-result
status creates a contamination channel (§4) that the general Mode-P policy was never designed to
close.

---

## 3. Operational definition of UNSEEN

| Category | Description | D-H1 eligibility |
| --- | --- | --- |
| **A** | Data never previously retrieved by anyone in this project | **Eligible.** Cleanest case. |
| **B** | Data retrieved but never inspected (bytes exist locally, unopened) | **Conditionally eligible** — only with a verifiable, checkable non-inspection attestation (e.g. a checksum recorded at first retrieval, never since referenced in any research artifact). Absent that proof, treat as **not eligible** — a negative is not provable after the fact, and the fail-closed default governs. |
| **C** | Data previously used for **qualification research** (Stage-D candidates, licensing/continuity work) | **Eligible, and structurally attractive** — see §7. Qualification research under `S.2` was expressly bound by a non-analysis undertaking (*"retain the minimum material necessary and do not analyse the values"*), which is precisely the property Stage D-H1 needs. Eligibility requires its own bounded release, mirroring `73d6f51`. |
| **D** | Data previously used for **A/B/C or Strategy-D simulation** | **Not eligible.** This is `MP-H1`/`MP-H2`/`MP-EV`/`MP-EV2`/`MP-DH0*` — the D-H0 window itself, or any overlapping span of it. |
| **E** | Data whose **summary statistics were already known** before selection (e.g. a stated CAGR, a known drawdown count) | **Not eligible.** This is dataset-specific outcome knowledge regardless of whether the bytes themselves were ever fetched. |
| **F** | Data whose **major market events are generally known** to the Owner (e.g. "2020 had a COVID crash," "2008 had a financial crisis") | **Does not, by itself, disqualify** — see §4. Excluding every window a financially literate person has ever heard of would make D-H1 impossible by construction; that is not this repository's intent for Stage D-H1's stated purpose (mechanical/behavioral independent validation, not a blind economic forecast). |
| **G** | Data **selected after inspecting its price path** | **Never eligible.** This is the literal act the whole exercise exists to prevent. |

## 4. Contamination boundary — general knowledge vs. dataset-specific inspection

> **GENERAL MARKET KNOWLEDGE** — unavoidable background awareness that broad macro events occurred
> (recessions, crashes, rallies), without having examined the *specific candidate file's* numeric
> content. Does not disqualify a window.
>
> **DATASET-SPECIFIC OUTCOME INSPECTION** — having viewed the candidate's own price path, computed or
> read its summary statistics, checked how many threshold-crossing events it contains, or consulted
> any report that already analyzed that specific candidate. Disqualifies the candidate immediately and
> permanently.

The dividing line is **whether the specific candidate file's content was examined, by anyone, for any
purpose, before the selection rule was mechanically applied to the eligible universe** — not whether
the Owner has ever heard of a famous market event in general.

> **Tightened, load-bearing statement — the exact test.** A predeclared deterministic selection rule
> (e.g. *"take the immediately following contiguous fixed-length period"*) is **not** converted into
> hindsight selection merely because the period it happens to select is historically recognizable. The
> relevant question is always: **did knowledge or inspection of the candidate's Strategy-D-relevant
> content influence selection, rejection, replacement, or rule modification?** If no, general market
> knowledge alone is not disqualifying — regardless of whether the resulting window contains a famous
> event.

**Correction to an earlier draft, recorded openly, not silently fixed.** A prior revision of this
policy characterized a same-instrument chronological holdout past D-H0 as a *"post-2020 trap"* and
treated it as effectively a hindsight-selection risk. On rigorous re-examination that characterization
was **wrong and is retracted.** A mechanically applied *"take the next N months"* rule, fixed before
any candidate value is inspected, satisfies the test above regardless of what the resulting period
turns out to contain — the earlier language improperly imported general awareness of subsequent market
history as if it were selection contamination, which directly contradicted this artifact's own stated
principle in the paragraph above it. See §5 (`DS-1`) and §8 for the corrected treatment.

**What remains a genuine, but different and narrower, consideration: temporal adjacency.** Having just
observed NDXJPY's specific volatility scaling and index-methodology character in D-H0, an *immediately
following* window of the *same* instrument shares more statistical continuity with the already-observed
sample than a temporally distant window, a different instrument, or both would. This is an
**independence** consideration — a question about how much new information the validation actually
adds — not a **contamination** violation, and it does not disqualify a same-instrument adjacent window;
it is one factor among several used to rank options in §7/§16A, never a reason to exclude one outright.

---

## 5. Selection mechanisms considered

| ID | Mechanism | Assessment |
| --- | --- | --- |
| **DS-1** | Chronological holdout — the next contiguous period after a predeclared cutoff on the *same* instrument | **ACCEPTABLE — corrected disposition.** An earlier draft rejected this as a *"post-2020 trap"* / hindsight risk; that characterization is **retracted** (§4). A mechanically applied *"next N months"* rule is not hindsight selection merely because the resulting period is historically recognizable. It is ranked below the already-held options in §16A for two legitimate, narrower reasons: it requires **new external retrieval** (the held NDXJPY snapshot stops at `2020-06-26`; a holdout past that date is not already-held data, contrary to what convenience might suggest), and it carries the **temporal-adjacency independence consideration** described in §4 — cost and independence-strength reasons, not a contamination violation. |
| **DS-2** | Predeclared fixed-length window — a duration and start-date **rule** (not a value) fixed before any candidate is touched | **Recommended, combined with DS-3.** Applicable to whichever instrument is selected; prevents length cherry-picking. |
| **DS-3** | Deterministic source/window rule from metadata alone (no price content) | **Recommended as the primary mechanism, for whichever instrument option (§7 A–D) is eventually chosen.** Already-held, non-analyzed Stage-D material — both the un-released portion of NDXJPY (Option A) and `XNDXJPY`/`XNDXNNRJPY` (Option B) — makes this cheaply available without new retrieval; it is not specific to one candidate over the other. |
| **DS-4** | Seeded/random selection from a frozen eligibility universe, using a recorded, unmanipulable seed | **Available as a fallback / higher-rigor option** if the metadata-only pick under DS-3 is ever judged to retain residual selection discretion (e.g., if more than one equally eligible candidate remains after DS-3's rule is applied). Higher operational cost than DS-3; not needed if DS-3 already yields a unique result. |
| **DS-5** | Third-party / pre-existing external period definition | **Usable opportunistically** if such a period definition exists and is independently verifiable as not itself outcome-selected — not required given DS-3's availability. |

## 6. Eligibility criteria — ex-ante, metadata-only

**Permitted** (knowable without examining price behavior):

instrument identity · source/publisher identity · date-availability metadata (as published by the
source, not read from the file's values) · observation frequency (daily) · minimum observation count
(a structural threshold — enough to exercise month **and** year boundaries multiple times, e.g. a
span of at least 24 calendar months, chosen for coverage-of-mechanics reasons exactly as `MP-P-D1`
reasoned for the original NDXJPY span — never for expected trigger richness) · minimum calendar span ·
currency/denomination as declared · continuity (no unexplained gaps beyond ordinary non-trading days)
· file/schema compatibility with the existing, unmodified `csv_loader.py` contract (date + close
columns) · licensing/retention constraints (via the inherited eight-axis framework) · checksum/freeze
capability.

**Forbidden, explicitly:** must contain a crash · must contain a `-20%` drawdown · must include both
bull and bear regimes · must generate enough Strategy-D triggers · must produce multiple Large-drop
events · any criterion phrased in terms of what the candidate's *price path* looks like or would cause
Strategy D to do.

## 7. Instrument question

**Two distinct properties are evaluated separately for every option below, and neither is inferred
from the other:** `DATA INDEPENDENCE` (how little the candidate's specific content is already known or
inferable from prior exposure) and `CONSTRUCT COMPARABILITY` (how closely the candidate matches the
NASDAQ-100-price-drawdown concept Strategy D's rule was framed against). A different instrument or
return representation may improve the former while weakening the latter — the two do not move
together, and this policy does not treat "different file" or "different instrument" as automatically
stronger validation on that basis alone.

### Option A — Same instrument, temporally distant, already-held NDXJPY window

- Same NDXJPY construct as D-H0 — **maximum construct comparability**, zero return-composition
  difference.
- **No new external retrieval** — a candidate window would be drawn from the portion of the already-held
  Stage-D `E-01` file (`1985-01-31`→`2020-06-26`) that falls **outside** the span `73d6f51` released
  (`2018-01-02`→`2020-06-26`) — for example, the earlier 1985–2017 portion, never released for Mode-P
  use and never inspected for Strategy-D-relevant content.
- Must be **completely non-overlapping** with the released D-H0 window.
- Must not have been previously inspected for Strategy-D-relevant behavior by anyone, for any purpose.
- Requires its **own new bounded-release authorization**, distinct from and not derivable by silently
  reinterpreting `73d6f51` (which explicitly prohibits span extension **of the same release** — a new,
  separate release decision for a non-overlapping span is a different act, not an extension of that one).
- The exact window remains selected **only** by the future approved deterministic rule (§16A) — no
  specific dates are chosen here.
- **Reduces the temporal-adjacency independence concern** (§4) relative to a window immediately
  following D-H0 — this is *not* a contamination question, and it is *not* a claim of established
  statistical independence either; only a narrower and more defensible claim than "independent."

### Option B — `XNDXJPY` / `XNDXNNRJPY` unused window

- Already held under the Stage-D `S.2` non-analysis undertaking; **low operational cost** — a bounded
  release decision analogous to `73d6f51` would suffice, no new external retrieval.
- **Strong file-level independence** — an entirely different file, never examined for price content by
  this project, at any window.
- **Possible return-composition construct difference must be disclosed, not assumed away.** Nasdaq's
  `X`-prefix naming convention is consistent with a total-return (dividends reinvested) variant rather
  than NDXJPY's price-return construct; this has not been independently verified by this project (no
  price content has been inspected), and is recorded here as an **unverified but plausible construct
  difference**, not a confirmed repository fact.
- **Must not be described as methodologically superior merely because it is cheap.** Low operational
  cost and high independence are real advantages; they do not by themselves establish that this option
  is the strongest construct-comparable validation input — see §16A.

### Option C — Same-instrument chronological holdout beyond D-H0 (`DS-1`)

- Methodologically defensible; deterministic next-period selection is **not** hindsight selection (§4,
  §5 — the earlier "post-2020 trap" characterization is retracted).
- Requires **new external retrieval** — the currently held NDXJPY snapshot stops at `2020-06-26`; a
  holdout past that date does not yet exist in this repository's evidence stores.
- Carries the temporal-adjacency independence consideration described in §4 — a factor in ranking, not
  a disqualification.
- Higher operational and governance cost than Options A/B (new acquisition research under the
  inherited §1 policy).

### Option D — Fresh external NASDAQ-related instrument/source

- Potentially the **strongest source/instrument independence** of the four options — an entirely new
  provider, an entirely new file, no prior project exposure of any kind.
- **May introduce construct-validity differences** (e.g. an ETF's price reflects fund mechanics —
  creation/redemption, tracking difference, periodic cash distributions — rather than a pure index
  calculation). Any specific instrument (for example an ETF tracking the NASDAQ-100) is mentioned here
  only as an **illustrative example of the category**, not a selected or endorsed candidate, and its
  exact return-composition character is a **future acquisition/research question**, not a fact this
  artifact establishes.
- Requires the **full inherited** `MP-S-01`…`MP-S-08` acquisition process — highest operational and
  governance cost of the four options.

**Which sub-choice is preferred between Options A and B, and the exact instrument if Option D is ever
pursued, remain OPEN for a future Owner Decision** — not resolved by this artifact (§18).

## 8. Time-window question

Recommended, subject to whichever instrument a future Owner Decision selects:

- A window **adjacent to D-H0 is not disqualified on hindsight-selection grounds** (§4) — the earlier
  draft's "post-2020 trap" reasoning is retracted. Adjacency remains relevant only as the narrower,
  legitimate **independence** consideration described in §4: a temporally distant window (Option A/C)
  or a different file entirely (Option B/D) adds more genuinely new information than an adjacent
  window of an already-observed instrument does. This is a ranking factor (§16A), not a contamination
  exclusion.
- A post-2020 window is not automatically preferred merely because it is convenient that D-H0 ends in
  2020, **nor is it automatically disqualified merely because it is convenient** — both would be errors
  in the same direction (letting convenience, rather than the predeclared rule, drive the outcome). No
  post-2020 price value was inspected in reaching any statement in this artifact.
- **Non-overlap with the released D-H0 window is mandatory regardless of instrument or era** (§3
  category D) — this is a hard eligibility requirement, not a preference.
- Length and start-date determined by a **predeclared rule** (`DS-2`/`DS-3`), not a hand-picked value.

## 8A. Staged validation architecture

**Recommended as the meta-policy governing how much any single dataset is asked to prove.** Rather
than requiring one dataset to simultaneously maximize both data independence and construct
comparability — properties that trade off against each other (§7) — this policy explicitly separates
D-H1 into stages:

**D-H1 — first independent validation.** Prefer a **low-cost, high-construct-comparability** unseen
input selected under this frozen policy (Option A or B, §7, ranked in §16A). Its purpose is exactly
D-H0's purpose extended to a genuinely unseen input: mechanical behavioral validation, not a
maximal-rigor cross-instrument robustness claim.

**Possible later validation stage (not authorized here).** If the Owner later wants a stronger
cross-source or cross-instrument independence bar than Option A/B can offer, a fresh external
instrument/source (Option D, or a same-instrument holdout, Option C) **may be separately authorized**
as its own future task, under its own bounded acquisition process and its own one-shot discipline. This
artifact **does not name, require, schedule, or authorize** that stage — it only records that the
option remains available so that D-H1 is not forced to answer every robustness question at once, and
so a future Owner Decision does not have to rediscover this reasoning from scratch.

## 9. One-shot validation discipline

**Supported by repository authority and recommended without qualification.** This directly mirrors
`MP-P-D1`'s own discipline for the original Mode-P run (*"source, series and span MUST be recorded
before any result is inspected"*) and `§18.4.6`'s confinement of provisional economic sensitivity to
its own separately authorized decision — neither contemplates an iterative, try-again process.

Sequence: **(1)** freeze this selection policy; **(2)** select exactly one eligible dataset/window
under it; **(3)** freeze bytes + checksum before Strategy D ever sees them; **(4)** execute Strategy D
once, under the predeclared plan; **(5)** preserve the result **whether favorable, unfavorable,
boring, or mechanically uneventful.**

> **A mechanically uneventful result — few or no Strategy-D triggers — is itself a valid independent
> result** (it tests robustness in a calm regime) and is explicitly **not** a legitimate ground to
> select a different dataset. Treating it as one would silently reintroduce exactly the outcome-based
> selection this policy exists to prevent.

## 10. Failure / replacement policy

**Legitimate** (checkable without inspecting price content): corrupt file · checksum instability
across repeated fetches · schema incompatibility with the existing loader contract · insufficient
observations/span relative to the §6 predeclared minimums · licensing/retention prohibition ·
source/file unavailable · candidate is a duplicate of already-seen data (§3 category D).

**Illegitimate, explicitly and permanently barred:** too few `-10%` triggers · no `-20%` event ·
Strategy D barely trades · Strategy D performs badly · Strategy D performs too well · the comparison
looks inconclusive · the period is "boring."

**Fail-closed procedure:** if a candidate fails on a legitimate ground, the failure reason is recorded
**before** any replacement candidate's content is examined; the next candidate comes from a
**pre-declared priority order fixed in advance**, never a newly chosen one; investigation is capped at
three candidates per round exactly as `MP-S-08` already requires, with a return to Owner Review if all
three fail.

## 11. Freeze boundary — minimum sufficient set, before any Strategy-D execution

dataset/source identity · exact date span · raw-byte snapshot · SHA-256 · retrieval date ·
`dataset_class` · provenance chain · **this selection-policy's identifier** · the eligibility result
against §6 · the full replacement-attempt history (including every rejected candidate and its
objective, non-outcome-based rejection reason). This extends the existing `MP-D2`/NDXJPY-release
provenance pattern with exactly one new required field: the replacement-attempt history, which the
original NDXJPY acquisition never needed to record because there was no prior Strategy-D result to
protect against.

## 12. Blinding

**Full separate-worker blinding: LOW VALUE / HIGH COST in this project's actual structure.** This is a
solo-operator project (Owner plus one assistant); there is no genuine second party to blind against,
and `MP-S-02` already normalizes human-in-the-loop acquisition without such machinery. Introducing an
artificial blind-acquisition role would be ceremony, not protection, since the same Owner reviews
everything regardless of who nominally performed which step.

**Recommended instead — a lightweight procedural rule, HIGH VALUE / LOW COST:** the acquisition and
freeze steps (checksum, observation count, date range, schema validation) are completed and the
manifest is written **before** any summary statistic, chart, or price-path description of the frozen
file is computed or displayed to the Owner. This requires no new infrastructure — only a discipline
about the *order of operations* already implicit in the freeze boundary (§11), made explicit here so
it is not accidentally skipped.

## 13. A/B/C/D execution ordering

**Recommended: Strategy D executes alone first, on the frozen D-H1 input, with its result irreversibly
preserved (committed and tagged) before any A/B/C run on the same window is even considered.** Running
A/B/C on the same window afterward — if ever wanted — is a **separate, later, separately authorized
task**, not bundled into D-H1 preparation or execution. Rationale: seeing A/B/C's result on the new
window first would let the Owner's read of Strategy D's result be shaped by an implicit comparison
before D's own result is locked in, reintroducing a subtler form of the same contamination this policy
prevents. No execution of any kind is authorized by this artifact.

## 14. Economic-evaluation boundary

**Mechanical validation** of Stage D-H1 (an engine run through completion, invariants, deterministic
replay, mechanical trace counts — exactly the D-H0 pattern) is achievable under **already-existing**
authority: the same `PERMITTED_TERMINAL_FIELDS`/`permitted_terminal_state()` boundary already used for
D-H0 applies unchanged to any dataset, since it is dataset-agnostic by construction.

**Economic evaluation** of Stage D-H1 (any terminal value, return percentage, or comparison) is
**not** automatically inherited from anything preserved so far. `MP-EV-D1`…`MP-EV-D4` were scoped
explicitly to the `MP-H2` A/B/C generation on the **D-H0** dataset; they do not extend to a new dataset
or to Strategy D without their own fresh, explicit Owner Decision — the same way `MP-EV-D1`…`D4`
themselves required a fresh decision extending `MP-D3` rather than being assumed. **D-H0's
restrictions establish the pattern (a separate decision is always required) but do not pre-authorize
D-H1's economic evaluation.** This remains explicitly OPEN.

## 15. Consequence of modifying Strategy D after inspecting a D-H1 result

**Supported by repository authority and recommended as a binding principle**, by direct analogy to:
Baseline Invariant 17 (*"parameters must not be retroactively optimized after results are observed and
then presented as pre-specified"*), applied to Strategy D's own rule definition rather than the frozen
Baseline; `AR-01`'s stable-identifier-vs-non-normative-name discipline; and the entire post-result
chronology already central to Strategy D's own governance.

> **Any substantive Strategy-D semantic modification made after inspecting a D-H1 result creates a
> new, distinctly versioned post-result hypothesis** (e.g. "Strategy D-v2"), with its own fresh
> post-result chronology disclosure — because the modification was itself informed by a result. **The
> original D-H1 run can never retroactively validate the modified rule.** Validating the modified
> version requires its own new Stage-D′-H1-class run against a **yet another** genuinely unseen window,
> not a re-reading of the original D-H1 result under the new rule.

This is the safeguard against iterative overfitting the Owner specifically asked to prevent.

---

## 16. Owner Decision matrix

| ID | Question | Recommended disposition | Alternatives | Contamination risk | Operational cost | Owner approval required? |
| --- | --- | --- | --- | --- | --- | --- |
| **`DH1-D1`** | Operational definition of unseen | §3 table; categories A/C eligible, B conditionally, D/E/G excluded, F non-disqualifying | Stricter (exclude C); looser (allow E) | Stricter = lower risk, higher cost (may exhaust Stage-D holdings); looser = higher risk | Low to adopt | **Yes** |
| **`DH1-D2`** | Eligible instrument/source universe | **Four ranked options (§7, §16A)**: Option A (same-instrument, temporally distant, already-held) methodologically preferred; Option B (`XNDXJPY`/`XNDXNNRJPY`) lowest-cost acceptable; Option C (same-instrument holdout) higher-cost acceptable; Option D (fresh external) fallback / stronger-independence | Any option could be adopted as primary instead; the ranking, not the eligibility, is what this decision fixes | **None of the four carries selection-contamination risk** (§4) — all are eligible under §3/§6. What differs is a disclosed *independence strength* / *construct-comparability* trade-off, not contamination: A carries a temporal-adjacency independence consideration; B carries an unverified construct-composition question; C carries the same adjacency consideration as A plus acquisition risk; D has the strongest independence and the largest construct-comparability and acquisition cost | A/B: Low. C/D: Medium–High | **Yes** |
| **`DH1-D3`** | Window-selection rule | `DS-3` (deterministic metadata rule) + `DS-2` (fixed-length rule) as primary; `DS-4` (seeded random) as fallback only if `DS-3` underdetermines the choice | `DS-4` as primary; `DS-1` chronological holdout treated as excluded | `DS-1` is **restored as ACCEPTABLE** (§5, corrected) — no longer treated as high-risk on hindsight grounds, only ranked by cost/adjacency; `DS-4` lowest residual risk but highest cost | `DS-3`/`DS-2` low; `DS-4` medium | **Yes** |
| **`DH1-D4`** | Minimum span / observation requirement | ≥24 months, daily observations, structural (boundary-coverage) justification only | A different fixed minimum | None — this criterion is outcome-blind by construction | Low | **Yes** (exact number) |
| **`DH1-D5`** | One-shot policy | Adopt without qualification (§9) | Allow bounded retries under strict pre-registered conditions | Any retry mechanism reopens cherry-picking risk | Low (one-shot is cheaper than iteration) | **Yes** |
| **`DH1-D6`** | Legitimate replacement conditions | §10's integrity/availability list only | Broader list including data-quality judgment calls | Broader lists risk smuggling in outcome-based reasoning | Low | **Yes** |
| **`DH1-D7`** | Freeze boundary | §11's minimum field set | Superset with additional metadata | Fewer fields = weaker audit trail | Low | **Yes** |
| **`DH1-D8`** | Blinding policy | Lightweight order-of-operations rule (§12); no separate-worker blinding | Full separate-worker blinding | Full blinding: marginal risk reduction in a solo-operator project | Full blinding: high cost, low marginal value here | **Yes** |
| **`DH1-D9`** | A/B/C/D execution ordering | D alone first, preserved, before any A/B/C consideration (§13) | Simultaneous A/B/C/D | Simultaneous risks implicit comparison shaping D's read | Low either way | **Yes** |
| **`DH1-D10`** | Permitted result/reporting boundary | Mechanical only, under existing `PERMITTED_TERMINAL_FIELDS`; economic evaluation requires a new, separate Owner Decision (§14) | Pre-authorize economic evaluation now | Pre-authorizing now risks defining the metric after knowing the dataset direction | Low to defer | **Yes** (for any future economic step) |
| **`DH1-D11`** | Effect of later Strategy-D modification | New versioned hypothesis; original D-H1 cannot validate it (§15) | Treat minor modifications as covered by the same D-H1 result | Treating modifications as covered reopens iterative overfitting | Low | **Yes** |

> **`DH1-D1` through `DH1-D11` — APPROVED BY OWNER DECISION, 2026-08-14, exactly as recommended
> above.** No disposition, rationale, alternative, risk assessment, or cost classification in this
> table was altered by this approval. This approves the **policy**; it selects no dataset, instrument,
> or window (§18 remains fully OPEN).

---

## 16A. Ranked policy tiers and explicit fallback rule

**This section exists to preserve, in the decision record itself, the reasoning needed to distinguish
methodologically preferred from merely cheapest — and to explain any future fallback from one to the
other without re-litigating the analysis.**

### METHODOLOGICALLY PREFERRED

**Option A (§7) — a temporally distant, already-held NDXJPY window, selected by the predeclared
deterministic rule (`DS-3`/`DS-2`), subject to eligibility (§6) and its own bounded-release
authorization.** Maximizes construct comparability (identical instrument, identical return
composition) while reducing — not eliminating — the temporal-adjacency independence concern, at low
operational cost since no new external retrieval is required.

### LOWEST-COST ACCEPTABLE

**Option B (§7) — an unused `XNDXJPY`/`XNDXNNRJPY` window**, usable if it materially simplifies the
release/selection process relative to Option A (for instance, if carving a clean non-overlapping
sub-span from the `73d6f51`-released file proves more than trivially fiddly), **provided the
unverified-but-plausible return-composition difference is explicitly disclosed** in whatever artifact
selects it, not silently assumed away.

### ACCEPTABLE HIGHER-COST

**Option C (§7) — deterministic same-instrument chronological holdout (`DS-1`, corrected)**, requiring
fresh external retrieval. Legitimate and not hindsight selection; ranked here on cost and the
adjacency consideration, not on contamination grounds.

### FALLBACK / STRONGER-INDEPENDENCE OPTION

**Option D (§7) — a fresh external NASDAQ-related instrument/source**, requiring the full inherited
`MP-S-01`…`MP-S-08` acquisition process and accepting a construct-comparability cost. Reserved for when
a stronger independence bar is specifically wanted (§8A's possible later validation stage), or when
Options A–C are all unavailable for a legitimate reason.

*(No option is ranked REJECT. Every one of the four is defensible; they differ in cost and in which of
the two competing properties — independence or construct comparability — they favor, not in legitimacy.)*

### Explicit fallback rule

If the methodologically preferred option (A) becomes unavailable or operationally disproportionate for
a **legitimate, predeclared, objective, non-outcome-based** reason, the policy may fall back to the
next tier. Permitted fallback reasons mirror §10's replacement policy exactly:

**Permitted:** release-boundary complexity or overlap ambiguity against a prior release · a
licensing/retention issue · a provenance defect · schema incompatibility · unavailable bytes ·
insufficient span/observations relative to §6.

**Forbidden, absolutely:** expected trigger count · known or suspected drawdown pattern · expected
Strategy-D activity level · expected return · expected superiority or inferiority · "the period looks
boring."

**The fallback reason must be recorded before any replacement candidate's content is examined** —
identical in spirit to §10's fail-closed replacement procedure, applied here to the *tier* decision
rather than to a single candidate within a tier.

---

## 17. Cost/value classification summary

| Safeguard | Classification |
| --- | --- |
| Inherit `MP-S-01`…`MP-S-08` unchanged | HIGH VALUE / LOW COST |
| Metadata-only eligibility criteria (§6) | HIGH VALUE / LOW COST |
| Prefer already-held candidates generally — same-instrument-distant (Option A) or Stage-D total-return variants (Option B) — over new external retrieval (§7, §16A) | HIGH VALUE / LOW COST |
| Ranking construct comparability and independence as separate, non-substitutable properties (§7) rather than collapsing "cheap" into "best" | HIGH VALUE / LOW COST |
| One-shot discipline (§9) | HIGH VALUE / LOW COST |
| Fail-closed replacement policy, capped at three candidates (§10) | HIGH VALUE / LOW COST |
| Freeze boundary with replacement-history field (§11) | HIGH VALUE / LOW COST |
| Lightweight order-of-operations blinding (§12) | HIGH VALUE / LOW COST |
| D-before-A/B/C ordering (§13) | HIGH VALUE / LOW COST |
| Versioned-hypothesis rule for later modification (§15) | HIGH VALUE / LOW COST |
| Full separate-worker blinding | LOW VALUE / HIGH COST — **not recommended** |
| Seeded/random selection (DS-4) as the *default* rather than fallback | HIGH VALUE / MEDIUM COST — reserved for when DS-3 underdetermines, not adopted as primary |
| Pre-authorizing economic evaluation now | LOW VALUE / avoids-a-decision-not-a-cost-saving — **not recommended**, risks defining the metric with the dataset direction already in view |

Every recommended safeguard in this policy is HIGH VALUE / LOW COST. No proposed mechanism requires
new infrastructure beyond what `MP-S-01`…`MP-S-08` and the existing Mode-P driver already provide.

---

## 18. Remaining unresolved questions (explicitly OPEN, not resolved here)

- Final choice among Option A (same-instrument, distant, already-held), Option B (`XNDXJPY`/
  `XNDXNNRJPY`), Option C (same-instrument holdout), or Option D (fresh external instrument) — §7,
  §16A rank them but do not select among them.
- If Option A: the exact non-overlapping window drawn from the already-held `1985`–`2017` portion of
  the Stage-D `E-01` file.
- If Option B: the final choice between `XNDXJPY` and `XNDXNNRJPY`, and independent verification of
  their actual return composition (currently recorded as unverified but plausible, §7).
- Exact window-start rule and span length (subject to the ≥24-month floor).
- Whether `DS-3` alone underdetermines the choice enough to require `DS-4`.
- The exact bounded-release decision text for whichever candidate is chosen (mirrors `73d6f51` but is
  not drafted here).
- Whether and when a future A/B/C run on the same D-H1 window is ever authorized.
- Whether and when the §8A "possible later validation stage" (Option D) is ever separately authorized.
- The exact terms of the future economic-evaluation Owner Decision, if D-H1 ever proceeds to one.

## 19. Qualification-state and prior-artifact preservation

Unchanged by this artifact: the Frozen Baseline; `experiment_spec_v2.md`; the criteria freeze
`1e8bc85`; `AR-01`; the existing Mode-P source-selection policy and ledger; every preserved Strategy-D
artifact (`5a3f54a`, `62c5c42`, `f16a815`, `486b994`); all `P1-x`/`M-x`/`O-4`/`HG-8`/Primary-Proxy/
Stage-G/Stage-H/Phase-2 state. No preserved evidence store is touched. No dataset was selected,
searched for, retrieved, or inspected in preparing this artifact.

---

**End of entry. Status: APPROVED BY OWNER DECISION, 2026-08-14 — POLICY ONLY. Selects no dataset. Does
not authorize acquisition, selection, or execution of Stage D-H1. The Frozen Baseline and every
preserved Strategy-D artifact are unchanged.**
