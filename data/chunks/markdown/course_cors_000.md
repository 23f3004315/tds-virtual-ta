---
chunk_id: course_cors_000
source_url: https://tds.s-anand.net/#/cors
source_title: cors
content_type: course
tokens: 495
---

## CORS: Cross-Origin Resource Sharing

CORS (Cross-Origin Resource Sharing) is a security mechanism that controls how web browsers handle requests between different origins (domains, protocols, or ports). Data scientists need CORS for APIs serving data or analysis to a browser on a different domain.

Watch this practical explanation of CORS (3 min):

[**[Course Image: CORS in 100 Seconds]** This image serves as the title card for a short video explaining CORS (Cross-Origin Resource Sharing). CORS is a browser security feature that restricts web pages from making requests to a different domain than the one which served the web page. This video aims to quickly explain the core concept of CORS, which is essential for web developers building applications that interact with APIs or resources from different origins. Understanding CORS is crucial to avoid common browser security errors and ensure that your application can securely access the resources it needs. It is particularly relevant in TDS projects involving APIs or client-server communication.of CORS, which stands for Cross-Origin Resource Sharing. CORS is a security feature implemented in web browsers that restricts web pages from making requests to a different domain than the one which served the web page. It essentially prevents malicious websites from accessing sensitive data from other websites you might be logged into. Understanding CORS is crucial for web developers to securely handle requests between different origins, especially when building applications that interact with APIs. Properly configuring CORS is essential to allow legitimate cross-origin requests while preventing unauthorized access to resources.)](https://youtu.be/4KHiSt0oLJ0)

Key CORS concepts:

- **Same-Origin Policy**: Browsers block requests between different origins by default
- **CORS Headers**: Server responses must include specific headers to allow cross-origin requests
- **Preflight Requests**: Browsers send OPTIONS requests to check if the actual request is allowed
- **Credentials**: Special handling required for requests with cookies or authentication

If you're exposing your API with a GET request publicly, the only thing you need to do is set the HTTP header `Access-Control-Allow-Origin: *`.

Here are other common CORS headers:

```http
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
```

To implement CORS in FastAPI, use the [`CORSMiddleware` middleware](https://fastapi.tiangolo.com/tutorial/cors/):
