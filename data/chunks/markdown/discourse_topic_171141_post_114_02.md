---
chunk_id: discourse_topic_171141_post_114_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/114
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 184
username: 22f3000819
post_number: 114
topic_id: 171141
---

="image" data-base62-sha1="vVy1Zl2FILIE7YmcgLMAd1engpp" width="690" height="374" data-dominant-color="F7F7F7">image1485×807 37.4 KB

---

The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?
