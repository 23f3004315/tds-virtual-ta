---
chunk_id: discourse_topic_169029_post_614_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/614
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 263
username: 23f3001764
post_number: 614
topic_id: 169029
---

## Post #614 by 23f3001764

**Direct Link**: [Post #614](https://discourse.onlinedegree.iitm.ac.in/t/169029/614)

***Request to Use Public DNS for Course Tool API Deployment or Use Alternate Endpoint**

Dear @Jivraj @Saransh_Saini @carlton

I hope you’re doing well!

I’m currently running my server and trying to access the API hosted at:

`https://sss-production-7a97.up.railway.app/api/
`
However, I’m encountering the following error:

`curl: (6) Could not resolve host: sss-production-7a97.up.railway.app
`
After some investigation, I found that the issue is related to DNS resolution. The API becomes accessible when using **public DNS services** like **Google (8.8.8.8)** or **Cloudflare (1.1.1.1)**. This suggests that the current deployment environment may be using a restricted or unreliable DNS resolver, which causes access issues on some networks (e.g., Jio).

Suggested Fix:
To ensure reliable access for all students, could you please consider updating the deployment or testing environment to use a **public DNS** provider?

Recommended options:
