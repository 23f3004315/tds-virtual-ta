---
chunk_id: discourse_topic_171141_post_37_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/37
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 178
username: Pritul_raut
post_number: 37
topic_id: 171141
---

## Post #37 by Pritul_raut

**Direct Link**: [Post #37](https://discourse.onlinedegree.iitm.ac.in/t/171141/37)

@Jivraj , @carlton

It was a good project, and I have obtained the log files. Upon reviewing the log files, I realized that they are unable to read the files. I checked my project on GitHub and discovered that I forgot to uncomment the line that defines the path using the `os` library. As a result, all file evaluations returned errors such as “can’t read the file.”

I understand that this oversight was my mistake. However, is there any way to reevaluate the code by simply uncommenting that line? I believe the rest of the code is properly written, but due to this single comment, all the files remained unchecked or resulted in errors.
