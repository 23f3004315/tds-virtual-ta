---
chunk_id: course_cors_001
source_url: https://tds.s-anand.net/#/cors
source_title: cors
content_type: course
tokens: 430
---

```http
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
```

To implement CORS in FastAPI, use the [`CORSMiddleware` middleware](https://fastapi.tiangolo.com/tutorial/cors/):

---

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins
# Or, provide more granular control:
app.add_middleware(
 CORSMiddleware,
 allow_origins=["https://example.com"], # Allow a specific domain
 allow_credentials=True, # Allow cookies
 allow_methods=["GET", "POST", "PUT", "DELETE"], # Allow specific methods
 allow_headers=["*"], # Allow all headers
)
```

Testing CORS with JavaScript:

```javascript
// Simple request
const response = await fetch("https://api.example.com/data", {
 method: "GET",
 headers: { "Content-Type": "application/json" },
});

// Request with credentials
const response = await fetch("https://api.example.com/data", {
 credentials: "include",
 headers: { "Content-Type": "application/json" },
});
```

Useful CORS debugging tools:

- [CORS Checker](https://cors-test.codehappy.dev/): Test CORS configurations
- Browser DevTools Network tab: Inspect CORS headers and preflight requests
- [cors-anywhere](https://github.com/Rob--W/cors-anywhere): CORS proxy for development

Common CORS errors and solutions:

- `No 'Access-Control-Allow-Origin' header`: Configure server to send proper CORS headers
- `Request header field not allowed`: Add required headers to `Access-Control-Allow-Headers`
- `Credentials flag`: Set both `credentials: 'include'` and `Access-Control-Allow-Credentials: true`
- `Wild card error`: Cannot use `*` with credentials; specify exact origins
