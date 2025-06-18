---
chunk_id: discourse_topic_169029_post_341_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/341
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 289
username: Algsoch
post_number: 341
topic_id: 169029
---

## Post #341 by Algsoch

**Direct Link**: [Post #341](https://discourse.onlinedegree.iitm.ac.in/t/169029/341)

:

From Problem to Platform: Building “Vicky” – A Smart Data Science Assistant for TDS @ IIT Madras
 **Project Demo Website**: https://app.algsoch.tech

During our college course *Tool for Data Science (TDS)* at **IIT Madras**, we were tasked with a challenging but exciting project: **to build a platform that can take in natural language questions and execute corresponding solutions through an API**.

The Mission:
Create a tool that behaves like a **chatbot**, accepts **user queries (text or file-based)** via **web or API**, processes them intelligently, **executes the appropriate code**, and returns accurate results—like a real data science assistant.

The Journey: From Fails to Final
At first, the natural choice was to try **LLM agents**—they sounded magical. But in real-world usage, they were slow, unreliable, and lacked precision. Most failed to parse or execute even moderately dynamic queries.

Then I thought—what if I manually mapped questions and answers using a **static JSON structure**? That quickly broke when users passed **different parameters, different files**, or queried in **non-standard formats** like “code -s” or “code -v”.
