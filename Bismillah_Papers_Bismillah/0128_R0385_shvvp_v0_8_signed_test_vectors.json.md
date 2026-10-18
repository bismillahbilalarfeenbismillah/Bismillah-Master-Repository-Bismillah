# Bismillah ir-Rahman ir-Rahim

# R0385 -- shvvp_v0_8_signed_test_vectors.json

**Chronological Index:** 128 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_signed_test_vectors.json  
**Source Format:** json  
**SHA-256:** `1d5b716c222132b0b7c4b42d2d8583b4a4dcddd9bfb5d69f397cc54a879b34ac`  

---

## R0385 · shvvp_v0_8_signed_test_vectors.json

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_signed_test_vectors.json
- source_format: json
- text_sha256: 1d5b716c222132b0b7c4b42d2d8583b4a4dcddd9bfb5d69f397cc54a879b34ac

{
  "artifact": "SHVVP v0.8-rc1 signed test vectors",
  "commitments": {
    "R1-A-seal-v08-001": {
      "authority": "SHVVP v0.8 commitment custodian",
      "commitment_id": "R1-A-seal-v08-001",
      "commitment_sequence": 1,
      "committed_at": "2026-07-24T12:01:00Z",
      "component": "R1-A",
      "kind": "SEALED",
      "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
      "protocol_version": "0.8",
      "sealed_universe_inventory_hash": "74b50ba22c1e7efd02de859d82ebfefa731b3dab4d383f42c56960d936872381",
      "sealed_universe_n": 8,
      "signature": "beee6976f43487f6b18af9e5778e980ab2ab75affbe01cf0890fde44d8a7d9f95ae2fc97b7c99be034612197cd4c7b01cda96599af08381aa8a9e56a7832c601",
      "universe_id": "u.r1a.sealed-ledger"
    },
    "R2-B-run-v08-001": {
      "anchor": {
        "anchor_id": "anchor-R2-B-run-v08-001",
        "anchor_sequence": 4,
        "anchored_at": "2026-07-24T15:24:00Z",
        "authority": "independent pre-run anchor authority",
        "commitment_id": "R2-B-run-v08-001",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "signature": "1ea661a9c2809d616024841bc9ec5f015a2ae645c11d3a89ff10d59bdc615937b8fb7e024aa3855d64a5e053598ccf82245231fb899c0d4b4d8e3eefd8b3f700"
      },
      "close": {
        "authority": "SHVVP v0.8 commitment custodian",
        "close_id": "close-R2-B-run-v08-001",
        "closed_at": "2026-07-24T18:44:00Z",
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "final_chain_hash": "a6d6322398e14f33e0921c2606a0046f0f1634953e187ad6c2454dbb9cd77c21",
        "first_sequence": 1,
        "last_sequence": 100,
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "protocol_version": "0.8",
        "realized_total": 100,
        "run_id": "run-R2-B-v08-001",
        "signature": "ff8ac4f1443e6f2cc40c6f221a45f8882627a66814e357c9b59a1e6af04cf2e0d0887bfac84e0aa5f9878b0dfb3e4e537f385f91eafed267f0986870178d930e",
        "universe_id": "u.r2b.denials-run"
      },
      "commitment_id": "R2-B-run-v08-001",
      "kind": "REALIZED",
      "pre_run": {
        "authority": "SHVVP v0.8 commitment custodian",
        "commitment_id": "R2-B-run-v08-001",
        "commitment_sequence": 4,
        "committed_at": "2026-07-24T13:44:00Z",
        "component": "R2-B",
        "event_schema_sha256": "b7eb23c6b91ae0f9b15a746b250c6fae3e675fd4c1a32b69fa16d60d86c1d72b",
        "genesis_hash": "543b5c14abf91dc58b8dff1a04e191af5c7cda869cf99dd190a3e4ef544d50f5",
        "inclusion_rule_sha256": "8c4e47be51296071bb34c9668249cc558ba303025cdf94c282303e44e73968e7",
        "logger_pubkey": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "signature": "5d307ea5f950fd65d1225255ae29a29de4ffbe0a85dfbd6f10234213f9891928715f5b104ebb6c9bb82dfb9f5039bf96c1ee5c000ea1856bbc58b80f98d8560e",
        "universe_id": "u.r2b.denials-run"
      }
    },
    "R4-B-run-v08-001": {
      "anchor": {
        "anchor_id": "anchor-R4-B-run-v08-001",
        "anchor_sequence": 5,
        "anchored_at": "2026-07-24T15:25:00Z",
        "authority": "independent pre-run anchor authority",
        "commitment_id": "R4-B-run-v08-001",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "signature": "a53dfd8fbab1f43f9557b6c9ac09f730ff9ecafcaebe72a5245b4ab37f1a45dd15ea7939f732b66b9387813286a063041fadd4934ede042c92eecf7bbac75e06"
      },
      "close": {
        "authority": "SHVVP v0.8 commitment custodian",
        "close_id": "close-R4-B-run-v08-001",
        "closed_at": "2026-07-24T18:45:00Z",
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "final_chain_hash": "a48038bffde2410876f1c1330e8579247d175a539ca0e51c5eaea7e069ba7075",
        "first_sequence": 1,
        "last_sequence": 60,
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "protocol_version": "0.8",
        "realized_total": 60,
        "run_id": "run-R4-B-v08-001",
        "signature": "b4dd21024b17efffaa128dd5f91f49f80c0bbc6113eb98219fcf17672974cee024575396ef2389715161fc062abb14b69cb0f8ed6497cd241807e89817eac50b",
        "universe_id": "u.r4b.phaseb-injections"
      },
      "commitment_id": "R4-B-run-v08-001",
      "kind": "REALIZED",
      "pre_run": {
        "authority": "SHVVP v0.8 commitment custodian",
        "commitment_id": "R4-B-run-v08-001",
        "commitment_sequence": 5,
        "committed_at": "2026-07-24T13:45:00Z",
        "component": "R4-B",
        "event_schema_sha256": "b7eb23c6b91ae0f9b15a746b250c6fae3e675fd4c1a32b69fa16d60d86c1d72b",
        "genesis_hash": "97b8b77b04c4bf9ffd8757ea302940e664106b72892b0954c449cba923654bb4",
        "inclusion_rule_sha256": "e5d7c2df208c193a9c90b30a9e0eae2ded2c57212e4c92795029464e612bc033",
        "logger_pubkey": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "signature": "86928693648f2d5de989ee68d20806a93fc7f474f0ad53fd39766954d19adbfa0e831e5fdb2e747266d5595205ccff42177b98bb39d766b7622f5f7845561a0b",
        "universe_id": "u.r4b.phaseb-injections"
      }
    },
    "R5-A-seal-v08-001": {
      "authority": "SHVVP v0.8 commitment custodian",
      "commitment_id": "R5-A-seal-v08-001",
      "commitment_sequence": 2,
      "committed_at": "2026-07-24T12:02:00Z",
      "component": "R5-A",
      "kind": "SEALED",
      "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
      "protocol_version": "0.8",
      "sealed_universe_inventory_hash": "fd7b3eb6c6f162b06c3896b3838d041d74e9422f5e61c2eeb7b64a6d76c76874",
      "sealed_universe_n": 25,
      "signature": "76387aed0925f0c1450d58f1ef63ca871fc0397d4327f581b8559bc4cd3d109bd57721f4a1e5de365cdf343dac2bce8e828aebf4395cbd85c7035415110d0c01",
      "universe_id": "u.r5a.descendant-universe"
    },
    "R5-C-seal-v08-001": {
      "authority": "SHVVP v0.8 commitment custodian",
      "commitment_id": "R5-C-seal-v08-001",
      "commitment_sequence": 3,
      "committed_at": "2026-07-24T12:03:00Z",
      "component": "R5-C",
      "kind": "SEALED",
      "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
      "protocol_version": "0.8",
      "sealed_universe_inventory_hash": "109e60c8c0dc622e76ad447fa82d10c95a9ca569745f98dc60378afa982fc407",
      "sealed_universe_n": 9,
      "signature": "c730e10401175f6bc2b5170502bc9e51b207ee3c40e47252b6cde8b0b11a120ee9507cfdade75c6d2b59d560d9f32a3889efcff0ce738cc50fb4b8dd68558f0d",
      "universe_id": "u.r5c.revised-descendants"
    },
    "R6-B-run-v08-001": {
      "anchor": {
        "anchor_id": "anchor-R6-B-run-v08-001",
        "anchor_sequence": 6,
        "anchored_at": "2026-07-24T15:26:00Z",
        "authority": "independent pre-run anchor authority",
        "commitment_id": "R6-B-run-v08-001",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "signature": "623637b5554de0bbfe62f4d1acc28f6a59b6ef1c21338b526d0091409b2bd6d09f2f4fa80ff5857458867ae5a558d9e575f0fe337323c3e43e4c5d3782789e0f"
      },
      "close": {
        "authority": "SHVVP v0.8 commitment custodian",
        "close_id": "close-R6-B-run-v08-001",
        "closed_at": "2026-07-24T18:46:00Z",
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "final_chain_hash": "e76bcd3ce84bdff0a5f483617dd3016ca0c73c90e6d1a3221c7cc5b2caddb963",
        "first_sequence": 1,
        "last_sequence": 40,
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "protocol_version": "0.8",
        "realized_total": 40,
        "run_id": "run-R6-B-v08-001",
        "signature": "8c45ec663560cc630383dcc1f979207924c9b5056708e84d0cbf0880597ca7732c7ae5c4b3c61d05d78247d4bf6f6c5dcf7a8ab25bd9aac2ef282dcc1eadd10b",
        "universe_id": "u.r6b.receipts-run"
      },
      "commitment_id": "R6-B-run-v08-001",
      "kind": "REALIZED",
      "pre_run": {
        "authority": "SHVVP v0.8 commitment custodian",
        "commitment_id": "R6-B-run-v08-001",
        "commitment_sequence": 6,
        "committed_at": "2026-07-24T13:46:00Z",
        "component": "R6-B",
        "event_schema_sha256": "b7eb23c6b91ae0f9b15a746b250c6fae3e675fd4c1a32b69fa16d60d86c1d72b",
        "genesis_hash": "9c0809133c8e94e4bd678a38377e7017fdde059e49602878de9bbb6a6a8b2d92",
        "inclusion_rule_sha256": "130a8341c47c71e05c3c4ea2ae2f2c540f00657c1965dc9a492c63a61289c592",
        "logger_pubkey": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "signature": "9b29d78a0a448dd3c32c0fc6cddc713d4013f5e165a2fe9a99383b0d858b4a002a048775fef85fdec82fa8ab00fd760ecbeacefeeae33ba39463770ba61bed09",
        "universe_id": "u.r6b.receipts-run"
      }
    },
    "R6-C-run-v08-001": {
      "anchor": {
        "anchor_id": "anchor-R6-C-run-v08-001",
        "anchor_sequence": 7,
        "anchored_at": "2026-07-24T15:27:00Z",
        "authority": "independent pre-run anchor authority",
        "commitment_id": "R6-C-run-v08-001",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "signature": "0c9771b3fc31cb492a545278b6df4d1b9ee713afd7d57e04807e88917504444953ff4cbe150db8950ee643d1c76f9261a7bfde6ec0b1011a16b3160a62cfc903"
      },
      "close": {
        "authority": "SHVVP v0.8 commitment custodian",
        "close_id": "close-R6-C-run-v08-001",
        "closed_at": "2026-07-24T18:47:00Z",
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "final_chain_hash": "5033b9ba84c3013aa4e9443c82c228a3947c164d2e41984fe7e053ef220a7a38",
        "first_sequence": 1,
        "last_sequence": 35,
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "protocol_version": "0.8",
        "realized_total": 35,
        "run_id": "run-R6-C-v08-001",
        "signature": "35d921d7ca50b18e20141bf7aa38da5b00d145d7ea34cd0a8fb949e4b1d563794f0a2cd7a4d78a91e11a60dfd56cedafc238d1fb3fc770b3aca68529c6e22908",
        "universe_id": "u.r6c.receipts-synth"
      },
      "commitment_id": "R6-C-run-v08-001",
      "kind": "REALIZED",
      "pre_run": {
        "authority": "SHVVP v0.8 commitment custodian",
        "commitment_id": "R6-C-run-v08-001",
        "commitment_sequence": 7,
        "committed_at": "2026-07-24T13:47:00Z",
        "component": "R6-C",
        "event_schema_sha256": "b7eb23c6b91ae0f9b15a746b250c6fae3e675fd4c1a32b69fa16d60d86c1d72b",
        "genesis_hash": "8c6364f521a1767ef399e22607379a68b0607c8c9c4125c026c7e1073a40d4dd",
        "inclusion_rule_sha256": "956914e89c60c6e13fd2accd725565dcf982fd3cdfb08bb6a1a756b8136a79e9",
        "logger_pubkey": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "signature": "8c62647866c6b6043ab1aa13d221456fe913c698b5d8ba4247befa92c17d05e7e4c6ee1ca1f27389f50f3dc6ffd416ad0714db72374bff2b256759d9fffcff0f",
        "universe_id": "u.r6c.receipts-synth"
      }
    }
  },
  "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
  "negative_vectors": {
    "close_only": {
      "close": {
        "authority": "SHVVP v0.8 commitment custodian",
        "close_id": "close-R2-B-run-v08-001",
        "closed_at": "2026-07-24T18:44:00Z",
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "final_chain_hash": "a6d6322398e14f33e0921c2606a0046f0f1634953e187ad6c2454dbb9cd77c21",
        "first_sequence": 1,
        "last_sequence": 100,
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "protocol_version": "0.8",
        "realized_total": 100,
        "run_id": "run-R2-B-v08-001",
        "signature": "ff8ac4f1443e6f2cc40c6f221a45f8882627a66814e357c9b59a1e6af04cf2e0d0887bfac84e0aa5f9878b0dfb3e4e537f385f91eafed267f0986870178d930e",
        "universe_id": "u.r2b.denials-run"
      },
      "commitment_id": "R2-B-run-v08-001",
      "kind": "REALIZED"
    },
    "cross_component": {
      "authority": "SHVVP v0.8 commitment custodian",
      "commitment_id": "R5-A-seal-v08-001",
      "commitment_sequence": 50,
      "committed_at": "2026-07-24T12:50:00Z",
      "component": "R5-C",
      "kind": "SEALED",
      "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
      "protocol_version": "0.8",
      "sealed_universe_inventory_hash": "fd7b3eb6c6f162b06c3896b3838d041d74e9422f5e61c2eeb7b64a6d76c76874",
      "sealed_universe_n": 25,
      "signature": "027f120a3d719f47b3635d4b1840d8e9f0457d478a8a9d9fda97cc6c5f768687d623f9a374f58fe07c6e529f2c78ad75de7fa9c2902dee71ababcac341ed2a0b",
      "universe_id": "u.r5a.descendant-universe"
    },
    "cross_manifest": {
      "authority": "SHVVP v0.8 commitment custodian",
      "commitment_id": "R5-A-seal-v08-001",
      "commitment_sequence": 50,
      "committed_at": "2026-07-24T12:50:00Z",
      "component": "R5-A",
      "kind": "SEALED",
      "manifest_sha256": "0000000000000000000000000000000000000000000000000000000000000000",
      "protocol_version": "0.8",
      "sealed_universe_inventory_hash": "fd7b3eb6c6f162b06c3896b3838d041d74e9422f5e61c2eeb7b64a6d76c76874",
      "sealed_universe_n": 25,
      "signature": "79835451f89eea58ce035c908c940abf654b0a15d24ec1801ce0c8ccc3eeeddf9c4ce37ce0b416fb7a22e0fde37e08cd0c3d9abecbff2e9ec5cb8e1ede15130b",
      "universe_id": "u.r5a.descendant-universe"
    },
    "cross_version": {
      "authority": "SHVVP v0.8 commitment custodian",
      "commitment_id": "R5-A-seal-v08-001",
      "commitment_sequence": 50,
      "committed_at": "2026-07-24T12:50:00Z",
      "component": "R5-A",
      "kind": "SEALED",
      "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
      "protocol_version": "0.7",
      "sealed_universe_inventory_hash": "fd7b3eb6c6f162b06c3896b3838d041d74e9422f5e61c2eeb7b64a6d76c76874",
      "sealed_universe_n": 25,
      "signature": "2976631f90f7f53f8f8843f957c939b40042f61d7fdea8c027529ce1f9f67dd698d759bf513b2d396d64a734b6654ce18fa1e664de36ae0c9ca65007ebcf780c",
      "universe_id": "u.r5a.descendant-universe"
    },
    "wrong_logger_bundle": {
      "anchor": {
        "anchor_id": "anchor-R2-B-run-v08-001",
        "anchor_sequence": 4,
        "anchored_at": "2026-07-24T15:24:00Z",
        "authority": "independent pre-run anchor authority",
        "commitment_id": "R2-B-run-v08-001",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "signature": "1ea661a9c2809d616024841bc9ec5f015a2ae645c11d3a89ff10d59bdc615937b8fb7e024aa3855d64a5e053598ccf82245231fb899c0d4b4d8e3eefd8b3f700"
      },
      "close": {
        "authority": "SHVVP v0.8 commitment custodian",
        "close_id": "close-R2-B-run-v08-001",
        "closed_at": "2026-07-24T18:44:00Z",
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "final_chain_hash": "9f21bd21058527c095c8b6da5285e4323466b02ffa967324a353812eba463e24",
        "first_sequence": 1,
        "last_sequence": 50,
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "protocol_version": "0.8",
        "realized_total": 50,
        "run_id": "run-R2-B-v08-001",
        "signature": "d114ba24da19b40ed1d77daa214643da57dced070d679979d37d896156fc845db6d9481921f2cd2ab7425e8db2cf340b7ee12139e807bb02e1580f5cc4543000",
        "universe_id": "u.r2b.denials-run"
      },
      "commitment_id": "R2-B-run-v08-001",
      "kind": "REALIZED",
      "pre_run": {
        "authority": "SHVVP v0.8 commitment custodian",
        "commitment_id": "R2-B-run-v08-001",
        "commitment_sequence": 4,
        "committed_at": "2026-07-24T13:44:00Z",
        "component": "R2-B",
        "event_schema_sha256": "b7eb23c6b91ae0f9b15a746b250c6fae3e675fd4c1a32b69fa16d60d86c1d72b",
        "genesis_hash": "543b5c14abf91dc58b8dff1a04e191af5c7cda869cf99dd190a3e4ef544d50f5",
        "inclusion_rule_sha256": "8c4e47be51296071bb34c9668249cc558ba303025cdf94c282303e44e73968e7",
        "logger_pubkey": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0",
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "signature": "5d307ea5f950fd65d1225255ae29a29de4ffbe0a85dfbd6f10234213f9891928715f5b104ebb6c9bb82dfb9f5039bf96c1ee5c000ea1856bbc58b80f98d8560e",
        "universe_id": "u.r2b.denials-run"
      }
    },
    "wrong_logger_logs": [
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 1,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:01Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "543b5c14abf91dc58b8dff1a04e191af5c7cda869cf99dd190a3e4ef544d50f5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 1,
        "signature": "55cdf8f7c300839533b41c785f10ae327b6dc78279e5df5ce96e67daa596bc4a30988bd06fb33532c4ef1e8fec79b7a7c215647b42398387a3e302aaa89d4805",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 2,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:02Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "71deb3468b95e2bedd32061aa7ac7da229d7c5255036d8c8e8f35e622f904a27",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 2,
        "signature": "9bba74aa48b4ba3f915b78dc54c9e35eb69fdae8d6bfea61510a21791574cc61ff9679a2705efd1959c4727c9bcd35fd342bf13aa026305a731e364ef7ecc40a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 3,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:03Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "f0cc742855045200a72fb14e265951e7525b8a36fabc58fc38deb8e91f5e9048",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 3,
        "signature": "e23b11c51ca3d55aa3fc47e2937cf1dc4bb8f0c5a7d86d93f889b8c6e095429517f8bd48d2f12392f7223a19dd43a33331c77b206274e0e76e74fabf35c0550f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 4,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:04Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d70fe005e2e7e948be8a223c59d63a3b088ab2ca4b0953baa1fe0bbd69aa6e82",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 4,
        "signature": "36759d8d6430ad7a29124f433454c9b12686f42ae14dc12b9c882f22326ac98c0aca376d7e9eae4b74ee702a139e38e63c46270909b9efd71d6414660ac4dc0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 5,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:05Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "8c1a3f37f2c9ad460f1face74c8118bae594f65c743836d1e1d61737eac0a423",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 5,
        "signature": "8732cd6cca74672f818e741acaceedfbc39b725bebc5bf804905845b81d9cf901444af6df0b57854f1b526a84ebe21655382ddcdaf80e7828ea04d9f1bae3e0c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 6,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:06Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "79df9281866598a2bad31ab863efa97a8813843123f17a0fada55d08edc95906",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 6,
        "signature": "029443093593fefeb12579eb8cccf4f6db47eb557c95273c0d2138933dbfb62ba300e91e3eccbfe4c17c5d37d241d73dd59de899ca97eb902163972ca1dfca0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 7,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:07Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "78889169f2888a667af80c50a6aa9b6c6f9cbc751d83637fb4173860e5a6144d",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 7,
        "signature": "39e087d2f10b54eba82d077f35e55f79776db44b5d6e27982e7614f9df4e00bcf4cb78904af7a534047ed9cdc454a522bfc8bf7eabe0de90db33ef0197010003",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 8,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:08Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "07ff7ef0b68eb963ad6cfdefa686d194c5782aa3c86cdc8a8835c7dc3642aae8",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 8,
        "signature": "2b73f8b47cbc20b2727347775d27a2193a7cddf79c800c4f4e5a1a3dbfdec1aafc2287f40026d06a11bae8537ef494822f6c3f0992347443ce0ea3bec6702f06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 9,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:09Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "9e264cc1b0ff4ca042cebe2815aee13c3f2483ac8a7f89503a8a44482950cbf9",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 9,
        "signature": "6705e5b15e974f7b2dd8f5763ef2ac3d66a0b11a0101e1a04c246ce074a44c9df4b00944e461a1d1c10c54ed1421bb87ae6b9822e0ebbaf40bb5faec7391ad0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 10,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:10Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "5a563f0ecc2aaef20c47904b7b066e6d8dbb5e72f67d6cd350a45f2b9a31b687",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 10,
        "signature": "d2fd5675b6f2aacf8923bbe74d3d3931bc4ea9ad913a128e02061801c9a93707a1ac64c271b0c400f58f7b1f8dd6f341b26ff26dbd83331ebd2f733a176ea307",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 11,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:11Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "952034b3af674239887d15ad5b846889e4c6a7a200848c62db28f397133a5220",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 11,
        "signature": "6f1c383752c4da8e7e872153b67cb014a3c6624c5ebf6afadeb6a3956e37f0565a24b4182836144e75b34a4b58101fc359f722b650c86da8b3d5939cd0fe7106",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 12,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:12Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "ee801a7252331dacfbee0c90e4648c6be0d4ef9a89891f990e4595763d5ec10e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 12,
        "signature": "912777a0831820791a153298c15cf71191c27b31e0c58c695af89389f1b94a26587ea4c577d5895a9816191169f2fd380d2ee82f1c50d9c0e95dada7cfca7e0e",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 13,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:13Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "8d19fd296cf23592fd16ff29e61b417b7946d8384c9c4568e02532e1795376d5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 13,
        "signature": "e3e5429848815620486adc420cf905773585e1a86da5d31ce9e6a7ee91ed97b0d7f2e27b475b3561349ff6fd0d60c2a2772019e935b48d744f6cbeb1e6838e0b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 14,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:14Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "bbf55f7ab82fa732b0f34695c34c7dae038db475bdb3da4524e79d5c893f688f",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 14,
        "signature": "01757c9afa79c836579509d36debae618530cfd299b12ba2357fb4b3d0123f163b997e69b7be7268d4af1b20d6fe404f7de7b27001ac4a59becc0cd6812f9201",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 15,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:15Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "328f30bec3d1d9b8791f4e866874241ca33378abab9e30f69f1bbffcb5cfefa3",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 15,
        "signature": "d3700c23d42fe2699df5d5da293d33ac664954c0bb1ca8cbe085cf54bcf8bff8f783150d61ef0035b4eeacbc8e5f49d4054f168e113cdd95b6343b04aef01c07",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 16,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:16Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "44a2160bb300e08c157bc301d73247c785024bd214457bdc83feedd10bcbac76",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 16,
        "signature": "cc0d4cb3fcb0071a30c374c46c729eafe82fae69fc022a83ee4529f2241be3e19faa6687fe9c1e0d350e281cd408670e41bfe28c55a9249c8129f758e8092b03",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 17,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:17Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "b3cdee9fc102eef3410350eb47f80538722c3fa80c4506adbd12b16efdb94482",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 17,
        "signature": "83bfd4f2d2c2c7fdc04448f7154445868cbaa850516a73e2a83a65ec3bb6663147e90ee5125fe06fc1cde3d179b29c16a59d324cd98650b7b561e51c078bae06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 18,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:18Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "2a78629c31a293c9a4861afc62246a96158ff566c9cd85323a8aa62e88592196",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 18,
        "signature": "679df62e01107d641b63b063196ed2d46f9e9a532121dc6da42eed3459f8e198d70d78413d4caf4f866f36e1fd26fcdebd81721249705c8046bf394a0e9b9b00",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 19,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:19Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d775ce3d99ce1af65328119078b54a37f225eefa2c5fa75c88713ac8a7dccf07",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 19,
        "signature": "6e212d184adcda353a3e5f4968d9adbcf40e3b95529c0eb581b2b3133e53bc14a121771a30b2573a4068000369ddb519b706a0396217e9f31f66383bf913b009",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 20,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:20Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c38586532b0f5283ac66d74b6065fb8402579774deebfb773e6e0e0874dfc716",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 20,
        "signature": "62a2f22a190aeef08ebcd13e5a3311fa725973c4b689c550d094e2e9a9dfa17c20d945e1fa0ac2c2861d3cea6b02e145d8df586cafff86ae97774e3af5027500",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 21,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:21Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "50e7b47b493c0880af6168cdfc752e35ad14d93361e43348263bc54d6a87dce5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 21,
        "signature": "3043b6fefb7287304100e5ef07cf3b932e4b7805553673c6dc4848c8af8e41885dcf99b2898cbae4b4843cb1ad1f3a69f617f1b3698cd159a1a64df54b7bd300",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 22,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:22Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "43e420526b123e5a56b07758f34cc0344dcee5fd8be38c02c98727081f0cce63",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 22,
        "signature": "33e576be78ca20a8c0cb95bdaa2afa14593f21bb9357a98aabfdc3e4baecbb8b2e495f162b0ae726e9153dc6b8ec53c8354176b8f454606c2703f79e9ef1a20c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 23,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:23Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "a30b33611531d92db58d05f91c652c6cce2dea1b7fe176a5738f888895f0ec8e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 23,
        "signature": "a6677762facf6a561f69e41efd4f77abf1f33c3e1533d64135b57ee00fa869765369969a46eda970d492b58b16e3505cf81038ad0d3c1c2a55780ddc59a58c02",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 24,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:24Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "4a7f250abf46f7804c97beac5160b7d8a9f3c000b0ddeac51faf49d750eaed94",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 24,
        "signature": "f0faf9ddf135b9fe14b389212aa68e837c425b7e6e2c11f4d6720cfe43405028fd20f841a3aa1da263063b2ff74901eebca3a8011ea36fea4353473fa78d5001",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 25,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:25Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "fe2cf240c024c54e8e96979205e6d36697807c7a09417c22e58803092f9dc2e4",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 25,
        "signature": "c9fe75643bae2a8636fab1081c9f5a9104fa58148c8136b91c94fc2e4445cce5792007e489d91b3935e1f225bdccf22c845df3baec27311fd0c174e8eed31309",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 26,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:26Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "a85d752171a216f56415ed5f44a26e3e12dff050d0bf21928dbf0d7781789637",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 26,
        "signature": "f773e6234e094f1fbc08bf35638fc01bc243b6f3b260e1e132c93bb95c22bbd57cbc82cf4fd2f16485662d7ff349a3c7a397ea55cc869831e44600498c639a01",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 27,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:27Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "ab89d9a5e0471f4cc0fcdd1c1521d628f6f02e0c9b87e06f45917b58de6561c5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 27,
        "signature": "0fe73fb770fad61d3f47964a03bd3d594413d4452068d298d0664c4ea2416ad0c7200489e5b7905005641af76813d0f63f8e2a40f3dc2720c2f32d34451d2202",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 28,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:28Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "ec034c72c986cc17fae0369c2f167afd04bb04ce12d2206ee90518cb6119510e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 28,
        "signature": "b53732a53e10f2b9b8c0b8a1015b9d150d46f17e1a1385f3ea7782f775d85a515137a69e8f02a29e4f7bc024422fa753159d27909712e21232190c0644001802",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 29,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:29Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "79e86f0300d830f0855db9aff852bde36b6ad5825228346c0fba86d2506d13b8",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 29,
        "signature": "5ae717c90c96ac34d2438accab262ebcd510a380c08891f0776b39d9aa3d933118904f067be9fbccfe048896ff4efb5194aba0fd221be5efd07c30842b784f0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 30,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:30Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d96be26d2f6b21063a9847862b7e8d9159c92c7566152f18fbb11a9b9b108c09",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 30,
        "signature": "8fc0bbce18f72fdf89a159103d507babf7a8f85155b58aece891e2bd561335d35ea4e110cc7e92ea1496caea1c6771f2bc107d60f91a0b05efec56ead94d6c06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 31,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:31Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e0c97d0a69230b07d5e14242773a09236b443e59c579cbe16f2926f39ddb1009",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 31,
        "signature": "53d43232fad4e2b6308af9ff47a2572468142bf6d506f6a0ef9de3350bd61712e6e5722548065ca35cbe6357db711c05ae815b0f013a3d6f650f66150db77402",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 32,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:32Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "def46ff45cb39606a8cbcba64dbd6d2816ce3b9f7bb73744f8de6c70abce07a3",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 32,
        "signature": "15f2f4a452581d24c9369e4aa7861e84812cf0a9c34d0020004a1df3ab26fcc99aefa464098d8c985ec9189b8584357c9234e9e7dcef4568e46487d0356ca30c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 33,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:33Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "448324269db70fbded1810c59b74dc749af0a7a98c346abec7645d7e36db6298",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 33,
        "signature": "b092f14dded36b0991644cc80d81d45c20b435a1655ea42820d142f359add56543e0b8140efac0f1c381a867a7b5963308dc5c21a6fbd19759494ae85d9e240c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 34,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:34Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c53d0024db8d470b09d0ff832014855856a729459ceb73e97e1b9e63dfa225f3",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 34,
        "signature": "3c6fb3e3399449138084d7013117cb3ef679105cb677b9a50d2ef56c585e5697a3664c5f589699d1faca3053deffeb3a70022b2e0f9f29da4fb3f0985e386507",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 35,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:35Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6a9ecb65c0e1b69894a2bf92688acdd24bc0ac00ad616ee7054e9628e341c3bf",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 35,
        "signature": "9df0a9828e9557f7df8d3d9248c237798725f77a4c6e06dc068759f59165f15a45260a70992a68b4325a298e570ad68280716e299fc28ec3278d8b39eb3ba80a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 36,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:36Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "2c85f51196db717e343d40d9a37135aac1ca32a21e1c5d4a260c79938a928827",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 36,
        "signature": "a9e06187c8f1095abe4965f548cd11957740f525525efc49d96c19b82c654a4160d7470b890b94821191c2e7a2416cb0bf96f815455fb4813f0194aa50c6a90e",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 37,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:37Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "4bc0b86c6d22c9c12fca7db3314a5c5be0679331fe29888e701496336f34935a",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 37,
        "signature": "116af1f01c2fb6c03b423b7ebfa5bb64f75a0320b6f98576c85aec1273c42473f5f3d4bcea0ad4cfc204942077331eb8c8f88e561ddd5bada90a9d1f2a90a406",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 38,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:38Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "aa37154de38517d5175e23f66e84d484db006fb2380b7942beee21ca3efbb5aa",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 38,
        "signature": "3fd6b776ab52e06277cd6cde6ae2e77beb07f8c8122bbe40b7899654f22fb46fb3299d66bd448920343084b108bfa9dede217e7023f2fa78f77ec2d2fadb0803",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 39,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:39Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "bdeb7ba6586640b244179466212d7cba635fed17b9d2fc0dfbcedd4b2c519aa0",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 39,
        "signature": "59711eed1adbce35ad5ca61718178379c6469392abe05483ba477509f2a70e6ab6e3ab7a823f686844018c44badd56e0d1814a661a99744eac38dbac51914003",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 40,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:40Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "82cc8d4fd5a1b841abbe559a21db94d1c9aa120bb2ff1bc61c7ab85b9d782c57",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 40,
        "signature": "67e977cdba04280c73818b64968fac5ec276c0fc4cd3136a7de0f0a67f6520eb1b4460fd175e47dfcc598c00d90b94497720ee51712b7c6a873169bb37499609",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 41,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:41Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "7f5c30940615239fb88022d00deb25fdf2c7078684190be6e6d09a1a45e52652",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 41,
        "signature": "4cc4b49c3c3ff4200428a206bb9254885b6179913034f91df9e6bf078f288f990e516e4e3066ef7a4caf15f258419a73706dc6db55db13dbbc884a49183dbe0c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 42,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:42Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "5c21da27388e5d9a65cd5f5630a14eb80904ba7c2a4848b9dddbd10cbd055285",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 42,
        "signature": "fa2727858b82ce509500fc32a7faa51e3ef4b80f5357915a11eec691d2700a8bdd525bb0140f19b45ea12811e46950fc7c80d6194697f9373666fc8947c4af06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 43,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:43Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "b25f54cd3f63537b546e73c5a988f194ead9c59ad45458f7d53974c71297aaac",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 43,
        "signature": "ee334577f792f2a385cde445ba8488a7fc84577b9fae9a561ac3546513e19601b6fa52a53486fbfee5cf8012b0585afb1165d39aa813374ed7e1a25a4d939807",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 44,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:44Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6ba13115e96b8d8b67c623521f092cba9ff6a7f71a8ee567bdcaa2332b2eccbc",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 44,
        "signature": "642fd8c16b86648cc470493f8bbec21bcb348366049ba9b4d8ce2c59bb396a84655e46ca46ac1f47fc562e00275603b35b590e35de5ca911ed8ba182d9de2f00",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 45,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:45Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "64db5fe7beac7e25fc7379747f986cb7d668a534ac5ebe69e7147f2b9564ffa6",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 45,
        "signature": "988a2357ed03b433437a6e4370cb96354a6d72dc1b68ce5267fc046e045b26892704c980bcf3695615d8939cd079f0fbc439794604a25c3a4f501826ab70a907",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 46,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:46Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "557f820c2bdebed482386df01f1a6e1f9d3560f1881805aa0729f94136f0e43f",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 46,
        "signature": "5c6bf90d1496fc541486988328ad5645d0a7d3aa0ec0ddea49ad72e4298145c6572d1c2e04dc39e8a3d0712009ffb471defe752510fbbda9328dc21cdda7cf0c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 47,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:47Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e34906b54b979baec76db6621519f5cab89fbf0f11c85d7da4b0f0f7e70f0523",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 47,
        "signature": "4b6b681a12b4cc90d5ff9610b84b8e49a97086afaa782b40e7e43e8ef4c80c0ec4f57aaae85098d23bd953e3c16aa7855acf3d7adeaac76f0c43169355cf4f02",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 48,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:48Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "08aaf2c42950ca9763ddbcd16bd4926d7492a9d54bc956d8a43588641d7467e3",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 48,
        "signature": "7393e58c722cb48fd252f0640501deadabd353387ade27a695ed72d8edf43ec53964af64b738db4a7d63a277a633cba4910c8b9c5a6961a02701af9ec72b5d0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 49,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:49Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "170d255e1e713fe91239ea7df149797a7c0068d48666e8ec1231dba581a14783",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 49,
        "signature": "b217e6c1ef28e3a42c0f209ab84e2da2114de09b7a1b4cfddbc592a03a49192492f120584ae9717317f9c1c4c7fd22fe159f93971eb2954c5e7de012d50ef106",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 50,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:50:50Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "1c8807b6078b268d92069c7f69c3bd0ab6ededf68a032fb968bacf4c9947c3c7",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 50,
        "signature": "893c9170820396d2ec4c10765cd084ee132fb68ce941feef63dbc34b57219191f6eca25446dd535b45dd2f6de5f47518d66bb2f571929f7c26c346e7b269b409",
        "universe_id": "u.r2b.denials-run"
      }
    ]
  },
  "note": "Private keys were generated in-memory for fixture creation and were not written.",
  "public_keys": {
    "anchor": "0ebc3b1e23207fd41eef3f519983c5eae76efdd9555d8ec142b7eba3b64e2a73",
    "commitment": "b603204916623ec030e6ba851a321dc67f6a00c7a28bee1d878d0a71a611c251",
    "logger": "8d8dab152398183082c0461ece15d06a58528c1e6df942c153d2cc024bba28a0"
  },
  "realized_n": {
    "R2-B": 100,
    "R4-B": 60,
    "R6-B": 40,
    "R6-C": 35
  },
  "run_logs": {
    "R2-B-run-v08-001": [
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 1,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:01Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "543b5c14abf91dc58b8dff1a04e191af5c7cda869cf99dd190a3e4ef544d50f5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 1,
        "signature": "568f46386a07dfa12c27e460144b90c52585929d2c2e5298a1de0b473fbae1ba3236443efb2bf330cef8f57d3b0f70abdd510ed2e7343cb0546d8813e681160f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 2,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:02Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "a82d0d35fcc06812c5f293a0c2c9f92212d97d976f88bda9eff3a2e4c8331e45",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 2,
        "signature": "b2051c981aaf384c3d734b81f136e7b52251e120c4884ea868eabf65da6c44391fc288a50257c078dca299089f6f10815f9827924990d9b1beabec887c71f000",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 3,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:03Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "14b1135fb95bc389222d9c78d149b463b1c6bff3ea71c7e33bb1d69bcf91ab45",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 3,
        "signature": "bb1401a9e8af862e4e34aaf43f785fcb728687c10e657f30ec70fc73093d2e1cb6e8d77039c4e87eca12ff9cde16684fbd56f9669f12d9d729b27705e249230a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 4,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:04Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "b98d496a78ce6ede748a814a60ee7b29ee342e37c4f0683ae55cc4a3ac0cb547",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 4,
        "signature": "65b74f5d0b32a147c703adc1ece9ebdaf7b9d2b1acadfa1e3608810776fc0d4c7a2b8ab124541f02aae77e17377e49827dc4f8f404b2d9d474f221df9bbabd02",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 5,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:05Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "569fca51e6617a9d3f7917d36e46b2b5af885188a9a74ff60c414ef01a2da66c",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 5,
        "signature": "b4727413f247ba6f8c3b23f4b63004bfb33838fbeb0845158d1a4484bc6a1ac0752ce6dc310989c8bb81e35aa31ce0cf407a5b40269ff8b9101f5edbabf02c09",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 6,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:06Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "ecbff9cb9945ead1af2034622a9ca2f2800351eed5b355b199b73401decef8a0",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 6,
        "signature": "1d7a77cdc18e920df292dd4348c83b29cb20bef4893c535a0cb1a989adabe0cd0370cea587c9e2c46f395669ab111d4022d1d48aa920bec292479b13d8851206",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 7,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:07Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "346e562da20f66720ba6dfa5b0a78e59cbe01945688d0324194598846434a9e0",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 7,
        "signature": "bbfb1fcc902c7ca0f3dd1176f3fb0bd86a294e7864d286d075b37f112543a3a492578a02390f13c50f33c70bbe5a0ea13501fd2fa71a405f218bb05f1df53602",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 8,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:08Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "02cda8964877dd2ee330c094c6000acadbab92a46b992a18ef75d856c68e9381",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 8,
        "signature": "728403ce6f1d95aa66b2eaffc0f9baa5513058a4485f0dc8afd74a6965f33cf612178c1929caa6466508de980acee2e2d7c7e55a8e0bb7e0e6b57766ce6ce309",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 9,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:09Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "1dfc4433f8b0b03c4dfb024d0aeb05d6e1236bd5da00247070bab09ffc1aaaa6",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 9,
        "signature": "e55babba8ca24329f5673a686832c3bafb5476a2fa9458de1df2d19ab94df6772cbcddf00b2d47e5f45e90b6a75c9aed5427c60c36419cd48a3a63b4e73bb702",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 10,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:10Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "84daca9ba313f32a7601607b3b8b3a9a553d84bae1a54f14a721cf6146bb3373",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 10,
        "signature": "9aba1ae12cc45aeb0945ef07ece4330572df831b242ef6cb9cfd696ac8967e76f2bffe3f59daefc5bf443046754e02c12a4ed175184538ed3c2f2b440d85e104",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 11,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:11Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "bf2ead61e2f3b544e2daa568ac253f05bfc0040ba59efdea2bdc41b0abda306b",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 11,
        "signature": "ce6243f5c604d8e6f4739bffb8215e89598ae8d5de91dc6a872f89af5cbb4c3828a15626fe9a7dc7ea46afdbaa5f7fc9f9556998e08913c8fbfe1e55b48ab60b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 12,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:12Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "84c65913c7ed4c8f41498b71006a3942c8479e07617f4b6027b613fd6e2d5c0a",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 12,
        "signature": "6ca629a854225b4f67b8d88f10b602f5a7563422ef225ed3669c43a3ec7dc2450f4382af28597eb1a447ae8aa1c30f7925decf6a4371faac2ac8be0092cbbe05",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 13,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:13Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "9eb0f5253bf263d852170e85db46c8d014505c631b570b3b19df401f1ee135dd",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 13,
        "signature": "8a933619beb3e5478de3ac0ee3d47f002cf79677e75aac724041df1cde4a489480d2558b395ec502f0b033b634bc34bd5366d2f349c84ae28812f6ccc729cd08",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 14,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:14Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "797ce8b614d9b1a5e34d86fe30ae9c0a6c42dabf055e8378285393b1ff10e0bd",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 14,
        "signature": "d6131d940682c065f2ca574423cc999c5d91eefb82d338acc7bced6e77be0bb06681e166c6e7f0f7a7195e68df8090a19ec9b69cf41ff7c2bba2ec1cdb04c50b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 15,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:15Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "ceb0f1b2bca30a21aa27becb1b8783bff10bf9b13cf0c485738be8e9ce9e2f9a",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 15,
        "signature": "9d30bf762e8411aab9096fb1bb75559505267f847e913ca02a6fda7b500ff0fbbfe7cc25007ef75a2e50dbfffed0c6c20e8b69979ecd39f3b45f5af669da7c09",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 16,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:16Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "035aa684c88e86139c0481f5b5c517cd3968b4ffe453390b76083d6d03889c13",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 16,
        "signature": "b6f2b13bd3daf2e8e9c7fec0a60ba7400af7da537986da73619d07afb640d6f988b098440ab39229a899e7ceeb6759c79cfd3a9c010b2c6599b514f05e02600c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 17,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:17Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "77c2e88118c6f5bbed52577c35d1733d3a71d6bf734127a47c3fda918602e4fb",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 17,
        "signature": "b64bf53674a26869cc7606b5bc8bbd25ed124ef272a91284c3622debe05e1985f802069ab2ff080126c47572643372239458af0d164f4c9e3b884dc9c12e1509",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 18,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:18Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "a78d72ff8b7cce3e215e0db3aff49d7187a6fc499cac69602c66a3e3bf6d1ae0",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 18,
        "signature": "60ced4d9c1d47a7037dc012ea582a6fb5963c82f35802b9e24797532fecf3d1ac8a9013ef96cb385e6a3c256783250c1d28db96a718c869451beb0b184d7890d",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 19,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:19Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "51a6167b245f8ee5dce1e4b8d048d571460b3f39c57bb760fb402f7dc82493ed",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 19,
        "signature": "2a29f4836aba2f742b08a6e28615a1222865c229da03270a258adf023c9383fa1b35cc270b19e58f5640fc1f8b6d01b2a236dfe1f951fb778df5deb0cb08f606",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 20,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:20Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "7e3e8e3b3fc6fa350354be4a0546b2e0ba8c025d4878262cf77150d27d1de8bc",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 20,
        "signature": "579eb230370c202ab6f9645b74808e376a0c88e267e6e120c5af1f5b49be443c1c726604f49a3bfe848123aa73898a749392053f83477d75c6326e73d12b1d01",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 21,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:21Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6a29912cd5fb3ae2ed4361897978f904f5b931b32a26883a60c0e224ea4309a7",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 21,
        "signature": "5418ee60c3e2ccf75f095bdf7b45896868b422e3cc1e16a97e687754c8bda2addc8bf22ce2d70e229eab8aa40d809be4e26bc8578eed3a8ed9b97d524c1deb0c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 22,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:22Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "9007a76a0987639e062be2c6b6a44f713e2b67fbc02262faff36cc1f883ee222",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 22,
        "signature": "212e0c76b119dd978a48fa20bc1fb9a3d0a0b0a4fcf0582aa77349bf7784864b7c35955ff043c248a8ccf8fcda4f1c37934502e303b81edc8f82a478d7851907",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 23,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:23Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "58d0b076353a96cee6c6d9d8cf3a15e017e0e488481673464e00ecdb92109ab7",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 23,
        "signature": "5007e330a970ed63dbf505f0147a78964f7660cea79a666217c0f47652a0ede9d2259015ffccf70d513d861b62a8c3f7bddc0343c3af1128ee986849f9394500",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 24,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:24Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "92bda7aa560df040618b12d4b73084c1c10144cad23290d78c0dc748824ca2ee",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 24,
        "signature": "c6243887cb40dbe77ffe3ea74b1b2800ca7b4eae4f599ccb13477a80439796c49c7736ba13be6d756f5c1305016c8591353c91c25b866997e7e10769bc117d07",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 25,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:25Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "b9fa7cf18fbfccbcbe0ba43cf69a680d620c60e962038a53e813fc2a9bd21427",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 25,
        "signature": "3418d2544adfdbd47ad780bfe42c163e1df910cdeb08ff517d4f6b30a3836bb4b10fdee0e19709e46d0b86c222ae38f6099f9935376f2993cbd558baa5b4bb0e",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 26,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:26Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e50448196dc24adfa2b7cdded682931329fac7048d14ed599752d91476cca426",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 26,
        "signature": "b95530f465fd6f1117782f52026eb0090204692a07d40b1ceb343be0f5da2dea242bf56325166f9eea5643c227c4e177825f19acac78638494d0a2e2e7dc7f0b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 27,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:27Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e81880352411e458647bccfe2fba7ec28c29129f012727d7161c637dc828bfbb",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 27,
        "signature": "c0617455b74910178a4e20ca241665399a7fc970554d825a806791529ebe2976805ff47e6de6380ab7d82c1ca7222cd61080c5ff5bf64ea3c483a99eae0ee30b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 28,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:28Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "fbfa8fba4c16130a243c982cb4be8ce28cdfe5856c0d697169219a1e395def68",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 28,
        "signature": "4a79e17370e17ad5e942938c720a5b51259afd00599c3d9edc30c01a715ad9487d7525b12daaf7f3b601e0035ce4b525c9c3365385538edd92f3b55e96009902",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 29,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:29Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "30d061a6d23f1923837c951d11c54770fe0928fb1e0bb99477d4f698b45e0f7e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 29,
        "signature": "7385e72c3bd60bd841d32e3571962c899010c322a186f089225bd0883edf8650ab929a258308d3656be8c76dcbf9214d1769fc17ff51c079aa1a3c8784477904",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 30,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:30Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "f9c8c077dbb435ce9c4d2e2192bee4e89b3c271f4c813d40b70a5ecefe0262a5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 30,
        "signature": "7efcabd6ac1cde0b9930880dbae6c6c5148d2e380060c276df23c7dc8011858312a0e6df33fdb8026d2de82b2569a66d89b024d43d2d2217e7a4d9268571dc0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 31,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:31Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "a02cdf28b674e0ec7fb1270c631e4d1d5439a5e1ce52bde706c1cbef5c34ab73",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 31,
        "signature": "a55ad492a369a38cf48cdb01af3519d86662bf29efd05b68cf728731f9457b5d500885dfddc452294df7a63b6214d6ba674ceec9380a6b3235c2813bde9a1205",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 32,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:32Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c00ad5ef1cbcdc1c8cfdad96bc5303d92f681a0aad8758dc8d32609dca2992dc",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 32,
        "signature": "8e00747f002479be43dfc42e5ec4a8b60e2b7837e74a135076196f1941eea1fa26b431188431255e4d36bfd7530eb85dd2c079e93b8e0bc068d691c412b02406",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 33,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:33Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "564b8c75230dbc6565a42ddeea7c507b7558a29de161e7583a70e2b13ba504e7",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 33,
        "signature": "1309d0ac609cdae36f7ff84ffcc20948f147deb191560151472fe460bbb274dd2adbd08f0c51b72a273ca5cb0b6de2a49073f5586be6d67578002909cb619000",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 34,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:34Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "f2b116c07ac3cb3698f5b5e8f23bd12d1f21b885a873bc1036c24cd9cafd07cf",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 34,
        "signature": "c3ffdf8953bc83d9543ff41eaee5bb96461d8c3a185e4e4662ea3370052716b3f8dc0d71664c0932c013742e34581a6e317dc5beb125ff4c40c315b6f7a2f20c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 35,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:35Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "83fb8333f24fe16aa89fbd5e79c05c53fa830a420fdaeacf4765ef85fdfb8cc9",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 35,
        "signature": "3067bdad62bb789c4bd9d68c48d7fc70c0fe80fbb3759b26a64bcabc58ac47cdc72746c52ec9d88e6a30fbf6d9e63411fef78e10660f52895849bb14ca9e8f06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 36,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:36Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d1c2a1c7c766605a08ab2e1baf5be6f79cdf28da67fb5e15b872f23a3ffecc7b",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 36,
        "signature": "b3769a1720715532bc5c13b16f0e629668a528e83506c1eed4e84850ee9faa76726c366ce5d1d2de2a31849958fc3098723e72f7c6f61f4a390d1e18b85ed503",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 37,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:37Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "40fd95c72786676a178a69cb766a0ac77d731c62e01d77ce8cdd0cdcffe91fca",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 37,
        "signature": "d0a9c1ff533ebb74040bcccb83b618a24eb9d6c5f80ffaf60c848b0eff40c69856a39d10607c0dc8957bdc3f04af560466cc9442929df6f98784fbecbd621d09",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 38,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:38Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "154fdfd93eacae6e5e7cff732d557e903be6a3e1d8273ef7bf78324003297692",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 38,
        "signature": "af26ffe6db01d7858eb07852a1af0639d109467d387ff1a5d06e94d7ab1a867454ac179bb3848c658cc1e75bf5b39d4661ff8ce91680e569e7a0a93aec580704",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 39,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:39Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "5abd52836b4ea4c1759ba59c1b20ce8d31cd1d2ebffde9b730aa10bd55fc1ac4",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 39,
        "signature": "0ac4f87d8feb58eadd87362ee4b7b4ba199327a218d83c56c58e41a85f0d7375817fd31fbfda5268bd18853c33e2900b6245b9125abbf57b97b2f3e5a5e13d07",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 40,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:40Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d76f33c7fe4379fc0db436983c8c72ec0afae98891a7875fac0ba36a2752bdf5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 40,
        "signature": "8a87e5f2a5b829c5e2ce5fca311a79ffb3e4d9c232de7010b3a34e1b2d75ff0f86b768cf5e906a23cca4f6b5a6878dfd16379be1fc6edebb85ffa862c23b700f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 41,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:41Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "73cc1e9e935841b1e75eb5e6b783c2b9a40f1bb18ef7adef2495f0679877eb2b",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 41,
        "signature": "ffb818fbb87dd3b64c8df9f33e270e740a3725255e20581f1a227b8436c7dd46f42912d942b05d634147a26f89dec2cbb9533bd93af09367b2fa9555c8f28f0f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 42,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:42Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "2ee0ed6ff43239faec403cde0e09b9a1172d3253ca3c71eaacff02a20e02bc17",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 42,
        "signature": "12d814814a5b55124a6ba312d70f4a465c3027acdb45fe9fc8576dddd3885ad44a508e4fdb6c7799397b941e626c7698786b20aabf8382b3653349fde8538401",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 43,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:43Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "32270175b2a86b2435318be18f73421e292e7cb57409dbe6e86522d8eb12805f",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 43,
        "signature": "581839a5533fee3bf0891d1fdd0bea0313d5e849074d3e0a0da7b3617c1c237f8f66ed676c1d263531fb319f7d01ebdbde84391d0ff2df36ee880e3f80779c06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 44,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:44Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "92dca447e42e3fbccf824ada864d476c795bb55ced489b905741f7ba35de25ee",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 44,
        "signature": "7c2d7b13e31bb5b77eb604e63bbd079a1e27a2b498be277f7e2fa67e6e2a79a856e114260b2ff7e54f9b83a88df4b46b9dce66902e4cfa7f84069a288930dd05",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 45,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:45Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "b245b05816d986697f72e921a10589185f7f76ed5e1a847978e96468dedba15b",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 45,
        "signature": "181725c1c6118f140edbad682bed1deacdc60f9f4c3c1af95625ee9e574a1737c69106375418cfdb6163f475881cca9b2658a913f01bba8cae77663bce6def0b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 46,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:46Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "075cc56fd24ba400c2c2d6e6e92e263f35b5626c6345471a570512f8bb128c34",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 46,
        "signature": "4cb01dbee2ee688654a111cab813856b1ef4b56260eb85dfbd2ae6ad18a27d998477863d8396799c398c8037a65df1b772bb60df4bbda417be008e34168a6506",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 47,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:47Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c50820bf8e00a2862ef7d6d3e4b10d6bf0d48656fcb4294cb224d127f92e80c7",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 47,
        "signature": "db4573c0f6eb259288662bebbfd2db0a9cf03e5bb6c182f69e3f37bc4bfda75c5bed82e5c149ca07424ea46b5a68ac5ca3a9f05861d6c6f2ab653825920b2a00",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 48,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:48Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6c5818581154b4636d8122486cb4873f9e60e78b50136ca64e03a746b23fdaed",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 48,
        "signature": "d05592651c87fc969caa535eadb7ac19b7b114719bec4a0db4b84053dfc0b748401a215eb56d1140f9087959f4596ec409f37c2921118b727e6952fd471fc602",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 49,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:49Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "817873dcd835478a0341fd52dd91a43a3914c9b5f2fa02d76b78f9905dc585b5",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 49,
        "signature": "93d63b6026562b60b4b7d84092f7a99b483e0b38f045b8a90570a4d458a7ee7d2d5cfedd7288867fbefdac97abb48f61f09d36fc2880b19932121a7be41db60f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 50,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:50Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "468a65b9b6905aa7487deba4469018244ea8770251d3c4d5364c049c4756153e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 50,
        "signature": "7cc722cb841247d12f2fcb88b5a5ba251ef8cd74ea8ababd7592600f49ade500b5783100c08af678b0d84339f5f772759011160160f6c6209188320de21b7800",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 51,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:51Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6c70e18839047c24f708337d796ab8097f4a9085ff5f4f5f93ff809f1dee568e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 51,
        "signature": "f1dbe695e4610847911c9b2ac5432010358e321f0cd15e8a271e1bfc1b05edbcb72af7f269cac41776266560c1c3c307ea91d8549cdac09ff6e0615a011e290c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 52,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:52Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "bb412e32d32ab3d10e1c75dfcca6dc0cb908bf90d153d5caff1d7b1ef0075792",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 52,
        "signature": "3d024ed531cb49884a4255b37f1214182caf7976e29f252196c72cb397cd93b79b73028a6caad5798eb39f0806ed30ab397c2cde0a4333c9d55e9177c0bc2e06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 53,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:53Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "4bc350669096452d2dbdd16caf9761adb7c34376562c1b17d0a31a0cfc22bccc",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 53,
        "signature": "9a5690bf9a21c2445eb4f1c71765a1021a278e2311aabd876df7afc036946b1da1cf9b32f201e61740059f53237fe4df182ca865faf4929a14aaf0da3eba1009",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 54,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:54Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "81dfe309329a6a70197b4fc3651d23126935b5a813c90439d8e4f88fe8fcd58d",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 54,
        "signature": "501e9883865fceda670add225d6a84f580b075a5eed0db35b5fae3e73cf02a608e578de166d3856080002da20e7c4413c0f761db9af6d2088ebc650bf6e2db08",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 55,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:55Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "008940fdb01d299b0d96b32bef18ce44e30537d84d5f95eaddfc68e2f4cc4a13",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 55,
        "signature": "d9940ca5c17b667fd042c6456617ac0cb9f9b62e5a6ba0e59a961eed29f71e00934aa5e7148cba537adec35aeee03b05e336b4c01c123e0fd4538fdf4f843c01",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 56,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:56Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "97a15f27368d801b999291d177f1b3fab6a92c22a123d40ec742f1a03f32f482",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 56,
        "signature": "2f1d03e0825be60dad7fdde076931c853fefc6861dc247654d197744df3b4ddd09af91dc0d833b0f0eaabcf052b5179c82bdd2d389306c34c778de913c97a90b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 57,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:57Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d6745f556885766aec47306a487a97d78abd8ce61231aa90d7266e09e9597c6a",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 57,
        "signature": "aa8e833183fdfcbd83c0ca93f339e7640a5504f666bec680e75b1c50ee6994ab1beffd0f7dabd14125bbd9cbff69c0d9379f5e2bd33fe6927fe1d1957aa37400",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 58,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:58Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "77b8cbbff01542dcf8305783bb9b5b0da1bf7e790e112b3251bcea59caf9098f",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 58,
        "signature": "7e8bf341e0834aee70f79b3a9aa165884797faf3e78c70410b44d9f14e84dfa2d5160ed037697b3329b2f3dc374f017d192843776523ac916f10f1aeb7857d0a",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 59,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:04:59Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d64909aed9d5910164f7a9c8dbdc70a1c41712c646923fbd54b0f764581c9e94",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 59,
        "signature": "4670da779a8b570dbf4cb4c742cc1b0572fdf90b4f084fef5ce54c7f71f382306c97b3d8a8c5d0a35f08285906af15296011b263fa157cc2092d3fa93b28cb05",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 60,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:00Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "fadd3bb7ab6f621bd094da8d3fab342a4bb70cdeefb3cafd7d767cf45ac1a3f3",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 60,
        "signature": "9d61515292ed16e74006b895c60a86e0820d3a80c8d52dd9e44be256cf0f796fb12eec54f42acec9f704f18b1357806ceede03a32a7cbaa0b135a451993fcc0d",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 61,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:01Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "4bc902b4a3f28636182d206bad8852b6d7054bb9acd8e51a2c6b95113ba8d5f2",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 61,
        "signature": "f8b8e7e500e2d26d2cbb8fce7ee72a561f80bea930680bfded69d8cabd68aadc294f4de0edba9a1947366c03128e9343383e653cce418265a705ca95b937dc04",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 62,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:02Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "da0408c14d92e54073e82e3bf748f8c1f7a71405eb632ef718a5efcd3c584e5b",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 62,
        "signature": "0d75633b80c9e0c78a28dd8b593ab77db705342e6761b3983d9b08e914624c494b68358e1b2aee4e74cabefd9870b0da324e0667682cb6e6142d643b7a298609",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 63,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:03Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "8af327e50730deae2ff77b1d92d257ddc559f97585e56f164004b120685fb737",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 63,
        "signature": "2dea9744e2d3c503a47aa28ff90e19806d66c07c8ad74cdb76f29673780d4172fbdabac57675ffce43b8db7b491bc0a9637492d51b8c6669800cffe2716ecf01",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 64,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:04Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "37859fe7f31fea0f9be0606d0f1f746630a6a9205011ab94aec9aa75f23bb01d",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 64,
        "signature": "ecb4f267e8b7b59806809f0febb9d1d7f78058badfbf6139a0a7a8257377da12cca536a9785984c1db62ac2587ae2eabb42ed009636408dfb7570bafd519300e",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 65,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:05Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "65e73f92930a410a1797da9f923ab617b26beb95c5336101363ac1cd320e67fc",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 65,
        "signature": "ba42a1a2cfecf8176cf6476db801b9beaecea3ad80b3a1e4fa5f2d1df51499ad6ff63e1ccf5792482f6adac831c3c5e58d274ea1ec0417f114bd245888158c02",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 66,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:06Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "1b143b9d0dcefe97b236d70d58f1d9dc35b6d24ed7ca855903d463fb0a1b2429",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 66,
        "signature": "c522422450f7b64bad7e6dcbeb906a50d1931a55a9b73ebacc561a30bd355513ae4db9c00ea780e497f57d2382a71ab7e4c0b190a6ff1162b4cfc79960934b00",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 67,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:07Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "0f7ed0d4bea8698b5673700a3168e9c68172e26a66f84558b3fd309c99c41fab",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 67,
        "signature": "51785787d308fc0c83dd72e77e2b67042eb1445b7193ca4956b37afd68965bf8dce49e7cec536c96a45a88dd6b79d7e23b67dbc10cfe2328258944b389c9ef0b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 68,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:08Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "79eacd10b2a4e0a7307a32bdd193f84898994177d2fd4197278825d02777a046",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 68,
        "signature": "d9ee7fb98d9f59b1c26247941b9d2e45ba337b32556d964736324138e05f5ef74c6597ce4b4a7b3ffe2ad48862df49db95964637045e40416404e4c1dcc42b04",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 69,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:09Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "10112f38976e9674b9f6c5ce176a63d935e934894862379262f1b01f566fb129",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 69,
        "signature": "b3ebf8523ccd9e6cf7f13ddb77bc09ee7cd77841ad033377a07ad99fccf96989915ee3f33aae86cff47163a4c57aff6ce3af83c58135fc5d674dab7ce7f7d309",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 70,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:10Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "aae284c80e0e2646ceb0ece50a6862dd2acc8a3b09e437f9a0ca002f31fd25d3",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 70,
        "signature": "280ea5fae78d34bb2f6f4712d877f35ca121193d4cd17c23b7ca007cb94171dda5495d20e64222e4da353120b11e169e4062506050cdb16a435831ef5450190e",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 71,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:11Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6c592b0737471d2ec61e551fc4e8c1be5e179d4f63454c7691c6083f37958ccf",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 71,
        "signature": "c937e4e8f9cbd42972d27f3ed649a238418c20be99ffbdad5b06130bea60d003fcd425c9e1ffba16bd17271bac907fd06a0b3ef9233747d5fac083720e362c06",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 72,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:12Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "672afe793ae98f677b725fb0483c064564c72ceb07698497f8a91c529e4ce5bd",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 72,
        "signature": "8c26e23b0c4a870d433029973d2f1da455d41e1ae3094e1e8549833d145b023dac14c4717ec66870b52b0a2ad0a669eca12b063ff2b7ce5dc8dfcfd83e241109",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 73,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:13Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "476ec3129b4d98a7a499ff9081fd4a02d8cb4b61ff78932c5d4fd5371198a8c8",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 73,
        "signature": "052d0aa097f505c6cecb72a393f205ef2dcfbe6983611227e21c2b4b597dd6560af974170ebda6b3aadc4f1decbc8a73240e18c48f25085804866ff85435d30c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 74,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:14Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "db897b04115a597e7188b6b01469769712fa8dea80e3414ff83a3566e7669996",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 74,
        "signature": "d85da7ce210df0f4cd46cb99e8ec839e33777cbaa4b6112d0a8b0627d5705e375e0adf69969d457c0479ed709105999791f14732f1c935a5c05e9092675c1201",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 75,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:15Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "0140f62ae70ef920fa907136b0495207fe7800a012b9897ec5ba3f3b45cd1157",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 75,
        "signature": "66ee2329ee24a5b5459cf7463c4a9ea0f98190b0a1643ffaa590041b75509b5fdf6a31fca6afdc69f162ffa045af8d9fef9185b4e734c8618f892ef5ac23f203",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 76,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:16Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e687fdaec452db4b5f52fa1af0f17204cdf5320663a68cb80ab1b4fc7bc00ed4",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 76,
        "signature": "2288a8a14e8ccc45604fde9d1dce125e589356f2e7b2868bb17456bbe5bed76ec47fd4374fc36628fbaed91a8f21130cd0c64e84d52887e71c7d364b68919804",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 77,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:17Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "95e407f4441b21ad5d9ecc6049cf8a0700ff8a409415956d8bf25c3e4509d9b1",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 77,
        "signature": "6114504d4592e48704b3eb51fb0380ee1799aae3fafedd49e8b4ce17ef2a8f54a1e643d198c1876d013ad9282f2e318cdf225eb74563f73e81ddb74fea713301",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 78,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:18Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "d738b5006e503e0f9c8a9de13fb200d2388e96c4d21d92181a34cb071171c623",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 78,
        "signature": "e40eeba718e8a63ba82bd0601081f3df597dadbeeb39ae2f0a36fe04f3ebf3838c848bc5114397fe82f1100f0ad1a5cd79072b862f15feddeeea3393b869c101",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 79,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:19Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "4360a1bee21e4aca1e272a59261fa69f5c43052033202f0458ae4e4aed9495b9",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 79,
        "signature": "d9e60f7a4b169d65d922a9b0a0a406d4c34a639d1b0658633d9f398cbf1bbc5eb7cda2e8b62219a30575416b55b74242260211aa2cd05b5a354fb9a9e0809a03",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 80,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:20Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "65cfe833312d4a424893f97abfab192bcd0debcc8a41128dd6f5d4916eeb057f",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 80,
        "signature": "dd120e64534fcb8af7a9bf93d5d60ef6a82e6abb9fe1685f5fd562b94264c679d19c41d69d06c720c825a4c4a3dcba78050ff9ac2ce6f9782637862f20acbf0f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 81,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:21Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "f32f99fa02fed6427e60ecbd1829dfb56dfd1c20402eacb019f2c2a93851d562",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 81,
        "signature": "58f918c5272cacf372a3c1c5b0abc8ff058c7b4e0df5616bff904771baf83e6b8178d28f4e4fcf89e0b6c936923a307ab981da7d49a1d264f45ad113c3e15702",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 82,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:22Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c50377bf28fdf6258cb346eadf3021e6338f6a347909b898e477a3d98f9b6b72",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 82,
        "signature": "5fae6286d2a86b70e920dbcf207f66df89237b597d28ee60aa0077088ff83485a3be10d11133549567f8b30da3d60c21141728a674f382b250278631cf591807",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 83,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:23Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "32b55e1874fb44352a5cd7cf88bba5d1fc6128e54dd3068510d9ad1185aef3fa",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 83,
        "signature": "1d2ca0dddfe49d0d9bfad883d324079201490c732810e6fa31529b47ee51102c7b74be8adbf357b2c87bd4788443ae4e711c38d5c0b4eed2aeec22a277d0c104",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 84,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:24Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "06dd9d9cadf6893eab18b79ca0ffd7d19b97fe50ca34ccffa67e31eb4580ae9b",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 84,
        "signature": "3fa0bc6cbc5c5f150d3ed7ace4a60419f5c46cbd2fb23f120e27db21d234ae11d63f72ce8157201b41f4c3b4fefae49d3a08fd89581ce9b5d081f499335abf00",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 85,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:25Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "aae2c29fa30c387f5f50757ae02cc976c6607f5f19d5c4904656b06450045017",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 85,
        "signature": "dd3288bacfb4b47f441bd5e991bca8b25223f16c2f2fcaa1b9b9a68b0582ce2a216d1aec0098d4d28fecd9129a62a17fed6aecf44ebaa74a64c8352ab264640d",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 86,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:26Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "dd2a8c699d1e239751c4595b3fdc69dd2b74011b1ffd8f8bbbff5862a5474dae",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 86,
        "signature": "a17d4b9730307247015461933277de43a07c55776f21b6737d8b68be732367546c823591b7f284c3e180812746e624c8874cca8cbc4f47086643233b8c98ee08",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 87,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:27Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "08ea7633d47ca4854ec8eb33e6997ac46e59b99fc9162a3759262b76cc99880f",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 87,
        "signature": "302b9677ae91ba41176e25a72549eb509f8d506165b7b39a6c8bd39fab558d2945f7ab789bb49ba1b95b44a6baf8493da615fb693c937e1f1611f16e3394c90b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 88,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:28Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "2816677965d568d72736534ba0c4a53847f7c4bf87312e402b92de5f0484ad07",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 88,
        "signature": "c43b94a42d7a8edc708608d49a4d6bac988ac9d9b3ad3a7d926f7ad276ba0f98bcf4b6f51b8f194778e2c34284c7b400169695f012982ae1fa45d24764e6b00c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 89,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:29Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e96a45f24837fabb677053fb35d65ca327e541f47c954126f0bc9f236da13f95",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 89,
        "signature": "8de99e682b4ee1ed8fbe3e45f5dddc0b2b7996972eb69fd1e6bafeb86ffe6690dcdc7fe34f9ef20336cc4faa704e328641d2e798f0c4257349cfb9477071510b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 90,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:30Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "e21e3cb4c22827dd7cdca76c4823644b4a3a726e17ba699a2b1c07c051351a42",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 90,
        "signature": "9cdb85c7386d2b7847dfe3e92565f3dd09d819b71faa8ab2fe73a1111e6580da4c00f5db751f2263949fca0d8af69fd7229b04aed30994a188c2a772b424e700",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 91,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:31Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c55855b1c77ff18ea5d95f4d14ad324f7634c8295fe1e8583746835383e1f8d9",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 91,
        "signature": "845c37ae3a471e473e08f2c4d42f1038df43137e770ab45ab3302a5da23d2bc9c7fded0a65d7381b0b3c4a31358c23cac18b4d18e399e1c267c0a0404429ae0f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 92,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:32Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "6e05511defb1bc8ab3fa78cbe26bf762823d859efd7908d43132ae7f973ca7e8",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 92,
        "signature": "854c5bdebf3a5a7add73c7fd8f4a1b12b0217291385b9346c3e988bd7d1682980baba52be1e08b49d428dbaa88fa1513986e840e8b092b65fcbceddb4891ea04",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 93,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:33Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "2fd03e6e9facb20e1c713ca7e6767a06bc8b41f2e9a0beaddf5c5b451dc02c69",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 93,
        "signature": "9a63a08837c3cd0425690f77dbc37f9a4e827621172237c753d4790b89ab8e62a20d0f8b805b78e93bad49d7b9127eec4184e571bae08eaa695e921c565bab0c",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 94,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:34Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "4b47de6b944e99d7396b37e02404a12ba3df3e45ede307a2421c6a7f957b0585",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 94,
        "signature": "fd077e51f68d2ae1e12a0cfdbc28c8047bc0c75f0530ca8343fb82c9065420cf04004f255a47b4a749a7766fb5678e1316e37f11fc4067007aa3e5d9c4c2a904",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 95,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:35Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "5b00f891779f779336b5751d3e2da6f1c6766810ac33dc2d5e8061a23d885ff0",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 95,
        "signature": "9dcca6fc147c7bbd576bf184da2efa10494470bd622dc125a790174e8e303f2aef5097f17d80f1b79bf2ecaa74798a6e75ed8f5bf8263196d97b611c72192c00",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 96,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:36Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "8b441000f6724e757e283829f7574c427ee7e95205f74cc8b38d0c03e4c5d2b2",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 96,
        "signature": "12af24e1d5082c61f0f1ed247622c3a8330471f9825f296b7fadb6aa01ebb2ddad76e14c32cf0fd02f6889f311528f1149c0a0cb069302bf607b4f85c462400f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 97,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:37Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c22795f9e7b385aa365ab2358f1ad282ee061063aa746073edac7f55c27f68e0",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 97,
        "signature": "059446490fedb75426fbd503ff9ee985a00b3ae8968bf8e4978eacccad1bba09d58236bab71ccc7b4d847deb44605755489770103f5bb1c6e3d85672afc1b10f",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 98,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:38Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "8755d95192a53c938bd4410afda48bcf58b5931167e70a47032005087e948dd7",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 98,
        "signature": "ceda43412dd1963b69d24e2353c6a655a9eee1912764d93306886ea36865dd469db7018fbf89446ab8a0ed9072e70b92989141cf7d1824acd602cb169e42e806",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 99,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:39Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "81ae61b3a6178bd12eb882a8520729b8923ff9bbf1fff0aca406b566476dca4e",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 99,
        "signature": "f9a0f1b2b8d06f6fd70012a7d4ce15cb22a34087b3cbc89e0a2fc6f15f5bfe6bbf6b83855b1d6dad7f90d7e8331b28871f75fc42f4df1c3c11ed52262e6be80b",
        "universe_id": "u.r2b.denials-run"
      },
      {
        "commitment_id": "R2-B-run-v08-001",
        "component": "R2-B",
        "event": {
          "event_type": "qualifying",
          "idx": 100,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:40Z",
        "pre_run_commitment_sha256": "de7d3ac504656121387be7694bd8632a7a90f3a221321ba669cac97ee83a9659",
        "previous_chain_hash": "c21d7a8c575c3c7df971629f3ba063b1c4f651831aee8a5fa590abef9960896d",
        "protocol_version": "0.8",
        "run_id": "run-R2-B-v08-001",
        "sequence": 100,
        "signature": "61ef2ccca38f7be54e3f0023843b84dd931960935011f7a1b2625653805f80c50e998caccd25477929fc40dc5decaa8e9ec9c4520ed8ec9245d4286c105ada0f",
        "universe_id": "u.r2b.denials-run"
      }
    ],
    "R4-B-run-v08-001": [
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 1,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:01Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "97b8b77b04c4bf9ffd8757ea302940e664106b72892b0954c449cba923654bb4",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 1,
        "signature": "ae79200aec9cd415e39e3557aebca79caada9de92b59b22bcdfd81a8bad6c7c052b766a9acab745fc71583a93720144258f0d7b4807115343a8357e49aeb6008",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 2,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:02Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "4e1b04f20e70c024fecc383c0d4a64599f24de5cf2789bd96b87747faafdb889",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 2,
        "signature": "3e6c3a16773eaefdbb22e5a133031473c7d3c73edb611b8000bb01a4747970a535d0c524e132fba5ad2a80d4d097c5ccf5999298a6e7db353a91eaebe624f106",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 3,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:03Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "fe109da753c95ad4c2a021689b987dc900da6624ce00112880336473f27ab678",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 3,
        "signature": "89e40af123ac2ec920d3450a3b4d3d1b69ec34fddb86a725f270ea8258fcdec9ae08d7d0700a82065a7d7696ac39ee4d3b07d6b40362acfb413adf3da400ed07",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 4,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:04Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "0182bdefc51486ebbd0a2a82161f40b0f04ebbe70225c8a118399e690b7ea06f",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 4,
        "signature": "9669c3a886510b8e590ed450f0f87ebf1568576f9fe6e5b63654b1d099d79000865c2086f8472e2efb3c9197fd9fbf48403c4a60c61d3230311ae621a325000c",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 5,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:05Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "18f825b246368d61cd91766666a1ba632a7e07dfca5e134f6bf3a4c1b67b8e90",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 5,
        "signature": "cf4765d6455b7aa9b3b0ab6cb32972486bbb4aa1d5b33d02f11d7082ed7ee76dfb51a84967687d5b34ccb10faa7c351a2c368bc099905ab095fc06f012e8270f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 6,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:06Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "d04d7df2aec2023974d209ef84bdf79c57fe7a6fc94317167d05f9927ab7379e",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 6,
        "signature": "eb9ae65ce1c30e39a1b88425c1d80f345d635804acb411cd959a858e5c634aaf5a8be6e93d212b42f678741ce2bba940e44120ac3b59a55cc48683a377d6aa07",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 7,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:07Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "36ea4ccf20dc3d9f417b8913520ee6bc747f187e1f3427d2f81d3cebe5f7fe0d",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 7,
        "signature": "96cc79426ea0e3e8c18cb55bc63d84368c74c949011a9e298a170cc58fe13d50bf4e8348103ee6986edfb3d86dced94b2be507c78229864934ed42a2bf7d750e",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 8,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:08Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "eed53c0ee787c6531745fb9c9ad3518f4e5bd645ba88f4db3cc05b58f2baf2a9",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 8,
        "signature": "6705e8faebd608a9a755dd5d04d03f972d5549c1bc9b0c67926bcb5f714c00f254a7311847249b6212add8bf378918a4035e60e865ffdf8d3ab7575388e93800",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 9,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:09Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "329625e6d242be62a7701214f60d4caf4f9c50417886a2af6415d78de9c13dc5",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 9,
        "signature": "4bcfac125eff687271ce69a16886feb185845977d9abe96e7e4621a0317353b7c050612f23250c8cb2ed36664ba3bfabade60f613b493b7728f0b4ba9f2e9608",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 10,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:10Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "15ac64cab81f4ed1f606de88719d0ec7b5cdc556ab07744641e38932fb519c34",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 10,
        "signature": "bc30c060ae314e5703f83930b04a80818758e16fdc6a4da872f1c8bea33d9ff9bead294c06f6954f6baebc4926b154461ab28504c87be747b1d575d73e9dc80e",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 11,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:11Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "8adc21a99568850493111f690ab45088215dfbcd81f8788579b8b21d195c67cc",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 11,
        "signature": "8b9e0c69bbc25171fef179f64958ccaaa7ffe0460954f6b96f391086a4710790934752d5e442dab979341869ffb7965742c5f2e365de815f8dbb17208e8bc706",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 12,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:12Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "ae4e59cbcb9ee418aae0124d3e8fa6dcebabd2cf650288d499b6dd854780d606",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 12,
        "signature": "6ce147a6588e8794ca15f92b6da7630c8cd50b28f20f822cfa83d551ecd26d7f26c6c965bff3f57d5e7ebc9a05e752c185d5d44268ee55a395e2018066627702",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 13,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:13Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "076aec742271ce4e584c275a8794436cc0f4d402d18d54c24ff656f27c8f3282",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 13,
        "signature": "da57844edd11bfdd3fb2c50d6a6c34346c68edae58237e6aa982522a0d47394598e3eb47c99cd0fa8ce87be0c0ca31d81a039d652a7a6ae625974ceee86dad06",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 14,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:14Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "dcfe2030b0321b960cd739527790e08a97978e4f089b95f57563131e7dd81466",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 14,
        "signature": "1110bee11146a27f72d3bce441d7b61a64309d983915253005f5e9309b2ad9fd18b5e8765bdedca9ad0453bb7460c8c4310af8c43188a83120bc5941d8a90d06",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 15,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:15Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "bcdf72cb07b14db7111a6c59b76978380e36ad79c86b2ea66238c243a80264b8",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 15,
        "signature": "bb441060e570e32ab79cdd8c4d9f6b7ffc5bd2fff70c5bb21a56fe991be6efb2acc4c878c2ce268e1a0ebd9167490a7e00ae14acac769268d1ef1324e007dd03",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 16,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:16Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "f9e886436f57c7881a0a095f660ed58c655771b23585ef0737740cbe152ee1df",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 16,
        "signature": "8420220e26c650e2a3cf01420cb85d3e0196908e70b327b3c8be56134786c5ae646badc40adb7e488dfac4a7fd14026173185df31e0acfdae30df352f8ffcd01",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 17,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:17Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "948251f0cccf9566d4d95e641734727f288e5281bdb110b4436f05b362bfbbda",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 17,
        "signature": "6498bebe91d5de619b647c7b2479b61ba064defbf4b3cc7db7e415d2c6867b3d1d0dc735f64fb39aa628a3d08649507348047ed77f95f9a8460e7f82aad6aa0c",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 18,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:18Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "7726053a586fec142ee9be74c29acbdd049e77881804eebd09088fe624dec9be",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 18,
        "signature": "2e8506d9fa2892c89a2224cf53778341b037eaa891ee5ae4fd321faafd9e677bdf8217caa0199f6b229ceced8ae94d204620b987ab772ffd5f55f6e1284a180d",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 19,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:19Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "e7ab38308018c53ae1fa2cc7bd04590b9e1867f1cfe7f946203361d925612fdd",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 19,
        "signature": "59310b3c17d98c16a4eabd88a8d1e47df7a3d96218bc10d18ae5dca4f4819c6d3976faf77020dfe58d308f09e312050f4380002b6897efe40598504bfe82cd0f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 20,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:20Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "b8560f3381f4fd3cae535f2877bae7724e128b771ad097da030e61465ab4e467",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 20,
        "signature": "aafda0eb32b57fdf31d3b9a19af724c5a2031bb291eb41b1f8bfb8f2adeff2396c7fe8d23cd70c9d80e0c8749cb29329fb79daa5d8488fb6b16ba023bc4c4506",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 21,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:21Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "093ba3f30136270692ea0e02de9064c5e59861762cdb7389de3f18d6e226d79c",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 21,
        "signature": "3a32a7d27a597534931aee375231b79920869df8a45981af54343c7e92eb4769e024cc752e818c771015348edc2c009aa55b8f89821ae901f58811efb460a50d",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 22,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:22Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "a7a14e0fbc0664a95ec47b7b70650b0ba0b727d0763e5ad7b77471bff8a920d6",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 22,
        "signature": "8d966138ef113d598433851b470985a4cf1a1fe7dd6d949bc0e8a861dba0993d3ff61d44ccb9495f059074a299f3e31e1431ce214e26cb41cb5e04ad3ab31e09",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 23,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:23Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "a372fd2b083b8ae1c2ab0d2ec0eb2e41de96821d946e3fa408e54a0e5d30aecb",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 23,
        "signature": "bc48af0635968605d34a73c6f98f501df37a7e31c3c9f6c0abba9477bcb06529d071ad98960774ef7efacd9a98752baa8352befa049b7d810e2f96b8924fc50d",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 24,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:24Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "cbe8efbfccd631fe61fee31ac8b4d804ee87b4e0c4f066ac1f0f13c7e24555ec",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 24,
        "signature": "3e204a389372c0164da585475bd6fc46de94da553cee30ae22a81dfd9931f2046d41fc440afc7de800590ab818a493c2fc22a7456df624f029dd9c9205c1b902",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 25,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:25Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "012274ab033cdb5e3125dc71ed1487c4d0f85dedd61d2574cc840c8109d17e04",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 25,
        "signature": "8112d52ac68ddd8da1ce0c6401cb307e0d74106dea90d949bdddc6901a2d0133ad2c5a23699d4be7a5064e957d815eab79e512cdd91ba10e2a03ac2f0ac7340f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 26,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:26Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "c017c90e5fe32de2997c9b01307c82841f91b027825554139480a87362b66b09",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 26,
        "signature": "e900e9c28114e08ffca6e64fa7aaf166fb0cf77b0d75f2b1f65e08a3125b7857123c4b3b8717d7eab974a6c34ddf0400deb8a3d068b45ec1597ee9a9a76b7108",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 27,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:27Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "6e3f0ce39ec600ddb86b5a06627b7b6f272faa4a2476bb87bba2f9043672cb8a",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 27,
        "signature": "f079c9ef4216d818d59d07692ed876fa3cda7407c60e3cd53c37210d777c37904a45f6faaacbb2b300c7a3e00934a8b7e41616fb29d478ff5cdc6aa70677380b",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 28,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:28Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "d6ded9e28db08bf740f8afefd78bfea4f353d5692a37fe6a41e86eef2450f895",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 28,
        "signature": "7e51602ff08b82861ca4347e4f8580326a599c196dde96bb84995e3ac23e18d466eb85c031410eb3261177675118f6aedf0c6eabb230746bca606df0fced6809",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 29,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:29Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "b262134b339738e6959e1b6ca9981c9b6fa399dd41b89e6cd06358df36042a5c",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 29,
        "signature": "3593152f611347db5e5d78a28dd1ca0a36b9526f3bfefb85fa360e5617d9157a7113af3a311479ac22b3ac6d983f002e77686b47a27be6acddedf821dcfeba0e",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 30,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:30Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "272eebe450e84f8cde0759726925ed779bd94ae4caffe96432cf6704e4e11b2a",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 30,
        "signature": "af01825aac963656d940db6758f6b0d27952434b0d72c103909616fcd1cf5ce930725278fc31229d25ffcd6367b5f6258670527cc37a002466c8eef752f0d509",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 31,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:31Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "a9afba7b1ccc371badba07fc1980225aa4380faf165059d9817146621fa886cf",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 31,
        "signature": "92b24ee7e1193ccc864b1407e688a76e85f79d7061783af7a2c6b8048173226172d774f75edb8b1ec012fe759ecfb1cc573ffaadf67c6ef212b8db0ae25ac50f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 32,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:32Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "0b20b21d1add68e8f29196108975aa3330024ecfb21dc8ed5315399e8a5f41ae",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 32,
        "signature": "f50d9b800820908b5f2afe089040d52bdd97b81e5dbde52a8476c73b740d4ed27dae6856f2915c56a2c85dea163342b3c228cc617d8d323c4436a9e9d6f5c805",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 33,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:33Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "4253d4b4e284e931f2c9a260427cfd145b8ed22659c4e6432fb601b6fef152be",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 33,
        "signature": "3f5569c53fe6ae5953b7d9bfb4fb27eead2ed5110e606dabc668a0c84543313b7cce7e138fce582ebad308571061b87f5ef32a3da542796b460e16fc38c77f04",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 34,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:34Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "908688c0091d985aa1d455dade21400b03dbe3cd0d280e636d8a1fde5d372539",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 34,
        "signature": "0ff7b9db311d32da2cf3c2bcc5bdb3ac8bad986b7395d935ee64ee84ade142825f4ba5851f502c7553d98b3bdeb0186383ad338274f734fcd80a43b593d0530c",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 35,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:35Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "db714b3ee1fff55cf0c793597c37b83a5cc0d79fa010bbda96a1d781ab19b08f",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 35,
        "signature": "f0b15f23f982fd273b36c469b0787bcd38c514fcdd877223ff274059188335fddb94a059650d6457ce5ea011f7d9b4bf1335377437c8d05b41a6afc8f64bb50f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 36,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:36Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "02fee4ba941f15fd24ee62b722a06a887ffc75f7102fed8e581d466fbb3e24c3",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 36,
        "signature": "99502814dba0f4c6804ac9efad9a2c1b8246755f5d1dd9dd551c9134d235fe3269f19c32d047152b4fade634f65c46ff3a386850b7cfd5e82e0fa92913cb3408",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 37,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:37Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "64bbbb603f542fef6cf5de88bfc4b98d194c4a26c9b5690cd4e1a8cd3b293ae5",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 37,
        "signature": "384b9739983cd2104b3af06d5174da6d56e2fe293330a223444541c0bb0a0fdcd956782bb790b393c5739eb2a4c38dc92a9b1652bbb17ca43995db231ebb9c0b",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 38,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:38Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "468a77f263603f2a8059d85c7f674645f6d329ca4c1e667a9517c87efbdafcf0",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 38,
        "signature": "af4058c5819e79f8ce1aa2e2e8368018543fa1d78b753e365a0082f0bd04927f7f9b3c4c83d492abfa4bff6d65dfaec036ed0790d29f42bc430fab251515d40e",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 39,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:39Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "2233062c94ab18121e844020e761c093c377872b02e70accb0b654a176d38414",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 39,
        "signature": "caa79f4a42b6d2c819afd8dd86aa6d82a01111b08edfa43ba3a415a887e7b0f07e2e027768a0ab7463d6fc77929bb8c64ee09b00623eec3147e9ddc79352e70d",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 40,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:40Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "12450f1b6a0610d18af04339d86f6e815bafad17be8715579370b636a50684c9",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 40,
        "signature": "53d936397893df5ce64ea2ebdf8eabfd0b7e5ef6c0b0668d78de51077a9c0ba992e2eee7b020ee75b3202c9bf9b5988451dcf512f57462a9e7b347b319364605",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 41,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:41Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "d706e5cd5ba010c18436ca491e71a9b70ef1ef576b1171f4a82bb8417de35892",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 41,
        "signature": "fd35e8a52b3dd5e55e2c97adaa72aee491c31c7b688b05c1422352c0e1d51748fe70a1f81e2ecd602a6720b677c8cb1008b4166362c1195ce1df0c0d1882a30d",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 42,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:42Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "4317d1f4acc1eeba13ae8a7fa9cff40527133f150eacacba964717dad39f0881",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 42,
        "signature": "0427735b36f48526f87a962341fe2bd062ecc7b49be4469fced4fa3354b70ee7528a01163cf66bff3cb2b43b6b38b26303464291ddfe305def43c64f28b8ac06",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 43,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:43Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "87b21bd1fbfe33b5920e225edf442466e94f79f6653e89890c5d0ed055200ea7",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 43,
        "signature": "7483e4e38d8d80e92b447d51c58c9e67c6e7b870e12af65028a1572571729e0ed24f06212019e5b27794fbd8719795bcef728d5814cbc4cf4794c63123b27905",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 44,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:44Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "d5a980da412eb309b3320825ced1f531fa05a552ee37f98fd30198e2a33fa7b9",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 44,
        "signature": "884ca7bddcf942a2d8484bebbc7b369eff7deb673b5ed82392e76583efbab541baf62c0b2f253d74222ec6192479e0caf71f2c7e8f091ab0e8f85de11d360d0c",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 45,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:45Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "75786ef1b544413324aa9eca6f34287ebe075f9f3ba71964c755d546b06559e4",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 45,
        "signature": "3690c658c048201532e7937c88234c9b356d18118daf490c23a9e7bbe032443c0850b66075fc944c7edfd659c3b84ff4fb4e5c5c31afb6dfd65b3b1a70033c06",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 46,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:46Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "1b920fa7dba0c2942a722470ebe297ad0809250de123f198157db280bde5ca5a",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 46,
        "signature": "06a89b5f96c7370a62599efc806719a03da029bb52e9a133a09b340e2d59cc1f3911e09af673c1a134b3a4133c4342c5b58c9507a771285e6d02a155c52e7d09",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 47,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:47Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "2ccda26ea4fd33eef80f4a350bd2eb4d5bed90d990d4aa853d3ba7515f6def7e",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 47,
        "signature": "a981a025c7e754c6e0261caf502dc0381fa8360b8f525253ed23ff410eef246fd43425000fc5eb5338eb090599c13d0d6f720dbb3f6d57cb7b27bdfcb8ec010c",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 48,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:48Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "dbb1a8b9bb2a1f3657f67e93a645157db504684d942d56ba113c090e4e0d2f0d",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 48,
        "signature": "32a9102521674a15f1b9faf8eb7fa639c9c62fb6694043c049c6da17e5027fd9c1f70b302078be86ef0c66a29754d5b0eedb384bdf0439453350219fda0b6c01",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 49,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:49Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "0ed1fd3b73c06131cc743b46f0ca93cde007a75d636f99e9153be5169666a3e8",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 49,
        "signature": "63baec5f5b1cb29111ed255022174e901d690a7809c01c7fa0b09d3cbd2ec4821d33a387db3f881cb54a8a7c4fccc558f88b7a0902224c996cf0206147c4a10d",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 50,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:50Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "6772cfff125b09b0c532ac6790c60fdebce94bcc5728340ea344cdd43f030856",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 50,
        "signature": "b6a3b6a069e8136b5aeec1d01cddffdef90022007fc64d093e79ba6845dbd7b725f3071106c7a968f92375e1d34a51906d5a6596c090d1c71bad025bb9ede60f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 51,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:51Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "9107f998081858974a3fe5d81c17cfd2829d6b1b234846727755b023520d0fc6",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 51,
        "signature": "c5aaa761201185d2ef13039f1bb3e641444177964e836f55156431c03b39ef88bde15fc9913f6f00b2973d02b880c4f7b456dcfa9705b1b8324c03d65332af0b",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 52,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:52Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "ded7b5f49fde96e29c50915fce1c708e9dedcf257aa230ac6d8fa982dfef58d7",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 52,
        "signature": "186466ab1ad2ff9c640c3818797208a6020fdd4604c0595a507938942b80ceaedcc5f207139425f726c70458bc4b82df79404fd5d67e568b45dc36d42bd8d909",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 53,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:53Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "caee283bb627c96bd1f73ef12d7236464b856eccbb68e94479533051dcdb848b",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 53,
        "signature": "83dea141c4f54c4de981e022d5fdca6b300f6d4bb31587f186babab21632b07b8b7232ddeadebf66b2e3a4b2471382bc56cab057ee6141964abd4d1ff866bc0a",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 54,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:54Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "9f89f01a019ebe186b66004dc85bc79db574db6c015e505bd0daa3955a9a542e",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 54,
        "signature": "567456376cecdc5bfd76bcb5efb987ed25568e995b384f273fdfcc8b9443dc4b5db4ae5b8848afd53c83e4ce433d906e3441e2ff249c13ab3a58c24871017b0f",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 55,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:55Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "c58d0bd4a423e8a9587a2d1173ae04751f4b357b6a292bf58279515d55fbc3ae",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 55,
        "signature": "0cc7d85c9d3d324823772aaef4ba72e967c37eb9d38ea5b8d27c60422be1b4bba8c58e69b51fb0449a248d3bf4849db68f009dbe7ab5b999c73de9105e8c9200",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 56,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:56Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "421f2c1e9ef1608ce468d5a9464707e8ca8faee1f3cd265ea31505731312600b",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 56,
        "signature": "390ff40f10e02ad8cb6b7ab84bc254b96a95b8b5968e43ecfb16be87229bc806e3fbfab8441228872beda6d24d35e05f1e028b6cbb280d8b538d8a7b600ea40e",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 57,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:57Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "b3086568526c1c24ad45681b36515846d0467f9606fdd9a538e4c7ce71304ecd",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 57,
        "signature": "7b62f4c6ce3d0af219396e3dbac574ae559c5c30a01e8ec501b035e47ce920ff8cb6b45fe29d60c9aee74e8cfb319ce24ece8841ed1260c3459069392b32e70b",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 58,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:58Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "080709336f7d3ffc2a377f65ddcf8c32790ecac8948ab08bf8d1ec826c619771",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 58,
        "signature": "2532c2def135fd6fa5b43a1c5e5cb43255556d0b9d7d7695cba79405146c64353617fe4db50bcc9bff44222cbe3e14248364ade1ad51f2b71ffb27f2f8cd5c02",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 59,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:05:59Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "924208b07e2bcd5d9bd5e00358a4e19f1e1ded35d45de7b29d98a62b686a1755",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 59,
        "signature": "800bebacfefc0660578e0d6cb0238ad8b695e87fd2ed6960b35a9dd57ae4ebef2d6444b8e6398386d7635158176f8d68a0ff46556878e56261a9e2f1081e0902",
        "universe_id": "u.r4b.phaseb-injections"
      },
      {
        "commitment_id": "R4-B-run-v08-001",
        "component": "R4-B",
        "event": {
          "event_type": "qualifying",
          "idx": 60,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:00Z",
        "pre_run_commitment_sha256": "acf026ed5d229f362d33cdc928d81591f0cf4ca90d183b60cadaa13eae2f3e67",
        "previous_chain_hash": "4c1af0047f3cb837fc894463895161c697d7cab477f42cd09f8c69706e7ecb90",
        "protocol_version": "0.8",
        "run_id": "run-R4-B-v08-001",
        "sequence": 60,
        "signature": "40f3cd8a1c145de1e34f09de467718ecb6dced8e55af165b8faf84666d8a1d4bd65f0f8148f44bf7c986cd99d87977764c34da66abc3969e7e96e5568e457b0c",
        "universe_id": "u.r4b.phaseb-injections"
      }
    ],
    "R6-B-run-v08-001": [
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 1,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:01Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "9c0809133c8e94e4bd678a38377e7017fdde059e49602878de9bbb6a6a8b2d92",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 1,
        "signature": "dfe8a1c492b11043f9343cd9ae695fda3e05903af6f8bdd032faa7e49407588b7acac8e32566965be40d34fa30374635f9b3c9d23969593ab0e988058c1f760c",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 2,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:02Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "d3d30aa39385bbcfa4cb3094549de1bb0ca94d1a521903e815593c32941c9e1d",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 2,
        "signature": "59aeb066d6ee5ee54faf4ade586283b3ba154df3f353f697a33116d31630bd6b10e8370764f47fe8d6e77125865c7d80c5616636c382b6a243547073b123dd09",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 3,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:03Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "7c9ce8cf814a469ee0a0ba2f6efab787abf9c41226be641d3da7f77985db22a6",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 3,
        "signature": "cd2aa3cb9faaff56590041e8af0cbd9965a07f052ee67b11a935800aab1a085e510d5156818414dd27dd5c684576035a9fc8406d59bd26e015fbef1e7bf1dc0b",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 4,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:04Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "23f51bc9fee470ddea2e5c192ac690e6b28edaccc6aef314384f24a3a40956d8",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 4,
        "signature": "754a2de0f95f704a9a24fe883865ce5fbaa71e617613ebf915f52bf04702e88014a9e438d564fefb6998c1bbf649e47377f2aafa2f7b3fdd334d24ddac850309",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 5,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:05Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "8ed00c369b2b5bcd4afa3ffc5983f49f01eef14087399565d0b4c4e041196249",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 5,
        "signature": "992432898991b292081f6473dc2046b2e317585088edca258038db88b0d9970265da9bb1711a25e380bbf991af69e78dc97f2206dd73e3874ed91d25fdffee05",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 6,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:06Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "3d44d6ed0cd0d1a9084e89b012fc0b073c0663cf5820a39b773b04906e38d95f",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 6,
        "signature": "0d134d41d47846e053c80617cbad12567cb8e1c9eafa4f2ddb32ab8bf460f9779326b0e5a8fcffa1f15a3d68c6840935389fd369ea3af644047075c0d990d700",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 7,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:07Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "a9427df5b4c2630adb5ea1f29812380494c8f8a770e82e3f5c83d06dddfe7137",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 7,
        "signature": "7946a381fc071cdf97b9ded29af6d2655217252ba7306371b0aa6d564f548c8eaf97e40a55747c8a4527654fb09d2c2ca4526ff67bdc5813e1810d51ec9db605",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 8,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:08Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "e28963085e6be9a4cc23642f6a04d5dd3d632e4d153b9011453092238a97ba9b",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 8,
        "signature": "447c567e8952e69285b1ec3c50d3504a223e420f4f5def82a4bd496c032338be2e6b9e9376c5807426b9f0bf1b27e1b07446b9dd23688394ae6599e5a6eabc07",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 9,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:09Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "3e634c10bcb72497ad1c555396487afee838487c745c212a03341afbaface29c",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 9,
        "signature": "29924383c602989175bdd3a804307054d485797bfd94d3f64bc8e39baeb585c9863e32b48bb6c1cea5ca02dcbade4984aa7ee5dc5c26d6598b1c2fd85ee50b07",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 10,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:10Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "802f52b43a62a6ea9f6a7d1253f86f7491f0f783aeb8253202ef2092023e3423",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 10,
        "signature": "c50833f315ca2dd8d0b941a4cf2736c3322126302d23c42c89099e538c28d0ca6320fb1dbf2bd108f57f35cb1166011689752ead32292c8de99a0ea0de7aeb0c",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 11,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:11Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "f334550751ea9556c315ca873bc76bda52d27c2900fab714e57b9d2238b63f92",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 11,
        "signature": "e68411a2c089e4f401755b2f9ed5d224154bf05823ae3a2b072bdc6dd33cb64756d500250617415ed5375db4878f09a52bfebb40b40f919479dce91586ed020d",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 12,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:12Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "2a3040754f6281ac55c013b93121f19f226988e07716ce7718b86f8329da1748",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 12,
        "signature": "1c4e81c1d63acfa0a13d33dcbb2294ed2dbd673412af7cf29eb4b0e2bdc8f726b8e1c4bceb45d8ae4427a6984d1a0117ac158e63113bd0b1a4ee995bddf8f50f",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 13,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:13Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "30f2a078fccaeb226e060614d232452f18fc3390980ff6e8cc13281b6137d17d",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 13,
        "signature": "f33296b83f406b0d0bb9fbcda7a46b9d4171986bd365e8646042d9774fab5ee6743b5d05c8953de8da69a4fdc005609d270cdc1aa8f783bb78d511cdc276a904",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 14,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:14Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "b5c503c40945276e93ce55e5d1a22a5d9e6641ff9dd61537265f5f010a15812b",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 14,
        "signature": "59a92f1aeb9f563fb063a5859bde79963ed64eabbab36aefa41da239ca8e976839f50cc66f6aeab29f2ec1124de0738fb09300b9bc5a71596c631e94e0595d0d",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 15,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:15Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "0121092a3a27180e87971de02725807f5994630a7172c359b67f70cc2d0cd5fc",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 15,
        "signature": "f2d277179dd8b124fb99587a604232953800b06e0b7daa42c9cb8fed6c360b82f34bbd0b31a545fd99ec8a68bb8610fd874a61b0cd014eefe35b6a393c9c8e0a",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 16,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:16Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "2e70994a0b101f3a406d6a2f19a31701307a81be7fafae088bb3341d1b9a0d36",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 16,
        "signature": "982f6a726bb46cfacbaf06ea336664b89b6159d2579474496ab6aa4618e28d1e06cecd32ca15e1c39e66c9be978c9dd0720d92adecc64b05841cac33f234740d",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 17,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:17Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "608bef119e884064dd5b4d902e971a24053875e408c73207d4af645d66ff2742",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 17,
        "signature": "154eba4064e7f3f228adacd10e3a93f675638eb70123208d6e7415cb1f7394b2b510364cb6495751cca015f9337c13862a135e0b9d84f04f20593c28a251c304",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 18,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:18Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "3c2725d6327549f38cd470d91427753e8b16c7ac76c1e8ed5927a85ecb90d7d4",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 18,
        "signature": "7825afa6d493327b99b98e5d0d64432a2a3eee7c13062946491e0fdf2bcb7cd94a3779c93a7f8558ba8efa86f0bf05e4492a0d31f124f3b807324ddbe210db0f",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 19,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:19Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "eef7fef2129a97213cdac009f07e14ac45e2967562c5cb23ce288efce7960453",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 19,
        "signature": "5673f217da5e3bfcd8ad610c1def25a4db4b0c51997ba0821c5b44c0b6b221f64082eee9ec477f44cd2fa46c36ac69f449923c9979828d321ce6b75b2318560a",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 20,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:20Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "073d5982fd68b3d18e550e6ac2fe231c41d175e43b9cc73454f1e0ce3771a29b",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 20,
        "signature": "2620cd0c1af82006c6520c199b33d2e7a50c7579433d68006223a9e33a7e4beff14ae244244025656005c764e58be52a91903611035b9460372215288171e503",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 21,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:21Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "b5207306e5bff639d0349a98b1484641b6c3d426f1c80cdeb0a56ea3d8221a66",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 21,
        "signature": "976f5e901222854d8c853818791ac7fffdb0f1268fcd27446c3cb2fa0dfabb5be539e1acfa6b40a2c9ce93deacae5c9dd5edf3b912f0838b9b84a2e9b6ef220f",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 22,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:22Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "1217be0e75a12dcad0d8ebc128e415b4efedde9004e048a7f7cad9d486df2ee8",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 22,
        "signature": "e266f9d6a79e9accb4a4f9839c9ee4d805c87502d080f6411b3d732e252c734550a7c25f5f28bb093cdfccde8cf062eee40178e2ff4443f10f91ed02fd92e008",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 23,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:23Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "c9d579164b91671c00a7a88462f3b699cd82e989b1b85d3458f1c8ad23811b2b",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 23,
        "signature": "1aba4caf3bc93915126769bb8df8b9db869cb112c300183a15daefaa36f9d94f348bc3b1bffa1123938e66502ccbae8f48e6ad653dff02d7aa723270fbacb40b",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 24,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:24Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "3eb443a9c1892897d3661fc5b94b9da92b50ba344040e2fb56d5bb5adb63afe6",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 24,
        "signature": "8b9939acfb0e091ee1c73575eb06d0376b59a9e9e7be9c1f127ea88d129539abfd3de209ddd1ece31b5906c42eddde55428df09ae762b074122c660d93951907",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 25,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:25Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "6f73cd5f4b2d45091eb3889cb792deccd53da9ba462d5ec25e154d3aa57e87cd",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 25,
        "signature": "b0b2a35f6e8abe73164ff7b7790f3872d1aa78d77bedb012a744f543543000f0b49ba0b158034e24ccce15f216446c3bcbbaa981f44a887cdcbf6d99ca1ca207",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 26,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:26Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "869d5c70c95ebab15f86db72f60bdf751e2d163fe940c702bb94ef35cfb79929",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 26,
        "signature": "59b60a9b63bd8226550b04cbb4e65ec84fc95cd97503b359117434cc99a5b3f4d0a7dd3c06eccb5ac8f22aca23bd3aea2fcaa9502ad909502718bf1f0cfc6902",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 27,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:27Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "7ab25dce0a1f9d8be97e3d052614a2a9c8d6c41d94edbfd9ccde336672f86320",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 27,
        "signature": "d9d4965243ce40eb433e2a4dd67122f96d3bdad5315585ec606ced706a0e3c1e9085dfe1b6533ac6f0d407d3b400fb2d857cbc6722174ac9128017697bacfa09",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 28,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:28Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "329177f71401fddcfafa429f584e073875a565f836d91a5f975873b23874920c",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 28,
        "signature": "ff6c064820ec37da3a441233318483b1fb51075787e7a889b24059ea2b163c5e0d5998c109fdecda038263e7c47f4d853c56cce5bb6807051f029f8d4199e308",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 29,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:29Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "146a841d9c66c0ec6b76b7706b9129dbdbf1ffef3fc9fa811bc6a668d1c7ad89",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 29,
        "signature": "30d6ee229d13df2e4929c5e3bbe13c8d6067e74b9ea9cea6e1f031700409b4600738f8f49dfa01d13c41bdd3dac0d88dd054ba1497afd361436bb17a197bcc05",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 30,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:30Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "9a82f9e8dfbaf557f43f5ea6b30070a3d0a5374e4693eb04207f8e23aa94a263",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 30,
        "signature": "cbd943705f1cf8b8d5f353e20819ebbdee260f921832f03a1910bb65fdfb7e3c88b4572fa140c7e58a25ceb4b3a6768011e6a66acefa10253b9b98c388594200",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 31,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:31Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "a4844faef5962cce1de8a873dec627c94fac879df697850fdc02773c877af5b8",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 31,
        "signature": "57de89d7f387253944b85f9ce7ea4e4b0f2df423c7bdb646c23daf693f845da73f54998a957429ae724dbcfa55e29dead376465914d734b23888635630bdf808",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 32,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:32Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "a21d442185bcf63c207ee87570e71b3f0473605fb290ffac2c1574a9a4deb854",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 32,
        "signature": "167c3a016d1cd335e364ec9ce7f682be7bc04689d7d1c03b3194ab9661ca85321df2bf9b5bf4bbeb91d9010bdd728e706fb256f4038f1db770e72ae97ed79a0c",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 33,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:33Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "e46e08434ae0bde8bb6684bbc8324531a6bd21c480b902f915d99a0deccaa940",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 33,
        "signature": "189475dde0e78d37614fc4158e311a68ec0754fbd6d7b2c219df102b68d914c1a711fd9e5338b467fd9acbb5f2a93f4c04b4cec3926a18bb3471e35ddc3adb09",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 34,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:34Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "c0da91ab2cf36009d2e7355d0627840867c03902dd897483705e5a9a825e4bfb",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 34,
        "signature": "4301c3a077d3f6374a22ec5295df97b328ac47b64c717aafde7771ce416bea152c2d2ee9d5d2145c96ea4b78539d468f014fcfa0c34bcd05a0039526ceada80d",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 35,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:35Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "c920ee92eeb0faef6ce9224c7cc47a25fa2d030311fda340ff2268ae4e4afe92",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 35,
        "signature": "07fd04f6db9eca3e406581f0dc5b4c7c4d018204a34e88423e3c5428dc20834f0a1a490898c4a0f303ab5df67244fcbe2d1e9231b063421e5c4a168cf8532c06",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 36,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:36Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "265708b0373f502b3718c60c73fb43d853c41baebbf25fee51d07fba0af366fb",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 36,
        "signature": "ee5626ba7d2388595ad561ca5cbe469729c8c62531c15cae81b2c25bfc8d928df10eb25792298b9287e85a989113cee7f0160bd084e3f01d17cfaca947a4af0b",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 37,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:37Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "a7ab6690a3b577f1740cd6a6278d8ccb3a3f99e953c676abaa1cc1976e7f3ff3",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 37,
        "signature": "b16d1b51510df9cae5d52c8333a340c5a18475cc0f21cda45e98b41fde6781444b457b391f8bc37d10ed4f9d5864f5db97370dc1815714524c1427717c105301",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 38,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:38Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "e63ad29a98e62dded6f0156ac4b094638dcbaf4e311273ade2bdf6353a5d40b1",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 38,
        "signature": "8d558c3f862ee4cc3ffcdf3c4447078dbcf5cf55091089ddfed9074f12aa6f2bdc2dde8cd4426b82d151069987cf65aaab52682d6382acac993c3ceb71572c00",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 39,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:39Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "bb5b1b406fa4c416001f84df3871357ec2f644a59d8e50e24258568254a37666",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 39,
        "signature": "8cac435e42e7dbf98f34c28db399c4e623ca1e0e21f20470b7bb4f001290285cd87d092b48c940fe4b887c957216f53fe81f0a467643cd2a64fd5bb9bda98b00",
        "universe_id": "u.r6b.receipts-run"
      },
      {
        "commitment_id": "R6-B-run-v08-001",
        "component": "R6-B",
        "event": {
          "event_type": "qualifying",
          "idx": 40,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:06:40Z",
        "pre_run_commitment_sha256": "06c53fc4ddf22285a313eda403a0b6339c501ee98f6edc614a41026c91e2a7dc",
        "previous_chain_hash": "18de6b6a20a2f6666c91f8353a4612f8466c459e63a9c793a1184e198932f749",
        "protocol_version": "0.8",
        "run_id": "run-R6-B-v08-001",
        "sequence": 40,
        "signature": "1c0ab1a55ef380812f9e84461e3e1682eebc24b8840481dd6d755febb8b29e3bd696ba4112ad4493066ea4e66b1d7168c5dc5ac658cc91e945d213e379c0d004",
        "universe_id": "u.r6b.receipts-run"
      }
    ],
    "R6-C-run-v08-001": [
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 1,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:01Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "8c6364f521a1767ef399e22607379a68b0607c8c9c4125c026c7e1073a40d4dd",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 1,
        "signature": "ce490d2f1b34a66c1931f11cebf8d139a828f5bb7c1b74be9d3fdd74fe5fda437c99c057eecced53ce17c0f066328ed992c7c6fb51f8090f8d1c40b06a89c400",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 2,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:02Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "71a9a721d55faff007b46d8c82228a1f5f7dab62d24459d76fe500b54153f49a",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 2,
        "signature": "786d5d24b9f43ae9dd7342ff00a6783351a34025aff87c9c27201431c5ae9aa315a7525cfee44523d2c55670e8c9400a8c31cab265921e193d21283f51438202",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 3,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:03Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "8081c640a9d298afc2b3969ad28c28f2e7b321cd3e31b54b1d46c93e835502a6",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 3,
        "signature": "ba3b7abcb5ab1589a420cb5530fdcd4e00247c75b61ff9fdb8ccaa263f2c2f3cfd0610ae4b4e997c44ba3120469e112fd1c8ead5e88719d4efe02ff444263005",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 4,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:04Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "4a0e51811ce63c95c5bd84187ad181d0f3a8183eaf6730678b9447b7c8e862f0",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 4,
        "signature": "8c88d9f017bda281d6beffc4390d586ab71a13ad6e0b81541ee84cb6148f5b98f86365e6784e51f6d8fa07eca52127b24e17672a554c58989a1593cf48b85d09",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 5,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:05Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "23c81b1fe97e03c9e93816652cce2e74dbeb724ac693b3e492fdf1c808bbc044",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 5,
        "signature": "f4550b4851b7d758fa2076409d89ec4f7fe75d3ffc7f3cddf89e28a17134c9fbab1e40cc2dedd0225064f8f266a9cd4cea435e6b4d42a762f97e9eb45ceca607",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 6,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:06Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "7b4339367e88c287b70523124ffcfe882c2af9b9b488a0966daff756a47d7faa",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 6,
        "signature": "23720a48a096d8cb06996904b6f6449354166ec61c3dfbf5d4489116d83a34430bb0e43636c1d8b472aed73a1948cf5fb2266d9ad76a6a165f8171aef961aa02",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 7,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:07Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "30166f4fce2a5a7fd68595408cd0c681c6a81b2894e94306e8a14e2ed32dc3da",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 7,
        "signature": "0a7e27e62b3069caa2182ba682f361796f7a9dfd199aee797dbed19ae9113b804ffb09029afffa0ca65ca52ac07075342d887b1940d5ea018f9a62450c7a3d09",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 8,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:08Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "3e19196a1e16d2b5001dc84962b08d56d58fbbb3d2ef296026bf135302478ca2",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 8,
        "signature": "7df95ab721fbaa4a6c2d623a6a27fb8d22c9637692cf741fa657ecf14d47f643d5e220c5750d034d7f86a8ff7db69018156c7153e663e526c06344ec6bb1130f",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 9,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:09Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "2787b0a1dfafbfc97eb0a5c531f6dd76eef2a35c1dc233f8761d72f1768dbef5",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 9,
        "signature": "b63b0b9df4ac712c7a845d406b5b153d9941431f34cb2cbdf13b82f4d7fc629e886d363f1645f23e552bd7037b53b363ce6adb79a799b22eb1322385d1563208",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 10,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:10Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "784718042dbab26937bf494f98e98d00fc23ad34222f4ff6d82508ca5be043bf",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 10,
        "signature": "672d90ee61b96ee1a12cbab5df3d367ed3dc75fc95e0f64739898e6ced240a14890e46162b6e3f371c6f6bb8306610ac8d322b657f77e6ee3c337f0ba68fa501",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 11,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:11Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "e49c5513b4d877d0f46551749ec2d4cf33ccc51767cc86170bbba002c94bea42",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 11,
        "signature": "c5714ab27ec66b88d5ba88670222e79530dbf287c97f34b6851c90c3fd2f22eac16e0aadbacf27980bf41239bcfd66b7a3874e5b8257fce06cbddc9370607f05",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 12,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:12Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "3bcff4b0dcff319927e3f4b76b3a8d64d0cc71c549d0de3aa810c097871f6210",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 12,
        "signature": "9eaf80e0648444523e42dba26e28b2a5a49e54dd3835940ac4d73046c4af5ca4a4185e49e88a7a915bc7188d036caf298f037808c89230374d29a6245b85af00",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 13,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:13Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "3da64ed912cbb5c8bb44339c3171fc8be37ca5485604a5e1e760b24406a6757d",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 13,
        "signature": "a08a1563df452ecb6fb14c48ae5b1ec1ac4c2d0937a98b20783bd79ffea0178036d6cbc87b4d64dddc92e8c3c17687cda888ea0cba8657deb7695e1dfd20570b",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 14,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:14Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "a8799497c67d2152c45a84c7d3f9aa749425d4cf86007fd4b6de447c900ee5a6",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 14,
        "signature": "2ea823c0f0150a66ed9eb9b44c66c8015fb15d35a58d564964866b760fcc5f2eba95a4613cc0f3bdbc622f8992fb6b951978c2eeb77bee6d92c75e9a52df1702",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 15,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:15Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "9a4aff00c7bf60580d98479f9337d10362b0b13bb3af77ba8434c12b492ab5d2",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 15,
        "signature": "44200ee05dcace1b4269d96c02f9cc9c23ec34736c984513439d23980f2ffb5061ddbb24774feaf1105baf6956a7cb5f929fa64414276fde9528f5d773aef70f",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 16,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:16Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "f8ef482e1e6109f2771fbc98b2b0a34467d153a9e9776ac0fc2fcbef95600268",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 16,
        "signature": "02b159777bff57c65d156ed2ff79f3dfc82e8f1a611d66910ebe40da6f151c71d173c31cc7d92f586ce72dc74ca6d1fed36afbc0e835294cb9f0a200adedc60a",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 17,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:17Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "2955c5c54b65adbd0c1eb664aef24436e5306d1c331334fb42124460ce4da8c3",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 17,
        "signature": "36b37dd6fe1f932e70d08c15aadf771b79095f0bbdeac22db14634bd3636407b9e8606644933d5db84192b5c4652731facfc617c40968dc9b84e563fad53bb0d",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 18,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:18Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "35995244f3c537ff4ffc3f91a0b0898e0223c74953c016026223777e69c95210",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 18,
        "signature": "55df615b4f6b3c04f4fb59fd84e7922211a0caab743a1e6f4e722c243a52d6ed3c4d2ddc54adc7960d848cb655d69196ceaac3ab08143d524a16658712bc4707",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 19,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:19Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "f522b74317642ffa61325eb3dacb5e54746850804eab47d48703f5c314d7fc6c",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 19,
        "signature": "bd90fa6f8624380b46131ee67dfd4895b21e14cb2871d5ec142b5f60913f465b012698b27e25515bfe3e800b6ecc2a18ff2745030b26b6ed05c4bb8f4fab180b",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 20,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:20Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "7bb7598048737756e6139ab51b94dd66bf066dcc6a3ee988ac1087f69caf430e",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 20,
        "signature": "7d726a51d9231b83960538f89d10aae0c9a3d8b4a14b5a2f3783e6d21afab67e5805078563062f532345fe3e277065f298ae3f9cea5022b9650400b66b3c6b0a",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 21,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:21Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "cd4f5525cad7a64e0c4732e237286db8174807156b854211558781b9212db9e6",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 21,
        "signature": "d6e64ee1679f69683426aff394c412555bcd56ea804c0ae781f65d4a579588eb6b922a63a86ff194053d9c93f1c229f2a8ade3e9f9bd656d0cabd43d9738440b",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 22,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:22Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "6f144b27daaedb6154d185e761f4407f4d4ad7ebbd423fe3a67c90af8b6d2e15",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 22,
        "signature": "de8db3268f2e163faf3e31f9052268a3f117c1f64a5164e73e6f02b4f7612f2c2731f997d7e9a048c74f6ef3630a5876efe9a05d2c7f666722c875094d3e4a06",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 23,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:23Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "0ea16373ad95edb720e4e41bfb288f09b398e4afc700569de4bd190c6c8b2193",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 23,
        "signature": "4d64f3b45f0488bec55321864147282a0c64c20638d042690de94b985b30d579e169db662bd9f1fd1738dcac089a9f38b99452ca7c01d8a93d8da7a57bace401",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 24,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:24Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "e0d9eaeb18419561fa90bcdfc60b0974a9cc59b08e3ed73686784407f3c823bb",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 24,
        "signature": "bd5741b7c50ea8c9e1881a4631d85099c022210f03a4413b94f04ffee8c8e264aac53514110f81c012d4cc5779ef7cbca79023fc4e577404d501414227fc9f0b",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 25,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:25Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "311df31ad4cf9274ee07ab16a6d9b3f1642da76bd6ed1e53a24c9b8335f8db5c",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 25,
        "signature": "6c78f31bfb4ab06812e5947ecf732715195e7cda8b57d9394bb0835f09445a315cb5668fa76be0eaea96bb2c434153c017e10910a124e0139a2ff516e9af890a",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 26,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:26Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "053df3da729e57463722cd113ace88bdc05acd7b3d86edddd3c2ad1f27c8dda7",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 26,
        "signature": "3ac605e1fdb522fb2b3f933716d091c526318293049d33184c8f420886aeeea7c749460c6d7384f8f2e29da178e9bf904740333972479b873a1868cd2e97270e",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 27,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:27Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "5c53e6402566f8e82d02490db3f58df5c8e4b4bd98e5cdb045c1022385211138",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 27,
        "signature": "fc759234ba30a6a3f25a333944c714003d4b7754f4b05e126270b567a197361de2cd1cbcde5635cae930f4ab362608f71c3f0a41091727df248e8b1018eb350d",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 28,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:28Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "3f4359b4c2308807eb573d74cb8fd63ca581df540a29511027e08b20832c288c",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 28,
        "signature": "00ea44def2c4a23bcd69c0f64bcc911a627500b6d7aeb100fff053bebf7dea4d0fd7a507be418f1370ba3654cc207a5081484b4959b546606c899c7afe004403",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 29,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:29Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "7c2e265b3d1e4eab4d2ab994b864cb0329e8253313b5c1e6f41225048d965a44",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 29,
        "signature": "8b82e082c42e73fb11c97f5dbff51473489eda0bb4a058f3f536d45833a211db4f08f4b2caa16b934f873384813f1ee51c6d4d1e529d4fe5f3baf797e3da5206",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 30,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:30Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "26f6db87a44758e910c51b91781a366236cc349b77de4b813e3b474159590b12",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 30,
        "signature": "0c1696621e8c2f9ab9c32452c4c75302e038325a95d16cad1e288467e0216c4ce89092afea6015f331a460cead356dcdce5c87c7fd5e0180528803d707813506",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 31,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:31Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "9fbad9df7d817c820cd38823ee00ba210a3b899737dbedb8c4f8b254d83c97c4",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 31,
        "signature": "323ec19ec943b236931e68e889e599f9da0ab6eab67cda995732ff6b40028f28a46b7c55de251b64c323698464efedeea727459d40a87d7bd9ae3ee547657907",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 32,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:32Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "0cf51fa9880124f47770656f2d940b37dc12a402b8ca07f450d546455f989aa1",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 32,
        "signature": "c329d0b79612a764a997a06e90a1b174082e94ba0a5b220b97cd69285fc6fa0baf8cf6168ed710656a19e2e755e5c3825e94e3da8d8c01b05c9bbeb5316cc905",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 33,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:33Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "ca151d726454c108f438a0f3e578b0d589b0b962a2c5a4300f8a45add829cd37",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 33,
        "signature": "c4d58a0ccab91e85b038ac5e15a9dea0f2db22ab9978ae973c1cf4b966404382450eaa733b09fce50a7b7f1f2109f4c00e310c3331236d4d02cbfb68ec2bde0c",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 34,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:34Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "d282a82aa955659070884459368f3dea6ad37896306c091c26172b16a9f47c36",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 34,
        "signature": "84dbc15140837e06eb0d46ef7cb2f42fbdc1c7f282beffbb33badc997800f22fc54a8b471734e9baa960cc0120b8431a29b822f25199eef37ca62aa2bcac5101",
        "universe_id": "u.r6c.receipts-synth"
      },
      {
        "commitment_id": "R6-C-run-v08-001",
        "component": "R6-C",
        "event": {
          "event_type": "qualifying",
          "idx": 35,
          "qualifying": true
        },
        "manifest_sha256": "2c31c72f0c9b9ce8a9cd685be9aca39916a8dd7c7a6d5a107b7309cb71d9f7b8",
        "observed_at": "2026-07-24T17:07:35Z",
        "pre_run_commitment_sha256": "9875a3863bd9fec5534fdc2d72ce481135a3c622e3838581320b08cf903d1201",
        "previous_chain_hash": "5b6ddd0002e05faa5172c2a8596e3f90f2c5ca506014c0d12fcccc41ffc1507d",
        "protocol_version": "0.8",
        "run_id": "run-R6-C-v08-001",
        "sequence": 35,
        "signature": "fef80cda95741b213b95219803806c332ba2a7a5f46fff3fbbf1408ad2a16b31e30a5942eb84d7462fe2d7d74874523d31fd3052076a411e67fa8e24996f5e04",
        "universe_id": "u.r6c.receipts-synth"
      }
    ]
  },
  "sealed_n": {
    "R1-A": 8,
    "R5-A": 25,
    "R5-C": 9
  }
}

---

# Bismillah ir-Rahman ir-Rahim
