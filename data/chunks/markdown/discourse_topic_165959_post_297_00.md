---
chunk_id: discourse_topic_165959_post_297_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/297
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 111
username: rohitgarg
post_number: 297
topic_id: 165959
---

## Post #297 by rohitgarg

**Direct Link**: [Post #297](https://discourse.onlinedegree.iitm.ac.in/t/165959/297)

@Abhay222 @22f3002184

if you look closely the expected value is `2024- ` and actual that you are supplying is `2024`.

Difference ? your value does have a `-` and a space at the end.

reason ? you might be scraping it ? `trim()` or maybe using `innerText` to get tag’s text ?
