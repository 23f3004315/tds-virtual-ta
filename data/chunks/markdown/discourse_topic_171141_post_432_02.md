---
chunk_id: discourse_topic_171141_post_432_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/432
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 260
username: 22f3000819
post_number: 432
topic_id: 171141
---

 project." alt="image" data-base62-sha1="nuja8ivRzao9XSmkZlLA9RYFAsP" width="690" height="455" data-dominant-color="313131">image1298×857 29.4 KB

---

I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.

Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…

But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.

Edit 2:

Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.
