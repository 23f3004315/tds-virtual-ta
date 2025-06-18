---
chunk_id: discourse_topic_169029_post_28_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/28
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 314
username: 23f1001231
post_number: 28
topic_id: 169029
---

 we cannot run our systems 24*7 during evaluation.

I can see only one option left that is renting a VPS from server providers like digitalocean, gcp, aws etc, which will provide us sudo access and 100% uptime.

Also, some ques requires external toolings like

---

In GA1 ques 5, it is written to explicitly use Excel and this will only work in Office 365.
In GA1 ques 6, we have to use Devtools to show/find the hidden element in the question. Now, the question parameter in the POST request will be plain text, so how the element can hide there?
GA 2 ques 4 and GA 2 ques 5 uses Google Colab specific python libraries like google.colab which can’t be installed locally.

How to solve these above questions that require explicit usage of external tools.

Also, handling POST request for some questions are not clear like

In GA 2 ques 2, we have to compress the image and upload the image as answer. So, now how to response such answer in json object. Should we encode the resultant compressed image as base64 string or Image URL or Data URI.
Some ques have images in them. For those images in GAs, I right clicked and used “Save as” to save the images and then done the required computations. So, now when this question will be sent as POST request, will the image be included as the base64 encoded string in the question parameter of the POST request itself or as an optional file attachment?
