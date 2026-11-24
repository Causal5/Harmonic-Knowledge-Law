# CH-chirps-01-rerun

**TL;DR.** A clean `--offline` run must reproduce CV 0.171 and the 71.94–190.45 mm range.

- **Claim:** C-chirps-01
- **Challenge:** If the committed extracts and script do not replay the decision statistics, the lock-before-compute story is unverifiable.
- **Hit if:** `--offline` fails to reproduce outcome `holds`, CV 0.171 (to three decimals), min 71.94 mm, or max 190.45 mm.
- **Miss if:** The replay matches those figures and PREREG.md is present.
