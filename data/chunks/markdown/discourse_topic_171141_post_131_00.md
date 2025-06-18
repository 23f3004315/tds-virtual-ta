---
chunk_id: discourse_topic_171141_post_131_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/131
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 303
username: 22f3002723
post_number: 131
topic_id: 171141
---

## Post #131 by 22f3002723

**Direct Link**: [Post #131](https://discourse.onlinedegree.iitm.ac.in/t/171141/131)

@Jivraj @carlton

Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build

`ARG http_proxy=http://www-proxy-adcq7.us.&lt;xxx&gt;.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.&lt;xxx&gt;.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}
`
This was required as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..

So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container started up without issues..

Checkin url: Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub

Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well.. didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help
