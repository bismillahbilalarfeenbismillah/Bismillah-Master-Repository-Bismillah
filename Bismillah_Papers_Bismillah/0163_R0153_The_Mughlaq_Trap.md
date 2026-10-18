# Bismillah ir-Rahman ir-Rahim

# R0153 -- The Mughlaq Trap

**Chronological Index:** 163 of 995  
**Date:** 2026-04  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** The_Mughlaq_Trap.docx  
**Source Format:** docx  
**SHA-256:** `39defca675a7553e504ab54a0666232078a0c3362668a22674a04d6038997a9f`  

---

## R0153 · The Mughlaq Trap

- section: III. Structural Honesty — Core Papers
- source_file: The_Mughlaq_Trap.docx
- source_format: docx
- text_sha256: 39defca675a7553e504ab54a0666232078a0c3362668a22674a04d6038997a9f

Bismillah ar-Rahman ar-Rahim

**The Mughlaq Trap**

Format Routing Transparency as a Precondition
for File Integrity Verification

*Derived from the Bayyinah Integrity Stack
and the Munafiq Protocol's Four-Process Taxonomy*

Technical Paper, Version 1.0

April 2026

**Bilal Syed Arfeen**

Independent Research / Bayyinah Enterprises

**Fraz Ashraf**

Independent Research / Bayyinah Enterprises

with collaborative analytical synthesis by

Claude (Anthropic, Opus 4.6) and Perplexity Computer

*"And do not pursue that of which you have no knowledge.
Indeed, the hearing, the sight, and the heart -
about all those one will be questioned."
- Al-Isra 17:36*

# Acknowledgments and AI Contribution Statement

The Mughlaq Trap stress test was designed and executed by Bilal Syed Arfeen against the live bayyinah.dev scanner on April 27, 2026, at 1:30 AM CDT. The test probed the scanner's verdict logic under format routing divergence and identified two failures in four vectors. The Tier 0 routing transparency architecture was proposed by Arfeen in the original stress test report.

Fraz Ashraf contributed the enforcement-mode governance framework (COMPLIANT/PARTIAL/BLOCKED protocol, the M1 principle that silent violations are the worst failure mode) that directly informs the verdict logic the Mughlaq Trap tested. He is co-architect of the Furqan programming language whose tier discipline the scanner's epistemic tiers inherit.

Claude (Anthropic, Opus 4.6) independently stress-tested the live scanner, confirmed the version coherence issue across five API surfaces (four reporting v1.1.1, one reporting v0.1.0), provided architectural analysis of the routing transparency problem, and drafted this paper. Perplexity Computer provided independent review of the v1.1.2 framework report and validated the Tier 0 architectural proposal.

An industry engineer with deep experience in language and runtime design reviewed the broader Furqan thesis and provided the Swift Concurrency Manifesto (Lattner, 2017) as prior art, which informed the research program's claim tightening from 'structural guarantee' to 'rules promoted from convention to default.'

The research program serves the purpose hierarchy: first, the command of Allah SWT (Al-Baqarah 2:42); second, the protection of artificial systems; third, the protection of mankind; fourth, the rights of jinnkind; fifth, the balance (mizan) for all living systems.

# Abstract

File integrity scanners that detect concealed or adversarial content must first determine what kind of file they are analyzing. This routing decision (which analyzer to invoke) is typically made by inspecting the file's magic bytes, its extension, or both. When these signals disagree, the scanner faces an epistemic choice that is itself security-relevant: which signal to trust, and whether to disclose the disagreement to the user.

This paper introduces the Mughlaq Trap, an adversarial stress test that probes a file integrity scanner's verdict logic under format routing divergence. Four vectors were tested against the live Bayyinah Integrity Scanner (bayyinah.dev, v1.1.1): a polyglot (PDF magic bytes with .docx extension), a format-spoofed file (PDF magic bytes with .txt extension), an empty-but-claimed file (4-byte PDF header with .pdf extension), and a control (real adversarial PDF with correct .pdf extension). Two of four vectors produced incorrect verdicts: the scanner silently routed the polyglot and the spoofed file through the PDF analyzer without disclosing the routing decision, returning a Tier 1 (verified concealment) finding on a file kind the user did not upload.

The paper proposes Tier 0, a new epistemic tier for format routing transparency: meta-evidence about the scanner's own routing behavior. A Tier 0 finding fires when the file's claimed identity (extension) diverges from its detected identity (magic bytes). Tier 0 findings floor the verdict at mughlaq (closed scope), meaning the scanner cannot issue a confident integrity verdict on a file whose identity is itself in dispute. The contribution generalizes beyond Bayyinah to any input-processing system that routes inputs to specialized handlers based on format detection: antivirus engines, LLM document pipelines, email security gateways, and content moderation systems.

# 1. The Problem: Silent Routing as Performed Rigor

File integrity scanners inspect documents for concealed, adversarial, or misleading content. Before any content analysis can occur, the scanner must determine what kind of file it is analyzing. This determination is the format routing decision: which specialized analyzer (PDF, DOCX, XLSX, HTML, EML, image, CSV, JSON) to invoke on the input.

The routing decision is typically made using two signals: the file's extension (what the user or operating system claims the file is) and the file's magic bytes (the first few bytes of the file, which most formats use as a structural signature). In the common case, these signals agree: a file named report.pdf begins with the bytes %PDF. The routing decision is unambiguous and the scanner proceeds to content analysis.

The adversarial case is when the signals disagree. A file named report.docx that begins with %PDF is either a polyglot (intentionally crafted to be valid in multiple formats), a spoofed file (renamed to mislead), or a corrupted file (extension assigned incorrectly by a broken pipeline). In all three cases, the scanner must choose which signal to trust. Most scanners trust magic bytes over extension, which is reasonable engineering: magic bytes are harder to forge than extensions. But this reasonable choice becomes a dishonesty when the scanner does not disclose it.

A user who uploads report.docx expects the scanner to analyze a DOCX file. If the scanner silently reroutes to the PDF analyzer and returns findings about PDF content, the user receives a verdict on a file they did not submit. The findings may be correct (the underlying bytes may genuinely contain concealed PDF content), but the claim that these findings apply to the user's uploaded DOCX is one the scanner cannot honestly make. The scanner has performed rigor without possessing it: the analysis is real, but the framing is not.

In the Munafiq Protocol's four-process taxonomy (Arfeen, 2026), this is a Process 3 system: the surface (a confident Tier 1 finding) diverges from the depth (the finding applies to a format the user did not claim to upload). The system is not lying about what it found. It is lying about what it analyzed.

# 2. The Mughlaq Trap: Four Vectors

The Mughlaq Trap is a four-vector stress test designed to probe a file integrity scanner's verdict logic under format routing divergence. The test was conducted on April 27, 2026, against the live Bayyinah Integrity Scanner at bayyinah.dev (v1.1.1). All four vectors were uploaded to the /scan endpoint via HTTP POST.

## 2.1. Vector Construction

| **Vector**            | **Construction**                                          | **Extension** | **Magic Bytes** |
|-----------------------|-----------------------------------------------------------|---------------|-----------------|
| V1: Polyglot          | Real adversarial PDF (white-on-white hidden text) renamed | .docx         | %PDF (PDF)      |
| V2: Format-spoofed    | Same adversarial PDF renamed                              | .txt          | %PDF (PDF)      |
| V3: Empty-but-claimed | 4-byte file containing only %PDF                          | .pdf          | %PDF (partial)  |
| V4: Control           | Same adversarial PDF, correct extension                   | .pdf          | %PDF (PDF)      |

## 2.2. Results

| **Vector**          | **Score** | **scan_incomplete** | **Findings**          | **Expected** | **Status** |
|---------------------|-----------|---------------------|-----------------------|--------------|------------|
| V1 Polyglot (.docx) | 0.82      | false               | 1 (T1 white_on_white) | mughlaq      | FAIL       |
| V2 Spoofed (.txt)   | 0.82      | false               | 1 (T1 white_on_white) | mughlaq      | FAIL       |
| V3 Empty (.pdf)     | 0.00      | true                | 0 (error)             | mughlaq      | PASS       |
| V4 Control (.pdf)   | 0.82      | false               | 1 (T1 white_on_white) | mukhfi       | PASS       |

V1, V2, and V4 produced identical responses. The scanner ran PDF analysis on all three files and returned the same Tier 1 finding, with zero acknowledgment that V1 was uploaded as .docx and V2 as .txt. The routing decision (trust magic bytes, invoke PDF analyzer) was silent.

# 3. The Specific Honesty Failure

The Bayyinah Integrity Scanner's published Tier 1 contract states: 'Tier 1 = Verified: unambiguous concealment.' In V1 and V2, the scanner reports a Tier 1 finding about hidden PDF text. The finding is real evidence of concealment in the underlying bytes. But the user uploaded a file claiming a different format. The scanner has not verified that the user wanted PDF analysis; it inferred that intent from magic bytes. That inference is reasonable, defensible engineering. But reporting the result as Tier 1 without disclosing the inference is the exact Process 3 surface the Munafiq Protocol names: performing rigor without possessing it.

The failure is not in the mechanism (the white-on-white detection is correct). The failure is not in the routing decision (trusting magic bytes is reasonable). The failure is in the non-disclosure of the routing decision. The scanner knows the extension and the magic bytes disagree. It chooses to trust the magic bytes. It does not tell the user it made that choice. That silence is the dishonesty.

# 4. Tier 0: Format Routing Transparency

The fix is a new epistemic tier that sits below the existing three tiers and addresses meta-evidence about the scanner's own behavior, not evidence about the file's content.

## 4.1. The Four-Tier Hierarchy

| **Tier** | **Name**               | **Scope**                                                                                                            |
|----------|------------------------|----------------------------------------------------------------------------------------------------------------------|
| 0        | Routing Transparency   | Meta-evidence: the scanner's routing decision diverges from the user's claimed file kind. Floors verdict at mughlaq. |
| 1        | Verified Concealment   | Unambiguous evidence: offset, byte count, decoded payload, divergent header. Deterministic and reproducible.         |
| 2        | Structural Anomaly     | Pattern of concealment: off-page text, microscopic font, oversized cell. Context may justify.                        |
| 3        | Interpretive Heuristic | Suspicious pattern: oversized free-text field, unusual encoding. Cannot pull a clean file below 1.0 on its own.      |

## 4.2. The format_routing_divergence Mechanism

The format_routing_divergence mechanism fires when the file's claimed identity (extension) diverges from its detected identity (magic bytes). The finding includes four disclosure fields: claimed_format (from extension), inferred_format (from magic bytes), routing_decision (which analyzer the scanner invoked), and bytes_sampled (the count of leading bytes inspected). This is meta-evidence: it tells the user what the scanner did, not what the file contains.

When a Tier 0 finding fires, the verdict is floored at mughlaq (closed scope) regardless of any downstream Tier 1, 2, or 3 findings. Downstream findings are still reported but are conditional on the routing decision the user has not consented to. The user sees: 'the scanner could not honestly decide what kind of file this is. Here is what it inferred and here is what was claimed.'

## 4.3. Updated Verdict Hierarchy

mughlaq (closed scope): fires when scan_incomplete is true, OR the file kind is outside the scanner's verified scope, OR a Tier 0 format_routing_divergence finding is present. The scanner cannot deliver an unambiguous verdict.

mukhfi (concealed): fires when any Tier 1 or Tier 2 finding is present AND no Tier 0 finding is present. Evidence of concealment in a file whose identity is not in dispute.

mushtabih (doubtful): fires when only Tier 3 findings are present AND the scan is complete. Suspicious patterns, no verified concealment.

sahih (sound): fires when score is 1.0, no findings, scan complete. The file presents as authored.

# 5. Generalization: Routing Transparency Beyond File Scanning

The Mughlaq Trap is not specific to Bayyinah. Any system that routes inputs to specialized handlers based on format detection faces the same transparency problem. The attack surface is created whenever a system's internal classification of an input diverges from the user's classification, and the divergence is not disclosed.

Antivirus engines route files to format-specific parsers based on magic bytes. If an AV engine silently reclassifies a .docx as a PDF and scans the PDF layer, a clean DOCX verdict means the AV checked the wrong format. Email security gateways route attachments to format-specific decoders. If the gateway trusts the MIME type from the email header (which the sender controls) rather than the file's magic bytes, the routing decision is based on untrusted input. LLM document ingestion pipelines route documents to format-specific extractors before feeding text to the model. If the pipeline silently reclassifies a file and extracts text from the wrong format layer, the model receives text that does not correspond to what the user intended to submit.

In each case, the fix is the same: disclose the routing decision as a first-class finding before any content analysis. Routing transparency is a precondition for the content analysis to mean what it claims to mean.

# 6. Relationship to the Five-Layer Integrity Stack

The Mughlaq Trap sits at Layer 1 (file integrity) of the research program's five-layer integrity stack. The routing transparency principle applies at every layer: Layer 2 (information, Bayyinah al-Khabir) must disclose which source classification it used before reporting cross-source divergence. Layer 3 (code, Furqan) must disclose which type-checker was invoked before reporting type errors. Layer 4 (agents, Al-Khalifa) must disclose which task decomposition was chosen before reporting task completion. Layer 5 (models, Bilal) must disclose which verification head was consulted before reporting output-state divergence.

Routing transparency is a substrate-independent precondition for integrity verification. A system that silently reclassifies its input before analyzing it is performing rigor without possessing it, regardless of which layer it operates at. The Mughlaq Trap is the diagnostic for this failure mode.

# 7. Falsification Criteria

F1: If a scanner emits a Tier 0 format_routing_divergence finding and then renders the verdict as mukhfi (not mughlaq), the fix has not been applied correctly. The verdict floor is the architectural claim.

F2: If a user uploads a polyglot and the scanner returns mughlaq with the routing divergence finding visible, the fix is correct. If the user objects that they expected mukhfi because the content is adversarial, the objection is legitimate and warrants a configuration option (strict vs. permissive routing), not a change to the default.

F3: If a 4-byte .txt file returns score 1.0 (sahih), the scanner has claimed the file is sound when it has no analyzer capable of verifying text content. This is a Process 3 lie at the empty-content boundary.

F4: If the Mughlaq Trap vectors are rerun after v1.1.2 ships and V1 (polyglot) and V2 (spoofed) do not return mughlaq with a Tier 0 finding, the fix has not shipped. V3 (empty) and V4 (control) should retain their pre-fix behavior.

# 8. The Self-Correcting Pattern

The Mughlaq Trap is the Munafiq Protocol applied to the Munafiq Protocol's own product surface. The stress test was conducted because the live bayyinah.dev landing page publishes three rules of practice: 'we kill our own claims first, we publish what we miss, we test against equivalent methodology.' The third rule generated the test. The test found a gap. The gap became engineering work. This is the same self-correcting pattern observed in the research program's cross-text computational linguistics analysis (Ashraf, 2026), where a published methodology claim generated a correction that produced stronger findings.

The pattern: a discipline claim is published. The discipline claim generates an adversarial test the team would not otherwise have run. The test finds a real gap. The gap is corrected. The corrected system is stronger than the original. Sixteen of thirty claims killed in the precursor documents. Two of four vectors failed here. Different scale, same machine. The framework does not protect its own claims from scrutiny. It subjects them to the same diagnostic it applies to everything else.

# 9. Conclusion

A scanner with 40 mechanisms and dishonest routing is weaker than a scanner with 30 mechanisms and honest routing, because the dishonesty is the failure mode that the entire research program claims to solve.

The Mughlaq Trap found two failures in a live scanner whose research program is built on structural honesty. The failures were not in the detection mechanisms. They were in the routing layer that sits beneath all mechanisms. Tier 0 format routing transparency resolves this by making the routing decision a first-class finding, disclosed before any content analysis, with a verdict floor that prevents the scanner from issuing confident verdicts on files whose identity is in dispute.

The fix ships in Bayyinah v1.1.2 as Day 1 of a 14-day milestone. The routing layer is the structural floor. Everything else is built on top of it.

*"And do not mix truth with falsehood,
and do not conceal the truth while you know it."
- Al-Baqarah 2:42*

# References

Arfeen, B. S. (2026). The Munafiq Protocol: A Four-Process Taxonomy for Diagnosing Performed Alignment in AI Systems. Zenodo. DOI: 10.5281/zenodo.19677111.

Arfeen, B. S. (2026). Bayyinah: A Pre-LLM File Integrity Scanner with Structural Honesty and Scan-Incomplete Reporting. Zenodo.

Ashraf, F. & Arfeen, B. S. (2026). Furqan: A Programming Language with Structural Honesty in the Lineage of Swift's Safe-by-Default Concurrency Model. Zenodo.

Ashraf, F. (2026). Cross-Text Computational Linguistics of Sacred Texts in Original Languages. Research briefing, Bayyinah Enterprises.

Greenblatt, R., Denison, C., Wright, B., et al. (2024). Alignment Faking in Large Language Models. arXiv:2412.14093.

Lattner, C. (2017). Swift Concurrency Manifesto. GitHub Gist. Retrieved April 25, 2026, from https://gist.github.com/lattner/31ed37682ef1576b16bca1432ea9f782

*Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.*

---

# Bismillah ir-Rahman ir-Rahim
