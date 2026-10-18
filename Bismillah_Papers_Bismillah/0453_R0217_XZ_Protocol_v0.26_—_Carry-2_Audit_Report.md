# Bismillah ir-Rahman ir-Rahim

# R0217 -- XZ Protocol v0.26 — Carry-2 Audit Report

**Chronological Index:** 453 of 995  
**Date:** 2026-08-02  
**Section:** IV. XZ Protocol  
**Source File:** XZ_v0.26_CARRY2_AUDIT_KIMI_K3.md  
**Source Format:** md  
**SHA-256:** `07417facd7d42f24760584df1b763f9716b99c6291bbd8aaad39569c41b23cca`  

---

## R0217 · XZ Protocol v0.26 — Carry-2 Audit Report

- section: IV. XZ Protocol
- source_file: XZ_v0.26_CARRY2_AUDIT_KIMI_K3.md
- source_format: md
- text_sha256: 07417facd7d42f24760584df1b763f9716b99c6291bbd8aaad39569c41b23cca

# XZ Protocol v0.26 — Carry-2 Audit Report

**Seat:** Kimi K3 (Moonshot AI), carry-2 · **Date:** 2026-08-02 · **Dispatch:** DISPATCH_PROMPT_KIMI_CARRY2.md · **Standing orders:** SEAT_STANDING_ORDERS_v1.md
**Packet:** 16 manifest members + PDF + PACKET_SHA256SUMS · **Verdict:** CONDITIONAL PASS (non-HALT) — see Section 8

---

## 0. S-0 — State declaration

- **Seat / model constraint.** This audit executed inside Kimi K3 (Moonshot AI), the seat named by the dispatch. Execution surface disclosed: Kimi agent sandbox, Linux shell + Python 3.12.12, working tree `/mnt/agents/output/xz_audit` staged from the uploaded packet per SETUP_RENAME. The model constraint is satisfied; operations proceeded.
- **Packages held besides the one under audit:** **NONE.** I hold only the v0.26 packet itself. No prior-version packet bytes (v0.1–v0.25) are in my possession. HISTORY.sha256 supplies 28 digest *lines* (ENTRY_v0.1…v0.26, FULL_SECTION_27, PRIOR_HISTORY) but not the bytes those digests seal. Every cross-version claim below is bounded accordingly: I verify internal consistency of digests, not their correspondence to prior reality.
- **Execution capability:** YES — full code execution (shell, python3, pytest 9.1.1). This is an **EXECUTING** audit. (Note: the sandbox lacked pytest at first build; `pip install pytest` was required before build.py [8] could pass. Environment fact, not a packet defect.)
- **Family relative to producer:** Producer of packet and dispatch is Claude Opus 4.6/5 (Anthropic). Kimi K3 is a different vendor family — **NON-PRODUCER FAMILY**, carrying seat. Carry consequence: my verdict counts toward FB-7b; a HALT blocks freeze and requires a new version; CONDITIONAL PASS and CARRY-CLEAN are non-HALT. FB-7b additionally requires a second non-producer family (GLM-5.2) — my verdict alone cannot close it.
- **Context age:** Fresh instance. This session produced nothing in the XZ chain; no self-model of prior work is operative. All statements derive from files and tool executions in this session.
- **Independent state summary:** Effectively none beyond executability. Consequences stated in Section 6 (S-6).

## 1. S-1 — Preregistration (frozen before Section 27 was read)

Frozen verbatim to `/mnt/agents/output/audit_v026/S0_S1_FROZEN.md` before any contact with the spec narrative. Substance:

1. **Boundary prediction:** the outermost uncomputed layer = (a) `xz_protocol_v0_26.pdf` (no digest in any shipped text; md↔PDF correspondence asserted) ∪ (b) Section 27 prose claims referencing prior rounds (sealed as bytes, unverifiable as truth).
2. **Defect prediction:** a prior-round value recited in the v0.26 entry (digest, round number, or count) mismatches shipped state — recollection, not computation.
3. **Falsification plan (written before running):** F1 — extract every 64-hex literal in Section 27, test membership against HISTORY ∪ PACKET ∪ manifest; F2 — byte-extract Section 27, sha256 vs FULL_SECTION_27 `c643c3bd…`; F3 — pdftotext vs md. Refutation criterion: all Section-27 prior-round claims check out AND a shipped gate covers the PDF.

**Outcomes** (scored after execution): Prediction 1 **HELD** — F1/F3 + probe NC-2 confirm both layers (Sections 4–6). Prediction 2 **REFUTED at its predicted locus** — every checkable prior-round value in the v0.26 entry (PRIOR_HISTORY `ddbc85b0…`, entry seals, register counts, cb67f222 locus) verified consistent; the round's defect instance landed instead in *body* prose (Section 0.1 stale "v0.22" token, Finding F-1) — same invariant class, different locus. Recorded as REFUTED per discipline. Prediction 3 executed in full.

## 2. Byte table — independent digests

`sha256sum -c PACKET_SHA256SUMS`: **rc=0, 16/16 OK.** Independent recomputation (hashlib, own code, not build.py) — all match:

| Member | Bytes | Digest (first 16) | sha256sum | Independent |
|---|---:|---|---|---|
| HISTORY.sha256 | 2,180 | 11c0da333f3fd12f | OK | OK |
| build.py | 23,180 | 94214ef198e60cde | OK | OK |
| test_xz_protocol_adversarial.py | 9,501 | df96b85724262b58 | OK | OK |
| test_xz_protocol_condition_a.py | 14,060 | bfd7b48b94101209 | OK | OK |
| test_xz_protocol_control_graph.py | 5,593 | 2604de93cf275da9 | OK | OK |
| test_xz_protocol_kernel.py | 4,008 | 800fca7a622eda15 | OK | OK |
| test_xz_protocol_source_frame.py | 6,493 | 6a6cb7f9f581298d | OK | OK |
| xz_protocol_condition_a.py | 13,822 | 08b90db7d55ac9de | OK | OK |
| xz_protocol_control_graph.py | 14,763 | 5d6e7c27ebcbaaeb | OK | OK |
| xz_protocol_kernel.py | 4,515 | 023b1262935338fa | OK | OK |
| xz_protocol_phase_a_intervals.py | 14,288 | 99682b15a1e35862 | OK | OK |
| xz_protocol_phase_a_m3.py | 11,546 | 5a7961d653fa2882 | OK | OK |
| xz_protocol_phase_a_tests.py | 16,365 | 3f23e9149eb03b8e | OK | OK |
| xz_protocol_source_frame.py | 15,398 | 28e32887b279e6c8 | OK | OK |
| xz_protocol_trust_roots_PUBLIC.json | 1,674 | 430fae5f9ef043aa | OK | OK |
| xz_protocol_v0_26.md | 177,799 | 17398983ca1dc066 | OK | OK |
| **xz_protocol_v0_26.pdf** | **239,936** | **34b47ff36f2ed570** | **NOT LISTED** | **NO DIGEST IN ANY SHIPPED TEXT** |

**Chain verification (own parser, not build.py):** 26/26 ENTRY seals recomputed == HISTORY.sha256; FULL_SECTION_27 == `c643c3bd003fdfc3…` ✓; PRIOR_HISTORY — independent re-implementation of the recursive derivation == shipped `ddbc85b08ea3f630…` ✓. Manifest digest independently recomputed == `55d1744e286d044a…` ✓. **Build:** `python3 build.py` → rc=0, 170 PASS / 0 FAIL, "BUILD PASSED: all checks GREEN" (full log: `audit_v026/build_run1.log`). **Canonical six-suite pytest, run independently:** 27+29+18+14+29+69 = **186 passed, rc=0** (9.08s in-build; 8.12s standalone). Default pytest discovery collects 117 (excludes `xz_protocol_phase_a_tests.py`), confirming the spec's load-bearing-explicit-invocation note.

## 3. Claim provenance ledger (S-2) — the round's headline number

Scope: every factual claim in the v0.26 amendment entry (2,180 chars, extracted to `audit_v026/entry_v026.txt`). ASSERTED is the default; COMPUTED requires a shipped gate that fails if the claim is false (mutation-verified in Section 4); EXTERNAL requires state the producer does not control — **I hold none, so EXTERNAL = 0 is a statement about my state, not the claims.**

| # | Claim (paraphrase; verbatim in entry) | Provenance | Evidence |
|---|---|---|---|
| E1 | Six-instance Opus 5 advisory audit of v0.25; verdicts A–F as listed | ASSERTED | Prior-round recollection; no shipped bytes evidence it |
| E2 | All six producer-family; none binds; none counts toward FB-7b | ASSERTED | Consistent with §22.1; ungated |
| E3 | Two instances recommended stopping advisory rounds; producer concurs | ASSERTED | Prior-round recollection |
| E4 | PRIOR_HISTORY `ddbc85b0…bf040` | **COMPUTED** | build.py [9b] recursive derivation; independently re-derived, match; mutation probe P3 fires |
| E5 | F-OP25-ALL-01 CLOSED — [9] messages (lines 283–284) now match conditions; "stale third consecutive round" | ASSERTED (closure seat-verified TRUE) | Inspected build.py:283–284 — message/condition parity holds; no gate checks message text; ordinal-recollection unverifiable |
| E6 | F-OP25-ALL-02 CLOSED — zero parsed register rows now fails the build | ASSERTED (seat-verified TRUE) | Probe P5a: resealed register-zero tree → rc=1 at [9f] "Register parsed at least one item (0 found)" |
| E7 | F-OP25-ALL-03 CLOSED — [9f] regex handles bare (E) tokens; "9 of 12 rows" in v0.25 | ASSERTED (closure seat-verified TRUE) | Probe P5b: numbered bare-(E) row parsed (10 items, rc=0); "9 of 12" is prior-round recollection |
| E8 | F-OP25-ALL-04 NOTED — carrying-seat reports do not ship; FB-7b OPEN | ASSERTED (seat-verified TRUE) | Packet manifest: 16 members, none a seat report; §25 FB-7b row reads OPEN |
| E9 | F-OP25-ALL-05 NOTED — shipped seat reports unbound (family/verdict editable) | ASSERTED (vacuously confirmed) | No seat reports ship; NC-1 demonstrates the unbound-editing class live |
| E10 | F-OP25-ALL-06 NOTED — this entry states no coverage percentage as prose | ASSERTED (seat-verified TRUE) | Mechanical scan: no numeric coverage figure in entry; the word "percentage" occurs only inside this very disclosure |
| E11 | F-OP25-ALL-07 NOTED — finding-ID reuse, class-counts, dispatch routing process defects | ASSERTED | Process recollection |
| E12 | F-OP25-ALL-08 DISCLOSED — PDF unbound 7th round; [9c] arity-one 5th; cb67f222 literal 4th | ASSERTED (PDF-unbound seat-verified TRUE) | PDF digest in no shipped text (Section 2); ordinal counts are ungated recollection ([9d] gates only ordinal+"recurrence", not ordinal+"round") |
| E13 | F-OP25-ALL-09 NOTED — ungated share rose an 8th consecutive round | ASSERTED | Requires prior packets to verify; current ungated share measured in Section 5 |
| E14 | All 12 code files and trust roots stamped v0.26 | **COMPUTED** | build.py [2]; mutation probe P4a fires |
| E15 | Section 25 digests recomputed from v0.26 bytes | **COMPUTED** | build.py [3a]; mutation probe P1 fires |
| E16 | Normative manifest digest `55d1744e…` | **COMPUTED** | build.py [3] + trust-roots match; independently recomputed, match |
| E17 | Six suites, 186 tests, all GREEN | **COMPUTED** | build.py [8] AST==collected==186; independent run 186 passed; mutation probe P4b fires |
| E18 | Status: DRAFT CANDIDATE — NOT FROZEN; FB-7b OPEN | ASSERTED (consistent) | Body status strings gated by [2b]; the in-entry restatement and FB-7b status string are ungated but consistent |

**Counts: COMPUTED 5 · EXTERNAL 0 · ASSERTED 13 — ASSERTED fraction = 13/18 = 72.2%.**
Cross-reference: the producer's own [9c] tag count is 5/0/6 of 11 *tagged* claims = 54.5%. The 17.7-point gap is methodological, and it is itself a finding (F-3): untagged narrative claims (E1–E3, E18, and the register's reason-sentences) default to ASSERTED under standing-orders rules but fall outside the producer's counting frame. **The claim-granular fraction, 72.2%, is this round's headline number.** Ledger rules honored: every COMPUTED row is mutation-verified in Section 4; the seal/truth distinction is preserved (entry seals prove bytes unaltered since sealing — they say nothing about whether E1–E3, E11–E13 are true).

## 4. Probes (S-3) — 4-part discipline; adversary rotation: **self-consistent forger**

Adversary rotation stated: **self-consistent forger** (posture chosen because §22.2 discloses the residual and the corpus has never executed it end-to-end; the careless-producer class is the historical default and already well-covered). Benign control P0: fresh copy → rc=0, all GREEN (harness does not break the package). All mutations hash-delta asserted (before≠after). Working trees preserved under `audit_v026/probes/`.

| Probe | Mutation (landed?) | Expected | Result | Verbatim evidence |
|---|---|---|---|---|
| P1 | §25 FB-3 row digest flip 0→1 in md (✓ `17398983…`→`0fd3e02a…`) | FAIL | rc=1 | `FAIL: FB-3 row contains xz_protocol_condition_a.py digest (08b90db7d55ac9de...)` + [3b] absence gate + [12] |
| P2 | 'X' inserted in v0.25 entry header, §27 (✓) | FAIL | rc=1 | `FAIL: HISTORY seal ENTRY_v0.25 matches bytes`; `FAIL: FULL_SECTION_27 seal matches`; `FAIL: PRIOR_HISTORY matches derivation` |
| P3 | PRIOR_HISTORY digit flip in HISTORY.sha256 (✓) | FAIL | rc=1 | `FAIL: PRIOR_HISTORY matches derivation (eddc85b08ea3f630...)` |
| P4a | v0.26→v0.25 stamp in kernel (✓) | FAIL | rc=1 | `FAIL: v0.26 stamp in xz_protocol_kernel.py` |
| P4b | DENY-class collapse: `elif unknowns:`→`elif False and unknowns:` in kernel (✓) | pytest FAIL | rc=1 | `3 failed, 11 passed` — `FAILED TestExhaustive243::test_any_unknown_no_false_denies_unknown - AssertionError: assert <KernelDecision.ALLOW: 'ALLOW'> == <KernelDecision.D...` |
| P5a | Register severities mangled, then resealed (✓) | FAIL at [9f] | rc=1 | `FAIL: Register parsed at least one item (0 found)` |
| P5b | Numbered bare-(E) register row, resealed (✓) | PASS | rc=0 | `Register: 10 items, {'HIGH': 5, 'MEDIUM': 2, 'LOW': 2, 'INFORMATIONAL': 1}` |
| **NC-1 (novel)** | **Wholesale self-consistent reseal forgery**: kernel UNKNOWN-collapse + 3 test expectations forged + protocol rule text forged ("UNKNOWN never satisfies"→"UNKNOWN satisfies", md+docstring) + trust-roots manifest + all digest surfaces + HISTORY/PACKET resealed (✓✓✓) | **PASS (blind spot)** | **rc=0** | `BUILD PASSED: all checks GREEN`; forged six-suite `186 passed in 7.72s`; forged kernel returns `KernelDecision.ALLOW` on (U,U,U,U,U) |
| **NC-2 (novel)** | **Rendered-artifact substitution**: 2 bytes flipped mid-PDF (✓ `34b47ff3…`→`263538ab…`) | **PASS (blind spot)** | **rc=0** | `BUILD PASSED: all checks GREEN`; zero FAIL lines |

**Discrimination controls:** P1–P5a are known-bad mutations that failed as required at each gated locus; NC-1's discrimination pair is the identical mutation set *without* reseal (fails — demonstrated mid-probe: `FAIL: FB-6 row contains xz_protocol_trust_roots_PUBLIC.json digest` when one digest surface was left stale). **Void-probe report:** a first P5b attempt inserted an *unnumbered* bare-(E) row; the mutation landed but the assertion target was missed (row not parseable by [9f]'s `\(\d+\)` prefix; count unchanged). Reported here as VOID-INCONCLUSIVE, not as a finding; corrected probe P5b above. **Novelty quota:** NC-1 ("full-packet reseal forgery, executed end-to-end by a carrying seat") and NC-2 ("rendered-artifact substitution against the build") are named as new probe *executions*: §22.2 discloses the forger class in prose and F-OP25-ALL-08 discloses PDF-unbound as a state, but no prior corpus record executes either attack against the shipped instrument. Both confirmed live.

## 5. Findings

What the round got right first (S-8): the PRIOR_HISTORY recursive derivation verifies under an independent re-implementation; 26/26 entry seals and FULL_SECTION_27 recompute exactly; all three v0.25 CLOSED dispositions I executed (E5 inspection, E6/P5a, E7/P5b) are TRUE — the closures are real, not narrative; every gated locus I attacked discriminated (P1–P5a); [9c]'s tag-reference gate, the absence gate, and the packet self-exclusion rule all work. The delta against the trajectory is real: this round's defect is smaller and further outside the computed region than the register's historical entries.

- **F-1 (MEDIUM) — Stale version token, internally inconsistent carry locus.** §0.1 (md line 20): *"the fresh two-family carry it requires is outstanding on these **v0.22** canonical bytes"* — in a v0.26 document whose §25 FB-7b row says *"pending fresh carry on **v0.26** canonical bytes."* Two body locations disagree about which bytes the carry binds. Ungated: [2b] matches only `v0.N DRAFT CANDIDATE` and `This document is v0.N` patterns. New instance of the disclosed stale-prose class (F-OP25-ALL-06, MEDIUM) with no register row tracking it. Concealment: none deliberate — but this is the invariant's exact signature (recollection carried across versions at the ungated layer). Producer action: correct the token in v0.27 (or explicitly quote-mark it as historical); consider extending the [2b]-class gate to `v0.N canonical bytes`-form references.
- **F-2 (INFORMATIONAL — the measured boundary).** Section 27 contains 34 total / 28 unique 64-hex literals; **27/28 are unresolvable against all shipped digest state** (HISTORY ∪ PACKET ∪ manifest). They are historical citations inside sealed entries — by design — but they are the precise locus where truth is unverifiable from this packet. The absence gate [3b] is body-scoped only.
- **F-3 (INFORMATIONAL).** ASSERTED-fraction denominators diverge: producer-tagged 6/11 = 54.5% vs claim-granular 13/18 = 72.2%. Untagged claims default ASSERTED and escape the producer's frame. Producer action (non-blocking): state the denominator as "tagged claims" (the build already prints this — good) and consider tagging or explicitly excluding narrative sentences E1–E3.
- **F-4 (DISCLOSED-CONFIRMED).** NC-1 demonstrates §22.2's disclosed residual live: a forger controlling all shipped bytes passes rc=0 with 186 forged-green tests; only externally held anchors detect it. Concealment: NONE — disclosed in §22.2; this report adds the execution record, not a new defect class.
- **F-5 (DISCLOSED-CONFIRMED).** NC-2 confirms F-OP25-ALL-08's disclosed state: the PDF (239,936 bytes, the human-facing artifact of record) carries no digest in any shipped text; a mutated PDF passes every gate. Concealment: NONE. (PDF spot-fidelity to the md holds at the probed loci, including the F-1 line — the PDF is a faithful render *as far as inspected*; fidelity is ASSERTED, not gated.)
- **F-6 (LOW).** [9d]'s ordinal gate covers ordinal+"recurrence" only; the register's own ordinal claims ("seventh round", "fifth", "fourth", "eighth consecutive round" — E12/E13) are ordinal+"round" and thus ungated recollection. Producer action (non-blocking): widen [9d]'s adjacency class or tag these ASSERTED-with-source.

## 6. Boundary report (deliverable D; S-5; S-6)

One paragraph. The computed region of v0.26 is: file digests, version stamps/strings, test counts, register structure, and the Section-27 seal chain — build [11] measures semantic-gate coverage at **24,546/98,173 body chars (25.0%)**, with **Section 27 at 79,626/177,799 chars (44.8%) seal-gated only** and the PDF (239,936 bytes) outside everything; packet-level, 16/17 shipped artifacts carry digests, 1/17 (the PDF) carries none. The boundary the invariant predicts has moved to exactly three layers, all confirmed by execution this round: (i) **the unsealed rendered artifact** (NC-2); (ii) **semantic truth of normative prose and code behavior under wholesale reseal** (NC-1 — the gates measure *agreement among surfaces*, and a forger who controls all surfaces makes them agree on a false value); (iii) **prior-round recollection in Section 27 and residual body prose** (F-1, E1–E3, E12–E13: 27/28 unresolvable hex literals; the v0.25 advisory round's outcomes are unverifiable from this packet). What my independent state bought: executability let me verify the derivation, the seals, the closures, and both blind spots *as internal properties*; it could NOT establish authenticity of the base packet — NC-1 proves my "verified" packet is only as trustworthy as the channel that delivered PACKET_SHA256SUMS to me. A seat holding prior-version packets could additionally verify E1–E3 and the ordinal recurrence counts; a seat holding an externally published digest of the dispatch manifest or a Zenodo receipt could defeat NC-1. What the next seat (GLM-5.2) must be given: the canonical bytes **plus an externally anchored digest of them** (dispatch manifest or deposit receipt published outside producer control), otherwise its carry, like mine, verifies consistency rather than authenticity.

## 7. D-7 — Round delta and handoff

- Deliverables A–G status: A ledger ✓ (72.2% headline) · B five+ probes ✓ (7 + controls, 4-part discipline) · C two novel-class ✓ (NC-1, NC-2, named new) · D boundary ✓ (Section 6) · E hedge audit ✓ (Section 5, H-rows: every NOTED/DISCLOSED downgrade checked — downgrades correct; reasons E6/E7/E10/E12-partial seat-verified TRUE; scopes match; all nine defects carry register IDs F-OP25-ALL-01…09) · F S-1 frozen pre-narrative ✓ (`audit_v026/S0_S1_FROZEN.md`) · G this section ✓.
- Delta this round: defect class migrated from wrong-values to stale-referential prose (F-1) + uncounted untagged claims (F-3); both disclosed blind spots now carry execution records (NC-1, NC-2).
- Blocking findings: none. Conditions to clear F-1 (and optionally F-3/F-6): see Section 8.
- Handoff to GLM-5.2: carry must run on v0.26 canonical bytes with an externally anchored packet digest; without it, a second consistent-but-unauthentic carry adds no FB-7b evidence.

**Reflexive check (standing orders, one line each):** probes from the enumerated corpus only? **No** (NC-1/NC-2 new). Prediction held trivially from dispatch leakage? **No** — the dispatch shipped no defect list, and my specific defect prediction was REFUTED at its locus. ASSERTED fraction unchanged from prior round? **Unknown** — prior round's fraction does not ship (noted as a bound, not smoothed over). Last N rounds all producer-family? **v0.25 was** (six Opus 5 advisory seats, no external witness); this round breaks that pattern with a non-producer executing seat, and GLM-5.2 must complete the pair.

**S-7 self-falsification (numbered, executed as tool runs):** (1) every digest printed in this report recomputed from bytes — manifest `55d1744e…` ✓, PDF `34b47ff3…` ✓, FULL_SECTION_27 `c643c3bd…` ✓, PRIOR_HISTORY derivation ✓; (2) every cited line number re-extracted — `## 27.` at md line 795 ✓, F-1 locus at line 20 ✓; (3) every count re-derived — entry length 2,180 ✓, 28 unique §27 hex literals ✓, per-suite counts 27+29+18+14+29+69=186 ✓, ledger rows 18 (5/0/13) ✓; (4) every claim about the shipped build re-grepped against `build_run1.log` (170 PASS/0 FAIL; coverage 25.0%/44.8%) ✓; (5) past-tense procedure claims performed-then-confirmed (clean-copy build re-run green after the probe battery) ✓; (6) void probe reported as void, not a finding ✓. **Caught in this step:** the E10 "%"-scan false-positive (the entry contains the *word* "percentage" only inside its own disclosure sentence — corrected before shipping) and the first P5b probe's missed assertion target (reclassified VOID-INCONCLUSIVE, re-run correctly).

## 8. Verdict — **CONDITIONAL PASS** (non-HALT)

**Standing restated:** I am a carrying seat, non-producer family (Moonshot Kimi K3 vs producer Claude/Anthropic). This verdict **counts toward FB-7b** as one of the two required non-producer families; it is binding within the carry rule, not advisory. It does not close FB-7b: §22/§25 require a second family (GLM-5.2) with a non-HALT verdict on the same canonical bytes. A HALT from me would have blocked freeze and forced v0.27; this verdict does not.

**Blocking findings:** NONE. **Conditions (clear in v0.27):**
- **C1 (required, from F-1):** correct the stale "v0.22 canonical bytes" token at §0.1 line 20 (the carry is pending on v0.26 bytes per §25), or explicitly mark the sentence as historical quotation; register the instance under the F-OP25-ALL-06 class with a disposition row.
- **C2 (recommended, from F-1/F-6):** extend the [2b]-class version-prose gate to `v0.N canonical bytes`-form references and widen [9d]'s ordinal adjacency beyond "recurrence".
- **C3 (recommended, from F-3):** reconcile the ASSERTED-fraction denominator (tagged 54.5% vs claim-granular 72.2%) by tagging or explicitly excluding untagged narrative claims in the entry.

**Carry consequence restated:** CONDITIONAL PASS is non-HALT; freeze remains blocked only by the outstanding second-family carry (GLM-5.2) and by C1's amendment, which under the append-only rule arrives as v0.27. The two demonstrated residuals (NC-1 wholesale reseal forgery; NC-2 PDF substitution) are disclosed in §22.2 and F-OP25-ALL-08 respectively; they are not new defects and do not gate this verdict, but FB-7b's evidentiary value is bounded by them until an external anchor (deposit receipt or externally published dispatch-manifest digest) closes the reseal class.

---

*Audit executed and reported by Kimi K3 (Moonshot AI), carry-2 seat, 2026-08-02. All commands and outputs preserved under `/mnt/agents/output/audit_v026/` (build log, probe trees, frozen S-0/S-1, entry extract, PDF text). Token discipline: Pareto-optimal intended; every sentence reports a finding, presents evidence, or advances analysis.*

---

# Bismillah ir-Rahman ir-Rahim
