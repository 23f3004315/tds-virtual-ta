---
chunk_id: discourse_topic_171999_post_2_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171999/2
source_title: Project 1 solution repository link
content_type: discourse
tokens: 447
username: carlton
post_number: 2
topic_id: 171999
---

 "content": user_prompt},
 ],
 },
 )
 response.raise_for_status()
 return response.json()["choices"][0]["message"]["content"]

system_prompt = """The user will provide a task description.
Write one or more `bash` or `python` scripts to execute the task.

CODING RULES:

---

- uv, the Python runner, is ALREADY installed. Run with `uv run [URL] [ARGUMENTS]`
- Parse dates with `python-dateutil`
- Sender email is in the `From: "Name &lt;email@...&gt;` header
- When removing a prefix (e.g. `/data/docs/`) from a path, retain the path after the prefix
- Call an LLM via a POST request to `https://llmfoundry.straive.com/openai/v1/chat/completions` with `Authorization: Bearer {os.getenv("LLMFOUNDRY_TOKEN")}` and this JSON body:
 {
 model: "gpt-4o-mini",
 messages: [
 { role: "system", content: "[INSERT SYSTEM PROMPT]" },
 { role: "user", content: [
 { type: "text", text: "[INSERT USER MESSAGE]" }, // for text
 { type: "image_url", image_url: { url: `data:[IMAGE MIME TYPE];base64,[IMAGE BASE64]`, detail: "low" } }, // for image. Get MIME type DYNAMICALLY from image
 ]}
 ],
 // response_format: "json_object", // forces JSON response
 }
 Response is in `response.choices?.[0]?.message?.content`. Error is in `response.error?.message`.
- Calculate embeddings with a POST request to `https://llmfoundry.straive.com/openai/v1/embeddings` with `Authorization: Bearer {os.getenv("LLMFOUNDRY_TOKEN")}` and this JSON body:
 {
 model: "text-embedding-3-small",
 input: [array of strings],
 }
 Embeddings are in response.data[*].embedding - an array of floats.
 Calculate the dot product of the embeddings (skipping the diagonal) to find the most similar pair of strings.
