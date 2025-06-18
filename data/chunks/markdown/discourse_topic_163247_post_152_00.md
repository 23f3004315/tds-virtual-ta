---
chunk_id: discourse_topic_163247_post_152_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/152
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 211
username: shaikyasirsy
post_number: 152
topic_id: 163247
---

## Post #152 by shaikyasirsy

**Direct Link**: [Post #152](https://discourse.onlinedegree.iitm.ac.in/t/163247/152)

Error: Invalid promptfooconfig.yaml: Missing required assertion for: https://api.github.com/orgs/

for 14th Question

`# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
 - file://prompt.json

providers:
 - openai:gpt-4o-mini
 - openai:gpt-4o-mini
 - openrouter:openai/gpt-4o-mini
 - openrouter:openai/gpt-4.1-nano
 - openrouter:google/gemini-2.0-flash-lite-001
 - openai:gpt-4o-mini

defaultTest:
 vars:
 system_message: file://system_message.txt
 previous_messages:
 - user: Who founded Facebook?
 - assistant: Mark Zuckerberg
 - user: What's his favorite food?
 - assistant: Pizza
