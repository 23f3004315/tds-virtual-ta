---
chunk_id: discourse_topic_169029_post_422_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/422
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 268
username: 22f3000819
post_number: 422
topic_id: 169029
---

## Post #422 by 22f3000819

**Direct Link**: [Post #422](https://discourse.onlinedegree.iitm.ac.in/t/169029/422)

@Saransh_Saini

Sir, I saw from the logs on Cloud Run that my project was probably evaluated on 5th April at around 11:51 PM and all the requests made during that time resulted in 3 response status codes: 302, 307 and 405 by no fault of my app, but rather errors in the request itself. I mentioned the exactly correct URL of my app in the form but the evaluation logs show three different types of URL to which request was made. As I mentioned in the form, my url is of the format “https://…/api/” and allows only POST requests.

The app was supposed to allow POST requests and I allowed only POST requests, so GET requests even to correct url resulted in 405 response
When POST requests were actually made, two wrong urls were used for all the POST requests

a. http://…/api/ → resulted in 302 response

b. https://…/api → resulted in a 307

whereas the url I gave was of the format “https://…/api/”

The logs from Cloud Run
