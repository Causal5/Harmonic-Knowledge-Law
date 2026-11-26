# Session 3 pre-registration — claim-table rescoping

**TL;DR.** This session extracts simple claims from the published worked examples and the existing stress-test record, tables them in Jordan's five-column format, attacks each row, and rules it. It does not develop theory arms, invent studies, or treat the core axiom as a thing to break. Rulings come only after this protocol is committed.

**Status:** proposed. Launch Pad Session 3, step A. Authorized under Jordan's t22u–t23u rescope (hobby work that builds systems thinking on specialists' published studies; simple claims, each backed by others' work).

**Branch and precedence.** Direct commits to `ai/evolution` only. No pull requests, no other branches, never `main`. `Release/` as published on `main` (currently `37522fc`) is primary; if wording conflicts, that copy wins. A commit on this branch is not a publication to `main`.

## What this session is

Jordan re-scoped the work: HKL is a hobby; he does not produce new field data; he uses specialists' published studies as baselines for simple statements. Worked examples should distill to simple claims tied to the framework. The model row is:

> Claim | best-fit study among those already reviewed | what it shows | its limit | link

His exemplars are the Paani Water Cup (organized watershed works tracked against wells and planting; limited by selection of high-performing villages), Modesto (applied water moving through soil layers), Oro Grande Wash (recharge taking about three years to a water table 117 m below ground; limited by nearby pumping), and Kraemer Basin (a particular basin reaching particular wells, with repeat travel times agreeing).

This session is **claim-table rescoping**, not a Layer 0 stress test and not a THEORY_MAB development cycle. It does not increment the R20–R29 holds / breaks / indeterminate scoreboard. A1–A8 stay undefined. No invented data, citations, or definitions.

## Scope of extraction

Extract simple claims each of the following makes or implies about the framework:

1. Central Valley worked example v0.2 / Tulare Lake (published `Release/` text).
2. Paani hydrological PAE page (published).
3. Ohio–Mississippi mussel / Keokuk worked example (published text on `main` wins if the branch copy conflicts).
4. Sahel worked example (published; withdrawn wording stays withdrawn).
5. Branch worked fills and R12–R29 / STRESS_TESTS outcomes, used as **support and limits** on those claims, and as a source of additional simple claims only where the fill itself already states a result (for example the DWR sign windows, the Table 3-1 mapping, or the independent \(C_{irr}\) search).

Do not invent a claim the current work does not already make or clearly imply. Prefer the published wording, narrowed if a later fill has already shown a tighter object class.

## Method (A → B → C)

**A (this commit and its companions).** For each in-scope example, list candidate rows in the five-column format, plus a **Support** column that records only existing work: already-cited published sources, R12–R29 results, and STRESS_TESTS outcomes. No rulings. No new studies.

**B.** Attack each row for:

- overreach (the claim is stronger than the study),
- a mislinked study (the link or paper is not about what the claim says),
- a missing limit,
- a claim that needs an undefined A1–A8 term.

**C.** Rule each row as one of: `supported` / `supported-with-limit` / `partial` / `unsupported` / `needs-definition`. Narrow wording where needed rather than dropping a claim. Check that every link resolves and that the retrieved source says what is claimed. Suggest a better best-fit study only if that study's existence is verified in this session. Write the master table to `ai/CLAIMS.md`, with a plain-English TL;DR, counts by ruling, and a short note per example.

## Pre-registered constraints

- Do not treat the core axiom as breakable in this session.
- Do not restore Sahel wording that the published page withdraws (dV/dt “flipped sign,” “passed a falsification test,” or a calibrated \(V\) / \(\lambda_{\mathrm{PAE}}\)).
- Do not treat winter (rabi) planted area as \(D_W\) (Round 26 Limb B already broke that object class).
- Do not treat WY 2025 Table 3-1 totals as \(Q_{sw}\) or \(D_W\) (Round 24).
- Do not treat shared InSAR / C-zone storage as independent \(C_{irr}\) (Rounds 23 and 28).
- Do not assign ebonyshell \(\eta\) or the flags *severed*, *net mining*, or *substituted* (Rounds 22 and 29).
- Do not claim the unretrieved Kelner and Sietman (2000) paper lacks rates; claim only that retrieved texts do not supply them.
- Do not use 85% irrigation efficiency as a locked conveyance correction (Round 29).
- Do not use undefined A1–A8 terms as if they had been defined.
- When citing the Tulare DWR sign result, name all three lag-justified windows (Round 27), not only the windows that hold.
- Qiaozigou: do not treat the “already during the hillside work” timing clause as verified (Round 25 residual gap).
- Regional Central Valley or San Joaquin Valley findings do not automatically become Tulare Lake 5-022.12 results.

## Deliverable and landmarks

- Master table: `ai/CLAIMS.md` (written at step C, after the attack).
- A-step extraction (no rulings): `EXTRACTION.md` in this proposal folder.
- Ledger claims: `C-claims-01` (this protocol locked before rulings) and `C-claims-02` (the extracted table, to be ruled at C).
- Trail, ledger index, changelog, and a verdict after C. THEORY_MAB arms are not developed.
