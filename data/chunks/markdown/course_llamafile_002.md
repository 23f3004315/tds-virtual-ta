---
chunk_id: course_llamafile_002
source_url: https://tds.s-anand.net/#/llamafile
source_title: llamafile
content_type: course
tokens: 130
---

 Python:

```python
import requests

response = requests.post(
 "http://localhost:8080/v1/chat/completions",
 headers={"Content-Type": "application/json"},
 json={"messages": [{"role": "user", "content": "Write a haiku about coding"}]}
)
print(response.json()["choices"][0]["message"]["content"])
```

Tools:

---

- [OpenAI API compatibility](https://platform.openai.com/docs/api-reference/chat): Use existing OpenAI code
- [Creating your own llamafiles](https://github.com/Mozilla-Ocho/llamafile#creating-llamafiles): Control output format
