---
chunk_id: discourse_topic_164277_post_64_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/64
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 137
username: s.anand
post_number: 64
topic_id: 164277
---

## Post #64 by s.anand

**Direct Link**: [Post #64](https://discourse.onlinedegree.iitm.ac.in/t/164277/64)

@21f3002390 - AI Proxy is working and you *did* get the result. You can ignore any `costError`. It won’t happen in the future anyway.

**What’s happening?** I was trying to generate a unique hash for each request, as a precursor to caching requests. But I made a mistake in the code. Specifically, `crypto.createHash` is not supported in CloudFlare. I fixed that by removing this. I’ll introduce caching later if required.
