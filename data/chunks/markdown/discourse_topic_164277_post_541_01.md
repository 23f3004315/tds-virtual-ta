---
chunk_id: discourse_topic_164277_post_541_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/541
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 229
username: Flibon
post_number: 541
topic_id: 164277
---

 header.
The payload is set as:

json

Copy

`{"model": "text-embedding-3-small", "input": ["Test"]}
`

Despite this, the response status is consistently 401 Unauthorized.

**Debug Output:**

Here’s a snippet of the debug output:

bash

Copy

---

`HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"
🔴 A9 failed: 'data'
`
This confirms that the issue is with the authentication rather than our processing logic.

What I Suspect

The token may be invalid, expired, or misconfigured.
There could be changes in the token permissions or endpoint requirements that I’m not aware of.
Alternatively, there might be an issue on the server side with token validation.

Request for Help
Has anyone else encountered this issue recently? Could someone verify if there are any changes to the authentication requirements for the embeddings endpoint? Any insights or updated instructions on how to ensure the token is valid and has the proper permissions would be greatly appreciated.

Thanks in advance for your assistance!
