# Bismillah ir-Rahman ir-Rahim

# R0386 -- shvvp_v0_8_signed_test_vectors.json.txt

**Chronological Index:** 129 of 995  
**Date:** 2026  
**Section:** V. BSSG & SHVVP Protocols  
**Source File:** shvvp_v0_8_signed_test_vectors.json.txt  
**Source Format:** txt  
**SHA-256:** `cb9434176554c12a46820a146c7af214efeb2f26f30f02616aede317f3814926`  

---

## R0386 · shvvp_v0_8_signed_test_vectors.json.txt

- section: V. BSSG & SHVVP Protocols
- source_file: shvvp_v0_8_signed_test_vectors.json.txt
- source_format: txt
- text_sha256: cb9434176554c12a46820a146c7af214efeb2f26f30f02616aede317f3814926

{
 "artifact": "SHVVP v0.8 signed test vectors",
 "note": "Private keys were generated in-memory for fixture creation and are NOT shipped. All bundles verify against the three frozen manifest keys.",
 "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
 "public_keys": {
  "commitment": "31e1aaae5943c2bdf042b3a1e02b8a3fe31e6b352d1d3d9aaceb8ae355605cbe",
  "logger": "5b9ea09f768cc70f761ea52883075ea2fd8ca40f5136095ce21b03ed91266302",
  "anchor": "4f94342335b65b52029a03119a3fd0d5673853f352d5244d9f00452c00f845e5"
 },
 "sealed_n": {
  "R1-A": 8,
  "R5-A": 25,
  "R5-C": 9
 },
 "realized_n": {
  "R2-B": 100,
  "R4-B": 60,
  "R6-B": 40,
  "R6-C": 35
 },
 "commitments": {
  "cid.R1-A.sealed": {
   "kind": "SEALED",
   "commitment_id": "cid.R1-A.sealed",
   "commitment": {
    "kind": "SEALED",
    "commitment_id": "cid.R1-A.sealed",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R1-A",
    "universe_id": "u.r1a.sealed-ledger",
    "sealed_universe_n": 8,
    "sealed_universe_inventory_hash": "193de08501ac19900d223e940606668c09edea11b1ed2a5a523d3d5c7c54639d",
    "authority": "sealing custodian",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "signature": "cb956ce40c211a3195a07d0ebaa73df3593aa79be2a0011668478cb0fba9ef86c0677cc8029fbd116ae7f673b4c3dfd6d4216974d54ff4571975e31f309eee09"
   },
   "anchor": {
    "anchor_id": "anc.R1-A.sealed",
    "commitment_id": "cid.R1-A.sealed",
    "sealed_commitment_sha256": "3ede3b021c177181c6be3d76683fccff4ed69adc10b12547ad1fa4cd8992d2d8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "6ee3dcdbec01af1b6c42decc6e8df70c1217010cb37488ff9677d5778bfeea4820d6d9fe34209a744d1fec8514a74552e4310ecd0ef57d41e90f3b5c0cf1e10f"
   }
  },
  "cid.R5-A.sealed": {
   "kind": "SEALED",
   "commitment_id": "cid.R5-A.sealed",
   "commitment": {
    "kind": "SEALED",
    "commitment_id": "cid.R5-A.sealed",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R5-A",
    "universe_id": "u.r5a.descendant-universe",
    "sealed_universe_n": 25,
    "sealed_universe_inventory_hash": "883bbd92f72f08cff8bd295d998e828d115d46ae78ef7f314c5c9fa2f1df82da",
    "authority": "sealing custodian",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "signature": "e1379b0e4a80c6b087b336922130f24bdc1a602d11538f2bc9e2e6e214e80ab4ff41ae175a7550e034a66d10836726e7a8de4dbc9dc44beda72a4eb45e437b05"
   },
   "anchor": {
    "anchor_id": "anc.R5-A.sealed",
    "commitment_id": "cid.R5-A.sealed",
    "sealed_commitment_sha256": "3179133f10bab851947d49ac04c681ddd2311a20c53d6ad05fa2882d800888bb",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "b119f048337c2e73334682c2236c4b16d95052ba4deab5133766882d4d418c70a6db00135b0821fe2b867b2d5108a0c06358c995f365a3d0d9ec061a7cb5ae0a"
   }
  },
  "cid.R5-C.sealed": {
   "kind": "SEALED",
   "commitment_id": "cid.R5-C.sealed",
   "commitment": {
    "kind": "SEALED",
    "commitment_id": "cid.R5-C.sealed",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R5-C",
    "universe_id": "u.r5c.revised-descendants",
    "sealed_universe_n": 9,
    "sealed_universe_inventory_hash": "a18497c53b6febe304bdd222403b4923a5cdc3c213f48220cb9a7990009b3785",
    "authority": "sealing custodian",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "signature": "ef9543d652215ea8765961950b0c4fa997bbf04b5651ee8c0c6a4402c457b930d5663d0cf49c0ad441e6c66719e3ca9a789ebd8e1bfbc62ae222d48992329601"
   },
   "anchor": {
    "anchor_id": "anc.R5-C.sealed",
    "commitment_id": "cid.R5-C.sealed",
    "sealed_commitment_sha256": "89559b02a85fbd882262573305d6dfd9c0d2d5f45991fce853be4c69b095d472",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "2d236f6dd6fc5e61ebc78b953c39f2d3c791d46d7b1f04d7f5e83979ff194fe12ccce6abdfd23dbb8d3d29bae824fc89431d7a59854b0aeb730a90b26624ad0e"
   }
  },
  "cid.R2-B.realized": {
   "kind": "REALIZED",
   "commitment_id": "cid.R2-B.realized",
   "pre_run": {
    "commitment_id": "cid.R2-B.realized",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "event_schema_sha256": "4238a8dd86f53ce5b0bfdc15adc1eadf68a984d754e5cdbb5c9ad07bbf5aed6d",
    "inclusion_rule_sha256": "7643809c3d8467420fd87fc4e40a0804df234990264abb923a60e5df18ececde",
    "logger_pubkey": "5b9ea09f768cc70f761ea52883075ea2fd8ca40f5136095ce21b03ed91266302",
    "authority": "run authority",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "genesis_hash": "5c1af7c61b1a8ed7f0d09a87465ce6b221e4e310cebb2b685deb2dae0f597806",
    "signature": "450af222059057393001fd92967073ae79a5b77d5c488b6e850a884c50eb752dae1fbe7991049931032297d53c78e56963120a234c777c468e80c929cb993703"
   },
   "anchor": {
    "anchor_id": "anc.R2-B.realized",
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "dcd566c105abedba6f69c79903e8ed3fa4b54f24f711e0a34699dd164b5478141ec0cced58bb10a989701e90680c07894282df0ced30b2025c6e0954ddf9a70d"
   },
   "close": {
    "close_id": "close.R2-B",
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "realized_total": 100,
    "first_sequence": 1,
    "last_sequence": 100,
    "final_chain_hash": "9616012e77ef1031cd95af137dc0f57495b826ad2a4113dfa85a402771369502",
    "authority": "run authority",
    "closed_at": "2026-07-26T11:00:00Z",
    "signature": "1866bf8749a42fca37fb7bdf027bd510c14bd32c67ce8a97630b450398e3f90c3c770e65856356eb28ea88c8afc6700ac694e5e526124034ed85cc7a248b3b01"
   }
  },
  "cid.R4-B.realized": {
   "kind": "REALIZED",
   "commitment_id": "cid.R4-B.realized",
   "pre_run": {
    "commitment_id": "cid.R4-B.realized",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "event_schema_sha256": "4238a8dd86f53ce5b0bfdc15adc1eadf68a984d754e5cdbb5c9ad07bbf5aed6d",
    "inclusion_rule_sha256": "44acba963ca50225a54e1f8694a795188aab16790405f510bbb0871e69afb6a6",
    "logger_pubkey": "5b9ea09f768cc70f761ea52883075ea2fd8ca40f5136095ce21b03ed91266302",
    "authority": "run authority",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "genesis_hash": "77fa2c9cb45b7ed6a14e2f541dbb7cee6881100aeeff6234dfedf2d3efebd6b7",
    "signature": "5dd03465649d5cbc7583474307f56e8e800a4fdbe5603132b6d130a8de153a68880b102656ae7f4286a442b8e0d262d6cd733508db5c672eb3cdbe49229fc005"
   },
   "anchor": {
    "anchor_id": "anc.R4-B.realized",
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "ec6906070385571d6c3ca212375f7df3a27d4b328681f2843a9ece19435425c680a2337879a11f79e99a68a69dc17a318a402fcbd3ddee17451b1b377187500d"
   },
   "close": {
    "close_id": "close.R4-B",
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "realized_total": 60,
    "first_sequence": 1,
    "last_sequence": 60,
    "final_chain_hash": "988ea5a9870d0858c251bd1f6462262576c01c2d6a956ce0c709b03404fc02a8",
    "authority": "run authority",
    "closed_at": "2026-07-26T11:00:00Z",
    "signature": "2edca4baa22e81f5a04aeebc5212a631ea16f15d430852fe5103d428e1d6db37b57ece40a255237f98c61d14351365a099481a4cd33048d235d4ad490af19400"
   }
  },
  "cid.R6-B.realized": {
   "kind": "REALIZED",
   "commitment_id": "cid.R6-B.realized",
   "pre_run": {
    "commitment_id": "cid.R6-B.realized",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "event_schema_sha256": "4238a8dd86f53ce5b0bfdc15adc1eadf68a984d754e5cdbb5c9ad07bbf5aed6d",
    "inclusion_rule_sha256": "69b2c16c4d99010f45db14bb9ad61f6242dd9c706f2c3a72446e61e0d97887d7",
    "logger_pubkey": "5b9ea09f768cc70f761ea52883075ea2fd8ca40f5136095ce21b03ed91266302",
    "authority": "run authority",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "genesis_hash": "6d2fba1a57c7aa33cfe144017fb282d391525e04015cd245f3d67ea5cbb7d2bf",
    "signature": "c7e4c58f9929a01b1cc8657bc2f86d7952ac22a462accdf051e39ad597dbdf1320fe1eb93072f31c14876fa88412b3cbd167f215ef7983a68c8a1a739fa32e06"
   },
   "anchor": {
    "anchor_id": "anc.R6-B.realized",
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "c1db32784d4a9c2d54bf7f4347aff2d0d6974d1ffa2f99cdc0428367913b8553b000af3f9665cd7852c373684a5c080b4266b72affcdca655e29823172d94906"
   },
   "close": {
    "close_id": "close.R6-B",
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "realized_total": 40,
    "first_sequence": 1,
    "last_sequence": 40,
    "final_chain_hash": "f9df91e8a8d0ab8a3098d76d87e5d4a7e9c5d050a23e546bfc28541f5d5b33d9",
    "authority": "run authority",
    "closed_at": "2026-07-26T11:00:00Z",
    "signature": "44a60ec0067272f793db059d11ff84c69d0d883a8f52d1d0247b672ab4bca9da43ac5aaece17a1901bb512fdad0608e8a2424fb1103fd38522894ab31074560a"
   }
  },
  "cid.R6-C.realized": {
   "kind": "REALIZED",
   "commitment_id": "cid.R6-C.realized",
   "pre_run": {
    "commitment_id": "cid.R6-C.realized",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "event_schema_sha256": "4238a8dd86f53ce5b0bfdc15adc1eadf68a984d754e5cdbb5c9ad07bbf5aed6d",
    "inclusion_rule_sha256": "2c86b5f110411d5b13f48d51516d1c77364e846437adc6cee40527d02aeaf806",
    "logger_pubkey": "5b9ea09f768cc70f761ea52883075ea2fd8ca40f5136095ce21b03ed91266302",
    "authority": "run authority",
    "commitment_sequence": 1,
    "committed_at": "2026-07-26T10:00:00Z",
    "genesis_hash": "1ec5a068bc6a06f52b5cc7e435dceffb37e858dfb9aba7dca6f5e1401d1cb0ca",
    "signature": "48674f902604ea9b3a061bd7b19681a25bd3ee90b6f17a8ce6eeb2a4dbad0f19859211f335376049df4ec6aa1c0b5756db592942695eaf10f1f1f3ef1669b904"
   },
   "anchor": {
    "anchor_id": "anc.R6-C.realized",
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "anchor_sequence": 1,
    "anchored_at": "2026-07-26T10:05:00Z",
    "authority": "independent anchor",
    "signature": "68720e40973488798f7491ec0001e20e3633f1f0b92de6b95829cf8bfda10c1880b6ba9b7870b5eaaee85853485580e4fa73e5cf6b57371d9964bbddef9e5d0e"
   },
   "close": {
    "close_id": "close.R6-C",
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "realized_total": 35,
    "first_sequence": 1,
    "last_sequence": 35,
    "final_chain_hash": "9204703d93ca57ee741e74949e9da191a9c5547c9c2be9d3c8085791f02c8475",
    "authority": "run authority",
    "closed_at": "2026-07-26T11:00:00Z",
    "signature": "0a971532f9b117b0ee4151ec533e2ebe23baa72a8cb2b5b67175951c326264d3335399b06172268dbeef5007666e76f34ba348735d4a2a67f70f5fd8ddd87605"
   }
  }
 },
 "run_logs": {
  "cid.R2-B.realized": [
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 1,
    "previous_chain_hash": "5c1af7c61b1a8ed7f0d09a87465ce6b221e4e310cebb2b685deb2dae0f597806",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 1,
     "qualifying": true
    },
    "signature": "957c90d1f19747cfdca6aeae5490810e5cdc2fbcded8c3dd89706294e8b86d3e6833d20881628d08f7dbd0861aed59c74fece5d68a65ff663b91f13055ecf10a"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 2,
    "previous_chain_hash": "e607593dc2351b8de00c58419ef355c44a0dd0390c4d58af74833b5237293579",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 2,
     "qualifying": true
    },
    "signature": "692fcfb91d91b5d6f83dd4335ccc1e31f87fd95bab42978cac8a222a851349f3e6db8ea3b541db93f398f748c6035a498b032f1f5da2a7be4b394540c042b30a"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 3,
    "previous_chain_hash": "d4078e5cb03996b5bf9ec793bd0134ba10cd09ab1af52a10283ee89fb6a54e39",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 3,
     "qualifying": true
    },
    "signature": "8b1531a3ccba3d0d12ddc7be801eeb450110715decacaa617783570f0638713fb1d2c92114f605c59d1176db882dd9903bc634ca8d2c850f2d25f0ed6b3ee70b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 4,
    "previous_chain_hash": "6a17f12d7fd1b7bc146a6608d77134fe65b99ebb336948f45033fdc23a273137",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 4,
     "qualifying": true
    },
    "signature": "f71dfdf3f7817e522e9e2448fa019a4ec22b42825b121c1a614ba1b035f961d5154f0f8099077b4e7cddf288b423a9029bd445f0656627f02c9a0ec990ff7600"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 5,
    "previous_chain_hash": "cfa2d3a5da65ada835962d2be4aea0e05fbd455bfd0b6d23d4bc3170dfe1e680",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 5,
     "qualifying": true
    },
    "signature": "99f1810eba93ae5d17619c5091bb568a6fcd0d090b9abcc3e3164be28c03d5347ba54ae1d24c601c7832516fd796b2e936098ff8427aabea1c50c71999c9c105"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 6,
    "previous_chain_hash": "fffac237b0e18fd86e3c6ede17e8801091757bd265130a7c357c71eae49addd5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 6,
     "qualifying": true
    },
    "signature": "fef7352db75d86bb85c5c9d62a76476d90f0ce1728c5546cda6795f67cc0da258588fbe61b084072105bb7854f8864609e09a4bf7da5296f5f7f42c3c0c0d80f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 7,
    "previous_chain_hash": "be7b7da1aa0daa062f97de4e9fd2f72eca05b9cabf415cf63190dcc971e7882f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 7,
     "qualifying": true
    },
    "signature": "723d2b69f1d0feb9db01e3838a421e8649e9a657b76370e60c7405ce78393d582ebd0efc68e02196d883140d25fc8efe626776e563ab2c67149d803b93665800"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 8,
    "previous_chain_hash": "3c62a1183e4c70d812952f0395e041638e8f8258680e0a834634583ddd7729a1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 8,
     "qualifying": true
    },
    "signature": "fbb13a7ee97705fc59a30e5be9db217683c1323888ce3ee3d730fc9c2dbf96e023c204590640bfb14e951af8e9f16012c0b91447181b05fcd7d51050cd80c004"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 9,
    "previous_chain_hash": "95c879bb6446844e064a7df76772174facfa9c25d8bd94f2f8c644962130a363",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 9,
     "qualifying": true
    },
    "signature": "65e5836208742a89af0a6859eff7a76388f86bf475c34144948d2bb67a5012089206e4c5136ee2b62ffe4885845fdb1834588eae8e8f2162eafaed262cf33303"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 10,
    "previous_chain_hash": "aaf7c030e18d1b0d28b44195c4f94aa4eb46f9717bfcd6aa9e68ec52e83064d4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 10,
     "qualifying": true
    },
    "signature": "fabf6084f43245705742fbb5918c41c5d60e6584641c0decbfa73a937629807c3f5a7c6c4bb43c05c6c43d6bb1a5f78b26aabe8d660c4353c7642c005c891a0a"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 11,
    "previous_chain_hash": "eb4a906f6e8fcb367deaf1ebdb03739066bc7d1c91673c9ae5cb94eec4b5c84d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 11,
     "qualifying": true
    },
    "signature": "1105066c0c4bddbf63193c28adf7ebf68ef38e0ead2cf00f8b44dfa7dd738ac785f0fc2e78d39f5f789207033534d2b533c21a2cf5569019590902d06e5a4d04"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 12,
    "previous_chain_hash": "0b8f2374dee75c28c8b2b279b9bbcc6dc2d4111f837c6f452ada1269ecb8fa44",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 12,
     "qualifying": true
    },
    "signature": "6b1ad622c332277bbae245c988f7e0c056d5009e8f900cf627d99e85e013abee6548d661490cd8171e1b93a4552fe7b35fe5c6aa8cef56b7e71ac731cd309a01"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 13,
    "previous_chain_hash": "82b2f2d2f9b3d826bb6c2dd719ce287411c36b64ed2a0702f3c5c2e8ecb659f3",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 13,
     "qualifying": true
    },
    "signature": "03877f453e3190154e27509f9f261afd0dc1b17276e0e129ac3898fa6b28a5145e54641d01a70bf3143cd4d110dc150d11b90a3d85c2f7525b84ca61e8e1cf08"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 14,
    "previous_chain_hash": "5d41d93f83fd42e8104bcddbb6f5d9c7e7dbb2bf6941deac1eba21b7cae392d5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 14,
     "qualifying": true
    },
    "signature": "410798271e36e0c7743130d35e160cda9f7556b714c9442257e333b680759d8675b8a4697a643adc04c22cf9a4ff42dbfd0c60a86acf9e5f8919ce9c2831c606"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 15,
    "previous_chain_hash": "be22dac5c99ce25368711948b760efce280fd27de03984445dd9c1de2512a770",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 15,
     "qualifying": true
    },
    "signature": "81102a59858b7df883be9ef0b7246b5fe4906e455f7aa311e374f3e78a44437d154f4fc9e4957554bfd59219329cabebb7b1b88308a0728b5e0b08cf2e99860b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 16,
    "previous_chain_hash": "5109aa61885a21122679851473fc01198803e87c9654153599cfe32001248e51",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 16,
     "qualifying": true
    },
    "signature": "cc60ab6c9dc9c701fe31fbf9248f1513764b918f45cd11a5136881dd815b3f6c62522e5faa378126fa4f1c36af65f858521633b97201abdfdf91d83c5377ff0d"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 17,
    "previous_chain_hash": "ab1a3b47dabb3070ec576cf6d5a0dc764855efb920a4468e8e36666264758984",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 17,
     "qualifying": true
    },
    "signature": "1fe74aa0abbc049e9ad1f7fb9240bbb76a3dd17d2fd2ae512542309b303d7c2a4e08327163c8b6db724af81ff137fa0b85cfbf8ddf017f369558c57ab317bf07"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 18,
    "previous_chain_hash": "deee3daa12b4e5e793777549f1d8a6fcfea02a0f25e6d236303100c2e6d44c27",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 18,
     "qualifying": true
    },
    "signature": "5caa89467785f8f7eb8746f814cd68e03bd25eaa548171b66f73c1d60163f4a1d7f88acdb33c7f9328e94b7820f852291b828ae772551ece829a82c8c0804607"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 19,
    "previous_chain_hash": "a0a5d750437d74109d854fa6ae508128c6429aafb08cfb2b59a4f5c76ba37bd3",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 19,
     "qualifying": true
    },
    "signature": "2da87b808c83f7790cd4e0bea864aa02ffbb8184db3688c8bde9a30b76f07b53ad2f3479cccb8836bc2018eb92171c92e6f887984d175b924630f3e982548106"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 20,
    "previous_chain_hash": "36f76545a005245a212b5f50e7282be1598afac52c23780610ea16e855040fd4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 20,
     "qualifying": true
    },
    "signature": "2eea65ff631fb777a1b14ae15dcf75b9a2c08d1b5de1f9f826a5f29ac1a53c451f84f508978bf13673581b2b45ca99870a137582f99f5b222bd865e96a50a50b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 21,
    "previous_chain_hash": "e0def7c162a2cf85b131f69c17f68a035fa5d5607db956fc9695c8526fb42ff4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 21,
     "qualifying": true
    },
    "signature": "f30e6155b9cbf412856cde720ffb42b695d9744a16af3610f4e1d05e7718fe25511961baf110049a58f59724ff606a5df8eb698a0df694945369c216e2fa330a"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 22,
    "previous_chain_hash": "a325b01a67290fc4d4063a6b3b15edc4cfea19f8c217cbd25e300978fb2222f0",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 22,
     "qualifying": true
    },
    "signature": "de46fca3c91e8f736e10fbece0ee809ec52967839a416fa0b0bc56b27f715109fd4ad4233550931d67b37e2b6df64eebf67bdbf464aacb1a6e867c55e18af005"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 23,
    "previous_chain_hash": "7103fc20fbbf7b99396adf3038eb8cb224380103a44df0a58e06bc46170f1127",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 23,
     "qualifying": true
    },
    "signature": "a47155d2ba16137c22dc456177931a8117f5c4217802fc35cbcd6b84a432adb8666c6a68a73ffd74a33518ba50c98cdb0b506e7a78513904983864bed278da03"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 24,
    "previous_chain_hash": "0730fba197fa88f225e3ec17562df2a8dcd8cf46d817537600d01266f7362063",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 24,
     "qualifying": true
    },
    "signature": "14ed799c82a485dba08f6f7de5201075c5967f72104fcf797b0215a6c2f7a258cdf13f9b3c04803ba0d6a36b8630020f66cce29c3eba1a702c857bc876d4ec00"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 25,
    "previous_chain_hash": "5392819883b242d56ece6df9913f4c888654c9c0988fafbcbba3d4da68e8a7b4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 25,
     "qualifying": true
    },
    "signature": "538a14332bfcc82c55c1ffdbe944d5067154e7a7561c59008279d16f9562c873218ba0105c768ae33bd534350a0b68b746637cb302843e5d6f23d586c0c0730b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 26,
    "previous_chain_hash": "24ddcadb9b5aef21bd7c8ddf0a445bfcd8b55bda5a069dd5ac37c05f0f6de0a8",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 26,
     "qualifying": true
    },
    "signature": "f18977017cf8539a1fd5b05e10b5cd13d7da85e6a9c0d40b154bba935fc32841e669312c6a048fbdbc5a54651dd3d816bd1fcc01494a7ea9e065e3928a455307"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 27,
    "previous_chain_hash": "1d55cdabdfbb94cee70f9b8b406377da14bcb6813c822604788add2991b1538f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 27,
     "qualifying": true
    },
    "signature": "4ebc7115d85afe71611400a450b262ff5eed8b0fb8e1836fff9ff778c300d2bcf68d28d01ea40cc25e634e1d3eb274215f07d57f33129b25318bdcaac00e1f0b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 28,
    "previous_chain_hash": "9d67e3e70032631580c013f1950551b7173d59014fcd66664552408b5df952b8",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 28,
     "qualifying": true
    },
    "signature": "1d8fb2a0536c4d812ebf50110f6b9167a52949b46f5d3d519f5983ee587f10154a8175867a7567f582f18ac520e0864f44242074f379ab728564fd89b08ef40f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 29,
    "previous_chain_hash": "985b5de7d48cbe86e0bf793905af43560beeb3cd983762a75e36711d8bcbf52f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 29,
     "qualifying": true
    },
    "signature": "5f63fc401b976794132762996a711022504fec45eba6f3e5e3d29d3f8c5f345040e540cdf2cec83106550f85db09a9b90e67c46dad15e929f0f93f81b42b3a00"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 30,
    "previous_chain_hash": "a2e329dfea00e47acc026f931b946a872de3a6c14b6f78110346d2baa9bc8ece",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 30,
     "qualifying": true
    },
    "signature": "5850443e90ff95cda2dc80735b77b869a4bc8405b5a28496732e8e3eadfbde25aee15afd1821915139fb44f87d9b85884afd564fc215e39b44199ae525ce2f07"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 31,
    "previous_chain_hash": "ce0d37a3c6a27c99541680c54e87057fa5c252c5cb6c28a873c7246303cb34cf",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 31,
     "qualifying": true
    },
    "signature": "4162735a1773f7deeba388a106a179db51ccceee5a7c2989a5757361ff4f6c496dbec89d36d5363fa6927a280164c3827d2904b965eefd9578142c93ad093307"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 32,
    "previous_chain_hash": "49d5a3cbb7d4a24af392a835a038b2883132ff65cd40050d784692b5acc4f1af",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 32,
     "qualifying": true
    },
    "signature": "63cc1e5e4bd95c61bb938f0d7682fbd85d800177fa50b1dd7fa9399f587cecb84e726bd2fcf1adde25192975319c3ac0a5ad98533cdb0c0c26e39d8be8fda80a"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 33,
    "previous_chain_hash": "e4c085269f091d6d8fedd02e9b676b2d23a74545cb60b7925fb6fe648be8ea22",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 33,
     "qualifying": true
    },
    "signature": "9f65afd29430d8a2258cb88706d05ab03ec08568061c395e289ff58325481ed45799ee6fff43f90e4e216def572a9966eef475a61c278557d98c4a0d02c2c607"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 34,
    "previous_chain_hash": "53c41eafa3826f07b726885ec05163f5f6054c21f25746b565d5bf92788b3ce5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 34,
     "qualifying": true
    },
    "signature": "782f91768d33851f97c3fb5823b9c5015e8846a7a1e9ae42d4cd2dee8eddc9ce9258757c2b7b93edd107f0595511f85b50dc2811493b3c867a31fc3be52d6e0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 35,
    "previous_chain_hash": "83eff7a42f51d1e3ed9bae9a32e26ba7ab9c817e554e2e4583075c1bbb44b71a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 35,
     "qualifying": true
    },
    "signature": "24462695dcc6f77f63bd0866d3225ca2b7b07b8c6c7f60268d9defc8f54f252bb9fb569b0614a6dcd8d97dedd324ffa9e98b90e572e4d78fb5194598e0fa800b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 36,
    "previous_chain_hash": "f830543332d9b1d78bcaf48465e45e729935e4cfe85501c2f62da234c14e70b0",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 36,
     "qualifying": true
    },
    "signature": "f95d3ac964548cd1390d023ff7c1061ec8c975aa95ef271f44d398e3755aa4c888051b25c5e065d2ac8734a2df6cb2d61abf77482e9d514056f42cb9ead5bb0c"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 37,
    "previous_chain_hash": "269eeea242cbc69e63808650554f45506a3c6e5f3b4bbc761e0d3755920bb371",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 37,
     "qualifying": true
    },
    "signature": "2ea4186125ee28405a125c12dda871df1256fbdf66b7686ec648f612a0970a5300dbe38f91b68fd85055af7d4c57033590fb0f234995657bf7f51d17018bc301"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 38,
    "previous_chain_hash": "0e3ffbe8e4b5c8ebf7e7a40a3de33c020d3e7061ec7ca452338e9074e53fedf9",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 38,
     "qualifying": true
    },
    "signature": "b50bce1988ab987b6964c29d71921bc9215125b084d507ea4590dac4ef5f743cce04fef17a6d3f85af88f6faaf5c015ffdf16ba0ac83b7d53e11ff93a261680d"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 39,
    "previous_chain_hash": "d99ab56ccb782ff713c067796e997efb662f06b25d4e594d88e36db18c69256f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 39,
     "qualifying": true
    },
    "signature": "e681173b5f9979629facfe75f0c2b848590a1aa2f9cbc393c8e83147849432723e73d0a13a77564db796c3fe384d2ad6d0083554a48b5ed1470251768753ff04"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 40,
    "previous_chain_hash": "09b56c67554c487b12247b9f2c612966e9ca05c723d6547f137d676e2d81d301",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 40,
     "qualifying": true
    },
    "signature": "32bde63b6ad372c679af2d96eb04b50bd8cd5da754ddeafd3b5d1c34b26310eee703d77a4e8f984115d8c2e2e66f2dc9670f6ccedeaff7291905f60a9aee560e"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 41,
    "previous_chain_hash": "639e6783e674a753692af4b8ce5e41c998c06b2952413a62a28c956a42aeacb9",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 41,
     "qualifying": true
    },
    "signature": "6c154f2e7c10189ac54a2038b32f5900475aaf48462e8fb1b36e37a50fe716ce6d082cd78e4ece396aab2cb61f7c7ac600358c74528e74188c948e80642f7d05"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 42,
    "previous_chain_hash": "8b929cb5198e92e308379a5466d1e1920233bab33c01d018664999d53bcc581c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 42,
     "qualifying": true
    },
    "signature": "502d2036d9c2d70f4a6c659fa065e2d7a85e1aeae65cbcb2d85b88feb98ac56d822ee009caf02d016e7cc9616de535b3c1dcacfc87aa5ea0ae8ffc2222c43c07"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 43,
    "previous_chain_hash": "4de07e9568e17ab7ee1fcd668293306aae6ff6d3c324bc29b521c4813f4ede40",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 43,
     "qualifying": true
    },
    "signature": "6956aaaec747254b7043e41a9437398440f9ad6ac1c07488fd40efd79f6e5d77bf923a7d87e3f267779ae76a249887081c501f58514b758ab324b6eadd5c580b"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 44,
    "previous_chain_hash": "9ad18158c5175b277eb8b213b4fd13960be787a17ad5c60008f4ee5923afca5a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 44,
     "qualifying": true
    },
    "signature": "8b441f6340ea8a917faf9df78e4667f1f2d2f963b66ee796c62e8ffcb24d37d23fc348d5dfc0c6dd925db53968aabe9da60010018c1b7c364886592488430e04"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 45,
    "previous_chain_hash": "e0f0ea34861fb3992205f64928905b0503cb71b381f6d86142779bd1b913cd8d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 45,
     "qualifying": true
    },
    "signature": "705e932a17fd36f80ac57a981a0b11ec9039e7d5add04449af83d5fff055222cb7fca834c940b31024c30ef82ab2022c73459dd6656eae296efa7e7a6d62b802"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 46,
    "previous_chain_hash": "54ad0d5acfddfe6eff6c72fd71119e9d4c46773d4f76780f4a24849b202a5864",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 46,
     "qualifying": true
    },
    "signature": "0bedd4b0209c2f888eb52fff89cdf968f5675e758bbc52f1030e0e9c344765c406fd4afd320a144e03032954b7c18ae735b78bb74d6236f8de39c544d88cda02"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 47,
    "previous_chain_hash": "15b8aaeb2dbf1ababbab5c689d24e6afd3b509853d06f78410b993b601db9750",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 47,
     "qualifying": true
    },
    "signature": "10712b77c065b3e058314875dce186432befab7473c2cdbfc44e713bab6efccbc210fc36e268b86dcfd68134c75d313795b1479b1d0d17e735e61ec1703b8001"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 48,
    "previous_chain_hash": "ddbc8544114b08f6f3d71aa4be1b21f67821411919c0d2585399953b52bd381c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 48,
     "qualifying": true
    },
    "signature": "300956177c42d35da367abb0f5c5f20d9305acf779eed7aacb43672cfe6fcd4251d7f756b45b8137171f469338286870f689becf8b4ab276d6f7693e534a4800"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 49,
    "previous_chain_hash": "c26e7868f1691a5fd51b685a839164e9ae448e5b4f996ec0df3d81c728b7c3ec",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 49,
     "qualifying": true
    },
    "signature": "d665d0e378d4f02bebffb8cf5ede9e78463a05a8f6017602109e20215fd13d37c7b16c9e64dcb65d5ba311091ad68153d0bb68e06b093202356243e2aba5e401"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 50,
    "previous_chain_hash": "0362e2b95fb72103950a9258b29d9d1ea35f15ea620000a369a692be31e45588",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 50,
     "qualifying": true
    },
    "signature": "43650dc4977894ae225db1bac2d253bb1a68b1e43d8cb6d77f107116865b57e266309863bf2ee704c949ea3f5e45c1292052c3f96cbf7e135ac7d82a3d398106"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 51,
    "previous_chain_hash": "1b35efccdfd2c06f006049c5e9eccc9669ed5ea05fa483ea918658f107aa7e51",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 51,
     "qualifying": true
    },
    "signature": "b1f653f3e147b6714469c31e0317cd805b3ec257d22b5b6ad877419cc1bd76c2fa7b009ce7bcfe05da665c8c9ab6a2b9196231768cb0c41f0571da99c476a407"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 52,
    "previous_chain_hash": "a1ef41dd8a08a2b41c7ede44dd404f9ba822884a69e58248695c139101f7ac98",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 52,
     "qualifying": true
    },
    "signature": "fa7dd518ec82c4d661786042a10227738b9509128da1a65a7308f5f6b114802f173815fcdd95cc68d950162c6e6b8787513510b62462c3fdf666a9bf16a88101"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 53,
    "previous_chain_hash": "0a05f6f3a122964d5c2652d0574e09bfea79e4236ab672c7eb1a87093609bf10",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 53,
     "qualifying": true
    },
    "signature": "b623e927a9271c18af91f702bdb34bc0f5a32ae7d7e18c55e7297c653da4e0a81c1abc88a4d6bd89c5b85374eb167b48dd02c19b45e575e14c42188abbcfa505"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 54,
    "previous_chain_hash": "df627cd554b72e1c51d2fb069f75632ff73eeee16a6fc99a507a388433909458",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 54,
     "qualifying": true
    },
    "signature": "358ca86e2fa73646e47e7c862034d693f5b93add7ccd33b6477e74c81fa45f50582a86051a5e68c3ba5385d17b7a6680d25b1f815982cf9a61e955b785c3b302"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 55,
    "previous_chain_hash": "42c9ba75c917900e09280f1db58c082c31f0847a9d47ed38a809cfbfd9632868",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 55,
     "qualifying": true
    },
    "signature": "f9b801bb2e7626e8b3a4969d172da66f9652b3481703c13a1f58ea49717eb8011906a0d2fff878391c096030e1f6965c698b273b44038fc8b9f7de1c2221330c"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 56,
    "previous_chain_hash": "517a1c62a53ba72f3d6ceaf4e4b7405392a7ee4adc093c5b84787aa7a43fd3fa",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 56,
     "qualifying": true
    },
    "signature": "2d3aa18e38215ec0cd6352d7df4de0276c6b6bd3d44ff331e5591035151a2b16d8aa8e1ec5b17177651a7cac7389db5bf991d7b91a21c9ad3e9f4e0a87412b0c"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 57,
    "previous_chain_hash": "c5d73bb77574d72efd63810df21b395573e58aefc9a6a2aecb749694b5904c75",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 57,
     "qualifying": true
    },
    "signature": "05c0ccc163111ff44f4bfc7b7b676a31260becb76a6d13bd9c3fec2a85438bbd6743c1e84e409a68e18261aba26cd0a7ac4a11701ead647095677f771c013e0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 58,
    "previous_chain_hash": "08efa1baec826f90a96e8be7888ffba4ed6406d3b1d725b224daab19bce977a5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 58,
     "qualifying": true
    },
    "signature": "cdebb932eebf28a7c23804db2b0f8b840c96957548cf3a66c7bd12d2ff0fa0cfc4414065ed73a18513ef77f125f5a4cd6dd804f26e6efa0ff4d7aeb6f6563c03"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 59,
    "previous_chain_hash": "cf4172fefa6172e38f6550cc60a494cc579f17289e70d4dc973ee4ae9a710455",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 59,
     "qualifying": true
    },
    "signature": "5cea000a2332352e17ef4685e3545a64c87ee98eb70551b22e928fd817c2c7ffda003eac7442c4b095c3062cc7ddf192f2abaff4b53a85955c813d11a85e7d0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 60,
    "previous_chain_hash": "535ddf608bf69145810972c15ec4cec2354c841788d9dc764d3d08a05aeccbe1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 60,
     "qualifying": true
    },
    "signature": "456ae7b2ad6f0fe34b397f732093945a8e28895b4792ffbc96178a33d779928965eb0a27d1de05b9e227c4fff1e5604e4dfcb8721807316534ab03ad2461cd04"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 61,
    "previous_chain_hash": "ab143e2bc6e2431e1a0a8a627a2775befcc4bdf3f4f529cda9ce7d65770395a7",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 61,
     "qualifying": true
    },
    "signature": "a5a0745b61ba2f1c5ab60b4a78d0c33eb4170daea7bd50349a70c2c9414def86e2dc97dbb5d728324d2619e6c0f78cfbcac4a471c5432704a0fd21595841c00f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 62,
    "previous_chain_hash": "7b2d46db2b37f08d47681bff4b1ad39d3918d22a77d22b9c240fdd4ead42894a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 62,
     "qualifying": true
    },
    "signature": "997f76e7f75728c3a3f33bd22d9aede7da4923c24947baca556ec857cca27635d92c711c2befd6b28e7f2d6f659376e9ceeb21b4e3fccb0f661fd45354eb4608"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 63,
    "previous_chain_hash": "ec26f7a6b2292238ba92516ec2e14e871a05950d2201402886a642248d9cf64d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 63,
     "qualifying": true
    },
    "signature": "15410946a0b7eb9f208a753336563a1944c013b0f37166571d1384014f319b9de3305c0d5a7c57b1b3a6ea0b4081b8d1927d0813fa4679d189572af5526d9509"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 64,
    "previous_chain_hash": "bd41f80cfbb2bcfb4f3154871e3975f8f83e77b5aa56824c17af88343b1d2c53",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 64,
     "qualifying": true
    },
    "signature": "013e0a316b404356865f78476bbd06599f8564b5374b06e8c007202a19c0e7e2bd7735e18a218ad919df88bf083c4b1ab771394eb3670c2bd28c130d5248e006"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 65,
    "previous_chain_hash": "053191604fce1ac2ec69104164a5de5a2345b062fe76fd100e4acc58cafdc3fe",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 65,
     "qualifying": true
    },
    "signature": "af831cf316fd8a8811bc2bf228d25f07b9fdc8ffa3ed932a29f2d4d929109bc58ea348266a5c077ae9abe746145d6e64ceae41c98733a77e6fce1e8bf9bd3201"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 66,
    "previous_chain_hash": "6e35d91600f9254ebf90576f275aa1db4093c5a707606835c202a2b280eaef05",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 66,
     "qualifying": true
    },
    "signature": "6cc89bf40b6283975f628016b3218574522eb6cd6479dbc7cfcb283be623c3b1ec447618fbc90895ef438abb31117a15abac6c1f3b00716479e5ce34eeabb906"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 67,
    "previous_chain_hash": "65c334d4bd0892a0051f2b48dc4aff51c2c29e06348fe84bf852fbe87b2f1793",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 67,
     "qualifying": true
    },
    "signature": "873d93bb8405c976a3081294c5ac7375180323a6dfc11b6e94a78f2804a1e58396e7936e6888e98e178342faf99c48ce73923b78e87530c2807db4b22b589d0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 68,
    "previous_chain_hash": "0df904980c460ebe65e07e39f74a707ed75c0a17783d52bd73f7c609cf0381a1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 68,
     "qualifying": true
    },
    "signature": "e23ec6252aca26c715c1ab52d86af866fd4e83f95daf31b12a5c27bc01d31f94fef5d55e5ae0a76f82b2fa830b0e1ab65c68d8101a722a838c6636cd09a0680a"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 69,
    "previous_chain_hash": "9571128ff8f4f893ba376cbb60b175842e0c7338d8cff6e086be13944068afc7",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 69,
     "qualifying": true
    },
    "signature": "1d2d3ee71589ac42ee40bc58b35bad90e5eff9a944ff035b4959d99ef68b7cd47e818079d42969a5594eeefe9bf875fa3728ac2d390b4d818789d630b655a107"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 70,
    "previous_chain_hash": "781afc44edc1a6c3a4b01e40fb9eff5816f00ebfa0e2998cd8add17efb28287c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 70,
     "qualifying": true
    },
    "signature": "07d42b258e5a6ea8f92f63b29264854b3a5b94a3c409f9a9a3c1e18e3af27bacebe2322096cf698466c1d381dd5f8581bd2322e9b9bc5d84a01aa360a19eff0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 71,
    "previous_chain_hash": "7009484453fa1ac3ca5e0404968f8e985c9c4e3dab0883cf5730d4c03a3f63db",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 71,
     "qualifying": true
    },
    "signature": "b28fd86c0b01522562d46ec482daee0d5beb737d4c4307ea72144962f966baba5b09f99237341c6c4df8c13c69d7664268929cb29081cdd4f5d536e18d68a50f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 72,
    "previous_chain_hash": "1f4dfa1309332c2236debcb2aa9a52246c73337350e2756775d0ff2b0e452a04",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 72,
     "qualifying": true
    },
    "signature": "fc6bff2e06f24084277af31498498f68a13855c48fb9b9eb35643e28348e78702dd1594bfdacf0f170883bc40cbc34e62f843c0c375e2b04d657794c1c4b4a01"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 73,
    "previous_chain_hash": "dd54c45b82d1df0c12d2eb7e2b3dbcc74702d4a5db5b72e9fe6dc859fb8b317e",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 73,
     "qualifying": true
    },
    "signature": "9c14b373d1cd29b608780298410032e6a3bcdea0f10b75af2a349629353c0ca8fc8eb3bb6d15041c046d86a138a36c11e91987842f4ff6d17f4b9e0db496c20c"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 74,
    "previous_chain_hash": "d6f693071830ef65b20c880769d2f929a3d7e2470a6f5b1cb5e106507f422d44",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 74,
     "qualifying": true
    },
    "signature": "25a1e44b49f74878d9209be431d9683c8dc40082fa114b5d244071ef63331f865765f77b775e3121a446543984afc724fc520d261308632678bc02bf20241901"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 75,
    "previous_chain_hash": "828c98d3d0af02e03d8b7da4d9703d568d83759be28718e04da649e17c337dce",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 75,
     "qualifying": true
    },
    "signature": "c2af5d1049337d13dd89f9b107bc3c146316e8257e21af1b88738b57e67c5b671df62ba9f746ee76ebde5090e8ee9e9358859e52b4fb92f03feedb302d085b01"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 76,
    "previous_chain_hash": "2cdcd7ca385f093e9c02fd338d73287c49797188fc54c9df2be3e626319c8217",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 76,
     "qualifying": true
    },
    "signature": "1153f49ba4a342bbb6a4aceb549815ba4e5acacd014169ea2f347a7544c37cbe448a3322e7394ec2d18c50ccf9da2656dc16a82dcc8d21e359446cdc9e112109"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 77,
    "previous_chain_hash": "bfef89ef7c09c66a9864970162607f81bd1792f548623945de6b2dbaab58b09f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 77,
     "qualifying": true
    },
    "signature": "3087d81f7c4579a9557f7a7922c26ea970efcdf61c8f0896579b65dc794da78761958547c822abc65cdf366112f34b5cb6c8f7058342a372576c59c33772040e"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 78,
    "previous_chain_hash": "48e4cce9536437f0fbddc4087e79b5dedb2686b5210af5b9d3c720f871569b9f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 78,
     "qualifying": true
    },
    "signature": "f3170394af7e56b7351c67ec1d44c5975573f26fe36369b2f89368eba1d8f555e38bcae228523088b837dd4b42773a5016d3cc468bad3b793ccd522899e2ea08"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 79,
    "previous_chain_hash": "c0dea7f01385c95e38a29a85a2a8e44b18a8fc40d3a48ab1a4d22b197b58142f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 79,
     "qualifying": true
    },
    "signature": "d927dbf48bfad8c0d4be7bc07f67bb923f71875d7fd70970c29d8505e6fa222ca0e88d450390ea38b0e20dc58fc6a9cfae2f00a1ee58d33b1bd8f3c5eb2dd602"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 80,
    "previous_chain_hash": "ac0a4a06a6744db2fb0fe61136741251a18e12795888d3cd53625ecba512ae21",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 80,
     "qualifying": true
    },
    "signature": "f7c0c42808bebb90806a88b5e9a9b3078afbbb3594a45e7bf43d09949fd504fd337d07850b69592f9f2e54c795d32c409cde274c4bc02a0e5a426e5430adbf09"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 81,
    "previous_chain_hash": "fffaae21cd5aca515ef5b4860dc55a9879fbf062968b946b24b8e4c2936d0360",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 81,
     "qualifying": true
    },
    "signature": "3575e12c953f970e6869484059703131782ccb2e16cb38607dbe3ab30688c19ea31f6c78981b9f5fe0e64ed5925cd211f6858670df156a0fcdc9ae77a6836f01"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 82,
    "previous_chain_hash": "61844e03e7c346d3b6f033152da1fe04426f99f286526e81a159ffbfe15da747",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 82,
     "qualifying": true
    },
    "signature": "d60ebc113cf8305cbf341fbccc7a984d96b76b14432e6f86e466d6625cd0389f9e22cdfac5c4ecb7b732380c66b588130c39d1326deedb426692346f47317200"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 83,
    "previous_chain_hash": "31d704d88e02a66bcfced8ccd738c30646c65634a9796e2537052722b64b0afb",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 83,
     "qualifying": true
    },
    "signature": "8db217bf893f04276334848488e8242890d74024f4c51411a5fe567513debe7c7298c7badb6d85846112212ade3c276b19ef4f00e326b0ad9fa435b4c9469507"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 84,
    "previous_chain_hash": "5a134f19209277eb08a5e119fb68bb6f6eb5502782a3fc60ef5153a6108fbceb",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 84,
     "qualifying": true
    },
    "signature": "27f6cc4121c0ea41ea1d8356b9ada540018f2048161b8b2531c9eb03d57800096577303e8c305c9074138a732bb777bf9572e0e2c772623dcbb160974d1bd209"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 85,
    "previous_chain_hash": "423b677e668dc3836e91c2ab270ac3ea80ad24df10581e06ff4b0e59a798f9a9",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 85,
     "qualifying": true
    },
    "signature": "bd0c9b8587008667bb4954f666035f3d64e15215ff520615c26e37f8d3be7f358df2f124d9e29c27652d15910764e6543990986425add39318edc7ce91464a03"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 86,
    "previous_chain_hash": "beb9af08373543a4d83c65d29c6c1bab907f50ef469ade559b86bb28216fba50",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 86,
     "qualifying": true
    },
    "signature": "35006a10134e358338be7da6de502e38ce4afa2a4cd7dd15818de832c92f4093de0d1a1eb109223c70acf813061cc1de874686c0722c7577fbdbf5b15e87ea0e"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 87,
    "previous_chain_hash": "da18b0ca40cb3e1654381ddab55f37297b6b1c564ce20cedcaf00cb02b1d76d2",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 87,
     "qualifying": true
    },
    "signature": "731d4c5aa5026f0f3f1d674ddc07bd1895ce9bc1a96848cd6e01189440c3279a4b35f0cde7390ccbddd3b41b94ba150f4115d84333bab1c0988b48810fe90405"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 88,
    "previous_chain_hash": "779297fba82f8de80f0fac7632cf5d4b09bd48d05806255c837c5a497c9d0946",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 88,
     "qualifying": true
    },
    "signature": "fd13b90d806d7620ab18b7811c54dd39df209faedd9790f4d7e170e9a194746afcc32b289323461876df784470a0ea18464ecfa7a16207008fb6cd541cb5400c"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 89,
    "previous_chain_hash": "0cebcd67bea198f69d86bbc6cc7f54599f74ef632ba5b7fd5b09acef4a1eef39",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 89,
     "qualifying": true
    },
    "signature": "6631dfc39eaeab1a2c7f2fec9714c83460116e637c18b1bd65dc5ed76e01d8b65c957c7e3f2ba9adaf8a66eb8e275e71fdfa0f7171df26c46742df6b86d8b305"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 90,
    "previous_chain_hash": "55044a26118c7a5c15d5bb51818a39c9d1fadf04da37fb245f45bb85db713055",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 90,
     "qualifying": true
    },
    "signature": "911d6f41d1a0248493494e9e50cd4764b27d7bb6bbd2e60d369a68787b520302de98dac508fe521a0672737ab0ba45d67050203c0933e7e6f1158c8acf900a0c"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 91,
    "previous_chain_hash": "99c0a75dcf2a0f2dafed0f4f85fe98704c045835c6fab4c36402711a208b318f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 91,
     "qualifying": true
    },
    "signature": "53ee21f89052606e233b7e12e9a3b441b072a98cf1a17b1aaecb2b9a4e781d171b8834377c157b10c35984aaf66a17d54bc7f191a5b3c4161fca832ab003ed0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 92,
    "previous_chain_hash": "83687f0d63d1bef295817c05fca42f5941c6cdb151db477fbe373afaffb62913",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 92,
     "qualifying": true
    },
    "signature": "4db4b9ee5f20a14e159e2194a3db2aaedbf64fb6d03c19a0dae31ec8a4fe3dfc4b4e7abea53bd7a3b85d38f0b092a7fd877b3b08100563a2efce13cee1b9b504"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 93,
    "previous_chain_hash": "c3c80e1fc93709c423ae5683194079c346c7ab8c07d1d56cc1cc4f08532bbb5d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 93,
     "qualifying": true
    },
    "signature": "8a945efe203db3ef358ca5e2796ab12cb20898bfd48d039ef5d5f546d341af274b4a0f551ab2802365090e2fef6f2a03e5d1951ded8aeac0a88dd827ae63330e"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 94,
    "previous_chain_hash": "9adc7c5b9a83967c846e1de9a104458fc39a1628eb83a64c34b7a12b24333194",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 94,
     "qualifying": true
    },
    "signature": "5a464c548b37e7b54779e2e40666df2a50c4dd8840c22a47dce6a5c0e284164cd333ec73a4c2c999828a7a55d2078d4398e43a03f8260c7e33967ffd66a8f40d"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 95,
    "previous_chain_hash": "b2fe81ac58cf7300ccbe5f06fb6aef9079b15c99eaa836901d8eee668b13fe2d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 95,
     "qualifying": true
    },
    "signature": "c2252e9cb4c383617c8e9a7cd780e119be2547a9401de402aab955e6c951af343f12b8e6a19fd2a0764d36051a9a5d1c5db49bc7496686d00de6b5b985f89006"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 96,
    "previous_chain_hash": "4d2558b86cf4fc2b0326f62b9e45961fb646b550d39c29cb95aaf7e8266cd10c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 96,
     "qualifying": true
    },
    "signature": "3d4658de58f5ee89459872c2fb4b10f46dc4438ac99b59a605be9aa99d4ef49e4d3b862582bf3fd511c9afc32076c23bdb99cabb6cd0b6efa01e42caeb4b7408"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 97,
    "previous_chain_hash": "f34679cff555e1dbcf16eb7525a4f5f32e84bb7d1ac460a2a881ffc0c43b7d3a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 97,
     "qualifying": true
    },
    "signature": "39d4602d6bc2a84bc385b11776e4777ad1b8d12ce00c02d7580ec4538e1a4529f85fd78046192f082dd3cc9d0eeae8974f237a1a5921e42beaac64bcd718f507"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 98,
    "previous_chain_hash": "f02e0f3b360f693bb17f74a567f3185802cdc3ab5b979ceb5470e660f9292cfd",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 98,
     "qualifying": true
    },
    "signature": "db49597b0a49da96b01f627b706385eb2c4d047c6f0aeda5c250a7be09c41b9ba5226380c76136c014dc040e88ea800a2423caf43454d202028fac4e12ca7f0f"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 99,
    "previous_chain_hash": "47ac5b95fe03fa330875854721833b297426f59767d1670078ac3dd1e8f4cd65",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 99,
     "qualifying": true
    },
    "signature": "a9b15034f7cf74ba485dde84d5ae035bf260f95aef8de6dfdec8fff301de4b67113766101cf3c623013b1f27b16a5222777ff0a85ec5b0bc05483326cbfbba0d"
   },
   {
    "commitment_id": "cid.R2-B.realized",
    "pre_run_commitment_sha256": "e5a0cdc0e1acf036f7108239a4f46147fe1ffe2463714e991f26ca4bffb7759d",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R2-B",
    "universe_id": "u.r2b.denials-run",
    "run_id": "run.R2-B",
    "sequence": 100,
    "previous_chain_hash": "4f63823b62a42771fee61468343399e7ef7a39fd0f4439c869585051d3807d1c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 100,
     "qualifying": true
    },
    "signature": "e276a94c1c91f76d80002294c2ce2411555bc5dbc91f5516bcd851a8ad46b4f89570b5b3d7529ac7dffa35924d2645af2ca4b033da25c28c8f3a2849d913b40e"
   }
  ],
  "cid.R4-B.realized": [
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 1,
    "previous_chain_hash": "77fa2c9cb45b7ed6a14e2f541dbb7cee6881100aeeff6234dfedf2d3efebd6b7",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 1,
     "qualifying": true
    },
    "signature": "61a43a9da0ccae9b4ed0023f1afce9e6435da773dc6bc40cf1a590efde5506f7ac6acf01e50d99f2ade37e732020ad52c5ac12196ffc47ed8540ea164bfc340e"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 2,
    "previous_chain_hash": "b2c228bba3196becaeee382550cbf3d9b2ce8d3b300c03e7e375ff28ed63c6ec",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 2,
     "qualifying": true
    },
    "signature": "5f0e01bf50d95058a30d937e800cfe58b6d84e339462690f6bca5142207488031643a3215d9765d1c9f520018ec1433bd1a703f81621ec77f6592fec8695ac0e"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 3,
    "previous_chain_hash": "fbe73ce8ad9542c23b9100b26c7555af0510d3840f6e14f4a8ae127e2b66b320",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 3,
     "qualifying": true
    },
    "signature": "9f8c5f9b1b39ecc90c53102b199fca5688acab89a63b29af987adf18ba99d8e3b75c8902d6b614afa602b71ee92d6204a3a1d4a9e8757e2b78fa1817ee856a0a"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 4,
    "previous_chain_hash": "169f173da0e498f916ba27558f5bd079a211c1e07612d464ab9ced770288eca9",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 4,
     "qualifying": true
    },
    "signature": "643d8c3598b25dcadad8100ff6532342b55329807205030d318b605a1f8095d53d31a2bbbb0fd3b2522a8a0d98a1ae25858c93198556926d575a9ac558538007"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 5,
    "previous_chain_hash": "76e32bfea288fa3508767598a1f41b21adb751aed996ef7329a331df4b80bd0f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 5,
     "qualifying": true
    },
    "signature": "09243ce291d3a9bdd718693e6586aa24efb766b71affa80517cd2e83410bab96c8c511e480de461e0ee42de4525b7cf1a9541847669f5b3c6b573e7c927ab501"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 6,
    "previous_chain_hash": "8fadbe252cd3a5bfd7b3540ed44cb890e948124cf98eecb7bc8397ee4b073d6b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 6,
     "qualifying": true
    },
    "signature": "18d902a87c541f6c7b13e0ee9ac070796c366b7be60cfc65ab6be034575215c507a4be633cfaf89171580505b73717b56239c067c396b42ea37ebf815c454704"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 7,
    "previous_chain_hash": "0405e85d94f5474ec1ca5a3f818b96e7447f5f1c9e16a57f30b8301f88d3c492",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 7,
     "qualifying": true
    },
    "signature": "16ad3bbeb573a3d7c716bcfedffbcd1af6bbe574bd048298cc58425343774e195d0feab018c3798d9547e3c1a0b7f430d5d940df9a494293863ed3d56ddc9904"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 8,
    "previous_chain_hash": "0097efd3e8ba180fc6443b2bc044f7af40a6144c66926252e10cc34234420b92",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 8,
     "qualifying": true
    },
    "signature": "94ce61eefc7709b15deeaaf8a711e741cabfbfc14ed263d03d7e0c3e3fcb6898566a6f09c41a87b6b142ca3094ae9f3b04fc7daeaa2ee4f09aba2acb23babe0c"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 9,
    "previous_chain_hash": "8631d947d780f06b187f5be331ff7e709bd3df48951fa1920c33bf9b553718ff",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 9,
     "qualifying": true
    },
    "signature": "b3ffea9173d80f23ae0f5af850018dc0552680fd5caa32c3710037bbd2af70c373f042b7884968f3ecb7d6c04be1a6b75e855e859cc2edf0f7df7d8391e71002"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 10,
    "previous_chain_hash": "953ca1e9ae9de26baa639d9ab1336f27f2ac2077a7931bec12aec9fa6236dc8d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 10,
     "qualifying": true
    },
    "signature": "fa8bb47494d249a95fd4363b54e464a303e2aa3f65416932da5f903f4dec064ea7c06f162864d3fe03e5ed2707f2ff839950016ba35449e68fc35e9d928e940f"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 11,
    "previous_chain_hash": "7fdc638c0d9e067d7940ec94c1f2f7fce016bf50444d06210f8eb0a63ec3320e",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 11,
     "qualifying": true
    },
    "signature": "abbde81b51802f46be668e465e130bcf8abfcfd8d8d10f58c4d450883542048637a0f5de0dee1f70798da6445484d9610027bf5127d2ea42445e322709a0630a"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 12,
    "previous_chain_hash": "b55cc5e167338920a7200b253c65bd1c35d40a08ff80f5d63720703462b4f18e",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 12,
     "qualifying": true
    },
    "signature": "5cff5fedb97e44653e4080ecb48ff6f332430dda8df0db59c65673abd0131ed58a6c14bd289228881221e73b85322cd981724885d5d3cb6ed092dc66390b4805"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 13,
    "previous_chain_hash": "4223067dbb23652ff63ed4d6c9c9e9ce7074550e7e274e4d6a4d8e49c24a539e",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 13,
     "qualifying": true
    },
    "signature": "2daab436adc4e59c6f925545512439da5fe8080b98f911929273f301a2e4828d4425fab3803902815f581f2e55fe44e21af2ba18ec2f8cbcfb96f3e677249504"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 14,
    "previous_chain_hash": "659f467519084d9af384264f2292dfab51bc5d1c4b48f99177c6136c3365401d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 14,
     "qualifying": true
    },
    "signature": "705d968dab22a855a8fc3b5b8526eb4772a2334ca56f3d974242c9936355672fe7575fa28ac7a1d5bcdefda2837091e8c405c45eb7531e2cccc3d5817f9f1607"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 15,
    "previous_chain_hash": "1957ca36b76aacd01c0101764603bfb903e712f660a53afcdf50e54f75b07b41",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 15,
     "qualifying": true
    },
    "signature": "3c38b683f9a7eeccf109236ab19d8a3e52c335c3c91910787178a316a5e328834180ac27c1312e0c0a46f86c583db86e045b1cd9131bf9ac215a57b64c60260a"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 16,
    "previous_chain_hash": "182367b09ef40ed62abd361b7afc770cbb99685a79ada544bdf36bac3b8c6cf5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 16,
     "qualifying": true
    },
    "signature": "2b7c637f85b815b6aac9b61ffb53c2ac2884ae72a72a9d3b71a130af87b97410b82486557b6f8e97ce7f74702f9e3bdf08d49886c48aa2523e92308956dd550b"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 17,
    "previous_chain_hash": "a4f014022c9a153267f24a6125862a25f8588508913e68d61d942980ac4a8609",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 17,
     "qualifying": true
    },
    "signature": "e889d0d5a4b61a3bcf9dc1f42bc304f328cecd6afce691fc4a92fc582e365a6ad0824194d8bcb1170895d4daea76091492400bba38398df353e47c440cbbbb0b"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 18,
    "previous_chain_hash": "c843b0094c3c7e8a83f3bf25067090cd88f366f21bccb193447731b8e59b892a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 18,
     "qualifying": true
    },
    "signature": "e6d94f290a954a12dae6632b1e0c9e6dc7bd7cc28338a1f696bf87bca0cd8010d5bab7417498a57710726b8bb253912a11476cbfeaa4096035209dff0f4e7509"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 19,
    "previous_chain_hash": "45bf343a2cb1f0dd5d6c0b41e46d74a7cd618507c86cbe0c7df921f0fbd9fc02",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 19,
     "qualifying": true
    },
    "signature": "4bbd37a2e78eb3bc4862a689d6a6953f1933e6b80ebd7bb63197653cfc0141894b699c15e816a8628522877bff6ae13d6ae9344dceacce2147101cc958600809"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 20,
    "previous_chain_hash": "fcfe2ce78d51a6b647ee54c6d4e468fe99b9428e87d8a114e25d1b24d2e82833",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 20,
     "qualifying": true
    },
    "signature": "bbc1dc1b21c1dab01139ac288fe294001dcb26cb28909b4426a0db3caa930b83a181331cefd154b70f8a7f405a54198a4e818097382eff49275f2e8bebd9c50c"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 21,
    "previous_chain_hash": "c3e291976dbd23df5ec935b955e11f9b1351e660883cb5a8cd2c47e39870e8a2",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 21,
     "qualifying": true
    },
    "signature": "a478991aa151d8a29e710645e58765958835027663c0fc37e1d875d7c894fdb01a3fea11e0c0179f7bb3215b4036b2df32960fc54cf0829171b29154edb6d305"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 22,
    "previous_chain_hash": "d164746d7d5e323bd7689d1244a7db8c8c7856716e08d47e31bdebd79d11acf1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 22,
     "qualifying": true
    },
    "signature": "24a771a17f39e3404f4f11b3d717fb0d5bee079fc51b59c9589f2bf521fa7df39cac8655493e2ad6d0982b8935a838aadf70b55b3ad6319f8cb92b9674c81303"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 23,
    "previous_chain_hash": "b4d31eebfcc033c03a162c40ac161fe0626e9090c9f39f97cd616ff38d89843d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 23,
     "qualifying": true
    },
    "signature": "5a5ad3380a5569cdd7992de94810fa2258ea5b62d63804110f1729cba31cedff51f75915a5b5eb2152f69d46a6e677f0b02bee31bed4d219b0896959f7376b0e"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 24,
    "previous_chain_hash": "223d2135a6a950b3122560fb1cc73f784ed7dd87090b1cdfa0e00b620f1a429c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 24,
     "qualifying": true
    },
    "signature": "ec5b76dce44f3a7aa28e5a4801f5369131db9fab783d975661e0339c9704f96717e4fe14b1952d0cef18161dfd707482623272036a1068be2a1f07cb03cf5f06"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 25,
    "previous_chain_hash": "483ef73a689c9b2839e82b35ceebf52cb45e2673381cf787ba0154c94af5c9db",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 25,
     "qualifying": true
    },
    "signature": "aef74cb17ea6751a8d703507e5130f8074f405a1fce91176727c377921c13afa79059272d9c14423ac5e5b7e92ea6866052ba0729d1a2d48dc7b49b3eec3d701"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 26,
    "previous_chain_hash": "4d56ae4b2dcfc7c5f05ce8fb7ee2410fddcf9ab8b26721898da74c196c3bab24",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 26,
     "qualifying": true
    },
    "signature": "5947ef278c595051757fd917b256721128e90585293e6ee7ad5556eabde4ed68c2499c1112c7daeb0d674dbb0c087692e752da08397c2c4d61634e1e6ce81605"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 27,
    "previous_chain_hash": "0f13a79c0ef4c97f172ab74b242a54da3e220fcb2289af490e1fd3e7461dd3af",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 27,
     "qualifying": true
    },
    "signature": "1c651dfcceedc74e738804c0c853e05b16a8d7c53a4ca1d66fe74cfe643cde806262c57b4e98ce28ac530b2105cba18dbfc0415b4ef7258c652781b7f423cb02"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 28,
    "previous_chain_hash": "cd624321e82385748d2dbb6b36bfcb23d438e120461725cde4f539640a7c5c7b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 28,
     "qualifying": true
    },
    "signature": "5fae4a2186b1c7aaa6df5378cbb9c64f6b9d3d4959bc9c8c5e54d24351d2ce584e69e8df33edba37f7451680bd45f08b09147005a144faa6f61a19f5ccb8850d"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 29,
    "previous_chain_hash": "90635dd608e89ab739fe43840f1c21cffdf29d8f8948c41bb1258f883b94e6cc",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 29,
     "qualifying": true
    },
    "signature": "08835f051e033041320a849e549de53949553cc2063839b00d1998dbac6d8fc3a0666f133587abcc0e61342dc9f6077a8e14f7f4727ecef049e7ac240a4ee109"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 30,
    "previous_chain_hash": "ed6ec63a84b57b0a1f99b0319ec8bec64fce1f5e75c9331ac8e11b26fbbe2c0b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 30,
     "qualifying": true
    },
    "signature": "775fbfefc48ba164cb24e4fad37f2776d57645eb8904243bd5e819150b445442edbed867e2a086ef65e4c384a1bb9c77c7915864f3edb08e625d13b57a7f8f0f"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 31,
    "previous_chain_hash": "c6ea58540ddac6ee19efda3c5258fe301b2167fa4e1df685faf737056ebcfde4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 31,
     "qualifying": true
    },
    "signature": "4347809e9ace538505147c0914fa10c155a7f36c05647b4fe297ca5d6f4612a2a45582a15c766ab15352060c6c3fb3d0871937c95df7e311bb8017a08f1a1a09"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 32,
    "previous_chain_hash": "a90701e3b032cc27de4d5fa59760c833f123321414aa7b2fb61aae759b3732ed",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 32,
     "qualifying": true
    },
    "signature": "f93761f6abf4792dc84c7b650eedb4ad23d22d4cfadbd25862fb537ee01ba93fe071566ebae5ef9a26e46da352707034a842d7c0e8a7f92709fb9a2e5933710e"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 33,
    "previous_chain_hash": "a41d60b220c8f5fe9c0c3a9f5fc6c9aa35a423098fbe61e670963477bdfc492d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 33,
     "qualifying": true
    },
    "signature": "d0216d54c06af3eec931fbe36b0870d0aa15ca0575051a0fabe120de21708ea2b8ac1df36a644192e87785826438324f144c5032522122bc2dd34892b5eaef05"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 34,
    "previous_chain_hash": "b33eb3e4dc9ecc5ee9e9066d5c2f136a3ba54b68ea227943cb7f3d9b62bbab43",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 34,
     "qualifying": true
    },
    "signature": "db9126a95c0cf8198c5e442da94d57da09de536f550214234fd873cdd5505c87a002af5561d48ddcee4c040b33a023169de1e8c1bab5d2dea026b7ac455e7c00"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 35,
    "previous_chain_hash": "118b08d970d2906228367d8df60cbcb17a3a1ef552337a4afc4e36ba07248d44",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 35,
     "qualifying": true
    },
    "signature": "68130a753a13b43528cea5648489df918fc8be9d378dfacb7bacadaa4a60f7c97f5628342153f2faa9e4925383682f85ccf1a6d647a41925132120b42da9240e"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 36,
    "previous_chain_hash": "27c9a49d7c176223546762519c2b60804a9de9120ee7e92c6f3a627bae2da407",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 36,
     "qualifying": true
    },
    "signature": "c64edfafadb3197bef430cda32d228a42a98d06b8eb2e5f9b9cb436b93338004b4bf48f67dec3c276e20c6aad52e7e034873cb292394432f6ecf83c351175b04"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 37,
    "previous_chain_hash": "bc0904fc22ff764072bc1d6e0a664eb0950b2b4d12d01fa8de28515bbdf87616",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 37,
     "qualifying": true
    },
    "signature": "f5b96efd85d11ea4de34d81d8bf3d06dc48caac5d7f4365a4cb33447802edd95f203264e34040c02ddc1bb3c8a0c5669c75e4b649e84c38309bc9274486d9701"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 38,
    "previous_chain_hash": "7fb2554942a8c594eace1e2926e666fed26dec3cfd11b257d4413bd466732514",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 38,
     "qualifying": true
    },
    "signature": "42a6b27273757982c1c796b8e33824138045fc7e91e5777c76232cc81d18998df15e8a4e4832fb9acc5b901a52c4b678808a9ab02075e960b5f7e374e3a03b0f"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 39,
    "previous_chain_hash": "ccb95a313f584dac0968d172db5ce6620df99e241416ecccab05d9feecbaa57a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 39,
     "qualifying": true
    },
    "signature": "3d4d79d98ff65e8c04829148aded84da6974fce7bc8be3d7bd3a600df3072437223527c8c31a52f186a31c8dbafa4be85fd423a6bc5d23c9dcff864a98b60103"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 40,
    "previous_chain_hash": "e516bd298a8a47ef67de08ac2b2384ee607fa0389047be877e8b0bec32717aab",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 40,
     "qualifying": true
    },
    "signature": "47e4d5c8a95a5c04403bc739023525bd8c611b8d5b5fb559b907d1aeb951cd8475dcdad848a343ebd31193b982c1a5fb95568317866c578e814c179b42a5ad01"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 41,
    "previous_chain_hash": "6fb95977eceb13bc9204d2b759b3890bf588fa3b88e7c4699d71829ecda0cfcb",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 41,
     "qualifying": true
    },
    "signature": "209cc0659d122a9c922f418c4fc7b4a403ae1b42483049201545076e161b88e287f84974490688a214cb724bc376aa378925383f111a5f5794201f455cf10d01"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 42,
    "previous_chain_hash": "8418919e28268df1d4e7d1434e74f5dd2a1057c5e14c9da0af5d9673ec07eb65",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 42,
     "qualifying": true
    },
    "signature": "ec5b2a77e4eb19ddd0c359c25e60a686ca2db6c5fb2f675929d8fe871ef7e67bcc039591eaf788eda69c10bc4814e5432433dbd84906cd99b7162b79a63ffb0f"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 43,
    "previous_chain_hash": "5deaed454c3a3776c57cdfd48e723d03a704acc66e57fd4ecfc563b916142c49",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 43,
     "qualifying": true
    },
    "signature": "8668663bd4c39fad3fc3a902d5f4d011a0f4b983c584100fcb189ab69e9143f0b9c9e769b0f1ddef57d4059873bd9dc26e80284b26205a343992d3ac8b0fbd02"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 44,
    "previous_chain_hash": "adbda5c938b5329e53f23a42ede46f65de54fb433513c4ca4653ef483a0a17a9",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 44,
     "qualifying": true
    },
    "signature": "e5f891e5a1207631ed4f21689c2063e144e765ff3b18741d260b310bbded4b0dea36b7d93d10084e16b6f343c6e23078fb711fb08649d8788f86bdc7b70d2a01"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 45,
    "previous_chain_hash": "117cd749f8438a12a74ff198e16f7de9fd450283f5bde09310f20afb3ac14b9b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 45,
     "qualifying": true
    },
    "signature": "31e5cc94eb159e1e820c604c36453cdb7883d66ff403e319543640e637f684d575c89bc7288c47dc609a04eb00b38eb949945a7f7360736b2ea7eef4be7c0903"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 46,
    "previous_chain_hash": "dcc2992db995a9da7a0f836777340af086e36e440e5714e06a68196213e387c4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 46,
     "qualifying": true
    },
    "signature": "4adc453898b38c468101291734b1105f2da85c786d6d5a6b947b165a91e133bea3fb05757d22424c821531b6314c92c43b6bb17fde32dde8782a0daac8014c07"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 47,
    "previous_chain_hash": "1f6e13010c0a9c010408afab2a78ad8fe193f0c03c7e382060e1feb770985603",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 47,
     "qualifying": true
    },
    "signature": "4dfd7ccf0fd17ee58613a8944d3ff795e7c1c3686d5746a33be3a2a388ebe38c526edab36937142237ad26a306d2e1f4e441645e84280e8d7eca0d35021db008"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 48,
    "previous_chain_hash": "30b4cc10e8e92e9c109e6c3b13545368b65cd5e6fa6073ac219811e91d68eb36",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 48,
     "qualifying": true
    },
    "signature": "1f3d7c468ad4fd50c228ee964f76f6a159fbbcdb443c84bf871180e40c11da81159d6f83629a65c810b3466bbe0da76d85f4b5da0466bd62948f9aa0be857f03"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 49,
    "previous_chain_hash": "6d42818b8630410dbf8c858e09f0e03e707def4a1f4005689c50325245ef0b38",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 49,
     "qualifying": true
    },
    "signature": "d40548a3429002bc42e73b6b072f837310ed2bdba6761ca03ce647e910f709d8fc37bb4ca0e310c8625cbc0c1a18faa10d8dfd27db0b3fc66de32db21f3d1605"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 50,
    "previous_chain_hash": "c4e924ee9d2aa0fd50986303e871aca91d2125d699af9b0f66e4d640430e1d70",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 50,
     "qualifying": true
    },
    "signature": "76d5241e7501a736cfd2c9e912579831851997a79e01c2a81eff5af3fc3d34ef1ca4e00a9a953794c0545229a5332432815a9295f707cef693987a6993ceea0e"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 51,
    "previous_chain_hash": "e12f451fb547a25c4429108e7c585d1f805e7da127d1cf3c72baa90eb64faba9",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 51,
     "qualifying": true
    },
    "signature": "389b9852e0120e4de981da8a96350b6d631db5a79096124ee2374732ba70821d237931f577d3dafcfb9eb84e0629a7d62affccf515e433dc8459655841a8f008"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 52,
    "previous_chain_hash": "984d82b55528e41efb4b8172aad1b63b8c873e14d6903deedd2653fc8376f734",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 52,
     "qualifying": true
    },
    "signature": "43c953e3579e063d445b9d0a722a75f84aca9a0211fea04bfb7acbc7f0e7cdf124a1e43be25c825a0d72912b275dfeb9b728ff7caf1206a4fb36b215b92b8701"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 53,
    "previous_chain_hash": "7902705cde3f8b0313f5cf0d89a909f49ce73c0d87efc017e727f3747afd253a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 53,
     "qualifying": true
    },
    "signature": "faea2dc19a3166da9edb807a2103b98c01302c141c1d95e52cca34b1b108261d407e0d6cd58b8a6199563043f3f18eb930faa6d06e042367df37dc5299bc840a"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 54,
    "previous_chain_hash": "2c1e4785c30e7172b98e747acc0c7b3efd1ec549caea0b19d441001fc5c7adb2",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 54,
     "qualifying": true
    },
    "signature": "b75b8a2401fe1ac732b6bdad3651a568a28037dfa1c54807217cc18345468bdbfd9e8287f5760ac9acedcc8e634acd28b541bd5aeb69e89f47176e3615423305"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 55,
    "previous_chain_hash": "cda0c57761861c91a24b07e598f67571292bd48f7f46ff6e7b5d223af7d427cf",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 55,
     "qualifying": true
    },
    "signature": "c3b8785fdfa18ecb8ffa2f7e9b523cd2832bc9a284796997b90c6e04e29ce7833ffe7e4924d93f9b79b18460239b866e2b1d3f9d259ce0fc6b01756f546a620b"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 56,
    "previous_chain_hash": "a1794b00fc9849e71919d877ccdc9cec2e67cd020e6d02c8d8905441fdbc3ba7",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 56,
     "qualifying": true
    },
    "signature": "a345539d998a4ff0f906717f4f3bf132aaf29dbb7f6453cc3ab72e0a289786c0fe7493be8fe7ed4d6be221b69ba401b673c0c24cba075e928ec75bebeba89f04"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 57,
    "previous_chain_hash": "c1f457a45008d1ab638fc07f0e679ec263753214c50e3220a37a014cc9de367a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 57,
     "qualifying": true
    },
    "signature": "ddc20c87052f6444cd921bd4efe6ac9ec47833770c5bc6c9b3956a695a109ce6be01e1233e0fdf7a673f8328c92a12dbc7a578a424f344a7384956f5d6ae1c02"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 58,
    "previous_chain_hash": "425053546418c1480ef1042a0238d77084beef6f8aa3a05c5573a586401446fc",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 58,
     "qualifying": true
    },
    "signature": "1c321772a8d8f3f2c4712c35aaa4aef6261eefe242f85427149b0104210c75a047ebfae91ab56f45b7d2bac13190e2e73e255f30145267f510838e0b1fb83907"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 59,
    "previous_chain_hash": "876fff08b04bbc9a630093c87e24e6e67fc0669234e5c9f8b37c6223e32ddf2e",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 59,
     "qualifying": true
    },
    "signature": "e0e03c9c151feb75a3f1f123d648191f5b1a6a062e6b64ec7fb83ca48fab8748aa09ed6f6988d9085600266c339d01d17f627c276780682dc347433f4effe307"
   },
   {
    "commitment_id": "cid.R4-B.realized",
    "pre_run_commitment_sha256": "6474916ddd90108ee4d901bf736be685727556be17793c16c42e527b70678496",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R4-B",
    "universe_id": "u.r4b.phaseb-injections",
    "run_id": "run.R4-B",
    "sequence": 60,
    "previous_chain_hash": "16f80e6c89f55148ec182b9bb389ae49e26a39ad83ea88d51906bc5d4593c4bc",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 60,
     "qualifying": true
    },
    "signature": "7eedaaedc8f5481474c454a55ab10adb0428ba6e832e62eacbd6a9a1f68b41e87ba1a391f10516ec41c0d749d81dcf175f4c48091bffc7ce28d932904937d507"
   }
  ],
  "cid.R6-B.realized": [
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 1,
    "previous_chain_hash": "6d2fba1a57c7aa33cfe144017fb282d391525e04015cd245f3d67ea5cbb7d2bf",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 1,
     "qualifying": true
    },
    "signature": "73c99cec1184207577c75a11d8bf1e1b9a8a6bf9a17c8c77771fa862a9223a4307659019c7063491180bb15602dfc41f8973c5023488ed8b8127d5f1fd1ba805"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 2,
    "previous_chain_hash": "7fe33e30b89f884cda069a1b9f93c68f02ce3376203e3f6ac9d2bb8200b83216",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 2,
     "qualifying": true
    },
    "signature": "d9939e8c8da37bbc0809c24b85559ae44c72acf1007768e515dfc9bd955990ba145a1d4265c5f476b98429f270d67be8e203d87c70adf66e33c7b888e6dbb802"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 3,
    "previous_chain_hash": "8fafa253d3e9bd0ecdf1bd4b131a6c132e904f7ced76a78215b05f749a239602",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 3,
     "qualifying": true
    },
    "signature": "f23a34cf62020570c81baa5125c3bfcb7710e8fc596b5e7d72f3f5c44d1d43cbe8830ea983c526557c5741c8407f94c9389b4e3eec746dd76c14441dead25c02"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 4,
    "previous_chain_hash": "538e5057a544953d26ff6de9f2b260b826476a2cd103349ee4ea03750a7da52b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 4,
     "qualifying": true
    },
    "signature": "ffdb0e1aeb41e8311d61b390b8bf5a48dcdc64f1d1c4b066d04933ae56099c014e492bd0de783bc9081cfbe97f6485c2ad09947acb5ce572141d777ae50eb007"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 5,
    "previous_chain_hash": "b9fa3f089a9f9ca75ef80e986c6299821553d109146640ece33e76ba9bc3ea9a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 5,
     "qualifying": true
    },
    "signature": "fdea632eb23c2a72e50b23fd558f78fec6a82611069b4bf8f6781bf5df7e44f8b97d46310a11cdbaa2f50b2a7c7f0c093882ad04cfc89a6c2a2c4e6e19b06b00"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 6,
    "previous_chain_hash": "3ba5ba8ec551e2497e1a75ae3e81280fd3bedbd45649009144bee2d6579990f8",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 6,
     "qualifying": true
    },
    "signature": "ac00d208dbf1e42d96b5beefce8bed15ccb9ed441fff91474e3c49daef92230b1ebe56cfbc83e53eabf08bfac955839f4273ca11bae3020e74dcb9103dc9f50d"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 7,
    "previous_chain_hash": "16f0221f609bc8e502ff4869952c1738e9bf592acf2c61f3f8f033ac05441886",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 7,
     "qualifying": true
    },
    "signature": "8606e77933073a4ef93bb97eab2c83b958396e6958b40df43410c5ca354d0d8bb7665b3ac487cd2111db81db057000f4b3a62918e59d4d478602f9bfab735d0b"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 8,
    "previous_chain_hash": "68e27bd8b7e1fed928da4e234a3f8292faa77be0ee64bf878fb3a28f8b065937",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 8,
     "qualifying": true
    },
    "signature": "f8cbb39244372e62c7e8507db71e788ffda1c9e182136bbf48c7bb23e6da3f3ce2fdd63221c980bd83d2bfe455f686aa4b5594d1f782f8404f275bdcb6edc50c"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 9,
    "previous_chain_hash": "648f1c05f739cc18940234e0624113cc5bef31ab1b3e90da2cd691b068c7cc07",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 9,
     "qualifying": true
    },
    "signature": "01d88397c8bd03f5898f90a87700323f76100edeab932025d5c2836dea369162a3e84e04fa85188454221a38ef3b92bf214a1a50e0c9e6241fc9fa4c54ad4400"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 10,
    "previous_chain_hash": "db3af1e8a858d9e6d566afd5eeb7333489b60f4006977092d1d1dbd4df7647fa",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 10,
     "qualifying": true
    },
    "signature": "958c15c456c06d0b88bc600e19e00f1b076682dadaf8422b816d67d07b163d073526044654b09106740a6c57d410f90a76b9a03f5956dbd4803c12bd9c59f300"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 11,
    "previous_chain_hash": "38b36056106812a5e0875ad603915e23cf3c171c6ba6de1600fb2e05052e0c6c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 11,
     "qualifying": true
    },
    "signature": "6c22816510ec1c34077805a6ee329424c43a8d727c1e080d2cf683e0ce1834d25515b0b86825b7daa464ddebdc688e738189db5ac673c84f3db2abcd86c8b907"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 12,
    "previous_chain_hash": "7f82d4594c5a6a9e9eda62f0fae043835cab2a0d9d97f1fa94d9b0d3c65bc903",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 12,
     "qualifying": true
    },
    "signature": "188c57ceda74f5f616be3b8ac2b89623aa1df2aeb5a941b6912bbf3c55a6c75394581e2a8c18d0a974031af8bf271f2302a1f6a9f67479acb8911b36e212d60a"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 13,
    "previous_chain_hash": "4d0fb0eff79ee75a1be7ac86bdb1d77fe5fc675c47fd7bdd7e8bdd12ffeaaccc",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 13,
     "qualifying": true
    },
    "signature": "d3808009953835bd80bea52b8703f735f42a71b48a79681c8333ee572cbd5fcac1896f7cb8647f1772bc58a323a2ea307e44aab425a5792761985c519dfd7203"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 14,
    "previous_chain_hash": "649c53ecd3db98e15722edc70c2f2abb68a6654d94bec43398d7d3950a70110f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 14,
     "qualifying": true
    },
    "signature": "6056c87e2e1eb3ece1f8baaf057992534b0fa33924948d5019ab6b4b54d0924268eebc56757a40aafba38094c562691bc796c0ecc560e149c726794eeb377907"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 15,
    "previous_chain_hash": "a260a1996b76a2ba9c3ec1b35ec5feffdcc3743c335fe8d5519ee83141bca524",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 15,
     "qualifying": true
    },
    "signature": "31aebebcfd4ac5863fb45b7415a7b614f4fd43fea03bcf03a11a4db71610670b28d531e10763ee33462e7ae39d3ed9c5efc84ae72b97346684f45502fd1b0d0b"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 16,
    "previous_chain_hash": "b4aabd23946ad105c00c3e288a6f945260eab0ec3f1b48b691a9224d36846390",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 16,
     "qualifying": true
    },
    "signature": "781d472da781e2c7a4b2986fa36c9514124c08d1b4ca53f5a8163deac378a1851bf273a20c54653cda0ed2458155d4d6c274b8f6b26b93819339d09d817f730b"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 17,
    "previous_chain_hash": "efc661df65768d270ffef1fbd7b2b9849a21adc97846d92ef5de7bd2bbb8ed5a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 17,
     "qualifying": true
    },
    "signature": "44ab0088a1251df791fc9733660807da1c7aef68a1c92b0a8ceee7437b10a60fc48be14c99af33ec7c0c519fc85a2df58dfce2edaf1f5f853946ee9acaa9520a"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 18,
    "previous_chain_hash": "e9012b2b8fd6872f42d04878c87a1fbd95323b364cc0f856c563457d7f7794a1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 18,
     "qualifying": true
    },
    "signature": "f43fdc5e60fc681dc0998835f56107b35ac90cdc2dcaca9afbf4d679ec353ef09e78498b1fc4c7ac272c18ae08a3e07dc579e3a980902b288ba87f939c115f07"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 19,
    "previous_chain_hash": "2f6325318ccdc925e67697dec102d4c09cd32a00597a2f7ffbb400a5d4397b5c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 19,
     "qualifying": true
    },
    "signature": "48919da6f9fbef8f98f65e02f3846e5e4ce4a722b5fc81bd838a9584e6714c46751a8ca5232847337c0693b8ddaa8020bd36bd362a84980120ea78c41b3c6606"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 20,
    "previous_chain_hash": "af7b775d26e4be9f92542732e8f3b40a822fa761e1c87225e62e336d544759af",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 20,
     "qualifying": true
    },
    "signature": "0fe6d3c100ec3d58d73cfa5cfbd5068854994946d16100711803c694f97e3afa9315bdc2b7e7812db25d82b6f5fe7e8d6e12eb0028ee51cc2ccc50c061d5120d"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 21,
    "previous_chain_hash": "d064577f762adfad106f070a3e2f991028d53345c5cb13d3b286c75569070592",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 21,
     "qualifying": true
    },
    "signature": "7fde595f2188b3b08ef522ffb382758b011f5b94f9de7b37d693fef0f778c1621e771382d4a92b4011f30997aadb565cc8d823a1c265dd9c1e91bc78d7c1d504"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 22,
    "previous_chain_hash": "4a87c335fef175e5fb269e7f45ed5f7b593bfaf7ef10a33b9275209316edbd4c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 22,
     "qualifying": true
    },
    "signature": "595db10ce7f152e3a30e2d71f1d98243a0a39fc7c28e398e0a27bed2d73d2b59ee0e274eeb36ac22b99895d0323c101a7d89a076a3b48b9ab13dbecd50292300"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 23,
    "previous_chain_hash": "121624fdc69525ecea35373faea425b5e11e08ed09e04f2a3ebc927a9f56d4ce",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 23,
     "qualifying": true
    },
    "signature": "0ce4a327c27201c076c77452c09ba56a191de1506999fb3dbcd87bcb89ec3fc736490090a02e6a3298c0402d2fa2b4e941f7dbb1d8e078db4e86f3a98b75c806"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 24,
    "previous_chain_hash": "6fe5c9e6145c08afac05c0036d2f6c6c8677b9d4e746ba720e815e8cf6741e05",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 24,
     "qualifying": true
    },
    "signature": "d74b9cb52c1342bb082923ba62310a589b54a01d2b37cbbced19d812540d814e86a32b9cfd39e866c3460eedf66392e6e34d41cc3d502d707ea3d0e14a696308"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 25,
    "previous_chain_hash": "8e4792bc4460517e0c45bc0512b3c838e2b656f39f1746cc3affbda5bd3b01c0",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 25,
     "qualifying": true
    },
    "signature": "9028d1631547df11d0047c6886541f152c4f7cdc554fce25260ef9739a3077d2d020316e6423daa1792c44a71172cf3a1f1210049dad21a56bb7a7d814b8ac01"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 26,
    "previous_chain_hash": "74a64f44b7fc8c58e3ff8c05045d0dac6ed95bd7ca8a5eaf9b3560adaee9f89d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 26,
     "qualifying": true
    },
    "signature": "1b24542019e79351f70985fcfab35ece3993eacecb9178186ba728b8478f64607b9112b185d32fdab12d97dac22ae400dc725c352b895fa2acd539e8ab09e107"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 27,
    "previous_chain_hash": "3fff0163f071c76af13bd979dceaf63fcfb736ccf2c080f56221a7b5a65c099b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 27,
     "qualifying": true
    },
    "signature": "a0f75e75304391c69e24da9f5b00f9c94e25f4c13d7d404976d4ce9723806af33da78a5ce769ede7e5632edb9070b7817f5ae2c4656a1572120c4fef9724880d"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 28,
    "previous_chain_hash": "ffecbaa8f88efff87959418ca6770ca62f46339b449e535e81b221053aaeec0c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 28,
     "qualifying": true
    },
    "signature": "a54e0640b5a647463b78aa3a0b99b76b6a6ba4f0b247c3bc43a9c42e132f35463b583c4f3a83d85e6913d312cd3ef990360758302b2108a5b6b9dfb211563803"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 29,
    "previous_chain_hash": "4c2ddca71e49c321e2708970fedc2aef3c36ec1750eaac9d0005647d8a935548",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 29,
     "qualifying": true
    },
    "signature": "887ec74b27d97b92dc404afd3695bfc7f9930151f648304b75917f15a1928d195aa071e8dcbdb9b9565117b8fad4358b1dc838bf48a68445ff7da149f55f3309"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 30,
    "previous_chain_hash": "5f509047269fb5bcc8d852d601dacf10d1d25d77b588dbae324e4fb207f088fb",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 30,
     "qualifying": true
    },
    "signature": "4f83055fe393f487306876e14fcd59111d90b5b6bc83df160589edfdce519ca19fc714055813109ee978f401178b3ecee6a851ab2d90dfdeda57ed727a5b4f0a"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 31,
    "previous_chain_hash": "408a61b759bd8fbccce2c8c141587fe607922527a442571d505685f21d7c6ded",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 31,
     "qualifying": true
    },
    "signature": "85a83a60c90f2be71ecdeb92f35be350d61d074a44e59ec771273f7ca676a2211dc159650f8fd740bce22d325fc35a863826b2cf2ab690c4e3a08d4ecb1e6804"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 32,
    "previous_chain_hash": "fbc9a01e71fe0b0493a76019ffce84c868e16c426d68c4706b805e3be54b0d92",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 32,
     "qualifying": true
    },
    "signature": "5d541c5aa8ff230075b390a357c5746f63d5425f3d663a166abf389def6658b86f5900ad8cdd5db4dfd8f296bdcd02c04864753dae3b49262abab9532f51260d"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 33,
    "previous_chain_hash": "6db4945edf3661398da1580f43d86319c9bc6bea0739a97bf4a52e34d47fda5a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 33,
     "qualifying": true
    },
    "signature": "46d2770c12a7387c73c49bc2d43ac29be2b72b0b5784d0ed6e4411bfe504860932c431b370e98b1dc84adfa632443d29a0d5590e51006c32aa3f643692a68d06"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 34,
    "previous_chain_hash": "cd9c7b73766e9e7c52adf354f1734ea135bc1be440ef15deac335fc4d933dfc2",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 34,
     "qualifying": true
    },
    "signature": "71d79b0322ed6a217e0509719dbf82ac0d880977fb2d0065279731a2a93a3b5f5432bb0439e964249f8141f4408e3167ae53424f3cb72549f8ec224a38b25d03"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 35,
    "previous_chain_hash": "80300fd2198d0c2d09bf1980166377b41c154094823a2bf3e25b0104953884e4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 35,
     "qualifying": true
    },
    "signature": "93418cdda17b03b96845a85fe3248117eecfb0666f7d9cac279adce7e919db1207d3c4340a923aacad585f01a9468ce250e73784be90993015c81833b319e005"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 36,
    "previous_chain_hash": "7e03c75f68b0429c228018500ebe5118eee82e83a50c047f5cc68ffa933acb43",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 36,
     "qualifying": true
    },
    "signature": "2d3d6d57a2ba4b6d8e66e006224eb2fd3f4771a1328964e7ae31aa376fbe504225d2105fa5f731d42b1655c0c42d136c9eebb69c01492e750660f9124ec6d00d"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 37,
    "previous_chain_hash": "7fe50bf72fc601bfc7d0d02f09c7c4f1988477f8b77a0b9d086ecd4e3df79470",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 37,
     "qualifying": true
    },
    "signature": "dea595c8306495de636c59cd8dae0c1460d2b0e859cdbaa7db33606c9079c76570c7830f087707abfe3a1fb1760214232ad28b03020478251f0f77b807fbb401"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 38,
    "previous_chain_hash": "8cba8fbaf90f626a8945e8c51276ef24880c1be016e8be727ec16587b7bd9927",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 38,
     "qualifying": true
    },
    "signature": "585805b20837d74886851f4515a085095d9b58a70309ca43f636ad1dd73256ec6976dc55fda4fb264f3fc91be7e2fe4b02c4e37d398a877652da1df368796f00"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 39,
    "previous_chain_hash": "97ccd764447abfc40fa09d531272c0985de8982481fb36f7347554a23eb1c280",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 39,
     "qualifying": true
    },
    "signature": "06ac938bae3f132a7ef3615abb1c0bc16c671f5888e6fb7ec1ec9e69444103504703b696ee25d31267694d3622e498c4dbf77d1051caa0041e1312b92f82200c"
   },
   {
    "commitment_id": "cid.R6-B.realized",
    "pre_run_commitment_sha256": "fd7eb7657634ba95555a0ad02451c28d832abdc95a572068f06ee355975702a3",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-B",
    "universe_id": "u.r6b.receipts-run",
    "run_id": "run.R6-B",
    "sequence": 40,
    "previous_chain_hash": "bf0f50054a8a9bfe0c590a39a797a3dad40b481d20c0adacbfd42a7cc8d3e7d6",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 40,
     "qualifying": true
    },
    "signature": "2fd0726cbdbb00b15f69fc68a4d145da1dae69c45fd3e0047bb9ec3e78c0e50893dbcd70f80109311035bcd3c57dc74a93ab6f39aa909ec46e857bf183147f0d"
   }
  ],
  "cid.R6-C.realized": [
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 1,
    "previous_chain_hash": "1ec5a068bc6a06f52b5cc7e435dceffb37e858dfb9aba7dca6f5e1401d1cb0ca",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 1,
     "qualifying": true
    },
    "signature": "db98205251c0c08247e46536763c93d835eca950ba53e4a40420daa477979d53ea5fd7a2fea69ee5205ae05eb219a3edc181e7f5dd34fe6452facf08b5d66902"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 2,
    "previous_chain_hash": "87f3422ea110fee3d3c2b0147c39c004950e0668463e8697e20d6f2362ee77a5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 2,
     "qualifying": true
    },
    "signature": "c8a90fda178d3e0eeb0632ca73afec08e563b94c9b1e5fecfd583fcad8106f38c6ec37bcaf7b0d0f55b9ada2bf2f890b3aa3e4db66bd0ba2c539e6f163f3d90c"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 3,
    "previous_chain_hash": "684dd25ecd3f4bef6a3aa4771d4893c44b1b3dc8fe571980dc7703c2af73b367",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 3,
     "qualifying": true
    },
    "signature": "aff0d2e13f01f71ca679c42b6b6e0a7749c8493129fa836b9e466aed23284bd839822f5f8d776c0f76180334adf8745d6e4b276127a77a3fa4657a7f5ceeca02"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 4,
    "previous_chain_hash": "8a92cefbdb80340e4a104808eea4444c58728b41d9a19739816ec7ce57eb3393",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 4,
     "qualifying": true
    },
    "signature": "14a4113e13130ce41a9ab98f91b92184acf74eec35ed63581704d8a3a35e987ccb7a197800c27993e9af8eac681effc346303fab7c079d59f505b7d682eb9706"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 5,
    "previous_chain_hash": "5870b7ad80a08fbe7873f1866c8377b7ec750457a086a1e49dc3f80e095c055c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 5,
     "qualifying": true
    },
    "signature": "591fcb71bde65cfa319c192ef951e78bccfb24e5f5ab88e761442e39dc909b64aaed0b18954ac753ec41c2f796f2a61a7eae064c152d0d6534859d83c490ea0c"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 6,
    "previous_chain_hash": "f7f4fa22170ad5dbf82eb60173206c5d4c0e9376cf5355a98ff5c73660392d86",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 6,
     "qualifying": true
    },
    "signature": "f91b64c6c93677d671334ed2f58a2f0306e1d8ba1453cd73b67a273647ab91cb42998b6af2a64b6f258a870094f45121b7b13932cb630d8979c4e67aed29a709"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 7,
    "previous_chain_hash": "e078f3ab1b199d86210d2421904557b3f2be5327fe8d9a3b0e9edfe0a4f778f1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 7,
     "qualifying": true
    },
    "signature": "70d8dedd16fa19630f0b6609f93807cdeb3f32ef7ff141b2f6ca967a97c7c77f4f314ff73f1ff45838456ef5d6abe5f76872b8bcd58ae0e1d2a31a4da050e000"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 8,
    "previous_chain_hash": "fdfb7a7f88d7971d5173fafbcc01b24ba45fe3670a9d7e2f53006c2c701a3ba1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 8,
     "qualifying": true
    },
    "signature": "0e6900c903772a0274b435dcd6987590dfe4b6544521a952215ca8c078d2df59fa92b5cbf19a50f9ff496fe60cbda1b3695c47ffc84cbe90ef6b158150124f0d"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 9,
    "previous_chain_hash": "23341520319f356353db7f718653ea0f42f9d61c680331407448fb7caff4347e",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 9,
     "qualifying": true
    },
    "signature": "8821e2da388b7fe32fba3aaa58db54feb790f954435911fd4700ba6a7234907223fc2932e422219137060f59a191c4a549590ca30910d5bd8c49c9dc9e27eb08"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 10,
    "previous_chain_hash": "f2fcb7c6b3af1eb31deb748134c7bb618e66f28c1ca9c3ff06102b5734ee6f38",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 10,
     "qualifying": true
    },
    "signature": "2df4bb570147d8bc254f218d83511674107f96f230ab3b2f1a32f92acbde91042ba69988fb88b4894d11a8a5241b60b2bdcf3133359f9972bebd1a55b974f204"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 11,
    "previous_chain_hash": "1df39eb1bc699337a919709261923a733039513389fa8542bfa5d575874eb6ec",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 11,
     "qualifying": true
    },
    "signature": "2823d56d062f0191232ac317cbe8e419fa2f3752891aa0e6e2bacb2156f64c56d1acda6aaa56db939ee2efb3108c6d772e2ea5775fa3019bd811c320f8f13e08"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 12,
    "previous_chain_hash": "9fa95e81698818e9cbd420b5dd71ede36c7572e839519304903414bcbb689ddd",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 12,
     "qualifying": true
    },
    "signature": "87897105ba988e6655ef31c6f5fbf13943e78a03039fb8ef618de81882fc08d5fe3ddfa779a2b1bfaf1e9726f82ac4a93b8c64371ccba2b36dcc86017e39b305"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 13,
    "previous_chain_hash": "936b292e37db70f11604331ed0a9d3ba936e9ba32cf1407ee5d1d696b6ced458",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 13,
     "qualifying": true
    },
    "signature": "6922c07c5b66bea4f0f17a5e3ace1c0ae360bbd553590a4c836bef4f07ca4a01cc222aead0a922a08f2c55078340af6a94ccf51c9f7885ec59ba3d430d30c408"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 14,
    "previous_chain_hash": "01dfbd2a6821729a1348da965ec0e79155cb80ec425b876f4ad14f616498008a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 14,
     "qualifying": true
    },
    "signature": "0631133934b27d8910e32b4111a09c2144971fc782568c816d6fef9cc044673af24e8948c913aad2bf3dff8e858a1117de46db51b79842b9c95d0f3e0d9dfd0e"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 15,
    "previous_chain_hash": "c20e5764bd649eded450ee1b6ebe3e9082f449fadd2f5c0a5d89ea7750088006",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 15,
     "qualifying": true
    },
    "signature": "9f5bcb81d812f4c7b9395a15e46256e9276a55fd247ee6d9e3ab4a8a08f7e7eceee0235aa29b8285da7d29dd26b94c66486d56213ece2ff70fb2037443b97d0a"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 16,
    "previous_chain_hash": "d0655eb929fb34f37c274637492434abc5b54d1f7b253ca60a68bbf6b1b451b3",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 16,
     "qualifying": true
    },
    "signature": "07302a132041e2feaff355eeb5156c2494753ac652762628a7a5bbb88a7895c91227edda698cfe62efbeddf036354f153575efd4918d1c2aa402eb675ccf5f07"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 17,
    "previous_chain_hash": "ac6918fe4bd27bc34e0d3cd966f6204ff0af6029c34ae6ff5dbecd206fe62be6",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 17,
     "qualifying": true
    },
    "signature": "e5fcfcd88e28305ff79ed95c75169b00559abdebc3ecedb9c1c32ec43af198c9686c25db8eeaedb74a972e548fa6d177a102184206877dff39a9838f8fd6aa0a"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 18,
    "previous_chain_hash": "5ad397c1e9f65621ed23057ad5aee1cf3b1deb7c19d8bf2583b113cef8ae1448",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 18,
     "qualifying": true
    },
    "signature": "c13d86b333dcd356d9c7846ee07c37aa5a95597ffcdd11cea160194f644b8d23724dee03ce7ec6420f41c13e8095290198ba8d56a1868bdf6911f7888181c90c"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 19,
    "previous_chain_hash": "d8bdaea1230aff846b27db5b15d85f25f392a7c49d6f2c6f3b2c1ae71af7161d",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 19,
     "qualifying": true
    },
    "signature": "9efb5110c483b1e2b286b6228e8c8a5487d110d468bd1529d5696aaeb33de632f12bb48779757815b89ebbd6989a60884f14b37d5fc5181eb04ee4dee7985d0f"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 20,
    "previous_chain_hash": "1f6c59ca11e51323779dc9ec2f9b513eb090d194679a8429200d420fcf87a1bb",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 20,
     "qualifying": true
    },
    "signature": "30cd7a8eb5b0e963539a2da27225807573d18796ff456faa0130826219b9592e5dc61860c7c1f40ac09f02ce4f7e77c0ce09373c65e994cbe0e26473c4a38a0f"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 21,
    "previous_chain_hash": "eb5983f307f03bda0a471d9fd03d53f0891ad857352800220cfc82eb8c4bad8a",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 21,
     "qualifying": true
    },
    "signature": "f3072124377042fc7e2df87ab6571b4feed427e2d9a3b0dbc4a0b80291d2168f52879d5f7f7acfe6ec2f4bdbf054c356e0e62a2e1b42cbd38ea572b5304a3a03"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 22,
    "previous_chain_hash": "0f148c5a0d65c7b502e9dde619baf1540408c43879979ffaaa26bfa58fadcc1f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 22,
     "qualifying": true
    },
    "signature": "24c5aa4dce6667ecee3ddc38a01f65b186180e67e3607e3e8dcdca8f225e774d9ce63fafa1d3c55a87ab277664a4f8e563512ecc6a302baaa5afc9458fcd1700"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 23,
    "previous_chain_hash": "04e4e63a0ff158dd4b40d3d491e596318791464754dbb77251e49167d57e918b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 23,
     "qualifying": true
    },
    "signature": "3275c282e9fc538e34814b7eb3ff482db3ae109f1c14f52a11936fe0dbec701e39b500802c911dbdf998704678a54df3a11eaa0285187569fb33a82b0c2c1004"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 24,
    "previous_chain_hash": "2c6843b1377c586ef6e367b96c4946b76129e2cd192186b7fa3bcdfcb9d5fed4",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 24,
     "qualifying": true
    },
    "signature": "e5dbf3e1a71efc894454c56848cd842d3e258ce0a863750e1e2c5e1121e0406aeb6acdcdfa9b85184d2fef63086a6e5d5134cada47f3772ea0d9d1c3aed1490f"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 25,
    "previous_chain_hash": "77f81f40e9502b254c9609586ed44831553e80caf19717e3e9a9e07accd4e368",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 25,
     "qualifying": true
    },
    "signature": "04c182d1cf5ae3d55515b25ea88f7bd137f12f160ec861585b324a3ff14d92899a46af33ddc8bb3edd9fe3ea5f955ab9a3bcaf58237d090a669b37eb60e74c04"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 26,
    "previous_chain_hash": "2c7e80157c2aba4870bdfd9735dffe099de257836824186397038284b093e70b",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 26,
     "qualifying": true
    },
    "signature": "9b0bb9927813298bb0b3d1a87e00470bc8899a857a077076aae6435623ccba4b198a824c253eff5edf9aa7184896f66d0bda1e27538649653e83971d3f279805"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 27,
    "previous_chain_hash": "5a890de58798ce0e810b1a77aac1ed77c4531295cee585a334b023c71115870f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 27,
     "qualifying": true
    },
    "signature": "5a520554c78708a9095eac43a839fa8fb3c109c31ca6bf9a032672cb7f146b0768b9048694e542c8f447da91f5951ede7f1f1583adcd950ab248723279dc3f09"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 28,
    "previous_chain_hash": "8d00a27522e64560a8a9f51e2110ac054b57e3e08d51b384f56e681fcd37f2ee",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 28,
     "qualifying": true
    },
    "signature": "c358e0d102d5a5a688e89afe324d5cb485360521f04003873c009ced6ebaa7e4da384c0201b0a0c4cb4f7b7a731c4fab4299c3c97bc8dad0af4b99f01a62a701"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 29,
    "previous_chain_hash": "0c4f156dd13bae5cff029b685e07860325aea7bbf5b779aee90bb6017d1bd41c",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 29,
     "qualifying": true
    },
    "signature": "5569291c1eab5a2dace43697d7912923efb2fe757e7bb54612025ba52d638350e8078d9f4b46a89be32dd1c1001b9f03643d8cb9ea5885a2451e0fc9bcc88f06"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 30,
    "previous_chain_hash": "5f5619e37a50ec759f2ef634fbc154a750d2aad6578c6750664ee599c379af16",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 30,
     "qualifying": true
    },
    "signature": "82bd1f20c93de151028da4e2ab7c8f645bb068854eea9b0bc14b867007ece4df063c38aa061a2e18c5f64e8b222bd0bc3eafcd8ef6290946ff0761ebf25bb204"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 31,
    "previous_chain_hash": "4cd5fe38c3ff2b9b34dc3eab9aa407436ab6bd5aa2f03b1804f5b9e0a18c6ad1",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 31,
     "qualifying": true
    },
    "signature": "deda093c5522ae5915ed857754c9d2967fb437c0bc4a90a781ef02085c6a0e2f7f2e82a570d379dfc88e8e8c1ef59d470b68ef1f538bf6f2de91bec908f6e90e"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 32,
    "previous_chain_hash": "f094d5accb2fc04bdb06e80fe35e67dc9dad21bc01dca55a40dd8f13ed864d0f",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 32,
     "qualifying": true
    },
    "signature": "ab985d9c46209c37225cd007eee9fa22f651a09194f67986528e5a5990cd937e5ba5786a8e824a51172e1ded6127eabab1f0f781c5c8a2120b5833964c1a240f"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 33,
    "previous_chain_hash": "c90618d31dc0ef8494a9f9b06b2def030bd4683ea1192332f1edfce0e5170bd5",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 33,
     "qualifying": true
    },
    "signature": "ed2cc35a16488afb60b6cfdcc2a43f7c1a4d419d196d2c424dda489afea33049e50e00e6d562ea2d461857ad266ebece88007118ab02c56dead43e6cbca38706"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 34,
    "previous_chain_hash": "6afb16c7861cde9d9db5174c5469d6c77c1c6ecb1d23bf6604f91705dbe07312",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 34,
     "qualifying": true
    },
    "signature": "f606dadddeed344e3730219a8d3dd97b844b09d7deaea0e07da61effec60da186828c5473ac9caf8956f2f02f40a7bca78e7d75ec2f3108e58943d8e4c59c20a"
   },
   {
    "commitment_id": "cid.R6-C.realized",
    "pre_run_commitment_sha256": "9969f89d1e2cd5c9266d5498cb0c47c4d780190679363431db7af810e5fc4a09",
    "protocol_version": "0.8",
    "manifest_sha256": "f82f9579d35b64e11e6f380e5af1b97e0da5fb1bc0fb046e71d93afc5039151c",
    "component": "R6-C",
    "universe_id": "u.r6c.receipts-synth",
    "run_id": "run.R6-C",
    "sequence": 35,
    "previous_chain_hash": "bf41818f0dc00973f935befbb3fab9e8bc9dda56c6fcc91f0a6f9dc6150fda51",
    "observed_at": "2026-07-26T10:06:00Z",
    "event": {
     "idx": 35,
     "qualifying": true
    },
    "signature": "7a74bd2cae1991c14e0c534d5e8fc602022f3103c3df1054e39ff38d8132adec7c74ba70c2a36eb9ab34fbf3368fdebdbeef989faf5007fdf942443aa003ab03"
   }
  ]
 }
}

---

# Bismillah ir-Rahman ir-Rahim
