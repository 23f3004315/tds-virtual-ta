---
chunk_id: discourse_topic_163247_post_64_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/64
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 593
username: 23f2003853
post_number: 64
topic_id: 163247
---

 #64 by 23f2003853

**Direct Link**: [Post #64](https://discourse.onlinedegree.iitm.ac.in/t/163247/64)

Dear Sir, I got the answer in json but none out put is correct. Please help me to correct the code

---

curl https://api.openai.com/v1/chat/completions \ &gt; -H “Content-Type: application/json” \ &gt; -H “Authorization: Bearer $TOKEN” \ '{ &gt; -d ‘{ &gt; “model”: “gpt-4o-mini”, "messa&gt; “messages”: [{ &gt; “role”: “user”, "c&gt; “content”: “List only the valid English words from these: zqndWw3FB, kM, K, njuHs9A, r, lkXJ1lG, Z, yLHDClp, G1Db, 7, m, MYieYF3B, pFTQ1JU8Fj, RL9n6kE, EVpChB, V6iCpP, 9YwiwAnBc5, R, UM, mrnyc, 4ej9x, 8X, CQA9, jHC, uL4G6, f, zzaozWC9, 0qsOenEndF, qaZ2WoX, nXGZ” &gt; }] &gt; }’ { “id”: “chatcmpl-AwTPGH241yjyg9EkO1t1tbeGU7KCu”, “object”: “chat.completion”, “created”: 1738499426, “model”: “gpt-4o-mini-2024-07-18”, “choices”: [ { “index”: 0, “message”: { “role”: “assistant”, “content”: “The valid English words from your list are:\n\n- my\n- is\n- an\n- or\n- in\n\n(Note: This assumes a focus on short English words. Longer words or specific proper nouns may also exist but were not included in this selection.)”, “refusal”: null }, “logprobs”: null, “finish_reason”: “stop” } ], “usage”: { “prompt_tokens”: 160, “completion_tokens”: 53, “total_tokens”: 213, “prompt_tokens_details”: { “cached_tokens”: 0, “audio_tokens”: 0 }, “completion_tokens_details”: { “reasoning_tokens”: 0, “audio_tokens”: 0, “accepted_prediction_tokens”: 0, “rejected_prediction_tokens”: 0 } }, “service_tier”: “default”, “system_fingerprint”: “fp_72ed7ab54c” }
