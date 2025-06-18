---
chunk_id: discourse_topic_169029_post_210_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/210
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 333
username: 22f3000819
post_number: 210
topic_id: 169029
---

_path}' not found.")
 return pd.DataFrame()

parsed_logs = []
 with gzip.open(file_path, 'rt', encoding='utf-8') as f:
 for line in f:
 parsed_entry = parse_log_line(line)
 if parsed_entry:
 parsed_logs.append(parsed_entry)
 return pd.DataFrame(parsed_logs)

---

# Convert time format
def convert_time(timestamp):
 return datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S %z")

df = load_logs(file_path)

if not df.empty:
 df["datetime"] = df["time"].apply(convert_time)
 df["day_of_week"] = df["datetime"].dt.strftime('%A')
 df["hour"] = df["datetime"].dt.hour

# Filter conditions
 filtered_df = df[
 (df["method"] == "GET") &amp;
 (df["url"].str.startswith("/telugu/")) &amp;
 (df["status"] &gt;= 200) &amp; (df["status"] &lt; 300) &amp;
 (df["day_of_week"] == "Monday") &amp;
 (df["hour"] &gt;= 11) &amp;
 (df["hour"] &lt; 20)
 ]

# Compute hash of the result
 result_hash = compute_hash(str(len(filtered_df)))

# Output the count and hash
 print("Successful GET requests for /telugu/ on Mondays (11:00-7:59 AM):", len(filtered_df))
else:
 print("No log data available for processing.")
`
Both give the same output: 2698. Please help me identify the error, if any.
