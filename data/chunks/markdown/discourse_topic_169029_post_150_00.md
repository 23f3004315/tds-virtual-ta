---
chunk_id: discourse_topic_169029_post_150_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/150
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 220
username: kushabarodekar
post_number: 150
topic_id: 169029
---

## Post #150 by kushabarodekar

**Direct Link**: [Post #150](https://discourse.onlinedegree.iitm.ac.in/t/169029/150)

Hi @Saransh_Saini @carlton ,

In the sample curl command

i.e.

`curl -X POST "https://your-app.vercel.app/api/" \
 -H "Content-Type: multipart/form-data" \
 -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?" \
 -F "file=@abcd.zip"
`
It is given that only one file arguement is passed , can there be a usecase where multiple files are sent , for example GA-5 10th question Image reconstruction where there could be one file be the image another could be separate file with mapping, Although mapping can be given with question as well,

But still can you please confirm if there will be only one file or there can be multiple files send to API?
