# Application-quantity inheritance firewall v0.1

> **Adoption, 24 November 2026.** The [published research procedure](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/f81967de6cca7062133fa1e28f2304e17e27f314/Release/Examples/empirical-review-procedure.md) records the approved scope. This file preserves the proposal reviewed on `ai/evolution`.

**TL;DR.** Some later definitions were born in a particular example — for
instance renewal coverage and the severed flag in the mussel case, or
sink-impairment accounting. This note is a decision sheet for when those
*application* quantities may be used in a new domain. It does not add
new primitives, does not rewrite Registry v0.3.1, and does not promote
v0.3.2. Three trial uses are classified: one is not eligible, two need
an explicit mapping before anyone computes a number.

**Status:** accepted-with-revisions (Round 6). **Adopted 24 November 2026
as a research procedure** (see `Release/Examples/empirical-review-procedure.md`
on `main` at `56c6ab5`). This is not a registry amendment, not a
promotion under `Release/ARCHITECTURE.md`, and not adopted Layer 1
definition vocabulary. The worksheet labels have procedural status only.

Parents: `Release/Examples/README.md` (“Application quantities do not
become universal primitives by appearing in an example.”);
`Release/ARCHITECTURE.md`; `ai/CHARTER.md` Layer 0; 16 and 30 October
decision records; Round 2 findings F4–F5; Round 3 ebonyshell protocol;
v0.2 freshwater protocol §6.1.

## 1. Why this note exists

v0.3.2 adopted several quantities from the mussel worked example
(renewal coverage \(\eta^{nat}_{TM},\eta^{tot}_{TM}\), the severed flag,
OIE temporal classes, sink impairment, corrective dependency,
\(\mathrm{ACR}^{ext}\)). The freshwater protocol already has related but
not identical tools (\(\rho_{TM}\), draw time, net-depletion estimates).
The unpromoted Sahel addendum invented a “basin-maintenance margin”
citing superseded section numbers. A later user can easily treat any of
these as if they were Layer 0 law. This note is a procedure, not a new
law.

## 2. Decision statuses (research-procedure labels, not Registry vocabulary)

These three labels are **research-procedure worksheet labels** adopted
24 November 2026 (see `Release/Examples/empirical-review-procedure.md`).
They are not Registry terms and not Layer 1 definitions. Later ledger
entries must not treat them as official Registry vocabulary.

For a proposed use of an already-registered *application* quantity in a
domain that is not the quantity’s source example, record exactly one of:

- **Ineligible** — the use would break a Layer 0 distinction, treat an
  application quantity as a universal primitive, or rely on superseded
  or unpromoted text as if it were current authority.
- **Needs-mapping** — the quantity may be usable if a published mapping
  to domain observations is locked first, including causal-structure
  differences (for example coupled renewal versus recharge that does not
  depend on the stock). This status is **not a license** to compute or
  to fill a dictionary in the present cycle. A later mapping is a new
  proposal.
- **Eligible-as-application** — the mapping is complete, the quantity is
  still labeled an application quantity, and no new universal cutoff or
  primitive is introduced. **“Eligible” never means “validated,” never
  means “now a primitive,” and never means “promoted.”** No trial in
  this note has this status.

A use may stay `needs-mapping` indefinitely. That is not a pass.

## 3. Required checks before a use can leave `needs-mapping`

1. Layer 0 distinctions hold (reality ≠ state ≠ observation ≠ model;
   expenditure ≠ correction; PAE is a principle, OIE is a process;
   \(V^*\neq V_{PCB}\neq V_{max}\) by definition; ACR is coverage, not
   ethics; definition adoption ≠ empirical truth; CI-A₀).
2. The source-example causal structure is declared, and any difference
   in the new domain is declared (the 30 October record already forbids
   transferring the freshwater “recharge does not depend on stock”
   assumption to coupled host-fish recruitment without a new term).
3. Each symbol is mapped to named observations, units, a window, and
   an uncertainty rule. Official IDs may be UNFILLED-REQUIRED.
4. The quantity is not renamed as a universal primitive or given a new
   universal cutoff.
5. Authority is the current paper or current decision record, not a
   superseded draft or unpromoted addendum.

## 4. Trial classifications (this cycle; not computed uses)

### T1 — Using \(\eta_{TM}\) as a freshwater (Central Valley) screen when timescales are not both finite

**Status: needs-mapping (not a license).** The 30 October record retains
\(\rho_{TM}\) where both timescales are finite and offers \(\eta_{TM}\)
when renewal is zero or a timescale is undefined. That is a possible
reuse, not an automatic one. The freshwater protocol’s
recharge-independence assumption, the Round 1 residuals on official
boundaries and \(\tau_d\) versus \(\tau_{d,\mathrm{net}}\), and the
difference between a water stock and a recruiting population must be
declared in a mapping before any \(\eta\) is computed. This note does
not compute one, does not add an \(\eta\) row to the Bite 1 dictionary,
and does not authorize such a filling in this cycle. Any later mapping
is a new proposal.

### T2 — Using the logistic addendum’s \(M(t):=\mathcal{F}_{PAE}-\mathcal{F}_{OIE}-\cdots\), or a term written \(\lambda_{PAE}(t)\,PAE(t)\), as if it were current HKL

**Status: ineligible.** Round 2 finding F5: those formulas cite “HKL
§5.1” and “Sahel §5.1” as the current papers do not contain them, and
they treat PAE as a number. Current AEF §2 and HKL §7 (v2 does not
override) decide this. Ineligibility here is not a new ban; it records
an already-established authority failure.

### T3 — Using the corrective-dependency *screen* (\(\eta^{nat}_{TM}<1\le\eta^{tot}_{TM}\)) outside the mussel example

**Status: needs-mapping (not a license).** The 30 October record already
says the substituted status only screens possible corrective dependency;
confirmation needs the buffer comparison or observation after a program
ends. A new domain must publish the mapping for \(\eta\), the horizon
\(h\), and the buffer margin, none of which are universal, and must not
treat the screen as confirmation. No screen is computed here. A later
mapping is a new proposal.

## 5. What this note does not do

It does not amend the registry, promote v0.3.2, demote a current paper,
compute a field quantity, invent data, or fill the freshwater
dictionary. Future uses still need evidence for their mappings and
measurements. These status words have procedural status only; they
are not official Registry vocabulary unless Jordan later defines them
as such (Review item A8).
