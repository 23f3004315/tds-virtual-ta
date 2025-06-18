---
chunk_id: discourse_topic_161120_post_52_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/52
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 313
username: carlton
post_number: 52
topic_id: 161120
---

-type','application/json')
 self.send_header("Access-Control-Allow-Origin", "*")
 self.end_headers()
 self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
 return
`
Notice there is no `if __name__ == "__main__":` code block.

---

This would instruct the interpreter that this is the starting point of your module. Clearly we do not want that, we want vercel to handle all the backend server stuff because vercel might be running some preflight code before it runs your application.

`if __name__ == "__main__":` is used to execute some code **only** if the file was run directly, and not imported. In vercel, it might not be the starting point of the application.

Try rewriting it with just the required endpoint function inside the default `handler` class. Avoid custom named classes until you can get a working prototype working using the boilerplate that has been shared.

Another possible problem:

By default, the JSON module encodes Unicode objects (such as str and Unicode) into the \u escape sequence when generating JSON data. The GA however is expecting a serialised UTF-8 JSON response instead. These might look the same on the screen but are not equivalent at the bytecode level. These encoding problems were covered in one of the videos that talked about encoding issues TDS &gt; Development Tools &gt; unicode

So converting your output to UTF-8 might fix it.

Let us know what worked. We are all learning from each other.

Kind regards
