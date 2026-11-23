# CH-prec-02-glossary-already-aligned

**TL;DR.** The glossary’s Round 18 amendment correctly describes the published mussel example on `main` in A8, but the inventory at the bottom of the same file still calls that example “already aligned.” That leftover list treats the branch rewrite as if it were the official text.

- **Claim:** C-prec-02
- **Challenge:** `ai/GLOSSARY.md` was only partly re-based against `Release/` on `main`. A8 and section B1 now say that the published example on `main` still contains the qualitative *severed* assignment at §8 item 3 (line 152), and that the Round 7 rewrite is unpublished branch work. Two later passages were not updated and say the opposite:

  1. The treatment table (line 22) still lists “Already-corrected examples, `src/_apply_pae`, mussel §8, Sahel addendum marks” as “Inventoried as already aligned.”
  2. Section C (lines 173–178), headed “Already aligned; not rewritten in this cycle,” still lists “unpromoted logistic addendum marks (Round 7)” and “Mussel example §8 item 3 and ebonyshell protocol §1 (Rounds 7–8, 12)” as already aligned. The residual-risk bullet (line 184) still says ordinary-language “severed” was “left in the official example body,” which collapses the line-40 host-fish sentence (both branches) with the still-published `main` flag-assignment sentence that A8 just distinguished.

  On `main`, mussel §8 item 3 still assigns the flag qualitatively, the Sahel addendum is unmarked, and the ebonyshell protocol does not exist. Calling those paths “already aligned” cites the branch copies as the official example text. C-prec-02’s falsifier includes a glossary entry that cites a non-`Release/` or non-`main` source as canonical when `Release/` on `main` says otherwise. No new definition should be invented to fix this; the inventory should be re-based the same way A8 was.

- **Hit if:** The treatment table or section C still calls the mussel §8 rewrite, the Sahel addendum marks, or the ebonyshell protocol “already aligned” official or published example text, without distinguishing `main` from the branch.
- **Miss if:** Those inventory lines already treat those edits as unpublished branch work, and already record that the published example on `main` still contains the qualitative *severed* sentence.
