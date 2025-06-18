---
chunk_id: discourse_topic_171141_post_206_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/206
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 321
username: thinkmachine
post_number: 206
topic_id: 171141
---

 alt="image" data-base62-sha1="m5oZT6ccNhYAMcg96GqKgDnNOWO" width="690" height="214" data-dominant-color="EEEFF1">image1272×395 25.7 KB

---

But here’s the catch:** Since the problem statement for Project 1 and Project 2 is nearly the same, I took the opportunity to improve upon my Project 1 and use it as the foundation for my Project 2 submission, which I did by:*

Implementing a ReAct-based workflow planning &amp; orchestration agent, inspired by the paper ReAct: Synergizing Reasoning and Acting in Language Models.
Implementing various tools for web-serping, web-scraping, read-eval-print-loops interpreters for quick calculations, etc.
Enhancing Shell-use &amp; Python-use by improving upon the existing code interpreter I had implemented for P1. This allowed the agent to dynamically generate and execute code without hardcoding anything.
Adding useful API endpoints, including an **`/api/`** multipart/form endpoint, alongside the existing **`/read`** and **`/run`** endpoints from Project 1, plus a **`/clear`** endpoint to reset the agent’s conversation memory if the context window gets saturated.
**Deploying the entire project on a paid GCP VM Instance with a static IP**, utilizing my own OpenAI API key while keeping OpenAI’s API as a fallback in case AIPROXY ever gave up.
