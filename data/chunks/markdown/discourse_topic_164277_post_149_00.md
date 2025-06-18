---
chunk_id: discourse_topic_164277_post_149_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/149
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 218
username: TRIGON
post_number: 149
topic_id: 164277
---

## Post #149 by TRIGON

**Direct Link**: [Post #149](https://discourse.onlinedegree.iitm.ac.in/t/164277/149)

Dear Instructors (@carlton, @iamprasna):

Confirming, just to be needfully pedantic:

It will **solely** be the responsibility of the Project Evaluator (human or machine) to parse the correct `AIPROXY_TOKEN` generated against my IITM email ID (presumably, per some database which holds all such generated `AIPROXY_TOKEN`s of the students who have generated one); and the correct `$IMAGE_NAME` (to-be-submitted by myself in the Project Submission Google Form) in `podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000`, correct?

Asking this seemingly obvious question, as (apparently) the actual `AIPROXY_TOKEN` is not to be included anywhere in the code, or the repository, or the dockerfile.
