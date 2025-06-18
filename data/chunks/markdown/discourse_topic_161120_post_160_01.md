---
chunk_id: discourse_topic_161120_post_160_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/160
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 561
username: Jivraj
post_number: 160
topic_id: 161120
---

 new URL each time it runs**, double-check that the **ngrok URL is correct** before submitting.

For **Question 9**, did you **enable CORS**? To verify, check your **browser console**—if CORS is not enabled, you should see an error message indicating the issue.

---

**[Discussion Image by Jivraj]** This image is from a student discussion thread and shows the Chrome Developer Tools Console, indicating a CORS (Cross-Origin Resource Sharing) error. The console output displays messages: "starting ajax request to the resource," "ajax request done," followed by an error message in red: "Access to XMLHttpRequest at 'http://google.com/' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource." This error means that the web application (origin 'null', likely due to running the HTML file directly from the file system) is attempting to make an AJAX request to 'http://google.com/', but the server (google.com) does not allow requests from that origin because it doesn't include the necessary 'Access-Control-Allow-Origin' header in its response. The error occurred in `index.html` at line 1, suggesting the student is encountering CORS issues during development. This suggests the student needs to either configure their local development environment to serve the files with an origin (e.g., using a local web server) or find an API that allows CORS requests from any origin, or configure a proxy to bypass CORS restrictions.Jan 2025]" thread, post #160. The console shows successful messages "starting ajax request to the resource" and "ajax request done," originating from index.html lines 14 and 29, respectively. However, an error message indicates "Access to XMLHttpRequest at 'http://google.com/' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource," which originates from index.html line 1. This CORS error indicates that the student's web application, running from a 'null' origin (likely a local file), is attempting to make a cross-origin request to google.com, which is blocked because the server at google.com does not include the necessary "Access-Control-Allow-Origin" header in its response, thus representing a common troubleshooting scenario for students during deployment. The student is likely facing issues related to cross-origin requests and server-side configuration and may need guidance on setting appropriate CORS headers or using a proxy." alt="image" data-base62-sha1="7dJYLvzlDP8Gb2dfAT6BF4N17QP" width="690" height="129" data-dominant-color="F2EAEB">image724×136 18.3 KB
