---
chunk_id: discourse_topic_161120_post_31_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161120/31
source_title: GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 968
username: kushabarodekar
post_number: 31
topic_id: 161120
---

Hi Team ,

For GA - 2 , Question 6:

I am done with the code, deployed same on vercel.

And It is working fine gives correct json response as expected in browser.

But When I try to that on portal It gives me “CORS Missing Allow Origin” Error.

---

**[Discussion Image by kushabarodekar]** This image shows a student troubleshooting their Vercel app deployment for a TDS assignment where they must expose an API. The assignment requires students to download a `q-vercel-python.json` file, deploy a Python app to Vercel, and create an API endpoint `/api?name=X&name=Y` that returns a JSON response with the marks of names X and Y. The student's attempted URL `https://vercel-[redacted]-bhagra-barodekars-projects.vercel.app/api` results in a "TypeError: NetworkError when attempting to fetch resource." The Chrome DevTools Network tab shows a GET request to `[redacted]QN&name=BUD4` with the status "CORS Missing Allow Origin," indicating a Cross-Origin Resource Sharing (CORS) issue, but another GET request has status 200. The student likely needs to configure CORS headers in their Vercel app to allow requests from the origin where they are testing the API, but one request succeeded suggesting the CORS issue may be intermittent or only apply to certain requests.client-side script from accessing the response. The task instructions ask students to deploy a Python app to Vercel, exposing an API to return JSON data for student names." alt="Screenshot 2025-01-16 at 6.58.43 PM" data-base62-sha1="2oTTntxP2h8xoBufCxOgrVYAQ1s" width="690" height="259" srcset="**[Discussion Image by kushabarodekar]** This image depicts a student encountering a "TypeError: NetworkError when attempting to fetch resource" when trying to access their deployed Vercel application, part of a TDS course assignment "GA2 - Deployment Tools". The student is trying to access an API endpoint following the structure "https://[student-specific-vercel-url].vercel.app/api", as instructed in the assignment, but is getting the error. Below the error, the Chrome DevTools 'Network' tab is open, showing multiple GET requests including one with status code 200 for a similar URL pattern "...vercel.app/api?name=Q&name=...", suggesting a successful request, however, another GET request with the error "CORS Missing Allow Origin" indicating a Cross-Origin Resource Sharing issue is also visible. The assignment requires deploying a Python app to Vercel and exposing an API endpoint to return JSON responses., **[Discussion Image by kushabarodekar]** This image captures a student's attempt to deploy a Python app to Vercel and expose an API as part of a TDS assignment. The student is facing a "TypeError: NetworkError when attempting to fetch resource" when trying to access their Vercel URL, specifically `https://[redacted]-shagra-barodekars-projects.vercel.app/api`. The browser's developer tools (Network tab) show multiple GET requests; one yields a "CORS Missing Allow Origin" error, while another to the same base URL but with appended name parameters returns a 200 OK status. This indicates a potential CORS (Cross-Origin Resource Sharing) issue, likely arising from the server not explicitly allowing requests from the client's origin, and suggests the student may need to configure their Vercel deployment to handle CORS appropriately, potentially within the Python application or Vercel's settings. 1.5x, **[Discussion Image by kushabarodekar]** This image depicts a student facing a "TypeError: NetworkError when attempting to fetch resource" in their Vercel deployment of a Python app, during a TDS assignment involving deployment tools. The student is attempting to access the Vercel URL, which should return a JSON response based on name parameters in the URL. The browser's developer tools are open to the "Network" tab, showing successful (200 OK) GET requests, but one request shows "CORS Missing Allow Origin" error related to cross-origin resource sharing issue. The student is facing CORS problem while trying to hit the /api endpoint, indicating the server is not configured to allow requests from the origin which is causing the TypeError, which could point towards misconfiguration of the server-side CORS policy for the API. 2x" data-dominant-color="EAE9EB">Screenshot 2025-01-16 at 6.58.43 PM3570×1344 436 KB
