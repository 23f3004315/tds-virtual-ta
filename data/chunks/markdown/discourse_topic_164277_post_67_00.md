---
chunk_id: discourse_topic_164277_post_67_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/67
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 280
username: 23f2005325
post_number: 67
topic_id: 164277
---

## Post #67 by 23f2005325

**Direct Link**: [Post #67](https://discourse.onlinedegree.iitm.ac.in/t/164277/67)

Getting the following error :

`127.0.0.1 - - [07/Feb/2025 01:44:54] "GET /run?task=generate%20data%20for%20ujanaishik109@gmail.com HTTP/1.1" 200 -
 File "/tmp/datagenyhqKlO.py", line 1
 404: Not Found
 ^^^
SyntaxError: illegal target for annotation

`
when executing the following code :

Main.py
`@routes.route("/run", methods=["GET", "POST"])
def run():
 task = request.args.get("task")
 try:
 res = get_func_name(task)
 func_name = res["func_name"]
 args = res.get("arguments", [])
 print("ARGUMENTS : ", args)
 if args:
 generated_func = globals()[func_name](*args)
 print("GENERATED FUNC :",generated_func)
 res = f"{func_name} executed successfully"
 else:
 generated_func = globals()[func_name]()
 print(generated_func)
 res = f"{func_name} executed successfully"
 except Exception as e:
 res = None
 print("error : ", e)
 return jsonify(res)
