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

Where the two differ, the specification governs Baseline behavior.

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

**Phase 2 implementation remains blocked** until the Phase-1 evidence
requirements recorded in
[docs/experiment_spec.md](docs/experiment_spec.md#19-open-items-register) are
resolved. No backtest code, methodology code, or data loader is written before
then.

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
