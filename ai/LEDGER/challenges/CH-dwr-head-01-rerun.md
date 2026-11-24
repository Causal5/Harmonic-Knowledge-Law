# CH-dwr-head-01-rerun

**TL;DR.** The offline replay must keep producing n_G=15 and a Good-quality median of 19.03 feet from the committed extracts.

- **Claim:** C-dwr-head-01
- **Challenge:** The protocol lock is only as good as the committed script and extracts. If `--offline` does not reproduce the decision statistics, the “locked before signed differences” story is unverifiable.
- **Hit if:** A clean `--offline` run fails to reproduce \(n_G=15\) or the Good-quality primary median of 19.03 feet, or if the pre-registration is missing from the tree.
- **Miss if:** The committed script, re-run offline, reproduces those statistics, and PREREG.md is present.
