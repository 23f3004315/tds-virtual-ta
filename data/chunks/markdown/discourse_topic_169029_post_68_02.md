---
chunk_id: discourse_topic_169029_post_68_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/68
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 363
username: 23f2000573
post_number: 68
topic_id: 169029
---

 binary, or will it be a string.

Example for string. Consider the table

Col 1
Col 2

Row 1, Col1
Row 1 Col 2

Row 2, Col 1
Row 2 Col 2

Will this be something like this

---

`"|Col 1| Col 2|\n|-|-|\n|Row 1, Col1 | Row 1 Col 2|\n|Row 2, Col 1|Row 2 Col 2|"
`
or something like

`"&lt;table&gt;\n&lt;thead&gt;\n&lt;tr&gt;\n&lt;th&gt;Col 1&lt;/th&gt;\n&lt;th&gt;Col 2&lt;/th&gt;\n&lt;/tr&gt;\n&lt;/thead&gt;\n&lt;tbody&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 1, Col1&lt;/td&gt;\n&lt;td&gt;Row 1 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 2, Col 1&lt;/td&gt;\n&lt;td&gt;Row 2 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;/tbody&gt;\n&lt;/table&gt;
"
`
HIDDEN BLOCK AND ANSWER : 2 TASKS
In one question, there were two tasks.

Find the answer to the question
Enable the `disabled` text block

In this question, what will the answer type be?

Should it just be the answer or should it be the html string which will have the disabled block enabled and also the answer string sitting inside the block
