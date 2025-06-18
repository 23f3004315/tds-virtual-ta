---
chunk_id: discourse_topic_164277_post_544_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/544
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 251
username: bhashwar_sengupta
post_number: 544
topic_id: 164277
---

## Post #544 by bhashwar_sengupta

**Direct Link**: [Post #544](https://discourse.onlinedegree.iitm.ac.in/t/164277/544)

I had a question on evaluation by the course team. To test that my application would run everywhere, I first deleted all images from my local machine using `podman rmi -a` and then ran `podman run --rm -p 8000:8000 -e AIPROXY_TOKEN=$AIPROXY_TOKEN $IMAGE_NAME` with the appropriate variables set. This is as per the instructions provided here. But this gave me the following error:

`Error: short-name "freshbash/dataworks-agent" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf
`
The above is the format in which we have to provide the image name in the Google form. So, I was confused whether this would succeed during actual evaluation.

The only way its working right now is when I specify the image name to be `docker.io/freshbash/dataworks-agent`

I’m not yet very good with how containers work so some insights would be very helpful. Thanks!
