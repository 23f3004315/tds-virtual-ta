---
chunk_id: discourse_topic_169029_post_515_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/515
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 383
username: 23f1002574
post_number: 515
topic_id: 169029
---

**[Discussion Image by 23f1002574]** This image shows a log output related to HTTP requests received by a server, likely part of the TDS (Traffic Data Server) project. The log entries indicate several types of requests, including "POST /tdsp2 HTTP/1.1" which resulted in a 200 OK response, and numerous "GET" requests for resources like "/," "/favicon.ico," and even potentially malformed requests like "PRI %2A HTTP/2.0," all returning a 404 Not Found error. Additionally, the logs include "WARNING: Invalid HTTP request received" messages, indicating improperly formatted or unexpected requests. These logs likely stem from peer testing or incomplete client implementations attempting to interact with the server, highlighting potential debugging points. The presence of both "INFO" and "WARNING" level messages can help developers filter and prioritize issues in the application.ver, including successful POST requests to "/tdsp2" (200 OK) and numerous unsuccessful GET requests resulting in 404 Not Found errors, particularly for the root path ("/"), favicon.ico, and potentially other resources. Some requests are marked with a "WARNING: Invalid HTTP request received" message, hinting at malformed or unsupported request formats. The entries also display the client IP address and port number, the HTTP method and path, and the HTTP version used. This likely represents a student debugging their TDS Solver implementation and encountering issues with handling certain HTTP requests, particularly GET requests for common resources or invalidly formatted requests." alt="Screenshot 2025-04-14 144745" data-base62-sha1="v0YKfuaRjegRAdkeCmN5wg5GTkn" width="690" height="361" data-dominant-color="151515">Screenshot 2025-04-14 144745934×490 31.1 KB
