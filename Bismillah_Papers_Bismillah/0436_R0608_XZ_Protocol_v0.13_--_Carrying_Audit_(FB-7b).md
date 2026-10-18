# Bismillah ir-Rahman ir-Rahim

# R0608 -- XZ Protocol v0.13 -- Carrying Audit (FB-7b)

**Chronological Index:** 436 of 995  
**Date:** 2026-08-01  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** DISPATCH_v13_KIMI.txt  
**Source Format:** txt  
**SHA-256:** `7ba4eaf04d2686082edf8de7dad62b8d6c25ddb6a0ea5142defdea7b6cc9ca66`  

---

## R0608 · XZ Protocol v0.13 -- Carrying Audit (FB-7b)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: DISPATCH_v13_KIMI.txt
- source_format: txt
- text_sha256: 7ba4eaf04d2686082edf8de7dad62b8d6c25ddb6a0ea5142defdea7b6cc9ca66

# XZ Protocol v0.13 -- Carrying Audit (FB-7b)

To: Kimi K3 (Moonshot, carrying seat 2/2, non-producer)
Seat 1: GLM-5.2 (Zhipu/Z.ai, non-producer)
Producer of v0.13: Claude Opus 5 (Anthropic, excluded from carry)
Date: 2026-08-01. Rename .txt to .py/.md/.json/.sha256.

v0.13 was authored by Opus 5 at the project lead's direction. The three v0.12 gates were rebuilt with fixture pairs and two new gates added. 22 canonical files, 210 tests.

SHA-256 manifest (22 files):
46393deec4f26ea46f19f814c09a9e3fefabeae498e65b5823a4b384059162f4  HISTORY.sha256
4140399de285da2e973ac09f75044fed1e9c595983b9c556956fd37952228767  test_xz_protocol_adversarial.py
119028c79d20a93885d7b39e07c0b5675f43ef1b3e50e52f3269773c67e41c0b  test_xz_protocol_condition_a.py
cc8fd9e2663755128e50deb23b6c6a30efcd8e12d50b4b7a19083363fbbfd4f5  test_xz_protocol_control_graph.py
611f7ca13b44bfbc9d50253722de790adb1d683385c86ca02783177bc7ab8c6f  test_xz_protocol_gates.py
75ad27efaf2482e5d32aaf8974413415084635c115f315d1034a031ed2370053  test_xz_protocol_kernel.py
9b3868b3d50af8f2a9ff7aec0531a916a7863a4fcb8ef10c5fab3a92b5f38554  test_xz_protocol_source_frame.py
c2c98cbe7c2fe659c61053f501455aaae68929e570a5829cf9e700b5f6698c1b  xz_protocol_closure_gate.py
4aaf9050ac0e19fed69f13ca27724ac6c9976936c44693e910f03167306392cc  xz_protocol_condition_a.py
e25c164297933ceb04ffc2a23631f9adfaafca0d9bf088e7db594995271ee05e  xz_protocol_control_graph.py
b12eb09c8a9a6bf60e9c26856f75f22a99d4f74cca44babcfe9a9a771a4108f0  xz_protocol_history_gate.py
6e315c46e57630cb9c8961600e8be0cd88ac2435cf779e0d0f3e55ab528a5f29  xz_protocol_kernel.py
3b0d2b290aca0369b972c0e6fdbddd5e98dc87ae40a10cdc0b8a567d2da98e04  xz_protocol_locus_register.json
0aae11292da81f163735b255a18bbb1788ef876ccd1a1283fef4d887c3d7e7c6  xz_protocol_manifest_gate.py
7d73f7e970268d985d16b0e6ec305b21c8805d119b7c940f5cdfd98fbc34df8a  xz_protocol_phase_a_intervals.py
2bbb2506dac83c0d3039fa6793e55071bcc71febb295bed0c87488da5c7c5e98  xz_protocol_phase_a_m3.py
b969c759a44899768cd2249182d7340a6be52af7d75f753793424da3491f4a11  xz_protocol_phase_a_tests.py
8f08767245c096a039bb16a77d7c91429abecff6e049222048701754dce166f4  xz_protocol_prohibited_content_verifier.py
6ae274b12995686fd8dcf74cc6e787111c3c33905f11047a0555eacffc83f860  xz_protocol_source_frame.py
b99f720e76a71c84ddd50489ee286426cc47899cf4f5e5b5a117ca6845b309cc  xz_protocol_trust_roots_PUBLIC.json
6e1b56492267ac109399cd9b30f51ca9c64f4e18052b1158833db2a162674ed0  xz_protocol_v0_13.md
cb780ad47b2e79f45eb8244f044a850f6588691388302c61a68b6c5eee8aab1a  xz_protocol_version_gate.py

Canonical test: pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py test_xz_protocol_gates.py

Gates: python3 xz_protocol_version_gate.py && python3 xz_protocol_version_gate.py --self-test && python3 xz_protocol_closure_gate.py && python3 xz_protocol_manifest_gate.py && python3 xz_protocol_prohibited_content_verifier.py && python3 xz_protocol_history_gate.py

Task:
1. SHA-256 (22/22)
2. 210/210 GREEN
3. All 5 gates PASS
4. ATTACK EACH GATE -- construct inputs that should make it fail and confirm it does; construct inputs that should make it pass and confirm it does; report any gate you can make return a false PASS
5. Attack commitment and decision paths
6. Verdict: CARRY-CLEAN / PASS / HALT

---

# Bismillah ir-Rahman ir-Rahim
