# AI-branch changelog

This log records changes on `ai/evolution` only. It is not the repository
publication changelog (`CHANGELOG.md` on `main`). An entry here is not a
publication to `main` and is not scientific validation.




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
