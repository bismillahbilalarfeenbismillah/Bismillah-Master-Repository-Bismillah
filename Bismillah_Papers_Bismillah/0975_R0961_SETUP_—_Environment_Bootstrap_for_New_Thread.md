# Bismillah ir-Rahman ir-Rahim

# R0961 -- SETUP — Environment Bootstrap for New Thread

**Chronological Index:** 975 of 995  
**Date:** Undated  
**Section:** IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)  
**Source File:** SETUP.md.pdf  
**Source Format:** pdf  
**SHA-256:** `d0b548a3f7d21208bf8f09f157669c24a9764ccc634c939db13d7a1e24cb3bf6`  

---

## R0961 · SETUP — Environment Bootstrap for New Thread

- section: IX. Multi-Model Audit Trail (dispatches, seat reports, councils, ledgers)
- source_file: SETUP.md.pdf
- source_format: pdf
- text_sha256: d0b548a3f7d21208bf8f09f157669c24a9764ccc634c939db13d7a1e24cb3bf6

SETUP — Environment Bootstrap for New Thread
The new co-work thread will need the following to become productive. Most of this should
be uploaded or re-created on the new thread's filesystem at /home/claude/work/ (or
equivalent).

Required Files (in this handoff folder)
code/solver_v2.py — scoring and test harness (core tool)
code/task_mapping.json — task number → ARC-AGI hash
code/arc_dsl_solvers.py — Hodel's 400 reference solvers (DSL source)
solutions.tar.gz — all 314 verified ONNX solvers (extract to solutions/ )

Required but NOT in This Folder (get from project or Kaggle)
Task JSONs (400 files, ~93 MB)

Originally at /home/claude/work/data/task{001..400}.json in the dev env.
These are derived from ARC-AGI 1 public task files. Each contains:
json

{
"train": [{"input": [[...]], "output": [[...]]}, ...],
"test": [{"input": [[...]], "output": [[...]]}]
}


Source: Download the ARC-AGI dataset (https://github.com/fchollet/ARC-AGI) and re-map
via task_mapping.json .
Python Dependencies
bash

pip install onnx onnxruntime numpy
# Optional (for profiling):
pip install onnx_tool

Directory Layout to Create on New Thread
/home/claude/work/
├── solutions/
├── data/
├── arc_dsl/
│ └── solvers.py
├── solver_v2.py
├── task_mapping.json
└── test_inshirah3b/

← extract solutions.tar.gz here
← 400 task JSONs (from project)
← copy from handoff code/arc_dsl_solvers.py
← copy from handoff code/
← copy from handoff code/
← scratch directory for builds

Verification Commands (run after setup)
bash


cd /home/claude/work
# 1. Count solutions
ls solutions/ | wc -l
# Expected: 314
# 2. Count task data files
ls data/ | wc -l
# Expected: 400
# 3. Test solver_v2 imports
python3 -c "from solver_v2 import test_network, score_file; print('OK')"
# 4. Verify a known-good solver (e.g., task197)
python3 -c "
import json
from solver_v2 import test_network, score_file
with open('data/task197.json') as f: t = json.load(f)
r, w = test_network('solutions/task197.onnx', t)
print(f'task197: {r} right, {w} wrong')
print(f'Expected: ~10+ right, 0 wrong')
s = score_file('solutions/task197.onnx')
print(f'Score: {s}')
"

Expected: task197: <N> right, 0 wrong; Score: (11.69, …) or similar.
If the score tuple returns None, the profiler shim is missing or the .onnx
uses ArgMax (which onnx_tool cannot profile). This is OK for Kaggle (their
profiler handles ArgMax) but means local scoring is blind for that task.


First Commands After Compliance Declaration
bash

# Re-confirm state
cd /home/claude/work
ls solutions/ | wc -l
# → 314
diff <(ls solutions/ | sed 's/task//;s/\.onnx//' | sort) \
<(cat /path/to/handoff/reference/saved_list.txt)
# should be empty
# Then: read IN_PROGRESS_task009.md and begin attempt 3.

If Something Breaks
onnx import fails: pip install onnx==1.15.0 onnxruntime==1.16.3 (known-good
versions).
score_file returns None: solver uses ArgMax; OK for Kaggle, just can't measure
locally.
test_network returns wrong counts: check that grid dims aren't exceeding 30
(converter fails silently on > 30).
Build script fails opset check: verify opset_imports = [make_opsetid("", 10)] in
make_model .

---

# Bismillah ir-Rahman ir-Rahim
