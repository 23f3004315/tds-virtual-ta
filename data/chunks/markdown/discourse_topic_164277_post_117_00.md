---
chunk_id: discourse_topic_164277_post_117_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/117
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 166
username: 23f2000983
post_number: 117
topic_id: 164277
---

## Post #117 by 23f2000983

**Direct Link**: [Post #117](https://discourse.onlinedegree.iitm.ac.in/t/164277/117)

I’m getting an error in task a2, def do_a2():

“”“Format markdown using prettier”“”

format_md_path = DATA_ROOT / “format.md”

subprocess.Popen([“prettier”, str(format_md_path), “–write”, “–parser”, “markdown”])

print(“data formatted successfully”)

any idea how to fix this? Also in A8, a 5 and a 3 is getting interchanged. Can someone help why that is hapening, I changed the prompt to include caution about not switching 3 and 5 as well, that didn’t help either
