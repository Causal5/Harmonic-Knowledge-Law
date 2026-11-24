# C-dwr-head-01

**TL;DR.** The hold/break rule and the October–November 2019 vs 2025 window were written down before signed paired differences were computed. The committed script replays the result from the committed extracts.

**Status:** accepted.

**Evidence.** [PREREG.md](../../../Release/Examples/central-valley/worked-fills/2026-11-24-tulare-dwr-head-contrast/PREREG.md); `python3 scripts/compute_tulare_dwr_head_contrast.py --offline`.

**Falsifier.** Show that the pre-registration was written after the signed results, that the decision window was changed after seeing signs, or that `--offline` does not reproduce \(n_G=15\) and a median of 19.03 feet.

**C outcome:** accepted. Offline replay reproduced \(n_G=15\) and median 19.03 ft. CH-dwr-head-01-rerun misses.
