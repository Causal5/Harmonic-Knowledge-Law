# AI-branch changelog

This log records changes on `ai/evolution` only. It is not the repository
publication changelog (`CHANGELOG.md` on `main`). An entry here is not a
publication to `main` and is not scientific validation.







## 2026-11-25 — Round 28: independent Tulare C_irr product search (indeterminate; accept-with-revisions)

Pre-registered a four-part qualification rule, then searched USGS extensometers, DWR/SGMA InSAR, CGPS and benchmark surveys, the Brandt et al. 1958–2018 data-release landing page, and OpenET. None of the seven products qualifies. Zero of 17 California NWIS extensometer wells fall inside 5-022.12. CGPS stations LEMA and CRCN are independent displacement records inside the subbasin, not a locked volume. OpenET is evapotranspiration. Shared InSAR / C-zone storage fails independence. The round is **indeterminate** (data / scope gap). ARM-07 stays `wait`. The signature stays unassigned. `main` was not edited.

## 2026-11-25 — Round 27: lag-justified Tulare DWR sign windows (breaks; accept-with-revisions)

Pre-registered one-, two-, and three-year fall October–November DWR Good-pair windows from published Oro Grande and Tulare orchard recharge lags, then computed them on the same zip and polygon as Round 20. W2 (2023–2025, median +14.20 ft, n=34) and W1 (2024–2025, median +2.72 ft, n=36) hold. W3 (2022–2025, median −20.49 ft, n=36, 33 of 36 shallower) breaks. The round therefore **breaks**. Cause: scope / window-dependence, not a Layer 0 failure and not a volume result. `main` was not edited.

## 2026-11-25 — Round 26: Paani service vs groundwater-condition records (breaks; accept-with-revisions)

Pre-registered a two-limb test of the published Central Valley justification that the Marathwada contrast is why Tulare needs separate water-service and groundwater-condition records. Limb A **holds** (Marathwada and North Maharashtra move the two series in opposite directions). Limb B **breaks**: rabi sown area is cropped area and a utilization/extraction indicator, not protocol \(D_W\). The justification therefore **breaks** as a scope / object-class limit, not a Layer 0 failure. `main` was not edited.

## 2026-11-25 — Round 25: published PAE citation check (holds; accept-with-revisions)

Compared `main` at `37522fc` with `ai/evolution`: the Paani PAE page and Central Valley v0.2 are already byte-identical. Updated the branch-only Examples README pin from stale `56c6ab5` to `37522fc`. Pre-registered, then checked the cited sources against retrieved PDFs or official abstracts. The test **holds**. Residual gaps: some page anchors, some unretrieved full PDFs, and one Qiaozigou timing clause not in the official abstract. This is not a Tulare recharge volume and not a Bite 5 score. `main` was not edited.

## 2026-11-24 — Round 24: Table 3-1 mapping onto Q_sw / D_W (breaks; accept-with-revisions)

Pre-registered a mapping test of WY 2025 Table 3-1 totals onto protocol \(Q_{sw}\) or \(D_W\). The totals include imported groundwater (2.0%–50.4% of the Total; 18.2%–50.4% in Dry years) and are supply accounting, not a declared delivered-service series. The test **breaks**. Cause: scope / object-class, not a Layer 0 failure. The ex-Imported subset is a candidate only. ARM-05 stays `wait`; ARM-06 and ARM-07 opened at `wait` and were not developed. `main` was not edited.

## 2026-11-24 — Round 23: Tulare temporal-mining signature completeness (indeterminate; accept-with-revisions)

Pre-registered a completeness test of protocol §5 against the WY 2025 filing. Table 3-1 supplies a six-year series (imported groundwater included), but independent \(C_{irr}\) cannot be locked because C-zone storage already uses InSAR. The signature is **indeterminate** and is left unassigned. `main` was not edited.

## 2026-11-24 — Round 22: ebonyshell η from published surveys (indeterminate; accept-with-revisions)

Pre-registered a test of whether published surveys supply the rates needed to compute ebonyshell η. The retrieved Kelner abstract and two USGS texts do not. The test is **indeterminate**. Flags stay unassigned. The Kelner PDF was not retrieved. `main` was not edited.

## 2026-11-24 — Round 21: CHIRPS vs WDI Niger rainfall (holds; accept-with-revisions)

Pre-registered a test of whether CHIRPS v2.0 shows interannual rainfall over Niger after WDI AG.LND.PRCP.MM proved to be a repeated 151 mm climatology. The test **holds** (CV 0.171; 71.94–190.45 mm, 1981–2022). The series is a national mean, not a site contrast; \(V\) was not constructed. `main` was not edited.

## 2026-11-24 — Round 20: DWR head-sign stress test (holds; accept-with-revisions)

Pre-registered a sign test of Central Valley v0.2’s net Tulare Lake storage loss against independent DWR wells in 5-022.12, October–November 2019 vs 2025. The test **holds** (15 Good-quality pairs, median depth to water +19.03 ft). A companion spring 2015–2024 contrast, not the decision, has the opposite sign. The result is not a volume confirmation and not a Bite 5 score. `main` was not edited.

## Launch Pad Session 1 summary (2026-11-24)

This session ran Rounds 20–24 on `ai/evolution` only, as direct `[A]` / `[B]` / `[C]` commits, after housekeeping that recorded the four process-aid sheets as adopted research procedures, accepted the pending Tulare pumping-storage proposal with revisions against v0.2, and noted that the freshwater-dictionary proposal folder is only in history at `6797c98`. No pull requests. `main` was not modified and remains at `56c6ab5`. Official papers and the Registry were not rewritten. A1–A8 stay undefined and were not used as if defined. Bite 5 and \(V_W\) were not scored. \(V\) was not constructed. Withdrawn Sahel claims were not restored. The temporal-mining signature, \(\eta\), and *severed* remain unassigned.

Scoreboard: **holds 2, breaks 1, indeterminate 2.** See [STRESS_TESTS.md](STRESS_TESTS.md).

### What moved

- **Round 20 — DWR head-sign test, Tulare 5-022.12.** `accept-with-revisions`. **Holds** on the locked October–November 2019 vs 2025 window (15 Good-quality pairs, median depth-to-water +19.03 ft). Not a volume confirmation of the v0.2 −468,635 AF figure. A companion spring 2015–2024 contrast, not the decision, has the opposite sign (median −42.97 ft, n=11).
- **Round 21 — CHIRPS vs WDI Niger rainfall.** `accept-with-revisions`. **Holds** the diagnosis that WDI AG.LND.PRCP.MM is not interannual (CHIRPS national mean CV 0.171; 71.94–190.45 mm, 1981–2022). The series is a national mean, not a site contrast. Sahel step 1 remains unfilled.
- **Round 22 — ebonyshell \(\eta\) from published surveys.** `accept-with-revisions`. **Indeterminate** (data gap). Retrieved Kelner abstract and two USGS texts do not supply recruitment and loss rates. The Kelner publisher PDF was not retrieved (HTTP 403). Flags stay unassigned.
- **Round 23 — Tulare temporal-mining signature completeness.** `accept-with-revisions`. **Indeterminate** (scope / data limit). Table 3-1 supplies a six-year series that includes imported groundwater, but independent \(C_{irr}\) cannot be locked because C-zone storage already uses InSAR. The signature was not declared to have fired or failed.
- **Round 24 — Table 3-1 mapping onto \(Q_{sw}\) / \(D_W\).** `accept-with-revisions`. **Breaks** (scope / object-class, not a Layer 0 failure). The Total cannot be \(Q_{sw}\) under the dictionary’s separation from groundwater withdrawal, and cannot be \(D_W\) without inventing a delivered-service identification. The ex-Imported subset is a candidate only.

### Theory MAB

ARM-05 was reassessed and stays `wait` (weights, held-out metric, and zone-locked volume conversion still missing). ARM-06 (CHIRPS at predeclared Sahel step-1 locations) and ARM-07 (independent \(C_{irr}\) for the Tulare signature) were opened at `wait` and were not developed.

### Still for Jordan

A1–A8 remain open. Bite 5 remains unscored. The Kelner 2000 PDF remains unretrieved. No arm is ready to develop.

## 2026-11-24 — Housekeeping: Tulare pumping-storage accepted with revisions

Ruled on the pending 24 November Tulare pumping-storage proposal against Central Valley worked example v0.2 on `main`. Accepted with revisions: published evidence is v0.2; the six water-year pairs are descriptive, not a closed budget; the 2017 sign change is not season-only. `main` was not edited.

## 2026-11-24 — Housekeeping: adopted process-aid status lines

Updated the four `ai/NOTES/` sheets so their body status lines say they were adopted as research procedures on 24 November 2026. Noted in `ai/PROPOSALS/README.md` that the freshwater-dictionary proposal folder is only in Git history (`6797c98`). `main` was not edited.

## 2026-11-24 — Sync from main 56c6ab5 (Central Valley v0.2)

Duplicated Central Valley worked example v0.2 and the archived v0.1 from `main` at `56c6ab5`. Synced the empirical review procedure, protocol/crosswalk/index updates, publication changelog, and selective draft status banners. Marked the branch `PUMPING-STORAGE.md` writeup superseded as the published narrative. Closed REVIEW §B1–B7 and §C1–C5 after a re-check; §A left open. Noted archive discrepancies (dictionary proposal folder is historical; Tulare pumping-storage proposal is still `proposed`; process-aid note bodies still say ratification-pending) rather than inventing fixes. `main` was not edited.

## 2026-11-24 — Adversary review carryover

Indexed the 19 accepted proposals, marked nested data directories, archived the reviewed GILN/IIF example and recorded adoption of the four empirical aids. The [Tulare Lake inventory](../Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/DWR-COVERAGE.md) reports well coverage and series limitations. [Author-approved main changes](https://github.com/Causal5/Harmonic-Knowledge-Law/commit/f81967de6cca7062133fa1e28f2304e17e27f314).

## 2026-11-23 — Round 19: Clarification and correction sweep (accept-with-revisions)

`main` moved to `270942c` when Jordan corrected mussel §8 item 4 (the 2023 fish-passage project is at Lock and Dam 22 near Saverton). This cycle adopted that published sentence on the branch and marked the earlier branch wording superseded. Leftover clarifications that do not need a new definition were finished: `SLP_Published.md` bannered; unpublished-vs-`main` banners on diverging `Release/` markdown and scripts; folder notices for branch-only data files; unofficial `src/` placeholders (0.1 distill cut, +0.5 connection increment, 0.4/0.3/0.3 HKL-AI weighting) disabled without replacements. An overreach audit of `Release/` on `main` is written up in `ai/REVIEW_FOR_JORDAN.md` for Jordan to work from (8 terms to define, 7 `main`-only wording items, 5 pending decisions). Official papers were not rewritten. No definition was invented. No theory arm was developed. `main` was not edited.

## 2026-11-23 — Round 18: Source precedence, Release on main (accept-with-revisions)

Jordan directed that the files in `Release/` on `main` are the primary and most up-to-date source, and that everything else is subject to obsolescence. That rule is now in the charter and the agent files. `Release/` on `main` wins a conflict. Official papers and the Registry already match `main`. Nine `Release/` files differ on this branch (example README rows, mussel §8, Sahel addendum marks, Working-draft marks), and worked fills and protocols were added only here; those edits are unpublished branch work, not a publication to `main`. The glossary was rechecked against `Release/` on `main`: AU’s status is reserved/undefined (still no unit); HKL-AI Score, SRI, HRS, Axis as an official symbol, Variation-Δ formulas, manuscript buffer primitives, and the Round 6–9 process labels remain needs-definition. Earlier verdicts were listed and marked, not silently rewritten. C applied three revisions: leftover “already aligned” inventory wording, standing-document pointers at branch READMEs, and a Layer 0 heading that had called `START_HERE.md` the current introduction. No definition was invented. `main` was not edited.

## 2026-11-23 — Round 17: Terminology map and erratum (accept-with-revisions)

Wrote `ai/GLOSSARY.md` as a map from Registry v0.3.2 and the reconciled papers to stale wording in working drafts and historical files. Official Layer 0/1 papers were not rewritten, and no definitions were invented. HKL Lyapunov v2 was bannered and marked where it still treated \(dV/dt\le 0\) as required and \(V^*\) as a PCB identity. Leftover PAE-as-number, AU, and \(PAE=E-C_{pae}\) wording in AEF v2 and the buffer draft was marked; C also marked AEF v2’s ELQ Triangle. Historical CorePrinciples glossaries and related files were bannered, original wording preserved. Undefined terms (AU, HKL-AI Score, SRI, HRS, and others) are flagged `needs-definition`. Branch READMEs now say the `ai/` tree is on `ai/evolution` only, not on `main`.

## Session 3 summary (2026-11-21)

This session ran Rounds 12–16 on `ai/evolution` only, as direct
`[A]` / `[B]` / `[C]` commits. No pull requests. `main` was not
modified. Nothing was moved to `ai/REJECTED/`. Four of the five
rounds were worked examples with retrieved public data, committed
scripts, and computed results or explicit n=0 / climatology findings.
Round 16 opened a theory MAB registry and assessed arms without
developing any of them. Official AEF, HKL, and current Sahel papers
were not rewritten except for a logged Session 3 note on the mussel
*example* §8 item 4 and a pointer in the ebonyshell protocol.
Withdrawn Sahel claims were not restored. \(\eta\) and the *severed*
flag were not assigned. Bite 5 and \(V_W\) were not scored.

### What moved

- **Round 12 — Keokuk / Lock 19 official status and USGS 05474500 discharge.**
  `accept-with-revisions`. Citation [38] locates the first-of-its-kind
  fish passage at Lock and Dam 22 near Saverton, Missouri, not at
  Keokuk. Official records describe a uADS carp deterrent at Lock and
  Dam 19 (River Mile 364.2 dated to a 24 January 2025 Wayback snapshot
  of a 30 August 2024 USACE page; live URL HTTP 403 on 21 November 2026;
  ICRCC FY2026 plan, retrieved live, says experimental operation through
  2026). Discharge at USGS 05474500 for locked USGS water years 2016–2025:
  3,652/3,653 days; period mean 100,725 ft³/s including 39 estimated days
  and 100,548 ft³/s excluding them; one missing day (2022-08-31). The
  modern OGC daily API was missing 923 of those days (0 value disagreements
  on overlapping days). NWIS DV was adopted as primary after those gaps
  were seen. Discharge is hydrologic context only.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/b524751256698c2fd770f7b6a1a240f9a916e41c
- **Round 13 — Tulare Lake 5-022.12 DTW contrast and retrieved CVHM2 figures.**
  `accept-with-revisions`. Official DWR Bulletin 118 subbasin 5-022.12
  (San Joaquin Valley–Tulare Lake, 837.356 sq mi) was locked from a
  FeatureServer GeoJSON. A predeclared USGS 72019 spring 2015 vs spring
  2024 contrast yielded n=0 qualifying wells (one in-polygon 2015
  measurement; zero in 2024). That is a coverage result in this API
  extract, not a finding of no water-level change; DWR/CASGEM series
  were not retrieved. The USGS Publications Warehouse abstract of
  Faunt et al. (2024) was retrieved and quotes approximately 158 km³ of
  Central Valley storage loss from pre-development to 2019, about 15%
  permanent — abstract-only, not recomputed, not a 5-022.12 2015–2024
  result. Bite 5 and \(V_W\) were not scored.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/716531b5db27d2f3c18c391d3ca1c6580c54ad8c
- **Round 14 — Niger WDI/FAOSTAT precipitation precursor.**
  `accept-with-revisions`. Indicator AG.LND.PRCP.MM for Niger is 151.0 mm
  per year in every year of locked 1961–2022 — a national long-term
  average, not an interannual or site rainfall series. No \(V\) was
  constructed. CHIRPS was not retrieved.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/511f1727c29a5d227f9dc7319de63a5f497e3d5d
- **Round 15 — Niger WDI/FAOSTAT cereal-yield precursor.**
  `accept-with-revisions`. Indicator AG.YLD.CREL.KG for Niger, 1961–2022:
  62 numeric years, 61 distinct values, mean 423.82 kg/ha, minimum
  257.1 kg/ha in 1984, maximum 599.3 kg/ha in 1964. Chosen after Round 14
  showed the precipitation indicator is not interannual; that choice is
  declared. Yield is not rainfall, not FMNR, and not \(V\).
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/f6c483733d46ca85130c1a35d23a46727604583f
- **Round 16 — Theory MAB registry and first assessments.**
  `accept-with-revisions`. Opened `ai/THEORY_MAB.md`. Assessments were
  written before any development. ARM-01–04 dropped; ARM-05 wait (not
  explore). Rewards are qualitative. Layer 0 unchanged. No arm developed.
  C commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/52b56294b066fe5ab1e09253d59cb02b0b995cd6

### New corpus findings

- Mussel example §8 item 4, citing [38], said that as of 2023 USACE was
  preparing a fish passage “at the dam” (Keokuk), “the first of its kind
  on the Mississippi River.” The retrieved article (Iowa Capital Dispatch,
  21 May 2023, and the Waterways Council reprint) names Lock and Dam 22
  near Saverton, Missouri, as that project. A logged Session 3 note was
  added to the example; the 2023 sentence was not silently deleted.

### Still open / for Jordan

- Official “the” Central Valley or San Joaquin Valley study boundary for
  Bite 5 remains an open choice among official units; 5-022.12 was a
  declared trial subbasin only.
- CHIRPS interannual rainfall was named in Session 3 and was not
  retrieved. Bounded-test comparable locations remain UNFILLED-REQUIRED.
- Ebonyshell recruitment and mortality series sufficient for \(\eta\)
  were not found. Official above/below mussel-reach river miles remain
  UNFILLED-REQUIRED.
- The leftover side branch
  `ai/proposal/2026-11-21-freshwater-data-dictionary` still exists; there
  is no delete_branch tool.
- Round 12’s first [A] commit (`6fcf923`) briefly wrote `$file:`
  placeholders into TRAIL and three data files; those were repaired in
  `[A] b731c57`. Later pushes inlined file contents in one JSON payload.

### What this is not

Not publication to `main`. Not scientific validation of HKL. Not a
computed \(\eta_{TM}\), Bite 5 score, or Sahel \(V\).
## 2026-11-21 — Round 16: Theory MAB registry and first assessments

Process aid, not a worked empirical fill. `accept-with-revisions`.
Opened `ai/THEORY_MAB.md` as a ratification-pending arm registry.
Assessments were written before any development. ARM-01–04 (spatial
sink-impairment shortcut; uADS as \(\eta\); score Bite 5 now; construct
Sahel \(V\) from WDI series) are `drop`. ARM-05 (later dictionary fill
once official series and predeclarations exist) is `wait`, which is not
explore and is not permission to score. Rewards are qualitative prose,
not a fitted algorithm. Layer 0 is unchanged. No arm was developed.
C commit: this commit.
Registry: `ai/THEORY_MAB.md`.
Verdict: `ai/LEDGER/verdicts/V-2026-11-21-theory-mab.md`.

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
