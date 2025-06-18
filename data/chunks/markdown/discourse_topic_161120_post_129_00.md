---
chunk_id: discourse_topic_161120_post_129_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/129
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 113
username: 23ds1000022
post_number: 129
topic_id: 161120
---

## Post #129 by 23ds1000022

**Direct Link**: [Post #129](https://discourse.onlinedegree.iitm.ac.in/t/161120/129)

Hi sakshi in vercel problem i also had similar error. remove this code if **name** == ‘**main**’:

24 # app.run(debug=True) frm your flask app then run it. it worked for me i found this with the help of chatgpt. vercel has some built in features to run so this is not required it seems.
