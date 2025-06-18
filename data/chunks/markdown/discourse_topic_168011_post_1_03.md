---
chunk_id: discourse_topic_168011_post_1_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/168011/1
source_title: Q3, GA5 not accepting right answer
content_type: discourse
tokens: 176
username: muskan2431
post_number: 1
topic_id: 168011
---

 parts = line.split(' ')
 log_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
 method, url, status = parts[5][1:], parts[6], int(parts[8])
 return log_time, method, url, status

---

with gzip.open(log_path, 'rt') as file:
 for entry in file:
 log_time, method, url, status = parse_log(entry)
 if method == 'GET' and url.startswith('/blog/') and 200 &lt;= status &lt; 300:
 if log_time.weekday() == 0 and start_time &lt;= log_time.time() &lt; end_time:
 log_data.append(entry)

print(f"Successful GET requests: {len(log_data)}")
`
ps: I shared code after the deadline hopefully no issues there!
