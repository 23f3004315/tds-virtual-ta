---
chunk_id: discourse_topic_163247_post_136_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/136
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 288
username: Jivraj
post_number: 136
topic_id: 163247
---

## Post #136 by Jivraj

**Direct Link**: [Post #136](https://discourse.onlinedegree.iitm.ac.in/t/163247/136)

Hi Sakshi

Sakshi6479:
[Quote]: 
Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

drive.google.com

2025-02-04 03-50-48.mkv

Google Drive file.

For question 7

Sakshi6479:
[Quote]: 
`import openai
`

You won’t be able to send request through openai python module, here is one example how you would make a request

`headers = {
 'Content-Type': 'application/json',
 'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
 'model':'gpt-4o-mini',
 'messages':[
 {
 'role':'user',
 'content':'What is 2+2?'
 }
 ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)
`
You would need to use professor Anand’s proxy or some other api key through which request can be made.

Url’s for free api keys:

AI Proxy
OpenAI GPT-4o · GitHub Models
