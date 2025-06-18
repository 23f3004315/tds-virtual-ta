---
chunk_id: discourse_topic_171141_post_149_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/149
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 173
username: carlton
post_number: 149
topic_id: 171141
---

## Post #149 by carlton

**Direct Link**: [Post #149](https://discourse.onlinedegree.iitm.ac.in/t/171141/149)

The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.

But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.

Kind regards
