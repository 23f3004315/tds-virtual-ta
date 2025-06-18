---
chunk_id: discourse_topic_164277_post_103_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/103
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 297
username: carlton
post_number: 103
topic_id: 164277
---

.**

So do not write your code so rigidly that it will only work in the very strict interpretation of `evaluate.py`. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general *idea* of the task.

---

That said, `evaluate.py` is a good way to know what to expect. Some of Phase A tasks although given a detailed specification in the project description, will still be given challenging prompts (i.e. hard difficulty, and requires some clever self correcting mechanism). Some of the tasks will be given straight forward prompt (i.e. easy for your application). Some of the tasks will be given with some level of parameterisation that deviates from the strict interpretation (i.e. medium difficulty).

Hope that helps with how you deal with Phase B tasks (and making your Phase A more robust to a stronger evaluation.)

**A word of caution:** *(i.e. this is just some advice, not a set in stone recommendation)* Your requirements.txt is massive. If your code does not execute a task (*possibly your first task*) within 20 seconds (on our server) then it will fail that task. You might want to consider a dynamic, flexible way of installing only required libraries when necessary and keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.

Kind regards
