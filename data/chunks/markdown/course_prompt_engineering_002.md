---
chunk_id: course_prompt_engineering_002
source_url: https://tds.s-anand.net/#/prompt-engineering
source_title: prompt-engineering
content_type: course
tokens: 559
---

 problem step by step. This leads to more logical, well-structured answers.

- **BAD**: _Given this transcript, is the customer satisfied?_ (Reason: No prompt for structured reasoning.)
- **GOOD**: _Given this transcript, is the customer satisfied? Think step by step._ (Reason: Directly instructs the model to break down reasoning into steps.)

---

> Ask the model to think step by step. Don’t ask the model to just give the final answer right away.
> That's like asking someone to answer with the first thing that pops into their head.
> Instead, ask them to break down their thought process into simple moves — like showing each rung of a ladder as they climb.
> For example, when thinking step by step, the model could, A, list each customer question, B, find out if it was addressed, and C, decide that the agent answered only 2 out of the 3 questions.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#strategy-give-models-time-to-think)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/break-down-prompts)

### Assign a role

Specify a role or persona for the model. This provides context and helps tailor the response style.

- **BAD**: _Explain how to fix a software bug._ (Reason: No role or perspective given.)
- **GOOD**: _You are a seasoned software engineer. Explain how to fix a software bug in legacy code, including the debugging and testing process._ (Reason: Assigns a clear, knowledgeable persona, guiding the style and depth.)

> Tell the model who they are. Maybe they’re a seasoned software engineer fixing a legacy bug, or an experienced copy editor revising a publication.
> By clearly telling the model who they are, you help them speak with just the right expertise and style.
> Suddenly, your explanation sounds like it’s coming from a true specialist, not a random voice.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-ask-the-model-to-adopt-a-persona)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/assign-role)

### Use XML to structure your prompt

Use XML tags to separate different parts of the prompt clearly. This helps the model understand structure and requirements.
