---
chunk_id: discourse_topic_166576_post_46_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/46
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 226
username: lakshaygarg654
post_number: 46
topic_id: 166576
---

## Post #46 by lakshaygarg654

**Direct Link**: [Post #46](https://discourse.onlinedegree.iitm.ac.in/t/166576/46)

@Saransh_Saini

Q5 fixed, thanks for fixing the issue.

Now we are struggling with Q8.

MY q8 is : Write a DuckDB SQL query to find all posts IDs after 2025-01-09T12:36:14.085Z with at least 1 comment with 4 useful stars, sorted. The result should be a table with a single column called `post_id` , and the relevant post IDs should be sorted in ascending order.

when i use below query, i get some some result, a table of post_id but error : **Error**: At root: Array length mismatch

**Reason**: below query checking only 1st comment (`$[0]` refers to the first comment in the array) we have to check all comments not 1st.

But when i change the query to check any one comment its giving different types of error.
