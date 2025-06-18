---
chunk_id: discourse_topic_171141_post_326_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/326
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 227
username: carlton
post_number: 326
topic_id: 171141
---

## Post #326 by carlton

**Direct Link**: [Post #326](https://discourse.onlinedegree.iitm.ac.in/t/171141/326)

You have to replicate this test environment for testing.

Tds-official-Project1-discrepencies Tools in Data Science
 
 [Quote]: 
 To replicate the test environment: 
git clone &lt;your repo url&gt; 
cd &lt;your repo directory&gt; 
docker build -t &lt;your image name&gt; 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt; 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was tested. 
You have to provide a token from your environment for testing. 
The…

Please replicate this first. We also run it on a linux server.

Kind regards
