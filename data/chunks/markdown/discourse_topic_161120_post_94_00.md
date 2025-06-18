---
chunk_id: discourse_topic_161120_post_94_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/94
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 116
username: Jivraj
post_number: 94
topic_id: 161120
---

## Post #94 by Jivraj

**Direct Link**: [Post #94](https://discourse.onlinedegree.iitm.ac.in/t/161120/94)

hi @23f2003853

I think you are running your application server inside a virtual machine because of which it doesn’t have visibility to outside world(request coming from other domains). So you would need to identify ipaddress of your virtual machine and would need to use that in place of `127.0.0.1`. Take help from GPT to identify ipaddress of virtual machine.
