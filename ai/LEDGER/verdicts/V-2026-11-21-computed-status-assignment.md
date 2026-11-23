# V-2026-11-21-computed-status-assignment

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. The procedure is an `ai/` note. It applies the 30 October / Registry test, which is on `main`. It referred to a mussel-example rewrite that is not on `main`. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** The branch may keep a procedure that says a flag defined by
a computed quantity cannot be assigned from a qualitative story. It is
not a registry amendment and no values were computed. All three
challenges hit and were fixed: the heading no longer sounds like
adopted official vocabulary; ordinary-language uses of the same word
are out of scope; and the protocol must be locked before the series
are inspected or the flag is assigned.

**Proposal:** `ai/PROPOSALS/2026-11-21-computed-status-assignment/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-computed-status-01-rule-sounds-official | C-computed-status-01 | hit | “Rule” could be read as adopted vocabulary. Heading changed to “procedure”; official-vocabulary warning added. |
| CH-computed-status-01-ordinary-language | C-computed-status-01 | hit | Scope did not clearly spare descriptive uses of the same word. Ordinary-language limit added. |
| CH-computed-status-02-lock-before-assignment | C-computed-status-02 | hit | “Locked protocol” did not require locking before inspection. Pre-lock requirement added. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-computed-status-01 | accepted-with-revisions | Still no new primitive; wording no longer reads as already adopted. |
| C-computed-status-02 | accepted-with-revisions | Qualitative assignment still barred; pre-lock added; no quantity filled. |
| C-computed-status-03 | accepted | Official papers untouched; no validation claim. |

## Mechanical checks (this box)

- [A] `7350a97` touched only `ai/` proposal, note, claims, ledger, and trail.
- The note still computes no $\eta$, $V$, or Sahel series.
- Ratification-pending banner remains. Mussel example body was not rewritten in this cycle.
