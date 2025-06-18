---
chunk_id: discourse_topic_164277_post_39_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/39
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 392
username: JoelJeffrey
post_number: 39
topic_id: 164277
---



**Direct Link**: [Post #39](https://discourse.onlinedegree.iitm.ac.in/t/164277/39)

Ok. So just to confirm, since there are files with the same name, the json file should map the filepath and not the filename to the title right?

---

**[Discussion Image by JoelJeffrey]** This image shows the specification for task A6 from "Project 1 - LLM-based Automation Agent" in a TDS course. The task requires students to find all Markdown files in the `/data/docs/` directory. For each file, the student must extract the first header line (identified by lines starting with `#`). The solution involves creating an index file named `/data/docs/index.json` which is a JSON formatted file that maps the filename (without the file path) to the file's extracted title, as demonstrated with the example: `{"README.md": "Home", "large-language-models.md": "Large Language Models", ...}`. This example helps students understand the desired JSON output format.tudents must extract the first header line denoted by a line starting with '#'. The extracted filename and header text should be stored in a JSON file called `index.json`, also located in `/data/docs/`, where the filename (without path) maps to its title. An example is given showing the desired structure of the JSON file, like `{"README.md": "Home", "large-language-models.md": "Large Language Models", ...}`." alt="Screenshot from 2025-01-31 12-25-29" data-base62-sha1="ueKbRWWjd5grI2e1vqOReD58S1t" width="690" height="102" data-dominant-color="EAEAEA">Screenshot from 2025-01-31 12-25-29790×117 19.9 KB
