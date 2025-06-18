---
chunk_id: discourse_topic_169029_post_65_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/65
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 543
username: 23f2004837
post_number: 65
topic_id: 169029
---

)
 if status_code != 200:
 return False
 
 # check the returned json matches the use case
 if "GA_No" in response_text and response_text["GA_No"] == use_case:
 return True
 else:
 return False
 else:
 #print("File does not exist.")
 return False

---

async def main():
 use_cases = [
 "GA1.1", "GA1.2", "GA1.3", "GA1.4", "GA1.5", "GA1.6", "GA1.7", "GA1.8", "GA1.9", "GA1.10", "GA1.11", "GA1.12", "GA1.13", "GA1.14", "GA1.15", "GA1.16", "GA1.17", "GA1.18",
 "GA2.1", "GA2.2", "GA2.3", "GA2.4", "GA2.5", "GA2.6", "GA2.7", "GA2.8", "GA2.9", "GA2.10",
 "GA3.1", "GA3.2", "GA3.3", "GA3.4", "GA3.5", "GA3.6", "GA3.7", "GA3.8", "GA3.9",
 "GA4.1", "GA4.2", "GA4.3", "GA4.4", "GA4.5", "GA4.6", "GA4.7", "GA4.8", "GA4.9", "GA4.10",
 "GA5.1", "GA5.2", "GA5.3", "GA5.4", "GA5.5", "GA5.6", "GA5.7", "GA5.8", "GA5.9", "GA5.10"
 ]
 use_cases = random.sample(use_cases, 5)
 a_score, a_total = 0, 0
 for use_case in use_cases:
 a_total += 1
 try:
 success = await evaluate(use_case)
 except Exception as e:
 logging.error(f"🔴 {use_case} failed: {e}")
 success = False
 if success:
 logging.info(f"✅ {use_case} PASSED")
 else:
 logging.error(f"❌ {use_case} FAILED")
 a_score += 1 if success else 0
 
 logging.info(f"🎯 Parsed: {a_score} / {a_total}")
