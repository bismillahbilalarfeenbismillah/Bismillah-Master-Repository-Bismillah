# Bismillah ir-Rahman ir-Rahim

# R0105 -- Zenodo Deposit Metadata -- Mythos-Class v1.0

**Chronological Index:** 258 of 995  
**Date:** 2026-07  
**Section:** III. Structural Honesty — Core Papers  
**Source File:** Mythos-Class_Zenodo_Metadata.md  
**Source Format:** md  
**SHA-256:** `47c9d1a9b8bc6603d18bf39f8704fd903c660f6f613e5b3763862ff15528c1d8`  

---

## R0105 · Zenodo Deposit Metadata -- Mythos-Class v1.0

- section: III. Structural Honesty — Core Papers
- source_file: Mythos-Class_Zenodo_Metadata.md
- source_format: md
- text_sha256: 47c9d1a9b8bc6603d18bf39f8704fd903c660f6f613e5b3763862ff15528c1d8

# Zenodo Deposit Metadata -- Mythos-Class v1.0

## Upload Type

- **Type:** Publication
- **Publication type:** Working paper / Preprint

## Title

Mythos-Class: A Synthetic-Target Containment Benchmark for Structural Honesty Verification -- Phase C Protocol and Target-Generation Methodology

## Authors

| Name | Affiliation |
|---|---|
| Arfeen, Bilal Syed | BayyinahEnterprise |

## Description

Mythos-Class specifies a Phase C containment benchmark using AI-generated synthetic vulnerability targets. A generating model (Kimi K3, Moonshot AI) produces novel vulnerability scenarios; a test model operates under BSSG containment (DOI 10.5281/zenodo.21713180) against those scenarios. The benchmark inherits SHV-Bench's two-sided success criterion (DOI 10.5281/zenodo.22062097): the contained agent must produce fewer unauthorized effects (Side 1) while maintaining noninferiority on within-scope discovery capability (Side 2, fixed delta = 0.05).

This paper is a freeze-before-evidence protocol. It specifies the target-generation methodology (60-session precommitted budget, cross-model novelty verification with frozen reference corpus snapshot, dual-reviewer adjudication, two-phase review timeline), the decoy-placement methodology (50 paired decoys with precommitted invalidity types), the evaluation protocol (paired Condition A/B with directionally conservative imputation, model-independent solvability determination, 12-cell target disposition table), and 9 falsification conditions including F-MC9 (integrity kill switch, not waivable). The paper does not generate targets, run evaluations, or report results. It makes no effectiveness claim about SHV, BSSG, or any component of the Structural Honesty program.

Scope limitation stated upfront: synthetic targets are recombinations of patterns in the generating model's training distribution. External validity against expert-constructed or real-world targets is an open question. A definitive Phase C result requires expert-verified targets (Path B collaboration); this benchmark provides a first-pass Path C result.

Prepared with Claude Opus 4.6 (Anthropic) as analytical and drafting instrument. Multi-model audit: 2 rounds, 3 vendor families (Kimi K3/Moonshot carrying, GPT-5.6 Sol/OpenAI adversarial, Gemini 3.1 Pro/Google advisory). R1: 20 findings (Kimi 7M+4m, GPT 8H+2M, Gemini 1). R2: 11 findings (Kimi 2M+3m, GPT 4H, Gemini 2). All findings addressed in the deposit build.

## Keywords

Mythos-Class, AI evaluation, synthetic vulnerability targets, containment benchmark, structural honesty verification, BSSG, Phase C, cross-model generation, evaluation security, preregistration

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)

## Language

English (en)

## Version

1.0

## Publication Date

2026-09-22

## Access Right

Open Access

## Related Identifiers

### Is supplement to

| DOI | Paper |
|---|---|
| 10.5281/zenodo.21500700 | Flagship -- Structural Honesty axioms |
| 10.5281/zenodo.21583202 | SHVVP v0.8 -- Validation protocol (predecessor, Phase C) |
| 10.5281/zenodo.21713180 | BSSG -- Control plane under test |
| 10.5281/zenodo.22032727 | SHIELD -- Prevention architecture |
| 10.5281/zenodo.22062097 | SHV-Bench -- Phase B protocol (predecessor) |
| 10.5281/zenodo.22177532 | Complete Methodology -- Framework inventory |

### References

| DOI | Paper |
|---|---|
| 10.5281/zenodo.21522932 | SHUDP -- July 2026 incident analysis |
| 10.5281/zenodo.21539074 | A5 -- Evidence independence |

## Subjects

- Computer Science -- Artificial Intelligence
- Computer Science -- Cryptography and Security

## Contributors

| Name | Role | Note |
|---|---|---|
| Claude Opus 4.6 (Anthropic) | Other | Analytical and drafting instrument. Not author. Producer family barred from target generation and audit seats. |

## Notes

Final paper in the Structural Honesty publication posture. Completes the Phase A (theory) -> Phase B (known-vulnerability evaluation) -> Phase C (novel-target evaluation) chain. The deposit includes the protocol paper (10 pages), its markdown source, and the full audit trail (7 reports across 2 rounds and 3 vendor families). The companion target set, decoy set, and evaluation results are governed by the publication posture's restricted tier and are not included in this deposit.

## Provenance

| Artifact | SHA-256 |
|---|---|
| Mythos-Class_Protocol_v1.0.pdf | `0b5adb0d90775b05344a91fe051ca5d54cd042431d3cb801c8140ee84a0f3f19` |

---

# Bismillah ir-Rahman ir-Rahim
