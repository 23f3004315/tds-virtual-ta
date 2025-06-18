---
chunk_id: discourse_topic_164277_post_638_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/638
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 288
username: Sakshi6479
post_number: 638
topic_id: 164277
---

## Post #638 by Sakshi6479

**Direct Link**: [Post #638](https://discourse.onlinedegree.iitm.ac.in/t/164277/638)

sir using prompt method also i am having the error please provide a step wise solution so then i can make functions accordingly.

`#/// Scirpt
# requires-python = "&gt;=3.13"
# dependencies = [
# "fastapi",
# "uvicorn",
# "requests",
# ]
#///

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import requests
import os
import json
from subprocess import run

app = FastAPI()

response_format = {
 "type": "json",
 "json_schema": {
 "name": "taks_runner",
 "schema": {
 "type": "object",
 "required": ["python_dependencies","python_code"],
 "properties": {
 "python_code": {
 "type": "string",
 "description": "Python code to perform the task"
 },
 "python_dependencies": {
 "type": "array",
 "items": {
 "type": "object",
 "properties": {
 "module": {
 "type": "string",
 "description": "Name of the python module"
 }
 },
 "required": ["module"],
 "additionalProperties": False
 }
 }
 }
 }
}
}
