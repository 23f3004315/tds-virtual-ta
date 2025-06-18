---
chunk_id: discourse_topic_164277_post_67_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/67
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 147
username: 23f2005325
post_number: 67
topic_id: 164277
---

 FUNC :",generated_func)
 res = f"{func_name} executed successfully"
 else:
 generated_func = globals()[func_name]()
 print(generated_func)
 res = f"{func_name} executed successfully"
 except Exception as e:
 res = None
 print("error : ", e)
 return jsonify(res)

---

`
Tasks.py
`def generate_data_files(user_email: str):
 subprocess.Popen(
 [
 "uv",
 "run",
 "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py",
 f"{user_email}",
 "--root",
 "../data",
 ]
 )
 print("data generated successfully")
`
Please Guide @s.anand @carlton @Jivraj
