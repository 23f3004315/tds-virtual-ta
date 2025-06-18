---
chunk_id: course_vision_models_003
source_url: https://tds.s-anand.net/#/vision-models
source_title: vision-models
content_type: course
tokens: 397
---

 a trendline. Finally, a ρ of 0 suggests no linear correlation, with points randomly distributed. Understanding correlation is crucial in vision models, particularly when analyzing feature dependencies or assessing the relationship between predicted and actual values."}`: The URL of the image.

You can send images in a [base64 encoded format](base64-image.md), too. For example:

---

```bash
# Download image and convert to base64 in one step
IMAGE_BASE64=$(curl -s "**[Course Image: ]** This image illustrates the concept of correlation coefficient (ρ) and its relationship to data points in scatter plots, a fundamental aspect when training vision models to identify relationships. It demonstrates how the value of ρ signifies the strength and direction of a linear relationship between two variables. When ρ = +1, it indicates a perfect positive correlation, where data points form a straight line with a positive slope. Conversely, ρ = -1 indicates a perfect negative correlation, with data points forming a straight line with a negative slope, while ρ = 0 suggests no linear correlation between the variables, displayed as scattered points with no clear trend. Understanding these correlations is crucial for interpreting the outputs and validating the performance of vision models that attempt to learn relationships from image data." | base64 -w 0)

# Send to OpenAI API
curl https://api.openai.com/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $OPENAI_API_KEY" \
 -d @- << EOF
{
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "user",
 "content": [
 {"type": "text", "text": "What is in this image?"},
 {
 "type": "image_url",
 "image_url": { "url": "data:image/png;base64,$IMAGE_BASE64" }
 }
 ]
 }
 ]
}
EOF
```
