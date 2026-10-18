# Bismillah ir-Rahman ir-Rahim

# R0558 -- audit_chain_log_F22_F26.csv

**Chronological Index:** 224 of 995  
**Date:** 2026-05-07  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** audit_chain_log_F22_F26.csv  
**Source Format:** csv  
**SHA-256:** `be3e88b178e8d979189bacd11f3503691886da2af03e49246d662a9cf48b21de`  

---

## R0558 · audit_chain_log_F22_F26.csv

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: audit_chain_log_F22_F26.csv
- source_format: csv
- text_sha256: be3e88b178e8d979189bacd11f3503691886da2af03e49246d662a9cf48b21de

finding_id,counter,global_round,phase_round,timestamp,repository,version,step,error_code,substrate_layer,scope_class,severity,fix_size_loc,fix_size_class,fix_location,root_cause,closure_shape,regularities
F22,B,38,29,2026-05-07,furqan-lint,0.11.2,step_2-3_dispatch,CASM-V-001,verifier_dispatch,whitelist_alignment,LOW,21,few_lines,verification.py,whitelist did not include rust adapter module path,A,"R1,R11"
F23,B,39,30,2026-05-07,furqan-lint,0.11.3,step_4_install,CASM-V-021,ci_install_matrix,extras_gap,LOW,1,one_word,ci.yml,CI workflow missing onnx extra for gate11 job,A,"R1,R2,R8"
F24,B,40,31,2026-05-07,furqan-lint,0.11.4,step_4_import,CASM-V-021,sigstore_api_drift,api_path_drift,LOW,3,few_lines,verification.py,sigstore-python TrustedRoot import path changed between versions,A,"R1,R2,R3,R5"
F25,B,41,32,2026-05-08,furqan-lint,0.11.5,step_6_identity,CASM-V-032,policy_construction,literal_vs_regex,LOW,1,one_word,ci.yml,Identity policy built with regex method when policy expects literal method,A,"R1,R2,R5,R6,R8"
F26,B,42,33,2026-05-08,furqan-lint,0.11.6,step_8_surface,SyntaxError,extractor_dispatch,wrong_language_dispatch,LOW,30,~30_lines,surface_extraction.py,extract_public_surface dispatches all files to Python ast.parse with no extension routing,A,"R1,R2,R7,R9,R11"

---

# Bismillah ir-Rahman ir-Rahim
