---
chunk_id: discourse_topic_171141_post_318_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/318
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 300
username: carlton
post_number: 318
topic_id: 171141
---

## Post #318 by carlton

**Direct Link**: [Post #318](https://discourse.onlinedegree.iitm.ac.in/t/171141/318)

@Arunvembu @22f2000008 @23f1000879 @22f3003201 @23f2000926 @22f3001702 @Santoshsharma @kartikay1 @Kasif

Check first by following the instructions show here:

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

Then post with your queries after testing as mentioned above.

Also check the evaluation logs first to see why it failed. Address that question.

Posting “it ran before submission” is insufficient evidence.
