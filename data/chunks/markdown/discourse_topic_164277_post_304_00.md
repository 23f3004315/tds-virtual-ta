---
chunk_id: discourse_topic_164277_post_304_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/304
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 124
username: carlton
post_number: 304
topic_id: 164277
---

## Post #304 by carlton

**Direct Link**: [Post #304](https://discourse.onlinedegree.iitm.ac.in/t/164277/304)

If you are using the function calling approach, you could just parse the ‘#’ and change it to ‘number’ and then send the prompt to the llm for that particular task.

Or another approach is tell the llm,

If you ever see the phrase ‘count the # of’ in a task, please interpret it as ‘count the number of’. For example

Count the # of Fridays means

Count the number of Fridays
