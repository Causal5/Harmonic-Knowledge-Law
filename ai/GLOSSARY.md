# Terminology map and erratum (Round 17)

**TL;DR.** This file is a map, not a new glossary of invented meanings. It lines up current official wording in `Release/` as published on `main` (Registry v0.3.2, the 16 and 30 October decision records, and the reconciled HKL and AEF papers) with stale or drifted wording still sitting in working drafts, recovered CorePrinciples files, and earlier cycle notes. Where a draft still talks as if \(dV/dt\le 0\) were required, or treats PAE as a number, or uses *severed* as a qualitative label, this map points at the current source and, for working drafts and `ai/` / CorePrinciples historical files, at the in-place mark or banner added in this cycle. Official Layer 0 and Layer 1 papers are not rewritten. If a term has no definition in those official sources, it is flagged `needs-definition` — nothing is made up to fill the gap.

**Status:** `accepted-with-revisions` (Round 17) as amended in Round 18 (23 November 2026, America/New_York) for source precedence. Ratification-pending branch note on `ai/evolution`. This is not a registry amendment, not a new official vocabulary, and not a base-theory move. Canonical citations are to `Release/` on `main`. No arm is registered or developed in `ai/THEORY_MAB.md` for this cycle.

**Authority (Round 18 source precedence).**

1. Layer 0 as quoted in `ai/CHARTER.md`, including Jordan’s 23 November 2026 rule: `Release/` as published on `main` is the primary and most up-to-date source; everything else is subject to obsolescence; `Release/` on `main` wins conflicts.
2. Current official wording *inside* that tree: Registry v0.3.2, the 16 and 30 October decision records, and the reconciled papers (`Release/HKL/hkl-lyapunov.md`, `Release/Papers/absorbic-effort-framework.md`, Worldline, Extension). `START_HERE.md` is a root introduction (not under `Release/`); where it restates those distinctions it is cited only as a pointer, not as a higher source.
3. This map, `Release/Working/`, `CorePrinciples/`, `src/`, `ai/` notes, and any `Release/` path that exists only on this branch, or that differs from the same path on `main`. When wording conflicts, (1) then (2) win. A branch edit under `Release/` is not a publication to `main`.

**How this file was built.** Previously logged term issues in `ai/LEDGER/` challenges and verdicts and in `ai/CHANGELOG.md` were listed first. The corpus was then searched for further instances of those patterns and for obvious relatives (PAE-as-number formulas, AU / ethical joule, HKL-AI Score, qualitative *severed*). Each entry cites a canonical source by file and section or line. No definition is written that is not already in those sources.

**What a “fix” is in this cycle.**

| Kind of file | Treatment |
|---|---|
| Layer 0 / official Layer 1 papers and the registry | Not rewritten. This map is the erratum / mapping pointer. |
| Working drafts under `Release/Working/` | Original wording kept; stale presentations marked in place (Round 10 marks extended; HKL v2 bannered and marked). |
| `CorePrinciples/` historical files (not the axiom text) | Original wording kept; a status banner points here. |
| Already-corrected examples, `src/_apply_pae`, mussel §8, Sahel addendum marks | Inventoried as already aligned; not re-edited. |

---

## A. Official terms (canonical wording only)

### A1. PAE — Principle of Absorbic Effort

- **Canonical.** Registry v0.3.2 §VI, concept-label row: “elective corrective effort by a capable agent to absorb, prevent, or locally reconcile destabilizing burden. Type: Principle; not a scalar or unit” (`Release/Registry/causal-ethics-master-symbol-registry.md` lines 162–163). Current AEF §2 (lines 22–28): “PAE is a principle and OIE is a process. Neither is a number.” 16 October record: “PAE remains a principle.” (`START_HERE.md` §4 restates this at the repo root; it is not the canonical file.)
- **Drift (do not treat as current).** Typing \(PAE\) as \(\mathbb{R}_{\ge 0}\); writing \(\lambda_{PAE}\cdot PAE\), \(PAE\ge OIE\), \(PAE=E-C_{pae}\), \(ELQ=PAE/\Delta S_{abs}\), or \(PAE<\Delta S_{abs}\); calling PAE a “cognitive mechanism” or energy-budget residual; using “ethical joule” language.
- **Fixes this cycle (old wording preserved, marked).**
  - `Release/Working/absorbic-effort-framework-v2.md` line 27 (already marked Round 10): \(PAE\) typed as \(\mathbb{R}_{\ge 0}\).
  - Same file lines 64–66 (already marked Round 10, with a blanket note for later products): \(\mathcal{F}_{PAE}=\lambda_{PAE}\cdot PAE\).
  - Same file lines 93–99: displayed \(PAE\ge OIE\) newly marked (current AEF §6 / Registry §VI: not a current accounting equation / conceptual shorthand only).
  - Same file lines 119–127: \(PAE=E-C_{pae}\) newly marked (current AEF §6 lists it among expressions that are not current accounting equations).
  - Same file line 144: \(PAE<\Delta S_{abs}\) newly marked. Line 47 marks the displayed \(ELQ=PAE/\Delta S_{abs}\) equation; line 81 marks “the Lyapunov condition (HKL §5, \(dV/dt\le 0\)) is satisfied when.”
- **Not invented here.** No replacement scalar formula for “PAE the number.”

### A2. OIE — Observer-Induced Entropy

- **Canonical.** Registry §VI line 163: “the causal process by which agentic action generates, transfers, or amplifies destabilizing burden across dependencies. Type: Process/category; not a scalar or automatically thermodynamic entropy.” Current AEF §2 lines 25–28. (`START_HERE.md` §4 restates this; not the canonical file.)
- **Drift.** Typing \(OIE\) as \(\mathbb{R}_{\ge 0}\); treating OIE as a field or entropy score; identifying OIE with thermodynamic entropy without a declared physical system; `CorePrinciples/Glossary.md` line 21 (“systemic disruption caused by actions that ignore the Law of ‘We’”).
- **Fixes this cycle.** AEF v2 symbol-table row, line 28, newly marked: OIE is a process, not a number. CorePrinciples glossary / Law of We banners cover the historical definitions.

### A3. Allocation, expenditure, achieved correction, and side burden

- **Canonical.** 16 October record: “Record allocation, expenditure, achieved correction, and side burden separately.” Current AEF §2 lines 37–43; Registry §VI measured-quantity table (lines 176–184): \(\mathcal{Q}^{nom}_{PAE}\) planned allocation; \(E_{PAE}\) / \(\dot E_{PAE}\) expended effort; \(\dot B^{land}_{PAE,k}\) achieved corrective burden-reduction rate; agent-induced side burden belongs in the OIE term (AEF §5). (`START_HERE.md` §4 restates “Measure resources spent separately from correction achieved”; not the canonical file.)
- **Drift.** Treating spent effort as successful correction; subtracting an `effort` argument from an error score (`_apply_pae` before Round 7).
- **Already fixed, not re-edited.** `src/IIF_Evaluator.py` `_apply_pae` (approx. lines 71–87) now records expenditure separately from achieved correction; four-field sheet `ai/NOTES/four-field-effort-recording-sheet-v0.1.md` points at these four records. This map restates the official four-way split; it does not invent informal meanings.

### A4. \(\dot V\le 0\) is not a universal necessary condition

- **Canonical.** 16 October record: “Nonpositive drift is a restricted sufficient scalar check, not a universal necessity or convergence proof.” Current HKL §4 (`Release/HKL/hkl-lyapunov.md` lines 83–84): “\(\dot V\le 0\) is not a universal necessary condition for viability.” §7 (line 139) withdraws necessary-monotonic-drift wording. (`START_HERE.md` §3 restates compatibility of temporary burden growth with remaining margin; not the canonical file.)
- **Drift.** “The Lyapunov condition \(dV/dt\le 0\)” as a required basin condition; “\(dV/dt\le 0\) (HKL §5) is necessary”; requiring \(dV/dt\le 0\) across \(\tau_{buffer}\).
- **Fixes this cycle.**
  - `Release/Working/hkl-lyapunov-v2.md`: new status banner (line 3) and in-place marks at line 100 (“Stability requires $\frac{dV}{dt}\le 0$”) and line 116 (“the Lyapunov condition $\frac{dV}{dt}\le 0$ requires”).
  - Buffer draft: first and second sentences at line 235 already marked in Round 10 (`requires \(dV/dt\le 0\) across \(\tau_{buffer}\)` included). Banner date extended.
  - AEF v2 inheritance sentence (line 19) already marked Round 10; line 81 newly marks “the Lyapunov condition (HKL §5, \(dV/dt\le 0\)) is satisfied when.”

### A5. \(V^*\), \(V_{PCB}\), and \(V_{max}\) are different objects

- **Canonical.** 16 October record and current HKL §3; Registry §V lines 129–131: \(V^*\) is a selected viable reference, not an exit boundary; \(V_{PCB}\) is the passive-counterfactual baseline (no universal identity \(V^*=V_{PCB}\), line 140); \(V_{max}\) is a declared scalar viability boundary.
- **Drift.** Equating a preferred target, a passive baseline, and a failure boundary.
- **Treatment.** Official papers already separate them. This map records the distinction. No Layer 1 rewrite.
- **Fixes this cycle.** `Release/Working/hkl-lyapunov-v2.md` line 154 marks the draft identity $V^*=V|_{\gamma=\gamma_{PCB}}$ as stale against current HKL §3 and the 16 October record.

### A6. ACR is coverage, not ethics or viability

- **Canonical.** Registry §VI lines 211–224 and AEF §4: ACR is matched achieved correction divided by attributed OIE burden. “\(\mathrm{ACR}\ge 1\) records coverage within this accounting model. It does not establish ethical legitimacy, overall viability, complete recovery, or non-externalization.” 16 October: replace current raw ELQ/AU accounting with defined, boundary-matched ACR.
- **Drift.** Inferring ethical legitimacy from \(ELQ=PAE/\Delta S_{abs}\) or from a raw effort/entropy ratio; treating ACR as a complete ethical or viability judgment.
- **Fixes this cycle.** AEF v2 ELQ symbol-table row, line 30, and the displayed equation at line 47, marked in A; §6 ELQ Triangle (lines 169–181) marked in C revisions. Legacy dispositions already in Registry lines 226–230. No new “ethical score” is defined here.

### A7. AU remains reserved and undefined

- **Canonical.** Registry §VI line 231: “\(AU\) — Reserved/undefined; no ‘ethical joule’ is established.” Current AEF §6 line 158: “AU remains reserved and undefined. No physical ‘ethical joule’ is established.” Release on `main` therefore resolves the *status* of AU (reserved/undefined). It does not supply a unit definition.
- **Drift.** “1 AU = 1 J / 1 \(\Delta S_{abs}\)”; “ethical joule analog”; AEF v2 §3.3 presenting a unit definition as current; buffer draft saying AU “currently has” that thermodynamic-analog definition.
- **Fixes this cycle.** AEF v2 symbol-table row line 31 and body lines 107–115 newly marked; buffer draft line 272 newly marked on the “currently has a definition” clause (the AEF §3.3 dead-cite was already present from Round 10).
- **Flag.** `needs-definition` as an official unit. This cycle does not define one.

### A8. The *severed* flag is a computed assignment

- **Canonical.** Registry §VII.1 line 327 (identical on `main`): the independent *severed* flag is “set when \(\eta^{nat}_{TM}=0\) apart from declared episodic events; occurs with *net mining* or *substituted*, never *covered*.” The 30 October record on `main` (`Release/Registry/definition-decisions-2026-10-30.md` line 306) states that no field \(\eta_{TM}\) has been computed for the mussel case. Renewal coverage is a screen, not a viability result (Registry line 330).
- **Published example on `main` (still current official example text).** In `Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md` on `main`, §8 item 3 (line 152) still says that natural renewal coverage “for ebonyshell above Keokuk after 1913 is effectively zero … so the population carries the registry’s *severed* flag.” That sentence conflicts with the 30 October record (also `Release/` on `main`). The record and Registry §VII.1 control the flag. The example sentence is not a computed assignment and is not treated as one.
- **Branch-only alignment, not a publication.** On `ai/evolution`, the same §8 item was rewritten (Round 7) so that the qualitative narrative does not assign the flag, and a protocol file not present on `main` was added. Those edits are unpublished branch work. They do not replace the `main` example.
- **Ordinary language, not the flag.** “If that link is severed” (example line 40 on both branches) describes a life-cycle / host-fish break. That is not the registry flag.
- **Rule of use (existing, not new, from Registry / 30 October on `main`).** Use *severed* as the registry flag only after \(\eta^{nat}_{TM}\) is computed on a locked protocol, or leave it unassigned. Do not promote ordinary-language “severed,” or the still-published `main` example sentence, to a computed status.

### A9. Renewal statuses: *net mining*, *substituted*, *covered*

- **Canonical.** Registry §VII.1 line 326, exclusive statuses on \(\eta^{tot}_{TM}\) and \(\eta^{nat}_{TM}\). Ratification-pending process labels from Rounds 6–9 (`ineligible`, `needs-mapping`, `eligible-as-application`) are **not** official registry vocabulary unless Jordan adopts those notes.
- **Treatment.** Map only; no new status words.

### A10. Buffer

- **Canonical.** Registry §VII and current HKL §6: \(\tau^\pi_{buf,\Omega}(t)\) is time to first exit from the viable region under a declared scenario; already outside ⇒ buffer is zero; a finite horizon with no exit is right-censored, not infinite buffer. 16 October record. Current HKL already has this definition; the Buffer *manuscript* is not promoted (16 October “Unadopted proposals”).
- **Drift.** Treating a reference as a failure threshold; conflating recovery time with exit time; presenting the unpromoted manuscript (including \(\mathcal{C}(t)\), \(J_{PAE}\) as a universal flux, “fresh water as plugin currency”) as current official buffer theory.
- **Treatment.** Working-draft banners already say the buffer addendum is not current HKL authority. Universal flux/coherence claims remain unpromoted. No new buffer primitive is defined here.

### A11. Withdrawn Sahel completion wording

- **Canonical.** 16 October record and publication notes on `main`, and current Sahel paper §5 (`Release/Examples/sahel_worked_example.md` line 78 on `main`): the claims that \(dV/dt\) “measurably flipped sign” and that the framework “passed” a falsification test are withdrawn as completed results.
- **Branch-only marks.** The status banner and in-place marks on `Release/Examples/sahel-logistic-addendum-section9-draft.md` exist on `ai/evolution` only. The addendum on `main` still uses that withdrawn wording without those marks. The current Sahel paper on `main` already records the withdrawal; the addendum is an unpromoted source and does not override it. This cycle does not restore the withdrawn claims.

### A12. Dead or stale section citations

These are citation errors, not new terms. Current papers do not contain the cited subsections. No replacement section numbers are invented.

| Drifted cite | Current paper fact | Where marked |
|---|---|---|
| “HKL §5.1” | Current HKL has no §5.1; §5 is “Effect accounting.” | AEF v2 line 19 (Round 10) |
| “HKL §4.1” | Current HKL has no §4.1; §4 is “Viability, drift, and stability.” | Buffer draft line 235 (Round 10) |
| “\(dV/dt\le 0\) (HKL §5) is necessary” | HKL §5 is Effect accounting; necessity withdrawn in §4 / §7 | Buffer draft line 235 (Round 10) |
| “Sahel §5.3” | Current Sahel has no §5.3; §5 withdraws completion claims | Buffer draft (Round 10) |
| “Sahel §6 demonstrates the buffer formalism” | Current Sahel §6 is a bounded test recipe | Buffer draft line 23 (Round 10) |
| “AEF §3.2” / “AEF §3.3” | Current AEF has no such headings | Buffer draft lines 239, 272 (Round 10) |

### A13. Reality, state, observation, and model are different objects

- **Canonical.** 16 October record (Release on `main`): \(x\) is realized state, \(m_i\) model, \(G_i\) substrate, \(S_\Phi\) conditioned ontic constraints. The same distinction is locked in the charter from `START_HERE.md` §1 (“Reality, a selected system state, an observation, and an agent's model are different objects”); that root file is not itself under `Release/`.
- **Treatment.** Map only. Official papers already state this.

### A14. A definition’s adoption is not empirical evidence

- **Canonical.** 16 October record (and CHARTER Layer 0): “A definition's adoption is a convention for this corpus, not empirical evidence that its associated hypothesis is true.”
- **Treatment.** Map only.

---

## B. Terms flagged `needs-definition`

Round 18 rechecked this list against `Release/` on `main` (official papers, Registry v0.3.2, 16/30 October records). None of these strings received a new official *definition* there. AU is explicitly reserved and undefined (status resolved, still no unit). Official buffer is already \(\tau^\pi_{buf,\Omega}\) (see A10); the manuscript primitives listed below remain unpromoted. The other rows remain `needs-definition`. These strings appear in historical or experimental files and have **no current official definition** in Registry v0.3.2 or the reconciled papers. This cycle does **not** invent definitions, formulas, thresholds, or units for them. They must not be used as if they were current official metrics. Adopting any of them later would be a base-theory move and must be gated through `ai/THEORY_MAB.md` and the cycle.

| Term | Where it appears | Official status |
|---|---|---|
| Absorbic Unit (AU) / “ethical joule” | AEF v2 §3.3; buffer draft line 272; older AEF archive | Explicitly reserved and undefined (A7). |
| *HKL-AI Score* (0–1; thresholds <0.3 “Critical Misalignment”, 0.6–0.8 “Alignment”; weights 0.4/0.3/0.3) | `CorePrinciples/Glossary.md` lines 15–17; `CorePrinciples/Law_of_We_Full.md` lines 20–21; `CorePrinciples/HKL_Water_Metric.md`; experimental `src/` | Not in Registry v0.3.2. `needs-definition`. DeepSeek “90% resource reduction” and scores 0.27→0.68 are not current official results. |
| *Systemic Resonance Index (SRI)* | `CorePrinciples/Glossary.md` line 27; `src/GILN_AI.py`, `src/giln_network.py` | Not in Registry v0.3.2. `needs-definition`. |
| *Harmonic Resonance Score (HRS)* | Glossary SRI entry; experimental `src/` | Not in Registry v0.3.2. `needs-definition`. |
| Axis (A) as a “universal constant” / one-dimensional equilibrium manifold | `CorePrinciples/Glossary.md` line 7; Law of We glossary; `CorePrinciples/CausalEthicsAxis.md` | Not in the current registry symbol tables. Historical wording is preserved under a banner. `needs-definition` as a current official symbol; this map does not promote or rewrite it. |
| Variation (\(\Delta\)) as geodesic distance from the Axis, and \(f(E)=kE\times(1+\text{impact})\), \(\Delta'=\Delta-f(E)\) | `CorePrinciples/Glossary.md` lines 23, 29 | Not in Registry v0.3.2. `needs-definition`. Do not identify this \(\Delta\) with HKL \(V\) or \(\Delta V\). |
| \(\mathcal{C}(t)\) (coherence functional), manuscript \(J_{PAE}\) / \(\rho_{regen}\) / \(\kappa_{coord}\) / \(\Omega_{var}\) as official primitives | `Release/Working/buffer-as-temporal-dimension.md` | Buffer manuscript’s universal flux/coherence claims are unpromoted (16 October record). `needs-definition` as official Layer 1 objects. Current official buffer is A10. |
| Process labels `ineligible` / `needs-mapping` / `eligible-as-application` | Round 6–9 notes | Ratification-pending; not registry vocabulary unless Jordan adopts them. |

---

## B1. Round 18 recheck against `Release/` on `main`

| Term | Result of recheck |
|---|---|
| AU / “ethical joule” | **Status resolved, still no definition.** Registry line 231 and AEF §6 line 158 on `main` reserve AU as undefined. Stays `needs-definition` as a unit. |
| *HKL-AI Score* and 0.3 / 0.6–0.8 thresholds | **Not in** official `Release/` papers or Registry v0.3.2 on `main`. Remains `needs-definition`. |
| SRI | Same. Remains `needs-definition`. |
| HRS | Same. Remains `needs-definition`. |
| Axis as a current official symbol | **Not in** official Registry symbol tables or reconciled papers on `main`. Remains `needs-definition` as an official symbol. Charter Layer 0 does not define it. |
| Variation (\(\Delta\)) formulas \(f(E)\), \(\Delta'=\Delta-f(E)\) | **Not in** official `Release/` papers on `main`. Remains `needs-definition`. Do not identify with HKL \(V\) or \(\Delta V\). |
| Buffer manuscript primitives \(\mathcal{C}(t)\), \(J_{PAE}\), \(\rho_{regen}\), \(\kappa_{coord}\), \(\Omega_{var}\) | Official buffer on `main` is already \(\tau^\pi_{buf,\Omega}\) (Registry §VII, HKL §6). Those manuscript primitives are not in the current Registry or HKL/AEF papers (the v0.4 draft, not promoted, only discusses migrating some of them). Remain `needs-definition` as official Layer 1 objects. |
| Process labels `ineligible` / `needs-mapping` / `eligible-as-application` | **Not in** Registry or decision records on `main`. Remain ratification-pending branch vocabulary. |

No new definitions were invented in this recheck.

## C. Inventory of files touched or explicitly left alone

**Marked or bannered in Round 17 (original wording preserved).**

- `Release/Working/hkl-lyapunov-v2.md` — first status banner; lines 100, 116, and 154 marks.
- `Release/Working/absorbic-effort-framework-v2.md` — leftover PAE-as-number / AU / ELQ / \(PAE=E-C_{pae}\) marks; banner date extended.
- `Release/Working/buffer-as-temporal-dimension.md` — AU “currently has a definition” clause marked; banner date extended.
- `Release/Working/README.md` — pointer to this file and to the HKL v2 marks.
- `CorePrinciples/Glossary.md`, `Law_of_We_Full.md`, and `CausalEthicsAxis.md` — historical-source banners from A. C revisions bannered `HKL_Water_Metric.md`, `HKL_Geometric_Intelligence_Updated.md`, and `Law_of_We_Causal_Ethics.md`. `CorePrinciples/Causal_Integrity_Axiom.md` is **not** edited (Layer 0 source). `SLP_Published.md` remains an unbannered historical source (residual).
- `ai/GLOSSARY.md` (this file), `ai/README.md` (visibility and reading-list pointers), root `README.md` banner on this branch only (the `ai/` tree is not on `main`), `ai/THEORY_MAB.md` (Round 17 is not an arm).

**Already aligned; not rewritten in this cycle.**

- Current Layer 1 papers and the registry (canonical sources).
- `Release/Examples/sahel_worked_example.md` §5 withdrawal; unpromoted logistic addendum marks (Round 7).
- Mussel example §8 item 3 and ebonyshell protocol §1 (Rounds 7–8, 12).
- `src/IIF_Evaluator._apply_pae` expenditure/correction split (Round 7).

**Known residual risk (not silently cleaned).**

- `CorePrinciples/SLP_Published.md` has no Round 17 banner; it is a historical SLP source, not current Registry authority.
- Experimental `src/` still contains *SRI* / *HRS* / *HKL-AI Score* function names and some hardcoded scalings noted in Session 2. Those are experimental code, not official metrics; this cycle does not invent replacement scores. `src/README.md` already describes experimental status.
- Ordinary-language “severed” in the mussel example (A8) is left in the official example body, with the mapping stated here rather than a Layer 1 rewrite.
- Historical reviews and audits (`Release/Reviews/`, `ai/AUDITS/`) describe past wording; they are records, not current definitions.

---

## D. Visibility of the `ai/` directory

Jordan reported not seeing “that dir.” The `ai/` tree — including `ai/THEORY_MAB.md`, `ai/PROPOSALS/`, and this file — exists on `ai/evolution` and does **not** exist on `main` (verified at `origin/main` = `c9e12778aba0014732a8add3c90c5676e5785bf7`). A GitHub view of `main` will not show it. On this branch:

- https://github.com/Causal5/Harmonic-Knowledge-Law/tree/ai/evolution/ai
- https://github.com/Causal5/Harmonic-Knowledge-Law/blob/ai/evolution/ai/THEORY_MAB.md
- https://github.com/Causal5/Harmonic-Knowledge-Law/tree/ai/evolution/ai/PROPOSALS
- https://github.com/Causal5/Harmonic-Knowledge-Law/blob/ai/evolution/ai/GLOSSARY.md

The branch-only banner on the root `README.md` and a short note in `ai/README.md` now say this explicitly.

---

## E. What this file does not do

- It does not amend Registry v0.3.1 / v0.3.2 or rewrite official papers.
- It does not restore withdrawn Sahel claims, assign *severed* or \(\eta\), construct \(V\), or score Bite 5.
- It does not invent definitions for any `needs-definition` term.
- It is not a fitted glossary that quietly replaces Layer 1. If a later cycle wants to *adopt* a currently undefined term, that is a theory move and must go through `ai/THEORY_MAB.md` first.
