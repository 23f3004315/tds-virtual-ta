---
chunk_id: discourse_topic_166576_post_100_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/100
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 110
username: Jivraj
post_number: 100
topic_id: 166576
---

## Post #100 by Jivraj

**Direct Link**: [Post #100](https://discourse.onlinedegree.iitm.ac.in/t/166576/100)

`SELECT DISTINCT post_id 
FROM (
 SELECT timestamp, post_id, UNNEST (comments-&gt;'$[*].stars.useful') AS useful
 FROM social_media
) AS temp
WHERE useful &gt;= 2.0 
 AND timestamp &gt; '2024-12-08T05:30:31.073Z'
`
