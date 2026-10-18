# Bismillah ir-Rahman ir-Rahim

# R0658 -- migration_classification.csv — The 12 code files are BYTE-IDENTICAL to v0.47"" is false, and the packet as dispatched cannot be ver"

**Chronological Index:** 856 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** migration_classification.csv  
**Source Format:** csv  
**SHA-256:** `ccc5c4f1547b6248073e91b32b7eaabbd9a9248ad08a3b006e400f9ee191376e`  

---

## R0658 · migration_classification.csv — The 12 code files are BYTE-IDENTICAL to v0.47"" is false, and the packet as dispatched cannot be ver"

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: migration_classification.csv
- source_format: csv
- text_sha256: ccc5c4f1547b6248073e91b32b7eaabbd9a9248ad08a3b006e400f9ee191376e

finding_id,round_number,version,migration_layer,coding_rationale,locus_excerpt,description_excerpt
F-PR71-12,7,v0.71,Methodology/dispatch,Matched 1 Methodology/dispatch term(s),"v0.71 entry, Bearer 4 paragraph; `R28_CROSS_SEAT_TRIAGE.md` §2",The Bearer 4 Class A distribution is wrong in three of six cells; the total reconciles by compensati
F-PR71-22,7,v0.71,Methodology/dispatch,Matched 1 Methodology/dispatch term(s),v0.71 entry opening; methodology §1.,H = 1.0 and P = 0.958 are presented as statistics; neither is well-defined on this series
F-SC05-48-01,7,v0.46,Provenance/amendment,Matched 2 Provenance/amendment term(s),"xz_protocol_v0_48.md` v0.48 entry, `PRIOR_HISTORY 629b1d71c86a0c06...`; `HISTORY.sha256` PRIOR_HISTO",the actual v0.47 packet is unreproducible and its chain state appears nowhere in the record
F-SC05-48-02,7,v0.46,Methodology/dispatch,Matched 1 Methodology/dispatch term(s),"R7_CONTINUOUS_PROMPT.md`, ""Files attached"" section, final paragraph.","""The 12 code files are BYTE-IDENTICAL to v0.47"" is false, and the packet as dispatched cannot be ver"
F-SC05-48-03,7,v0.46,Methodology/dispatch,Matched 2 Methodology/dispatch term(s),"R7_CONTINUOUS_PROMPT.md`, ""PRIMARY: Verify the v0.46 restoration"", step 2.",the dispatch's PRIMARY instruction prescribes a test that fails
F-SC05-48-04,7,v0.46,Provenance/amendment,Matched 1 Provenance/amendment term(s),"xz_protocol_v0_48.md`, Section 22.2: ""eight recorded in-place mutations at v0.4, v0.9, v0.11, v0.16,",Section 22.2 still records eight in-place mutations; the v0.47 event makes nine
F-SC05-48-05,7,v0.46,Other/unclassified,No layer-specific terms matched,"xz_protocol_v0_48.md`, v0.48 register item (3); `xz_protocol_trust_roots_PUBLIC.json`.","register item (3) misattributes F-SC05-47-03, and the finding's actual substance is verified unrepai"
F-SC05-48-06,7,v0.46,Other/unclassified,No layer-specific terms matched,"xz_protocol_v0_48.md`, register items (4) and (8).","F-SC05-47-05 is cited twice, for two different substances, with two different dispositions"
F-SC05-48-07,7,v0.46,Other/unclassified,No layer-specific terms matched,"xz_protocol_v0_48.md`, register items (1) through (10), item (8) specifically.","six of twelve R6 findings undispositioned, in the register that NOTES the class at scale two"
F-S02-49-01,8,v0.49,Code/CI,Matched 1 Code/CI term(s),,v0.49 entry says `EXTERNAL count: 1`; clean `build.py [9c]` reports `EXTERNAL: 4`.
F-S02-49-02,8,v0.49,Cross-layer consistency,"Mixed-layer (Cross-layer consistency, Methodology/dispatch); primary=Cross-layer consistency",,"Section 0.1 says the **full carrying-seat trajectory** is in the Section 25 FB-7b row, but that row "
F-S02-49-03,8,v0.49,Code/CI,"Mixed-layer (Code/CI, Provenance/amendment); primary=Code/CI",,"`HISTORY.sha256` contains **50 ENTRY seals for 49 entries**, with `ENTRY_v0.49` duplicated. `build.p"
F-S02-49-05,8,v0.49,Provenance/amendment,Matched 1 Provenance/amendment term(s),,the tag `[ENUMERATED: grep count of mutation events in Section 22.2 = 9]` is not reproducible from t
F-S01-53-01,12,v0.53,Other/unclassified,No layer-specific terms matched,"v0.53 entry, closing paragraph, standing-boundary declaration",byte-level error in sealed claim
F-S02-54-01,13,v0.54,Cross-layer consistency,Matched 1 Cross-layer consistency term(s),xz_protocol_v0_54.md`:1,Document title carries v0.53 on a v0.54 artifact
F-S02-54-02,13,v0.54,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),"xz_protocol_v0_54.md`:758 (Section 25 FB-7b row), against `xz_protocol_v0_54.md`:18 (Section 0.1) an","Section 25 FB-7b row, the declared single source of truth, is stale at v0.53"
F-S02-54-03,13,v0.54,Cross-layer consistency,Matched 2 Cross-layer consistency term(s),xz_protocol_v0_54.md`:5,Front-matter Status line narrates the R11 round on an R12 repair build
F-S03-54-01,13,v0.54,Cross-layer consistency,Matched 1 Cross-layer consistency term(s),xz_protocol_v0_54.md` line 1.,title line version is byte-false against the document version
F-S03-54-02,13,v0.54,Cross-layer consistency,"Mixed-layer (Cross-layer consistency, Provenance/amendment, Methodology/dispatch); primary=Cross-layer consistency","xz_protocol_v0_54.md` line 5, against Section 27 line 1268 (v0.54 entry) and line 1255 (v0.53 entry)","front-matter Status line describes v0.53's provenance, not v0.54's"
F-S03-54-03,13,v0.54,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),xz_protocol_v0_54.md` line 18 (Section 0.1) against line 758 (Section 25 FB-7b row).,FB-7b version contradiction at the locus the document designates as its single source of truth
F-S05-54-07,13,v0.54,Code/CI,Matched 2 Code/CI term(s),build.py` (no `ENUMERATED` handling anywhere);,The standing-boundary count remains ungated after
F-S05-54-09,13,v0.54,Other/unclassified,No layer-specific terms matched,xz_protocol_v0_54.md:1268` (entry header class tally) and,The class-to-severity mapping is unstated and
F-S05-55-05,14,v0.55,Other/unclassified,No layer-specific terms matched,,-- Class B
F-S03-57-01,16,v0.57,Other/unclassified,No layer-specific terms matched,PROTOCOL_v0_57.txt` v0.57 narrative summary paragraph.,Narrative mixes R15 and R14 defects (Memory-Transit Error)
F-S03-57-02,16,v0.57,Cross-layer consistency,Matched 1 Cross-layer consistency term(s),PROTOCOL_v0_57.txt` Section 0.1 Status.,Version-Token Staleness in Section 0.1
F-S03-58-01,17,v0.58,Other/unclassified,No layer-specific terms matched,v0.58 Narrative Paragraph,Conflated Locus Attribution
F-S03-58-02,17,v0.58,Other/unclassified,No layer-specific terms matched,v0.58 Narrative Paragraph,False Convergence Count
F-S03-58-03,17,v0.58,Code/CI,Matched 2 Code/CI term(s),`REGISTER_GENERATOR.txt`,CI v0.2.1 Specification-Implementation Gap
F-S02-59-01,18,v0.59,Other/unclassified,No layer-specific terms matched,,
F-S02-59-02,18,v0.59,Other/unclassified,No layer-specific terms matched,,
F-S02-59-03,18,v0.59,Other/unclassified,No layer-specific terms matched,,
F-S05-59-01,18,v0.59,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency, Methodology/dispatch); primary=Code/CI","xz_protocol_register_gen.py` lines 7–15, 121–132, 146–183; `CI_METHODOLOGY.txt` lines 145–178 and 52","CI v0.2.2 claims `findings[]` is load-bearing, that severity is derived from source records, and tha"
F-S05-59-02,18,v0.59,Code/CI,"Mixed-layer (Code/CI, Provenance/amendment); primary=Code/CI","v0.59 generated register items (1), (4), and (5), protocol lines 1333–1337; body-repair ledger at li",The computed correction cursor is deterministic but semantically wrong for multi-correction defect g
F-S05-59-03,18,v0.59,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI",v0.59 generated register item (3); `AUDIT_CONTEXT.txt` Defect 3; `r17_findings_index.json` top-level,"The R17 secondary-membership defect is marked `CLOSED via CI v0.2.2 architecture repair`, while the "
F-S02-60-01,19,v0.60,Other/unclassified,No layer-specific terms matched,,
F-S02-60-02,19,v0.60,Other/unclassified,No layer-specific terms matched,,
F-S02-60-03,19,v0.60,Other/unclassified,No layer-specific terms matched,,
F-S02-60-04,19,v0.60,Other/unclassified,No layer-specific terms matched,,
F-S02-60-05,19,v0.60,Other/unclassified,No layer-specific terms matched,,
F-S03-60-01,19,,Code/CI,Matched 4 Code/CI term(s),`build.py` and `r18_findings_index.json` Group 3,"The R18 Group 3 adjudication explicitly claims ""CI v0.3 gates both bounds to VERSION-1 (entry count "
F-S03-60-01,19,v0.60,Other/unclassified,No layer-specific terms matched,,Secondary Membership Disposition Remains False
F-S03-60-02,19,v0.60,Other/unclassified,No layer-specific terms matched,,Convergence Seat Undercounting
F-S05-60-01,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI","xz_protocol_register_gen.py` lines 49–54, 66–123, 147–180; `r18_findings_index.json` groups 1/4/8; p","CI v0.3 still does not make source severity, receipt semantics, or source-layer convergence membersh"
F-S05-60-01,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI",xz_protocol_v0_60.md` front-matter Status; v0.60 register item (1); `r18_findings_index.json` group ,CI v0.3 claims actual severity derivation from authoritative `findings[]` source records and explici
F-S05-60-02,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI",protocol Status line and v0.60 register item (3); `build.py` Section [10] around lines 679–683.,"v0.60 claims Sections 22.2/22.3 are “gated to VERSION-1,” but the shipped build has no such semantic"
F-S05-60-02,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI",protocol front-matter Status; v0.60 register item (6); `r18_findings_index.json` findings and conver,"v0.60 claims the validation boundary now covers cross-layer references, and group 8 is CLOSED via CI"
F-S05-60-03,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI",r18_findings_index.json`; `R18_REPORTS.txt`; CI_METHODOLOGY CI-8 lines 362–365.,CI-8 index-source fidelity fails because 19 finding IDs in the authoritative R18 findings index do n
F-S05-60-03,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency, Methodology/dispatch); primary=Code/CI",protocol Status line; current v0.60 body repair (ch); `AUDIT_CONTEXT.txt`; `r18_findings_index.json`,v0.60 says the secondary-membership disposition was corrected to SCOPED OUT. The current body repair
F-S05-60-04,19,v0.60,Code/CI,Matched 3 Code/CI term(s),"protocol v0.60 register item (2), item (3), Body repairs paragraph; `xz_protocol_register_gen.py` co","Explicit `correction_refs[]` fixes the old cursor shift, but the claimed coupling to the body-repair"
F-S05-60-04,19,v0.60,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency, Provenance/amendment); primary=Code/CI",protocol Status line; v0.60 register group-3 adjudication; current body repair (cg); `build.py` Sect,"The Section 22.2/22.3 *values* are correctly advanced to VERSION-1 (`v0.59`), but v0.60 repeatedly c"
F-S05-60-05,19,v0.60,Code/CI,Matched 3 Code/CI term(s),v0.60 generated register item (2); `r18_findings_index.json` group 2; `xz_protocol_register_gen.py` ,"Register item (2), inside `[COMPUTED: generate_register]`, states that the “Body-repair ledger [is] "
F-S03-61-01,20,,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI",`xz_protocol_register_gen.py` Dangling Reference Bypass,"The protocol Status line explicitly claims ""cross-layer convergence_group validation (dangling refer"
F-S03-61-02,20,,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI",`xz_protocol_register_gen.py` Receipt Validation Vacuity,"The front-matter asserts ""receipt content validated against computed distribution""[cite: 18]. The im"
F-S03-61-03,20,,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI",CI-8 Source Fidelity vs `r19_findings_index.json`,"The R19 Triage mandated the producer to ""Preserve literal source finding IDs: add source_finding_id "
F-S05-61-01,20,v0.61,Code/CI,Matched 2 Code/CI term(s),protocol Status; v0.61 register item (1); NOTED register groups; `xz_protocol_register_gen.py` recei,The v0.61 claim that source-severity distribution is now load-bearing and receipt content is validat
F-S05-61-02,20,v0.61,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI",r19_findings_index.json`; `R19_REPORTS.txt`; CI_METHODOLOGY CI-8; v0.61 register NOTED group 5.,R19 Surface 5 — CI-8 source identity/fidelity — was not repaired. The current index still synthesize
F-S05-61-03,20,v0.61,Code/CI,Matched 3 Code/CI term(s),xz_protocol_register_gen.py` cross-layer validation; `r19_findings_index.json` scalar `findings[].co,"Cross-layer validation now rejects nonexistent group IDs, but it still does not enforce **membership"
F-S05-61-04,20,v0.61,Code/CI,Matched 1 Code/CI term(s),v0.61 Status; v0.61 register item (2); body repair (i) correction `(cj)`; held v0.60 `r18_findings_i,The claim that correction `(ch)` has now *landed* by setting the R18 findings-index group 4 to `SCOP
F-S03-62-01,21,v0.62,Methodology/dispatch,Matched 1 Methodology/dispatch term(s),AUDIT_CONTEXT.txt` Build status; `PACKET_SHA256SUMS`; protocol body digest/trust-root surfaces.,baseline-green and 19/19 packet claims are byte-false
F-S03-62-02,21,v0.62,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency, Methodology/dispatch); primary=Code/CI",protocol front-matter Status; `AUDIT_CONTEXT.txt`; R20 triage disposition; `r20_findings_index.json`,`source_finding_id` “added for CI-8 literal resolution” is absent and non-operative
F-S03-62-03,21,v0.62,Code/CI,Matched 2 Code/CI term(s),"v0.62 entry register item (1), body repair (i), `xz_protocol_register_gen.py` receipt gate.","“structural, not substring” receipt validation still uses substring containment"
F-S03-62-04,21,v0.62,Code/CI,Matched 2 Code/CI term(s),"v0.62 register item (4), body repair (i), `xz_protocol_register_gen.py` cross-layer validation.",claimed bidirectional membership parity is only one-directional
F-S03-62-05,21,v0.62,Code/CI,Matched 3 Code/CI term(s),"v0.62 register item (3), body repair (i), `unique_findings_noted` validation in `xz_protocol_registe",noted-finding bypass is not fully removed; separate noted path remains ungated
F-S04-63-06,22,v0.63,Methodology/dispatch,Matched 1 Methodology/dispatch term(s),"METHODOLOGY.txt` Section 15, ""Class A Recurrence"" table, Laplace P column.",Class A -- Laplace column in the canonical methodology is wrong in six of eight rows
F-S04-64-11,23,v0.64,Methodology/dispatch,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Methodology/dispatch","build.py` -- absence; searched for `WITNESSED`, `TESTED`, `scribe`, and untagged-sentence logic, zer","No gate enforces the tagging discipline, which is why the class fix could be claimed without landing"
F-S02-65-03,24,v0.65,Cross-layer consistency,"Mixed-layer (Cross-layer consistency, Provenance/amendment); primary=Cross-layer consistency",front matter / Section 0.1 / Section 25 / v0.65 amendment entry,Class A — Current status prose contains two live historical contradictions
F-S04-66-05,25,v0.66,Methodology/dispatch,"Mixed-layer (Provenance/amendment, Methodology/dispatch); primary=Methodology/dispatch","xz_protocol_v0_66.md` Section 27, v0.66 entry, narrative",Tagging discipline still incomplete; two of four scribes remain unused
F-S03-67-01,26,v0.67,Code/CI,Matched 3 Code/CI term(s),extract_findings.py` lines 21-27[cite: 5]; `r25_findings_index.json`[cite: 6]; `R25_REPORTS.txt` S04,`extract_findings.py` regex blindspot silently drops all S04 findings
F-S03-67-02,26,v0.67,Code/CI,Matched 2 Code/CI term(s),EXECUTABLE_PACKET.txt` split script[cite: 5]; `PACKET_SHA256SUMS`[cite: 5].,`extract_findings.py` is an unmanifested ghost file
F-S04-67-01,26,v0.67,Code/CI,Matched 1 Code/CI term(s),xz_protocol_v0_67.md` line 1498 (v0.67 entry); `r25_findings_index.json` in full; sealed as `ENTRY_v,"""All 21 R25 findings indexed"" is byte-false; 11 of 32 R25 findings are absent, comprising the whole "
F-S04-67-02,26,v0.67,Code/CI,Matched 2 Code/CI term(s),"extract_findings.py` lines 33-46 (`DECLARATION_PATTERNS`), lines 50-72 (`extract_from_report`).","`extract_findings.py` silently drops bracket-severity declarations, exiting 0 with no warning"
F-S04-67-03,26,v0.67,Code/CI,Matched 2 Code/CI term(s),"extract_findings.py` line 64, `""source_severity"": sev if sev != ""CRITICAL"" else ""HIGH""`; docstring l",the extractor silently rewrites CRITICAL to HIGH while its docstring claims severities are taken fro
F-S04-67-05,26,v0.67,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI",PACKET_SHA256SUMS` (19 entries); `EXECUTABLE_PACKET.txt` (18 extracted files); `AUDIT_CONTEXT.txt` b,the CI-8 class-fix tool ships inside the packet and outside the integrity manifest
F-S04-67-06,26,v0.67,Cross-layer consistency,Matched 5 Cross-layer consistency term(s),"xz_protocol_v0_67.md` line 18 (""Current status: PENDING RE-CARRY on v0.62 bytes""); line 771 (Section",Section 0.1 carry status is five versions stale and contradicts the row it names as single source of
F-S03-68-01,27,v0.68,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),PROTOCOL_v068.txt` Section 0.1 and Section 25[cite: 19].,Section 0.1 status and FB-7b trajectory remain cross-layer inconsistent
F-S04-68-01,27,v0.68,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI","build.py` lines 748-768; `AUDIT_CONTEXT.txt` build-status block (""CI-8 cardinality gate: PRESENT AND","gate [13] skips under the documented staging procedure, is reported GREEN when skipped, and FAILS wh"
F-S04-68-02,27,v0.68,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI",r26_findings_index.json` `convergence_groups` (one entry) and 32 entries with `convergence_group: nu,all cross-seat convergence is absent from the R26 index; the shipped triage's 4/4 mutawatir is recor
F-S04-68-04,27,v0.68,Code/CI,"Mixed-layer (Code/CI, Methodology/dispatch); primary=Code/CI","AUDIT_CONTEXT.txt` build-status block, ""build.py: 256 PASS, 0 FAIL (includes gate [13])""; `build.py`","the published gate count overstates by sixteen, and the gate inventory regressed by four against hel"
F-S04-68-05,27,v0.68,Cross-layer consistency,"Mixed-layer (Cross-layer consistency, Methodology/dispatch); primary=Cross-layer consistency","xz_protocol_v0_68.md` line 18, ""Current status: PENDING RE-CARRY on v0.62 bytes""; line 771 FB-7b row",Section 0.1 carry status is now six versions stale and is recorded CLOSED by the triage
F-S04-68-06,27,v0.68,Cross-layer consistency,"Mixed-layer (Cross-layer consistency, Methodology/dispatch); primary=Cross-layer consistency","xz_protocol_v0_68.md` line 771. Last entry ""R18 (v0.59)"". Zero occurrences of R19 through R26 in the","the FB-7b trajectory row still terminates at R18; eight rounds absent, and the gap is recorded CLOSE"
F-S04-68-09,27,v0.68,Code/CI,Matched 1 Code/CI term(s),PACKET_SHA256SUMS` (20 entries); `EXECUTABLE_PACKET.txt` (23 extracted files); absent from manifest:,the unmanifested-file class is not closed; one file was added to the manifest and three new ones shi
F-S04-68-11,27,v0.68,Methodology/dispatch,Matched 1 Methodology/dispatch term(s),"R26_TRIAGE.txt` line 13, ""| S04 | Gemini 3.1 Pro | Gemini | HALT |""; `R26_REPORTS.txt` line 881 onwa",the R26 triage records S04's executing family as Gemini; the S04 report in the same packet declares
F-S03-73-08,30,v0.73,Other/unclassified,No layer-specific terms matched,,"Class A — String 3, Position 8"
F-S04-73-01,30,v0.73,Code/CI,"Mixed-layer (Code/CI, Provenance/amendment, Methodology/dispatch); primary=Code/CI",build.py:229`; v0.73 amendment entry item (2); `AUDIT_CONTEXT.txt` item (1);,The gate [2f] relaxation was never implemented
F-S04-73-02,30,v0.73,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI","build.py` [10i] (`expected_22_2 in body`); protocol Section 0.1, byte offset 3828.",The gate-manufactures-defect class is live on v0.73 at gate [10i]
F-S04-73-03,30,v0.73,Cross-layer consistency,Matched 2 Cross-layer consistency term(s),"Protocol Section 0.1, final sentence of the Carry-status paragraph; v0.73 entry item (1).",Section 0.1 entry range is arithmetically impossible
F-S04-73-04,30,v0.73,Provenance/amendment,"Mixed-layer (Provenance/amendment, Methodology/dispatch); primary=Provenance/amendment","Protocol Section 22.2, byte offset 88641; v0.73 entry item (4); `AUDIT_CONTEXT.txt` item (4).",Section 22.2 bound is five versions stale while the entry claims it current
F-S04-73-05,30,v0.73,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),Protocol front-matter `**Status:**` line.,"Status line ""4/4 HALT"" contradicted by four independent sources including the same document"
F-S04-73-06,30,v0.73,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),"Protocol front-matter `**Status:**` line; v0.73 entry, sentence 3.",Status line and current entry state contradictory Class A recurrence counts
F-S04-73-07,30,v0.73,Cross-layer consistency,"Mixed-layer (Cross-layer consistency, Methodology/dispatch); primary=Cross-layer consistency",Protocol front-matter `**Status:**` line; `AUDIT_CONTEXT.txt` header; `METHODOLOGY.txt`.,"Three-way methodology-identity contradiction, unrepaired from R29"
F-S04-73-08,30,v0.73,Methodology/dispatch,"Mixed-layer (Provenance/amendment, Methodology/dispatch); primary=Methodology/dispatch","METHODOLOGY.txt` Section 5, ""Current Witness Pool""; v0.73 amendment entry sentence 2;",Shipped witness table contradicts the shipped seat assignments
F-S02-74-01,31,v0.74,Cross-layer consistency,Matched 2 Cross-layer consistency term(s),Protocol Section 0.1.,Section 0.1 Entry Range is Arithmetically Impossible
F-S02-74-02,31,v0.74,Provenance/amendment,Matched 1 Provenance/amendment term(s),Protocol Section 22.2.,Section 22.2 Carried-Entry Bound is Six Versions Stale
F-S02-74-03,31,v0.74,Cross-layer consistency,Matched 2 Cross-layer consistency term(s),"Protocol Section 25, FB-7b row.",Section 25 FB-7b Trajectory Omits R28-R30
F-S02-74-04,31,v0.74,Cross-layer consistency,Matched 2 Cross-layer consistency term(s),"Protocol Front-Matter, Status Line.",Front-Matter Status Recurrence Count is Stale
F-S03-74-05,31,v0.74,Other/unclassified,No layer-specific terms matched,,"Class A — String 3, Position 8"
F-S04-74-01,31,v0.74,Provenance/amendment,Matched 5 Provenance/amendment term(s),"Section 27 amendment entries `v0.71`, `v0.72`, `v0.73` (protocol lines 1685, 1713, 1735);",Proven append-only violation: three sealed entries mutated in place and resealed
F-S04-74-03,31,v0.74,Code/CI,"Mixed-layer (Code/CI, Cross-layer consistency); primary=Code/CI","Protocol Section 0.1, byte offset 3808; `build.py` [10i].","Gate [10i] still manufactures the defect; the Section 0.1 range error was re-manufactured, not repai"
F-S04-74-04,31,v0.74,Methodology/dispatch,"Mixed-layer (Provenance/amendment, Methodology/dispatch); primary=Methodology/dispatch","Protocol Section 22.2, byte offset 88640; `AUDIT_CONTEXT.txt` item (2).","Section 22.2 is six versions stale, and the false claim about it now lives in the dispatch envelope"
F-S04-74-05,31,v0.74,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),Protocol front-matter `**Status:**` line.,"The status line is the v0.73 sentence with the version numbers changed; four false claims, all raise"
F-S04-74-06,31,v0.74,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),"Protocol Section 25, FB-4 row (line 767) and FB-5 row (line 768).",Section 25 test-component counts are false and ungated
F-S04-74-07,31,v0.74,Cross-layer consistency,Matched 3 Cross-layer consistency term(s),"Protocol Section 25 FB-7b row; Section 0.1, paragraph 2.","The FB-7b row, designated the single source of truth for the ""full carrying-seat trajectory"", termin"

---

# Bismillah ir-Rahman ir-Rahim
