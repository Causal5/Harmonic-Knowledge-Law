# CH-layer1-consistency-02-import-behavior

**TL;DR.** A looked at filenames and guessed the imports will fail on
Linux. That is a fair suspicion, but the claim’s own falsifier is about
whether a case-sensitive import actually works. The verifier has to run
it. If the imports succeed, the challenge hits. If they fail as predicted,
it misses.

- **Claim:** C-layer1-consistency-02
- **Challenge:** Finding F2 is stated as an import-behavior fact, but the
  proposal commit only observes a filename/module-name mismatch. Alternate
  import hooks, a package layout, or a case-insensitive check-out could
  still load the modules. F3 (random scorers) is independent and is not
  disputed here.
- **Hit if:** On a case-sensitive system, `from giln_ai import GILNNetworkAI`
  or `from iif_evaluator import IIFEvaluator` succeeds as written, or F2 is
  left as an untested filename remark presented as a demonstrated import
  failure.
- **Miss if:** A case-sensitive interpreter fails those imports as predicted,
  and the random-scorer citations in F3 are present as written.
