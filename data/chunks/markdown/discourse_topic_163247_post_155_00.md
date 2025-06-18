---
chunk_id: discourse_topic_163247_post_155_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/155
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 165
username: Tanmay1
post_number: 155
topic_id: 163247
---

## Post #155 by Tanmay1

**Direct Link**: [Post #155](https://discourse.onlinedegree.iitm.ac.in/t/163247/155)

Question 4:

I am trying this :

`{
 "model": "gpt-4o-mini",
 "messages": [
 {
 "role": "user",
 "content": [
 {"type": "text", "text": "Extract text from this image."},
 {
 "type": "image_url",
 "image_url": { "url": "data:image/png;base64,iVBORw0KGgoAAAANS.......=" }
 }
 ]
 }
 ]
}
`
I am getting this error :

Error: The image_url.url must be the base64 data URL of the image

I verified that my Base64 encoding for the image is correct ..
