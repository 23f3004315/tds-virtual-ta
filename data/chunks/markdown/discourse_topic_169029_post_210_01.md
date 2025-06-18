---
chunk_id: discourse_topic_169029_post_210_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/210
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 346
username: 22f3000819
post_number: 210
topic_id: 169029
---

 tell me where I am going wrong.

My script:

`import subprocess
from datetime import datetime

def isDay(dtobj, day):
 return dtobj.weekday() == day

def isTime(dtobj, l, u):
 return l &lt;= dtobj.hour &lt; u

---

step1 = subprocess.run("cat data | grep -i 'GET /telugu/'", capture_output=True, shell=True, text=True)
subprocess.run("rm -f forstep2.txt", shell=True)
with open('forstep2.txt', 'a') as f:
 for line in step1.stdout.splitlines():
 try:
 status = int(line.split()[8])
 except Exception as e:
 status = 400
 if 200 &lt;= status &lt; 300:
 f.write(line + '\n')
step2 = subprocess.run("cat forstep2.txt | cut -d ' ' -f4", capture_output=True, shell=True, text=True)
count = 0
for line in step2.stdout.splitlines():
 log_datetime = datetime.strptime(line.strip('['), "%d/%b/%Y:%H:%M:%S")
 if(isDay(log_datetime, 0) and isTime(log_datetime, 11, 20)):
 count += 1

count
`
I had extracted and uploaded the `data` after extraction using gzip into colab and then executed the script.

The other script:

`import pandas as pd
import gzip
import re
import os
from datetime import datetime
import hashlib
from google.colab import files

# Function to compute SHA-256 hash
def compute_hash(text):
 return hashlib.sha256(text.encode()).hexdigest()
