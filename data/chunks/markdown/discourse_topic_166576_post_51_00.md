---
chunk_id: discourse_topic_166576_post_51_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/166576/51
source_title: GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 289
username: lakshaygarg654
post_number: 51
topic_id: 166576
---

## Post #51 by lakshaygarg654

**Direct Link**: [Post #51](https://discourse.onlinedegree.iitm.ac.in/t/166576/51)

Thank you for your response @carlton. You are absolutely right—my query was unnecessarily complex. Initially, I attempted a simpler approach, using various JSON extraction functions. However, I encountered multiple errors, including:

**`json_extract`**: *“Table Function with name ‘json_extract’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*
**`json_each`**: *“Table Function with name ‘json_each’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*
**`json_extract_path_text`**: *“Table Function with name ‘json_extract_path_text’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*

Since the simple approach did not work, I attempted a more complex query to achieve the desired result. However, that too did not yield the expected output. To gain better insight, I extracted ten values into a table using the console and then reconstructed the query accordingly. Unfortunately, I am still facing issues related to functions not being recognized in the catalog.
