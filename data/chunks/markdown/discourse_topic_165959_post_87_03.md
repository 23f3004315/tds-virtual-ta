---
chunk_id: discourse_topic_165959_post_87_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165959/87
source_title: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 129
username: 24ds3000090
post_number: 87
topic_id: 165959
---

.

I have tried these steps:

`import pymupdf4llm
md_text = pymupdf4llm.to_markdown("/content/q-pdf-to-markdown.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())
`
Then i run this in bash

---

`prettier --write output.md
`
And what i got frankly telling was far from this, I did some manual touchups, and this what i have now. This is the best version i could come up with. Saw the preview, it does matches with the pdf.

#Can someone please advise me a better approach?
