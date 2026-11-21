# CH-sahel-test-01-local-regulation-list

**TL;DR.** Step 5 is supposed to test whether *declared* local-regulation
variables improve held-out results. The plan locks a baseline list for
step 4, but it never requires the local-regulation variable list itself
to be locked before that test. If those variables can be chosen after
seeing the held-out score, the challenge hits.

- **Claim:** C-sahel-test-01
- **Challenge:** “Declared local-regulation variables” are the treatment
  in step 5. A predeclaration that names only the baseline, and not those
  variables, leaves the actual test unlocked.
- **Hit if:** The committed plan does not require a locked local-regulation
  variable list before step 5 may be scored.
- **Miss if:** That list is already a required, locked predeclaration.
