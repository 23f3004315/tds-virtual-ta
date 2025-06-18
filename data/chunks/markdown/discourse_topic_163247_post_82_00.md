---
chunk_id: discourse_topic_163247_post_82_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/82
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 196
username: 23f1002382
post_number: 82
topic_id: 163247
---

## Post #82 by 23f1002382

**Direct Link**: [Post #82](https://discourse.onlinedegree.iitm.ac.in/t/163247/82)

**Q4**

s3 string was given by

`image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
 binary_data = f.read()
 image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"
`

s4 string given by :

used this link to generate image url

Then checked them both, they were the same

`for x,y in zip(s3,s4):
 if (x != y):
 print(x,y)
`
i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?

I know i’m missing something, but why?
