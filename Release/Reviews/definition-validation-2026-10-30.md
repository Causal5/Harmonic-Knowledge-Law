# Definition validation — 30 October 2026

This record covers Registry v0.3.2 and its
[decision record](../Registry/definition-decisions-2026-10-30.md).

| Check | Result |
|---|---|
| Realized and attributed balance forms (decision record §1) | Equal to floating-point precision across 10,000 random cases with unclipped differences; mixing the forms double counts by exactly the impairment term |
| Tank model, pathway restored (§8) | Simulated equilibrium 0.8333 matches $K(1-m/(bv))=0.8333$ |
| Tank model, substitution continuing | Simulated level 0.334 at $t=150$ approaches the exact equilibrium 0.3333; the low-stock approximation $P/|r|=0.5$ overstates it at these parameters, as the record notes |
| Tank model, substitution stopped | Stock 0.367 at $t=60$ falls to 0.042 by $t=150$ |
| Half-lives in the figure | $\ln 2/|r|$ = 8.7, 23.1, and 69.3 years for $r$ = −0.08, −0.03, −0.01 per year |
| Relative links in the 12 changed or added Markdown files | All resolve; one pre-existing URL-encoded link in `Release/README.md` resolves on GitHub |
| Inline math delimiters in the registry and decision record | Balanced |
| v0.3.1 definitions | Unchanged, including ACR; the extended ratio $\mathrm{ACR}^{ext}$ is a separate quantity that equals ACR when no impairment is declared. Additions are confined to the registry header, §V note, §VI.1, §VII.1, and §X |
| Renewal statuses | Net mining, substituted, and covered partition all $(\eta^{nat}_{TM},\eta^{tot}_{TM})$ with $\eta^{tot}_{TM}\ge\eta^{nat}_{TM}$; the severed flag occurs only with net mining or substituted |
| Figure scenarios | Predation terms $s_r$ and $c_a$ are zero in all plotted scenarios, as the caption states |

These checks confirm internal consistency and reproducibility of the figure.
They are not empirical validation of HKL or of any worked example.
