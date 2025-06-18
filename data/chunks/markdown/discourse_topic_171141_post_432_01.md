---
chunk_id: discourse_topic_171141_post_432_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/432
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 418
username: 22f3000819
post_number: 432
topic_id: 171141
---



Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.

---

**[Discussion Image by 22f3000819]** This image shows a student's code error and related traceback in a discussion thread, likely asking for help. The error is an `OSError: cannot open resource`, specifically related to the PIL (Pillow) library and its inability to find or open a font file. The traceback indicates the error originates in the `ImageFont.truetype()` function when trying to load both "arial.ttf" and "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf". The error occurs within the PIL library's functions for handling TrueType fonts, specifically while creating the font object with `core.getfont()`. The double traceback suggests that the initial exception triggered a secondary error during exception handling. `OSError: cannot open resource`. The error occurs when trying to load fonts using `ImageFont.truetype()`, first with "arial.ttf" and subsequently with "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf". The traceback reveals the error originates from the PIL (Pillow) library's `ImageFont.py` file when the `core.getfont()` function fails to open the specified font resource, likely due to the font file not being found or accessible at the given path. The double traceback suggests the initial exception triggered a subsequent one during exception handling, and indicates potential configuration or path issues related to accessing font files within the environment. The student is likely facing difficulty in properly linking the font to the project." alt="image" data-base62-sha1="nuja8ivRzao9XSmkZlLA9RYFAsP" width="690" height="455" data-dominant-color="313131">image1298×857 29.4 KB
