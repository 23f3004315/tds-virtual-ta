---
chunk_id: discourse_topic_168011_post_1_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168011/1
source_title: Q3, GA5 not accepting right answer
content_type: discourse
tokens: 282
username: muskan2431
post_number: 1
topic_id: 168011
---

 data-base62-sha1="34qcnwBcLwmxZulqWMVZUZGT9gX" width="690" height="352" data-dominant-color="F5F5F5">image1337×683 31.9 KB

---

It seems that the question in *Graded Assignment 5 for TDS* is producing incorrect results despite the same logic working correctly for other variations of the problem. Please check into this question once as I have cross checked with many of the students and chatgpt and all of us faced this issue in this question. Thanks!

@carlton @s.anand

code to take reference from:

`import gzip
import pandas as pd
from datetime import datetime

log_path = 's-anand.net-May-2024.gz'
start_time = datetime.strptime('01:00:00', '%H:%M:%S').time()
end_time = datetime.strptime('15:00:00', '%H:%M:%S').time()
log_data = []

def parse_log(line):
 parts = line.split(' ')
 log_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
 method, url, status = parts[5][1:], parts[6], int(parts[8])
 return log_time, method, url, status
