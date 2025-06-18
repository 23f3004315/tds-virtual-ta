---
chunk_id: discourse_topic_171141_post_394_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/394
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 398
username: 22f2001640
post_number: 394
topic_id: 171141
---

itm.ac.in/t/171141/394)

Hi @carlton ,

I couldn’t find my Docker logs or evaluation logs in the latest result mail, even though I had passed the prerequisites. I also tried reproducing the test environment and scored 9/25 (screenshot attached below).

---

**[Discussion Image by 22f2001640]** This image depicts a student's terminal output during the TDS project, specifically showcasing an error related to file reading. The output shows an HTTP GET request to `http://localhost:8000/read?path=/data/c5.txt` which resulted in a "500 Internal Server Error," indicating a problem on the server side. Critically, the error message "C5 failed: Cannot read /data/c5.txt" reveals the root cause: the application is unable to locate or access the specified file. The student's score is 9/25, suggesting multiple test cases have failed. The terminal also displays a successful HTTP POST request to the OpenAI embeddings endpoint, showing that at least network connectivity is working correctly. that the program is unable to access the file `/data/c5.txt`. The HTTP request "GET http://localhost:8000/read?path=/data/c5.txt" resulted in a "500 Internal Server Error", suggesting a problem on the server-side when trying to access the requested file. The test case C5 is marked as failed, leading to a score of 9/25, signaling the student did not correctly implement the file-reading functionality. The successful POST request to the embeddings API suggests that the issue is localized to the file access part of the code, not the OpenAI API communication." alt="image" data-base62-sha1="A7coZQExGa1MqCCfz5m4svLGMDf" width="690" height="164" data-dominant-color="252424">image1124×268 9.8 KB
