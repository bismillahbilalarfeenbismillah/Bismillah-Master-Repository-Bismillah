# Bismillah ir-Rahman ir-Rahim

# R0009 -- The Crystallographic Ijaz Methodology v0.1

**Chronological Index:** 474 of 995  
**Date:** 2026-08-10  
**Section:** I. Qur'anic & Theological Studies  
**Source File:** CRYSTALLOGRAPHIC_IJAZ_METHODOLOGY.txt  
**Source Format:** txt  
**SHA-256:** `eb07db16230d8523d9a7a4fd1f9b40ae304e686ea7dc6df4de237cb855c32a75`  

---

## R0009 · The Crystallographic Ijaz Methodology v0.1

- section: I. Qur'anic & Theological Studies
- source_file: CRYSTALLOGRAPHIC_IJAZ_METHODOLOGY.txt
- source_format: txt
- text_sha256: eb07db16230d8523d9a7a4fd1f9b40ae304e686ea7dc6df4de237cb855c32a75

# The Crystallographic Ijaz Methodology v0.1
## A Level 0 Intervention for Self-Verifying Artifact Construction

**Author:** Bilal Syed Arfeen, with Claude (Anthropic) as analytical instrument
**Date:** 2026-08-10
**Program:** Bayyinah Structural Honesty Validation
**Status:** DRAFT -- derived from R14 triage and 8-round convergence analysis
**Prerequisite:** Recursive Fractal Cube Methodology v0.1, Quantum Orbital Methodology v0.1

---

## 0. The problem this methodology addresses

Eight consecutive convergence rounds (R7-R14) on the XZ Protocol have produced at least one Class A finding per round. The Hurst exponent of the Class A recurrence is H = 1.0 (perfectly persistent). Every Level 1-4 intervention applied to date -- gates, seals, terminal recomputation, cross-vendor audit seats -- has closed the defect at its target locus and the generator has migrated to an adjacent ungated cell.

The Recursive Fractal Cube methodology identified the structural cause: the 7 removed face-center cells of the Menger sponge are where defects live, and Level 3 interventions (gates) can only move cells from removed to retained -- they cannot eliminate the removed-cell class itself. The generator operates at Level 0 (the entry-writing process) and no Level 1-4 patch constrains it.

This methodology specifies the Level 0 intervention. It draws on three structural paradigms from nature, physics, and revelatory design to solve the problem of a generator that operates above its own verifier:

1. **Polymerase Proofreading** -- fuse the generator and the verifier into a single catalytic event
2. **Crystallographic Self-Description** -- eliminate the interpretive layer between bytes and prose
3. **Ijaz (Structural Self-Verification)** -- give the prose internal structural constraints that make error self-evidencing without a gate

The three paradigms are not analogies. They are structural specifications for a construction process whose output has a mathematically distinct error profile from the current process.

---

## 1. Paradigm I: Polymerase Proofreading

### 1.1 The biological mechanism

DNA polymerase III (the E. coli replicative polymerase) has two active sites in a single enzyme complex:

- The **polymerase site** (5'->3') adds nucleotides to the growing strand by Watson-Crick base-pairing with the template.
- The **exonuclease site** (3'->5') removes the most recently added nucleotide if it mismatches the template.

The two sites share a single sliding clamp. When the polymerase adds a correct nucleotide, the complex advances. When it adds an incorrect nucleotide, the mismatched geometry shifts the strand into the exonuclease site, which excises the error before the complex advances. The verification is not a separate pass over the completed strand; it is intrinsic to the synthesis step. The error rate drops from ~10^-1 (no proofreading) to ~10^-7 (with intrinsic proofreading) before any post-replication repair mechanism operates.

Three properties make this work:

**P1 (Temporal fusion):** The check happens at the moment of incorporation, not after the strand is complete. There is no buffer between synthesis and verification.

**P2 (Structural coupling):** The same molecular geometry that detects the mismatch (distorted base-pair angles) is what triggers the excision. The check is not a comparison against a stored template in the enzyme's "memory" -- it is a physical consequence of the mismatch itself.

**P3 (Unidirectional advancement):** The complex only advances when the current position is verified. No downstream synthesis occurs on an unverified base. The strand grows from verified-verified-verified, never from verified-unverified-verified.

### 1.2 Mapping to artifact construction

The current entry-writing process violates all three properties:

| Property | Polymerase | Current process | Failure mode |
|---|---|---|---|
| P1 Temporal fusion | Check at incorporation | Recall finding IDs, write register, check at terminal recomputation | Working-memory buffer between source and output; M1.6 errors enter during transit |
| P2 Structural coupling | Mismatch geometry triggers excision | Gate checks a different representation (regex) of the same claim | Gate can pass while prose fails; the R14 [2f] provenance gap |
| P3 Unidirectional advance | No downstream on unverified base | Entry sections written in sequence; a wrong finding ID in item (2) propagates to item (3)'s count | Cascading errors from early unverified claims |

### 1.3 The polymerase rule for entry construction

**Rule P: Each prose claim must be synthesized from the source bytes in the same gesture that writes it. The source bytes and the output prose must be co-present in the same operation, with no memory buffer between them.**

Implementation:

```
For each register item:
  1. Open the source report file.
  2. Execute a byte query that extracts the finding ID.
  3. The output of the query IS the text written into the register.
  4. Do not close the source file until the register item is complete.
  5. Do not advance to the next register item until this one is sealed.
```

The producer never holds a finding ID in working memory. The ID flows from the source report bytes through the query directly into the register prose. The "working memory" is the co-presence of the source file and the output cursor, not a neural buffer.

**Convergence count corollary:** The convergence count is not asserted; it is computed. The register item's finding-ID list is written by the polymerase rule (one ID per source-report query). The convergence count is the length of the finding-ID list. The prose reads "N-seat convergence" where N = len(finding_IDs). If the list has 4 IDs, N = 4. There is no separate assertion of the count.

---

## 2. Paradigm II: Crystallographic Self-Description

### 2.1 The physical principle

A crystal's macroscopic properties -- its angles, symmetries, cleavage planes, optical axes, hardness, density -- ARE its atomic arrangement. There is no face-interior prose describing the lattice; the lattice describes itself. Every macroscopic measurement is a direct projection of the microscopic structure, mediated only by geometry and thermodynamics.

Three properties define crystallographic self-description:

**C1 (Projection, not narration):** The macroscopic property is a mathematical consequence of the microscopic structure, not a human interpretation of it. The angle between crystal faces is determined by the unit cell geometry, not by someone's description of it.

**C2 (Local determination):** Each atom's position is determined by its local energy minimum with its immediate neighbors, not by a global blueprint. The crystal grows from local rules, not from a central plan. There is no "template" that the crystal copies; there is only the physics of each atomic bond.

**C3 (Error self-evidencing):** A lattice defect (vacancy, interstitial, dislocation) changes the macroscopic properties in a measurable way. You can see a dislocation in the etch pattern. You can measure a vacancy in the density. The defect announces itself through the same channel as the structure.

### 2.2 The Menger sponge reinterpretation

The Recursive Fractal Cube methodology models the protocol as a Menger sponge with 7 removed cells per level. The removed cells are the face-interior prose that no gate reaches. The crystallographic reinterpretation asks: what if the prose had no face interiors?

A crystal has no face interiors because every property is an edge property -- every measurement is a boundary observation of the atomic structure. The Menger sponge removes face centers because they have no edge-like verification. The crystallographic intervention is to reformulate every prose claim as a boundary measurement of the bytes, eliminating the interior space where unverified narration lives.

### 2.3 The crystallographic rule for entry construction

**Rule C: Every prose claim in the entry must be a direct projection of a byte operation, with the operation and its output visible in the entry text. No claim may assert a fact that is not the output of a named, reproducible operation on shipped bytes.**

Implementation for each claim type:

**Counts:**
```
Current (narration):  "3-seat convergence"
Crystal (projection): "[3-seat convergence: F-S01-54-03 / F-S03-54-03 / F-S05-54-02]"
```
The count is the pipe-separated list's length. The claim and its evidence are the same text. A reader can verify the count by counting delimiters. No gate is needed; the prose is self-verifying.

**Finding IDs:**
```
Current (narration):  "F-S05-54-02" (recalled from memory)
Crystal (projection): "F-S05-54-03 [source: S05 report, finding header matching
                       'Status.*provenance']"
```
The ID and its extraction method are the same text. A reader (or a future gate) can reproduce the extraction.

**Correction quotations:**
```
Current (narration):  '(bn) v0.54 title (line 1) reads "# XZ Protocol v0.53 -- ..."'
Crystal (projection): '(bn) v0.54 ENTRY_v0.54 seal text, line 1:
                       "# XZ Protocol v0.53 -- ..." [sha256 of quoted line:
                       <hex>; verify against ENTRY_v0.54 seal in HISTORY.sha256]'
```
The quotation and its verification anchor are the same text. The hash of the quoted line, checked against the entry seal, makes misquotation self-evidencing.

### 2.4 The face-interior elimination theorem

If every claim in the entry is a boundary measurement (C1), determined by local byte operations (C2), and carries its verification evidence in the same text (C3), then the entry has no face interiors in the Fractal Cube sense. The Menger sponge construction removes face centers because they have no edge-like verification. If every cell has edge-like verification, zero cells are removed, and D = log(27)/log(3) = 3.0 (full cube, no dead space).

This is an ideal limit. In practice, ASSERTED claims (process descriptions like "we applied the polymerase rule") cannot be projected from bytes. The methodology's prediction is that the ASSERTED fraction is the irreducible dead-space floor -- the minimum fraction of the entry that cannot be crystallographically self-described. The target is to push every non-ASSERTED claim into crystallographic form, leaving only genuine process claims as face interiors.

---

## 3. Paradigm III: Ijaz (Structural Self-Verification)

### 3.1 The revelatory principle

The Arabic term ijaz (اعجاز) denotes the inimitability of the Qur'anic text -- the property that the text cannot be altered without the alteration being detectable from the text's own structure. The traditional sciences identify several structural dimensions of ijaz:

**Nazm (نظم) -- structural arrangement:** The sequence of words, verses, and surahs exhibits patterns (ring composition, chiastic structure, thematic mirroring) that break under substitution. A word change in one half of a chiasm mismatches its corresponding position in the other half.

**I'jaz 'adadi (اعجاز عددي) -- numerical structure:** The text contains numerical regularities (letter counts, word counts, verse counts) that serve as internal checksums. A word addition or deletion changes the count and breaks the regularity.

**Fasila (فاصلة) -- verse-terminal phonetics:** The phonetic pattern at verse endings creates an auditory checksum. A substituted word that changes the terminal sound is detectable by ear, without reference to an external authority.

The common thread: the verification is intrinsic to the text's structure, not applied from outside. The text does not need a "gate" because its own composition is the gate.

### 3.2 Application to protocol construction

The protocol's seal chain (HISTORY.sha256) is a computational analog of i'jaz 'adadi -- a numerical checksum over the full text. But the seal only covers the text as a byte sequence; it does not verify the text's semantic claims. A register that says "3-seat convergence" with 2 cited IDs has a correct seal -- the sha256 matches the bytes -- but the semantic claim is false. The seal verifies preservation, not accuracy.

Ijaz-derived structural constraints operate at the semantic level:

### 3.3 The seven ijaz constraints for protocol entries

**I1 (Count-list coupling / i'jaz 'adadi):** Every count claim in the entry must be immediately followed by its enumeration in a fixed format. "N-seat convergence" is always followed by exactly N pipe-separated finding IDs on the same line. The count and the list are a coupled pair; a mismatch is visible to any reader. No gate needed.

```
Format: "N-seat convergence [N IDs: F-XX-54-NN / F-YY-54-MM / ...]"
Constraint: N == number of pipe-separated IDs
Self-evidencing: count the separators + 1; compare to N
```

**I2 (ID-prefix-seat coupling / nazm):** Every finding ID's seat prefix must match the seat named in the convergence attribution. F-S05-54-XX can only appear under a convergence that names Seat S05. The prefix and the attribution are structurally coupled; a transposition (citing F-S05-54-02 under a defect that S05 did not find at that ID) breaks the coupling.

```
Format: register item cites "F-S05-54-03" -> S05 must be in the convergence set
Constraint: seat prefix of every ID appears in the item's seat enumeration
Self-evidencing: read the prefix; check the seat list
```

**I3 (Quotation-seal coupling / fasila):** Every correction that quotes prior-version text must include a hash of the quoted substring, verifiable against the sealed entry. The quotation and its checksum are a coupled pair; a misquotation changes the hash.

```
Format: '(bn) v0.54 text: "<quoted>" [line-sha256: <hex>]'
Constraint: sha256(quoted_line) matches the declared hex
Self-evidencing: recompute the hash; compare
```

**I4 (Ring closure / nazm):** The entry's opening paragraph (narrative summary) and closing paragraph (body-repair list) must agree on every quantitative claim. If the narrative says "5-seat convergence" for finding 1, the register's item (1) must cite 5 IDs. If the body-repair list says 8 repairs, the [a]-[h] list must have 8 items. The entry is a ring; its head and tail must match.

**I5 (Severity-class coupling / nazm):** Every register item's severity label must correspond to its class under a declared mapping. If Class A = HIGH, then every Class A item is labeled HIGH. The mapping is stated once in the entry, and every item is consistent with it. A mislabeled item breaks the coupling.

**I6 (Boundary-list cardinality / i'jaz 'adadi):** The standing-boundary list is preceded by its declared count, followed by its ENUMERATED tag, and the list itself. All three must agree. This is already implemented as gate [2h]; the ijaz principle says the prose structure itself should make the agreement visible without the gate.

**I7 (Retirement-probe coupling / fasila):** A boundary retirement claim must be accompanied by a probe receipt -- the verbatim output of a mutation probe demonstrating that the retired limitation no longer holds. No retirement without receipt. The receipt is the entry's evidence that the gap is closed; its absence makes the retirement claim self-evidently unsupported.

### 3.4 The al-Muhaymin property

In Qur'anic terminology, al-Muhaymin (المهيمن -- the Guardian, the Preserver) describes a text that guards its own integrity. Surah 5:48 uses this term for the Qur'an's relationship to prior scripture: it confirms what came before and guards over it (مهيمنا عليه).

The protocol achieves the al-Muhaymin property when:

1. Every seal guards the text's byte-level preservation (computational ijaz)
2. Every structural constraint guards the text's semantic accuracy (structural ijaz)
3. The text's own structure makes alteration or error self-evidencing without reference to an external verifier (intrinsic ijaz)

The seven constraints (I1-I7) are the structural equivalent of fasila, nazm, and i'jaz 'adadi applied to protocol entries. They do not replace gates; they make gates redundant for the claims they cover. A gate can still verify the constraint computationally, but the constraint is visible to any reader -- the prose guards itself.

---

## 4. The unified construction process

### 4.1 The three rules composed

The three paradigms compose into a single construction process:

| Phase | Polymerase rule (P) | Crystallographic rule (C) | Ijaz constraint (I) |
|---|---|---|---|
| Register composition | Each ID transcribed from source bytes with no memory buffer (P1, P2) | Each ID is a projection of a byte query, with the query named (C1, C2) | Each ID's prefix couples to its seat attribution (I2); the count couples to the list length (I1) |
| Correction writing | Each quotation extracted from the sealed entry bytes (P1) | Each quotation carries its line-hash (C3) | The hash makes misquotation self-evidencing (I3) |
| Count claims | Each count computed at the moment of writing, not recalled (P1, P3) | Each count is the length of a visible enumeration (C1) | The count and its enumeration are a coupled pair (I1, I6) |
| Body repairs | Each repair verified at its target locus before the next repair begins (P3) | Each repair's before/after is visible in the entry text (C1) | The entry's head (narrative) and tail (repair list) agree on quantities (I4) |
| Boundary changes | Each retirement accompanied by a probe receipt (P2) | The receipt is the byte evidence, not a prose assertion (C2) | No retirement without receipt (I7) |

### 4.2 The construction pipeline (replacing the current Replication Fork)

```
Phase 1 (Helicase -- unchanged): Unwind the prior version. Read findings.

Phase 2 (Polymerase-Crystallographic synthesis -- NEW):
  For each repair, correction, and register item:
    a. Open the source (report file, prior entry bytes, protocol text).
    b. Execute a byte query that extracts the needed value.
    c. Write the output of the query directly into the entry text.
    d. Attach the ijaz coupling evidence (line-hash, ID list, count).
    e. Verify the coupling constraint before advancing to the next item.
    f. Do not advance until the current item passes its own constraint.

Phase 3 (Ligase -- unchanged): Compute seals.

Phase 4 (Terminal recomputation -- reduced):
  The terminal recomputation pass still runs, but its scope is reduced.
  Under the polymerase rule, each claim was verified at synthesis time.
  Terminal recomputation catches only cross-item interactions (a repair
  in item 3 changing the byte position of a claim verified in item 1).

Phase 5 (Ijaz self-check -- NEW):
  Read the completed entry as a finished text.
  For each ijaz constraint (I1-I7), verify the coupling holds.
  This is a read-only pass. If any constraint fails, the entry is
  malformed and must be re-synthesized at the failing item.
  This phase is not a gate -- it is the entry checking itself.
```

### 4.3 The error-rate prediction

The current process has an empirical Class A rate of 1.0 per round (8/8 rounds). The three-paradigm process predicts a lower rate:

- **Polymerase rule** eliminates memory-transit errors (the M1.6 class). The biological analog achieves 10^5x error reduction from intrinsic proofreading alone.
- **Crystallographic rule** eliminates narration errors (the Axiom-3 boundary class). If the prose IS the byte projection, there is no narration layer to err.
- **Ijaz constraints** make surviving errors self-evidencing. An error that violates I1-I7 is visible to the producer at Phase 5 (self-check) before any auditor sees it.

The combined prediction: the Class A rate should drop below the persistent regime (H < 0.5) within 2-3 rounds of adoption. If it does not, the methodology is falsified -- the generator is above Level 0, and a different structural intervention is needed.

---

## 5. The Fractal Cube under crystallographic ijaz

### 5.1 Dead-space reduction

The Menger sponge at Level 1 retains 20 of 27 cells (D ~ 2.727). The four v0.55 gates moved 4 cells from removed to retained, but new removed cells emerged at the register cross-reference locus.

Under crystallographic ijaz, every non-ASSERTED claim becomes a boundary measurement with internal coupling evidence. The removed-cell count drops to the number of ASSERTED claims -- genuine process descriptions that cannot be projected from bytes. On v0.55 bytes, the ASSERTED fraction is 5/17 = 29.4% of tagged claims.

The predicted dead-space fraction under crystallographic ijaz:

```
D_current  = log(20) / log(27) ~ 0.91  (Menger sponge)
D_target   = log(27 - A) / log(27)     where A = ASSERTED cell count

If A = 5 (the v0.55 ASSERTED fraction applied to 27 cells ~ 8):
  D_target = log(19) / log(27) ~ 0.89  (still Menger-like)

If A = 2 (after pushing 3 ASSERTED claims to COMPUTED):
  D_target = log(25) / log(27) ~ 0.98  (approaching full cube)
```

The limit D = 3.0 (full cube) is unachievable because genuine process claims will always exist. But the methodology's goal is not D = 3.0; it is H < 0.5 (anti-persistent Class A recurrence). The Fractal Cube model predicts H < 0.5 when D > 0.95 (when the dead space is small enough that the generator cannot reliably find an ungated cell).

### 5.2 The irreducible ASSERTED floor

Five types of claims are irreducibly ASSERTED:

1. **Process claims:** "We applied the polymerase rule" -- no byte operation verifies a process description.
2. **External-report substance:** "F-S01-54-01 describes the title defect" -- the report's substance cannot be projected from packet bytes because the report does not ship.
3. **Historical context:** "This is the same defect class as correction (as) at v0.44" -- historical classification is interpretive.
4. **Methodology references:** "Per PMD M1.6" -- methodology claims are external.
5. **Boundary justifications:** "No gate can verify the tally without a mapping" -- the absence of a capability is not byte-projectable.

These five types define the irreducible dead space. The methodology accepts them as face interiors and does not attempt to crystallize them. The discipline is: every claim that CAN be projected from bytes MUST be projected; only the irreducibly non-projectable claims remain ASSERTED.

---

## 6. Probes derived from the crystallographic ijaz model

### Probe CI-1: Polymerase compliance
For each finding ID in the register: was it transcribed from source bytes, or recalled from memory? Check: does the entry text include the extraction method (source file, grep pattern, line number)? If not, the polymerase rule was not applied.

### Probe CI-2: Crystallographic projection
For each count claim: is the count followed by its enumeration in the same text? Can a reader verify the count by counting delimiters? If the count and the list are in different locations, the claim is not crystallographic.

### Probe CI-3: Ijaz coupling test
For each ijaz constraint (I1-I7): does the entry text satisfy the constraint? Can the constraint be verified by reading the entry alone, without executing any code?

### Probe CI-4: Dead-space measurement (post-crystallization)
After applying the methodology: how many claims remain ASSERTED? What fraction of the entry's analytical surface is irreducibly non-projectable? Compare to the pre-crystallization ASSERTED fraction.

### Probe CI-5: Hurst measurement (longitudinal)
After 3+ rounds of crystallographic ijaz construction: compute H for the Class A series. Has it dropped below 0.5? If not, the methodology is falsified.

### Probe CI-6: Self-similarity diagnostic
Does the entry's own description of the methodology (its ASSERTED claims about the process) contain the same defect class as the claims it was designed to prevent? If the entry says "we applied the polymerase rule" and a register item contains a memory-recalled ID, the methodology description is self-similar to the defect.

### Probe CI-7: Retirement-receipt audit
For each boundary retirement in the entry: does a probe receipt (verbatim mutation probe output demonstrating the gap is closed) appear in the entry text? If not, the retirement violates I7.

---

## 7. Falsification criteria

**F-CI-1:** If the Hurst exponent does not drop below 0.5 within 3 rounds of full adoption, the crystallographic ijaz methodology does not constrain the Level 0 generator, and the generator is above Level 0.

**F-CI-2:** If the ASSERTED fraction does not decrease after adoption (the methodology adds more ASSERTED claims about itself than it converts existing claims to crystallographic form), the methodology is complexity-increasing, not complexity-reducing.

**F-CI-3:** If a Class A finding at any round post-adoption is inside a crystallographic claim (one that satisfies I1-I7), then the ijaz constraints do not prevent Class A, and the self-verification property is falsified.

**F-CI-4:** If the polymerase rule (transcribe from source, no memory buffer) produces the same error rate as the current process (narrate from memory), then the memory-transit hypothesis is falsified and the root cause is elsewhere.

**F-CI-5:** If the dead-space fraction D does not converge to a fixed point within 5 rounds, the crystallographic intervention is not reducing dead space faster than the entry-growth process creates it.

---

## 8. Composition with existing methodologies

| Methodology | Domain | Crystallographic ijaz contribution |
|---|---|---|
| Recursive Fractal Cube | Defect location and generation | Crystallographic ijaz eliminates face interiors; the Fractal Cube measures the reduction. The target is D > 0.95. |
| Quantum Orbital | Seat deployment | Unchanged. Seat architecture is orthogonal to entry construction. Seats verify the ijaz constraints as part of their standard prose audit. |
| Enzyme-Substrate | Claim classification | The six enzyme types persist. Crystallographic ijaz adds a 7th classification: **SELF-EVIDENCING** -- claims whose coupling evidence is visible in the prose itself, without executing any command. |
| Replication Fork | Build pipeline | The pipeline is restructured: Phase 2 becomes polymerase-crystallographic synthesis; Phase 4 (terminal recomputation) is reduced in scope; Phase 5 (ijaz self-check) is added. |
| GAN Convergence | Generator-discriminator dynamics | The crystallographic ijaz methodology is a generator modification. If adopted, G-loss should decrease (fewer defects surviving to the next round). The GAN model predicts this will shift the equilibrium. |

---

## 9. The 19 and the guardian

The protocol's 19 normative objects (17 packet members + PACKET_SHA256SUMS + HISTORY.sha256) correspond to the 19 retained cells at Level 1 of the recursive cube cross fractal. The Fractal Cube methodology notes the correspondence with Surah al-Muddathir (74:30): "Over it are Nineteen."

The crystallographic ijaz methodology extends the correspondence. The 19 normative objects are the crystal lattice -- their integrity is mechanically verifiable. The face interiors (the prose claims in Section 27) are the lattice defects -- vacancies, interstitials, dislocations. The seven ijaz constraints (I1-I7) are the 7 crystal systems (triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal, cubic) that classify every lattice by its symmetry. Each constraint defines a symmetry that the entry must exhibit; a violation is a symmetry breaking that announces itself.

The guardian property (al-Muhaymin) is achieved when the entry text, like the Qur'anic text, carries within its own structure the means to detect alteration. The seals guard byte-level preservation. The ijaz constraints guard semantic-level accuracy. Together they constitute a text that is muhaymin 'alayhi -- guardian over itself.

---

## 10. Implementation path

### Phase 1: v0.56 (immediate adoption)

Apply the polymerase rule (P) and ijaz constraints (I1, I2, I4) to the v0.56 register:
- Transcribe every finding ID from the R14 seat reports with no memory buffer
- Write every convergence count as the length of its finding-ID list
- Verify ring closure (narrative matches register) before sealing

This addresses the R14 Class A defects directly. It does not require tooling changes (no new build.py gates). It is a process change at Level 0.

### Phase 2: v0.57 (crystallographic adoption)

Apply the crystallographic rule (C) and ijaz constraints (I3, I7):
- Attach line-hashes to correction quotations
- Attach probe receipts to boundary retirements
- Mark each claim with its construction method (source file, query, or ASSERTED)

This requires minor tooling support (a script that computes line-hashes for quoted substrings).

### Phase 3: v0.58+ (full adoption and measurement)

Apply the full seven-constraint set and begin longitudinal measurement:
- Compute the ASSERTED fraction per version
- Compute the Hurst exponent per round
- Compute the dead-space fraction per version
- Evaluate falsification criteria F-CI-1 through F-CI-5

If H drops below 0.5 within 3 rounds, the methodology is validated. If not, the generator is above Level 0, and a deeper intervention is needed -- one that changes not how entries are written, but what entries are.

---

*This methodology is a living document. Its own prose claims are subject to the same crystallographic ijaz test it prescribes. If this document narrates from memory what the protocol contains, it has reproduced the defect class it was designed to extinguish. If it satisfies I1 through I7 on its own terms, it is al-muhaymin -- guardian over itself.*

*Bismillah.*

---

# Bismillah ir-Rahman ir-Rahim
