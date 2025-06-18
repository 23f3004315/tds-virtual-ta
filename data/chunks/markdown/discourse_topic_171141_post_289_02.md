---
chunk_id: discourse_topic_171141_post_289_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/289
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 350
username: thinkmachine
post_number: 289
topic_id: 171141
---

rection based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.

---

**Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers**: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.

At the core of it, it’s all about **how much flexibility vs rigidity** we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.

Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,

Reason about the task, understand intent,
Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e. *design* a DAG, where each node can be a python step or a shell step or something else)
Execute those workflows (*walk* the DAG) observing the feedback at each step and reiterating if needed.
Observe the final result, and repeat if needed.
