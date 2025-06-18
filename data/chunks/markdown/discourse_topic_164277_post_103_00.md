---
chunk_id: discourse_topic_164277_post_103_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/103
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 220
username: carlton
post_number: 103
topic_id: 164277
---

## Post #103 by carlton

**Direct Link**: [Post #103](https://discourse.onlinedegree.iitm.ac.in/t/164277/103)

Hi Andrew,

You have done a great job with the Phase A tasks. Very methodical, well structured, logical and even incorporates (unnecessarily) two different ways of evaluating its performance via local llm or the project proxy.

I just want to forewarn you (and others who are tempted to just blindly copy and paste) that evaluate.py is not meant to give you an exact expectation of what prompts will be sent to your application.

**In other words getting 10/10 in `evaluate.py` does NOT guarantee 10/10 or even 5/10 or 1/10 in the real evaluation.**

So do not write your code so rigidly that it will only work in the very strict interpretation of `evaluate.py`. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general *idea* of the task.
