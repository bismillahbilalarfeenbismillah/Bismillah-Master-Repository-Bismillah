# Bismillah ir-Rahman ir-Rahim

# R0607 -- XZ Protocol v0.9 -- Carrying Audit

**Chronological Index:** 435 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** DISPATCH_v09_KIMI.txt  
**Source Format:** txt  
**SHA-256:** `4ecd4d53f833fae505dca68f06f7c6f5604126014d95cf1de1259055e8e54982`  

---

## R0607 · XZ Protocol v0.9 -- Carrying Audit

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: DISPATCH_v09_KIMI.txt
- source_format: txt
- text_sha256: 4ecd4d53f833fae505dca68f06f7c6f5604126014d95cf1de1259055e8e54982

# XZ Protocol v0.9 -- Carrying Audit

To: Kimi K3 (carrying seat 2/2, non-producer)
Seat 1: GLM-5.2 (Zhipu/Z.ai) | Producer: Claude Opus 4.6 (excluded)
Date: 2026-08-01. Rename .txt to .py/.md/.json.

Your v0.8 HALT had three blocking findings. All three closed:
- F-K3-01: "25 tests" corrected to "29 tests" (AST-derived)
- F-K3-02: false pytest-pinning claim replaced with accurate description; canonical command added to Section 0.1
- F-K3-03: kernel gate changed from isinstance to exact type check (type(v) is ConjunctVector)
- F-K3-08 (non-blocking): "eleven rules" corrected in code docstrings

SHA-256 manifest (14 files):
c37c69e3107c1d1e1fd61cde47a8a6999adbbbb5e1e275fa00d6dd803fcf4ff6  xz_protocol_v0_9.md
eda31a66bcf0d198dac363988960f99eca6c72aa49d5e8f7bd174b9eba0e371b  xz_protocol_kernel.py
b0d57e012b490f40ae8436eefd547dcce6d5ee42443b002e292de34ad5e1a59e  xz_protocol_phase_a_m3.py
e5247646cd83f03274469c2053d084c989ef7fd3a9f3b991b3ae1cee8ff414af  xz_protocol_phase_a_intervals.py
f08050c50f1e1f653852405b3c4ec0fcaed29f31c78a37c4bc5d09a63826aaa3  xz_protocol_phase_a_tests.py
b020a8ef740d915b812d93b35f1dc94186c6d2e366d21df490e4c0e558df43ee  xz_protocol_condition_a.py
119028c79d20a93885d7b39e07c0b5675f43ef1b3e50e52f3269773c67e41c0b  test_xz_protocol_condition_a.py
2645054d43dd9ad4cfe12a9d2a91546874c3c4fe9692dbaa86c6daecd30ca580  xz_protocol_source_frame.py
9b3868b3d50af8f2a9ff7aec0531a916a7863a4fcb8ef10c5fab3a92b5f38554  test_xz_protocol_source_frame.py
1b0d8bac6180e9faa1030114fce45f5333a1ddb304d61d36b382454be493d31d  xz_protocol_control_graph.py
cc8fd9e2663755128e50deb23b6c6a30efcd8e12d50b4b7a19083363fbbfd4f5  test_xz_protocol_control_graph.py
75ad27efaf2482e5d32aaf8974413415084635c115f315d1034a031ed2370053  test_xz_protocol_kernel.py
4140399de285da2e973ac09f75044fed1e9c595983b9c556956fd37952228767  test_xz_protocol_adversarial.py
42bfda3a6361bb11f6284ccdee8b430f667baaaf06caa16d076a8fbac693badd  xz_protocol_trust_roots_PUBLIC.json

Canonical verification: pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py

Task: 1. SHA-256 (14/14). 2. 185/185 GREEN. 3. Verify F-K3-01/02/03/08 discharged. 4. Attack (especially descriptor laundering against the type fence). 5. Verdict.

---

# Bismillah ir-Rahman ir-Rahim
