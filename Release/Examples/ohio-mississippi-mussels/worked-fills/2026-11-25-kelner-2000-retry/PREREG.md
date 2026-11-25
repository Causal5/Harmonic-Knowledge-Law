# Pre-registration: Kelner and Sietman (2000) legitimate-route retry

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 29, 25 November 2026).** Not a publication to `main`. Written before this retry scored a full-text outcome, and before any fallback test was scored.

**TL;DR.** Round 22 left \(\eta\) unassigned because the Kelner and Sietman (2000) full text was not retrieved and the available texts lacked recruitment and loss rates. This round retries the full text by legitimate routes only. If the full text cannot be obtained, the Kelner test is not scored as a theory result; the round instead runs the predeclared fallback below. Sahel step-1 sites will not be invented. ARM-06 stays `wait`. A1–A8 remain undefined.

**Parents.** Round 22 fill and pre-registration; ebonyshell protocol for \(\eta^{nat}_{TM}=R^{nat}_s/L_s\); `main` at `37522fc`.

## Stage 1 — Kelner full-text retry

**Paper.** Kelner, D. E., and B. E. Sietman. 2000. Relic populations of the ebony shell, *Fusconaia ebena* (Bivalvia: Unionidae), in the Upper Mississippi River drainage. *Journal of Freshwater Ecology* 15(3). DOI [10.1080/02705060.2000.9663755](https://doi.org/10.1080/02705060.2000.9663755).

**Legitimate routes (only these):** author or co-author manuscript or preprint; institutional repository or university profile copy; USGS or other agency reprint; Google Scholar or publisher versions that are openly offered; library or interlibrary-style copies that are already public without login. Paywall circumvention, credential sharing, and shadow libraries are forbidden. A 403 or a subscription HTML page is not a retrieval.

**Limb A (retrieval).** Holds if a full-text copy of this paper is retrieved by one of those routes, hashed, and excerpted. Fails if those routes are exhausted and no full text is in hand.

**Limb B (rates), scored only if Limb A holds.** Holds only if the retrieved text supplies a declared-window natural recruitment rate and a gross loss rate for ebonyshell that can be locked to a stated reach (Keokuk / LD 19, or the paper’s own stated reach) without inventing a window, life stage, or value. Qualitative relic or host-blockage language is not a rate.

**Stage 1 outcomes.**

- **Holds** if Limb A and Limb B both hold. Then, and only then, \(\eta\) may be computed under the existing protocol. Computing it is not validation.
- **Indeterminate** if Limb A holds and Limb B fails (the paper is in hand but does not supply both rates). Cause: data gap in the paper. \(\eta\) and *severed* stay unassigned.
- **Breaks** (procedure) if flags are assigned without both rates, or if a non-legitimate copy is used.
- If Limb A fails, Stage 1 is **unobtainable**. Do not treat that as a finding that the paper lacks rates (Round 22 already recorded that limit). Proceed to Stage 2.

## Stage 2 — fallback, used only if Stage 1 is unobtainable

**Fallback test.** Resume the Round 24 gap: can a public GSP or annual-report Appendix D, or an equivalent official methods/notes attachment for Tulare Lake 5-022.12, be retrieved and used to lock or reject the ex-Imported Table 3-1 subset as dictionary \(Q_{sw}\)?

**Locked rule (copied from the Round 24 pre-registration, not rewritten after seeing a new appendix).** The sum of Kings, Kaweah, Tule, Deer, Poso, SWP, and CVP, excluding Imported, is a locked \(Q_{sw}\) only if the retrieved official notes describe those columns as surface-water sources with no groundwater mixing and document the conveyance-efficiency correction as a number or method that can be applied without invention. A retrieved appendix that shows groundwater mixing in that subset **breaks** the candidate as \(Q_{sw}\). If the appendix or equivalent official notes cannot be retrieved, or retrieved notes still leave the correction or mixing unstated, the candidate stays unfilled and Stage 2 is **indeterminate** (data gap). The subset is not \(D_W\) unless the notes declare it as delivered service within a stated tolerance. This fallback does not invent Sahel sites, does not develop ARM-06, and does not evaluate the temporal-mining conjunction.

Stage 2 is not opened unless Stage 1 is unobtainable. Its sources are not scored until that switch is recorded.

## What this test will not do

- Circumvent a paywall or use a shadow copy.
- Invent recruitment or loss rates, or treat qualitative language as a rate.
- Invent Sahel step-1 locations, or move ARM-06 off `wait`.
- Use A1–A8 as if defined.
- Edit `main`.
