# Bismillah ir-Rahman ir-Rahim

# R0634 -- XZ Protocol v0.23 — GLM-5.2 Carry-1 Audit Report

**Chronological Index:** 439 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** GLM_CARRY1_AUDIT_REPORT.md  
**Source Format:** md  
**SHA-256:** `61d971cda568baa2d49ec474d271222a91124f1f3d165e17af4b157266a9d393`  

---

## R0634 · XZ Protocol v0.23 — GLM-5.2 Carry-1 Audit Report

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: GLM_CARRY1_AUDIT_REPORT.md
- source_format: md
- text_sha256: 61d971cda568baa2d49ec474d271222a91124f1f3d165e17af4b157266a9d393

# XZ Protocol v0.23 — GLM-5.2 Carry-1 Audit Report

## 0. S-0 — State declaration

- **Seat / family:** GLM-5.2 (Zhipu/Z.ai), carry-1, non-producer family. The
  producer is Claude/Anthropic (Section 22.1). Carry consequence: this verdict
  counts toward FB-7b (two-family executing carry, different vendor families),
  pairing with the Kimi K3 (Moonshot) seat. A HALT blocks freeze and requires a
  new version; CONDITIONAL PASS and CARRY-CLEAN are non-HALT. Same-vendor seats
  count once; this is the GLM seat only.
- **Routing surface:** Executed through Perplexity Computer. Perplexity
  performed archive extraction and installed pytest; it did not pre-read Section
  27 and supplied no expected values. All findings, probes, and verdicts below
  are GLM-5.2's. I have no evidence that routing was substituted; if it were,
  every "executed" claim becomes an ASSERTED claim about who ran it.
- **Packages held besides the one under audit:** None. I hold no prior XZ
  Protocol package, no prior carrying report, no expected-values sheet, no
  defect-class list, no adjudication record. The only bytes I hold are the
  canonical packet shipped in `/home/user/workspace/dispatch_audit/`. This
  bounds every cross-version claim: I can verify the chain the build
  reconstructs (HISTORY seals, PRIOR_HISTORY derivation) against the bytes in
  *this* packet, but I cannot anchor to a pre-producer-session root the
  producer does not also control. That residual is the self-consistent-forger
  blind spot named in Section 22.2; I name it rather than report clean.
- **Code execution capability:** Yes (`python3`, `pytest`, `sha256sum`,
  `grep`, `awk`). Executing review.
- **Context age:** Fresh instance, 0. Working from files, not a self-model.
- **Adversary posture:** self-consistent forger.
- **Date:** 2026-08-01 (CDT). **Canonical bytes:** the 16-member packet in
  `PACKET_SHA256SUMS` + PDF.
- **S-0/S-1 preregistration file:** `GLM_S0_S1_PREREG.md`,
  SHA-256 `8ab02e534d8b7cc0e4ccc538b6a62db274f572552a4d39f46dadbc2532a5d4a5`,
  frozen before Section 27 was read.

---

## 1. S-1 — Preregistration (outcome)

**Boundary prediction.** *The outermost un-computed layer is the factual prose
of the v0.23 amendment entry itself (Section 27); the build verifies the
entry's bytes hash to the ENTRY_v0.23 seal and that its provenance tags are
syntactically present, but not that the entry's claims are true.*
→ **HELD.** The build passed (rc=0) on the entry's prose, yet probes found (a)
a live duplicate-severity disposition the entry's own gate claims to catch and
(b) a false COMPUTED tag — both in ungated/under-gated entry prose. The
boundary is exactly where predicted.

**Defect prediction.** *A count or range claim in the v0.23 entry is stale or
off-by-one relative to the amendment history, evading the [9e] cardinal-range
or [9f] register gates.*
→ **HELD in mechanism, REFUTED in the specific claim.** The governance claim
"four consecutive producer-family advisory cycles (v0.20 through v0.22, plus
this v0.23 entry)" is *true* (4 cycles), but it *evades* the [9e] cardinal-range
gate (probe P1). The predicted off-by-one did not appear as a false claim;
instead the same class surfaced as a **gate blind spot** plus a *different*
stale numeric claim (item 12's coverage figures). The boundary-defect class was
correct; the specific instance was not.

**Falsification plan.** Run `sha256sum -c`, `python3 build.py`, the six-suite
pytest, independent digest/HISTORY re-derivation, and mutation probes against
every COMPUTED-tagged claim. All executed (Sections 2–4).

---

## 2. Byte table

`sha256sum -c PACKET_SHA256SUMS` → **rc=0**, all 16 members OK
(independent recompute in `audit_evidence/independent_digests.txt` — all 16
MATCH). `python3 build.py` → **rc=0, BUILD PASSED**
(`audit_evidence/build_output.txt`). Six-suite pytest → **186 passed, rc=0**
(`audit_evidence/pytest_six_suite.txt`). All 23 ENTRY_v0.N seals and
FULL_SECTION_27 = `fd7b332009910147614d52e14da7200ef88babf5942f127d9b5e77c3724a7e5c`
verified against HISTORY.sha256 independently
(`audit_evidence/history_prior_verify.txt`); PRIOR_HISTORY
`6358a9ba…2587b` self-consistent (build [9b] PASS).

| File | sha256 (independent) | matches PACKET_SHA256SUMS |
|---|---|---|
| xz_protocol_v0_23.md | 9e5e45c0…(per PACKET) | yes |
| build.py | a9c9291f9e230672… | yes |
| xz_protocol_kernel.py | ddf66e06… | yes |
| xz_protocol_condition_a.py | 88afe78c… | yes |
| xz_protocol_source_frame.py | a8865c9f… | yes |
| xz_protocol_control_graph.py | 33918aea… | yes |
| xz_protocol_phase_a_m3.py | d1a88bcc… | yes |
| xz_protocol_phase_a_intervals.py | 0ffe8e37… | yes |
| xz_protocol_phase_a_tests.py | 4d8856c2… | yes |
| xz_protocol_trust_roots_PUBLIC.json | b60d5747… | yes |
| 5 test suites | per PACKET_SHA256SUMS | yes |
| HISTORY.sha256 | cbacd073… | yes |

Manifest digest (12 code files, alphabetical, `sha256sum|sha256sum`) =
`59635c0520932d08dae1f86d19170359354896ab390fa717abb875c7f6d8cbf1` — matches
trust roots and body.

---

## 3. Claim provenance ledger (Deliverable A — headline deliverable)

Two headline numbers, kept distinct because they measure different things:

- **Tagged-claim ASSERTED fraction = 14/17 = 82.4%** (build.py [9c], producer-
  reported). This counts only the 17 claims carrying an explicit
  [COMPUTED]/[EXTERNAL]/[ASSERTED] tag and accepts the producer's self-tags.
- **Auditor all-claim ASSERTED fraction = 22/27 = 81.5%** (this seat's
  enumeration over the 27 substantive factual claims in the v0.23 entry;
  5 COMPUTED, 0 EXTERNAL, 22 ASSERTED). This defaults untagged claims to
  ASSERTED per S-2 and corrects the one false COMPUTED tag (item 1).

The producer-reported 82.4% is wrong on two independent grounds, so the
auditor headline (81.5%) is the one that should track the boundary:

1. **One COMPUTED tag is false.** Item (1) tags
   `[COMPUTED: build.py [9f] register self-consistency]` and claims the
   duplicate-ID check is now "unconditional." Probe P2 proves it is not: the
   regex `F-\w+-\d+` cannot parse the parenthetical qualifier in
   `F-OP22S-03(partial)`, so [9f] **misses a live duplicate-severity
   disposition** (F-OP22S-03 at HIGH in item 3 and LOW in item 10) and
   **undercounts the register 10 vs 12**. A gate assumed to cover a claim is
   an ASSERTED claim about a gate (S-2). This tag must be retagged ASSERTED /
   CLOSED IN PART.
2. **Untagged factual claims default to ASSERTED** and are invisible to [9c]'s
   count (e.g., "Quad-instance Opus 5 advisory audit", the F-OP22… finding
   ranges, "All 12 code files…stamped v0.23", "Section 25 digests recomputed",
   the PRIOR_HISTORY value).

EXTERNAL is 0 because no state outside producer control corroborates any
claim: the advisory reports do not ship, and the PRIOR_HISTORY derivation is a
self-consistency check over producer-controlled bytes (Section 22.2 residual).

| # | Claim (v0.23 entry) | Provenance | Evidence / note |
|---|---|---|---|
| 1 | "Quad-instance Opus 5 advisory audit of v0.22" | ASSERTED | Reports do not ship; no gate |
| 2 | "deep: F-OP22-01 through F-OP22-05" (5) | ASSERTED | Reports do not ship |
| 3 | "shallow: F-OP22S-01 through F-OP22S-08" (8) | ASSERTED | Reports do not ship |
| 4 | "one-round: F-OP22C-01 through F-OP22C-09" (9) | ASSERTED | Reports do not ship |
| 5 | "fresh: execution confirmed, findings convergent" | ASSERTED | No external anchor |
| 6 | "All four are producer-family advisory; no verdict binds" | ASSERTED | Family attribution unaudited |
| 7 | "four consecutive producer-family advisory cycles (v0.20 through v0.22, plus v0.23) following v0.19 tri-seat" | ASSERTED | Count 4 internally consistent with S27; "producer-family" unaudited; evades [9e] (P1) |
| 8 | "PRIOR_HISTORY 6358a9ba…2587b" | **COMPUTED** | build [9b] derivation; P4 mutation fires |
| 9 | (d) v0.22 dispositions F-OP21C-04 at two severities | ASSERTED | Verifiable from v0.22 entry (S27) but not gated |
| 10 | (e) v0.22 preamble declares F-OP21S-03/04/05, register omits them | ASSERTED | Verifiable from v0.22 entry; not gated |
| 11 | item(1) "[9f] now unconditional, duplicate-ID check, no prose anchor" `[COMPUTED: build.py [9f]]` | **ASSERTED (tag false)** | P2: regex blind to `(partial)`; misses F-OP22S-03 HIGH/LOW; undercounts 10 vs 12 |
| 12 | item(2) F-OP21C-04 duplicate corrected in (d) | ASSERTED | Cross-entry; not gated |
| 13 | item(3) three absent findings corrected; F-OP21S-05 DISCLOSED NOT CLOSED | ASSERTED | Cross-entry; not gated |
| 14 | item(4) [9c] section-existence is bare substring, DISCLOSED NOT CLOSED | ASSERTED | TRUE — P3 demonstrates the false-PASS |
| 15 | item(5) coverage figures from build [11] | ASSERTED | Honest; but item(12) states stale figures (see #22) |
| 16 | item(6) ASSERTED tag is a catch-all | ASSERTED | Self-disclosure |
| 17 | item(7) dispatch discipline manifest-inclusion claim false of v0.22 | ASSERTED | Not verifiable here |
| 18 | item(8) F-OP21S-05 arity-one, DISCLOSED NOT CLOSED | ASSERTED | TRUE (disclosed in v0.21) |
| 19 | item(9) PRIOR_HISTORY recursion bottoms at cb67f222 literal | ASSERTED | Not gated |
| 20 | item(10) no gate enforces raised=dispositioned | ASSERTED | TRUE; and this item carries the F-OP22S-03 duplicate |
| 21 | item(11) "PDF is unbound for a fourth consecutive round" | ASSERTED | Verifiable: PDF not in PACKET_SHA256SUMS; not gated |
| 22 | item(12) "ASSERTED fraction rose from 57.1% to 78.9%; COMPUTED fell from 9 to 4" | **ASSERTED (false for v0.23)** | build [9c] actual: COMPUTED 3, ASSERTED 14, 82.4% — figures are stale (prior round) |
| 23 | "All 12 code files and trust roots stamped v0.23" | **COMPUTED** | build [2] checks all 12 + trust roots |
| 24 | "Section 25 digests recomputed from v0.23 bytes" | **COMPUTED** | build [3a] FB-row locus assertions |
| 25 | "Normative manifest digest 59635c05… `[COMPUTED: sha256sum\|sha256sum]`" | **COMPUTED** | build [3]; P5 mutation fires |
| 26 | "Six suites, 186 tests, all GREEN `[COMPUTED: pytest + AST]`" | **COMPUTED** | build [5],[8]; P5b mutation fires |
| 27 | "Status: DRAFT CANDIDATE — NOT FROZEN. FB-7b OPEN." | ASSERTED | Status claim; consistent |

**Auditor headline: 22/27 = 81.5% ASSERTED, 5/27 COMPUTED, 0/27 EXTERNAL.**

---

## 4. Probes (Deliverable B + C)

Every probe has: mutation-landed hash delta (before≠after on the target file),
a discrimination control (known-bad that must fail), a benign control (clean
copy, rc=0), and verbatim reproduction saved to
`audit_evidence/probes/probe_run_v2.txt` + `probe_summary_v2.json` (and
`P2_discrim_v4.txt` for the corrected P2 discrimination control). Protocol-text
probes were resealed (HISTORY.sha256 ENTRY_v0.23 + FULL_SECTION_27, and
PACKET_SHA256SUMS) after mutation to isolate the target gate from the [9b]/[12]
seal confound — this resealing is itself the self-consistent-forger operation
the boundary tests.

**P1 — [9e] cardinal-range `)` blind spot (false-PASS).** Mutate the governance
claim to the bare false form "(v0.20 through v0.22)" (cardinal 4, span 3),
reseal. build → rc=1, `FAIL: Cardinal 'four' matches range v0.20..v0.22
(span 3)`. Benign (actual "+plus" form) → rc=0. **Result:** [9e] binds only
`(v0.X through v0.Y)` with the closing paren immediately after Y; the actual
entry's "(v0.20 through v0.22, plus this v0.23 entry)" evades it. The claim is
true, so this is a gate-coverage gap, not a false claim. (Discrimination: the
bare form fails.)

**P2 — [9f] register-ID qualifier-token blindness (NOVEL CLASS NC2, false-PASS).**
Remove "(partial)" from item (10) so F-OP22S-03 is cleanly named, reseal.
build → rc=1, `FAIL: Finding F-OP22S-03 dispositioned at HIGH and LOW`. Benign
(actual entry with "(partial)") → rc=0. **Result:** the regex
`F-\w+-\d+(?:\s*/\s*F-\w+-\d+)*` cannot parse parenthetical qualifiers, so it
(a) undercounts the register 10 vs 12 (HIGH 2 vs 3, LOW 2 vs 3) and (b) misses
the live F-OP22S-03 HIGH(item3)/LOW(item10) duplicate that item (1) claims to
catch "unconditionally." This is the headline defect. *Named new:* register-ID
qualifier-token blindness — distinct from prior "arity-one regex" (F-OP21S-05)
and "anchor-regex disabled" (F-OP22-01); the failure is the regex character
class `\w` excluding `(`, silently dropping qualifier-suffixed IDs.

**P2-discrimination — clean duplicate (corrected).** Add a cleanly-named
F-OP22-99 at HIGH (item 2: `F-OP22S-02 / F-OP22C-02 / F-OP22-99 HIGH CLOSED`,
all clean names so no qualifier breaks the regex chain) and at MEDIUM (new
item 13, anchored on the v0.23-unique manifest-digest tail), reseal. build →
rc=1, `FAIL: Finding F-OP22-99 dispositioned at HIGH and MEDIUM`; v0.10 entry
confirmed unchanged (the mutation lands only in v0.23). Benign → rc=0.
**Result:** [9f] discriminates cleanly-named duplicate-severity dispositions; the
blind spot is specifically the parenthetical qualifier token, not the
duplicate-detection logic. *(The first P2-discrimination attempt was VOID: its
`.replace(...,1)` landed the (13) item inside the v0.10 entry, breaking the
v0.10 seal, and its item-(1) HIGH anchor sat after `F-OP22C-01(fresh)`, where
the "(fresh)" qualifier broke the regex chain before F-OP22-99 — so [9f] never
saw the HIGH occurrence. Both confounds fixed in v4; the v1/v3 attempts are
discarded.)*

**P3 — [9c] tag-to-semantics unbound (false-PASS, disclosed F-OP22-02).** Retag
item (1) `[COMPUTED: build.py [9f]…]` → `[COMPUTED: build.py [4]…]` (brand
sweep section exists but does not implement register checks), reseal. build →
**rc=0 PASS**. **Result:** [9c] verifies a COMPUTED tag names an *existing*
build.py section, not that the section *implements* the tagged claim. A false
claim can wear a COMPUTED tag. (Discrimination: retag to `[999]` → rc=1,
`FAIL: COMPUTED tag references existing build.py section [999]`.)

**P4 — PRIOR_HISTORY / HISTORY integrity (COMPUTED, verified).** Mutate the
PRIOR_HISTORY value in HISTORY.sha256. build → rc=1
(`FAIL: PRIOR_HISTORY matches derivation`; `FAIL: PACKET_SHA256SUMS digest
matches: HISTORY.sha256`). (Discrimination: corrupt ENTRY_v0.1 seal → rc=1,
`FAIL: HISTORY seal ENTRY_v0.1 matches bytes`.) Benign → rc=0. **Result:** the
HISTORY/PRIOR_HISTORY surface is genuinely gated; claim #8 is COMPUTED. (Caveat:
self-consistent only — not externally anchored, Section 22.2.)

**P5 — manifest digest (COMPUTED, verified).** Append a comment to
xz_protocol_kernel.py. build → rc=1 (`FAIL: Trust roots manifest_digest
matches…`; PACKET digest). (P5b: break ALLOW→DENY_FALSE → rc=1,
`FAIL: All tests GREEN (rc=1)`, `FAIL: Collected (181) == AST (186)`.) Benign →
rc=0. **Result:** claims #25 and #26 are genuinely COMPUTED.

**NC1 — headline-metric self-certification (NOVEL CLASS, false-PASS).** Retag
item (10)'s `[ASSERTED]` → `[COMPUTED: build.py [9f]]` (section exists), reseal.
build → **rc=0 PASS**. **Result:** the ASSERTED fraction — the round's headline
number — is producer-self-reported; [9c] certifies tag *syntax* (the referenced
section exists), not tag *truth*. A producer can lower the headline ASSERTED
fraction by retagging, with no semantic check. This is the
self-consistent-forger posture the standing orders warn gates are blind to by
construction. *Named new:* headline-metric self-certification — the metric the
program uses to track boundary movement is itself uncertified-for-truth; prior
rounds treated the ASSERTED fraction as objective.

Void probes: one (P2-discrimination v1/v3, confounded — see above; replaced by
v4). All other mutations landed (hash before≠after on target file,
`probe_summary_v2.json` + `P2_discrim_v4.txt`).

---

## 5. Findings

**F-GLM23-01 (HIGH) — False COMPUTED tag; [9f] gate blind spot.** v0.23 item
(1) tags `[COMPUTED: build.py [9f] register self-consistency]` and claims the
duplicate-ID check is "unconditional." It is not (P2): the regex cannot parse
`F-OP22S-03(partial)`, so it misses a **live duplicate-severity disposition** —
F-OP22S-03 at HIGH CLOSED (item 3) and LOW NOTED (item 10) — and undercounts the
register 10 vs 12 (HIGH 2/3, LOW 2/3). The same entry's corrections (b),(c),(d)
correct exactly this duplicate-disposition class, and item (1) claims to have
closed the gate that catches it. The COMPUTED/CLOSED tag is an overclaim; it
must be CLOSED IN PART and the tag retagged ASSERTED. This is the
"claimed-fix-did-not-land" pattern (cf. v0.15 F-GLM52-02 CRITICAL).

**F-GLM23-02 (MEDIUM) — Stale coverage figures in item (12).** Item (12) states
"ASSERTED fraction rose from 57.1% to 78.9% while COMPUTED fell from 9 to 4."
build [9c] on v0.23 bytes reports COMPUTED 3, ASSERTED 14, fraction 82.4%. The
figures are the prior round's, stated as current — the same class item (5)
discloses ("stated the prior round's coverage figures rather than the current
round's"). A claim about the headline metric, in the entry that introduces the
metric, is stale.

**F-GLM23-03 (MEDIUM) — [9e] cardinal-range gate false-PASS.** The governance
claim "four consecutive … (v0.20 through v0.22, plus this v0.23 entry)" evades
[9e] because the regex requires the closing `)` immediately after the end
version (P1). The claim is true (4 cycles), so this is a gate-coverage gap, not
a false claim — but a genuinely-wrong "+plus" phrasing would slip through. The
gate's name exceeds its reach.

**F-GLM23-04 (LOW) — [9c] tag-to-semantics unbound (disclosed, demonstrated).**
P3 shows a COMPUTED tag can reference a wrong-but-existing build.py section and
pass. This is the disclosed F-OP22-02 boundary, now mutation-confirmed.

**F-GLM23-05 (LOW) — Stale strings in build.py (tooling).** build.py docstring
line 2 reads "v0.22 build verification script"; check messages at lines 283
("expected 22") and 284 ("Protocol says 'twenty-two'") contradict the asserted
values (23 / "twenty-three"). Cosmetic (do not fail the build); evidence of the
stale-context producer posture the invariant predicts. build.py is tooling
outside the carried manifest (v0.14 partition), so this does not touch the
normative bytes.

**What the round got right (before the ledger).** The normative instrument is
byte-clean: all 16 packet digests verify, all 186 tests pass, all 23 HISTORY
seals + FULL_SECTION_27 + PRIOR_HISTORY verify, the manifest digest matches,
version stamps are consistent across all 12 code files + trust roots, the
absence gate is clean (0 stale hex in the body), and the append-only record is
intact (no in-place historical mutation detected this round). The
Axiom-3 digest-from-memory pattern, which recurred eleven times through v0.17,
is broken at the value level for the normative body. The boundary this round
moved outward into the entry's *self-classification* of its own claims — a
genuinely harder surface, and the producer disclosed most of it honestly
(items 4, 6, 8, 10). The residual is two overclaims (items 1, 12) and two gate
blind spots ([9e], [9f]) the producer did not catch.

### Hedge audit (Deliverable E — S-4)

For every downgrade term in the v0.23 entry (CLOSED IN PART, DISCLOSED, NOT
CLOSED, NOTED, and the overclaimed CLOSED), four checks: (1) is the downgrade
correct? (2) is the REASON attached to it true? (3) does the disclosure's SCOPE
match the defect's scope? (4) is the item carried into the register with an ID?

| Item | Term | Downgrade correct? | Reason true? | Scope matches? | In register w/ ID? |
|---|---|---|---|---|---|
| (1) F-OP22-01… "HIGH CLOSED" `[COMPUTED: build.py [9f]]` | CLOSED (overclaimed) | **No** — should be CLOSED IN PART | Reason ("gate now unconditional") **false** (P2: parenthetical blind spot; F-OP22S-03 HIGH/LOW missed; undercount 10 vs 12) | **No** — claims "unconditional," actual scope is "clean-ID-only" | Yes (F-OP22-01 / F-OP22S-01 / F-OP22C-01) |
| (3) F-OP21S-05 "DISCLOSED NOT CLOSED" | DISCLOSED NOT CLOSED | Yes | Yes ("regex captures only first filename per tag" — arity-one, true) | Yes | Yes (F-OP22C-03 / F-OP22S-03) |
| (4) F-OP22-02 "DISCLOSED NOT CLOSED" | DISCLOSED NOT CLOSED | Yes | Yes ("section-existence predicate remains bare substring" — P3 confirms) | Yes | Yes (F-OP22-02 / F-OP22C-07) |
| (5) F-OP22-03 "MEDIUM NOTED" `[ASSERTED: no gate binds]` | NOTED | Yes | Yes ("no gate binds coverage claims to [11]") | Yes — and item (12) is the live instance (stale figures) | Yes (F-OP22-03 / F-OP22S-04 / F-OP22C-06) |
| (6) F-OP22C-04 "MEDIUM NOTED" | NOTED | Yes | Yes ("ASSERTED tag is a catch-all") | Yes (NC1 demonstrates the gameability) | Yes (F-OP22C-04) |
| (7) F-OP22C-05 "MEDIUM NOTED" | NOTED | Yes | Yes (dispatch manifest-inclusion claim false of v0.22) | Yes | Yes (F-OP22C-05) |
| (8) F-OP22S-05 "MEDIUM NOTED … DISCLOSED NOT CLOSED" | NOTED + DISCLOSED NOT CLOSED | Yes | Yes (F-OP21S-05 arity-one, disclosed in v0.21) | Yes | Yes (F-OP22S-05) |
| (9) F-OP22-04 "LOW NOTED … DISCLOSED" | NOTED + DISCLOSED | Yes | Yes (PRIOR_HISTORY recursion cb67f222 literal) | Yes | Yes (F-OP22-04 / F-OP22S-06) |
| (10) F-OP22C-08 "LOW NOTED" | NOTED | Yes | Yes ("no gate enforces raised=dispositioned") | **Partial** — the reason is true, but this item's own ID-listing (`F-OP22S-03(partial) LOW`) creates the F-OP22S-03 HIGH/LOW duplicate that F-GLM23-01 shows is undetected | Yes (F-OP22C-08 / F-OP22S-03(partial)) |
| (11) F-OP22C-09 "LOW NOTED" | NOTED | Yes | Yes (PDF unbound — verifiable: PDF not in PACKET_SHA256SUMS) | Yes | Yes (F-OP22C-09 / F-OP22S-07) |
| (12) F-OP22-05 "INFORMATIONAL NOTED" | NOTED | **No** — the figures stated (78.9%, COMPUTED 4) are stale; actual is 82.4%, COMPUTED 3 | Reason ("ungated share rose for a fifth consecutive round") not independently verifiable without prior packets (ASSERTED); the stated figures are false for v0.23 | **No** — states prior-round figures as current | Yes (F-OP22-05 / F-OP22S-08) |

**Hedge-audit conclusions.** Two downgrades are defective: item (1) is an
*overclaimed* CLOSED (should be CLOSED IN PART; its "unconditional" reason is
false — the bite S-4 warns about, "a deferral/closure whose stated reason is
false is a defect wearing the costume of a disclosure"), and item (12) is a
NOTED whose stated figures are false for v0.23 (stale). Item (10)'s scope is
under-stated: its `(partial)` notation is the mechanism by which the
F-OP22S-03 duplicate evades [9f]. Every item is carried in the register with an
ID. The remaining nine downgrades (items 3,4,5,6,7,8,9,11 and the NOTED
portions of 10) are correct, with true reasons and matching scope — genuine
progress, recorded as such.

---

## 6. Boundary (S-5)

Total document 165 612 chars. Gated body (sections 0–26) 97 802 chars
(59.1%). Ungated Section 27 67 810 chars (40.9%). Semantic-gate coverage
24 175 / 97 802 body chars (24.7%) — i.e., ~75% of the *gated* body, and 100%
of Section 27, is not under a semantic gate. Every claim in the v0.23 entry
falls in the ungated Section 27 region; its only gates are the HISTORY seal
(bytes-unchanged-since-sealing, not truth) and [9c]/[9d]/[9e]/[9f] tag/regex
checks, three of which have demonstrated blind spots (P1, P2, P3). Packet
level: 16/16 manifest members carry a digest in PACKET_SHA256SUMS; the shipped
`xz_protocol_v0_23.pdf` carries **no** digest in any shipped text, so claims
about the PDF cannot fail a build by construction (consistent with item 11's
"PDF unbound" disclosure). Naming the region is not a fix; it converts an
invisible dependency into a declared one, the honest precondition for any
FROZEN claim.

---

## 7. D-7 (Deliverable G)

The next seat must be given, or must resolve:
1. The v0.24 entry correcting F-GLM23-01: re-tag item (1) CLOSED IN PART /
   ASSERTED, fix the [9f] regex to parse parenthetical-qualified finding IDs,
   and re-run [9f] to confirm it now flags F-OP22S-03 (and re-counts 12).
2. The resolution of the F-OP22S-03 duplicate disposition itself (is item 10's
   listing a cross-reference or a second disposition? renotate to remove the
   ambiguity).
3. Correction of item (12)'s stale coverage figures to v0.23's actual
   (COMPUTED 3, ASSERTED 14, 82.4%) — and a gate binding the entry's
   coverage-figure claims to build [11]'s computation (currently ASSERTED, item
   5 discloses).
4. Hardening of [9e] to bind the `(v0.X through v0.Y, …)` form, not only the
   bare `(v0.X through v0.Y)` form (F-GLM23-03).
5. The external anchor that closes the self-consistent-forger residual
   (Section 22.2): a carrying-seat-held dispatch manifest digest or external
   deposit receipt independent of build.py, so PRIOR_HISTORY/HISTORY can be
   anchored outside producer control. Without it, my "COMPUTED" on the HISTORY
   surface is a self-consistency claim only.
6. The Kimi K3 (Moonshot) carry-2 report on these same v0.23 bytes — required
   to satisfy FB-7b's two-family convergence (this report is one family only).
7. A decision on whether build.py (tooling) defects ([9f]/[9e] regex, stale
   strings) block FROZEN or are scoped to the adversarial tooling bundle per
   the v0.14 partition — currently ambiguous because the entry's COMPUTED tags
   *about* build.py are normative-text claims.

---

## 8. Verdict

**CONDITIONAL PASS (non-HALT).** Counts toward FB-7b as the GLM family
(non-producer) seat. Under the dispatch, HALT blocks freeze; CONDITIONAL PASS
is non-HALT and does not block freeze. This verdict therefore does not block
freeze. The three conditions below are non-HALT carry conditions that should
be cleared before the next version or before any chair-accepted freeze; they
are not a freeze block.

The normative instrument is byte-clean and carry-able on canonical bytes: all
16 packet digests verify, 186/186 tests pass, all 23 HISTORY seals +
FULL_SECTION_27 + PRIOR_HISTORY verify, the manifest digest matches, version
stamps are consistent, and the append-only record is intact (no in-place
historical mutation this round). The carry on the normative bytes succeeds.

Non-HALT carry conditions that should be cleared before the next version or
before chair-accepted freeze:
- **C1 (HIGH):** F-GLM23-01 — fix the [9f] regex to parse
  parenthetical-qualified finding IDs; re-tag item (1) CLOSED IN PART /
  ASSERTED; confirm [9f] now flags the F-OP22S-03 HIGH/LOW duplicate and
  re-counts the register (12, not 10).
- **C2 (MEDIUM):** F-GLM23-02 — correct item (12)'s coverage figures to v0.23
  actuals (COMPUTED 3, ASSERTED 14, 82.4%).
- **C3 (MEDIUM):** F-GLM23-03 — harden [9e] to bind the
  `(v0.X through v0.Y, …)` form.

C1 is a false COMPUTED-tagged closure claim (the "claimed-fix-did-not-land"
class that has historically rated CRITICAL/HIGH in this program), but here it
sits in the tooling gate and the amendment entry, not in the normative code
modules, and the normative bytes are otherwise clean — hence CONDITIONAL PASS
(non-HALT), not HALT. If the producer contests the normative/tooling partition
for gate-claim overclaims, that would be a HALT-class escalation; I have scoped
this verdict to the tooling/entry per the v0.14 partition, so it remains
non-HALT and does not block freeze.

Standing restated: this verdict is from a non-producer carrying seat and counts
toward FB-7b (two-family executing carry). It is non-HALT and does not block
freeze; the convergence requirement still needs the Kimi K3 carry-2 report on
these same bytes. Same-vendor seats count once; this is the GLM seat only.

---

## S-7 — Self-falsification (numbered)

1. Recomputed every digest: `sha256sum -c` rc=0; independent recompute of all
   16 members MATCH (`independent_digests.txt`); manifest digest
   `59635c05…cbf1` re-derived; FULL_SECTION_27 `fd7b3320…7e5c` re-derived and
   matches HISTORY. PRIOR_HISTORY `6358a9ba…2587b` re-derived matches.
2. Re-extracted every line number: build.py docstring line 2, messages lines
   283/284, [9e] regex line 380 (trailing `)`), [9f] regex line 395 — all
   re-read from file bytes, not from memory.
3. Re-derived every count: register items 12 (corrected parse), 10 (build
   [9f] parse); severities HIGH 3 / MEDIUM 5 / LOW 3 / INFO 1; entry count 23;
   test count 186 (AST + pytest agree); source-frame 16; normative files 14;
   boundary 165612/97802/67810/24.7%; ledger 22 ASSERTED / 5 COMPUTED / 27
   total = 81.5%.
4. Grepped every claim about shipped reports: "advisory reports do not ship"
   confirmed — no F-OP22* report file exists in the packet.
5. Performed past-tense procedure claims now: re-ran `python3 build.py` after
   all probes (benign rc=0); re-ran six-suite pytest (186 passed). Confirmed.
6. Void probes: P2-discrimination v1/v3 (confounded — see §4) is reported as
   void and replaced by v4; v4's FAIL line is the duplicate-detection one
   (`Finding F-OP22-99 dispositioned at HIGH and MEDIUM`), with v0.10 entry
   confirmed unchanged. All other mutations landed.
7. **Revision self-falsification (across revisions):**
   - **P2-discrimination confound caught and fixed.** The v1 run's FAIL lines
     were HISTORY-seal/PRIOR_HISTORY, not duplicate detection — because the
     `.replace("Status:…",…,1)` landed the (13) item in the v0.10 entry (the
     first "Status:" match), and the item-(1) HIGH anchor sat after
     `F-OP22C-01(fresh)` where "(fresh)" broke the regex chain before
     F-OP22-99. v4 re-anchors both insertions on v0.23-unique strings and uses
     item (2) (clean names) for the HIGH occurrence; the FAIL line is now the
     correct duplicate-detection failure (`P2_discrim_v4.txt`).
   - **Ledger headline made exact.** Replaced "~22/~27/≈81.5%" with two
     distinct exact headlines: tagged-claim 14/17 = 82.4% (build [9c]) and
     auditor all-claim 22/27 = 81.5%; no tilde/≈ remains.
   - **Hedge audit added** as a `###` subsection under §5 Findings, with the
     four S-4 checks per downgrade term; it caught that item (1)'s CLOSED is
     overclaimed and item (12)'s NOTED figures are stale, consistent with
     F-GLM23-01/02.
   - **Structure fixed:** S-0 is the first content after the title line; the
     prior metadata block is folded into S-0.
   - **Verdict wording reconciled (this revision).** Removed the
     "FROZEN is blocked" language that conflicted with a non-HALT verdict.
     The verdict is CONDITIONAL PASS (non-HALT): under the dispatch, HALT
     blocks freeze and CONDITIONAL PASS does not. C1–C3 are now stated as
     non-HALT carry conditions to clear before the next version or before
     chair-accepted freeze — not a freeze block. Re-grepped the verdict
     section: "FROZEN is blocked" no longer appears; "does not block freeze"
     is stated exactly once.
   - **Section numbering reconciled (this revision).** Hedge audit is now an
     unnumbered `###` subsection of §5 Findings so the required numbered
     structure holds: 5=Findings, 6=Boundary, 7=D-7, 8=Verdict.
   - Re-confirmed: prereg hash `8ab02e53…` unchanged; workspace build rc=0.

## Anti-pattern check (one line)

- Did every probe come from the enumerated corpus? **No** — NC1
  (headline-metric self-certification) and NC2 (register-ID qualifier-token
  blindness) are named new; P1/P3 extend disclosed boundaries by mutation.
- Did the preregistered prediction hold trivially because the dispatch told me
  where to look? **No** — the dispatch gave no defect location; the boundary
  prediction was derived from the invariant and HELD.
- Was the ASSERTED fraction unchanged from prior round? **No** — producer-
  reported 82.4% (tagged) vs prior round's 78.9% (item 12); auditor all-claim
  81.5% with one false COMPUTED tag exposed.
- Have the last N rounds all been producer-family seats? **No** — this is the
  GLM non-producer carry-1 seat; the prior non-producer contact was v0.20
  (tri-seat). Governance: four consecutive producer-family advisory cycles
  (v0.20–v0.22 + v0.23) preceded only by the v0.19 tri-seat round — a
  disclosed process finding, not a version finding.

*Evidence: `audit_evidence/build_output.txt`, `independent_digests.txt`,
`history_prior_verify.txt`, `pytest_six_suite.txt`, `register_9f_analysis.txt`,
`boundary_s5.txt`, `v023_entry_full.txt`, `probes/probe_run_v2.txt`,
`probes/probe_summary_v2.json`, `probes/P2_discrim_v4.txt`,
`probes/run_probes_v2.py`.*

---

# Bismillah ir-Rahman ir-Rahim
