---
chunk_id: discourse_topic_166576_post_71_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/71
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 265
username: bhashwar_sengupta
post_number: 71
topic_id: 166576
---

## Post #71 by bhashwar_sengupta

**Direct Link**: [Post #71](https://discourse.onlinedegree.iitm.ac.in/t/166576/71)

For Q8, I wrote the following query,

`SELECT smo.post_id
FROM social_media as smo
WHERE smo.timestamp &gt;= '2024-11-15T06:02:28.656Z'
AND EXISTS (
 SELECT 1
 FROM LATERAL (
 SELECT UNNEST(json_extract(comments, '$[*]'))
 FROM social_media as sm
 WHERE sm.post_id = smo.post_id
 ) AS c(value)
 WHERE json_extract(c.value, '$.stars.useful')::DOUBLE = 4)
order by smo.post_id;
`
What it does is for each post_id, checks the timestamp and then checks the presence of a json object in comments that has 4 stars useful rating for this post_id. Finally returns all the post_id’s in ascending order.

But it’s giving me an `Array length mismatch` error. I’m stuck here. Any hints would be helpful. @Jivraj @carlton

P.S. I also noticed that the timestamp given in the question keeps changing with each page reload. But the output from the query stays the same.
