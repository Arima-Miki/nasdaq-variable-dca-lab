# Phase 1 TTM Qualification Owner Decision

**Status:** APPROVED

**Scope:** Phase 1 — Data Foundation

**Decision date:** 2026-08-11

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Owner Decision** |
| Subject | Qualification of MUFG/MURC historical USD/JPY TTM as a candidate Japan-side FX approximation |
| Decision status | **APPROVED** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this decision** |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| Nissay FX provider | **NOT IDENTIFIED** |
| Phase 2 | **BLOCKED** |

### Artifact role and precedence

This is a **Phase-1 Owner Decision**. It authorizes the use of **one research input** within a
narrowly defined Phase-1 research scope.

> **It is NOT a modification of the Phase-0 Baseline.**

- It is **not** part of the Frozen Phase-0 Owner Decision series OD-01 … OD-14, and it does not
  create, amend, or supersede any of them.
- The normative Baseline remains [`docs/experiment_spec.md`](../experiment_spec.md). Where this
  decision and that specification could be read as differing, **the specification governs
  Baseline behavior**.
- The Phase-0 decision history remains
  [`phase0_baseline_decisions.md`](phase0_baseline_decisions.md) and is unchanged.
- This decision contains **no Baseline results and no performance claims.**

---

## 2. Decision

**MUFG/MURC historical USD/JPY TTM is qualified for use as a candidate Japan-side FX
approximation.**

---

## 3. Scope

The qualification authorizes use of this source in:

- **local Phase-1 research;**
- **FX residual decomposition research;**
- **sensitivity analysis.**

The qualification exists because the source is **structurally similar** to the conversion
concept described in the Nissay prospectus:

> 「国内における計算日の対顧客電信売買相場の仲値」

Structural similarity of concept is the **entire** basis of the qualification.

---

## 4. Explicit non-claims

The qualification is deliberately narrow. It does **NOT** establish that:

- Nissay uses MUFG;
- Nissay uses MURC;
- MUFG/MURC is Nissay's actual FX provider;
- the MUFG/MURC TTM reproduces Nissay's actual FX conversion;
- Nissay uses the same fixing time;
- approximately 09:55 JST is an established MUFG fixing time;
- the commonly cited approximately ¥1 re-fixing threshold is valid;
- the archived final TTM was necessarily the point-in-time value available at every historical
  decision moment;
- raw MUFG/MURC data may be redistributed;
- raw MUFG/MURC data may be committed to this public repository;
- a Baseline FX convention has been approved;
- a Primary Proxy has been approved.

---

## 5. Required 2024-08-07 sensitivity treatment

Any future Phase-1 study using MUFG/MURC TTM **must explicitly handle 2024-08-07**, on which the
published quotation was suspended and a second quotation issued.

| Publication | TTM (JPY/USD) |
| ----------- | ------------- |
| Initial / first publication | ≈ **144.80** |
| Final / second publication | ≈ **147.04** |
| Difference | ≈ **¥2.24** — approximately **1.55 %** |

> **The future study must not silently choose one.**
>
> The choice must be **stated**, **justified**, and **where relevant tested under both
> readings**.

Supporting evidence is recorded in
[`../evidence/phase1_japan_side_ttm_qualification.md`](../evidence/phase1_japan_side_ttm_qualification.md)
§10.

---

## 6. Timing limitation

Approximately 09:55 JST may be described **only** as:

- conventional;
- secondary-source based;
- an assumption for sensitivity analysis.

> **It must NOT be described as an established MUFG determination time.**

No primary or near-primary source establishing the determination moment was found
(**PRIMARY TIMING EVIDENCE NOT FOUND**).

Additionally, JST observes no daylight saving while the United Kingdom and the United States
both do, on transition dates that are not always identical. **Any relative-timing statement
between JST, London, and New York observations must use calendar-aware timezone conversion per
observation date.** No fixed-hour relationship may be asserted.

---

## 7. Re-fixing limitation

> **Do NOT model a quantitative approximately ¥1 re-fixing threshold.**

No primary or near-primary evidence established such a threshold. The publisher's documented
trigger is qualitative only (「大きな変動」 — large movement).

---

## 8. Licensing and data-handling limitation

- **MUFG/MURC raw values must remain outside the public repository.**
- The qualification authorizes a **research input, not redistribution**.
- **Derived statistics** may be proposed for repository evidence, but their publication remains
  subject to the evidence and licensing boundaries already recorded in
  [`../evidence/phase1_japan_side_ttm_qualification.md`](../evidence/phase1_japan_side_ttm_qualification.md)
  §12 and [`../evidence/phase1_fx_source_research.md`](../evidence/phase1_fx_source_research.md)
  §6.
- MUFG's own site terms prohibit unauthorised use, reproduction, and modification; MURC's FX
  site publishes no terms-of-use page. **No legal conclusion is drawn by this decision beyond
  the recorded evidence.**

---

## 9. Relationship to the Phase-1 open items

This decision **does not change** any Phase-1 status recorded in
[`docs/experiment_spec.md` §19.1](../experiment_spec.md#191-phase-1-blocking-evidence-requirements),
which remains the authoritative register.

| # | Requirement | Status | Relationship to this decision |
| - | ----------- | ------ | ----------------------------- |
| **P1-7** | Currency treatment | **SUBSTANTIALLY ADVANCED** | A qualified candidate now exists for the Japan-side leg. The item does **not** reach RESOLVED: Nissay's provider and fixing time remain undisclosed, and the candidate remains an approximation of a concept. |
| **P1-8** | Licensing / redistribution | **PARTIAL** | This decision authorizes a bounded research use only. **Nothing is cleared for redistribution or for committing raw values.** |
| **P1-9** | Revision / restatement behaviour | **PARTIAL** | The re-fixing mechanism is documented and one in-window event is fully characterised, but no timestamps exist and annotation exhaustiveness is unverified. The §5 sensitivity condition exists because of this. |
| **P1-2** | Approved Primary Proxy | **OPEN — unchanged** | **This decision does not touch P1-2.** |

**P1-2 remains OPEN.**

**Phase 2 remains BLOCKED.** The Phase-1 blocking evidence requirements and the methodology
requirements recorded in [`docs/experiment_spec.md` §19](../experiment_spec.md#19-open-items-register)
are unchanged by this decision.

---

## 10. Evidence references

| Artifact | Role |
| -------- | ---- |
| [`../evidence/phase1_japan_side_ttm_qualification.md`](../evidence/phase1_japan_side_ttm_qualification.md) | Primary evidence basis for this decision — source chain, TTM definition, historical-data assessment, retrieval hazard, fixing-time tiers, re-fixing semantics, 2024-08-07 case study, reproducibility assessment, licensing |
| [`../evidence/phase1_fx_source_research.md`](../evidence/phase1_fx_source_research.md) | Preceding broad FX-source survey that identified the Japan-side TTM leg as the binding source-qualification question |
| [`../evidence/phase1_empirical_alignment_study.md`](../evidence/phase1_empirical_alignment_study.md) | Observation-time alignment evidence establishing the post-alignment residual that motivates FX residual decomposition |
| [`../experiment_spec.md`](../experiment_spec.md) | Normative Frozen Baseline — **unchanged** |

---

## 11. Confirmations

- **No Japanese bank is identified as Nissay's FX provider by this decision.**
- **No Primary Proxy is approved. P1-2 remains OPEN.**
- **No Baseline FX convention is approved.**
- **The Frozen Phase-0 Baseline and OD-01 … OD-14 are unchanged.**
- **No FX residual decomposition is authorized to report results by this decision** — it
  authorizes a research **input** only, under the limitations in §4 through §8.
- **No raw MUFG/MURC data may be committed to this repository.**
- **Phase 2 remains BLOCKED.**

---

**End of Phase-1 Owner Decision. Status: APPROVED, narrow and bounded.
P1-2 remains OPEN. Phase 2 remains BLOCKED.**
