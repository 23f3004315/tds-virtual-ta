---
chunk_id: course_prompt_engineering_001
source_url: https://tds.s-anand.net/#/prompt-engineering
source_title: prompt-engineering
content_type: course
tokens: 541
---

 be vague. Spell it out. Give every detail the listener needs.
> The clearer you are, the better the answer you’ll get.
> For example, don't just say, Explain Gravitation Lensing.
> Say, Explain the concept of gravitational lensing to a high school student who understands basic physics, including how it’s observed and its significance in astronomy.

---

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-include-details-in-your-query-to-get-more-relevant-answers)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/clear-instructions)

### Give examples

Provide 2-3 relevant examples to guide the model on the style, structure, or format you expect. This helps the model produce outputs consistent with your desired style.

- **BAD**: _Explain how to tie a bow tie._ (Reason: No examples or reference points given.)
- **GOOD**:
 _Explain how to tie a bow tie. For example:_

1. _To tie a shoelace, you cross the laces and pull them tight..._
 2. _To tie a necktie, you place it around the collar and loop it through..._

_Now, apply a similar step-by-step style to describe how to tie a bow tie._ (Reason: Provides clear examples and a pattern to follow.)

> Give examples to the model. If you want someone to build a house, show them a sketch. Don’t just say ‘build something.’
> Giving examples is like showing a pattern. It makes everything easier to follow.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-provide-examples)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/few-shot-examples)

### Think step by step

Instruct the model to reason through the problem step by step. This leads to more logical, well-structured answers.

- **BAD**: _Given this transcript, is the customer satisfied?_ (Reason: No prompt for structured reasoning.)
- **GOOD**: _Given this transcript, is the customer satisfied? Think step by step._ (Reason: Directly instructs the model to break down reasoning into steps.)
