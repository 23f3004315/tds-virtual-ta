---
chunk_id: discourse_topic_167471_post_9_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167471/9
source_title: Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
content_type: discourse
tokens: 186
username: carlton
post_number: 9
topic_id: 167471
---

## Post #9 by carlton

**Direct Link**: [Post #9](https://discourse.onlinedegree.iitm.ac.in/t/167471/9)

So the reason for the failure is:

You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)

Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.

Then once you realised your mistake, on **Feb 17th at 9:11 pm IST** i.e *yesteday*, you changed your repo to put the files in the correct locations.

Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]
