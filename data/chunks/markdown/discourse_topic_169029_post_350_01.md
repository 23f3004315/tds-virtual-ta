---
chunk_id: discourse_topic_169029_post_350_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/350
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 454
username: 23f2004912
post_number: 350
topic_id: 169029
---

**[Discussion Image by 23f2004912]** This image depicts a log from the TDS (Tenable Data Stream) Python application, indicating a mix of successful (200 OK) and unsuccessful (404 Not Found, 405 Method Not Allowed) HTTP requests. The log entries show timestamps, the process ID (79249), request types (GET, POST, PROPFIND), requested paths (e.g., "/t4", "/favicon.ico", "/.env", "/logincheck"), and the corresponding HTTP status codes. Notably, there are several "404 Not Found" errors for requests to files like ".env" and ".git/config", likely indicating attempts to access sensitive files. The presence of "405 Method Not Allowed" errors suggests attempts to use the PROPFIND method, which might not be supported. Finally, an "Invalid HTTP request received" warning is present, and the shell prompt "azureuser@TDS:~$" suggests the logs originate from an Azure environment.ET" and "PROPFIND" requests for different paths. Several requests result in "404 Not Found" errors, specifically for paths like "/t4", "/.env", "/.git/config", "/autodiscover/autodiscover.json?@zdi/Powershell", "/actuator/health", and "/logincheck", indicating that these resources were not found on the server. Some requests return "200 OK", showing successful retrieval of resources like "/favicon.ico" and "/", while "PROPFIND" requests receive a "405 Method Not Allowed" error, suggesting the server doesn't support the "PROPFIND" method. The output also contains a warning: "Invalid HTTP request received," suggesting an issue with the format of a request. The azureuser@TDS:~$ prompt indicates the current user and directory in the terminal session." alt="Screenshot 2025-04-05 232353" data-base62-sha1="zMnakAIYnzMopEfpJrr1w3jfyDJ" width="690" height="221" data-dominant-color="212121">Screenshot 2025-04-05 2323531758×564 57.8 KB
