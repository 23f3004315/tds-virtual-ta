---
chunk_id: discourse_topic_164277_post_541_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/541
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 303
username: Flibon
post_number: 541
topic_id: 164277
---

## Post #541 by Flibon

**Direct Link**: [Post #541](https://discourse.onlinedegree.iitm.ac.in/t/164277/541)

Hi everyone,

I’m running into an issue with the AI Proxy embeddings endpoint while executing the A9 task. Every time I send a POST request to:

bash

Copy

`https://aiproxy.sanand.workers.dev/openai/v1/embeddings
`
I receive a **401 Unauthorized** response. This, in turn, causes my code to fail with a `KeyError: 'data'` because the expected JSON response doesn’t include the `"data"` key.

What I’ve Tried

**Token Verification:**

I’m using the `AIPROXY_TOKEN` obtained by logging in at aiproxy.sanand.workers.dev with my IITM email.
The token is passed in the header as follows:

python

Copy

`"Authorization": f"Bearer {AIPROXY_TOKEN}"
`

I added debug prints to confirm that the token is being used correctly (printing the first few characters).

**API Request Details:**

The request includes the correct `Content-Type: application/json` header.
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
