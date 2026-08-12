# Phase 1 Evidence Artifact — Primary Proxy Qualification, Stage F: Licensing and Reproducibility

---

## 1. Metadata

| Field | Value |
| ----- | ----- |
| Artifact type | **Phase-1 Evidence Artifact** |
| Study | **Primary Proxy Candidate Qualification — Stage F** |
| Research date | **2026-08-12** (new source access dates 2026-08-12; retained Stage-C/E sources accessed 2026-08-11 and 2026-08-12) |
| Authorising decisions | Study design [`phase1_primary_proxy_qualification_study_decision.md`](../decisions/phase1_primary_proxy_qualification_study_decision.md) (criteria frozen at `1e8bc85`); Stage-F Owner Decisions **F-1 … F-8** |
| Closure decision | [`phase1_primary_proxy_stage_f_closure_decision.md`](../decisions/phase1_primary_proxy_stage_f_closure_decision.md) (**F-9 … F-13**) |
| Owner Review | **PENDING — prepared for Owner Review** |
| Phase | **Phase 1 — Data Foundation** |
| Baseline status | **Phase 0 Frozen — unchanged by this study** |
| Publication classification | **PUBLIC QUALITATIVE EVIDENCE** — documentary characterizations, classifications, and provenance descriptions only |
| Publisher wording | **PARAPHRASED, not reproduced.** Per Owner Decisions F-9 and F-12, publisher terms are characterized rather than quoted; no Terms-of-Use text is reproduced |
| Historical values | **NONE PUBLISHED.** No observation value, return, or derived statistic appears in this artifact |
| Source material | Retained **outside** the repository. No publisher file, provenance index, checksum file, or extracted text enters Git |
| Primary Proxy status | **NOT APPROVED — P1-2 remains OPEN** |
| `OJ-5` | **RESOLVED** by Owner Decision F-11 — bounded research-use disposition |
| `P1-8` | **PARTIAL** |
| Phase 2 | **BLOCKED** |

> **What this artifact is.** The record of what Stage F *researched and found* about each publisher's
> located terms, about `HG-11`, and about third-party reproducibility. It classifies located terms.
> It approves no Primary Proxy, applies no hard gate to the candidate set, eliminates no candidate,
> authorizes no redistribution or publication, and draws **no legal conclusion**.

> **On repository entry at Stage F.** The frozen study design records `Repository entry: Nothing`
> for Stages A–G and `Owner gate: No (reported at G)` for Stage F. This artifact exists because the
> Owner **explicitly directed** an execution-level review checkpoint (F-8) and a durable closure
> record (F-12). That is an Owner-authorized deviation, recorded rather than made silently. It does
> **not** amend the frozen study design. The same deviation was recorded at Stages C, D and E.

**Relationship to other documents.** The normative Frozen Baseline is
[`docs/experiment_spec.md`](../experiment_spec.md); this artifact does not modify it. The frozen
criteria — `HG-1 … HG-13`, `CT-1 … CT-9`, `ND-1 … ND-7`, `OJ-1 … OJ-6`, `SC-1 … SC-20` — are fixed
by the study design and are **used, never amended, here**. Stage-C, Stage-D and Stage-E findings
remain authoritative for their own stages; this artifact is **additive** and rewrites none of them.

---

## 2. Research objective

Stage F asks one question per publisher, and one per candidate:

> **What do located, readable, authoritative publisher terms establish about each of the eight
> frozen use classes — and does any of it positively restrict legitimate local research use?**

The governing severance, from Owner Decision S.1:

> **Publication capability is NOT a Primary Proxy hard gate.** It may be recorded as a comparative
> consideration (`CT-6`), a reproducibility limitation, or a publication-boundary constraint, but
> it must not silently become a reason to reject an otherwise methodologically qualified candidate.

### 2.1 Owner Decisions governing this execution

| # | Subject | Effect on execution |
| - | ------- | ------------------- |
| **F-1** | C-2A's unidentified FX provider | Assess Nasdaq and Invesco fully; FX leg recorded **NOT YET EVALUABLE**; route-level `HG-11` **PARTIAL**; do not fail C-2A for a gap the governance design created |
| **F-2** | Per-publisher scope | Matrix covers every publisher whose material materially entered the evidence record; `HG-11` consequences attach only through candidate-supporting publishers |
| **F-3** | Authoritative class list | The frozen §12 eight-class list governs; prior Phase-1 matrices are precedent and evidence only, and differently defined classes may not be silently equated |
| **F-4** | Stage F versus Stage H | Stage F performs **documentary characterization**; Stage H owns the binding publication determination |
| **F-5** | `N-4` | A `P1-8` publication issue with **no `HG-11` candidate consequence**; `F-02` not re-opened |
| **F-6** | Gate outcome versus elimination | Stage F records an `HG-11` outcome; **Stage G** owns application and elimination |
| **F-7** | Access boundary | No account, login, personal information, payment, entitlement, publisher contact, or click-through acceptance; gated evidence routes are stopped and reported |
| **F-8** | Owner Review checkpoint | Added at execution level; does not amend the frozen "Owner gate: No (reported at G)" |

---

## 3. Publisher and candidate scope as executed

| Publisher | Role | `HG-11` consequence |
| --------- | ---- | ------------------- |
| **Nasdaq, Inc.** | Index publisher for all four candidates | **Yes** — C-1 ×3 and C-2A |
| **Invesco** | Fund publisher for C-2A | **Yes** — C-2A only |
| **ニッセイアセットマネジメント** | S.3 evidence source; published no candidate | **None** (F-2) |
| **USD/JPY provider** | Required by any future C-2A construction | **Unidentified by design** (F-1) |

Candidates carried: C-1 `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY`; C-2A. C-2B does not advance; C-3 is out
of scope. The three C-1 series share a single publisher and therefore received one identical
assessment, satisfying `AC-4`.

---

## 4. Source inventory

All sources are **PRIMARY**. Every new retrieval was of a publicly served document requiring **no**
account, login, personal-information disclosure, payment, entitlement, publisher contact, or
click-through acceptance. Files are retained outside the repository; identifiers below are the
durable citation handles.

| ID | Document | Publisher | Date / version | Status |
| -- | -------- | --------- | -------------- | ------ |
| `D-02`, `D-04`, `D-05`, `F-01` | Calculation Manual; Index Methodology Guide; Recalculation Policy; Withholding Tax Rates | Nasdaq | 2026 | Retained at Stages C/E; **re-read**, not re-retrieved |
| `D-01`, `D-03`, `E-07` | NDX Index Methodology; NDX Index Versions; Feb-2026 Consultation | Nasdaq | 2026 | Retained; re-read |
| `T-01` | Terms of use | Invesco | last updated 2018-05-06 | **New** |
| `T-02` | Site terms of use | ニッセイアセットマネジメント | undated | **New** |
| `T-03` | Index-site disclaimer | Nasdaq | accessed 2026-08-12 | **New** |
| `T-04` | Data-entitlement catalogue | Nasdaq | accessed 2026-08-12 | **New** |
| `T-05`, `T-06` | `robots.txt` | Nasdaq index hosts; Invesco | accessed 2026-08-12 | **New** |

### 4.1 Sources not read, and why

| Source | Outcome |
| ------ | ------- |
| Nasdaq site-wide legal / terms | **NOT RETRIEVED.** The host was unreachable from the research environment on every attempt, across two HTTP versions and two independent clients. Its `robots.txt` was likewise unreachable. Recorded as an **access limitation, not an absence of terms** |
| Nasdaq index-data terms | **ROUTE STOPPED** under F-7. Reading them would require subscription or publisher contact. No account created, no contact made, no payment attempted, **no access control bypassed** |
| Nissay `robots.txt` | **NOT PUBLISHED.** The path returns HTTP 404 — the server answered with an error page. Recorded as an absence, which is distinguishable from unreadability |
| Broadridge (delivery channel for Invesco statutory documents) | **OUT OF SCOPE** by Owner Decision F-13. Recorded here only as a provenance/access caveat |

---

## 5. Nasdaq — eight-class matrix

**Operative located text, characterized rather than reproduced.** Four of the retained Nasdaq
documents carry a common front-matter clause asserting that the document's content is owned or
licensed by Nasdaq, and stating that unauthorized use is prohibited without Nasdaq's written
permission. The clause does not define which uses are authorized, does not mention research, and
grants nothing. The remaining three Nasdaq documents carry a **copyright assertion only**, with no
use clause. The index-site disclaimer carries a copyright assertion and an investment-advice
disclaimer, and contains **neither a reuse grant nor a reuse prohibition**.

| # | Class | Label | Basis |
| - | ----- | ----- | ----- |
| 1 | Local research access | **UNCLEAR** | The clause neither grants research use nor positively restricts it; "unauthorized" is undefined |
| 2 | Automated retrieval | **UNCLEAR**, with a positive `robots.txt` signal | The index hosts' `robots.txt` is readable and does not disallow any path used. **`robots.txt` is not a licence**; the site-wide policy could not be read |
| 3 | Local storage | **UNCLEAR** | Not addressed |
| 4 | Raw-value redistribution | **UNCLEAR** | Not addressed for index values; the index-data terms are entitlement-gated and unread |
| 5 | Transformed-series redistribution | **UNCLEAR** | Not addressed |
| 6 | Derived-statistic publication | **UNCLEAR** | Not addressed |
| 7 | Methodology / provenance citation | **UNCLEAR** | Not addressed; the clause conditions "use" on written permission but is silent on bibliographic citation |
| 8 | Repository inclusion | **UNCLEAR** | Not addressed |

**Class distinctions actually drawn by the located text.** The clause governs *document content*.
Index **values** are distributed through entitlement channels whose terms were not read. The located
text draws **no** distinction between transformed data and derived statistics. Nothing was inferred
from one class to another.

---

## 6. Invesco — eight-class matrix

**Operative located text, characterized rather than reproduced.** The terms assert copyright and
trademark protection over site materials and grant use limited to the reader's personal
non-commercial purposes or internal business purposes. A separate enumerated list of prohibited
activities addresses copying and redistribution, framing, automated access performed on a repeated
basis, automated data gathering and extraction, derivative use, and commercial exploitation. The terms are posted rather
than click-accepted; reaching them required no acceptance step.

| # | Class | Label | Basis |
| - | ----- | ----- | ----- |
| 1 | Local research access | **PERMITTED** | Express grant covering personal non-commercial and internal business use |
| 2 | Automated retrieval | **RESTRICTED** | The prohibited list expressly addresses automated access performed on a repeated basis, and automated data-gathering and extraction tools |
| 3 | Local storage | **UNCLEAR** | The personal-use grant and a separate prohibition on copying site content without express written permission are in tension; both are recorded, and the tension is **not resolved here** |
| 4 | Raw-value redistribution | **RESTRICTED** | The prohibited list expressly addresses copying, republishing, transmitting and distributing site material |
| 5 | Transformed-series redistribution | **RESTRICTED** | The prohibited list expressly addresses creating derivative use of site content |
| 6 | Derived-statistic publication | **RESTRICTED** | Same derivative-use limb |
| 7 | Methodology / provenance citation | **UNCLEAR** | Not addressed as such |
| 8 | Repository inclusion | **RESTRICTED** | Follows from the redistribution prohibitions |

Invesco's `robots.txt` disallows a number of fund-performance and historic-price paths; **none of
the paths actually used by this study is among them**.

---

## 7. Nissay — eight-class matrix

**Publication and evidence-handling axis only. No candidate `HG-11` consequence** (F-2).

**Operative located text, characterized rather than reproduced.** Two clauses apply. The first
asserts that all copyright and intellectual-property rights in the material belong to the company
and prohibits reproduction, reprinting and **quotation** without permission. The second asserts
copyright over site works and, **except where copyright law itself permits**, prohibits
unauthorized use and a list of enumerated acts — including reproduction, modification, **analysis**,
uploading, transmission, distribution, transfer, lending, licensing, sale and publication — absent
the company's prior written permission.

| # | Class | Label | Basis |
| - | ----- | ----- | ----- |
| 1 | Local research access | **RESTRICTED**, subject to a statutory carve-out **not interpreted here** | Analysis is named in the enumerated prohibited acts |
| 2 | Automated retrieval | **UNCLEAR** | No `robots.txt` published; the terms are silent on automation |
| 3 | Local storage | **RESTRICTED**, subject to the carve-out | Reproduction is named |
| 4 | Raw-value redistribution | **RESTRICTED** | Reproduction, reprinting and distribution are named |
| 5 | Transformed-series redistribution | **RESTRICTED** | Modification is named |
| 6 | Derived-statistic publication | **RESTRICTED** | Distribution and publication are named |
| 7 | **Methodology / provenance citation** | **RESTRICTED**, subject to the carve-out | **Quotation is expressly named** among the prohibited acts |
| 8 | Repository inclusion | **RESTRICTED** | Follows from the above |

> The clause's own statutory carve-out is recorded as part of the located text. **Whether that
> carve-out applies to any particular act is a legal question, and this study does not answer it.**

---

## 8. `HG-11` findings under the §5.5 three-way rule

### 8.1 C-1 — `NDXJPY`, `XNDXJPY`, `XNDXNNRJPY`

Each depends on **Nasdaq alone**, whose local-research-access class is **UNCLEAR** — readable terms
that neither grant nor positively restrict research use. Under §5.5's third row this escalates to
`OJ-5`; it is **not** an automatic failure.

Owner Decision **F-11** then resolved `OJ-5` for the current evidence state:

> **`HG-11` = BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED.**

### 8.2 C-2A

| Leg | State |
| --- | ----- |
| Nasdaq | **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY RESTRICTED** |
| Invesco | **PERMITTED** for local research use |
| USD/JPY provider | **UNIDENTIFIED BY DESIGN**; `HG-11` **NOT YET EVALUABLE** |

> **Route-level `HG-11` = PARTIAL**, unless the frozen Stage-G application requires a more specific
> state.

### 8.3 What was not established

- **No candidate failed `HG-11`.** No positive restriction on legitimate local research use was
  located for any candidate-supporting publisher.
- **No candidate passed `HG-11`.** A bounded qualification is **not** a PASS and must not be
  silently converted into one.
- **`SC-12` was not triggered** — the terms are not entirely unreadable; the Nasdaq clause was read
  directly from four independently retained documents.
- **`SC-13` was not triggered** — no positive restriction on local research use was located for any
  candidate publisher.

---

## 9. Third-party reproducibility assessment

Assessed **separately** from `HG-11`, and deliberately **not** converted into a hidden hard gate.

| Access class | C-1 | C-2A |
| ------------ | --- | ---- |
| Publicly viewable documentation | **Yes** — the full methodology chain | **Yes** — statutory and financial documents |
| Manually retrievable | **Yes** | **Yes**, one document via the issuer's delivery service |
| Automated retrieval available | Not required; permitted-by-signal only | **Restricted by terms** |
| Entitlement-gated material | **Yes — the index value series** | A full NAV history is not established as publicly retrievable |
| Inaccessible / unreadable terms | Nasdaq site-wide and index-data terms | Same, plus Invesco fully readable |
| Unidentified dependencies | None | **Yes — the FX provider** |
| Redistribution limitations | UNCLEAR throughout | RESTRICTED for several classes |

> **C-1: the documentary path is fully reproducible; the data path is not**, because the value
> series is entitlement-gated. An independent researcher could verify how each series is defined,
> but could not obtain the series on the same terms. This compounds the Stage-D findings that
> `SC-6` excludes the pre-base-date segments and that `H-1` is NOT ESTABLISHED.

> **C-2A: not reproducible end-to-end by anyone, including this project**, because one required
> input is unidentified by design.

---

## 10. Publication-boundary implications

### 10.1 The composition rule

Permissions were **not averaged**. A jointly derived result can be no more publishable than its
least-clear contributing source.

- **C-1-derived results** are governed by Nasdaq — UNCLEAR across classes 4–8 → **not authorized**
  under the fail-closed policy.
- **C-2A-derived results** are governed by the more restrictive of Nasdaq and Invesco → **not
  authorized**.

Both are presently moot in practice: `AC-2` means no derived numerical result exists.

### 10.2 Verbatim publisher quotations already committed

Stage F established that all three publishers' located terms condition reproduction of their text
on prior permission. The committed Stage-C, Stage-D and Stage-E artifacts each contain **short
verbatim publisher quotations**, recorded because the frozen study design requires publisher
characterizations to be captured verbatim.

The project's bounded finding, and no more:

> **The available terms evidence is not treated as sufficient to affirmatively authorize public
> reproduction of those quotations under the project's fail-closed publication policy.**

Per Owner Decision F-9: **no existing artifact is modified**, no history is rewritten, and no
characterization is made that prior publication or retrieval was unlawful, that the quotations are
legally prohibited, or that any statutory exception does or does not apply. The final disposition
belongs to **Stage H**, which is directed to review explicitly whether the public artifact should
retain, paraphrase, or de-quote them.

This artifact applies that direction to itself: publisher wording is **paraphrased throughout**.

### 10.3 `N-4`

The located Nasdaq document-level clause conditions use of Nasdaq document content on written
permission, and **does not establish publication or redistribution permission** for any Nasdaq
document. The Nasdaq site-wide terms could not be read. `F-02` was **not** re-opened, **not**
re-inspected, and **not** reproduced.

> **`N-4` = OPEN / FAIL-CLOSED FOR PUBLICATION**, handed forward to Stage H / `P1-8`.

No claim is made that publication is legally prohibited, that the marking is ineffective, that
public accessibility overrides it, or that retrieval was unlawful.

---

## 11. Comparative-criteria inputs

Recorded as **inputs to Stage G**, applied only among survivors, never scored (`AC-8`).

| # | Criterion | C-1 (×3) | C-2A |
| - | --------- | -------- | ---- |
| **`CT-5`** | Clarity of local-research-use permission | Nasdaq **UNCLEAR** | Nasdaq **UNCLEAR**; Invesco **PERMITTED**; FX **unassessed** |
| **`CT-6`** | Publication / redistribution capability | **UNCLEAR** across classes 4–8 | **UNCLEAR** (Nasdaq) and **RESTRICTED** (Invesco) |

Per **S.1**, `CT-6` is a comparative consideration only and must not become a reason to reject an
otherwise methodologically qualified candidate.

---

## 12. Stop conditions

**None triggered.**

| # | Status | Reason |
| - | ------ | ------ |
| `SC-7` | Not triggered | Every characterization rests on primary publisher text; no secondary summary was substituted |
| `SC-12` | Not triggered | Terms are not entirely unreadable |
| `SC-13` | Not triggered | No positive restriction on local research use for any candidate publisher |
| `SC-14` | Not triggered | No automated retrieval was required; every retrieval was a single manual fetch |
| `SC-15` | Not triggered | No plausible-wrong-value hazard arose |
| `SC-18` | Not triggered | No frozen criterion needed to change |
| `SC-19` | Not triggered | No coverage regression |

"Terms unreadable" and "terms readable but silent" were kept strictly apart throughout.

---

## 13. Evidence-integrity caveats

1. **An unreachable host is not an absent policy.** The Nasdaq site-wide terms host failed with
   three distinct transport signatures across two HTTP versions and two independent clients. Because
   a transport failure and an absence of terms are indistinguishable in a bare result, the outcome
   is recorded as *terms not read due to access limitation*, and **no inference is drawn in either
   direction** about their content.
2. **A 404 is different.** The Nissay `robots.txt` request was answered — with an error page. That
   distinguishes *no policy published* from *policy unreadable*, and both are recorded as such.
3. **A literal search of the Nasdaq documents returns a false negative** on the operative use
   clause, because subset-font encoding garbles the key word. The clause was confirmed from four
   independently retained documents that agree.

Consistent with the Stage-C research-integrity finding: fluent extraction output and zero-hit
extraction were not trusted without an integrity check. The temporary tooling is **not** committed
and is deliberately not recorded as a repository architecture requirement.

---

## 14. Anti-circularity verification

- **`AC-2`.** No performance quantity was computed. Stage F performed **no calculation of any kind**.
- **`AC-3`.** `ND-1 … ND-7` were not used. **No candidate performance was used to interpret any
  licensing term.**
- **`AC-4`.** The three C-1 series share one publisher and received one identical assessment.
- **`AC-8`.** No scoring, no weighting, no ranking. The matrices carry labels, never scores, and no
  publisher or candidate was ranked by permissiveness.
- No Primary Proxy was selected, and no candidate was eliminated.

---

## 15. Publication and external-material boundary

**No publisher source file, provenance index, checksum file, extracted text, or Terms-of-Use text
enters Git.** Publisher wording is paraphrased, not reproduced. No historical value, return, or
derived statistic appears. No credentials or personal information appear.

All source material is retained **structurally outside** the repository. Redistribution terms remain
**unestablished** for every source used at Stages C, D, E and F; the fail-closed policy applies and
**nothing is cleared for republication**.

---

## 16. What this artifact establishes

1. **Located primary terms exist and were read for all three publishers whose material materially
   entered the evidence record.**
2. **No candidate-supporting publisher positively restricts legitimate local research use**, so no
   candidate fails `HG-11`.
3. **Nasdaq's local-research-access class is UNCLEAR** — identically for all four candidates,
   because they share that publisher.
4. **Invesco's local-research-access class is PERMITTED** for personal non-commercial and internal
   business use.
5. **Nissay's terms restrict several classes**, including citation, subject to a statutory carve-out
   this study does not interpret — with **no candidate consequence**.
6. **Redistribution and publication are not authorized for any source**, on the evidence located.
7. **C-1's documentary path is reproducible; its data path is not. C-2A is not reproducible
   end-to-end by anyone.**

---

## 17. What this artifact does NOT establish

- It does **not** approve a Primary Proxy — **P1-2 remains OPEN**.
- It does **not** pass any hard gate. A bounded qualification is **not** a PASS.
- It does **not** eliminate any candidate — that is Stage G's application.
- It does **not** establish that Nasdaq has granted permission for anything.
- It does **not** authorize redistribution, publication, repository inclusion, automated retrieval,
  entitlement-gated access, or retrieval of historical index values.
- It does **not** resolve `P1-8`.
- It does **not** draw any legal conclusion, and does **not** decide whether any statutory exception
  applies to any act.
- It does **not** determine what this project will publish — that is **Stage H**.
- It does **not** resolve `O-3`, `HG-4` for C-2A, `HG-8`, `OJ-1`, `OJ-4`, `N-2` continuity, `N-3`,
  or `N-4`.
- It does **not** amend the Frozen Phase-0 Baseline, OD-01 … OD-14, or any frozen criterion.
- It does **not** authorize Stage G or Stage H, and does **not** unblock Phase 2.

---

## 18. Phase-1 requirement impact

| # | Requirement | Status | Effect of Stage F |
| - | ----------- | ------ | ----------------- |
| **P1-2** | Approved Primary Proxy | **OPEN** | Unchanged |
| **P1-7** | Currency treatment | **Unchanged** | The FX provider remains unidentified by design |
| **P1-8** | Licensing / redistribution | **PARTIAL** | Three publishers now carry located primary terms and a recorded matrix. **Nothing is cleared for redistribution or for committing raw values.** Two Nasdaq class groups remain unread by authorized design |

---

## 19. Handoffs

**To Stage G.** Per-candidate `HG-11`: C-1 ×3 **BOUNDED QUALIFICATION — UNCLEAR, NOT POSITIVELY
RESTRICTED**; C-2A **PARTIAL** (Nasdaq bounded, Invesco PERMITTED, FX NOT YET EVALUABLE). The three
matrices as the citation base. `CT-5` and `CT-6` inputs. The reproducibility assessment. **No
candidate eliminated.**

**To Stage H.** The per-source publication-boundary determination, including: the composition-rule
consequences; `N-4`; the already-committed-quotation question under F-9, with the four options the
Owner named — retain, paraphrase, reduce to non-quotational characterization, or otherwise apply the
publication boundary; and the unread Nasdaq classes.

**Carried unresolved.** `O-3`; the C-2A FX leg and `HG-4`; `HG-8`; `HG-5` and `HG-13` (unassigned to
any stage); Stage-D `SC-6` and `H-1`; `OJ-1`; `OJ-4`; `N-2` continuity; `N-3`; `N-4`.

---

## 20. Limitations

1. **Stage F is documentary.** It records what located terms say, not what they mean in law.
2. **Two Nasdaq class groups were not read** — the site-wide terms (host unreachable) and the
   index-data terms (entitlement-gated, route stopped under F-7). Their labels are UNCLEAR by
   absence of evidence, not by evidence of absence.
3. **The Nissay statutory carve-out is unresolved by design**, and the classification is recorded
   subject to it.
4. **The Invesco local-storage tension is recorded, not resolved.**
5. **Terms change.** Every label is anchored to a dated retrieval and may not describe the terms at
   any other time.
6. **Broadridge was not assessed**, per F-13; if reproducibility or lawful local research use is
   later shown to depend on it rather than merely on delivery through it, the matter returns to the
   Owner.

---

## 21. Confirmations

- **The Frozen Phase-0 Baseline is unchanged.** OD-01 … OD-14 are untouched.
- **The frozen qualification criteria are unchanged.** `1e8bc85` remains the criteria-freeze
  boundary.
- **No prior evidence artifact or decision was rewritten**, and no Git history was altered.
- **No Primary Proxy was approved. P1-2 remains OPEN.**
- **No candidate was ranked, scored, selected, or eliminated. No hard gate was applied.**
- **No legal conclusion was drawn.**
- **No account was created, no login used, no personal information disclosed, no payment made, no
  entitlement requested, no publisher contacted, and no click-through accepted. No access control
  was bypassed.**
- **No publisher source material, extracted text, or Terms-of-Use text is committed to this
  repository.**
- **Stage G has not begun. Stage H has not begun.**
- **Phase 2 remains BLOCKED.**
