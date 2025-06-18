---
chunk_id: discourse_topic_166576_post_47_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/47
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 278
username: carlton
post_number: 47
topic_id: 166576
---

## Post #47 by carlton

**Direct Link**: [Post #47](https://discourse.onlinedegree.iitm.ac.in/t/166576/47)

@lakshaygarg654

Your query construction is unnecessarily complicated and therefore will be difficult to debug.

Query construction is best done by thinking what you want at the end.

In this case its an ordered `post_id`

So thats where you begin:

`SELECT post_id
FROM (
...
)
ORDER BY post_id
`
Doing this, produces the actual result without giving the logic yet.

Then at each stage you add the next stage of complexity.

You will still need the `post_id` for the *outermost layer* so you have to continue extracting it from the *inner layers* of the nested query.

`...
...
FROM (
 SELECT post_id, ( ... ) as max_stars
 FROM social_media
 WHERE time_stamp &gt;= (whatever the parameter you have been given)
 AND max_stars &gt;= (whatever the parameter for min stars you have been given)
)
...
...
`
Then the final layer of the nest

`...
...
(

) as max_stars
...
...
`
You are not expecting me to solve the whole question right? (Hint: the inner most extraction involves JSON or “structure” extraction, which is a powerful capability)
