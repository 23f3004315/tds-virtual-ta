---
chunk_id: course_rest_apis_001
source_url: https://tds.s-anand.net/#/rest-apis
source_title: rest-apis
content_type: course
tokens: 522
---

 = ">=3.13"
# dependencies = [
# "fastapi",
# "uvicorn",
# ]
# ///
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

# Create a list of items that will act like a database
items: List[Dict[str, float | int | str]] = []

---

# Create a GET endpoint that returns all items
@app.get("/items")
async def get_items() -> List[Dict[str, float | int | str]]:
 return items

# Create a GET endpoint that returns a specific item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int) -> Dict[str, float | int | str]:
 if item := next((i for i in items if i["id"] == item_id), None):
 return item
 raise HTTPException(status_code=404, detail="Item not found")

# Create a POST endpoint that creates a new item
@app.post("/items")
async def create_item(item: Dict[str, float | str]) -> Dict[str, float | int | str]:
 new_item = {"id": len(items) + 1, "name": item["name"], "price": float(item["price"])}
 items.append(new_item)
 return new_item

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)
```

Test the API with curl:

```bash
# Get all items
curl http://localhost:8000/items

# Create an item
curl -X POST http://localhost:8000/items \
 -H "Content-Type: application/json" \
 -d '{"name": "Book", "price": 29.99}'

# Get specific item
curl http://localhost:8000/items/1
```

Best Practices:

1. **Use Nouns for Resources**
 - Good: `/users`, `/posts`
 - Bad: `/getUsers`, `/createPost`
2. **Version Your API**
 ```
 /api/v1/users
 /api/v2/users
 ```
3. **Handle Errors Consistently**
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
