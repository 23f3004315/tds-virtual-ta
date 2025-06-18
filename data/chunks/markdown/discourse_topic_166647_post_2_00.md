---
chunk_id: discourse_topic_166647_post_2_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166647/2
source_title: I have doubt in Q10
content_type: discourse
tokens: 138
username: 22f3000092
post_number: 2
topic_id: 166647
---

## Post #2 by 22f3000092

**Direct Link**: [Post #2](https://discourse.onlinedegree.iitm.ac.in/t/166647/2)

Try using the pymupdf4llm Library

pip install pymupdf4llm

import pymupdf4llm

md_text = pymupdf4llm.to_markdown(“input.pdf”)

import pathlib

pathlib.Path(“output.md”).write_bytes(md_text.encode())

import pymupdf4llm

llama_reader = pymupdf4llm.LlamaMarkdownReader()

llama_docs = llama_reader.load_data(“input.pdf”)
