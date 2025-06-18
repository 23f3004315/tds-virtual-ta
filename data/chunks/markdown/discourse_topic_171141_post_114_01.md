---
chunk_id: discourse_topic_171141_post_114_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/114
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 419
username: 22f3000819
post_number: 114
topic_id: 171141
---

**: [Post #114](https://discourse.onlinedegree.iitm.ac.in/t/171141/114)

@carlton

My docker logs shows that `OSError: Cannot find resource` error occurred when the data generation script tried to access font files in generation for a8.

---

**[Discussion Image by 22f3000819]** This image shows a traceback from a student's code, indicating an `OSError: cannot open resource`. The error occurs when the code attempts to load a font using `ImageFont.truetype` from the PIL library, first with "arial.ttf" and then with "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf". The traceback indicates the error originates within the PIL library's `ImageFont.py` file during the initialization of the font object. This suggests the script cannot find or access the specified font files, likely due to an incorrect path or missing font files in the environment. The image represents a student question regarding this error as part of a peer discussion on discrepancies. `OSError: cannot open resource` when the code attempts to load a font using `ImageFont.truetype` from the PIL (Pillow) library. First, it attempts to load "arial.ttf", which fails, then it tries "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", which also fails with the same error. The error originates within the PIL library's `ImageFont.py` during the font initialization process, suggesting the font file is either missing or inaccessible at the specified paths. The INFO line at the bottom shows the install command, indicating that uv was used for package management. The student is likely encountering issues because the font files are not correctly installed or accessible within the container environment." alt="image" data-base62-sha1="vVy1Zl2FILIE7YmcgLMAd1engpp" width="690" height="374" data-dominant-color="F7F7F7">image1485×807 37.4 KB
