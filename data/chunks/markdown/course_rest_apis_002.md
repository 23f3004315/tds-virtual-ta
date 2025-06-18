---
chunk_id: course_rest_apis_002
source_url: https://tds.s-anand.net/#/rest-apis
source_title: rest-apis
content_type: course
tokens: 210
---

 ```python
 {
 "error": "Not Found",
 "message": "User 123 not found",
 "status_code": 404
 }
 ```
4. **Use Query Parameters for Filtering**
 ```
 /api/posts?status=published&category=tech
 ```
5. **Implement Pagination**
 ```
 /api/posts?page=2&limit=10
 ```

Tools:

---

- [Postman](https://www.postman.com/): API testing and documentation
- [Swagger/OpenAPI](https://swagger.io/): API documentation
- [HTTPie](https://httpie.io/): Modern command-line HTTP client
- [JSON Schema](https://json-schema.org/): API request/response validation

Learn more about REST APIs:

- [REST API Design Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)
- [Google API Design Guide](https://cloud.google.com/apis/design)
