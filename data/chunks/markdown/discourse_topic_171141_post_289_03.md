---
chunk_id: discourse_topic_171141_post_289_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/289
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 360
username: thinkmachine
post_number: 289
topic_id: 171141
---

 appropriate (i.e. *design* a DAG, where each node can be a python step or a shell step or something else)
Execute those workflows (*walk* the DAG) observing the feedback at each step and reiterating if needed.
Observe the final result, and repeat if needed.

---

Interestingly, a similar framework was suggested in this ICLR 2022 paper. That was all the validation I needed to know I was stepping in the right direction.

To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of **general-purpose tools**:

A REPL executor (for quick calcs)
A Python script runner
A Shell executor

With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.

As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training &amp; tuning ML models autonomously, reporting results etc.) — that was **emergent behavior**, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research. *Frankly, I AM personally very keen about researching stuff!*

I am actually very thankful to the TDS course team &amp; @s.anand for devising such a thoughtful project that sparked some interesting ideas that I can tinker with. **Food for thought! Really!**
