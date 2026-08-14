# Simulation Trial — Mode P Dataset Source Selection and Human-in-the-Loop Policy

**Status:** **APPROVED BY OWNER DECISION, 2026-08-14.**
**Date drafted:** 2026-08-14
**Owner approval date:** 2026-08-14
**Controlling Baseline:** v2 (effective 2026-08-13)
**Controlling Decision:** Mode P Decision Boundary — `91378fe`
**Controlling Plan:** Mode P Execution Plan — `535de39`

Additive clarification of **how** a provisional Mode-P dataset is selected and acquired. It changes
no frozen normative text and resolves no `P1-x` / `M-x` item.

---

## 1. Reconciliation with repository authority

| Question | Finding |
| --- | --- |
| Does Baseline v2 constrain *who* acquires data, or *how*? | **No.** §18.4.9 requires dataset ID, class, parameters, assumptions and limitations. It is silent on the acquisition agent and method. |
| Do the preserved Mode-P artifacts assume automated retrieval? | **No.** `91378fe` and `535de39` were searched for automation, agent, API, script and robot terms — **zero matches**. `MP-D2` requires *"one frozen snapshot with retrieval date and SHA-256"*, which a human download satisfies exactly as well as a script. |
| Does this clarification require changing frozen normative text? | **No. `SC-18` is not engaged.** |
| Does it alter any qualification-lane state? | **No.** |

> **`MP-S-01`.** Human-in-the-loop acquisition is **already compliant** with preserved governance.
> No amendment is required to permit it. The unstated assumption that the acquiring agent must be
> the AI was mine, in the unapproved acquisition-request draft — never repository authority.

---

## 2. Human-in-the-loop acquisition policy

> **`MP-S-02`.** A manual Owner-performed acquisition step is an **operational cost, not a rejection
> condition**. A source MUST NOT be rejected solely because autonomous AI retrieval is unavailable.

Canonical procedure, when a source requires human acquisition:

1. Owner opens the publisher page and accepts any applicable terms.
2. Owner downloads the file through the publisher's normal interface.
3. Owner places it in the declared Mode-P input directory, unmodified.
4. The simulator records SHA-256, byte size, observation count, first/last dates and retrieval
   metadata, and writes the §18.4.9 manifest.
5. All later processing is local.

**Binding prohibitions.** Do **not** automate around a restriction that requires human action. Do
**not** evade access controls, terms, rate limits, authentication, robots directives, or publisher
restrictions. If a publisher requires a human, a human does it — the simulator verifies and processes
only what it is given.

**Reproducibility is unaffected.** Determinism is a property of *engine + frozen snapshot*, already
established in E4. A human-fetched snapshot, once hashed, replays byte-identically like any other.
What a manual step costs is **repeatability of acquisition**, not reproducibility of results — and
`MP-D2` already requires a single frozen snapshot, so re-acquisition is out of scope by design.

---

## 3. Rights are evaluated on eight separate axes

> **`MP-S-03`.** A candidate MUST NOT be collapsed to PASS/FAIL. Each axis is assessed on its own
> terms, and a restriction on one axis MUST NOT be inferred onto another.

| Axis | Question |
| --- | --- |
| **A** | May an AI agent autonomously retrieve it? |
| **B** | May the human Owner manually retrieve it? |
| **C** | May the retrieved file be retained locally? |
| **D** | May it be transformed/processed by ordinary local software? |
| **E** | May it be input to the historical simulator? |
| **F** | May derived simulation outputs be retained? |
| **G** | May those outputs be inspected or summarized by AI? |
| **H** | Are there AI-training / model-development restrictions? |

A prohibition at **H** does **not** imply prohibition at **B–F**. Permission at **B** does **not**
imply permission at **C–G**. Where an axis is genuinely unclear, it is recorded as **AMBIGUOUS** with
its cost — **never resolved by assuming permission**.

The Owner does not require AI training on source data or on simulation results; **H** is therefore
usually satisfiable by *declining that use*, not by obtaining permission for it.

---

## 4. Candidate classification

| Class | Definition | Disposition |
| --- | --- | --- |
| **A** | AI-acquirable and simulator-usable | Lowest friction; preferred |
| **B** | Human acquisition required; simulator use acceptable | **Fully viable.** MUST NOT be rejected for the manual step alone |
| **C** | Acquirable, but retention / processing / simulator use / output handling carries a material unresolved restriction | Higher cost and risk; usable only with the defect explicitly accepted |
| **D** | Cannot lawfully or technically support the workflow under a reasonable interpretation | Reject unless every lower-cost candidate fails **and** a new Owner Decision reopens it |

**Class is decided by axes D–E (downstream use), not by axis A (who downloads).** A source failing
only axis A is Class **B**, not Class D.

---

## 5. Rejection status vocabulary

| Status | Meaning |
| --- | --- |
| **SELECTED** | Chosen for the current run |
| **CONDITIONAL** | Usable if a specified human / manual / paid / clarification step is accepted |
| **SOFT REJECT** | Usable, but inferior to another candidate — **retains fallback value** |
| **HARD REJECT** | Incompatible with the intended workflow under a reasonable reading |
| **NOT YET EVALUATED** | Identified, not assessed |

> **`MP-S-04`.** For every **SOFT REJECT** and **CONDITIONAL** candidate the ledger MUST answer,
> without restarting the investigation: *if all preferred candidates fail, how expensive would it be
> to make this one usable?*

**Hard-reject rules** — any one suffices: no lawful acquisition path of any kind; retention of a
local copy prohibited outright; simulator processing prohibited under **both** a broad and a narrow
reading of the terms; the data is not a daily close series for the required index; or the required
span is unavailable and cannot be assembled from one snapshot.

**Soft-reject rules:** materially inferior data quality or provenance; heavier recurring effort;
higher monetary cost; weaker reproducibility; or an ambiguity that is real but cheaply mitigable —
where a better candidate already exists.

---

## 6. Cost-ledger schema

> **`MP-S-05`.** Every seriously evaluated candidate is recorded — including rejected ones. A
> rejected candidate may later become the best available candidate, and its evaluation cost MUST NOT
> be spent twice.

Required fields per candidate: candidate/source identity · dataset identity · source authority ·
coverage · frequency/granularity · return composition · denomination · data-quality concerns ·
**axes A–H each with a verdict and evidence** · redistribution restriction · authentication/account
requirement · monetary cost · recurring human effort · engineering effort · reproducibility cost ·
provenance quality · unresolved legal/terms ambiguity · class · status · reason not selected ·
workaround · workaround cost · residual risk after workaround · fallback rank.

**Additive-only handling — a genuine tension, resolved.** A ledger is by nature mutable, but the
Owner-approved implementation-evolution rule states expressly that it **does not generalize to
preserved `docs/` artifacts**. The ledger therefore follows the **Baseline v1 → v2 full-restatement
precedent**: each evaluation round produces a **new numbered edition** (`…_ledger_001.md`,
`…_002.md`), superseding but never modifying its predecessor. No preserved edition is ever edited.

---

## 7. Fallback ranking

Ranking is multi-dimensional and MUST NOT optimize for data perfection alone. Dimensions: fitness for
the question · expected simulation error · coverage · data quality · provenance · reproducibility ·
legal/terms confidence · acquisition friction · recurring Owner effort · implementation effort ·
monetary cost · automation potential · maintainability.

Each round names: **BEST PRACTICAL CANDIDATE**, **LOWEST-COST FALLBACK**, **HIGHEST-QUALITY
FALLBACK**, and only as a last resort **NO ACCEPTABLE CANDIDATE**.

> **`MP-S-06`.** *Imperfection is a cost to measure, not automatically a reason to stop.*
> **NO ACCEPTABLE CANDIDATE** MUST NOT be returned merely because every candidate has defects. It
> requires showing that each candidate is HARD REJECT on the rules in §5. Conversely, a materially
> **misleading** dataset MUST NOT be accepted merely because it is easy to obtain.

---

## 8. Source-investigation stopping rule

> **`MP-S-07`.** Investigation stops at the **first Class A or Class B candidate** that meets the
> minimum properties below. Once one exists, further search requires an identifiable expected value
> exceeding the delay it imposes on the first Mode-P run — and that expectation must be stated in
> writing before the search continues.

**Minimum acceptable dataset properties:** daily observations of the NASDAQ-100 index; observation
date + closing level; the declared span obtainable in one snapshot; identifiable series semantics and
denomination; lawful local retention and simulator processing; and reproducible capture (stable
identity + hash).

**Maximum investigation depth per round:** terms and metadata for **at most three** candidates, in
the declared order, **no data retrieved**. If all three fail, stop and return to Owner Review with
the ledger — do not open a fourth without authorization.

**Search order** (identity only; none evaluated, none endorsed): (1) sources whose published terms
expressly permit programmatic access and private retention; (2) publisher-direct index data;
(3) general market-data aggregators. Selection MUST NOT consider simulated results — none exist
(§18.4.7).

---

## 9. Treatment of the FRED fail-closed attempt

> **`MP-S-08`.** The fail-closed outcome is **preserved exactly** and MUST NOT be rewritten. It is
> **not** retroactively claimed that autonomous AI retrieval was permitted; it was not.

But *"AI-agent acquisition failed closed"* MUST NOT be converted into *"FRED is unusable."* On the
axes of §3, and recorded in ledger edition 001:

- **A — NO.** FRED's prohibited-use clause bars *"robots, scraping, or similar data-gathering or
  extraction methods except as expressly allowed by the terms of use applicable to the FRED API."*
  The API route needs a key, i.e. account creation.
- **B — YES, apparently.** Browser download is expressly contemplated by FRED's own FAQ.
- **C — YES.** *"Copyrighted: Pre-approval required"* permits *"non-commercial educational or
  personal use"* without permission.
- **D / E — AMBIGUOUS, and this is the real obstacle.**

> **The decisive finding: human-in-the-loop acquisition does NOT cure FRED.** The blocking clause
> restricts *use*, not acquisition — *"Use the FRED® Services or FRED® Content **in connection with
> the development or training of any software program or system** or machine learning, including…
> large language models…"*. Read broadly, using the data to develop and validate the Mode-P simulator
> is prohibited **however the file arrives**. Read narrowly — the enumeration is entirely AI/ML, so
> *"software program or system"* may be coloured by that context — ordinary local simulation is fine.
> Both readings are available on the text. **The ambiguity is recorded, not resolved, and permission
> is not invented.**

FRED is therefore **CONDITIONAL / Class C**, blocked on a `D`/`E` question. Mitigation is Owner
action: a written clarification request to FRED (`stlsFRED@stls.frb.org`), low effort, unknown
latency, uncertain outcome — FRED cannot grant permission on Nasdaq's behalf, so a definitive answer
may require Nasdaq pre-approval. **Fallback value is preserved in full.**

---

## 10. Scope

This policy does not retrieve data, select a source, implement or execute Mode P, modify any
qualification-lane state, resolve any `P1-x` / `M-x` item, or treat any Simulation Trial output as
formal evidence.
