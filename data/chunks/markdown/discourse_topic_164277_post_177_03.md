---
chunk_id: discourse_topic_164277_post_177_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/177
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 356
username: 23f1002382
post_number: 177
topic_id: 164277
---

 print(response.json())
 result = response.json() 
response = query_gpt_image("data/credit_card.png","Extract the credit card number from image")
`
Why is this not working?

EDIT: Requires prompt engineering as “credit card” is sensitive information

&lt;Response [200]&gt;

---

{‘id’: ‘chatcmpl-B0Dlie1ZIS68PZBCT0XJKhLKbyPAC’, ‘object’: ‘chat.completion’, ‘created’: 1739392626, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: ‘The numbers extracted from the image are:\n\n- 3009 1429 5211 59\n- 09/29\n- 113’, ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘stop’}], ‘usage’: {‘prompt_tokens’: 871, ‘completion_tokens’: 31, ‘total_tokens’: 902, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_bd83329f63’, ‘monthlyCost’: 0.05092764000000002, ‘cost’: 0.002799, ‘monthlyRequests’: 52}

`response = query_gpt_image("data/credit_card.png","Extract number from image")
`
