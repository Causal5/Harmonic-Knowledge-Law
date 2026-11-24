# C-chirps-01

**TL;DR.** The hold/break rule, the 1981–2022 window, and the Natural Earth Niger polygon were written down before the CHIRPS national mean was computed. Standard-library `--offline` replay reproduces the decision statistics.

**Status:** accepted.

**Falsifier.** Show that the pre-registration was written after the series was computed, or that `--offline` does not reproduce CV 0.171, min 71.94 mm, max 190.45 mm, and outcome `holds`.

**C outcome:** accepted. Offline replay reproduced CV 0.171, min 71.94 mm, max 190.45 mm, outcome holds. CH-chirps-01-rerun misses.
