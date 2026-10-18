# Bismillah ir-Rahman ir-Rahim

# R0482 -- Bayyinah al-Mizan v1.0 -- Deposit Companions

**Chronological Index:** 778 of 995  
**Date:** Undated  
**Section:** VI. Applied Audits & Public-Data Studies  
**Source File:** README.txt  
**Source Format:** txt  
**SHA-256:** `02d3223765a6c9774b29c742a0f92c1c8f520607b8e31534c749d12365f70912`  

---

## R0482 · Bayyinah al-Mizan v1.0 -- Deposit Companions

- section: VI. Applied Audits & Public-Data Studies
- source_file: README.txt
- source_format: txt
- text_sha256: 02d3223765a6c9774b29c742a0f92c1c8f520607b8e31534c749d12365f70912

Bayyinah al-Mizan v1.0 -- Deposit Companions
=============================================

These are the companion artifacts for the paper
"Bayyinah al-Mizan: An Audit of the Audit" (v1.0), deposited separately as a PDF.
Together they let anyone independently reproduce and verify every figure in the paper
without trusting the paper's own text.

CONTENTS
--------
reproduction-package/        The dataset and reproduction code.
  reproduce_mizan.py           Run it to recompute every Tier-1 figure and check it
                               against expected values. Run with --selftest to confirm
                               the checks are genuine (perturbs 17 values, catches all).
  MANIFEST.json                Pins the canonical source URL and the SHA-256 hashes of
                               the frozen snapshot pages.
  snapshot/                    The frozen public source pages the figures come from
                               (paymentaccuracy.gov agencies-and-programs, numbers; HHS).
  data/mizan_seed_snapshot.json  The extracted seed values.
  README.md                    Package-specific instructions.

  To reproduce:  cd reproduction-package && python3 reproduce_mizan.py
  Expected:      all checks [OK], "Snapshot verification: PASS", Exit 0.

Bayyinah_al-Mizan_CitationLedger_v1.0.md   Standalone source-URL registry; every URL in
                                           the paper is accounted for here.

Bayyinah_al-Mizan_ConvergenceRecord_v1.0.md  The certification: the nine-round cross-instance
                                             audit trail, both convergences (content at R6/R7,
                                             release at R8/R9), and the artifact hashes.

al-Mizan_v1.0.md   The frozen converged source of the paper. Its SHA-256 is what the
                   convergence record certifies, so you can verify it directly.

VERIFY THE CERTIFIED BYTES
--------------------------
al-Mizan_v1.0.md                            SHA-256 44cc9902f8ffa3fd509b59cc75af7474e93448f5ac1e240a2c2bae33ad578d14
Bayyinah_al-Mizan_CitationLedger_v1.0.md    SHA-256 7031bdd97d3dc872dd3b9ff811482029a54c6d3bd5f59fc360c7a746e964ab3b

Both hashes match the values recorded in the convergence record and independently
published by the audit council.

---

# Bismillah ir-Rahman ir-Rahim
