---
chunk_id: course_llamafile_001
source_url: https://tds.s-anand.net/#/llamafile
source_title: llamafile
content_type: course
tokens: 551
---

 prompt or terminal, run `Llama-3.2-1B-Instruct.Q6_K.llamafile`.
3. Optional: For GPU acceleration, use `Llama-3.2-1B-Instruct.Q6_K.llamafile --n-gpu-layers 35`. (Increase or decrease the number of layers based on your GPU VRAM.)

---

You might see a message like this:

```text
██╗ ██╗ █████╗ ███╗ ███╗ █████╗ ███████╗██╗██╗ ███████╗
██║ ██║ ██╔══██╗████╗ ████║██╔══██╗██╔════╝██║██║ ██╔════╝
██║ ██║ ███████║██╔████╔██║███████║█████╗ ██║██║ █████╗
██║ ██║ ██╔══██║██║╚██╔╝██║██╔══██║██╔══╝ ██║██║ ██╔══╝
███████╗███████╗██║ ██║██║ ╚═╝ ██║██║ ██║██║ ██║███████╗███████╗
╚══════╝╚══════╝╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚══════╝
software: llamafile 0.8.17
model: Llama-3.2-1B-Instruct-Q8_0.gguf
compute: 13th Gen Intel Core i9-13900HX (alderlake)
server: http://127.0.0.1:8080/

A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.
```

You can now chat with the model. Type `/exit` or press `Ctrl+C` to stop.

You can also visit `http://127.0.0.1:8080/` in your browser to chat with the model.

LlamaFile exposes an OpenAI compatible API. Here's how to use it in Python:

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
