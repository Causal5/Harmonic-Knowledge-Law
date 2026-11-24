# Round 21 — CHIRPS vs WDI Niger rainfall stress test

**TL;DR.** CHIRPS v2.0 national-mean annual rainfall for Niger, 1981–2022, has CV 0.171 (71.94–190.45 mm). WDI is 151 mm every year. The pre-registered test **holds**: WDI is not an interannual series. The CHIRPS national mean is not a comparable-location series and was not used to construct \(V\).

**Status:** accepted-with-revisions (Round 21 [C]), Launch Pad Session 1. Parents: [Sahel worked example](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/sahel_worked_example.md) on `main`; Round 14 WDI fill; [empirical review procedure](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/empirical-review-procedure.md).

**Evidence.** [PREREG](../../../Release/Examples/sahel/worked-fills/2026-11-24-niger-chirps/PREREG.md) · [Fill](../../../Release/Examples/sahel/worked-fills/2026-11-24-niger-chirps/WORKED_FILL.md) · [Series](../../../Release/Examples/sahel/worked-fills/2026-11-24-niger-chirps/outputs/niger_chirps_v2_national_mean_1981-2022.csv)

- [C-chirps-01](../../LEDGER/claims/C-chirps-01.md): protocol locked before the national mean was computed; `--offline` replays it.
- [C-chirps-02](../../LEDGER/claims/C-chirps-02.md): outcome is holds (CV 0.171); \(V\) and withdrawn claims were not restored.

**Verdict:** [V-2026-11-24-niger-chirps](../../LEDGER/verdicts/V-2026-11-24-niger-chirps.md)
