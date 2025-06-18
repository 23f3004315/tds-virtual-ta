---
chunk_id: course_prompt_engineering_000
source_url: https://tds.s-anand.net/#/prompt-engineering
source_title: prompt-engineering
content_type: course
tokens: 428
---

## Prompt Engineering

Prompt engineering is the process of crafting effective prompts for large language models (LLMs).

One of the best ways to approach prompt engineering is to think of LLMs as a smart colleague (with amnesia) who needs explicit instructions.

The most authoritative guides are from the LLM providers themselves:

- [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/)
- [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design)
- [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)

Here are some best practices:

### Use prompt optimizers

They rewrite your prompt to improve it. Explore:

- [Anthropic Prompt Optimizer](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver)
- [OpenAI Prompt Generation](https://platform.openai.com/docs/guides/prompt-generation)
- [Google AI-powered prompt writing tools](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/ai-powered-prompt-writing)

### Be clear, direct, and detailed

Be explicit and thorough. Include all necessary context, goals, and details so the model understands the full picture.

- **BAD**: _Explain gravitation lensing._ (Reason: Vague and lacks context or detail.)
- **GOOD**: _Explain the concept of gravitational lensing to a high school student who understands basic physics, including how it’s observed and its significance in astronomy._ (Reason: Specifies the audience, scope, and focus.)

> When you ask a question, don’t be vague. Spell it out. Give every detail the listener needs.
> The clearer you are, the better the answer you’ll get.
> For example, don't just say, Explain Gravitation Lensing.
> Say, Explain the concept of gravitational lensing to a high school student who understands basic physics, including how it’s observed and its significance in astronomy.
