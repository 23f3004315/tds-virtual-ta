---
chunk_id: discourse_topic_164277_post_514_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/514
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 243
username: 23f2001286
post_number: 514
topic_id: 164277
---

 "You are a function classifier that extracts structured parameters from queries."},
 {"role": "user", "content": prompt}
 ],
 "tools": [
 {
 "type": "function",
 "function": function
 } for function in function_definitions_llm
 ],
 "tool_choice": "auto"
 },
 )

---

print("DId suceessful llm calll")#Debug
`
`INFO: 127.0.0.1:52108 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 400 Bad Request
`
