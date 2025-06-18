---
chunk_id: course_vision_models_001
source_url: https://tds.s-anand.net/#/vision-models
source_title: vision-models
content_type: course
tokens: 526
---

**: Convert extracted image data to various formats like Markdown tables or JSON arrays.
- **Handling Model Hallucinations**: Address inaccuracies in extraction results, understanding how different prompts can affect output quality.
- **Cost Management for Vision Models**: Adjust detail settings (e.g., "detail: low") to balance cost and output precision.

Here are the links used in the video:

---

- [Jupyter Notebook](https://colab.research.google.com/drive/1bK0b1XMrZWImtw01T1w9NGraDkiVi8mS)
- [OpenAI Chat API Reference](https://platform.openai.com/docs/api-reference/chat/create)
- [OpenAI Vision Guide](https://platform.openai.com/docs/guides/vision)
- [Sample images used](https://drive.google.com/drive/folders/14MFc7XmGIUDU4-vbmF9305c1SSQrM-gR)

Here is an example of how to analyze an image using the OpenAI API.

```bash
curl https://api.openai.com/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $OPENAI_API_KEY" \
 -d '{
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "user",
 "content": [
 {"type": "text", "text": "What is in this image?"},
 {
 "type": "image_url",
 "detail": "low",
 "image_url": {"url": "**[Course Image: ]** This image illustrates the concept of correlation coefficient (ρ) in the context of vision models, showing the strength and direction of a linear relationship between two variables. The image presents five scatter plots, each representing a different correlation coefficient value: ρ = -1 (perfect negative correlation), -1 < ρ < 0 (negative correlation), 0 < ρ < +1 (positive correlation), ρ = +1 (perfect positive correlation), and ρ = 0 (no correlation). Understanding correlation helps in vision models to identify relationships between image features and target variables. A common mistake is assuming correlation implies causation; this image helps clarify the distinction by visually representing different degrees of association without implying a cause-and-effect relationship. By understanding how correlation is measured and interpreted, students can better analyze the performance and behavior of their vision models, particularly when dealing with feature selection or understanding model biases."}
 }
 ]
 }
 ]
 }'
```

Let's break down the request:
