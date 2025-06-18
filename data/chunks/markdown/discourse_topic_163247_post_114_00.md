---
chunk_id: discourse_topic_163247_post_114_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/114
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 90
username: Jayeshbansal
post_number: 114
topic_id: 163247
---

## Post #114 by Jayeshbansal

**Direct Link**: [Post #114](https://discourse.onlinedegree.iitm.ac.in/t/163247/114)

import numpy as np

def most_similar(embeddings):

words = list(embeddings.keys())

dot_product_df =

for i in words:

for j in words:

dot_product_df.append(np.dot(embeddings[i], embeddings[j]))

return max(dot_product_df)
