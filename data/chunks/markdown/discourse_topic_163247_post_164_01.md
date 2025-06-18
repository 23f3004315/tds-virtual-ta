---
chunk_id: discourse_topic_163247_post_164_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/164
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 312
username: TheVishal
post_number: 164
topic_id: 163247
---

/gpt-4o-mini
 config:
 max_tokens: 1024
 - id: openrouter:openai/gpt-4.1-nano
 config:
 max_tokens: 1024
 - id: openrouter:google/gemini-2.0-flash-lite-001

---

tests:
 - vars:
 API_KEY: "ghp_example"
 assert:
 - type: regex
 value: 'https://api\.github\.com/orgs/linkedin/repos'
 name: "Uses correct endpoint"
 - type: regex
 value: 'per_page=16'
 name: "Limits to 16 repositories"
 - type: regex
 value: 'sort=stars'
 name: "Sorts by stars"
 - type: regex
 value: 'direction=desc'
 name: "Sorts in descending order"
 - type: regex
 value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
 name: "Includes authorization header with $API_KEY"
 - type: llm-rubric
 value: |
 The response should be a valid curl command that:
 - Uses the GitHub organization repositories endpoint for "linkedin"
 - Limits results to exactly 16 repositories
 - Sorts by stars in descending order
 - Uses $API_KEY as the authorization placeholder in the header
 name: "LLM rubric: task compliance"
`
Error: Error: Invalid promptfooconfig.yaml: Your config must include at least 5 test assertions.
@carlton @s.anand @Jivraj
