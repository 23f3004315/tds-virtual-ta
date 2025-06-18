---
chunk_id: course_prompt_engineering_003
source_url: https://tds.s-anand.net/#/prompt-engineering
source_title: prompt-engineering
content_type: course
tokens: 570
---

uides/prompt-engineering#tactic-ask-the-model-to-adopt-a-persona)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/assign-role)

### Use XML to structure your prompt

Use XML tags to separate different parts of the prompt clearly. This helps the model understand structure and requirements.

---

- **BAD**: _Here’s what I want: Provide a summary and then an example._ (Reason: Unstructured, no clear separation of tasks.)
- **GOOD**:
 ```xml
 
 Provide a summary of the concept of machine learning.

Then provide a simple, concrete example of a machine learning application (e.g., an email spam filter).
 
 ```
 (Reason: Uses XML tags to clearly distinguish instructions from examples.)

> Think of your request like a box. XML tags are neat little labels on that box.
> They help keep parts sorted, so nothing gets lost in the shuffle.

[Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
| [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering#tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input)
| [Google](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts)

### Use Markdown to format your output

Encourage the model to use Markdown for headings, lists, code blocks, and other formatting features to produce structured, easily readable answers.

- **BAD**: _Give me the steps in plain text._ (Reason: No specific formatting instructions, less readable.)
- **GOOD**: _Provide the steps in a markdown-formatted list with ### headings for each section and numbered bullet points._ (Reason: Directly instructs to use Markdown formatting, making output more structured and clear.)
- **BAD**: _Correct the spelling and show the corrections._ (Reason: No specific formatting instructions)
- **GOOD**: _Correct the spelling, showing &lt;ins&gt;additions&lt;/ins&gt; and &lt;del&gt;deletions&lt;/del&gt;._ (Reason: Directly instructs to use HTML formatting, making output more structured and clear.)

> Markdown is a simple formatting language that all models understand.
> You can have them add neat headings, sections, bold highlights, and bullet points.
> These make complex documents more scannable and easy on the eyes.

### Use JSON for machine-readable output

When you need structured data, ask for a JSON-formatted response. This ensures the output is machine-readable and organized.

- **BAD**: _Just list the items._ (Reason: Unstructured plain text makes parsing harder.)
- **GOOD**:
