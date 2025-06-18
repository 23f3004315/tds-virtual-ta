---
chunk_id: course_project_1_008
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 238
---

 try and avoid that.)
- **Stick to GPT-4o-Mini**. This is the only generation model that AI Proxy currently supports. When this page says "LLM", it means GPT-4o-Mini.
- **Keep your prompts short and concise**. Each call to `/run` and `/read` must complete within 20 seconds.

---

## Evaluation

This [evaluation script](project-1/evaluate.py) evaluates the scripts.Here's how will evaluate a task, e.g. **Task A2**.

1. Call `POST http://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2`. Ensure that the respose is a HTTP 200.
 - Note: The task may be worded differently. It may use a different prettier version. But the broad task is the same.
2. Call `GET http://localhost:8000/read?path=/data/format.md` and get the revised file contents.
3. Verify that the response was formatted using `prettier@3.4.2`.

Here's how we will score the results.
