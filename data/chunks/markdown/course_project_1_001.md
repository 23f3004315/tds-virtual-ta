---
chunk_id: course_project_1_001
source_url: https://tds.s-anand.net/#/project-1
source_title: project-1
content_type: course
tokens: 271
---

 Large Language Model (LLM) as an intermediate transformer. In this role, the LLM will perform small, reasonably deterministic tasks.

Your assignment is to build an automation agent that accepts plain‑English tasks, carries out the required (multi‑step) process leveraging an LLM where required. The finished processing artifacts must be exactly verifiable against pre‑computed expected results.

---

## Create an API

Write an application that exposes an API with the following endpoints:

- **POST `/run?task=`**
 Executes a plain‑English task. The agent should parse the instruction, execute one or more internal steps (including taking help from an LLM), and produce the final output.
 - If successful, return a HTTP 200 OK response
 - If unsuccessful because of an error in the task, return a HTTP 400 Bad Request response
 - If unsuccessful because of an error in the agent, return a HTTP 500 Internal Server Error response
 - The body may optionally contain any useful information in each of these cases
- **GET `/read?path=`**
 Returns the content of the specified file. This is critical for verification of the exact output.
 - If successful, return a HTTP 200 OK response with the file content as plain text
 - If the file does not exist, return a HTTP 404 Not Found response and an empty body
