---
chunk_id: discourse_topic_161083_post_96_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/96
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 99
username: Jivraj
post_number: 96
topic_id: 161083
---

## Post #96 by Jivraj

**Direct Link**: [Post #96](https://discourse.onlinedegree.iitm.ac.in/t/161083/96)

Hi Arnav,

I tried your script on your dataset.

Problem might be you are not executing `grep . * | LC_ALL=C sort | sha256sum` in correct directory, you would need to execute it from `all_files` directory also there should not be any extra file other than that gets generated.
