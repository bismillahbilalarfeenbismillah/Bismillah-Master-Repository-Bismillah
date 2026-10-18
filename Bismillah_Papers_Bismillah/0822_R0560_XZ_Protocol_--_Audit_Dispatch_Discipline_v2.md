# Bismillah ir-Rahman ir-Rahim

# R0560 -- XZ Protocol -- Audit Dispatch Discipline v2

**Chronological Index:** 822 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AUDIT_DISPATCH_D0_D7.md.txt  
**Source Format:** txt  
**SHA-256:** `583b3639647dae0a7ae24449a06a3a872b430123be87194623d4e6c5867127df`  

---

## R0560 · XZ Protocol -- Audit Dispatch Discipline v2

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AUDIT_DISPATCH_D0_D7.md.txt
- source_format: txt
- text_sha256: 583b3639647dae0a7ae24449a06a3a872b430123be87194623d4e6c5867127df

# XZ Protocol -- Audit Dispatch Discipline v2
# Supersedes AUDIT_DISPATCH_DISCIPLINE (v1). Include the ROLE-APPROPRIATE
# variant in every dispatch. Do NOT ship the full document to every seat --
# see the leakage matrix at D-0.
#
# Version and integrity: this block is versioned and its digest is recorded in
# the dispatch manifest alongside every other member. v1 was not, and v1
# opened by narrating a recurrence count from memory, which is the defect it
# exists to prevent. This version states no ordinal. Where a count is needed,
# cite the recurrence table; if the table does not yet exist, say the count is
# not derivable and stop.

## D-0 -- WHAT EACH SEAT RECEIVES (leakage matrix)

The v1 block shipped an enumerated list of nine known defect classes to every
seat. That has two costs. First, producer and auditor both read the same list,
both converge on those nine, and the next instance lands in class ten -- the
gate-displacement thesis operating on the audit methodology instead of the
build tool. Second, a list of what to find is enough to write a plausible
audit without executing anything. This program has already voided one
re-confirmation because the brief leaked expected values, and has already
caught a seat returning simulated execution output.

| Section | Advisory seat | Adversarial seat | Carrying seat |
|---|---|---|---|
| D-1 invariant and method | yes | yes | yes |
| D-2 role, standing, verdict discipline | yes | yes | yes |
| D-3 mandatory steps | yes | yes | yes |
| D-4 novelty quota and adversary rotation | yes | yes | yes |
| D-5 execution proof | optional | yes | **required** |
| Expected digests, counts, manifest value | yes | yes | **withheld** |
| Enumerated historical defect classes | **withheld** | yes | **withheld** |
| Prior seats' findings for this version | withheld until return | yes | withheld until return |

Carrying seats receive the bytes and the challenge, not the answers. The
enumerated class list moves to the producer side as a regression suite the
build must fail on; it is not auditor guidance. Adversarial seats get it
because their job is regression, not discovery.

## D-1 -- THE INVARIANT (replaces the trajectory list)

This instrument's defects have consistently occupied the boundary between what
is computed by a tool and what is asserted from recollection, and that
boundary has moved outward each time a layer was brought inside the tooling.
Inside the computed region the producer's accuracy is near-total. Outside it,
accuracy is uncorrelated with how confident or well-formed the prose is.

The corresponding detection record: gates have caught value-level errors only
after the class was named; executing external seats have caught everything
else; non-executing seats have caught nothing and have produced false passes;
the producer's own green build check has caught none of the recorded
recurrences.

**Your task is to locate the current boundary, measure it, and attack the
first layer outside it.** Findings that do not locate the boundary close this
round's instances and leave the mechanism intact.

## D-2 -- ROLE, STANDING, VERDICT

Open your report by naming your role, your family relative to the producer,
whether your verdict binds, and whether it counts toward the two-family carry.
Repeat the standing inside the verdict itself.

Verdicts: **PASS** (or CARRY-CLEAN), **CONDITIONAL PASS**, **HALT**. Name the
blocking findings and what clears each. A carrying seat's HALT blocks freeze
outright. An advisory seat's HALT is recorded and forwarded and blocks
nothing; state that, so the record cannot later misdescribe it.

Producer-family seats: your findings do not discharge any part of the carry.
If the last several rounds have all been producer-family, say so in the
verdict as a governance note. That condition is invisible to everyone except
whoever notices it.

## D-3 -- MANDATORY STEPS

**D-3.1 Byte verification.** Digest every normative file. Run the canonical
command. Run the build. Report counts and exit codes. Table stakes.

**D-3.2 Claim provenance ledger.** For every factual claim in the current
version's amendment entry, assign exactly one provenance:

- COMPUTED -- a shipped gate fails if this is false; cite the gate and the
  output line, and verify by breaking the claim and confirming the gate fires.
- EXTERNAL -- verified against state the producer does not control; name the
  holder and digest.
- ASSERTED -- no gate, no external confirmation; true only insofar as you
  looked.

ASSERTED is the default. A seal over a region does not make that region's
claims COMPUTED: a seal proves the text is unaltered since sealing and says
nothing about whether it is true. Report the three counts and the ASSERTED
fraction. **That fraction is the round's headline number, not the finding
count.**

**D-3.3 Hedge and deferral audit.** For every downgrade term (CLOSED IN PART,
DISCLOSED, NOTED, DEFERRED, NOT VERIFIABLE): is the downgrade correct, is the
stated REASON true, does the disclosed scope match the actual scope, and does
a register row track it? A deferral with a false reason is a defect wearing
the costume of a disclosure and closes inquiry rather than opening it.

**D-3.4 Historical integrity, with a cross-version anchor.** Recompute all
seals from the shipped text and compare to the shipped seal file. Then compare
every historical seal against the prior version's seal file. If the prior file
does not ship, that absence is itself the finding: a seal file regenerated
each version by the party who edits the text is self-attestation, and
self-attestation plus drift is indistinguishable from correctness from the
inside. Any historical value that changed must be declared in the current
entry.

**D-3.5 Build-tool attack.** Copy the package. Mutate. Run the build. Every
probe carries: a mutation-landed assertion (hash before and after; assert they
differ), a discrimination control (a known-bad that must fail), a benign
control (a clean run that must pass), and a verbatim reproduction. **A probe
whose mutation did not land is VOID and must be reported as void in the
method section, never as a finding.** A benign control proves the build
discriminates; it does not prove your mutation landed. These are different
controls and both are required.

**D-3.6 Coverage measurement.** Characters total, characters covered by at
least one semantic gate, characters covered by none, and the percentage. Then
state which region each claim in the current entry occupies. Repeat at packet
level: how many shipped members carry a digest in any shipped text and how
many carry none. Claims about unhashed members cannot fail a build by
construction.

**D-3.7 Cross-version consistency.** Values a prior report recorded as
tool-computed against the current entry's claims about them. Findings raised
in prior reports against the current register: the count raised must equal the
count dispositioned, and a finding may be closed, disclosed, or noted, but not
absent. Any CLOSED must have byte evidence in THIS package.

**D-3.8 Boundary report.** Name the outermost layer the build does not compute.
State what would bring it inside. This is the deliverable that ends the
trajectory rather than servicing it.

## D-4 -- NOVELTY QUOTA AND ADVERSARY ROTATION

**Quota.** At least two probes must exercise defect classes not recorded in
the prior corpus. Name them and flag them as new. They are appended to the
program's class register on return. The register grows FROM the seats; it is
not shipped INTO them.

**Rotation.** Declare which adversary you modelled:

- *Careless producer* -- global replace, stale copy, unlanded fix.
- *Stale-context producer* -- claims true of an earlier build.
- *Self-consistent forger* -- every surface agrees on a false value. Most gates
  check self-consistency and are blind to this by construction.
- *Patient contributor* -- the protocol's actual subject. No gate in this
  instrument's history has been tested against it. A seat taking this posture
  should expect to conclude that the instrument does not defend against it,
  and should say so rather than reporting clean.

## D-5 -- EXECUTION PROOF (carrying seats: required)

Report the environment, the verbatim exception strings your probes produced,
and the challenge value from the dispatch's sealed nonce. Expected values are
withheld from carrying dispatches precisely so that a matching value
demonstrates execution rather than transcription.

A matching challenge shows that code ran. It does not establish which model
ran it, and it does not establish that the gate logic is correct. Claim only
what it shows.

If you cannot execute, stop and say so. Label the report NON-EXECUTING in the
first paragraph. A non-executing review is a legitimate deliverable when
labelled and worthless when not.

## D-6 -- WHAT NOT TO DO

- Do not treat the build's output as evidence. Run it, report it, then verify
  independently.
- Do not treat the amendment entry as evidence. It is the producer's
  self-description of a region no gate reads.
- Do not treat a CLOSED as closed. Verify the fix in the bytes.
- Do not treat a source comment as a fix. Comments naming finding IDs have
  been shipped over predicates that did not change.
- Do not treat a correct hedge as a correct claim.
- Do not rubber-stamp, and do not simulate execution. Both are recorded
  failure modes in this program with named instances.

## D-7 -- HOW TO TELL THIS BLOCK IS FAILING

Answer in one line each, in every report:

- Did every probe come from an enumerated list? (The block has become the
  gate; the quota at D-4 is being met in form only.)
- Did the dispatch tell me where to look, such that my findings were
  predetermined? (Leakage.)
- Is the ASSERTED fraction unchanged from the prior round? (Rounds are
  producing findings without moving the boundary. This is the most important
  of the four.)
- Have the recent rounds all been producer-family? (The apparatus is measuring
  itself.)

A yes is a finding about the process and belongs in the report.

---

# Bismillah ir-Rahman ir-Rahim
