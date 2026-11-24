# Theory multi-armed bandit (MAB) registry

**24 November disposition for ARM-05.** The [study boundaries](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/f81967de6cca7062133fa1e28f2304e17e27f314/Release/Examples/central-valley/README.md#study-boundaries-adopted-24-november-2026) are fixed. The [public-data inventory](../Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/DWR-COVERAGE.md) found paired DWR records and a calendar-year/water-year break in pumping totals. Continue source matching and uncertainty accounting. Bite 5 scoring remains at `wait` pending matched series and prespecified limits, weights and held-out comparisons.

**Launch Pad Session 1 (24 November 2026, Rounds 20–24).** ARM-05 stays `wait`. Boundaries and a DWR signed head contrast are now in hand, but weights, a held-out metric, and a zone-locked volume conversion are not, and Round 24 shows that Table 3-1 totals do not instantiate \(Q_{sw}\) or \(D_W\). ARM-06 and ARM-07 are opened at `wait` and are not developed. Bite 5 remains unscored. \(V\) was not constructed.

**Status:** accepted-with-revisions (Round 16 / Session 3). Ratification-pending as a process aid on `ai/evolution`. It is not Layer 0, not a registry amendment, and not an official HKL primitive. It is not a fitted bandit algorithm and it does not assign numeric rewards.

**Opened:** 2026-11-21, America/New_York (Session 3, Round 16), after four worked-example rounds (12–15).

## TL;DR

Jordan asked that if base theory moves forward, it be fashioned like a multi-armed bandit: first assess whether it is beneficial to explore from a premise. This file is the arm registry and assessment log. Candidate premise extensions are arms. An assessment — expected information value, cost, risk to Layer 0, falsifiability, and worked-example evidence as a qualitative reward signal — is written **before** an arm is developed. Worked-example results from Rounds 12–15 are used as that signal. In this opening cycle, four arms are dropped and one is marked wait. **No arm is developed here.** Layer 0 is unchanged.

## How an assessment is written (before any development)

Each arm record has:

1. **Premise / arm.** The candidate extension, in one paragraph.
2. **Expected information value.** What would be learned if the arm were explored, and whether that knowledge is required to proceed under Layer 0.
3. **Cost.** Data, protocol locks, and review burden.
4. **Risk to Layer 0.** Whether exploring it would quietly rewrite v0.3.1, invent primitives, restore withdrawn claims, or treat application quantities as universal.
5. **Falsifiability.** What observation would drop the arm later.
6. **Worked-example reward signal.** Qualitative only, taken from retrieved and computed Session 3 results (and standing Session 1–2 constraints). Not a numeric score.
7. **Decision.** `explore`, `exploit`, `wait`, or `drop`, with a date. `exploit` would mean developing a already-supported arm; none is in that state here.

Do not develop an arm in the same cycle that first assesses it, unless Jordan directs otherwise. A `drop` or `wait` is a complete outcome. A `wait` is not an `explore` and is not permission to score Bite 5, choose weights, or construct \(V\). It expires only after a new assessment written when the missing official series and predeclarations are actually in hand. “Reward signal” in this file is qualitative prose, not a computed score, prior, or regret bound.

## Round 17 note (2026-11-23)

Round 17 opens `ai/GLOSSARY.md` as a terminology map / erratum against Registry v0.3.2 and the reconciled papers. It invents no definitions, restores no withdrawn claims, and does not extend the premise. It is therefore **not registered as an arm** and no arm is developed in that cycle.

## Round 18 note (2026-11-23)

Round 18 records Jordan’s source-precedence rule (`Release/` on `main` is primary; everything else is subject to obsolescence) and rechecks the glossary against that tree. It invents no definitions and does not extend the premise. It is **not registered as an arm** and no arm is developed in that cycle.

Round 19 is a clarification and correction sweep after `main` moved to `270942c`. It invents no definitions, develops no arm, and does not extend the premise. It is **not registered as an arm**.


## Launch Pad Session 1 note (2026-11-24)

Rounds 20–24 are pre-registered stress tests of the current Release model. Two held, two were indeterminate, and one broke as a scope / object-class limit (Table 3-1 totals). No arm is developed in this session. ARM-05 is reassessed below and stays `wait`. ARM-06 and ARM-07 are assessed for the first time and marked `wait`. A `wait` is not permission to score Bite 5, choose weights, construct \(V\), or invent a mixed surface-water symbol.

## Arm records

### ARM-2026-11-21-01 — Spatial above/below Keokuk contrast as sink-impairment

- **Premise / arm.** Treat a spatial contrast of ebonyshell (or hosts) above versus below Lock and Dam 19 as the registry’s same-reach sink-impairment counterfactual.
- **Expected information value.** Low under present rules: the ebonyshell protocol already says the above/below contrast is spatial, not automatic sink-impairment. A new premise would mainly relabel a contrast the protocol already refuses to treat as impairment.
- **Cost.** Would require rewriting a locked protocol distinction and new same-reach counterfactual data that have not been retrieved.
- **Risk to Layer 0.** Medium-high: it would blur a documented application distinction and invite treating an application contrast as a universal impairment rule.
- **Falsifiability.** A retrieved same-reach (dam-absent vs dam-present) recruitment series could still be used under the existing protocol without this arm.
- **Reward signal.** Round 12 filled dam status and discharge context and still found no recruitment series, so \(\eta\) and *severed* remain unassigned. That does not reward a shortcut from spatial contrast to impairment.
- **Decision (2026-11-21):** `drop`. Do not develop.

### ARM-2026-11-21-02 — uADS or ICRCC carp-passage figures as host-passage or \(\eta\)

- **Premise / arm.** Treat official uADS effectiveness, or the ICRCC “about 50 percent” reduction in Silver Carp and Bighead Carp passage, or native-fish behavioral results, as evidence of host-fish passage or ebonyshell \(\eta\).
- **Expected information value.** Low: those quantities are about an invasive-carp deterrent, not pathway-restoring host access for ebonyshell.
- **Cost.** Low to quote, high if allowed to substitute for \(\eta\).
- **Risk to Layer 0.** High if a carp-deterrent result became a renewal-ratio or correction result.
- **Falsifiability.** The ICRCC sentence is already plural (“these dam structures”) and covers BAFF plus uADS; detailed results were still forthcoming in 2026–2027 in the retrieved plan.
- **Reward signal.** Round 12 retrieved those records and declined to use them as \(\eta\) or as a Keokuk fish-passage result. The official project at Lock 19 is a deterrent, not a fish passage.
- **Decision (2026-11-21):** `drop`. Do not develop.

### ARM-2026-11-21-03 — Score Bite 5 / \(V_W\) now on 5-022.12 or “the” Central Valley

- **Premise / arm.** Using currently retrieved USGS field measurements and/or the published CVHM2 “approximately 158 km³” figure, score Bite 5 or compute \(V_W\) for Tulare Lake 5-022.12 or for the Central Valley, with weights chosen now.
- **Expected information value.** Low now: a score without locked official study-boundary choice (among official options), hydrologic-year convention, weights, and a held-out metric would not be a Bite 5 test.
- **Cost.** High review cost and a high chance of having to withdraw the score later.
- **Risk to Layer 0.** High: ad-hoc weights and a mixed model-output / sparse-well score could be mistaken for validation.
- **Falsifiability.** The Round 4 checklist already states what must be locked first.
- **Reward signal.** Round 13: locked 5-022.12 contrast of USGS 72019 spring 2015 vs 2024 returned **n=0** qualifying wells (coverage, not “no change”); DWR/CASGEM not retrieved; 158 km³ is an abstract quotation for a larger domain through 2019, not a 5-022.12 2015–2024 head change.
- **Decision (2026-11-21):** `drop` as a present-tense scoring arm. Do not develop a score now.

### ARM-2026-11-21-04 — Construct Sahel \(V\) or restore \(dV/dt\) sign-change from WDI series

- **Premise / arm.** Use the official Niger precipitation climatology (151.0 mm/year) and/or national cereal yield (1961–2022) to construct \(V\) or to restore the withdrawn claim that \(dV/dt\) measurably flipped sign, or that the framework passed a falsification test.
- **Expected information value.** Low: those series do not fill comparable locations, interannual rainfall, or steps 1–5 of the bounded test.
- **Cost.** Low to misuse, high to unwind.
- **Risk to Layer 0.** High: it would restore withdrawn wording and skip the locked step order.
- **Falsifiability.** Current Sahel §5 already withdraws the completion claims; the plan forbids \(V\) before steps 1–5.
- **Reward signal.** Round 14: AG.LND.PRCP.MM is a repeated national long-term average, not interannual site rainfall. Round 15: cereal yield is interannual but is not rainfall and not an FMNR result. CHIRPS was not retrieved. Comparable locations remain UNFILLED-REQUIRED.
- **Decision (2026-11-21):** `drop`. Do not develop.

### ARM-2026-11-21-05 — Later dictionary fill once DWR/CASGEM (or equivalent) and predeclarations exist

- **Premise / arm.** After official water-level or storage series with usable coverage (for example DWR/CASGEM/SGMA, or a denser USGS product), and after official study-unit, hydrologic-year, weights, and held-out metric are locked, fill dictionary fields and only then assess whether a Bite 5 / application test is informationally worth running.
- **Expected information value.** Potentially high *later*, because Rounds 13–15 show that the missing inputs are coverage and predeclarations, not a need for a new primitive.
- **Cost.** High (data retrieval, boundary choice among official options, weight lock). Worth paying only after those locks exist.
- **Risk to Layer 0.** Low if the existing checklist and inheritance firewall are kept; high if exploration starts by inventing weights.
- **Falsifiability.** If retrieved official series still cannot support a locked contrast, the arm stays at wait or drops; it does not become a score of zero change.
- **Reward signal.** Round 13’s n=0 and unretrieved DWR series, plus Jordan’s still-open official CV/SJV boundary question, say “not yet,” not “explore now.”
- **Decision (2026-11-21):** `wait`. Do not develop in this cycle. Re-assess only after the missing official series and predeclarations are actually in hand.

- **Reassessment (2026-11-24, Launch Pad Session 1).** Study boundaries are now locked (USGS CVHM2 footprint, the 19 Bulletin 118 5-022 subbasins, and Tulare Lake 5-022.12 for the pilot). Round 20 supplies a locked DWR Good-pair sign contrast (fall 2019–2025 holds; the spring companion, not the decision, has the opposite sign). That is not a volume conversion, not a spatially weighted subbasin head, and not a held-out metric. Round 24 shows that Table 3-1 totals cannot be assigned to \(Q_{sw}\) or \(D_W\) under published labels. Weights, a held-out comparison, and a zone-locked volume conversion remain missing.
- **Decision (2026-11-24):** `wait`. Do not develop. Do not score Bite 5.


### ARM-2026-11-24-06 — CHIRPS (or equivalent) at predeclared Sahel step-1 locations

- **Premise / arm.** After Sahel bounded-test step 1 locations are predeclared, use a pre-locked rainfall product (for example CHIRPS v2.0) at those locations as an environmental precursor series. Round 21 already shows that a Niger national CHIRPS mean is interannual (CV 0.171) while WDI AG.LND.PRCP.MM is a repeated 151 mm climatology. That national-mean result is not a license to construct \(V\) or to pick locations after seeing the maps.
- **Expected information value.** Potentially high *later*, once locations are locked, because a climatology series cannot support an interannual precursor test and CHIRPS can.
- **Cost.** Moderate once locations are predeclared; high if location choice is left open and becomes a fishing expedition.
- **Risk to Layer 0.** High if locations are chosen post hoc or if a national mean is treated as a site contrast. Low if step 1 is locked first and withdrawn Sahel claims stay withdrawn.
- **Falsifiability.** If predeclared locations still cannot support a locked contrast (coverage, missing years, or an unusable polygon), the arm stays at wait or drops; it does not restore withdrawn claims.
- **Reward signal.** Round 21 holds the “WDI is not interannual” diagnosis and also shows that a national mean leaves step 1 unfilled.
- **Decision (2026-11-24):** `wait`. Do not develop until step 1 locations are predeclared.

### ARM-2026-11-24-07 — Independent \(C_{irr}\) for the Tulare temporal-mining signature

- **Premise / arm.** Lock an irreversible-compaction or storage-capacity-loss series that is independent of the InSAR already used in v0.2 C-zone storage (for example an extensometer or another product not already in that storage calculation), and only then test whether the protocol §5 conjunction is completable.
- **Expected information value.** High *later*, because Round 23 shows the public WY 2025 filing cannot complete the signature under the independence rule.
- **Cost.** High (source identification, overlap check against the v0.2 C-zone inputs, window lock).
- **Risk to Layer 0.** High if the same InSAR is reused as if it were independent, or if deliveries are used to declare the signature fired or failed without both limbs. Low if the independence rule is kept and the signature stays unassigned until both limbs lock.
- **Falsifiability.** If no independent public series can be locked, the arm stays at wait or drops; that is not a finding that the signature failed.
- **Reward signal.** Round 23 is indeterminate (no independent \(C_{irr}\)). Round 24 further shows that Table 3-1 totals are not a locked \(D_W\).
- **Decision (2026-11-24):** `wait`. Do not develop until an independent series is actually in hand. Do not evaluate the conjunction now.

## What this file does not do

- It does not change Layer 0 or rewrite v0.3.1.
- It does not invent a numeric reward, prior, or exploration rate.
- It does not develop any arm in the opening cycle or in Launch Pad Session 1.
- It does not treat “wait” as a hidden go-ahead to score Bite 5, choose weights, construct \(V\), or invent a mixed surface-water symbol.
