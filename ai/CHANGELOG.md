# AI-branch changelog

This log records changes on `ai/evolution` only. It is not the repository
publication changelog (`CHANGELOG.md` on `main`). An entry here is not a
publication to `main` and is not scientific validation.







## Session 1 summary (2026-11-21)

This session ran Rounds 2–6 on `ai/evolution` only, after Round 1, as
direct `[A]` / `[B]` / `[C]` commits. No pull requests. `main` was not
modified. Nothing was moved to `ai/REJECTED/`. No empirical series,
field \(\eta_{TM}\), \(V_W\), or Sahel burden score was computed or
invented. Official papers were not rewritten.

### What moved

- **Round 1 (already on the branch before this five-run):** freshwater
  Bite 1 schema-only data dictionary, accepted-with-revisions.
- **Round 2 — Layer 1 / implementation consistency audit.**
  `accept-with-revisions`. Dated audit at
  `ai/AUDITS/2026-11-21-layer1-consistency.md` and a status notice at
  `src/README.md`. C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/e69a892ba7792140ee275d0f5158bf2d3c67311a
- **Round 3 — Ebonyshell renewal-coverage protocol.**
  `accept-with-revisions`. Blank preregistration sheet at
  `Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md`.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/d71a7ebb3f8c34840d631205df43e40d74617288
- **Round 4 — HKL Bite 5 falsification checklist.**
  `accept-with-revisions`. Blank score sheet at
  `Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md`.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/b3c67662f81f6d5af55ccc6a8431eca0fbc8349b
- **Round 5 — Sahel bounded test plan.**
  `accept-with-revisions`. Blank six-step plan at
  `Release/Examples/sahel_bounded_test_plan_v0.1.md`. Withdrawn §5
  wording was not restored. C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/dbb11e9f0432bda886e53c086f2e091d7b47dcd7
- **Round 6 — Application-quantity inheritance firewall.**
  `accept-with-revisions`. Ratification-pending branch note at
  `ai/NOTES/application-quantity-inheritance-v0.1.md`. C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/8352550bfab6366518f4e9ffd52df59a50f3497d

### What was rejected

No proposal in this session was rejected or filed under `ai/REJECTED/`.
Every later-round verdict was `accept-with-revisions`, except some
individual claims accepted as written. Negative scientific results were
not produced, because no empirical test was run.

### Errors B found in the original human corpus

These are in-tree issues, not defects invented by A:

1. **Experimental PAE helper.** `src/IIF_Evaluator.py` `_apply_pae`
   subtracts a term built from an `effort` argument from an error score.
   That treats expenditure as successful correction, which the 16 October
   record and current AEF paper reject. The root README already lists
   `src/` as experimental. A status notice was added; function bodies
   were not patched.
2. **Import names and random scores.** `from giln_ai import …` and
   `from iif_evaluator import …` do not match `GILN_AI.py` /
   `IIF_Evaluator.py`. On Linux those lowercase imports raised
   `ModuleNotFoundError`. Several `_score_*` methods return
   `np.random.uniform(0.5, 1.0)` and cannot be evidence for the
   framework.
3. **Unpromoted Sahel logistic addendum.** It still uses the withdrawn
   “measurably flipped sign” wording as an empirical / falsification
   anchor. It cites “Sahel §5.1” (an OIE integral) and “HKL §5.1” (a
   basin-maintenance margin \(M(t)\)) that the *current* Sahel and HKL
   papers do not contain; the margin formula resembles superseded
   `Release/Working/hkl-lyapunov-v2.md`. It treats PAE as a number in
   \(\lambda_{PAE}(t)\,PAE(t)\). The addendum was already labeled
   unpromoted; its body was not edited in this session.
4. **Mussel worked example §8.** The example says ebonyshell natural
   renewal coverage above Keokuk after 1913 is “effectively zero … so
   the population carries the registry’s *severed* flag,” while the
   30 October remaining-work list says no field \(\eta_{TM}\) has been
   computed. That is an uncomputed status assignment in the original
   example. The new protocol refuses to treat it as a measured ratio
   and does not rewrite the example body.

Current official AEF, HKL, and Sahel *papers* were not found to be
internally inconsistent with the 16 / 30 October records on the points
checked.

### Open questions

- Official Central Valley / San Joaquin boundary IDs, hydrologic year,
  time interval, and retrieved source versions (Round 1 residuals)
  still need evidence before Bite 5 can be scored.
- Ebonyshell \(\eta_{TM}\) above and below Keokuk, and the Keokuk fish-
  passage test, remain unfilled; construction status as of October 2026
  was already recorded as unconfirmed.
- The Sahel six-step plan remains blank: locations, sources, series,
  and a locked held-out score are still `needs-evidence`.
- Whether Jordan wants the mussel example’s qualitative severed sentence
  reworded, or a banner on the logistic addendum, is left to him.
- Whether to repair `src/` imports and `_apply_pae` is later work.
- The inheritance-firewall status words are ratification-pending and
  must not be treated as official registry vocabulary unless he adopts
  them.
- After Round 1, Jordan deleted
  `ai/PROPOSALS/2026-11-21-freshwater-data-dictionary/` with the message
  “New rule verified.” Later rounds still opened proposals under
  `ai/PROPOSALS/` as `CYCLE.md` requires. He may want to confirm whether
  accepted proposal files should be removed after the verdict.


## 2026-11-21 — Round 6: application-quantity inheritance firewall (accept-with-revisions)

Branch-local note at `ai/NOTES/application-quantity-inheritance-v0.1.md`.
No registry amendment and no computed quantities. The unpromoted
addendum’s “HKL §5.1” margin remains ineligible; freshwater reuse of
\(\eta_{TM}\) and reuse of the corrective-dependency screen remain
needs-mapping. Challenges that hit: mark the new status words
ratification-pending; warn that “eligible” is not validation; say
explicitly that needs-mapping is not a license to fill freshwater
\(\eta\) in this cycle.


## 2026-11-21 — Round 5: Sahel bounded test plan (accept-with-revisions)

Blank six-step plan at `Release/Examples/sahel_bounded_test_plan_v0.1.md`.
Withdrawn Sahel §5 wording was not restored; the unpromoted logistic
addendum is not used as authority; no series were computed. Challenges
that hit: lock the local-regulation variable list before step 5; declare
comparability dimensions; allow retrieval of primaries the current paper
already points to. The current Sahel paper body was not edited.


## 2026-11-21 — Round 4: HKL Bite 5 falsification checklist (accept-with-revisions)

Blank score sheet at
`Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md`.
No weights or \(V_W\) were computed. All three challenges hit: the
comparison metric is now required to be a held-out score on the
protocol’s named outcomes; the sheet records whether a condition fired
instead of inventing a weaken-versus-reject split; and the hard-threshold
list must be locked before use. Round 1 official-boundary residuals
remain open.


## 2026-11-21 — Round 3: ebonyshell renewal-coverage protocol (accept-with-revisions)

Preregistration sheet at
`Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md`.
No rates, ratios, or statuses were computed. Challenges that hit:
life stage and loss components were not locked before data arrive;
inclusion of the 1986 episode in the \(\eta^{nat}_{TM}\) numerator was
unspecified. Both were fixed. The above/below contrast is not the
registry’s sink-impairment counterfactual (challenge missed; disclaimer
added). The original worked example’s qualitative “effectively zero /
severed” assignment remains an uncomputed status in the standing corpus
and was recorded, not rewritten.


## 2026-11-21 — Round 2: Layer 1 / implementation consistency audit (accept-with-revisions)

Dated audit at `ai/AUDITS/2026-11-21-layer1-consistency.md`. Official AEF,
HKL, and current Sahel papers were not edited and are not the defective
objects. Findings that held: experimental `_apply_pae` treats expenditure
as correction; `giln_ai` / `iif_evaluator` imports fail on Linux; several
IIF scores are random; the unpromoted Sahel logistic addendum still uses
withdrawn sign-change wording as an anchor. Challenge
`CH-layer1-consistency-03-stale-section-citations` hit: the same addendum
cites “Sahel §5.1” and “HKL §5.1” formulas the current papers do not
contain, and treats PAE as a number. Finding F5 and `src/README.md` (status
notice only) were added. Other challenges missed.


## 2026-11-21 — Round 1 accepted with revisions (freshwater data dictionary schema)

- Work agent proposed a schema-only Central Valley / Temporal Mining Bite 1
  data dictionary, without invented measurements.
- Adversarial hits on missing §4 separations (`dG_W_obs`, streamflow
  capture), undefined `tau_d`, a misleading deliverable path, and blank
  §13 source classes were addressed in the verifier commit.
- Verdict: `accept-with-revisions`. See
  `ai/LEDGER/verdicts/V-2026-11-21-freshwater-data-dictionary.md`.
- Official boundaries, time interval, and retrieved source versions remain
  unfilled. This is not a publication to `main` and not empirical
  validation.

## 2026-11-21 — Cycle changed to direct commits on `ai/evolution`

- Jordan's cardinal rule: work only on `ai/evolution`, by direct commit.
  No pull requests, no other branches, never `main`.
- Updated `ai/AGENTS/CYCLE.md`, the three agent files, `ai/README.md`, and
  the process / ownership section of `ai/CHARTER.md`. Layer 0 of the
  charter is unchanged. This process amendment was directed by Jordan.
- Cycle is now: A commits a proposal and claims with status `proposed`
  (`[A]`); B commits challenges (`[B]`); C commits the verdict (`[C]`)
  and either promotes the proposal or moves it to `ai/REJECTED/`.
- One commit per role step. Every action still appends `ai/TRAIL.md` and
  every proposal, challenge, and verdict file still opens with a
  plain-English TL;DR.

## 2026-11-21 — Branch README, license notice, and human trail

- Rewrote `ai/README.md` as the labeled AI-evolution branch orientation
  (what the branch is, AI authorship under the charter, not validated
  science, not human-owned `main`, how the three agents work, where to
  start).
- Added a short banner at the top of the root `README.md` on this branch
  only; the rest of that file is unchanged.
- Recorded the repository's GNU Affero General Public License, version 3,
  from `License.md` (Harmonic Knowledge Law (HKL) by Jordan LeDuc; version 3
  or, at the licensee's option, any later version; no warranty), and stated
  that AI-branch content is under the same license.
- Added a commercial licensing contact section pointing at GitHub
  [@Causal5](https://github.com/Causal5), with email marked as not yet
  provided.
- Added `ai/TRAIL.md` as the chronological human landmark log.
- Required every agent action to append a trail entry, and every proposal,
  challenge, and verdict file to open with a plain-English TL;DR
  (`ai/AGENTS/CYCLE.md` and the three agent files).
- No theory, example, or corpus changes beyond these operating-layer and
  banner edits. `main` was not changed.

## 2026-11-21 — Scaffold created

- Added the AI-evolution charter, agent rule files, cycle description, empty
  ledger, and orientation README.
- No theory, example, or code changes to the existing corpus.
- Pinned starting snapshot: `c9e12778aba0014732a8add3c90c5676e5785bf7`.
