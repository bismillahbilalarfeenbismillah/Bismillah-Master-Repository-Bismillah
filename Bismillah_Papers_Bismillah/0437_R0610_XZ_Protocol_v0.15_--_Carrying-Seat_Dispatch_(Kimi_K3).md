# Bismillah ir-Rahman ir-Rahim

# R0610 -- XZ Protocol v0.15 -- Carrying-Seat Dispatch (Kimi K3)

**Chronological Index:** 437 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** DISPATCH_v15_KIMI.md.txt  
**Source Format:** txt  
**SHA-256:** `7e53c953071f98fc4d1a2f833804438cef7d829a2ab1eafff47202e2b8a16400`  

---

## R0610 · XZ Protocol v0.15 -- Carrying-Seat Dispatch (Kimi K3)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: DISPATCH_v15_KIMI.md.txt
- source_format: txt
- text_sha256: 7e53c953071f98fc4d1a2f833804438cef7d829a2ab1eafff47202e2b8a16400

# XZ Protocol v0.15 -- Carrying-Seat Dispatch (Kimi K3)

**Seat:** Kimi K3 (Moonshot), non-producer carrying seat
**Task:** FB-7b two-family executing carry, seat 1/2
**Date:** 2026-08-01
**Producer:** Claude Opus 4.6 (Anthropic) -- fresh instance, clean-room build from v0.14 bytes

## Task items (execute in order)

1. **SHA-256 verification.** Verify all 14 files against the manifest below. Report the count of matches. If any file fails, HALT immediately.

2. **Canonical test suite.** Run the canonical pytest command. Report the count and exit code. If any test fails, HALT immediately.

3. **Verify v0.15 fixes.** The v0.15 amendment entry (Section 27) claims to close F-GLM52-01 through F-GLM52-08 and the BayyinahEnterprise brand finding. For each claimed fix, verify against the bytes:
   - Is the front-matter Version line "0.15"?
   - Is PA-Z14 non-vacuous? (Are there unconditional assertions? Does the direct reversion test exercise the PA-Z14 code path?)
   - Do the FB-3/4/5/6 digests in Section 25 match the shipped files?
   - Does Section 22 item 6 reflect the normative/tooling partition?
   - Is BayyinahEnterprise absent from all 14 files?

4. **Attack.** Independently attempt to find false-PASS paths, commitment/decision-path defects, vacuous tests, and unreachable assertions. If you find a blocking defect, report it with reproduction evidence. You previously shipped a gate implementation for v0.14 -- you may use it or build new checks from the specification.

5. **Verdict.** Issue one of: CARRY-CLEAN (non-HALT, FB-7b satisfied for this seat), CONDITIONAL PASS (non-HALT with findings), or HALT (blocks freeze, requires new version). CARRY-CLEAN is a non-HALT verdict. A HALT from either carrying seat blocks freeze outright and requires a new version.

## Normative instrument: 14 files

SHA-256 manifest (verify every file before proceeding):

```
e916468f3a8a2494cb0715c4f9d57497417a302c18a723e9e71b33d5a05e6f6d  xz_protocol_v0_15.md
a533bb8f54c8ef6e84d6479b1e227bed9beb36a3715f11ecfa2a5daea37598b5  xz_protocol_kernel.py
3bd0b5fd37aac8f95fc9593a374255fb9dc77ecca52a4af50e10cec183ba53f3  xz_protocol_condition_a.py
2f0baf05e18ae46689aa1548f544eb87f63645ee16b79890de0b185b0e717559  xz_protocol_source_frame.py
ca2abb03c0181e3da792605aa1511dac4335e9b5102d69be2b7ce3d89a816086  xz_protocol_control_graph.py
423be034562cf35ca1c41c2d64f1a2151a4d39b07365f6d4d4910131af06a359  xz_protocol_phase_a_m3.py
03b56b5f836e03cdae154429b354c96beff7da7715b1c6dc82bdea5dfd76c6ba  xz_protocol_phase_a_intervals.py
7ea3ffa30f0df549f528dd7c23fd5f0f333a38e3381dba7da8689f163fa78a99  xz_protocol_phase_a_tests.py
75ad27efaf2482e5d32aaf8974413415084635c115f315d1034a031ed2370053  test_xz_protocol_kernel.py
119028c79d20a93885d7b39e07c0b5675f43ef1b3e50e52f3269773c67e41c0b  test_xz_protocol_condition_a.py
9b3868b3d50af8f2a9ff7aec0531a916a7863a4fcb8ef10c5fab3a92b5f38554  test_xz_protocol_source_frame.py
cc8fd9e2663755128e50deb23b6c6a30efcd8e12d50b4b7a19083363fbbfd4f5  test_xz_protocol_control_graph.py
4140399de285da2e973ac09f75044fed1e9c595983b9c556956fd37952228767  test_xz_protocol_adversarial.py
59836366ec5ce386786e20b624d3eb796344399779aa6f2bd1879b97f3be3148  xz_protocol_trust_roots_PUBLIC.json
```

Normative manifest digest (12 code files, alphabetical, SHA-256): `34d42812b80d802f17997fb7d456c4f5a9f4902dbaa4ff9ab9e820e2c17160b3`

## Canonical verification command

```
pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py \
  test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py \
  test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py
```

Expected: 186 passed, rc=0.

## Reference PDFs (8, for context only -- not carried)

BAF_v3_0.pdf, BSSG_PAPER.pdf, Dissertation_v1_4.pdf, Flagship_v0_13.pdf, PMD_v1_8.pdf, SHUDP_v0_5_flagship.pdf, SHVVP_v0_8_flagship.pdf, SHV_Method_v1_1.pdf

## What changed from v0.14

1. Front-matter Version corrected from 0.13 to 0.15 (CRITICAL F-GLM52-01).
2. PA-Z14 test made non-vacuous: two tests replace one vacuous test (CRITICAL F-GLM52-02). Test count: 185 -> 186.
3. Five stale SHA-256 digests in FB-3/4/5/6 replaced with tool-computed values (CRITICAL F-GLM52-03).
4. Section 0.1 rewritten with correct counts and canonical command (HIGH F-GLM52-04).
5. Section 22 item 6 body text amended per v0.14 entry claim (HIGH F-GLM52-05).
6. BayyinahEnterprise removed from 3 code files (HIGH).
7. All code modules and trust roots stamped v0.15.
8. Version 0.15 amendment entry appended to Section 27.
9. FB-7b pointer corrected from "v0.12" to "v0.15".
10. Trust roots manifest note corrected from "18 code-artifact files" to "12 normative code files."
11. Producer handoff: v0.15 produced by a fresh Claude Opus 4.6 instance from a clean-room build specification.

## Prior audit reports (for reference)

The v0.14 bytes received convergent HALT from both carrying seats:
- GLM-5.2: 3 CRITICAL, 5 HIGH, 7 MEDIUM, 1 LOW (verdict.json)
- Kimi K3: 3 CRITICAL, 6 HIGH, 4 MEDIUM (normative carry audit)
- GPT-5.6 Sol: 10 false-PASS paths on v0.13 gates (adversarial, self-disqualified from carry)

---

# Bismillah ir-Rahman ir-Rahim
