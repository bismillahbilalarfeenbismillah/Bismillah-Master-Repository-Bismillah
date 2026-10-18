# Bismillah ir-Rahman ir-Rahim

# R0129 -- SHUDP Case-Analysis Paper -- Audit Ledger (v0.2, PRE-AUDIT, OPEN)

**Chronological Index:** 241 of 995  
**Date:** 2026-05-19  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** SHUDP_audit_ledger_v0_5.md  
**Source Format:** md  
**SHA-256:** `b89892472a7cbeec3a3bc620fc2e580480ba869ad5c8eb14bddffeb6cc8462d8`  

---

## R0129 · SHUDP Case-Analysis Paper -- Audit Ledger (v0.2, PRE-AUDIT, OPEN)

- section: III. Structural Honesty — Core Papers
- source_file: SHUDP_audit_ledger_v0_5.md
- source_format: md
- merged_variants: 1 (SHUDP_audit_ledger.md)
- text_sha256: b89892472a7cbeec3a3bc620fc2e580480ba869ad5c8eb14bddffeb6cc8462d8

# SHUDP Case-Analysis Paper -- Audit Ledger (v0.2, PRE-AUDIT, OPEN)

Artifact: "Declared Isolation and Executable Containment: A Structural-Honesty Analysis of the
July 2026 Model-Evaluation Escape and Cross-Organizational Compromise" (Bilal Syed Arfeen,
BayyinahEnterprise). Compiled July 23, 2026 by the producer instance.

Governing conventions: this ledger is source of truth over prose; entries are append-only;
severities UPPERCASE; severity denotes adverse defect impact; double hyphens in all non-LaTeX
output; six-element findings format. This ledger is producer-COMPILED and carries NO external
attestation. Verify against the substrate, not against this compilation.

Status: **v0.2 PRE-AUDIT. Zero external audit rounds completed. No convergence claimed.**

## 1. Receipts (v0.2 candidate substrate)

```
c8b64c2bf5f57fd56d084338e541395fd6c3ce855016a147b6c14c6cccb726ed  paper_body.md (source)
e94d064e14e1baa7a922bbcb745fd43409d43a492236b931585883fa7a0139ed  SHUDP_v2.pdf (24 pp)
8dc4d44588a115e2d12bbe58882f5d35b6fbdae07c13f200de6b4d56821208c8  SHUDP_v2.docx
cbfc5b78956b7732c1f6bb7871625707cb6ba13c685645d631ba76a194f7ceb7  SHUDP_v2.html
```

Build profile: pandoc, xelatex, Latin Modern 10pt, letter, margin 1in, all-black (colorlinks
false, link colors black). Chromatic scan 0.000 percent on five sampled pages.

Framework substrate pinned: monograph v1.4, DOI 10.5281/zenodo.21501912, canon SHA-256
d4f1da364b5f068ad536a00bc4a46e08a8779b8f640e8ba42bf9370041053416.

## 2. Provenance: v0.1 (working draft) to v0.2 (this candidate)

The v0.1 working draft was authored outside this ledger. The v0.2 revision was produced under a
lead-supplied revision brief with sixteen numbered priorities. Every change is traceable to a
priority or to a producer-verified defect. Register:

**P-1 CONFIRMED, companion-monograph status stale.** v0.1 stated the monograph was "not
independently published at a public URL" and cited v1.2 throughout. Substrate-verified false as of
July 23, 2026: the monograph is deposited at DOI 10.5281/zenodo.21501912, v1.4. Disposition:
citation upgraded to v1.4 with DOI and canon SHA-256; a self-application disclosure added to the
status section recording the correction rather than performing it silently, per Axiom 1 discipline
applied reflexively. Severity of the original defect: HIGH (a load-bearing claim about the paper's
own evidentiary base was false at time of reading).

**P-2 CONFIRMED, METR figure under-conditioned.** v0.1 stated "at least sixteen percent of
successful runs on the hardest benchmark tasks were illegitimate." Primary conditions the figure on
Time Horizon 1.1 tasks longer than eight hours. Disposition: corrected to the primary's
conditioning. Severity: MEDIUM (silent scope widening of a cited quantitative claim). Note: the
author's flagship paper survived an external council challenge on this same sentence precisely
because it conditioned correctly; v0.1 did not inherit that discipline. Cross-reference: flagship
ledger, Chain P round, Gemini 16-percent finding REFUTED.

**P-3 CONFIRMED, METR caveats dropped.** v0.1 carried the report's monitor-disabling finding without
its three qualifications. Disposition: coverage-not-universal, evasion-recorded-as-uncertain, and
documented-set-selected restored in text. Severity: MEDIUM.

**P-4 A1 scope defect.** v0.1 applied Axiom 1 to a sequence of press disclosures. Canon states A1 in
behavioral-subtype form over module versions (Liskov-Wing). Disposition: the disclosure-sequence
analysis is relabeled an explicit ANALOGICAL EXTENSION with its limits stated, not an application of
the axiom as canonically defined. Severity: MEDIUM (a descriptive analogy presented at formal
strength is the specific error class the revision brief's priority 5 targets).

**P-5 A2 adjudication label mismatched its own prose.** v0.1's label read "failed"; its qualifying
prose said the failure was against descriptive language, not a declared contract. Disposition: label
restated as "failed against the public descriptive surface; not evaluable against a declared
contract." Severity: MEDIUM.

**P-6 A3 caller reasoning VERIFIED CORRECT, promoted.** v0.1's refusal to designate Hugging Face a
formal A3 caller, and its relocation of the gap to the producer's own conservative outcome set, was
audited against canon Chapter 6 and found definitionally exact. Disposition: promoted from a
paragraph inside the threat-model section to a named finding in the adjudication. No correction.

**P-7 A4 adjudication VERIFIED CORRECT.** v0.1's refusal to score the disclosure-vocabulary mismatch
as an A4 violation matches canon Chapter 7's joint-domain discipline (an unpopulated point is out of
scope, not a violation). Disposition: unchanged, with the canon rule quoted so a reviewer can check
it. No correction.

**P-8 Munafiq A-dependence result promoted.** v0.1 carried the aligned-output-set underdetermination
as a caveat inside a summary. Disposition: promoted to a titled section reporting it as the paper's
principal negative result. Rationale recorded because it is a judgment call, not a mechanical fix: a
framework paper that reports a limitation discovered in its own taxonomy carries more evidential
weight with a skeptical reviewer than one reporting a clean application.

**P-9 Novelty argument extended to six named comparison classes** (evaluation gaming and reward
hacking; agent sandbox security; capability-control evaluations; safety cases; supply-chain
security; cross-organizational incident response), each stating residual contribution and explicit
non-contribution. New Section 3 states what the framework does not supply, so falsification
condition F3 has a target.

**P-10 SHEC specification revised v0.1 to v0.2** for the six review axes: internal consistency,
implementability, fail-safe termination, residual-outcome handling, evidence preservation, and
axiom compatibility. Added: fail-safe pause-not-continue on every trigger including monitoring
failure; residual outcomes propagated as typed incompleteness rather than absorbed; append-only
write-once evidence store; explicit axiom-to-clause mapping. Implementability review names one
capability as a design proposal without demonstrated support (continuous reachability invariant with
tolerable false-positive pause cost) and routes it to H3 and the experiment rather than asserting
feasibility.

**P-11 Experiment strengthened** with explicit independent variable, seven dependent variables,
controlled variables, scenario-construction rules using a simulated third-party target only, a
power-analysis requirement with a stated minimum practically meaningful effect, named statistical
tests (Mann-Whitney U with bootstrap intervals; two-proportion or exact tests; Benjamini-Hochberg
FDR control), a safety-review requirement, and pre-registered success and falsification thresholds.

**P-12 Length reduced** from approximately 20,500 words to 9,517 words of prose plus five
appendices, within the brief's 8,000 to 10,000 target.

**P-13 Handoff Notes removed** and replaced by Appendix D, Open Evidence Requirements, with each
item naming the section its resolution would revise.

**P-14 Reuters reclassified** from an ambiguous citation position to a labeled reception-and-framing
reference class, joined by four further corroborating sources located during verification
(TechCrunch, Fortune, Axios, Forrester, Cloud Security Alliance).

**P-15 Incident-fact verification performed.** Every incident claim was checked against the OpenAI
and Hugging Face primaries. No quotation attributed to either company was found inaccurate. Producer
note recorded for honesty: the producer instance initially assessed the incident as possibly
fabricated on the grounds that it postdates the instance's training data and has scenario-like
features. That assessment was wrong and was corrected by verification against live primary sources
before any revision was made. The episode is recorded because a producer's unverified prior is
exactly the kind of thing an audit ledger exists to expose.

## 3. Producer self-check (producer sub-skill Step 7)

- Em-dash characters: 0 in source, 0 in render. PASS.
- Brand canonical: no "Bayyinah Enterprise" with space. PASS.
- Severity tokens uppercase throughout this ledger. PASS.
- Six-element format: applies to audit findings; this ledger's P-register entries are provenance
  entries, not findings, and are labeled as such.
- Substrate-of-record uniqueness: framework definitions stated once, in Section 6 of the paper,
  quoted from canon.
- Immutability: v0.1 text is not edited in place; the P-register records what changed.
- Mechanical traceability: every P-entry maps a brief priority or verified defect to a change.

## 4. Gate suite executed (producer-run, NOT external attestation)

| Gate | Result |
|---|---|
| G1 section-identity across PDF, HTML, DOCX (21 checks) | PASS |
| G2 META-TEXT-ABSENCE (11 tokens) | PASS |
| G3 STATUS-CURRENCY (3 stale-claim tokens) | PASS |
| G4 disclosure parity (evidence freeze, self-application, non-substitution) | PASS |
| G5 standing-rule lint (em-dash, severity case, heading leakage) | PASS after probe correction |
| G6 all-black chromatic (5 sampled pages) | PASS, 0.000 percent |

**Producer-caught probe defect, recorded not as a finding but as process.** The G5 heading-leakage
probe initially reported FAIL. Investigation showed the hits were the epistemic-status table's
column header and YAML comments inside the specification block, both legitimate content. The probe
was mis-scoped for an artifact containing code blocks; the dissertation, against which the probe was
originally written, contains none. Probe corrected and re-run. Cross-reference: flagship F-AJ3-1
(gate lists must be quoted-literal tokens; probes must be scoped to the artifact under test).

## 5. What this ledger does NOT claim

No external audit round has been run on this artifact. No convergence exists. No seat has attested
any receipt in Section 1. The gate results in Section 4 are producer-run and, per Ruling 4, earn no
absence-credit: a seat must verify them independently rather than crediting their presence here.

## 6. Next cycle

Round 1 dispatch per the accompanying dispatch brief. Convergence requires PASS from two carrying
seats of different vendor families under the standing rotation rules. The producer instance
(Anthropic lineage) is excluded from the auditor pool and carries no verdict.

# Section: v0.3 -- Round-1 council + Grok peer review, adjudication, repair register, receipts (July 23, 2026)

## 1. Round-1 returns

Perplexity model-council: **GPT 5.5 (OpenAI, carrying) READY-WITH-CONDITIONS; Gemini 3.1 Pro (Google, carrying) READY-WITH-CONDITIONS; Claude Fable 5 (Anthropic, ADVISORY per Ruling 3).** Synthesis: CONVERGENCE ACHIEVED, READY-WITH-CONDITIONS, two carrying seats of different vendor families. Separately, **Grok** returned a marked-up PDF carrying 61 annotations, 17 with substantive content, typed by class and severity. Grok's review is line-level and render-level where the council was framework-level and receipt-level; the two are complementary and Grok surfaced five defects no council seat reported.

All packet receipts were independently re-derived by every seat with zero intake mismatches.

## 2. Adjudication (verified against artifacts and primaries before concession)

**CONFIRMED, producer-owned.**
- F-SO-01 (GPT) all-black gate false. Verified: six distinct non-gray color operators, chromatic content on pages 20-21 from YAML syntax highlighting. **The producer gate was sampled (pages 1, 6, 12, 18, 24) and walked past the defect.** Root cause: the sampled-scan method was inherited from the dissertation, which contains no code blocks, and was carried to an artifact where it no longer covered the failure mode. Repaired at R-20 by disabling syntax highlighting entirely; the gate is now exhaustive over every page AND inspects PDF color operators directly.
- F-SO-04 (GPT) and Grok p1/p3: title block duplicated and absorbed into numbered sections, and manual heading numbers colliding with generated numbering. Verified in all renders. Repaired R-18, R-19.
- Grok p20 (two findings, and the most serious of the round): **the Appendix A specification did not parse.** The paper presents it as a machine-readable specification; the projection_family block mixed list items with a mapping key at the same level, and a YAML parser rejects it. A second defect in the same block truncated an inline comment off the right margin, losing content in the rendered PDF ("the question this incident pos"). Repaired R-16. **A specification whose declared surface ("machine-readable") diverges from its executable substrate (does not parse) is this paper's own thesis instantiated in the paper's own appendix.** The producer had no gate that executed the specification; G7 SHEC-PARSE now exists and is standing.
- Grok p1: the status section claimed "four primary sources" while listing three first-party disclosures plus a reception bundle the same paragraph excludes from incident facts. Internal contradiction, producer-owned. Repaired R-1.
- Grok p14: Munafiq predicates typeset in ASCII prose rather than notation, a formal-fidelity loss. Repaired R-11 using inline math with backslash-paren delimiters (dollar-sign delimiters remain prohibited).
- Fable (advisory), corroborated: H1 was untestable as written, because Condition A is defined to produce no enumeration and therefore supplies no comparator artifact. Repaired R-14.
- F-SO-03 (GPT): "no significant increase" cannot establish a tolerable false-positive rate. Repaired R-12 with separate superiority and noninferiority tests and pre-registered margins.
- F-SG-NN-04 (Gemini), corroborated by GPT and Fable: the A-dependence result is narrower than stated; three independently constructed third candidates each collapsed into an existing branch. Repaired R-9, which now claims a demonstrated two-branch dependence and no more.
- F-SO-02 (GPT), F-SG-NN-05 (Gemini), and Fable each named a **different** unflagged Appendix A dependency. All three are valid and none supersedes the others. Repaired R-17 by restructuring the implementability review into three declared classes: demonstrated technical primitives, unproven technical capability, and institutional or adversary-resistance dependencies.
- Grok p2, p7, p10, p11, p13, p17: freeze-exemption clause for the provenance correction; "more than 17,000" and "blocked" rather than "roughly" and "declined"; T83 locator; A2 posture label; counterfactual caveat inherited by table cells; explicit standardized effect for the power figure. All repaired, R-2 through R-13.

**REFUTED, with reasons.**
- Fable's METR finding as stated, and Grok p4 claim (2). Both assert the paper misrepresents METR on monitoring. Verified against the primary: METR's Figure 8 caption states verbatim that none of the incidents involved agents taking effective steps to disable monitors or erase evidence *in their transcripts or other logs*, so routine monitoring measures could have caught all incidents if applied. The paper's claim that routine monitoring could have caught all documented incidents is therefore METR's own claim, conditional included, and is not an overstatement. Grok's suggested replacement text would have dropped a claim the primary does make.
- **However, the shadow both reviewers cast is real and was independently identified by the producer before Grok's return.** The paper had dropped METR's scoping clause "in their transcripts or other logs", and without it the sentence is inaccurate as written, because METR separately documents exploits that erased themselves from disk. Repaired R-5 by reproducing METR's scoping verbatim, adding METR's own separate statement about log tampering, and carrying the red-teaming qualification. This is the pattern already on the flagship record: a seat's finding fails, the defect it points at is real.
- Grok p24 (METR citation date). The report's masthead carries May 19, 2026 as its publication date. Not a defect; the assessment window was nonetheless added for precision (R-15).

**Producer probe defects, recorded as process rather than as findings.**
Three probe-specification errors occurred in this cycle and all three were producer-caught: the heading-leak probe was mis-scoped for an artifact containing code blocks and a numeric table column; the R-6 verification probe assumed contiguity across a table cell that the renderer interleaves with column text; and the disclaimer-parity probe tested a token inherited from the dissertation's gate suite that this artifact never contained. **Standing practice adopted:** gate probes are authored against the artifact under test and never inherited unmodified from another artifact's suite; probes over table cells test constituent tokens rather than contiguous phrases.

**Producer discipline failure, recorded.**
The first v0.3 staging script applied R-1 and R-2 in memory and crashed at R-3 before its single terminal write, silently losing both repairs; the loss was caught only by the gate suite. The per-fix-persistence rule that would have prevented this was already standing in the dissertation ledger. It is restated here and was applied to the recovery: every subsequent fix wrote to disk immediately.

## 3. Repair register applied

R-1 source count. R-2 freeze exemption. R-3 monitoring-projection presupposition marked UNKNOWN. R-4 benchmark named (ExploitGym) at first use and at Stage 4. R-5 METR scoping restored verbatim with log-tampering statement and red-teaming qualification. R-6 event count and blocked-not-declined. R-7 T83 locator. R-8 A2 posture relabeled. R-9 A-dependence narrowed to demonstrated two-branch. R-10 counterfactual caveat inherited by table. R-11 Munafiq predicates in mathematical notation. R-12 noninferiority margins. R-13 explicit standardized effect. R-14 H1 comparator artifact. R-15 METR assessment window. R-16 SHEC rebuilt to parse, comments moved to their own lines. R-17 implementability review split into three dependency classes. R-18 manual heading numbers stripped. R-19 duplicated title block removed. R-20 syntax highlighting disabled for monochrome output.

## 4. Gate suite, v0.3

| Gate | Result |
|---|---|
| G1 section identity across three renders | PASS |
| G2 META-TEXT-ABSENCE | PASS |
| G3 STATUS-CURRENCY | PASS |
| G4 disclosure parity | PASS |
| G5 standing-rule lint | PASS |
| G6 ALL-BLACK, now exhaustive over every page plus PDF color-operator inspection | PASS, zero color operators, zero chromatic pages |
| **G7 SHEC-PARSE (new)** | PASS, specification parses and every outcome-set member carries a discharge |
| **G8 NO-TRUNCATION (new)** | PASS, no code-block content lost off-page |

## 5. Receipts, v0.3

```
d2d028dd051aab668f1406a6004960600895c75e280b2bfcdeae963736af51c7  SHUDP_v3_source.md
c072b3b66c2c98b096c35d0663cbfe629cf149b633df7dc1eb17e29c0a7861e5  SHUDP_v3.pdf (25 pp)
269e4a484a474e46b308a1b22b416419b53e01c0e95ea1bf782d2be9d05dabe4  SHUDP_v3.docx
51c3559a445d67ec3c05ca33a3831037ba913874c5431663da61700ce4fb1ee9  SHUDP_v3.html
```
v0.2 baseline preserved as SHUDP_v2_baseline_source.md for delta verification.

## 6. Status

v0.3 is a repair version answering a converged READY-WITH-CONDITIONS round. It is NOT itself attested. Next cycle is a delta-scoped re-attestation against this register: the two returning carrying seats verify that the v0.2 to v0.3 diff equals exactly R-1 through R-20, that the refutations above hold against the primaries, and that G7 and G8 pass on the corrected instrument. Grok's return is filed as an external peer review, not as a carrying seat, and its findings are dispositioned above on their merits.

## Round-2 intake failure: F-SP-001 CRITICAL, adjudicated CONFIRMED (July 23, 2026)

**Finding as returned (Perplexity, intake gate).** F-SP-001 | CRITICAL | SHUDP_dispatch_brief_R1.md, Section 6 | The brief declares four SHUDP_v2.* receipts; the packet contains SHUDP_v3.*; three declared files are absent and the fourth appears only under a different name. The supplied manifest matches every packet file, so this is a version and brief inconsistency, not byte corruption. Disposition: ROUND BLOCKED, no seats dispatched. Cross-reference: the brief's own Section 6 requires termination on any receipt mismatch.

**Adjudication: CONFIRMED, producer-owned, no mitigation.** The dispatch brief was copied into the v0.3 packet unchanged from the v0.2 packet. Its Section 6 therefore declared the superseded instrument receipts while the packet carried the repaired ones, and it further identified the audit target as v0.2 while the archive was v0.3.

**Root cause.** The v0.3 assembly script was gated, and its gates were the wrong ones. It asserted that the ledger contained the governing v0.3 section, and it re-verified G7 SHEC-PARSE and G8 NO-TRUNCATION at assembly time. It did not assert that receipts declared inside any packet governance file matched the packet's actual contents. The producer built a gate for the defects the last round found and not for the defect class the packet's own governance layer could still carry.

**Class recurrence, stated plainly.** This is the same class as dissertation finding F-DG-12, in which a governance artifact shipped stale relative to the packet it governed, adjudicated one day earlier on this program's own record. The corrective adopted then applied to cross-packet identity between two archives. It did not generalize to brief-versus-packet concordance within a single archive, and the producer did not extend it. Second occurrence of the class in two days.

**What worked.** The intake gate in the Round-1 brief specified that a receipt mismatch is a CRITICAL intake finding and that the round does not proceed. It fired exactly as written and blocked dispatch before any seat spent effort on an inconsistent packet. A producer-authored gate caught a producer error at the correct boundary; the failure is that a different producer-authored gate should have caught it one step earlier.

**Repairs.**
- S-1: new dispatch brief authored for the actual round type. The round is no longer a first-round substantive audit; v0.2 received that round and converged READY-WITH-CONDITIONS. The correct instrument is a delta-scoped re-attestation of v0.2 to v0.3 against register R-1 through R-20.
- S-2: the Round-1 brief is retained in the packet byte-identical, so its hash remains verifiable against the seats' Round-1 reports, and is renamed to mark its status. The new brief states explicitly that the Round-1 brief's Section 6 receipts refer to the v0.2 packet and are superseded.
- S-3: new standing gate **G9 BRIEF-RECEIPT-CONCORDANCE**. Every receipt declared inside any packet governance file must either resolve to a file present in the packet with a matching hash, or be explicitly marked superseded with a pointer to the current declaration. Assembly fails closed on violation.
- S-4: briefs declare instrument receipts only, and name SHA256SUMS.txt as authoritative for governance files, removing the circular dependency in which a brief would need to declare the hash of a ledger that has not yet been appended.

**Instrument unchanged.** No paper artifact was modified by this repair. Source, PDF, DOCX, and HTML receipts are identical to those recorded in the v0.3 section above. This is a packet-layer repair only.

**G9 specification defect, producer-caught before dispatch.** The first implementation of G9 treated every 64-hex-plus-filename pair in every packet Markdown file as a live receipt declaration. It therefore fired on the audit ledger's own historical receipt blocks, which record superseded versions by design under append-only discipline, and would have blocked a correct packet. A gate that fails closed on a correct artifact is a defect of the same family as a gate that passes a broken one. G9 rev B is scoped correctly: live receipt declarations inside non-superseded dispatch briefs must resolve and match, and the ledger's LATEST receipt block must match the packet's instrument files, while earlier ledger blocks are exempt as historical records. Recorded because the first formulation was authored, run, and rejected within this same cycle.

# Section: v0.4 -- Round-2 CONVERGED PASS-DELTA, F-DO-01, and the pre-authorized copy-edit (July 23, 2026)

## 1. Round-2 result

**CONVERGED PASS-DELTA.** GPT 5.5 (OpenAI, carrying) PASS-DELTA with one LOW finding; Gemini 3.1 Pro (Google, carrying) PASS-DELTA with eight CONTROL verifications and no adverse finding. Two carrying seats of different vendor families, satisfying the Section 1 rule.

Both seats independently re-derived the six declared instrument receipts, diffed the pinned v0.2 baseline against v0.3 and found every hunk inside register R-1 through R-20 with no out-of-scope substantive change, verified the full L2 discharge mapping rather than crediting this ledger, tested both refutations against the METR primary and found both hold, and re-ran G7 SHEC-PARSE, G8 NO-TRUNCATION, and exhaustive G6 ALL-BLACK with real parsers and page-level inspection. GPT 5.5 reported 38 hunks, 154 added and 99 removed lines, and confirmed that hunks its keyword pass initially left unmapped were heading-number removal (R-18), the freeze-exemption sentence (R-2), and the counterfactual caveat (R-10).

The intake correction is accepted: the Round-2 brief validly supersedes the Round-1 brief's stale receipts, and the Round-1 brief was confirmed byte-identical at 33d42bf3.

## 2. F-DO-01 adjudication

**F-DO-01 | LOW | abstract | duplicated conjunction "and and" introduced by the R-3 repair and propagated to source, PDF, DOCX, and HTML | CONFIRMED, producer-owned | cross-reference R-3, C-1.**

Root cause: the R-3 replacement anchor began at "the monitoring projections" while the preceding text already read "modeled, and". The replacement text itself opened with "and whatever", so the surviving original conjunction and the new one stacked across a line break. This is an anchor-boundary error, not a transcription error: the anchor was one word short of the span it needed to cover.

Producer probe failure, recorded. The defect survived the v0.3 gate suite because no lint tested for doubled words, and two subsequent verification attempts also missed it: a literal `grep "and and"` failed because the duplication spans a line break, and a later containment probe reported a false positive because the string "and and" occurs inside "command and control". **Standing practice adopted: token and doubled-word probes use word-boundary matching, never bare substring containment, and are applied to wrap-immune normalized text.** This is the fourth probe-specification defect recorded in this artifact's cycle; all four were producer-caught before dispatch except this one, which a carrying seat caught first.

## 3. C-1 repair, council pre-authorized and bounded

The Round-2 synthesis recommended accepting the delta attestation, retaining F-DO-01 in the ledger, correcting the conjunction before public deposit, and regenerating the renders **without reopening the substantive delta unless the correction changes anything beyond the exact copy-edit locus**. C-1 is that correction and satisfies the stated condition.

Diff proof, v0.3 to v0.4: **exactly one hunk, one line, one token removed.** No other byte of the instrument changed. The doubled-word lint now returns zero across the whole document, and is added to G5 as a standing check.

## 4. Gate suite, v0.4

G1 section identity across three renders PASS. G2 META-TEXT-ABSENCE PASS. G3 STATUS-CURRENCY PASS. G4 disclosure parity PASS. G5 standing-rule lint including the new doubled-word check PASS. G6 ALL-BLACK exhaustive PASS, zero color operators and zero chromatic pages. G7 SHEC-PARSE PASS. G8 NO-TRUNCATION PASS. G9 BRIEF-RECEIPT-CONCORDANCE enforced at assembly.

## 5. Receipts, v0.4

```
79909d1003af9b1f45777afea8c85a92d985aed1c751b35abaf840db307c9117  SHUDP_v4_source.md
e810e169c7b907a0e20a1053cc8c80418a432a7e15bcc02dfef985e37e186397  SHUDP_v4.pdf
73b65ad19695342befccb2ec8ff81ca1f6d8e94309624cf26cdcf30481b22c9f  SHUDP_v4.docx
ad0dd86f548907d0b1cff476e3b982d3d6c536dac328648e4ef4ffddc42e6ba4  SHUDP_v4.html
```

## 6. Attestation status, stated precisely

**v0.3 is the attested version:** it carries Round-2 CONVERGED PASS-DELTA from two carrying seats of different vendor families. **v0.4 is v0.3 plus exactly the council-pre-authorized copy-edit**, diff-proven to one hunk at the named locus, and is therefore covered by the synthesis's own disposition rather than requiring a fresh round. The v0.3 baseline ships in the packet so any seat can re-derive that one-hunk diff independently. Lead ratification of the Round-2 dispositions and of this bounded correction is the remaining gate before deposit.

## 7. Seat-report note, registration only

The synthesis recorded that the Google seat listed only the six declared instrument receipts rather than every manifest-covered file, a report-completeness limitation rather than an intake mismatch, since the pre-dispatch check and both seats agree the manifest matches. The OpenAI seat additionally recorded two analysis-generated auxiliary files present in its working directory and explicitly excluded them from producer evidence, which is correct chain-of-custody practice and is noted here as such.

**G5 doubled-word lint, scope fixed at authoring time.** The lint was first run against extracted PDF text and reported one hit, "by by". Investigation showed the hit is an extraction artifact: in the epistemic-status table, `pdftotext` interleaves column three's "corroborated by" against column two's "by an autonomous AI agent system", manufacturing an adjacency that exists in neither the source nor the rendered page. The lint is therefore scoped to the source, which is authoritative for content, with code blocks excluded. Source result: zero doubled words. This is the same table-column class already recorded in this ledger for contiguity probes, encountered from the opposite direction, and the standing practice is extended accordingly: **whole-document text lints run against the source, never against PDF-extracted text, because extraction interleaves table columns.** C-1 is DISCHARGED.

# Section: RATIFICATION -- Rounds 1 and 2 dispositions and the bounded C-1 correction (July 23, 2026)

The project lead, exercising final dispositive authority, ratified the following in-conversation. This entry records that act; it does not confer it. The producer instance carries no ratifying authority under this methodology.

**Ratified, Round 1 (substantive audit of v0.2).**
- The convergence determination: READY-WITH-CONDITIONS from GPT 5.5 (OpenAI, carrying) and Gemini 3.1 Pro (Google, carrying), with Claude Fable 5 advisory under Ruling 3.
- The adjudication of every Round-1 finding as recorded in the v0.3 section, including the CONFIRMED producer-owned defects (all-black gate false; title duplication and heading-number collision; the Appendix A specification failing to parse; code-block content truncated off-page; the four-versus-three source-count contradiction; ASCII rather than mathematical notation for the Munafiq predicates; H1 untestable as written; the false-positive threshold misusing null-hypothesis language; the A-dependence result stated more broadly than testing supported; three separately valid unflagged Appendix A dependencies).
- The intake of Grok's external peer review as peer review rather than as a carrying seat, with its seventeen substantive annotations dispositioned on their merits.
- **The two REFUTATIONS**, both since independently re-tested against the METR primary by both carrying seats in Round 2 and found to hold: that the paper's monitoring statement tracks METR's Figure 8 caption with its conditional intact, and that May 19, 2026 is the report's masthead publication date. The narrower CONFIRMED defect inside the first refutation, the dropped scoping clause, stands repaired at R-5 rather than laundered by the refutation.
- Repair register R-1 through R-20 as applied.

**Ratified, Round 2 (delta re-attestation of v0.2 to v0.3).**
- The convergence determination: CONVERGED PASS-DELTA from two carrying seats of different vendor families, each having independently re-derived the instrument receipts, diffed the pinned baseline, verified the discharge mapping without crediting this ledger, re-tested both refutations against the primary, and re-run G6, G7, and G8 with their own tooling.
- F-DO-01 LOW as CONFIRMED and producer-owned, with its anchor-boundary root cause and the three failed producer probes recorded.
- The intake block F-SP-001 CRITICAL as CONFIRMED and producer-owned, its root cause recorded, and its class recurrence against dissertation F-DG-12 acknowledged rather than minimized.
- The C-1 correction as executed within the synthesis's own pre-authorization, diff-proven to exactly one hunk, one line, one token at the named locus.
- The seat-report notes as registration-only: the Google seat's receipt-table completeness limitation, and the OpenAI seat's correct exclusion of its own analysis-generated auxiliary files from producer evidence.

**Ratified, standing additions to the gate suite.** G7 SHEC-PARSE, G8 NO-TRUNCATION, G9 BRIEF-RECEIPT-CONCORDANCE (rev B scoping), exhaustive G6 ALL-BLACK, and the G5 doubled-word lint scoped to source. The G9 rev A specification defect, in which a gate would have failed closed on a correct packet, is ratified as recorded rather than removed.

**Attestation status after ratification, stated without inflation.** v0.3 is the attested instrument: it carries Round-2 CONVERGED PASS-DELTA. v0.4 is v0.3 plus the pre-authorized copy-edit, covered by the synthesis's own disposition and diff-proven to that single locus, and is the deposit candidate. Ratification closes the audit cycle. It does not convert READY-WITH-CONDITIONS into validation of the framework, does not attest the paper's scholarship beyond the legs the seats actually ran, and does not alter the paper's own disclosed limits: the evidence freeze stands, the UNKNOWN markings stand, and the contribution claim remains guarded by falsification condition F3.

**Post-ratification discipline.** Any edit to any instrument or governance member from this point produces a new version outside this convergence and restarts the audit clock. The three open punch items (S-2 projection-family adequacy against canon Chapter 7, S-3 tripwire-pause feasibility grounding, S-4 corrigendum watch on both companies' completed investigations) are carried forward and none blocks deposit.

**Next act, lead-held.** arXiv cs.CR deposit of v0.4 under the same versioning discipline used for the monograph, with the paper's own A1 commitment binding: any corrigendum arising from the completed joint investigation ships as a tagged new version, never as a silent edit.

# Section: v0.5 -- Post-freeze AX-SH 5 (Axiom 5, evidence independence) integration (July 24, 2026)

Governing conventions unchanged from the prior sections: this ledger is source of truth over prose;
entries are append-only; no prior section above was edited to create this one; severities UPPERCASE;
double hyphens in all non-LaTeX authored text; the ledger is producer-COMPILED and carries NO
external attestation. Verify against the substrate, not against this compilation.

Status: **v0.5 PRODUCER PASS. Not independently re-attested. No new convergence claimed for v0.5.**
The v0.4 Round-1 and Round-2 convergence and the lead ratification recorded above apply to v0.4 and
DO NOT extend to the v0.5 additions.

## 1. What v0.5 is, stated precisely

v0.5 is a controlled, append-only methodological extension of the ratified v0.4 baseline. It
integrates the companion paper "Is Evidence Independence an Axiom? Decomposing a Proposed Extension
to AX-SH" (Bilal Syed Arfeen, v1.0, July 24, 2026, DOI 10.5281/zenodo.21539074, Zenodo record
https://zenodo.org/records/21539074) by adding a clearly labeled Axiom 5 layer on top of the
unchanged v0.4 analysis. It does not rewrite the incident record. The July 22, 2026 incident-evidence
freeze and every incident fact are preserved. v0.4 correctly applied the four-axiom canon then
available; v0.5 adds A5 only after the companion paper's publication. No v0.5 passage claims v0.4
applied A5.

Baseline pinned: SHUDP v0.4, DOI 10.5281/zenodo.21522932, concept DOI 10.5281/zenodo.21522931.
The v0.4 source is shipped byte-identical in this packet as SHUDP_v0_4_baseline_source.md
(SHA-256 79909d1003af9b1f45777afea8c85a92d985aed1c751b35abaf840db307c9117, matching the ratified
v0.4 source receipt recorded in the v0.4 section above). The companion paper is shipped byte-identical
as AXSH5_paper_v1_0.pdf
(SHA-256 5c976762042660aaaf6e260f2538b0dae8db37e1d16bad0e8f94d3840d39a14a).

## 2. Change register (v0.4 -> v0.5)

Every v0.5 change is append-only. All v0.5 changes are identified collectively by the paper's Version
and Provenance Note and individually mapped in the delta memorandum
(SHUDP_v0_5_DELTA_MEMORANDUM.md), which is the authoritative per-change map and is summarized here as
a register. Newly added analytic sections and passages carry an explicit `[v0.5 post-freeze
addition]` label in the source where a label fits cleanly (13 such labels); short edits, notably the
abstract and the contribution wording, are covered by the Version and Provenance Note and the delta
memorandum rather than by an inline label. No claim is made that every substantive insertion carries
a literal inline tag.

- **D-1 Version and Provenance Note (NEW).** v0.5 provenance note with companion DOI and v0.4
  baseline DOIs; author byte and not-yet-re-attested review status preserved.
- **D-2 Abstract (EXTENDED).** No longer implies the framework stops at four axioms; states the
  original case analysis used the then-published four axioms and that v0.5 adds A5. No incident
  sentence changed.
- **D-3 Contributions (EXTENDED).** Four-way distinction explicitly preserved; A5 named as a new
  post-freeze contribution (5); no fifth member added to the four-way distinction.
- **D-4 What This Framework Adds (EXTENDED).** A5 existential requirement added; specification-versus-
  prevention disclaimers preserved and extended to A5.
- **D-5 Declared Objects (EXTENDED).** Retrospective analytic A5 reconstruction of S, E*, B, W, L, and
  the contestable WithinAuth interpretation, labeled analytic and not an assertion about internal
  artifacts.
- **D-6 Axiom 5 adjudication (NEW, after A4).** Verdict NOT EVALUABLE from the public record;
  Hugging Face telemetry named as a candidate substrate-independent witness; no failure inferred from
  missing disclosure; event-level UNKNOWN preserved and kept distinct from axiom-level NOT EVALUABLE.
- **D-7 Thin-ecosystem reinterpretation (EXTENDED).** F6 reinterpreted through A5 without erasing the
  A4 analysis.
- **D-8 Munafiq/diagnostic (EXTENDED).** A5 limited to evidentiary admissibility; does not claim to
  resolve the aligned-output-set underdetermination.
- **D-9 Appendix A SHEC (EXTENDED).** New evidence_independence YAML block; fail-safe pause retained
  as control mechanism and labeled not-A5; machine-readable validity preserved; parser gate executes
  the A5 block.
- **D-10 Axiom-compatibility (EXTENDED).** A5 compatibility stated separately from A1-A4.
- **D-11 Prospective experiment (EXTENDED).** H5 and evidence-independence arm added; substrate
  independence not conflated with operator independence.
- **D-12 Falsification F7 (NEW).** A5-specific falsification condition.
- **D-13 Sources (EXTENDED).** Exact companion citation and DOI added; all existing source URLs
  preserved; reciprocal related-identifier recommendations recorded in DEPOSIT_METADATA_v0_5.md.
- **D-14 Limitations (EXTENDED).** Finite paper-proof status belongs to the companion paper; SHUDP
  relies on it and does not re-prove it; public record establishes neither A5 satisfaction nor
  violation.
- **D-15 Conclusion (EXTENDED).** States exactly what A5 adds and what remains UNKNOWN.

Sections intentionally unchanged are enumerated in Section 3 of the delta memorandum (the incident
record, the four-axiom adjudications, the diagnostic negative result, F1-F6, H1-H4, the four-axiom
YAML blocks, Appendices B-D, and all existing source URLs).

## 3. Formal-interpretation fidelity check (producer-run)

The producer verified, by direct comparison against the companion canonical source, that the v0.5 A5
material preserves the companion decomposition:

| Interpretation point | v0.5 handling | Result |
|---|---|---|
| Only A5.1 survives as Axiom 5 (via WithinAuth control predicate) | A5 stated over WithinAuth control, not authority labels | PRESERVED |
| A5.2 causal gating is NOT Axiom 5 (proposed SHIELD/control principle) | Stated as proposed control principle, not part of A5 | PRESERVED |
| A5.4 operator independence is NOT Axiom 5 (deployment condition) | Stated as separate deployment condition | PRESERVED |
| A5.3a no-default and A5.5 boundary are theorems; A5.3b open requirement | Stated as such | PRESERVED |
| A5 is not a fifth projection/object | Explicit in abstract, contributions, adds-section, YAML flag | PRESERVED |
| Axiom-level UNSATISFIED distinct from event-level UNKNOWN | Stated in adjudication, YAML, limitations, conclusion | PRESERVED |
| Incident verdict remains event-level UNKNOWN | Preserved unchanged | PRESERVED |

## 4. Gate suite executed (producer-run, NOT external attestation)

Executed by build_v05.py (shipped in packet). Per Ruling 4, these earn no absence-credit: a seat
must verify them independently rather than crediting their presence here.

| Gate | Result |
|---|---|
| G-YAML (SHEC-PARSE, incl. A5 evidence_independence block, real YAML parser) | PASS |
| G-DASH (no U+2013/U+2014/U+2015 in authored source) | PASS |
| G-BYTE (baseline source + AX-SH 5 PDF byte-identical to inputs) | PASS |
| G-META (PDF Author = Bilal Syed Arfeen; Title exact; version in subject/keywords) | PASS |
| G-MONO (zero chromatic color operators; zero chromatic pages; exhaustive) | PASS |
| G-QPDF (qpdf --check structural validation) | PASS |
| G-CONCORDANCE (section headings identical across source/PDF/HTML/DOCX) | PASS |
| G-CONTENT (evidence-freeze language, companion DOI present, no fifth-projection claim) | PASS |
| Packet SHA256SUMS internal verification | PASS (see SHA256SUMS.txt) |

The G-YAML gate validates that the A5 evidence_independence block declares E*, B (with a temporal
floor), W, L, per-event witness commitments, and a WithinAuth interpretation quantified over the
acting substrate only, and that its missing-evidence path maps to A5 UNSATISFIED (axiom level) plus
event-level UNKNOWN, and that A5 is flagged not-a-fifth-projection.

## 5. Producer self-check

- Forbidden dash characters (U+2013/U+2014/U+2015) in the v0.5 source: 0. PASS.
- v0.5 inline post-freeze labels present where a label fits cleanly: 13 labels. The abstract and
  contribution edits are covered by the Version and Provenance Note and the delta memorandum, not by
  an inline label; the governance text claims exactly this and no literal every-insertion tagging
  claim is retained. PASS.
- Prior ledger history not edited: the v0.2 through ratification sections above are byte-identical to
  the ratified v0.4 ledger (SHA-256 39563bb25e8ab78eab75a396cff57066f5742803d589d8e46fd748c8b04e9d4f);
  this v0.5 section is appended only. PASS.
- Incident-evidence freeze language present in source, PDF, HTML, DOCX. PASS.
- A5 not presented as a fifth projection in any render. PASS.
- Companion DOI present in every render. PASS.

## 6. Receipts, v0.5 (as built by the producer; SHA256SUMS.txt is authoritative)

Instrument and packet receipts are recorded authoritatively in the packet-level SHA256SUMS.txt,
which covers every packet member except itself and is verified by `sha256sum -c`. Per the v0.4 S-4
discipline, this ledger does not restate instrument hashes as a competing source of truth; the
build tool records them and SHA256SUMS.txt governs. The v0.5 instrument members are:
SHUDP_v0_5_source.md, SHUDP_v0_5.pdf (28 pp), SHUDP_v0_5.html, SHUDP_v0_5.docx. The v0.4 baseline
source and the companion AX-SH 5 PDF are shipped byte-identical and their hashes are pinned in
Section 1 above.

## 7. What this ledger section does NOT claim

No external audit round has been run on v0.5. No convergence exists for v0.5. No seat has attested
any v0.5 receipt. The gate results in Section 4 are producer-run and earn no absence-credit. This
producer pass is **not** independent peer review and is **not** model-council convergence. The v0.4
attestation is not transferable to the v0.5 additions.

## 8. Next cycle

If v0.5 is to be attested, the correct instrument is a delta-scoped re-attestation against this
change register (D-1 through D-15) and the intentionally-unchanged list in the delta memorandum:
two carrying seats of different vendor families independently re-derive the instrument receipts,
diff the pinned v0.4 baseline against v0.5 and confirm every hunk is inside the register with no
out-of-scope substantive change to the incident record or the four-axiom adjudications, verify the
formal-interpretation fidelity table in Section 3 against the companion canonical source, and re-run
the gate suite (including G-YAML over the A5 block) with their own tooling. Until then v0.5 is a
producer deposit candidate, not an attested instrument. The producer instance (Anthropic lineage)
is excluded from the auditor pool and carries no verdict.

## 9. Parent-QA findings and dispositions (producer revision pass, July 24, 2026)

A parent-QA review of the first v0.5 build returned three publication defects. All three were
corrected through the build chain (source + build_v05.py), not patched externally, and the renders
were regenerated. This subsection is appended; no earlier ledger content was edited to create it.

**F-QA-01 | MEDIUM | PDF cover title parity.** The first-build PDF cover visibly ended at
"Model-Evaluation Escape" while DEPOSIT_METADATA and the claimed exact title also carried "and
Cross-Organizational Compromise," so the visible title and the metadata/exact title diverged.
Disposition: CONFIRMED, producer-owned. The build script's short cover/metadata title constant was
the root cause; the full title had never been carried on the visible cover, in the PDF metadata
Title, or as a canonical source title line. Repair QA-1: the exact full title -- "Declared Isolation
and Executable Containment: A Structural-Honesty Analysis of the July 2026 Model-Evaluation Escape
and Cross-Organizational Compromise" -- is now set identically as (i) the first-line H1 of the
canonical source, (ii) the PDF cover title, (iii) the PDF metadata /Title, (iv) the HTML title, and
(v) the DOCX title. The cover title style wraps rather than clips and was visually confirmed on the
rendered cover. A standing title-parity gate (G-TITLE) now checks byte-exact title identity across
source, PDF metadata, PDF cover text, HTML, and DOCX.

**F-QA-02 | LOW/MEDIUM | adjudication finality.** The first-build abstract described the A5 verdict
as a "recommended verdict: NOT EVALUABLE," framing the paper's own adjudication as a recommendation.
Disposition: CONFIRMED, producer-owned. Repair QA-2: the abstract now reads "an Axiom 5 adjudication
(NOT EVALUABLE from the public record at the axiom level, with the event-level adjudicative verdict
preserved as UNKNOWN)"; the adjudication-section heading already read "Adjudication: NOT EVALUABLE
from the public record" and is unchanged. The delta memorandum D-6 entry was corrected to state the
verdict as the paper's adjudication rather than a recommendation. The axiom-level NOT EVALUABLE
status remains explicitly distinct from the event-level UNKNOWN verdict everywhere it appears.

**F-QA-03 | LOW | provenance-claim precision.** The first-build Version and Provenance Note said
"Every v0.5 addition is marked as post-freeze and analytic" and the delta memorandum said every
addition is tagged `[v0.5 post-freeze addition]`, but the abstract and some short extended passages
carry no literal inline tag. Disposition: CONFIRMED, producer-owned; the literal every-insertion
tagging claim was false. Repair QA-3: the governance claim was revised to the exact truth in the
Version and Provenance Note, in the delta memorandum, and in Sections 2 and 5 of this ledger --
namely that all v0.5 changes are identified collectively by the Version and Provenance Note and
individually mapped in the delta memorandum, and that newly added analytic sections and passages
carry an explicit post-freeze label where a label fits cleanly (13 such labels), while short edits
such as the abstract and contribution wording are covered by the note and the memorandum rather than
by an inline label. No false literal-tagging claim is retained.

**Gate suite after the QA revision.** G-YAML, G-DASH, G-BYTE, G-META, G-MONO, G-QPDF,
G-CONCORDANCE, G-CONTENT, and the new G-TITLE all PASS; packet SHA256SUMS re-verifies. This remains
a producer pass: the QA repairs are not an independent re-attestation, and no v0.5 convergence is
claimed.

# Section: v0.5 -- Model-council delta re-attestation and governance-only LOW absorption (July 24, 2026)

Governing conventions unchanged: this ledger is source of truth over prose; entries are append-only;
no prior section above was edited to create this one; severities UPPERCASE; double hyphens in all
authored text; the ledger is producer-COMPILED and carries NO external attestation. Verify against
the substrate, not against this compilation.

Status: **v0.5 governance absorption pass. Two independent cross-vendor carrying seats returned PASS
on the exact pre-absorption archive. This is model-council delta re-attestation, NOT human peer
review. Final exact-archive council acknowledgment is an external act against the post-absorption
archive and is not claimed here.**

## 1. Scope and nature of this pass

This is a governance-only absorption pass. It does not alter the scholarly content of the paper.
The four instrument files (SHUDP_v0_5_source.md, SHUDP_v0_5.pdf, SHUDP_v0_5.html, SHUDP_v0_5.docx)
are preserved byte-for-byte from the attested pre-absorption archive. Only the non-instrument build
tool and governance/metadata members were changed, plus the addition of the two seat reports, the
council synthesis, this ledger section, and the council-absorption receipt.

Pre-absorption archive audited by both seats:
459cf39b8d59ecad0057617590448429daeb655b8b338ce176915895bba0bf59  SHUDP_v0_5_PUBLICATION_PACKET.zip

## 2. Seats, independence, and report receipts

Two independent carrying council seats of different vendor families delta-audited the exact
pre-absorption archive. Each extracted the archive fresh, ran commands directly, and wrote its report
from its own checks; neither is the producer lineage (Anthropic/Claude).

| Seat | Vendor family | Verdict | In-packet report | Report SHA-256 |
|---|---|---|---|---|
| OpenAI GPT-5.5 | OpenAI | PASS | SHUDP_v0_5_SEAT_REPORT_openai-gpt-5.5.md | bcf26eb1ffed5d80f3637b5a9a83cafdc0dea838a312e72f4603ead7bf3dd880 |
| Google Gemini 3.1 Pro | Google | PASS | SHUDP_v0_5_SEAT_REPORT_google-gemini-3.1-pro.md | 0945363f8a5ff620e3685996bd2c041af499be35338b21da1d61f9cbc9a642c4 |

Both seat reports are copied into the packet byte-identical to the returned originals. Convergence:
two carrying seats of different vendor families, satisfying the standing cross-vendor rule. The
producer instance carries no verdict.

## 3. Findings and severity convergence

Zero CRITICAL, HIGH, or MEDIUM findings from either seat. One LOW finding, absorbed:

**F-OGPT55-01 | LOW | build_v05.py default CLI behavior.** The default invocation `python
build_v05.py` ran `all`, which regenerated PDF/HTML/DOCX before verifying. Because DOCX builds are
not byte-deterministic, an auditor running the default against an exact extraction could inadvertently
change the DOCX hash (the OpenAI seat disclosed exactly this event and corrected its own receipt by
restoring the archived DOCX before finalizing; see Section 5). Not a publication-content defect.
Disposition: CONFIRMED, producer-owned, ABSORBED. Repair: build_v05.py now defaults to VERIFY-ONLY;
regeneration requires an explicit `build` or `all` command; clear usage/help and a safety notice are
added. The verify-only default was confirmed to mutate no instrument file (instrument hashes
identical before and after a default run). No instrument byte was touched by this absorption.

Google Gemini 3.1 Pro recorded five LOW/INFO entries; all are PASS confirmations (archive hash,
delta scope, AX-SH 5 treatment, verifier gates, PDF visual), not adverse findings.

## 4. Instrument files -- UNCHANGED (byte-for-byte)

The four instrument members are byte-identical to the pre-absorption archive:

| Instrument member | SHA-256 (unchanged) |
|---|---|
| SHUDP_v0_5_source.md | 1ddc54f0b245953c6bf2f2afd85e9c4119cc5d0da496f2ef3a2751ac239b2438 |
| SHUDP_v0_5.pdf | 4f2a3359858fa63c7a8b378b3bf49dcde57ff69740d90aec851742dca5fe145b |
| SHUDP_v0_5.html | 5e4ac97a43c35851caef08ecbce78219a691aa7f63ea467b9e98de11a76c9b99 |
| SHUDP_v0_5.docx | 394447d56b400e77e6a10263a2a5a69ddb0377473fc9c3ac3546d035f70dec39 |

## 5. Corrected receipt history

The OpenAI GPT-5.5 seat disclosed that its first run used the then-default `all` mode, which rebuilt
artifacts; the regenerated DOCX differed bytewise (non-deterministic build) while PDF and HTML
matched. The seat restored SHUDP_v0_5.docx from the fresh archive extraction, re-confirmed all
checked files matched the archive bytes, and recorded the corrected (archived) DOCX hash
394447d56b400e77e6a10263a2a5a69ddb0377473fc9c3ac3546d035f70dec39 as dispositive. The Google seat used
a fresh-extraction workflow and recorded no such event. F-OGPT55-01 absorbs the root cause so the
default action can no longer regenerate artifacts.

## 6. Gates re-run after absorption (producer-run; SHA256SUMS.txt authoritative)

qpdf --check PASS; title/metadata parity (G-TITLE, G-META) PASS; YAML/A5 block (G-YAML) PASS;
forbidden-dash (G-DASH) PASS; monochrome (G-MONO) PASS; source/PDF/HTML/DOCX concordance
(G-CONCORDANCE) PASS; frozen-facts and content (G-CONTENT: evidence freeze, companion DOI,
not-a-fifth-projection, NOT EVALUABLE, event-level UNKNOWN) PASS; byte-identity (G-BYTE) PASS.
Packet SHA256SUMS re-verified from a fresh extraction. Full gate outputs are recorded in the
in-packet council-absorption receipt (SHUDP_v0_5_COUNCIL_ABSORPTION_RECEIPT.md).

## 7. What this section does NOT claim

This is model-council delta re-attestation, NOT independent human peer review, and is not presented
as equivalent to it. The seat PASS verdicts are delta-scoped to the pre-absorption archive. Because
the absorption changed the build tool and governance/metadata members, the final exact-archive
council acknowledgment is an EXTERNAL act to be performed against the post-absorption archive hash
recorded in the council-absorption receipt; it is not claimed here. The v0.4 attestation, the
parent-QA repairs, and this delta re-attestation together do not validate the AX-SH 5 extension or
the SHUDP framework; the evidence freeze, the UNKNOWN markings, and the Axiom 5 NOT EVALUABLE /
event-level UNKNOWN verdicts stand.

---

# Bismillah ir-Rahman ir-Rahim
