---
chunk_id: discourse_topic_171141_post_344_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/344
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 257
username: afsalshah
post_number: 344
topic_id: 171141
---

## Post #344 by afsalshah

**Direct Link**: [Post #344](https://discourse.onlinedegree.iitm.ac.in/t/171141/344)

@carlton @Jivraj

Dear Sir,

I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.

I debugged that I had a small issue in the dockerfile that was submitted and it is

CMD [“/root/.local/bin/uv”, “run”, “app.py”] has an **invisible Unicode non-breaking space** (`U+00A0`) between `"run", "app.py"` instead of a regular space. This causes the shell to misread the command.

I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE. Expecting a positive response from your end.
