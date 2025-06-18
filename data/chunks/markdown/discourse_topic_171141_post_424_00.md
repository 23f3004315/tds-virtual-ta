---
chunk_id: discourse_topic_171141_post_424_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/424
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 302
username: 23F300327
post_number: 424
topic_id: 171141
---

## Post #424 by 23F300327

**Direct Link**: [Post #424](https://discourse.onlinedegree.iitm.ac.in/t/171141/424)

`🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
 "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1 | 2 | 3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")

`
 RESULT:

Header

Start
Mid
End

1
2
3

Paragraph has extra spaces and trailing whitespace.

`print("23f3003027@ds.study.iitm.ac.in")

`
 A2 FAILED
