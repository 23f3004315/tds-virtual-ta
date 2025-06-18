---
chunk_id: discourse_topic_165959_post_203_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/203
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 194
username: 24f2003130
post_number: 203
topic_id: 165959
---

## Post #203 by 24f2003130

**Direct Link**: [Post #203](https://discourse.onlinedegree.iitm.ac.in/t/165959/203)

The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.

In your output, there are only two unique issueDate values:

2025-02-08T04:00:00-05:00

2025-02-08T16:01:58-05:00

This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you need to modify your approach by using the actual forecast day for each day instead.
