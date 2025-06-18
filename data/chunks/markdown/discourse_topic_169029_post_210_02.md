---
chunk_id: discourse_topic_169029_post_210_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/210
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 351
username: 22f3000819
post_number: 210
topic_id: 169029
---

 the script.

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

---

# Function to parse Apache log entries
def parse_log_line(line):
 log_pattern = (r'^(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (.*?) (\S+)" (\d+) (\S+) "(.*?)" "(.*?)" (\S+) (\S+)$')
 match = re.match(log_pattern, line)
 if match:
 return {
 "ip": match.group(1),
 "time": match.group(4),
 "method": match.group(5),
 "url": match.group(6),
 "protocol": match.group(7),
 "status": int(match.group(8)),
 "size": match.group(9),
 "referer": match.group(10),
 "user_agent": match.group(11),
 "vhost": match.group(12),
 "server": match.group(13)
 }
 return None

# Upload file
uploaded = files.upload()
file_path = list(uploaded.keys())[0] # Get uploaded file name

# Load and parse the log file
def load_logs(file_path):
 if not os.path.exists(file_path):
 print(f"Error: File '{file_path}' not found.")
 return pd.DataFrame()

parsed_logs = []
 with gzip.open(file_path, 'rt', encoding='utf-8') as f:
 for line in f:
 parsed_entry = parse_log_line(line)
 if parsed_entry:
 parsed_logs.append(parsed_entry)
 return pd.DataFrame(parsed_logs)
