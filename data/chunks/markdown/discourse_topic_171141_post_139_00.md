---
chunk_id: discourse_topic_171141_post_139_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/139
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 172
username: Mystic_9803
post_number: 139
topic_id: 171141
---

## Post #139 by Mystic_9803

**Direct Link**: [Post #139](https://discourse.onlinedegree.iitm.ac.in/t/171141/139)

Hi @carlton @Jivraj

I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe_open function that will throw a HTTP_403_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?

Thanks for considering, any help would be appreciated. Worked very hard for this
