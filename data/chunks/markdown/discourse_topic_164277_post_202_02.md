---
chunk_id: discourse_topic_164277_post_202_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/202
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 174
username: 21f2000709
post_number: 202
topic_id: 164277
---

Screenshot 2025-02-13 at 1.31.01 PM" data-base62-sha1="23Nzhqv7fQsw7MQIWGUG4ZEkERS" width="690" height="75" data-dominant-color="353F44">

---

The command:

`podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000`

gives the error:

`crun: executable file `-e` not found in $PATH: No such file or directory: OCI runtime attempted to invoke a command that was not found`

However the correct command seems to be:

`podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 $IMAGE_NAME`

This works totally fine.
