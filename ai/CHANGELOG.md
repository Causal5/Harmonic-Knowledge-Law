# AI-branch changelog

This log records changes on `ai/evolution` only. It is not the repository
publication changelog (`CHANGELOG.md` on `main`). An entry here is not a
publication to `main` and is not scientific validation.







## 2026-11-21 — Round 15: Niger WDI/FAOSTAT cereal-yield precursor

Worked example with a retrieved official interannual series.
`accept-with-revisions`. WDI indicator AG.YLD.CREL.KG for Niger, sourced
from FAOSTAT QCL, 1961–2022: 62 numeric years, 61 distinct values, mean
423.82 kg/ha, minimum 257.1 kg/ha in 1984, maximum 599.3 kg/ha in 1964.
The indicator was chosen after Round 14 showed the official precipitation
indicator is not interannual; that choice stays declared. Yield is not
rainfall, not an FMNR result, and not \(V\). CHIRPS was not retrieved.
The verifier re-ran the script and checked that the API resolves.
C commit: this commit.
Fill: `Release/Examples/sahel/worked-fills/2026-11-21-niger-cereal-yield-wb/`.
Verdict: `ai/LEDGER/verdicts/V-2026-11-21-niger-cereal-yield.md`.

## 2026-11-21 — Round 14: Niger WDI/FAOSTAT precipitation precursor

Worked example with a retrieved official series. `accept-with-revisions`.
World Bank WDI indicator AG.LND.PRCP.MM for Niger, sourced from
FAOSTAT, is 151.0 mm per year in every year of the locked 1961–2022
window — a long-term national average, not an interannual rainfall
series, and not a site or southern-Sahel climatology. No \(V\) was
constructed; withdrawn Sahel claims were not restored; comparable
locations remain UNFILLED-REQUIRED. CHIRPS was not retrieved. The
verifier re-ran the script and checked that the API resolves.
C commit: this commit.
Fill: `Release/Examples/sahel/worked-fills/2026-11-21-niger-precip-wb/`.
Verdict: `ai/LEDGER/verdicts/V-2026-11-21-niger-precip-wb.md`.

## 2026-11-21 — Round 13: Tulare Lake 5-022.12 DTW contrast and retrieved CVHM2 figures

Worked example with retrieved public records. `accept-with-revisions`.
Official DWR Bulletin 118 subbasin 5-022.12 (San Joaquin Valley–Tulare
Lake, 837.356 sq mi) was locked from a live FeatureServer GeoJSON.
A predeclared USGS 72019 spring 2015 vs spring 2024 contrast yields
n=0 qualifying wells (one in-polygon 2015 measurement; zero in 2024).
That is a coverage result in this API extract, not a finding of no
water-level change; DWR/CASGEM series were not retrieved. The USGS
Publications Warehouse abstract of Faunt et al. (2024) was retrieved
and quotes approximately 158 km³ of Central Valley storage loss from
pre-development to 2019, about 15% permanent — abstract-only, not
recomputed, not a 5-022.12 2015–2024 result. Bite 5 and V_W were not
scored. The verifier re-ran the script and checked that the pubs page
and FeatureServer query resolve.
C commit: this commit.
Fill: `Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/`.
Verdict: `ai/LEDGER/verdicts/V-2026-11-21-tulare-lake-dtw.md`.

## 2026-11-21 — Round 12: Keokuk / Lock 19 official status and USGS 05474500 discharge

Worked example with retrieved public records, not a blank template.
`accept-with-revisions`. Citation [38] locates the first-of-its-kind
fish passage at Lock and Dam 22 near Saverton, Missouri, not at
Keokuk. Official USACE (Wayback 24 January 2025 of a page published
30 August 2024; live URL HTTP 403 on 21 November 2026) and ICRCC
FY2026 records describe a uADS carp deterrent at Lock and Dam 19
(River Mile 364.2 in the snapshot; experimental operation through
2026 in the live ICRCC plan). Discharge at USGS 05474500 for locked
USGS water years 2016–2025: 3,652/3,653 days, period mean 100,725
ft³/s including 39 estimated days and 100,548 ft³/s excluding them;
one missing day (2022-08-31). The modern OGC daily API was missing
923 of those days; values agreed on all overlapping days. NWIS DV
was adopted as primary after those gaps were seen. Discharge is
hydrologic context only; \(\eta\) and the *severed* flag were not
assigned. A logged Session 3 note was added to mussel example §8
item 4. Verifier re-ran the script and checked that cited sources
resolve.
C commit: this commit.
Fill: `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/`.
Verdict: `ai/LEDGER/verdicts/V-2026-11-21-keokuk-ld19-status.md`.

## Session 2 summary (2026-11-21)

This session ran Round 7 (the four Session 1 corpus corrections, through
a full A/B/C cycle so B and C could check the fixes) and Rounds 8–11
on `ai/evolution` only, as direct `[A]` / `[B]` / `[C]` commits. No
pull requests. `main` was not modified. Nothing was moved to
`ai/REJECTED/`. No empirical series, field \(\eta_{TM}\), \(V\), or
Sahel burden score was computed or invented. Official AEF, HKL, and
Sahel papers were not rewritten.

### What moved

- **Round 7 — Session 2 corpus corrections.**
  `accept-with-revisions`. Expenditure is recorded separately from
  correction in `_apply_pae`; `src/` imports run on case-sensitive
  Linux; `np.random` placeholder scores return `None`; the unpromoted
  Sahel addendum has a status banner and in-place dead-cite marks;
  mussel example §8 item 3 no longer assigns the *severed* flag from a
  qualitative line. Verifier also fixed leftover invented scores,
  `CorePrinciples/Law_of_We_Full.md` random placeholders, an unmarked
  AEF §3.2 body cite, and a stale protocol quote. Scripts were run on
  this Linux box. C commits:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/19a78bc05ba32b23aa88a92d70798ca69eb40650
  and
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/e21b554192949b4164292c417c9cc10de8afcc05
- **Round 8 — Computed-status assignment procedure.**
  `accept-with-revisions`. Ratification-pending note at
  `ai/NOTES/computed-status-assignment-v0.1.md`. A registry flag
  defined by a computed quantity may not be assigned from a qualitative
  narrative; the protocol must be locked before inspection. C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/ab7a52d5f3d8dff64f706cb88c5626f77a48fbb6
- **Round 9 — Object-class declaration sheet.**
  `accept-with-revisions`. Blank proposed aid at
  `ai/NOTES/object-class-declaration-sheet-v0.1.md`. Later fills may
  label each symbol as reality, state, observation, or model. C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/9e1f1ff30a925f8544b7dc79fdd1816a1415862f
- **Round 10 — Working-draft dead-cite marks.**
  `accept-with-revisions`. Banners and in-place marks on
  `Release/Working/absorbic-effort-framework-v2.md` and
  `Release/Working/buffer-as-temporal-dimension.md`. C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/316e6f8c50f832cf4381e97347c2bd067ae3cd0f
- **Round 11 — Four-field effort declaration sheet.**
  `accept-with-revisions`. Blank proposed aid at
  `ai/NOTES/four-field-effort-recording-sheet-v0.1.md`. Allocation,
  expenditure, achieved correction, and side burden stay separate.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/251885052e483a57dde13bb958f4ae7fa7455d7c

### What was rejected

No proposal in this session was rejected or filed under `ai/REJECTED/`.
Every later-round verdict was `accept-with-revisions`, except some
individual claims accepted as written. Negative scientific results were
not produced, because no empirical test was run.

### Errors B found in the original human corpus

These are in-tree issues, not defects invented by A. Several were
fixed in this session; residuals are noted.

1. **`CorePrinciples/Law_of_We_Full.md`.** Still used
   `np.random.uniform` to invent an OIE-impact score and a
   decision-balance score. Round 7 C replaced those two returns with
   `None`.
2. **Ebonyshell protocol §1.** After the mussel example’s *severed*
   assignment was reworded, the protocol still quoted the old “so the
   population carries the registry’s *severed* flag” sentence as
   current. Round 7 C marked that wording superseded.
3. **Unpromoted Sahel logistic addendum.** Most dead cites were marked
   in Round 7 A, but a body sentence still cited “AEF §3.2, §5”
   unmarked. Round 7 C marked it. No replacement section was invented.
4. **Experimental `src/` leftovers.** After the `np.random` removal,
   `_score_reasoning` still returned a connection-count number, and
   Libra still invented EGR, GDS, and an entropy score. Round 7 C set
   those to `None`. `GILN_AI.py` still scales hardcoded
   `resource_metrics` by 0.1 on “distill” and still adds `+0.5` to
   connection weights (residual, not treated as a failed claim).
5. **Working drafts (new this session).**
   `Release/Working/absorbic-effort-framework-v2.md` and
   `Release/Working/buffer-as-temporal-dimension.md` cited “HKL §5.1,”
   “HKL §4.1,” “Sahel §5.3,” “AEF §3.2 / §3.3,” and a “Sahel §6
   demonstrates this formalism” line that current papers do not
   support. The buffer draft treated \(dV/dt \le 0\) as a necessary
   HKL condition; current HKL §4 says that is not a universal
   necessary condition, and §7 withdraws necessary-monotonic-drift
   wording. AEF v2 types PAE as a number, which current AEF §2
   rejects. Round 10 marked these in place and did not rewrite the
   official papers.

Current official AEF, HKL, and Sahel *papers* were not found to be
internally inconsistent with the 16 / 30 October records on the points
checked in this session, beyond what Session 1 already recorded.

### Open questions

- Official Central Valley / San Joaquin boundary IDs, hydrologic year,
  time interval, and retrieved source versions still need evidence
  before Bite 5 can be scored.
- Ebonyshell \(\eta_{TM}\) above and below Keokuk, and the Keokuk
  fish-passage test, remain unfilled; construction status as of
  October 2026 was already recorded as unconfirmed.
- The Sahel six-step plan remains blank: locations, sources, series,
  and a locked held-out score are still `needs-evidence`.
- The inheritance-firewall status words, the computed-status
  procedure, the object-class sheet, and the four-field declaration
  sheet are all ratification-pending. They must not be treated as
  official registry vocabulary or as required cycle steps unless
  Jordan adopts them.
- After Round 1, Jordan deleted
  `ai/PROPOSALS/2026-11-21-freshwater-data-dictionary/` with the
  message “New rule verified.” Later rounds still opened proposals
  under `ai/PROPOSALS/` as `CYCLE.md` requires. He may want to confirm
  whether accepted proposal files should be removed after the verdict.
- A leftover side branch
  `ai/proposal/2026-11-21-freshwater-data-dictionary` still exists
  (there is no delete-branch tool on this path). `main` is still
  unprotected. Commercial contact remains GitHub @Causal5 only; no
  email was invented.
- Cycle.md prefers one commit per role. Several steps in this session
  landed as a pair of commits because a single push may carry at most
  four large file substitutions.

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


## 2026-11-21 — Round 11: four-field effort declaration sheet (accept-with-revisions)

Blank ratification-pending aid at
`ai/NOTES/four-field-effort-recording-sheet-v0.1.md`. Allocation,
expenditure, achieved correction, and side burden stay separate. No
rows were filled. Challenges that hit: the heading must not sound like
measured data; the four names point at the 16 October / AEF §2
definitions; non-correction rows use N/A rather than invent a
correction.

C commit lands with this entry.

## 2026-11-21 — Round 10: Working-draft dead-cite marks (accept-with-revisions)

Status banners and in-place marks on
`Release/Working/absorbic-effort-framework-v2.md` and
`Release/Working/buffer-as-temporal-dimension.md`. Dead section numbers
and withdrawn necessary-dV/dt ≤ 0 wording, plus leftover PAE-as-number
lines, are marked against current HKL §4 / §7 and AEF §2. Official
papers were not rewritten. No replacement sections or formulas were
invented.

C commit: https://github.com/Causal5/Harmonic-Knowledge-Law/commit/316e6f8c50f832cf4381e97347c2bd067ae3cd0f

## 2026-11-21 — Round 9: object-class declaration sheet (accept-with-revisions)

Blank ratification-pending sheet at
`ai/NOTES/object-class-declaration-sheet-v0.1.md`. Later fills may
label each symbol as reality, state, observation, or model, and as
computed or qualitative. No rows were filled. Challenges that hit:
the sheet is a proposed aid, not a required cycle step; one row per
use; effort-related rows must separate expenditure from correction.

C commit lands with this entry.

## 2026-11-21 — Round 8: computed-status assignment procedure (accept-with-revisions)

Branch-local, ratification-pending note at
`ai/NOTES/computed-status-assignment-v0.1.md`. A registry flag defined
by a computed quantity may not be assigned from a qualitative
narrative. No quantities were computed. Challenges that hit: the
heading must not read as adopted official vocabulary; ordinary-language
uses of the same word are out of scope; the protocol must be locked
before the series are inspected.

C commit lands with this entry.

## 2026-11-21 — Round 7: Session 2 corpus corrections (accept-with-revisions)

Patched `_apply_pae` so expenditure is recorded separately from
correction; fixed `src/` imports for case-sensitive Linux and replaced
`np.random` placeholder scores with `None`; added a status banner and
in-place dead-cite marks to the unpromoted Sahel logistic addendum;
reworded mussel example §8 item 3 as qualitative/provisional, citing
the 30 October record. Verifier revisions: leftover invented scores in
`_score_reasoning` and Libra; `np.random` placeholders in
`CorePrinciples/Law_of_We_Full.md`; unmarked AEF §3.2 body cite; stale
“so … severed” quote in the ebonyshell protocol. Scripts were run on
this Linux box. No η or Sahel series was invented.

C commit lands with this entry.

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
