---
chunk_id: discourse_topic_164277_post_411_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/411
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 451
username: Nelson
post_number: 411
topic_id: 164277
---

**[Discussion Image by Nelson]** This image shows a student (Nelson) encountering an error while trying to use `curl` in PowerShell to send a POST request to the `aiproxy.sanand.workers.dev` endpoint for embedding generation. The `curl` command includes headers for `Content-Type` and `Authorization`, attempting to use the `$AIPROXY_TOKEN` environment variable for authentication. However, the server returns a JSON response with the message "Missing Authorization: Bearer header," indicating that the authorization token was either not correctly passed or not recognized by the server. The response also directs the student to a GitHub repository (`https://github.com/sanando/aiproxy`) for more information about the AI proxy. This suggests a problem with the environment variable or how `curl` is interpreting/passing it, or a general setup issue with the AI proxy token and is a student question, not instructor answer or peer discussion.ings, which results in an authentication error. The command used is `curl -X POST http://aiproxy.sanand.workers.dev/openai/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AIPROXY_TOKEN" -d '{"model": "text-embedding-3-small", "input": ["king", "queen"]}'`. The error message, `"message": "Missing Authorization: Bearer header. See https://github.com/sanand0/aiproxy"`, indicates that the `$AIPROXY_TOKEN` variable was not correctly set or accessible within the PowerShell environment, causing the request to fail due to a missing or invalid authorization header; the reference link might provide details on how to set the token correctly. Therefore, Nelson is facing an authentication issue that needs to be resolved by properly configuring the `$AIPROXY_TOKEN` environment variable with the correct API key before running the `curl` command." alt="image" data-base62-sha1="r2Mjja9KwWVfUIYbgXLiuB4qsH4" width="690" height="208" data-dominant-color="16191A">image967×292 16.5 KB
