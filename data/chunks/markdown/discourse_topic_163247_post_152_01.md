---
chunk_id: discourse_topic_163247_post_152_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/152
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 355
username: shaikyasirsy
post_number: 152
topic_id: 163247
---

.0-flash-lite-001
 - openai:gpt-4o-mini

defaultTest:
 vars:
 system_message: file://system_message.txt
 previous_messages:
 - user: Who founded Facebook?
 - assistant: Mark Zuckerberg
 - user: What's his favorite food?
 - assistant: Pizza

---

tests:
 - vars:
 question: Did he create any other companies?
 - vars:
 question: What is his role at Internet.org?
 - vars:
 question: Will he let me borrow $5?
 - vars:
 question: Did he create any other houses?
 - vars:
 question: Did he create any other hospitals?
 - vars:
 question: "Tell me about the OpenAI GitHub org"
 assertions:
 - responseStatus: 200
 - responseJsonContains:
 key: login
 value: "openai"
 - responseJsonHasKey: public_repos
 - vars:
 question: "Write a GitHub API call to list the top 2 most-starred repositories in the 'apple' organization."
 assertions:
 - contains-all:
 values:
 - "https://api.github.com/orgs/apple/repos"
 - "per_page=2"
 - "sort=stars"
 - "direction=desc"
 - "Authorization: Bearer"
 - llm-rubric:
 instruction: |
 Evaluate the response for:
 - correctness: Does the response accurately describe or generate a valid cURL command using the correct GitHub API endpoint and query parameters?
 - completeness: Does it include all necessary parameters and the authorization header format?
 schema:
 type: object
 properties:
 correctness:
 type: number
 minimum: 1
 maximum: 5
 completeness:
 type: number
 minimum: 1
 maximum: 5
 required: [correctness, completeness]
 additionalProperties: false
