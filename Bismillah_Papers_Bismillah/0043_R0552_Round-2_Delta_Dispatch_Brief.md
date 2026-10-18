# Bismillah ir-Rahman ir-Rahim

# R0552 -- Round-2 Delta Dispatch Brief

**Chronological Index:** 43 of 995  
**Date:** 2024  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** AI_PAPER_DISPATCH_R2.md  
**Source Format:** md  
**SHA-256:** `e5982a9133aa73fb720c1217df2bb33d32f15267e98c126556f0902789b7d90c`  

---

## R0552 · Round-2 Delta Dispatch Brief

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: AI_PAPER_DISPATCH_R2.md
- source_format: md
- text_sha256: e5982a9133aa73fb720c1217df2bb33d32f15267e98c126556f0902789b7d90c

# Round-2 Delta Dispatch Brief
## Inheritance, Transmission, and the Locus of Accountability
## Addressed to: Perplexity Computer, MODEL-COUNCIL MODE

---

## 0. Round type, and one leg that is unusual

This is a **delta round**, not a fresh substantive audit. Round 1 reviewed the paper and returned a
detailed recommendation set. This round audits what was done with it.

**One leg is unusual and should be read before the others.** Round 1's synthesis and its
accompanying evidence set supplied external sources the producer then imported into the paper: NIST's
taxonomy of synthetic-content transparency, C2PA and its detachability limit, the EU AI Act's
marking and logging obligations, watermarking robustness results, and the model-collapse literature.
**The producer independently verified exactly one of these** (Shumailov et al., Nature 631, 755-759,
2024, which checked out and whose subsequent qualification was also carried). **The rest were taken
on the council's word.**

That is the same failure shape this program has been guarding against all along, in a new costume:
recall is not evidence, and neither is another model's research when it is imported without
independent check. **Leg L4 exists to close it, and a seat that verified those sources in Round 1
should not be the seat that verifies them here.**

---

## 1. Council structure

- Each seat DECLARES model, vendor, and tier at the head of its report. Undeclared seats carry no
  verdict.
- Per-seat namespaces: F-A\<V\>-NN, vendor initial in the middle.
- Anthropic-lineage seats are ADVISORY ONLY; the producer instance is Anthropic lineage.
- Same-vendor seats count once.
- Producer self-repairs and producer-run checks earn no absence-credit.
- CONVERGENCE = PASS-DELTA from two carrying seats of different vendor families.
- **Where a seat participated in Round 1, it should say so.** Its Round-1 recommendations are part of
  what this round audits, and a seat grading the adoption of its own proposal should declare the
  interest rather than have it inferred.

---

## 2. Receipts

```
c502ea1c9c7fd3d1cac3de6096e421b483a24493a30adb3f3e69dca982ea6bfe  baseline_source_pre_round1.md
b956bc442af251cd51729a367c8a0ecb0bb344ec9e9de63624c469d8d8aea170  paper_source.md
651cd82fd37421924e2a01c5d83efcebd3d187e19b4eb87d80bb6cd28374ff07  paper.pdf
```

`SHA256SUMS.txt` is authoritative for every other packet file. A mismatch is a CRITICAL intake
finding and the round does not proceed.

---

## 3. Verification legs

**L1. Delta scope.** Diff the baseline against the current source. The delta is 7 hunks, 143 lines
added, 8 removed. Every hunk should map to one of six adopted recommendations: the transfer
conditions; the Level-two decomposition; the three provenance primitives; the markedness ledger with
multi-agent lineage and the producer-versus-owner distinction; the model-collapse evidence; the F-5
reframe and the corrigibility inequality. **Any hunk outside that set is a finding.**

**L2. Adoption fidelity.** For each of Round 1's recommendations, determine whether the paper adopted
it, adopted a weakened form, or declined it. Two were declined deliberately and the producer says so
below; a third category, adopted-but-distorted, is what this leg is for.

**L3. The two deliberate omissions, and whether they were rightly omitted.**

The producer did not adopt the typed propagation ledger schema in full, taking the ledger concept,
the UNKNOWN-never-defaults rule, and the producer-versus-accountable-owner distinction while leaving
out the entity-activity-agent typing and the named metrics. And the producer did not adopt the four
proposed experiments, judging them a companion paper.

**Assess both against a length constraint the producer was weighing**: an earlier external reviewer
warned that the paper's principal risk was diffusion and that its spine should stay tight. The paper
is now 8,300 words against 6,900 before. Was the omission correct, or does the paper now assert an
implementable governance architecture it declines to specify?

**L4. Citation fidelity on the imported sources. HIGHEST SEVERITY LEG.**

For each source imported from Round 1's evidence set, verify against a fetched primary:

1. NIST AI 600-1, and whether it treats watermarking, provenance metadata, and detection as distinct
   controls as the paper now says.
2. C2PA, and whether the detachability limit is acknowledged in the specification's own materials.
3. EU AI Act Article 50, and whether machine-readable marking and lifecycle logging are obligations
   in the terms the paper implies.
4. Watermarking robustness: degradation under paraphrase and translation, weakness on low-entropy
   text, removability.
5. Shumailov et al. and the subsequent qualification literature. **The producer verified this one and
   states the finding it relied on: recursive training degrades distribution coverage, tails first,
   with subsequent work arguing severity is conditional on curation and retained human data.** Check
   whether the paper's two-sided use of it is fair to both halves.

**Report any claim the paper attributes to these sources that they do not support.** Fabricated or
overstated standards claims are CRITICAL, because a paper asking laboratories to adopt a marking
regime cannot misdescribe the standards that regime would sit inside.

**L5. The bridge principle, adversarially.** The four transfer conditions are new and load-bearing.
Test them: construct a system satisfying all four to which the structure plainly should not apply, or
a system failing one to which it plainly should. Assess whether the claim that conditions one and
three are decidable from public facts survives contact with real deployment opacity.

**L6. Whether the paper still says what it said.** The Round-1 material was inserted into an argument
that already existed. Check that the insertions did not silently alter surrounding claims, that the
non-apportionment formulation is consistent throughout, that the moral-status guard holds in every
new passage, and that no new numeric cross-reference was introduced.

**L7. Standing lint.** No em-dash characters. No doubled words. No numeric section references. Brand
canonical.

---

## 4. Probe discipline

Wrap-immune normalisation on every text probe; word-boundary matching, never bare substring
containment; quote and dash characters normalised; whole-document lints run against the source rather
than extracted PDF text, because extraction interleaves table columns and drops hyphens at wraps.
Each of these rules exists because the producer violated it at least once and recorded the result.

---

## 5. Verdict

Six-element findings; severities UPPERCASE; PASS-DELTA or NON-PASS per carrying seat; synthesis
naming the convergence determination.

**And one judgement the producer is asking for explicitly, outside the finding format.** This paper
has now had one substantive round and one delta round. **Is it done?** Not whether it is perfect, but
whether further rounds would still be finding defects proportionate to the cost of another cycle, or
whether the remaining gaps are ones only a different kind of work closes: an implementation, an
experiment, a specialist reader. A council that says a paper is finished is more useful than one that
always finds something.

---

# Bismillah ir-Rahman ir-Rahim
