---
chunk_id: discourse_topic_164277_post_176_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/176
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 269
username: 22f3001315
post_number: 176
topic_id: 164277
---

## Post #176 by 22f3001315

**Direct Link**: [Post #176](https://discourse.onlinedegree.iitm.ac.in/t/164277/176)

ANY SUGGESTIONS (just one digit away) ::

`import easyocr
from pathlib import Path
import re

def extract_credit_card_number(input_image: str, output_file: str):
 
 input_path = Path(f".{input_image}")
 output_path = Path(f".{output_file}")

if not input_path.exists():
 raise ValueError(f"Image file {input_path} does not exist.")

# Step 1: Use OCR to extract text from the image
 reader = easyocr.Reader(['en'])
 try:
 result = reader.readtext(str(input_path))
 except Exception as e:
 raise ValueError(f"OCR processing failed: {str(e)}")

# Combine all extracted text into a single string
 extracted_text = " ".join([text for (_, text, _) in result])

# Step 2: Use the LLM to refine the extracted text and extract the credit card number
 prompt = f"""
 The following text was extracted from an image. It may contain a credit card number. 
 Extract the credit card number and return only the number without spaces or dashes. 
 If no credit card number is found, return "None".
