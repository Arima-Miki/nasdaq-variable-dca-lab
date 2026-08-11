# nasdaq-variable-dca-lab

An experimental research environment for evaluating **deterministic variable-DCA
strategies** for NASDAQ-100-related investments.

> **Current status: Phase 1 — Data Foundation**
>
> **Phase 0 Baseline Specification: Frozen — Owner Approved**
>
> No deterministic reproducible Baseline backtest has been implemented yet.
> No strategy has been validated yet.
> No performance conclusion has been reached.
>
> "Frozen" means the strategy rules were pre-specified before any
> repository-implemented deterministic Baseline backtest was run. Exploratory
> analysis predating this repository informed the research question and
> experiment design; it is not Baseline evidence. Frozen does not mean the
> strategy has been validated or approved for live use.

## Documents

| Document | Role |
| -------- | ---- |
| [docs/experiment_spec.md](docs/experiment_spec.md) | The normative Frozen Phase 0 Baseline specification — strategy rules, budget accounting, metrics, and open Phase-1 / methodology requirements |
| [docs/decisions/phase0_baseline_decisions.md](docs/decisions/phase0_baseline_decisions.md) | Decision history: why Owner Decisions OD-01 through OD-14 were selected |
| [docs/evidence/phase1_empirical_alignment_study.md](docs/evidence/phase1_empirical_alignment_study.md) | Phase-1 Evidence Artifact: observation-time alignment between the Nissay fund NAV and the Nasdaq JPY candidate series (Owner-approved evidence; **no Primary Proxy approved**) |
| [docs/evidence/phase1_fx_source_research.md](docs/evidence/phase1_fx_source_research.md) | Phase-1 Evidence Artifact: availability, observation timing, and licensing of candidate USD/JPY FX sources (Owner-approved evidence; **no FX source approved**) |
| [docs/evidence/phase1_japan_side_ttm_qualification.md](docs/evidence/phase1_japan_side_ttm_qualification.md) | Phase-1 Evidence Artifact: qualification of a Japanese-bank USD/JPY TTM series as a candidate Japan-side FX approximation (Owner-approved evidence) |
| [docs/decisions/phase1_ttm_qualification_decision.md](docs/decisions/phase1_ttm_qualification_decision.md) | Phase-1 Owner Decision: bounded qualification of MUFG/MURC TTM as a Phase-1 research input. **Not a Phase-0 Baseline change** |
| [docs/decisions/phase1_fx_residual_decomposition_study_decision.md](docs/decisions/phase1_fx_residual_decomposition_study_decision.md) | Phase-1 Owner Decision: authorization, scope limits, and staged execution boundaries for the FX Residual Decomposition Study. Owner authorization only — **no study results**. **Not a Phase-0 Baseline change** |
| [docs/evidence/phase1_fx_residual_decomposition_study.md](docs/evidence/phase1_fx_residual_decomposition_study.md) | Phase-1 Evidence Artifact: results of the FX Residual Decomposition Study — qualitative findings only, with detailed numerical results deliberately unpublished (Owner-approved evidence; **no Primary Proxy approved**) |

Where the specification and the decision history differ, the specification governs
Baseline behavior. Evidence artifacts record Phase-1 findings; they do not modify the
Baseline.

---

## Research question

> Can a mechanically executed satellite investment strategy that varies purchase
> timing and allocation size according to market drawdown improve capital
> deployment relative to simple fixed DCA?

The purpose of this repository is to produce **reproducible evidence for or
against** that hypothesis.

A positive result is not assumed. A finding that simple DCA performs better is a
valid and valuable research outcome, and will be reported as such.

## Research principles

1. **Evidence before conclusions.** Claims are made only where backtest evidence
   supports them.
2. **Deterministic and reproducible calculations.** Given the same inputs and the
   same specification, results must be identical and independently reproducible.
3. **No discretionary market timing.** Tested strategies are rule-driven; no
   judgement calls are permitted inside a strategy.
4. **No look-ahead bias.** A rule may only use information that would have been
   available at the moment of the simulated decision.
5. **Baseline rules are specified before results are examined.** The baseline
   specification is written and frozen before any Baseline backtest output is
   inspected.
6. **Parameter optimization is not baseline validation.** Tuned results are
   reported separately from the pre-specified baseline and are never presented as
   confirmation of it.
7. **Failed hypotheses and negative results are valid evidence** and will be
   published rather than discarded.
8. **Backtest performance does not constitute approval for live investment use.**

## Initial strategy scope

The first experiment compares three strategies:

| ID | Strategy | Research role |
| -- | -------- | ------------- |
| A | Simple DCA (control) | Fixed DCA |
| B | Daily Drawdown Trigger | Pure drawdown timing |
| C | Daily Drawdown Trigger + Month-End Fallback | Drawdown timing with a DCA floor |

### Baseline satellite concept

The frozen satellite concept uses:

- NASDAQ-100-related exposure
- 1 unit = JPY 10,000
- 12 new units of satellite budget per year
- Unused units carry forward without expiry
- Future annual budget may **not** be borrowed against
- Mechanically determined purchase timing
- Mechanically determined allocation sizes of 0.5 / 1.0 / 2.0 units
- At most one committed satellite allocation per calendar month

**The exact trigger definitions, budget accounting, and evaluation methodology are
deliberately not restated here.** They are specified in
[docs/experiment_spec.md](docs/experiment_spec.md). This README is an entry
document, not the specification.

## Planned data research

The Nissay NASDAQ100 Index Fund has a short operating history, so the project
expects to investigate longer-history proxies suitable for backtesting.

Candidates currently under consideration:

- A NASDAQ-100 Total Return JPY series, as a primary proxy candidate
- QQQ total-return data combined with USD/JPY, as an independent cross-validation
  candidate
- Nissay NASDAQ100 Index Fund data from its actual operating period, for proxy
  validation

These are **candidates, not approved data sources.** Their availability, history,
licensing, redistribution terms, and suitability as proxies are open questions
under investigation in Phase 1. No claim is made here about any of those
properties.

## Planned research phases

| Phase | Name | Intent | Status |
| ----- | ---- | ------ | ------ |
| 0 | Baseline Specification | Define the strategies, budget rules, evaluation metrics, and methodology in writing, before implementation. | **Frozen — Owner Approved** |
| 1 | Data Foundation | Investigate, evaluate, and document data sources and proxy validity. | **Current** |
| 2 | Deterministic Backtest | Implement the pre-specified rules as reproducible code. | Blocked |
| 3 | Evidence Review | Examine baseline results, including negative results. | Not started |
| 4 | Sensitivity Analysis | Test robustness across parameters, periods, and data sources, reported separately from the baseline. | Not started |
| 5 | Operational Candidate Evaluation | Assess whether any strategy is even a candidate for further real-world consideration. | Not started |

### Phase 1 scope

Phase 1 investigates, from evidence rather than assumption:

- candidate data sources and their availability, history, and quality
- proxy validity for the intended live product
- licensing and redistribution rights
- the execution / NAV mapping for the intended Japanese mutual fund
- currency treatment where a proxy requires conversion
- cost and expense treatment, without double-counting or assumed tracking
  difference

Phase 1 is **in progress**. Approved findings are recorded as evidence artifacts
under [docs/evidence/](docs/evidence/); **several Phase-1 Evidence Artifacts now
exist**, each authoritative for its own study, and this README is not a
research-results document.

Two Phase-1 Owner Decisions have been recorded.

The first
([docs/decisions/phase1_ttm_qualification_decision.md](docs/decisions/phase1_ttm_qualification_decision.md)):
MUFG/MURC historical USD/JPY TTM is **qualified only as a bounded Phase-1
research input** — a candidate approximation of the fund's Japan-side FX
conversion concept, for local research and sensitivity analysis. That
qualification does **not** identify any bank as the fund's FX provider, does
**not** approve a Baseline FX convention, and does **not** permit raw FX data to
be committed to this repository. It is a Phase-1 research authorization, not a
change to the Frozen Phase-0 Baseline.

The second
([docs/decisions/phase1_fx_residual_decomposition_study_decision.md](docs/decisions/phase1_fx_residual_decomposition_study_decision.md)):
the **FX Residual Decomposition Study** is authorized, with scope limits, to
investigate how much of the observed fund-vs-candidate residual is attributable
to FX observation convention. That artifact records **Owner authorization only
and contains no study results**. It approves one bounded return-space research
construct, keeps raw data outside this repository, and leaves publication of any
derived statistics to a separate later review. It approves no Primary Proxy, no
Baseline FX convention, and no change to the Frozen Phase-0 Baseline.

That study has since been **completed and recorded** as a Phase-1 Evidence Artifact
([docs/evidence/phase1_fx_residual_decomposition_study.md](docs/evidence/phase1_fx_residual_decomposition_study.md)).
At a high level, it found that **FX observation convention is a first-order empirical
contributor** to the residual between the fund and the JPY candidate series — **under the
qualified research approximations used**, not under any identified production convention. The
**actual production FX conventions on either side remain unidentified**, and a structured
residual remains after the FX component is accounted for.

**Detailed numerical results and source-derived data are not published** where the applicable
publication and licensing boundary does not support doing so. That omission is deliberate, and
the artifact states what was withheld and why. The artifact approves **no Primary Proxy**, no
Baseline FX convention, and no change to the Frozen Phase-0 Baseline. This README remains an
entry document, not a research-results document; the artifact is authoritative for its own study.

**Phase 2 implementation remains blocked** until the Phase-1 evidence
requirements recorded in
[docs/experiment_spec.md](docs/experiment_spec.md#19-open-items-register) are
resolved. No backtest code, methodology code, or data loader is written before
then. In particular, **no Primary Proxy has been approved** — P1-2 remains open.

## Repository boundary

This is a research repository. It is **not**:

- a production trading system
- an automated brokerage execution system
- a source of individualized investment advice
- part of HQ-Equity production code
- evidence that any strategy is suitable for live deployment

Research findings may later serve as design input elsewhere. Code or strategies
must not be treated as production-approved merely because they exist here.

Nothing in this repository is investment advice.

## Public repository policy

This repository is intentionally public, to support transparency,
reproducibility, and citation of its research evidence.

It must **never** contain:

- credentials or API keys
- brokerage account information
- personally identifiable information
- private portfolio information
- proprietary or redistribution-restricted market datasets, unless redistribution
  is explicitly permitted

Raw market data must not be assumed safe to commit merely because it is publicly
obtainable. Public availability and redistribution rights are different
questions, and the second must be established before any dataset is committed.

## Reproducibility

Reproducibility is treated as a requirement, not a goal:

- Strategy rules were specified in writing and frozen before implementation, and
  before any reproducible Baseline result existed.
- Backtest calculations are deterministic — no randomness, no discretionary input.
- Data sources, transformations, and any adjustments are documented so a third
  party can reconstruct the inputs.
- Baseline results and optimized results are reported separately.
- Results that contradict the hypothesis are published.

Where data cannot be redistributed, the repository will document how to obtain
and prepare it rather than committing it.
