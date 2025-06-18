---
chunk_id: discourse_topic_163247_post_156_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/156
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 175
username: Nomad
post_number: 156
topic_id: 163247
---

## Post #156 by Nomad

**Direct Link**: [Post #156](https://discourse.onlinedegree.iitm.ac.in/t/163247/156)

Getting the same issue -

`# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
 - |
 Generate a curl command to fetch ONLY the top 18 most-starred repositories
 from the "stripe" organization using the GitHub API.
 Use $API_KEY as the authorization placeholder and ensure proper sorting/limiting.

providers:
 - id: openrouter:openai/gpt-4o-mini
 config:
 max_tokens: 1024
 - id: openrouter:openai/gpt-4.1-nano
 config:
 max_tokens: 1024
 - id: openrouter:google/gemini-2.0-flash-lite-001
