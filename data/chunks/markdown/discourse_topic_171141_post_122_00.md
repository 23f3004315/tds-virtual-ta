---
chunk_id: discourse_topic_171141_post_122_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/122
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 176
username: carlton
post_number: 122
topic_id: 171141
---

## Post #122 by carlton

**Direct Link**: [Post #122](https://discourse.onlinedegree.iitm.ac.in/t/171141/122)

When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.

In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.

But we can detect changes made to the docker repo through our image id. I hope that is clear.

We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.

Kind regards
