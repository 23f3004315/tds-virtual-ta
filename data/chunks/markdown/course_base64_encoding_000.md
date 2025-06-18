---
chunk_id: course_base64_encoding_000
source_url: https://tds.s-anand.net/#/base64-encoding
source_title: base64-encoding
content_type: course
tokens: 460
---

# Base 64 Encoding

Base64 is a method to convert binary data into ASCII text. It's essential when you need to transmit binary data through text-only channels or embed binary content in text formats.

Watch this quick explanation of how Base64 works (3 min):

[**[Course Image: What is Base64? (3 min)]** This image introduces the core question: "What is Base64?". Base64 encoding is a method used to represent binary data in an ASCII string format, which is particularly useful for transmitting data over channels that only support text. It works by converting binary data into a 64-character alphabet (A-Z, a-z, 0-9, +, /), making it safe for transport in text-based formats like email or XML. Understanding Base64 is essential when dealing with embedding images, handling API authentication, or working with data formats that require text-based representation of binary information. The purpose is to allow binary data to be represented and transmitted as text, and the subsequent learning will dive into the mechanics of how it works.o convert binary data into an ASCII string format. This encoding is particularly useful when you need to transmit binary data over media that only supports ASCII characters. The encoding scheme represents binary data in a radix-64 representation, hence the name "Base64." It works by dividing the binary data into 6-bit blocks, each of which is then translated into one of 64 characters, making it safe for transport in various text-based formats. The question mark in the image emphasizes the introductory nature of this material, prompting learners to explore what Base64 is.)](https://youtu.be/8qkxeZmKmOY)

Here's how it works:

- It takes 3 bytes (24 bits) and converts them into 4 ASCII characters
- ... using 64 characters: A-Z, a-z, 0-9, + and / (padding with `=` to make the length a multiple of 4)
- There's a URL-safe variant of Base64 that replaces + and / with - and \_ to avoid issues in URLs
- Base64 adds ~33% overhead (since every 3 bytes becomes 4 characters)

Common Python operations with Base64:

```python
import base64
