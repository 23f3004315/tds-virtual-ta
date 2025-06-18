---
chunk_id: discourse_topic_169029_post_210_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/210
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 234
username: 22f3000819
post_number: 210
topic_id: 169029
---

## Post #210 by 22f3000819

**Direct Link**: [Post #210](https://discourse.onlinedegree.iitm.ac.in/t/169029/210)

@Saransh_Saini @Jivraj @carlton

Sir, I have an issue in GA5 Q3

What is the number of successful GET requests for pages under **/telugu/** from **11:00** until before **20:00** on Mondays?

For this, I have used two python scripts to get the answer, one written completely by me and another from someone else’s solution; both give the same answer - **2698**

However, the portal says it’s incorrect. No modifications resulting in different answer are being accepted either and the modifications themselves seem to break the bounds of the question.

Please check the scripts and tell me where I am going wrong.

My script:

`import subprocess
from datetime import datetime

def isDay(dtobj, day):
 return dtobj.weekday() == day

def isTime(dtobj, l, u):
 return l &lt;= dtobj.hour &lt; u
