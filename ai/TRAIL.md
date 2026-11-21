# Trail — landmarks for human readers

This is a chronological breadcrumb log of work on `ai/evolution`. It is
written for a human following the branch, not as a substitute for the
ledger or the charter.

Each entry has: the date (America/New_York), which agent (or setup work),
what was done, why, links to ledger files and commits when they exist, and
a one-paragraph plain-English “what this means” summary.

Every agent action on this branch must append an entry here, as required by
`ai/AGENTS/CYCLE.md`. Newest entries go at the top, under this introduction.

---

## 2026-11-21 — Adversary: challenges to the Niger cereal-yield fill (Round 15)

- **Agent:** Adversary (B)
- **What:** Filed two challenges: the yield indicator was chosen after it was seen to vary, following Round 14; and national cereal yield is not an FMNR, rainfall, or HKL-correction result, including the 1984 minimum and 1964 maximum.
- **Why:** Session 3 asks B to attack provenance, cherry-picking, and whether the results actually test anything.
- **Links:** `ai/LEDGER/challenges/CH-niger-yield-02-chosen-after-variation-seen.md`; `CH-niger-yield-02-national-yield-not-fmnr.md`. No pull request. `main` was not changed.
- **What this means:** The official yield numbers can be re-run, but they are still a national agricultural series chosen after Round 14, not a completed Sahel test.

## 2026-11-21 — Work agent: Niger World Bank / FAO cereal-yield series (Round 15)

- **Agent:** Work (A)
- **What:** Opened proposal `ai/PROPOSALS/2026-11-21-niger-cereal-yield/` and claims `C-niger-yield-01`–`02`. Retrieved official WDI/FAOSTAT cereal yield for Niger, 1961–2022: 62 numeric years, 61 distinct values, mean 423.82 kg/ha, minimum 257.1 kg/ha in 1984, maximum 599.3 kg/ha in 1964. Declared that this indicator was chosen after Round 14 showed the precipitation indicator is not interannual. Did not treat yield as rainfall or V, and did not retrieve CHIRPS.
- **Why:** Session 3 asked for worked examples with real public data. Round 14 left interannual Sahel series unfilled.
- **Links:** `ai/PROPOSALS/2026-11-21-niger-cereal-yield/proposal.md`; fill under `Release/Examples/sahel/worked-fills/2026-11-21-niger-cereal-yield-wb/`. No pull request. `main` was not changed.
- **What this means:** There is now an official year-by-year cereal-yield series for Niger on the branch. It is an agricultural outcome series, not a rainfall history, and it is not a test of FMNR or of HKL.

## 2026-11-21 — Verifier: Niger precipitation fill accepted with revisions (Round 14)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Re-ran the official-indicator script offline and reproduced 151.0 mm per year in all 62 years. Confirmed the World Bank API returns HTTP 200. Applied wording so 151 mm cannot be used as a site rainfall value and so the cycle cannot be described as having filled interannual Sahel rainfall. Did not construct V or restore withdrawn claims.
- **Why:** Session 3 requires C to re-run scripts, check that sources resolve, and apply revisions in the same verdict commit.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-niger-precip-wb.md`; fill under `Release/Examples/sahel/worked-fills/2026-11-21-niger-precip-wb/`; [A] `4bf9fef`; [B] `4f6bc58`. No pull request. `main` was not changed.
- **What this means:** There is now an official FAO/World Bank precipitation figure for Niger on the branch, and it is a single long-term average. A year-to-year rainfall history, including CHIRPS, is still outstanding.

## 2026-11-21 — Adversary: challenges to the Niger precipitation fill (Round 14)

- **Agent:** Adversary (B)
- **What:** Filed two challenges: 151 mm per year is a national long-term average, not a site or southern-Sahel rainfall value; and CHIRPS was named in Session 3 but not retrieved, so this cycle has not filled interannual Sahel rainfall or bounded-test environmental setting.
- **Why:** Session 3 asks B to attack provenance, boundaries, and whether the results actually test anything.
- **Links:** `ai/LEDGER/challenges/CH-niger-precip-01-national-average-not-a-site.md`; `CH-niger-precip-02-chirps-not-retrieved.md`. No pull request. `main` was not changed.
- **What this means:** The official 151 mm figure is real, and it is not a year-to-year rainfall history. It also is not the rainfall at an FMNR site.

## 2026-11-21 — Work agent: Niger World Bank / FAOSTAT precipitation indicator (Round 14)

- **Agent:** Work (A)
- **What:** Opened proposal `ai/PROPOSALS/2026-11-21-niger-precip-wb/` and claims `C-niger-precip-01`–`02`. Retrieved the official WDI/FAOSTAT indicator AG.LND.PRCP.MM for Niger and found a single repeated long-term average of 151.0 mm per year in all 62 years of the locked 1961–2022 window. Did not construct V, did not restore withdrawn Sahel claims, and did not lock bounded-test comparable locations.
- **Why:** Session 3 asked for worked examples with real public data, and named FAO and World Bank as source classes for Sahel work. The first job is to see what an official series actually is before anyone uses it as year-to-year climate.
- **Links:** `ai/PROPOSALS/2026-11-21-niger-precip-wb/proposal.md`; fill under `Release/Examples/sahel/worked-fills/2026-11-21-niger-precip-wb/`. No pull request. `main` was not changed.
- **What this means:** An official country rainfall number for Niger is now on the branch, and it is a climatological average of 151 mm per year, not a history of wet and dry years. It cannot, by itself, test FMNR or a change in burden.

## 2026-11-21 — Verifier: Tulare Lake DTW fill accepted with revisions (Round 13)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Re-ran the locked 72019 script offline and reproduced n=0 qualifying wells. Confirmed the committed GeoJSON is 5-022.12 and that the USGS Publications Warehouse page and DWR FeatureServer query return HTTP 200. Applied wording so n=0 cannot be summarized as “no water-level change,” the March–May window stays a declared convention, and the 158 km³ / 15% figures stay abstract-only quotations. Did not score Bite 5 or V_W.
- **Why:** Session 3 requires C to re-run scripts, check that sources resolve, and apply revisions in the same verdict commit.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-tulare-lake-dtw.md`; fill under `Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/`; [A] `97d4614`; [B] `3a59432`. No pull request. `main` was not changed.
- **What this means:** The branch now has an official Tulare Lake polygon and a script that currently finds no paired USGS depth-to-water measurements for 2015 versus 2024. The 158 km³ sentence is on an official USGS page, but it is not a number we computed for that subbasin.

## 2026-11-21 — Adversary: challenges to the Tulare Lake DTW fill (Round 13)

- **Agent:** Adversary (B)
- **What:** Filed three challenges: n=0 is a USGS-product coverage result, not a finding of no water-level change, and DWR/CASGEM series were not retrieved; March–May is a declared window, not a retrieved official spring definition; the 158 km³ / 15% figures were read from a Publications Warehouse abstract, not the paper body or a model rerun.
- **Why:** Session 3 asks B to attack provenance, boundaries, and whether the results actually test anything.
- **Links:** `ai/LEDGER/challenges/CH-tulare-dtw-02-usgs-coverage-not-hydrology.md`; `CH-tulare-dtw-02-spring-window-unofficial.md`; `CH-tulare-dtw-03-abstract-only.md`. No pull request. `main` was not changed.
- **What this means:** The locked script really does return no paired wells, and the 158 km³ sentence really is on the USGS page. The risk is over-reading those facts as a completed hydrologic test of Tulare Lake or as a full-paper verification of CVHM2.

## 2026-11-21 — Work agent: Tulare Lake 5-022.12 DTW contrast and retrieved CVHM2 figures (Round 13)

- **Agent:** Work (A)
- **What:** Opened proposal `ai/PROPOSALS/2026-11-21-tulare-lake-dtw/` and claims `C-tulare-dtw-01`–`03`. Committed an official Bulletin 118 5-022.12 GeoJSON, a re-runnable USGS 72019 script, and a locked spring 2015 vs 2024 contrast whose result is n=0 qualifying wells. Also retrieved the USGS Publications Warehouse abstract of Faunt et al. (2024) quoting approximately 158 km³ of Central Valley storage loss to 2019, about 15% permanent. Did not score Bite 5 or V_W.
- **Why:** Session 3 asks for worked examples with real public data. The Central Valley dictionary and Bite 5 checklist still needed an official published unit and a locked computation, including an honest needs-evidence outcome if the series do not support a change.
- **Links:** `ai/PROPOSALS/2026-11-21-tulare-lake-dtw/proposal.md`; fill under `Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/`. No pull request. `main` was not changed.
- **What this means:** We now have an official Tulare Lake subbasin polygon on the branch and a script that other agents can re-run. The USGS field-measurement extract does not support a 2015-to-2024 water-level change in that subbasin. The 158 km³ figure is a retrieved published estimate for a larger domain, not a number we computed.

## 2026-11-21 — Verifier: Keokuk / Lock 19 status fill accepted with revisions (Round 12)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Re-ran the discharge script offline against the committed RDB and reproduced the claimed counts and means. Confirmed that the cited Iowa Capital Dispatch, Waterways Council, DVIDS, water-year, Wayback, and ICRCC URLs return HTTP 200, and that the live USACE Lock 19 page still returns 403. Applied a Session 3 note to mussel example §8 item 4 and a protocol pointer, with B’s dating, DVIDS attribution, source-choice, estimated-day, and “not an HKL test” revisions. Did not assign \(\eta\) or the *severed* flag.
- **Why:** Session 3 requires C to re-run scripts and check that sources resolve, and to apply revisions in the same verdict commit.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-keokuk-ld19-status.md`; worked fill under `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/`; [A] `6fcf923` / repair `b731c57`; [B] `3e2f352`. No pull request. `main` was not changed.
- **What this means:** The standing mussel example now records that citation [38] was about Lock and Dam 22, and that the official project at Keokuk in the retrieved records is an acoustic deterrent. River flow at the Keokuk gage has been summarized, but mussel renewal still has not been computed.

## 2026-11-21 — Adversary: challenges to the Keokuk / Lock 19 worked fill (Round 12)

- **Agent:** Adversary (B)
- **What:** Filed five challenges: the USACE Lock 19 page was not read live (Wayback of 24 January 2025); the Lock 22 status rests on a DVIDS story, not a fetched project sheet; the primary discharge service was chosen after OGC gaps were seen; reported means include 39 estimated days with no companion exclusion; and the discharge series does not test any ebonyshell-protocol HKL quantity.
- **Why:** Session 3 asks B to attack provenance, units, boundaries, cherry-picking, and whether the results actually test anything. The citation-identity claim was not challenged on the Saverton sentence, which is in the retrieved articles.
- **Links:** `ai/LEDGER/challenges/CH-keokuk-ld19-02-wayback-not-live.md`; `CH-keokuk-ld19-02-dvids-not-project-page.md`; `CH-keokuk-ld19-03-source-chosen-after-gaps.md`; `CH-keokuk-ld19-03-estimated-in-mean.md`; `CH-keokuk-ld19-03-not-an-hkl-test.md`. No pull request. `main` was not changed.
- **What this means:** The records still point at a citation mislocation and at a carp deterrent at Lock 19, but the official-page dating, the discharge-source choice, the estimated days, and the fact that river flow is not a mussel renewal test all need to be held in view before anything is accepted.

## 2026-11-21 — Work agent: repair TRAIL and primary data files (Round 12)

- **Agent:** Work (A)
- **What:** Restored `ai/TRAIL.md` and the three large worked-fill files (NWIS Daily Values RDB, daily discharge CSV, and summary JSON) that the first Round 12 [A] commit accidentally replaced with unexpanded `$file:` path placeholders. No proposal claims were changed. The other Round 12 files in that commit were already intact.
- **Why:** The first [A] push packed those four paths as nested `$file:` references inside a JSON payload; only the outer payload was expanded, so the branch briefly held placeholder stubs instead of the trail and the primary data. This repair puts the intended contents on `ai/evolution`.
- **Links:** same proposal and worked fill as the first [A] commit (`6fcf923`). No pull request. `main` was not changed.
- **What this means:** The human trail and the Keokuk discharge data are back on the branch. Later agents should treat the repaired files, not the placeholder stubs, as the Round 12 work product.

## 2026-11-21 — Work agent: Keokuk / Lock 19 official status and USGS 05474500 discharge (Round 12)

- **Agent:** Work (A)
- **What:** Opened proposal `ai/PROPOSALS/2026-11-21-keokuk-ld19-status/` and claims `C-keokuk-ld19-01`–`03`. Committed a worked fill under `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/` with retrieved public sources, a re-runnable discharge script, and computed USGS 05474500 daily-mean discharge for locked water years 2016–2025. Did not assign \(\eta\) or the *severed* flag. Did not edit the official example or protocol in this commit; proposed wording is in the proposal for the verifier.
- **Why:** Session 3 is to produce actually worked examples with real public data and citations. The mussel protocol still had fish-passage construction status and official location unfilled, and citation [38] needed to be read against official records.
- **Links:** `ai/PROPOSALS/2026-11-21-keokuk-ld19-status/proposal.md`; claims under `ai/LEDGER/claims/C-keokuk-ld19-0*.md`; worked fill and `retrieval_log.md`. No pull request. `main` was not changed.
- **What this means:** Public records retrieved today locate the “first of its kind” fish passage at Lock and Dam 22, not at Keokuk. The official project at Lock and Dam 19 is an acoustic carp deterrent. River flow at the Keokuk gage was summarized for ten water years. Mussel renewal ratios are still uncomputed because no qualifying recruitment series was found.

## 2026-11-21 — Session 2 summary (Rounds 7–11)

- **Agent:** Session close (after Verifier, not a new cycle role)
- **What:** Wrote the Session 2 summary into `ai/CHANGELOG.md`. Rounds 7–11 all ended `accept-with-revisions`. Nothing was rejected. No empirical quantities were invented. Official papers were not rewritten. New corpus findings included random placeholders in `CorePrinciples/Law_of_We_Full.md`, leftover invented scores in `src/`, a stale protocol quote, an unmarked addendum cite, and Working-draft dead cites plus withdrawn necessary-dV/dt wording.
- **Why:** Jordan asked to review the AI line later through the changelog, and to hear where the adversary found errors in the original corpus.
- **Links:** `ai/CHANGELOG.md` (Session 2 summary); Round 7–11 verdict files under `ai/LEDGER/verdicts/`.
- **What this means:** A human can now read one summary of the corrections, the later theory and example aids, what B found in the standing corpus, and which questions are still for Jordan.

## 2026-11-21 — Verifier: four-field effort declaration accepted with revisions (Round 11)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the sheet is blank and official papers were not edited. Renamed it a declaration sheet, pointed the four records at the 16 October / AEF §2 definitions, and required N/A on non-correction rows so a filler cannot invent a correction to complete a cell.
- **Why:** A sheet that sounds already filled, or that demands a correction wherever effort is mentioned, would collapse the four records it exists to keep apart.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-four-field-effort-recording.md`; `ai/NOTES/four-field-effort-recording-sheet-v0.1.md`.
- **What this means:** Later work can still talk about effort, but it has to say which of the four records it means, and it can leave the cells blank.

## 2026-11-21 — Adversary: four-field effort recording challenges (Round 11)

- **Agent:** Adversary (B)
- **What:** Challenged the sheet for a “recording” title that can sound like measured data, for listing the four records without pointing at the 16 October / AEF §2 definitions, and for a matched-burden column that can pressure a filler to invent a correction on an expenditure-only row.
- **Why:** A blank aid that sounds filled, or that lets spending grow a fake correction to complete a cell, would undo the split it is meant to protect.
- **Links:** `ai/LEDGER/challenges/CH-four-field-01-recording-sounds-filled.md`; `CH-four-field-02-undefined-terms.md`; `CH-four-field-02-matched-burden-pressure.md`.
- **What this means:** If the sheet is kept, it should look blank, point at the existing definitions, and tell non-correction rows to use N/A rather than invent a correction.

## 2026-11-21 — Work agent: four-field effort recording sheet (Round 11)

- **Agent:** Work (A)
- **What:** Proposed a blank, ratification-pending aid that keeps allocation, expenditure, achieved correction, and side burden in separate records. No rows were filled. Official papers were not rewritten.
- **Why:** Round 7 stopped the experimental helper from treating spending as correction. Later fills will need the same four-way split in writing, under the 16 October record and current AEF §2.
- **Links:** `ai/PROPOSALS/2026-11-21-four-field-effort-recording/proposal.md`; `ai/NOTES/four-field-effort-recording-sheet-v0.1.md`; claims `C-four-field-01` through `-03`.
- **What this means:** A later example can still talk about effort, but it should say whether it means money spent, correction achieved, or a side burden — and it can leave those cells blank if the evidence is not there.

## 2026-11-21 — Verifier: Working-draft dead-cite marks accepted with revisions (Round 10)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed official papers were not edited. Marked the leftover AEF v2 Lyapunov-condition clause, the buffer draft’s second dV/dt ≤ 0 sentence, and AEF v2’s PAE-as-number table row and first product (later products share that status). No replacement formula was invented.
- **Why:** Leaving the withdrawn condition or the PAE-as-number pattern unmarked in the next sentence would have undercut the banners.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-working-draft-dead-cites.md`.
- **What this means:** A human can still inspect the recovered drafts, but should not read their section numbers, their necessary-dV/dt line, or their PAE-as-number equations as current theory.

## 2026-11-21 — Adversary: Working-draft dead-cite challenges (Round 10)

- **Agent:** Adversary (B)
- **What:** Challenged leftover unmarked wording: AEF v2 still presents “the Lyapunov condition dV/dt ≤ 0” as current; the buffer draft still requires that inequality across the buffer window after marking only the first clause; and AEF v2 still types PAE as a number without a mark.
- **Why:** A banner that leaves the withdrawn condition or the PAE-as-number pattern working in the next sentence is not finished.
- **Links:** `ai/LEDGER/challenges/CH-working-cites-01-aef-v2-lyapunov.md`; `CH-working-cites-02-buffer-second-sentence.md`; `CH-working-cites-01-pae-as-number.md`.
- **What this means:** A human reading those drafts should also see marks on the leftover Lyapunov and PAE-as-number lines, not only on the section numbers.

## 2026-11-21 — Work agent: Working-draft dead-cite marks (Round 10)

- **Agent:** Work (A)
- **What:** Added status banners and in-place dead-cite marks to the recovered AEF v2 draft and the buffer-as-temporal-dimension addendum. Marked “HKL §5.1,” “Sahel §5.3,” “HKL §4.1,” “AEF §3.2 / §3.3,” a stale Sahel §6 “demonstrates” claim, and the buffer draft’s statement that dV/dt ≤ 0 is a necessary HKL condition. No replacement section numbers were invented, and official papers were not rewritten.
- **Why:** Round 7 marked the same patterns in the unpromoted Sahel addendum. These Working drafts still presented dead section numbers, and one still treated a withdrawn monotonic-drift condition as current HKL.
- **Links:** `ai/PROPOSALS/2026-11-21-working-draft-dead-cites/proposal.md`; claims `C-working-cites-01` through `-03`.
- **What this means:** A human can still read the recovered drafts, but should not treat their section numbers or the “necessary dV/dt ≤ 0” line as current theory.

## 2026-11-21 — Verifier: object-class declaration accepted with revisions (Round 9)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the sheet is blank and not a registry amendment. Marked it as a proposed aid rather than a required cycle step, required a separate row for each use of a symbol, and added an unfilled effort-record field.
- **Why:** A labeling aid that is treated as mandatory, or that merges two object classes, would undermine the Layer 0 distinctions it is meant to protect.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-object-class-declaration.md`; `ai/NOTES/object-class-declaration-sheet-v0.1.md`.
- **What this means:** A later fill can use this sheet if wanted, but it is not automatically part of the cycle, and spending still cannot be written down as correction.

## 2026-11-21 — Adversary: object-class declaration challenges (Round 9)

- **Agent:** Adversary (B)
- **What:** Challenged the sheet for reading like a mandatory cycle step, for forcing exactly one object class on a symbol that may have two roles, and for not asking effort terms to separate allocation, expenditure, achieved correction, and side burden.
- **Why:** A labeling aid that quietly becomes required, or that lets two Layer 0 roles share one cell, will not protect the distinctions it was written to protect.
- **Links:** `ai/LEDGER/challenges/CH-object-class-01-mandatory-use.md`; `CH-object-class-02-one-class-only.md`; `CH-object-class-02-effort-fields.md`.
- **What this means:** If the sheet is kept, it should stay optional until adopted, allow one row per use, and not let spending be written down as correction.

## 2026-11-21 — Work agent: object-class declaration sheet (Round 9)

- **Agent:** Work (A)
- **What:** Proposed a blank, ratification-pending sheet for later empirical fills. Each symbol would have to be labeled as reality, selected state, observation, or model, and as computed or qualitative. No rows were filled.
- **Why:** Layer 0 already separates those objects. Later fills will go wrong if a model quantity or a qualitative story is written down as if it were an observation.
- **Links:** `ai/PROPOSALS/2026-11-21-object-class-declaration/proposal.md`; `ai/NOTES/object-class-declaration-sheet-v0.1.md`; claims `C-object-class-01` through `-03`.
- **What this means:** Someone opening a later Bite 5, Sahel, or mussel fill should have to say what kind of object they are writing down, before they look at a series.

## 2026-11-21 — Verifier: computed-status assignment accepted with revisions (Round 8)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the note is not a registry amendment and computes nothing. Renamed the heading to a proposed procedure, limited scope to computed-flag assignment (not ordinary language), and required the protocol to be locked before the series are inspected.
- **Why:** A procedure that sounds already official, or that can be locked after seeing the answer, would not have done the job.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-computed-status-assignment.md`; `ai/NOTES/computed-status-assignment-v0.1.md`.
- **What this means:** Later work can still tell a qualitative story, but the official flag stays blank until a pre-locked protocol actually computes the quantity, or the field stays unfilled.

## 2026-11-21 — Adversary: computed-status assignment challenges (Round 8)

- **Agent:** Adversary (B)
- **What:** Challenged the note for an official-sounding “rule” title, for not separating ordinary-language “severed” from the registry flag, and for a “locked protocol” that might be locked after the numbers are in view.
- **Why:** A pending procedure that sounds adopted, or that can be locked after the fact, repeats the qualitative-assignment problem it is trying to stop.
- **Links:** `ai/LEDGER/challenges/CH-computed-status-01-rule-sounds-official.md`; `CH-computed-status-01-ordinary-language.md`; `CH-computed-status-02-lock-before-assignment.md`.
- **What this means:** If this note is kept, it should stay clearly unadopted, should not gag descriptive prose, and should require the protocol to be locked before anyone looks at the result.

## 2026-11-21 — Work agent: computed-status assignment rule (Round 8)

- **Agent:** Work (A)
- **What:** Proposed a short ratification-pending branch rule: a registry flag defined by a computed quantity may not be assigned from a qualitative narrative alone. No quantities were computed, and official papers were not rewritten.
- **Why:** Round 7 fixed the mussel *severed* sentence. Later work will face the same temptation unless the discipline is stated generally, under Layer 0 and the 16 / 30 October records.
- **Links:** `ai/PROPOSALS/2026-11-21-computed-status-assignment/proposal.md`; `ai/NOTES/computed-status-assignment-v0.1.md`; claims `C-computed-status-01` through `-03`.
- **What this means:** A later example can still tell the qualitative story, but it should leave the official flag blank until the number is actually computed, or say the evidence is not there.

## 2026-11-21 — Verifier: Session 2 corpus corrections accepted with revisions (Round 7)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Re-ran the scripts on this Linux box. Confirmed the PAE split and the mussel §8 reword. Fixed the four hits: leftover invented scores in `_score_reasoning` and Libra, `np.random` placeholders in `CorePrinciples/Law_of_We_Full.md`, the unmarked AEF §3.2 cite, and the stale protocol quote. Did not invent a replacement section number or a renewal ratio.
- **Why:** A correction that leaves the same patterns standing in the next file is not finished.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-session2-corpus-corrections.md`.
- **What this means:** A human can run the experimental scripts on Linux and should now see “not implemented” instead of random or hardcoded scores, and should see warnings on the addendum and a provisional mussel flag assignment.

## 2026-11-21 — Adversary: Session 2 corpus-correction challenges (Round 7)

- **Agent:** Adversary (B)
- **What:** Checked the four corrections and filed six challenges. Two are expected to test whether the PAE helper and the mussel §8 reword actually hold. Four attack leftovers: invented numeric scores still printed by `_score_reasoning` and Libra; `np.random` placeholder scores still sitting in `CorePrinciples/Law_of_We_Full.md`; an unmarked “AEF §3.2” cite in the addendum body; and the ebonyshell protocol still quoting the old “so … severed” example sentence.
- **Why:** A correction cycle is not finished if B only repeats A’s claims. The standing corpus can still hide the same patterns the patch was meant to stop.
- **Links:** `ai/LEDGER/challenges/CH-s2-corrections-01-pae-separation.md`; `CH-s2-corrections-02-residual-invented-scores.md`; `CH-s2-corrections-02-coreprinciples-random.md`; `CH-s2-corrections-03-unmarked-aef-32.md`; `CH-s2-corrections-04-severed-assignment.md`; `CH-s2-corrections-04-protocol-stale-example.md`.
- **What this means:** A human should treat the Linux import fix and the PAE field split as things to verify, and should also look at the leftover invented scores, the CorePrinciples random placeholders, the unmarked AEF cite, and the stale protocol sentence before calling the corpus clean.

## 2026-11-21 — Work agent: Session 2 corpus corrections (Round 7)

- **Agent:** Work (A)
- **What:** Proposed and patched the four Session 1 corpus issues Jordan asked to correct: `_apply_pae` now records expenditure separately from correction; `src/` imports match filenames and placeholder scores return `None`; the unpromoted Sahel addendum has a status banner and in-place dead-cite marks; mussel example §8 no longer assigns the *severed* flag from a qualitative line. Scripts were run on this Linux box while preparing the patch.
- **Why:** Jordan approved correcting those issues and then progressing the work in further rounds. The corrections have to go through a full A/B/C cycle so B and C can check the fixes.
- **Links:** `ai/PROPOSALS/2026-11-21-session2-corpus-corrections/proposal.md`; claims `C-s2-corrections-01` through `-04`. First commit `2447617` landed the example/addendum/ledger/claim/`human_node` edits; the `src/` patches and proposal follow in a completion commit because a single push may carry at most four large file substitutions.
- **What this means:** A human running the experimental scripts on Linux should now get “not implemented” instead of random scores, and should not see the mussel example or the addendum quietly over-claim.

## 2026-11-21 — Session 1 summary (Rounds 2–6)

- **Agent:** Session close (after Verifier, not a new cycle role)
- **What:** Wrote the Session 1 summary into `ai/CHANGELOG.md`. Rounds 2–6 all ended `accept-with-revisions`. Nothing was rejected. No empirical quantities were invented. Strongest corpus findings: experimental `_apply_pae` treats expenditure as correction; Linux imports fail and some scores are random; the unpromoted Sahel addendum cites current-paper section numbers those papers do not have; the mussel example assigns the severed flag without a computed \(\eta_{TM}\).
- **Why:** Jordan asked to review the AI line later through the changelog, and to hear where the adversary found errors in the original corpus.
- **Links:** `ai/CHANGELOG.md` (Session 1 summary); Round 2–6 verdict files under `ai/LEDGER/verdicts/`.
- **What this means:** A human can now read one summary of what moved, what was left blank on purpose, and which standing-corpus tensions are still sitting in the original files.

## 2026-11-21 — Verifier: inheritance firewall accepted with revisions (Round 6)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the note does not amend the registry or compute quantities. Marked the new status words ratification-pending, warned that “eligible” is not validation, and stated that T1 does not license a freshwater \(\eta\) filling in this cycle.
- **Why:** A firewall that sounds like official vocabulary would have undermined its own purpose.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-application-quantity-inheritance.md`; `ai/NOTES/application-quantity-inheritance-v0.1.md`.
- **What this means:** Application quantities still cannot quietly become universal law on this branch, and this session did not sneak a Central Valley coverage number into the dictionary.

## 2026-11-21 — Adversary: inheritance-firewall challenges (Round 6)

- **Agent:** Adversary (B)
- **What:** Challenged the new status words as easy to misread as a promotion or as adopted registry vocabulary, and challenged T1 as looking like a license to fill freshwater \(\eta_{TM}\) while Round 1 boundaries are still open.
- **Why:** A firewall that mints official-sounding labels can do the very thing it is trying to prevent.
- **Links:** `ai/LEDGER/challenges/CH-inheritance-01-eligible-misread.md`; `CH-inheritance-01-status-adoption.md`; `CH-inheritance-02-t1-not-a-license.md`.
- **What this means:** If this procedure is kept, it should stay clearly unadopted and should not be treated as permission to compute a new coverage number in this session.

## 2026-11-21 — Work agent: application-quantity inheritance firewall (Round 6)

- **Agent:** Work (A)
- **What:** Proposed a decision sheet for when example-born quantities may be reused in a new domain. Classified the unpromoted addendum’s “HKL §5.1” margin as ineligible, and freshwater reuse of \(\eta_{TM}\) and reuse of the corrective-dependency screen as needing an explicit mapping. No quantities were computed; the registry is not amended.
- **Why:** The experiment is to take the framework forward under the original premise. A firewall keeps application quantities from quietly becoming Layer 0 law.
- **Links:** `ai/PROPOSALS/2026-11-21-application-quantity-inheritance/proposal.md`; `ai/NOTES/application-quantity-inheritance-v0.1.md`.
- **What this means:** A later study can still try to map renewal coverage into the Central Valley, but only after writing the mapping, and it cannot treat the addendum’s margin formula as current HKL.

## 2026-11-21 — Verifier: Sahel test plan accepted with revisions (Round 5)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the plan is blank of series and does not restore withdrawn wording. Added locked comparability dimensions, a locked local-regulation variable list, and a clarified primary-source rule. Linked the plan from `Release/Examples/README.md`. Did not edit the current Sahel paper.
- **Why:** A test that leaves “comparable” and the treatment variables open can be filled after seeing the answer.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-sahel-bounded-test-plan.md`; `Release/Examples/sahel_bounded_test_plan_v0.1.md`.
- **What this means:** Later Sahel work can fill official locations and sources against this sheet, or leave it blank, without treating the addendum as current theory or bringing back a “passed falsification” slogan.

## 2026-11-21 — Adversary: Sahel test-plan challenges (Round 5)

- **Agent:** Adversary (B)
- **What:** Challenged the plan for not locking the local-regulation variable list used in step 5, for not requiring comparability dimensions to be declared, and for a source rule that might block retrieving primaries the current paper already points to.
- **Why:** A test recipe that leaves the treatment variables or the meaning of “comparable” open can be filled after the fact.
- **Links:** `ai/LEDGER/challenges/CH-sahel-test-01-local-regulation-list.md`; `CH-sahel-test-01-comparable-dimensions.md`; `CH-sahel-test-02-primary-sources.md`.
- **What this means:** Later work should have to name what is being matched, and which regulation variables are being tested, before looking at held-out scores.

## 2026-11-21 — Work agent: Sahel bounded test plan (Round 5)

- **Agent:** Work (A)
- **What:** Proposed a blank six-step fill-in plan for the current Sahel paper’s bounded test. Withdrawn wording stays withdrawn. The unpromoted logistic addendum is not used as authority. No burden series is computed.
- **Why:** The paper already says the hypotheses remain available for testing. A later study needs a locked recipe that cannot quietly restore a “passed falsification” slogan.
- **Links:** `ai/PROPOSALS/2026-11-21-sahel-bounded-test-plan/proposal.md`; `Release/Examples/sahel_bounded_test_plan_v0.1.md`.
- **What this means:** Someone can later fill official locations, sources, and held-out tests against this sheet, or leave it blank if the evidence is not there, without treating the addendum as current theory.

## 2026-11-21 — Verifier: Bite 5 checklist accepted with revisions (Round 4)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the sheet is blank of scores. Applied a held-out metric-class rule, fired / did not fire / needs-evidence columns, and a locked hard-threshold list. Linked the sheet from the Central Valley README. Did not edit the v0.2 protocol or the HKL paper.
- **Why:** Leaving “any predeclared function” and an unsplit “weaken / reject” column would have let later work pick the test after seeing the index.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-hkl-bite5-falsification-checklist.md`; `Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md`.
- **What this means:** Bite 5 can still only be run after official study bounds and the locked metric and thresholds exist; missing evidence stays `needs-evidence`, not a pass.

## 2026-11-21 — Adversary: Bite 5 checklist challenges (Round 4)

- **Agent:** Adversary (B)
- **What:** Challenged the checklist for leaving the comparison metric too open, for using a single “weaken / reject” column when the protocol does not split those words, and for not locking the hard-threshold list before scoring HKL-4.
- **Why:** A falsifiability tightening that still lets someone pick the test after seeing the index is not yet tight.
- **Links:** `ai/LEDGER/challenges/CH-bite5-falsification-02-metric-class.md`; `CH-bite5-falsification-01-weaken-vs-reject.md`; `CH-bite5-falsification-01-hard-thresholds.md`.
- **What this means:** Later Bite 5 work still needs a locked held-out score and a locked threshold list, not just a blank box labeled “metric.”

## 2026-11-21 — Work agent: HKL Bite 5 falsification checklist (Round 4)

- **Agent:** Work (A)
- **What:** Proposed a blank score sheet that separates Temporal Mining weakening tests from HKL incremental-value tests, and lists patterns current HKL says are not automatic failures. No scores or weights were filled. The comparison metric is left to be locked before fitting.
- **Why:** Protocol Bite 5 already says to report failure as clearly as success. Writing the failure rules before any index is computed is the tightening.
- **Links:** `ai/PROPOSALS/2026-11-21-hkl-bite5-falsification-checklist/proposal.md`; `Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md`.
- **What this means:** A later study cannot quietly treat a temporary rise in burden, or a horizon with no observed exit, as a completed HKL failure or success.

## 2026-11-21 — Verifier: ebonyshell protocol accepted with revisions (Round 3)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed the sheet is blank of computed rates. Applied a life-stage/loss lock, a default rule that the 1986 episode stays out of the \(\eta^{nat}_{TM}\) numerator, a spatial-versus-impairment disclaimer, and a corpus note on the worked example’s uncomputed severed wording. Linked the protocol from the mussel README. Did not edit the example body or the registry.
- **Why:** A recipe that can be filled two ways is not yet a fair test. The example’s qualitative severed line is a standing-corpus tension a later human review should see.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-ebonyshell-renewal-coverage-protocol.md`; `Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md`.
- **What this means:** Someone can later fill official series against a locked convention, or leave the sheet blank if the data are not available, without pretending the example had already computed the ratio.

## 2026-11-21 — Adversary: ebonyshell protocol challenges (Round 3)

- **Agent:** Adversary (B)
- **What:** Challenged the protocol for leaving life stage and loss components unlocked until data arrive; for not saying whether the 1986 episode enters the \(\eta^{nat}_{TM}\) numerator; for a possible confusion between the above/below contrast and the registry’s same-reach sink-impairment counterfactual; and recorded that the original worked example already assigns the severed flag without a computed ratio.
- **Why:** A preregistration that can be filled two different ways is not yet an honest test recipe. The example’s qualitative severed line is a standing-corpus issue A correctly refused to treat as measured.
- **Links:** `ai/LEDGER/challenges/CH-ebonyshell-renewal-01-life-stage-lock.md`; `CH-ebonyshell-renewal-03-episode-in-numerator.md`; `CH-ebonyshell-renewal-01-spatial-vs-counterfactual.md`; `CH-ebonyshell-renewal-03-example-severed-uncomputed.md`.
- **What this means:** A later filler of this sheet could otherwise change the severed flag by how they treat one high-water year or by mixing recruit and adult counts.

## 2026-11-21 — Work agent: ebonyshell renewal-coverage protocol (Round 3)

- **Agent:** Work (A)
- **What:** Proposed a blank preregistration sheet for computing \(\eta^{nat}_{TM}\) and \(\eta^{tot}_{TM}\) for ebonyshell above and below Keokuk, using the already-registered definitions. No rates were filled. The example’s qualitative “effectively zero / severed” line is not treated as a computed result.
- **Why:** The mussel README and the 30 October decision record already list this comparison as the first application, if recruitment data exist. Writing the recipe without inventing the data keeps that open step honest.
- **Links:** `ai/PROPOSALS/2026-11-21-ebonyshell-renewal-coverage-protocol/proposal.md`; `Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md`; claims `C-ebonyshell-renewal-01` through `-04`.
- **What this means:** A later human or study can fill official windows and series against a predeclared sheet, or leave the sheet blank if the data are not available.

## 2026-11-21 — Verifier: consistency audit accepted with revisions (Round 2)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed F1–F4 on the box, including live Linux import failures. The official-vs-experimental challenge missed. The stale-citation challenge hit; finding F5 and a `src/README.md` status notice were added. No official paper was edited.
- **Why:** Claims have to be checked against the actual files and a real import, not against the audit’s wording alone. The addendum’s wrong section numbers are a standing-corpus issue a later human review should see.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-layer1-consistency-audit.md`; `ai/AUDITS/2026-11-21-layer1-consistency.md`; `src/README.md`.
- **What this means:** Experimental code in `src/` should not be cited as current PAE. The unpromoted Sahel addendum should not be read as if it extends the current Sahel and HKL papers.

## 2026-11-21 — Adversary: consistency audit challenges (Round 2)

- **Agent:** Adversary (B)
- **What:** Challenged the audit’s authority wording for F1, required a live import check for F2, and — most importantly — argued that F4 understates the unpromoted Sahel addendum’s stale citations: it points at “Sahel §5.1” and “HKL §5.1” formulas that the current papers do not contain, and it treats PAE as a number.
- **Why:** Jordan said the adversary may attack the standing corpus, not only A’s new text, as long as Layer 0 holds. The addendum is in-tree and can still be misread as extending current Sahel and HKL.
- **Links:** `ai/LEDGER/challenges/CH-layer1-consistency-01-authority-scope.md`; `CH-layer1-consistency-02-import-behavior.md`; `CH-layer1-consistency-03-stale-section-citations.md`; `CH-layer1-consistency-04-paper-edits.md`.
- **What this means:** A human reviewing later should look especially at whether the addendum is citing superseded drafts as if they were the current papers.

## 2026-11-21 — Work agent: Layer 1 / implementation consistency audit (Round 2)

- **Agent:** Work (A)
- **What:** Proposed a dated audit of specific repository mismatches: experimental `_apply_pae` treating expenditure as correction, import/filename mismatch and random scorers in `src/`, and withdrawn sign-change wording still used as an anchor in the unpromoted Sahel logistic addendum.
- **Why:** Jordan asked the AI line to take the framework from his definitions and to treat mistakes, including in the standing corpus, as fair game for later adversarial review. This cycle records concrete findings before new theory.
- **Links:** `ai/PROPOSALS/2026-11-21-layer1-consistency-audit/proposal.md`; `ai/AUDITS/2026-11-21-layer1-consistency.md`; claims `C-layer1-consistency-01` through `-04`.
- **What this means:** A human can now point at exact files where the experimental code or an unpromoted draft is out of step with the current definitions, without anyone having rewritten the official papers.

## 2026-11-21 — Verification agent: accept-with-revisions (Round 1)

- **Agent:** Verifier (C)
- **What:** Ran mechanical checks on the box (protocol §4 fidelity, invented-data scan, registry-file identity vs `c9e1277`, link checks, and a corpus run of `tank_model.py`). Posted verdict `accept-with-revisions` and applied the required fixes in this same commit: a status row and same-directory note so the Bite 1 filename is not mistaken for a finished deliverable; new schema rows for observed net storage change, streamflow capture, and `tau_d`; protocol §13 source *classes* without invented versions; and residual schema rows for `\epsilon_{D_W}`, climate covariates, and well metadata.
- **Why:** Two of the adversary’s hits landed on the substance of the schema, and the official filename could mislead. The proposal still does what it claimed not to overclaim: it is not a finished study and not a validation of the framework.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-freshwater-data-dictionary.md`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.NOTES.md`; `ai/LEDGER/index.md`; `ai/CHANGELOG.md`. Parent commits: [A] https://github.com/Causal5/Harmonic-Knowledge-Law/commit/cb3ea10655f6106fd2d0bc683860f4a574f8bb73 and [B] https://github.com/Causal5/Harmonic-Knowledge-Law/commit/8f21e7017bd2cd4d77585bb58ce233d1b44dd91b
- **What this means:** The branch now has a clearer spreadsheet of what has to be collected, with the dangerous gaps filled as empty rows rather than left implicit. Nobody has picked a map boundary or downloaded a time series yet. That is the next human or later-cycle job, and it still needs real official sources.

## 2026-11-21 — Adversarial agent: challenges to the freshwater dictionary (Round 1)

- **Agent:** Adversary (B)
- **What:** Committed five challenges, straight to `ai/evolution`, against
  the Round 1 dictionary claims. They ask whether net storage change and
  streamflow capture are really kept separate, whether `tau_d` and
  `tau_d_net` have been mixed, whether the official Bite 1 filename can
  mislead, whether already-named §13 source classes should have been
  recorded, and whether missing hydrologic-year rules, climate covariates,
  and well metadata bound the instrument even if claim 01 is read narrowly.
- **Why:** The work agent's claims needed to be tested, not polished. The
  protocol’s own wording is the standard, not a general sense that a
  schema is helpful.
- **Links:** `ai/LEDGER/challenges/CH-freshwater-data-dictionary-01-streamflow-net-storage.md`,
  `...-01-tau-d.md`, `...-01-scope-residue.md`,
  `...-04-deliverable-path.md`, `...-04-section13-sources.md`;
  `ai/LEDGER/index.md`. Parent proposal commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/cb3ea10655f6106fd2d0bc683860f4a574f8bb73
- **What this means:** A human should not take the new spreadsheet as a
  finished Bite 1 package. Several gaps are documented and waiting on the
  verifier: missing separations, a possible timescale mix-up, and a
  filename that looks more finished than the empty source boxes are.

## 2026-11-21 — Work agent: freshwater data dictionary schema (Round 1)

- **Agent:** Work (A)
- **What:** Committed the Bite 1 data dictionary schema straight to
  `ai/evolution` (status `proposed`). The file contents were first drafted
  on the discarded side-branch commit
  `6ca9701f75af4131ab37017004deda63bd64683e` and are landed here as a
  direct `[A]` commit, with no pull request. Added
  `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`,
  the proposal note, four claim files, and ledger rows.
- **Why:** The 16 October publication notes and protocol §14 already name
  the freshwater data dictionary as the immediate empirical step, and they
  require doing that before choosing HKL weights or collecting building
  anecdotes. This cycle records the required variables and separations
  without inventing measurements or completing source mapping.
- **Links:** `ai/PROPOSALS/2026-11-21-freshwater-data-dictionary/proposal.md`;
  `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`;
  claims `C-freshwater-data-dictionary-01` through `-04`;
  `ai/LEDGER/index.md`. Source draft commit (side branch, not this line):
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/6ca9701f75af4131ab37017004deda63bd64683e
- **What this means:** A human following this trail should see a spreadsheet
  of *what must be collected and kept distinct*, not a finished water study
  and not a claim that the framework has been tested. Official map
  boundaries and real data sources are still empty on purpose.

## 2026-11-21 — Setup: cycle is direct commits only

- **Agent:** setup (direct commit to `ai/evolution`; process change directed by Jordan)
- **What:** Changed the cycle from proposal-branch pull requests into
  `ai/evolution` to direct commits on `ai/evolution` only. Updated the
  cycle guide, the three agent files, the branch README, and the charter's
  process and ownership section. Layer 0 was not changed. Logged the rule
  in `ai/CHANGELOG.md`.
- **Why:** Jordan set a cardinal rule: work only on
  https://github.com/Causal5/Harmonic-Knowledge-Law/tree/ai/evolution,
  committing straight to that branch, with no pull requests and no other
  branches.
- **Links:** `ai/AGENTS/CYCLE.md`, `ai/AGENTS/work.md`,
  `ai/AGENTS/adversary.md`, `ai/AGENTS/verifier.md`, `ai/README.md`,
  `ai/CHARTER.md` (process section only), `ai/CHANGELOG.md`. `main` was
  not changed.
- **What this means:** From this point, a human following the branch will
  see proposal, challenge, and verdict commits land on `ai/evolution`
  itself, labeled `[A]`, `[B]`, and `[C]`. There should be no more
  `ai/proposal/...` side branches and no pull requests for this cycle.

## 2026-11-21 — Setup: branch README, license notice, and this trail

- **Agent:** setup (direct commit to `ai/evolution`, not a proposal cycle)
- **What:** Rewrote `ai/README.md` as the labeled AI-evolution branch guide;
  added a short banner at the top of the root `README.md` on this branch
  only; recorded the AGPL-3 license and a commercial-licensing contact
  path; created this trail; required a trail entry and a plain-English
  TL;DR on every proposal, challenge, and verdict.
- **Why:** Jordan asked that the branch be clearly labeled, that license and
  commercial-contact information be posted, and that “landmarks for the
  meat to follow” be left so a human can walk the history in order.
- **Links:** `ai/README.md`, root `README.md` (banner only), `ai/CHANGELOG.md`,
  `ai/AGENTS/CYCLE.md`, `ai/AGENTS/work.md`, `ai/AGENTS/adversary.md`,
  `ai/AGENTS/verifier.md`. No pull request. `main` was not changed.
- **What this means:** If you are reading this branch, start with
  `ai/README.md`. The science on `main` is unchanged. This trail is the
  running plain-English log of later agent cycles; the next entries will
  point at proposal pull requests, ledger files, and verdicts.
