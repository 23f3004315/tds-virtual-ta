---
chunk_id: discourse_topic_171141_post_330_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/330
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 358
username: 23f2003751
post_number: 330
topic_id: 171141
---

 with an expected or ideal project setup within the discussion." alt="image" data-base62-sha1="bCYFeHxVzBnl2fAh3CxgzgJ8Xdw" width="205" height="88">image274×118 2.87 KB

---

All the files are in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.

carlton:
[Quote]: 
Keep datagen.py and evaluate.py in same folder

when i do this( ) i get this error

carlton:
[Quote]: 
`docker build -t &lt;your image name&gt;`

`PS D:\TDS_Project_1\tds-project-1&gt; docker build -t "tushar2k5/tds-project-1" 
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage: docker buildx build [OPTIONS] PATH | URL | -

Start a build
`
Instead,in order to run the docker image successfully we have to do either of the two things(taken help from chatgpt ):

1)

`Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1
`
**OR**

2)

`Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .
`
*Both the things work for me*()
