---
chunk_id: course_prompt_engineering_005
source_url: https://tds.s-anand.net/#/prompt-engineering
source_title: prompt-engineering
content_type: course
tokens: 380
---

’. Models are not good with numbers.
> They don't know how to grade something 7 versus 8 on a 10 point scale. ‘Yes or no?’ is simple. It’s clear. It’s quick.
> So, break your question into simple parts that they can answer with just a yes or a no.

### Ask for reason first, then the answer

---

Instruct the model to provide its reasoning steps _before_ stating the final answer. This makes it less likely to justify itself and more likely to think deeper, leading to more accurate results.

- **BAD**: _What is the best route to take?_ (Reason: Direct question without prompting reasoning steps first.)
- **GOOD**: _First, explain your reasoning step by step for how you determine the best route. Then, after you’ve reasoned it out, state your final recommendation for the best route._ (Reason: Forces the model to show its reasoning process before giving the final answer.)

> BEFORE making its final choice, have the model talk through their thinking. Reasoning first, answer second.
> That way, the model won't be tempted to justify an answer that they gave impulsively. It is also more likely to think deeper.

### Use proper spelling and grammar

A well-written, grammatically correct prompt clarifies expectations. Poorly structured prompts can confuse the model.

- **BAD**: _xplin wht the weirless netork do? make shur to giv me a anser??_ (Reason: Poor spelling and unclear instructions.)
- **GOOD**: _Explain what a wireless network does. Please provide a detailed, step-by-step explanation._ (Reason: Proper spelling and clarity lead to a more coherent response.)

> If your question sounds like gibberish, expect a messy answer. Speak cleanly.
> When you do, the response will be much clearer.
