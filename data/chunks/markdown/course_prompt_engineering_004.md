---
chunk_id: course_prompt_engineering_004
source_url: https://tds.s-anand.net/#/prompt-engineering
source_title: prompt-engineering
content_type: course
tokens: 571
---

 bullet points.
> These make complex documents more scannable and easy on the eyes.

### Use JSON for machine-readable output

When you need structured data, ask for a JSON-formatted response. This ensures the output is machine-readable and organized.

- **BAD**: _Just list the items._ (Reason: Unstructured plain text makes parsing harder.)
- **GOOD**:

---

````markdown
 Organize as an array of objects in a JSON format, like this:

```json
 [
 { "name": "Item 1", "description": "Description of Item 1" },
 { "name": "Item 2", "description": "Description of Item 2" },
 { "name": "Item 3", "description": "Description of Item 3" }
 ]
 ```
 ````

(Reason: Instructing JSON format ensures structured, machine-readable output.)

Note: Always use [JSON schema](playground#attachments) if possible. [JSON schema](https://json-schema.org/) is a way to describe the structure of JSON data. An easy way to get the JSON schema is to give ChatGPT sample output and ask it to generate the schema.

> Imagine you’re organizing data for a big project. Plain text is like dumping everything into one messy pile — it’s hard to find what you need later.
> JSON, on the other hand, is like packing your data into neat, labeled boxes within boxes.
> Everything has its place: fields like ‘name,’ ‘description,’ and ‘value’ make the data easy to read, especially for machines.
> For example, instead of just listing items, you can structure them as a JSON array, with each item as an object.
> That way, when you hand it to a program, it’s all clear and ready to use.

### Prefer Yes/No answers

Convert rating or percentage questions into Yes/No queries. LLMs handle binary choices better than numeric scales.

- **BAD**: _On a scale of 1-10, how confident are you that this method works?_ (Reason: Asks for a numeric rating, which can be imprecise.)
- **GOOD**: _Is this method likely to work as intended? Please give a reasoning and then answer Yes or No._ (Reason: A binary question simplifies the response and clarifies what’s being asked.)

> Don’t ask ‘On a scale of one to five...’. Models are not good with numbers.
> They don't know how to grade something 7 versus 8 on a 10 point scale. ‘Yes or no?’ is simple. It’s clear. It’s quick.
> So, break your question into simple parts that they can answer with just a yes or a no.

### Ask for reason first, then the answer
