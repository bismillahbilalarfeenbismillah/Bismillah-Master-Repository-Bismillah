# Bismillah ir-Rahman ir-Rahim

# R0946 -- Seat 2 -- Kimi K3 Fresh LEO Carrying (Binding)

**Chronological Index:** 962 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SEAT_02_COVER.md.txt  
**Source Format:** txt  
**SHA-256:** `a84fb29fb0a86cbe8c1a3aa5484082dd3af8882178b88a6da638402cb0e9ee9d`  

---

## R0946 · Seat 2 -- Kimi K3 Fresh LEO Carrying (Binding)

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SEAT_02_COVER.md.txt
- source_format: txt
- text_sha256: a84fb29fb0a86cbe8c1a3aa5484082dd3af8882178b88a6da638402cb0e9ee9d

# Seat 2 -- Kimi K3 Fresh LEO Carrying (Binding)

**Quantum numbers:** n=1 (K-shell / LEO), l=0 (s-orbital / uniform), m_l=0, m_s=-1/2 (fresh)
**Family:** Kimi K3 (Moonshot) -- non-producer, carrying
**Instance type:** FRESH
**Finding prefix:** F-S02-45
**Carries from:** nothing (fresh instance)
**Binding:** YES -- your HALT verdict blocks the freeze per FB-7b

## Seat-specific instructions

You are a fresh carrying seat. Your HALT is binding and blocks the protocol freeze. This is the highest-responsibility seat in the architecture.

Your task is the same LEO baseline verification described in the common prompt: integrity, repair verification, and byte-truth checking of every O-CLAIM in the v0.45 entry. As a carrying seat, your verification must be exhaustive.

**Carrying-seat obligation:** Every finding you file must be independently verified against the shipped bytes using tool-driven checks. State the exact command you ran and the exact output you received. Narrative-only findings carry zero weight.

## Priority checklist

1. Run `sha256sum -c PACKET_SHA256SUMS` and `python3 build.py`
2. Verify all 5 v0.45 repairs against bytes
3. Verify every numeric claim in the v0.45 entry (counts, ranges, IDs)
4. Check append-only: entries v0.1-v0.44 must be byte-identical to the v0.44 packet
5. Verify seal chain integrity
6. Issue binding verdict

## FB-7b exit condition

If you return non-HALT on these bytes, and at least one other non-producer carrying seat from a different family also returns non-HALT, the FB-7b PENDING RE-CARRY condition is satisfied.

---

# Bismillah ir-Rahman ir-Rahim
