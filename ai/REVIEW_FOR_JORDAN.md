# Review for Jordan — remaining definitions, main-only fixes, and decisions

**TL;DR.** `Release/` on `main` (now `270942c`, 23 November 2026, America/New_York) is the published source. You already fixed mussel §8 item 4 (the fish-passage site is Lock and Dam 22 near Saverton). What is left for you is: (A) terms only you can define, retire, or leave unofficial; (B) a short list of wording on `main` that a hostile reviewer could use against the premise, with suggested replacement text; (C) a few pending decisions. This branch has done the agent-fixable clarifications. Nothing here invents a definition, and nothing here is a publication to `main`.

**How to use this.** Work A and B first; they are the ones that can sink the premise. Suggestions in B are suggestions only — you edit `main`. Prioritized by reviewer risk.

---

## A. Terms only you can define

Each item is used in the corpus, has no official definition in Registry v0.3.2 or the reconciled papers on `main`, and will not be filled in by an agent. You may define it, retire it, or explicitly leave it unofficial. Do not treat any historical formula below as a proposed official meaning.

### A1. Absorbic Unit (AU) / “ethical joule” — high

- **Where used.** Official papers already *reserve* it: Registry v0.3.2 line 231, “Reserved/undefined; no ‘ethical joule’ is established”; current AEF §6 line 158, same statement. Older drafts still talk as if a unit existed: `Release/Working/buffer-as-temporal-dimension.md` on `main`, line 263, “currently has a thermodynamic-analog definition (\(1\,AU = 1\,J / 1\,\Delta S_{abs}\))”; AEF v2 §3.3.
- **Why it needs a decision.** A reviewer who finds the draft first will think you have a physical “ethical joule.” The official papers already say you do not. If you want a unit, only you can define it. If you do not, a one-line confirmation that it stays reserved would close the gap.
- **What the corpus already says.** AU is reserved and undefined. No official unit, conversion, or ethical-joule equivalent is established. This cycle invents none.

### A2. *HKL-AI Score* (0–1, informal thresholds and weights) — high if a reviewer opens CorePrinciples or `src/`

- **Where used.** `CorePrinciples/Glossary.md` lines 15–17 and related CorePrinciples files (`HKL_Water_Metric.md`, `Law_of_We_Full.md`); experimental `src/IIF_Evaluator.py` (former 0.4 / 0.3 / 0.3 weighting, now disabled). Mentioned with informal thresholds <0.3 “Critical Misalignment” and 0.6–0.8 “Alignment,” and a DeepSeek 0.27→0.68 / “90% resource reduction” story.
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

---

## B. Errors or overreach on `main` that only you can fix

Suggested wording is a suggestion, not a silent edit of `main`. Official papers themselves are already carefully hedged. The risks below are almost all in the mussel example and in unmarked drafts a reviewer might open.

### B1. Mussel §8 item 3 assigns the *severed* flag from a story — highest

- **File.** `Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md` on `main`, line 152.
- **Quote.** “Natural renewal coverage, \(\eta^{nat}_{TM}\) (natural renewal divided by losses), for ebonyshell above Keokuk after 1913 is effectively zero apart from rare high-water passage such as 1986, so the population carries the registry’s *severed* flag.”
- **Why it can sink the premise.** The same `Release/` tree, 30 October record line 306, says no field \(\eta_{TM}\) has been computed for the mussel case. Registry §VII.1 sets the flag only when a computed \(\eta^{nat}_{TM}=0\). A reviewer can quote the example against the registry and call the framework inconsistent. You already corrected the neighboring item 4; this is the remaining internal contradiction.
- **Suggested wording.** “The 30 October 2026 decision record states that no field \(\eta_{TM}\) has been computed for the mussel case, and that computing \(\eta^{nat}_{TM}\) for ebonyshell above and below Keokuk would be the first application, if recruitment data exist. Qualitatively, and provisionally only, host-fish access above Keokuk after 1913 appears effectively blocked apart from rare high-water passage such as 1986 [4]. That narrative is not a computed ratio and does not by itself assign the registry’s *severed* flag. The flag is set when \(\eta^{nat}_{TM}=0\) apart from declared episodic events; that assignment remains pending a computed renewal ratio on a locked protocol. Whether the stock would be *net mining* or *substituted* also remains unmeasured here.”

### B2. Conclusion calls the case “an example of buffer depletion” with no computed buffer — highest

- **File.** Same example on `main`, line 168.
- **Quote.** “Within HKL, this is an example of **buffer depletion**, temporally delayed reproductive consequences, loss of some native functional response options, and subsequent requirements for targeted corrective effort.”
- **Why it can sink the premise.** The 30 October record (line 306) also says no buffer has been computed for the mussel case. Naming the case “buffer depletion” inside HKL, in the official example, is the same kind of qualitative assignment as B1.
- **Suggested wording.** “Within HKL, this case is a source-qualified illustration of interrupted renewal pathways, temporally delayed reproductive consequences, and later corrective effort. It is not a computed buffer, ACR, or \(\eta\) result. The 30 October 2026 record states that no field ACR, \(\eta_{TM}\), or buffer has been computed for the mussel case. The comparative work on Sahel regulation and Central Valley temporal mining supplies conceptual neighboring cases, not evidentiary substitutes. [15, 17, 18]”

### B3. Yangtze analog over-claims “operational versions of this test,” and uses “severed” next to the registry flag — high

- **File.** Same example on `main`, line 155.
- **Quote.** “The Yangtze already supplies operational versions of this test.” Later in the same paragraph: “the endpoint when a severed pathway has no substitute.”
- **Why it can sink the premise.** The paragraph is useful and sourced, but “operational versions of this test” sounds like a completed HKL test, and “severed pathway” sits next to the official *severed* flag. A reviewer can say you ran the test on the Yangtze, or assigned the flag there.
- **Suggested wording (opening and the paddlefish clause only; keep the cited findings).** “Cross-basin analog (outside this example’s boundary). Published Yangtze cases are useful comparisons, not a completed HKL test of the Keokuk case.” … “The Chinese paddlefish, for which no captive population was ever established, lost reproduction first and was later declared extinct — the endpoint when a blocked migratory pathway has no substitute. [35]”

### B4. Ordinary-language “severed” in §8 item 5 — medium (same word-collision as B3)

- **File.** Same example on `main`, line 157.
- **Quote.** “whose access can be severed independently.”
- **Why it matters.** After B1, a reviewer will search the word. Line 40 (“If that link is severed”) has the same issue; both are ordinary language, not the flag.
- **Suggested wording.** “whose access can be blocked independently.” (And at line 40, “If that host-fish link is broken.”)

### B5. Conclusion “shows that especially clearly” — medium

- **File.** Same example on `main`, line 164.
- **Quote.** “The Keokuk–skipjack case shows that especially clearly.”
- **Why it matters.** The header already says this is not an empirical validation or HKL score. “Shows that especially clearly,” right after a claim about losing autonomous renewal, is stronger than the computed record (none).
- **Suggested wording.** “The Keokuk–skipjack record, as cited here, is a clear historical illustration of that distinction; it is not a computed HKL score.”

### B6. Unmarked withdrawn wording in the Sahel addendum on `main` — medium

- **File.** `Release/Examples/sahel-logistic-addendum-section9-draft.md` on `main`, e.g. lines 105, 187–188 (sign-flip as an “empirical anchor” / “falsification anchor”).
- **Why it matters.** The current Sahel paper on `main` already withdraws the completed sign-change and “passed falsification” claims. This file is already statused as an unpromoted source in `Release/Examples/README.md`. A reviewer who opens the addendum first can miss that.
- **Suggested wording.** Add a short status banner: unpromoted source; current Sahel §5 withdraws the completed sign-change and “passed” wording; those passages are historical. This branch already has such a mark; it is not on `main`.

### B7. Unmarked stale wording in Working drafts on `main` — medium

- **Files on `main`.** `Release/Working/absorbic-effort-framework-v2.md` §6 “ELQ Triangle” (lines 154–164: “a single phenomenon described in three namespaces”); `Release/Working/hkl-lyapunov-v2.md` lines 87 and 107 (stability / Lyapunov condition treated as requiring \(dV/dt\le 0\)); `Release/Working/buffer-as-temporal-dimension.md` line 263 (AU “currently has” a thermodynamic-analog definition).
- **Why it matters.** `Release/ARCHITECTURE.md` and the 16 October record already say Working drafts do not override current definitions. A reviewer can still quote an unmarked draft as current.
- **Suggested wording.** A status banner at the top of each draft pointing at the current HKL and AEF papers, and in-place stale marks at those passages. This branch already has those marks; they are not on `main`.

---

## C. Decisions pending

These are not wording errors. They wait on you.

1. **Official Central Valley / San Joaquin Valley Bite 5 boundary.** Still open. Round 13 used Bulletin 118 subbasin 5-022.12 as a locked official unit and got n=0 qualifying wells in that extract. ARM-05 in `ai/THEORY_MAB.md` is `wait`, not explore, until official series and predeclarations are actually in hand.
2. **Whether to keep or archive accepted `ai/PROPOSALS/`.** The cycle currently leaves accepted proposal records in place. You can leave them, or ask for a later tidy into an archive folder. Not required for the premise.
3. **Whether to ratify the branch process aids** (computed-status procedure, application-quantity inheritance labels, object-class declaration, four-field recording sheet). They are ratification-pending `ai/` notes, consistent with official papers, but not Registry vocabulary unless you adopt them (see A8).
4. **What to do with experimental `src/`.** It is now clearly labeled unofficial, and the invented 0.1 / +0.5 / 0.4-0.3-0.3 numbers no longer compute. You can leave it as a marked exhibit, or later replace it with an implementation against Registry v0.3.2. No official scorer should be built until A2–A4 are decided.
5. **Whether to copy the branch marks in B6–B7 onto `main` yourself.** Agents will not write to `main`.

---

## D. Closed this round (Round 19)

- Re-pulled `main`. It moved only in the mussel example: commit `270942c` (23 November 2026, 5:07 PM America/New_York), §8 item 4 now names Lock and Dam 22 near Saverton. Official papers, Registry, and decision records are still identical on both branches.
- Branch §8 item 4 adopted the published `main` sentence. The earlier branch wording of item 4, and the part of the Session 3 note that was only correcting that typo, are marked superseded. The LD19 / uADS retrieval remains as unpublished branch work.
- `CorePrinciples/SLP_Published.md` now has a historical-source banner; body preserved.
- Diverging and branch-only `Release/` markdown and scripts on this branch now carry an “unpublished vs `main`” banner. Folder-level `UNPUBLISHED.md` notices were added for branch-only data files (CSV, JSON, source excerpts) and beside the freshwater dictionary CSV, because a markdown banner would break those formats. `main` was not edited.
- Experimental `src/`: unofficial SRI / HRS / HKL-AI *names* are documented; the hardcoded 0.1 distill scaling, +0.5 connection increment, and 0.4/0.3/0.3 HKL-AI weighting no longer run. No replacement official metrics were invented.
- Overreach audit of `Release/` on `main` completed; findings that only you can fix are in §B. Official HKL and AEF papers are already hedged (“Law” names the research program; a publication checkpoint is not empirical validation).
- This file. No theory arm was developed.

---

**What should be left after you finish A and B.** Terms you have defined, retired, or explicitly left unofficial; official example wording on `main` that no longer contradicts the 30 October record; and the pending decisions in §C, which do not have to be resolved before a reviewer can be shown the official papers.
