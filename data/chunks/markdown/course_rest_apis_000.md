---
chunk_id: course_rest_apis_000
source_url: https://tds.s-anand.net/#/rest-apis
source_title: rest-apis
content_type: course
tokens: 486
---

## REST APIs

REST (Representational State Transfer) APIs are the standard way to build web services that allow different systems to communicate over HTTP. They use standard HTTP methods and JSON for data exchange.

Watch this comprehensive introduction to REST APIs (52 min):

[**[Course Image: REST API Crash Course - Introduction + Full Python API Tutorial (52)]** This image is a title card for a crash course video aimed at introducing REST APIs. The video intends to provide a full Python API tutorial. The objective is to give learners a foundational understanding of REST APIs, which involves learning about different HTTP methods and using JSON for data exchange. Upon completing this video, students should be able to build simple RESTful APIs using Python. Prior knowledge of Python programming and basic web concepts would be beneficial for understanding the material.through a crash course format, aiming to provide a foundational understanding within approximately one hour. The focus is on grasping the core principles of RESTful architecture and how APIs facilitate communication between different software systems. Students will learn how to design, build, and interact with REST APIs using Python. The course covers essential concepts like HTTP methods (GET, POST, PUT, DELETE), request/response structures, and data serialization formats (e.g., JSON). After completing this module, students should be able to implement basic API functionalities in TDS projects.)](https://youtu.be/qbLc5a9jdXo)

Key Concepts:

1. **HTTP Methods**
 - `GET`: Retrieve data
 - `POST`: Create new data
 - `PUT/PATCH`: Update existing data
 - `DELETE`: Remove data
2. **Status Codes**
 - `2xx`: Success (200 OK, 201 Created)
 - `4xx`: Client errors (400 Bad Request, 404 Not Found)
 - `5xx`: Server errors (500 Internal Server Error)

Here's a minimal REST API using FastAPI. Run this `server.py` script via `uv run server.py`:

```python
# /// script
# requires-python = ">=3.13"
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
