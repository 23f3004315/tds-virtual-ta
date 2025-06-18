---
chunk_id: discourse_topic_166576_post_46_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/46
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 197
username: lakshaygarg654
post_number: 46
topic_id: 166576
---

: Array length mismatch

**Reason**: below query checking only 1st comment (`$[0]` refers to the first comment in the array) we have to check all comments not 1st.

But when i change the query to check any one comment its giving different types of error.

---

`WITH filtered_posts AS (
 SELECT post_id
 FROM social_media
 WHERE timestamp &gt;= '2025-01-09T09:48:01.303Z'
 AND EXISTS (
 SELECT 1
 FROM social_media AS sm
 WHERE json_extract_path_text(sm.comments, '$[0].stars.useful') IS NOT NULL
 AND CAST(json_extract_path_text(sm.comments, '$[0].stars.useful') AS INTEGER) &gt; 4
 )
)
SELECT post_id
FROM filtered_posts
ORDER BY post_id ASC;
`
Kindly check if any issue with Q8.

May be my query is wrong or may be not.

Thankyou
