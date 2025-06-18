---
chunk_id: course_llm_sentiment_analysis_001
source_url: https://tds.s-anand.net/#/llm-sentiment-analysis
source_title: llm-sentiment-analysis
content_type: course
tokens: 315
---

 scripts to securely access the OpenAI API for sentiment analysis tasks. Once the key is in place, remember to source your `.zshrc` file with `source ~/.zshrc` or restart your terminal to apply the changes, enabling you to then call the API in your sentiment analysis code.)](https://youtu.be/Xz4ORA0cOwQ)

---

Here's a minimal example using `curl` to generate text:

```bash
curl https://api.openai.com/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $OPENAI_API_KEY" \
 -d '{
 "model": "gpt-4o-mini",
 "messages": [{ "role": "user", "content": "Write a haiku about programming." }]
 }'
```

Let's break down the request:

- `curl https://api.openai.com/v1/chat/completions`: The API endpoint for text generation.
- `-H "Content-Type: application/json"`: The content type of the request.
- `-H "Authorization: Bearer $OPENAI_API_KEY"`: The API key for authentication.
- `-d`: The request body.
 - `"model": "gpt-4o-mini"`: The model to use for text generation.
 - `"messages":`: The messages to send to the model.
 - `"role": "user"`: The role of the message.
 - `"content": "Write a haiku about programming."`: The content of the message.
