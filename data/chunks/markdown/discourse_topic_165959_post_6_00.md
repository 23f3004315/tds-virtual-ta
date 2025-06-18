---
chunk_id: discourse_topic_165959_post_6_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/6
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 150
username: s.anand
post_number: 6
topic_id: 165959
---

## Post #6 by s.anand

**Direct Link**: [Post #6](https://discourse.onlinedegree.iitm.ac.in/t/165959/6)

@22f3001315 @21f3002277 @24ds2000024 – please try again after reloading the page. The new error message will be clearer, like this:

`Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4
`
FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.
