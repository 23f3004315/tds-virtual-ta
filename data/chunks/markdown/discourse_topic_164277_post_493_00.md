---
chunk_id: discourse_topic_164277_post_493_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/493
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 209
username: 22f3000819
post_number: 493
topic_id: 164277
---

## Post #493 by 22f3000819

**Direct Link**: [Post #493](https://discourse.onlinedegree.iitm.ac.in/t/164277/493)

@carlton @Jivraj @Saransh_Saini

When I run my docker image using

`podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`

Task A2 fails as the podman container is unable to find npx.

Running the same image using

`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`

works fine and Task A2 passes. I can’t understand why this is happening.

I also ran the image in both docker and podman in interactive mode as show in the below snippet from terminal.

When run using docker, `which node` gives `/usr/bin/node` as output but when run using podman, nothing.
