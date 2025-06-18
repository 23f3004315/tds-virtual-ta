---
chunk_id: discourse_topic_164277_post_76_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/76
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 159
username: 22f3001315
post_number: 76
topic_id: 164277
---

## Post #76 by 22f3001315

**Direct Link**: [Post #76](https://discourse.onlinedegree.iitm.ac.in/t/164277/76)

` expected = sum(1 for date in dates if parse(date).weekday() == 2)
 if result.strip() != str(expected):
 return mismatch("/data/dates-wednesdays.txt", expected, result)
 return True```

`
 /data/dates-wednesdays.txt

EXPECTED:

129

RESULT:

“129”

If it is expecting str then why throw error sir ? @carlton @Jivraj

or just tell me how to pass count as an int here

`with open(output_file, "w") as f:
 f.write(str(count)) 
`
