---
chunk_id: discourse_topic_169029_post_77_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/77
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 123
username: Jivraj
post_number: 77
topic_id: 169029
---

 a url and if it get’s downloaded by clicking then it will come from requester’s machine.

23f2000573:
[Quote]: 
so, can I assume that the table will be given as a html element in the “question” attribute and the image in the “file” attribute?

---

For questions that have table they will either come as html code or as markdown. Keep a if else condition for identifying which case it is, if it’s a html then beautiful soup should be able to find table tag, if it’s markdown table then it can be identified with `|` characters.

Kind regards
