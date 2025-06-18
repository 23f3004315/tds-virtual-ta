---
chunk_id: discourse_topic_166357_post_1_06
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166357/1
source_title: Doubts in Q7, Q8
content_type: discourse
tokens: 352
username: Sakshi6479
post_number: 1
topic_id: 166357
---

 issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -&gt; Dict[str, Any]:
 """Extract parameters from the query string."""
 # Convert the query to lowercase for case-insensitive matching
 query = query.strip().lower()

---

if match := re.match(r"what is the status of ticket (\d+)\?", query):
 return {
 "name": "get_ticket_status",
 "arguments": {"ticket_id": int(match.group(1))}
 }
 elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
 return {
 "name": "schedule_meeting",
 "arguments": {
 "date": match.group(1),
 "time": match.group(2),
 "meeting_room": match.group(3)
 }
 }
 elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
 return {
 "name": "get_expense_balance",
 "arguments": {"employee_id": int(match.group(1))}
 }
 elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
 return {
 "name": "calculate_performance_bonus",
 "arguments": {
 "employee_id": int(match.group(1)),
 "current_year": int(match.group(2))
 }
 }
 elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
 return {
 "name": "report_office_issue",
 "arguments": {
 "issue_code": int(match.group(1)),
 "department": match.group(2)
 }
 }
 return {}
