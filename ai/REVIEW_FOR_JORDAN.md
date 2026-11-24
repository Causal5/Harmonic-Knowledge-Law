# Review for Jordan — remaining definitions, main-only fixes, and decisions

**TL;DR.** As of 24 November 2026 (America/New_York), `Release/` on `main` is at `56c6ab5`. Jordan has now: published Central Valley worked example v0.2; locked the Bite 5 spatial boundaries (Bite 5 still unscored); adopted the four process aids as a published research procedure; archived experimental `src/` as example-only code; applied selective status banners to the Sahel, AEF, HKL, and buffer drafts; and corrected the mussel-example wording in §B. What remains for him is **§A only** — terms to define, retire, or leave unofficial. No definition is invented here, and this file is not a publication to `main`.

**How to use this.** Work §A. Sections B and C are closed against `main` at `56c6ab5`, with a re-check recorded below. Suggestions that were in §B were suggestions only; he has now edited `main`.

---

## A. Terms only you can define

Each item is used in the corpus, has no official definition in Registry v0.3.2 or the reconciled papers on `main`, and will not be filled in by an agent. You may define it, retire it, or explicitly leave it unofficial. Do not treat any historical formula below as a proposed official meaning.

### A1. Absorbic Unit (AU) / “ethical joule” — high

- **Where used.** Official papers already *reserve* it: Registry v0.3.2 line 231, “Reserved/undefined; no ‘ethical joule’ is established”; current AEF §6 line 158, same statement. Older drafts still talk as if a unit existed: `Release/Working/buffer-as-temporal-dimension.md` on `main`, line 263, “currently has a thermodynamic-analog definition (\(1\,AU = 1\,J / 1\,\Delta S_{abs}\))”; AEF v2 §3.3.
- **Why it needs a decision.** A reviewer who finds the draft first will think you have a physical “ethical joule.” The official papers already say you do not. If you want a unit, only you can define it. If you do not, a one-line confirmation that it stays reserved would close the gap.
- **What the corpus already says.** AU is reserved and undefined. No official unit, conversion, or ethical-joule equivalent is established. This cycle invents none.

### A2. *HKL-AI Score* (0–1, informal thresholds and weights) — high if a reviewer opens CorePrinciples or `src/`

- **Where used.** `CorePrinciples/Glossary.md` lines 15–17 and related CorePrinciples files (`HKL_Water_Metric.md`, `Law_of_We_Full.md`); experimental `src/IIF_Evaluator.py` (now archived at `archive/examples/giln-iif/`; former 0.4 / 0.3 / 0.3 weighting, now disabled). Mentioned with informal thresholds <0.3 “Critical Misalignment” and 0.6–0.8 “Alignment,” and a DeepSeek 0.27→0.68 / “90% resource reduction” story.
- **Why it needs a decision.** The name looks like an official HKL metric. It is not in Registry v0.3.2. A reviewer can quote the historical glossary as if it were current scoring.
- **What the corpus already says.** Not in the current registry or reconciled papers. Bannered as historical on this branch. `src/` no longer computes the old weighting. No official score, threshold, or weight is invented here.

### A3. Systemic Resonance Index (SRI) — high, same reason as A2

- **Where used.** `CorePrinciples/Glossary.md` line 27; experimental `src/GILN_AI.py` (`calculate_sri`).
- **Why it needs a decision.** Same reviewer path: a named index in recovered files and code, with no official definition.
- **What the corpus already says.** Not in Registry v0.3.2. Experimental code may return `None`. No official formula is invented here.

### A4. Harmonic Resonance Score (HRS) — high, same reason as A2

- **Where used.** CorePrinciples glossary (SRI entry); experimental `src/` (`hrs` arrays).
- **Why it needs a decision.** Same as A3.
- **What the corpus already says.** Not in Registry v0.3.2. Initial `hrs` values are `None`, not zeros pretending to be scores. No official formula is invented here.

### A5. Axis (A) as a current official symbol — medium

- **Where used.** `CorePrinciples/Glossary.md` line 7; `CorePrinciples/CausalEthicsAxis.md`; Law of We glossary. Described there as a “universal constant” / one-dimensional equilibrium manifold.
- **Why it needs a decision.** The word is load-bearing in the historical files and easy to confuse with HKL’s declared viable region or \(V^*\).
- **What the corpus already says.** Not in the current registry symbol tables or reconciled papers. Charter Layer 0 does not define it. Historical wording is preserved under a banner. This map does not promote or rewrite it.

### A6. Variation (\(\Delta\)) formulas \(f(E)=kE\times(1+\text{impact})\), \(\Delta'=\Delta-f(E)\) — medium

- **Where used.** `CorePrinciples/Glossary.md` lines 23, 29, as geodesic distance from the Axis.
- **Why it needs a decision.** Easy to confuse with HKL \(V\) or \(\Delta V\).
- **What the corpus already says.** Not in Registry v0.3.2. Do not identify this \(\Delta\) with HKL \(V\) or \(\Delta V\). No official formula is invented here.

### A7. Manuscript buffer primitives \(\mathcal{C}(t)\), \(J_{PAE}\), \(\rho_{regen}\), \(\kappa_{coord}\), \(\Omega_{var}\) — medium

- **Where used.** `Release/Working/buffer-as-temporal-dimension.md` (a working draft, not an override authority).
- **Why it needs a decision.** Only if you want any of them as official Layer 1 objects. Official buffer already exists.
- **What the corpus already says.** Current official buffer on `main` is \(\tau^\pi_{buf,\Omega}\) (Registry §VII, HKL §6). The 16 October record leaves the manuscript’s universal flux/coherence claims unpromoted. The v0.4 draft, also unpromoted, only discusses migrating some of them. No official promotion is made here.

### A8. Process labels `ineligible` / `needs-mapping` / `eligible-as-application` — lower

- **Where used.** Round 6–9 notes on this branch only (`ai/` ratification-pending aids).
- **Why it needs a decision.** Only if you want them as Registry vocabulary. They are not required to read the official papers.
- **What the corpus already says.** Not in the Registry or the 16/30 October records on `main`. Application quantities do not become universal primitives by appearing in an example (`Release/Examples/README.md` on `main`).
- **24 November 2026 note (not a new definition).** The published [`empirical-review-procedure.md`](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/empirical-review-procedure.md) on `main` now uses these as *worksheet labels with procedural status*, not as Registry vocabulary. They still need an explicit decide / retire / leave-unofficial as official symbols if you want them in the registry.

---

## B. Errors or overreach on `main` — re-checked 24 November 2026

Re-checked against `main` at `56c6ab5` (mussel corrections landed in `f81967d`). **B1–B7 are closed.** Original findings are preserved below so the history is not silently rewritten.

### B1. Mussel §8 item 3 qualitative *severed* assignment — closed

- **Was.** `main` line 152 assigned the flag from a story (“so the population carries the registry’s *severed* flag”) while the 30 October record said no \(\eta_{TM}\) had been computed.
- **Now (`f81967d`, still at line 152).** “Historical records suggest that the dam largely blocked upstream host-fish access after 1913, with rare high-water passage such as the 1986 episode [4]. Natural renewal coverage (\(\eta^{nat}_{TM}\)) remains uncomputed above and below Keokuk. The registry assigns *severed* when that ratio is zero apart from declared episodic events. The flag and the *net mining* or *substituted* classifications remain unassigned pending recruitment and loss data under a prespecified protocol. [15]”
- **Status.** Closed. The flag is no longer assigned from the narrative.

### B2. Conclusion called the case “an example of buffer depletion” — closed

- **Was.** Line 168 used that phrase though the 30 October record said no buffer had been computed.
- **Now (line 168).** “The historical record illustrates interrupted renewal, delayed reproductive consequences and later corrective effort. The 30 October decision record reports that field renewal coverage, ACR and buffer have yet to be computed for this case. The Sahel and Central Valley studies provide comparisons. [15, 17, 18]”
- **Status.** Closed.

### B3. Yangtze analog over-claimed “operational versions of this test,” and used “severed pathway” — closed

- **Was.** Line 155.
- **Now (line 155).** Opens “Published Yangtze studies offer comparisons for how stocking and habitat restoration affect renewal.” The paddlefish clause now says “the endpoint when a blocked migratory pathway has no substitute.”
- **Status.** Closed.

### B4. Ordinary-language “severed” in §8 item 5 and line 40 — closed

- **Was.** “whose access can be severed independently” (line 157) and “If that link is severed” (line 40).
- **Now.** “whose access can be blocked independently” (line 157); “If that host-fish link is broken” (line 40).
- **Status.** Closed.

### B5. Conclusion “shows that especially clearly” — closed

- **Was.** Line 164.
- **Now (line 164).** “The Keokuk–skipjack record illustrates this distinction historically.”
- **Status.** Closed.

### B6. Unmarked withdrawn wording in the Sahel addendum — closed (selective)

- **Now.** `Release/Examples/sahel-logistic-addendum-section9-draft.md` on `main` has a top-level status banner: unpromoted addendum; current Sahel §§5–6 withdraw the completed drift-sign and falsification claims. Some body passages (for example the old sign-flip “empirical anchor” language) are still present under that banner. That matches Jordan’s “selective” marking. The earlier, more extensive in-place `[STALE]` / `[DEAD CITE]` marks from this branch were not all copied to `main`; Git history on `ai/evolution` still has them.

### B7. Unmarked stale wording in Working drafts — closed (selective)

- **Now.** `Release/Working/absorbic-effort-framework-v2.md`, `hkl-lyapunov-v2.md`, and `buffer-as-temporal-dimension.md` on `main` each have a top-level status banner pointing at the current HKL and AEF papers (and, for the buffer draft, at the reserved status of AU). The stale body sentences named in the original finding remain in the drafts under those banners. Again, that is the selective marking Jordan applied. This branch was synced to those published drafts on 24 November 2026.

**Still open on `main` from this B list:** none of B1–B7 as originally filed. The only leftover is that the draft *bodies* still contain historical wording, now clearly statused as historical. That is not a new contradiction with the 30 October record.

---

## C. Decisions — closed 24 November 2026

Jordan stated that all five decisions are resolved and implemented. Verified against `main` at `56c6ab5` and the current `ai/evolution` archive:

1. **Bite 5 boundaries — closed.** Recorded in `Release/Examples/central-valley/README.md` on `main` (“Study boundaries adopted 24 November 2026”): USGS CVHM2 historical-grid footprint for the Central Valley; union of the 19 DWR Bulletin 118 `5-022.01`–`5-022.19` subbasins for the San Joaquin Valley; Tulare Lake `5-022.12` as the pilot. The v0.2 worked example and the Examples README say **Bite 5 remains open / unscored**. Protocol v0.2 on `main` now points at that boundary decision.
2. **Accepted proposals archive — closed, with a bookkeeping note.** `ai/PROPOSALS/README.md` indexes 19 accepted proposals through Round 19, each with a verdict and evidence link. The freshwater-dictionary proposal folder is not in the current tree; the index points at it in Git history (`6797c98`). A later 24 November Tulare pumping-storage proposal (`ai/PROPOSALS/2026-11-24-tulare-pumping-storage/`, status `proposed`) is on the branch and is **not** one of those 19.
3. **Process aids — closed as published research procedures.** `Release/Examples/empirical-review-procedure.md` on `main` (`f81967d`) adopts the four aids (computed-status assignment; application-quantity inheritance labels; object-class declaration; four-field effort recording) and says when each worksheet applies. The original `ai/NOTES/` sheets are preserved and now carry an adoption banner pointing at that procedure. Their body status lines still say “ratification-pending”; the published procedure is the adopted text.
4. **Experimental `src/` — closed.** On both `main` and this branch the code lives at `archive/examples/giln-iif/` and is labeled example-only. The two trees are identical. There is no live `src/` on either branch.
5. **Draft markings on `main` — closed (selective).** Status banners are on the Sahel addendum and the AEF, HKL, and buffer Working drafts on `main` (`f81967d`). This sync copies those published drafts onto `ai/evolution`.

---

## D. Closed earlier (Round 19), and in this sync

**Round 19 (preserved).** Re-pulled `main` at `270942c` for the item 4 site correction; bannered historical and unpublished files; disabled unofficial `src/` placeholders; wrote this review’s original A–C list. Official papers were not rewritten. No definition was invented.

**24 November 2026 sync (this update).**

- Fetched `main` at `56c6ab5`. Copied Central Valley worked example **v0.2** and the archived **v0.1** (byte-identical to `main`) onto `ai/evolution`, replacing the live v0.1 path. Protocol v0.2, the definition crosswalk, MANIFEST, publication index, empirical review procedure, and the selectively marked drafts were synced from `main`.
- Branch-only CV files (dictionary, Bite 5 checklist, worked fill, DWR coverage audit) were kept. The standalone `PUMPING-STORAGE.md` writeup is marked **superseded as the published narrative** by v0.2; the crosswalk CSV is on both branches.
- Mussel §8 and the conclusion on this branch now follow the published `main` text. The LD19 retrieval note remains unpublished branch work.
- §B1–B7 and §C1–C5 marked closed as re-checked above.
- Charter current-`main` pointer updated to `56c6ab5`. Starting pin `c9e1277` preserved.

---

**What should be left.** The §A terms, which only Jordan can define, retire, or explicitly leave unofficial. Official example wording on `main` no longer contradicts the 30 October record on the *severed* flag or an uncomputed buffer. Bite 5 remains unscored, as he directed.
