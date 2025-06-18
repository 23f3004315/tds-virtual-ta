---
chunk_id: discourse_topic_169029_post_614_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/614
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 256
username: 23f3001764
post_number: 614
topic_id: 169029
---

 deployment environment may be using a restricted or unreliable DNS resolver, which causes access issues on some networks (e.g., Jio).

Suggested Fix:
To ensure reliable access for all students, could you please consider updating the deployment or testing environment to use a **public DNS** provider?

Recommended options:

---

**Google DNS**: `8.8.8.8`, `8.8.4.4`
**Cloudflare DNS**: `1.1.1.1`, `1.0.0.1`

This can typically be configured via Docker settings or the environment’s networking configuration.

Alternate Option:
If the DNS change isn’t possible at the moment, I kindly request that you evaluate my project using the **previously deployed endpoint** instead:

`https://tds-project-2-pnlm.onrender.com/api/
`
Please note that this endpoint may take **50 to 60 seconds** to respond, as it’s hosted on a platform with a cold start delay — but it is fully functional and provides the correct outputs.

Both endpoints are currently active and return identical results.

Thank you so much for your time and support — I truly appreciate the effort you’re putting into helping us succeed in this course!

Best regards,

**Sahil Raj**
