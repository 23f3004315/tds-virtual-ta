---
chunk_id: discourse_topic_171141_post_289_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/289
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 305
username: thinkmachine
post_number: 289
topic_id: 171141
---

 goal was purely exploratory — to explore the boundaries of what’s possible **within the scope of the problem statement**.

What began as just another (pun intended) *tedious* assignment slowly evolved into a hobbyist research project on LLM agents.

*(…caution: long post ahead )*

---

I noticed that **test cases in Project 1 and 2 were highly specific and often overlapping on Python &amp; Shell use**. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the **inherent randomness in LLM-generated payloads**. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.

Some might suggest using `temperature=0` to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.
