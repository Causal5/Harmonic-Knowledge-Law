# C-sahel-test-01

**TL;DR.** The plan follows the current Sahel paper’s six steps, in
order, and does not build a burden score until the last step. If a step
is skipped or a new kind of quantity appears, the claim fails.

- **Proposal:** `ai/PROPOSALS/2026-11-21-sahel-bounded-test-plan/`
- **Statement:** The plan restates the current paper’s six steps in order, forbids constructing \(V\) before step 6, and adds no new primitive.
- **Falsifier:** A step is omitted or reordered, \(V\) is constructed earlier, or a new primitive appears.
- **Status:** proposed
