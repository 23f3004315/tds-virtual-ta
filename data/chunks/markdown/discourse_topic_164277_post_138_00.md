---
chunk_id: discourse_topic_164277_post_138_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/138
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 279
username: Adithya
post_number: 138
topic_id: 164277
---

## Post #138 by Adithya

**Direct Link**: [Post #138](https://discourse.onlinedegree.iitm.ac.in/t/164277/138)

*For task A2*:

**A2**. Format the contents of `/data/format.md` using `prettier@3.4.2`, updating the file in-place

I am getting the following error:

`🔴 A2 failed: Command '['npx', 'prettier@3.4.2', '--stdin-filepath', '/data/format.md']' returned non-zero exit status 1.`

However, running a **POST request** to https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2 gives successful output.

`{"success":true,"message":"Formatted and verified successfully!"}% `

Here is my code snippet:

`def format_file(filepath):
 while True: # Loop until formatting and verification pass
 try:
 result = subprocess.run(
 ["npx", "prettier@3.4.2", "--write", filepath],
 check=False, # Don't raise exception automatically
 capture_output=True,
 text=True
 )

if result.returncode != 0:
 return {"success": False, "message": f"Prettier write failed: {result.stderr}"}
