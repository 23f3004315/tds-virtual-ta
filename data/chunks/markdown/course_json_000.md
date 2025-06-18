---
chunk_id: course_json_000
source_url: https://tds.s-anand.net/#/json
source_title: json
content_type: course
tokens: 488
---

## JSON

JSON (JavaScript Object Notation) is the de facto standard format for data exchange on the web and APIs. Its human-readable format and widespread support make it essential for data scientists working with web services, APIs, and configuration files.

For data scientists, JSON is essential when:

- Working with REST APIs and web services
- Storing configuration files and metadata
- Parsing semi-structured data from databases like MongoDB
- Creating data visualization specifications (e.g., Vega-Lite)

Watch this comprehensive introduction to JSON (15 min):

[**[Course Image: JSON Crash Course]** This image introduces JSON (JavaScript Object Notation) as a data format using a "Crash Course" approach, emphasizing its role in data serialization. JSON structures data as key-value pairs within curly braces `{}`. The example displays a JSON object representing information about a company, with keys like `"name"`, `"employees"`, `"ceo"`, and `"rating"` and their corresponding values such as `"Big Corporation"`, `10000`, `null`, and `4.3` respectively. A key learning point is understanding that values can be strings, numbers, or even `null`. JSON is a foundational concept for effectively using externalization specifications like Vega-Lite within TDS.t JSON based on the image:

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. The image showcases a JSON crash course covering how data is structured within JSON using key-value pairs such as `"name": "Big Corporation"` and `"numberOfEmployee": 10000`, where keys are enclosed in double quotes, followed by a colon, and then the corresponding value. Values can be strings, numbers, booleans, or even nested JSON objects. This structure allows for representing complex data in a simple and organized manner, making it a fundamental skill for data science projects, including working with APIs and configurations files.)](https://youtu.be/GpOO5iKzOmY)

Key concepts to understand in JSON:

- JSON only supports 6 data types: strings, numbers, booleans, null, arrays, and objects
- You can nest data. Arrays and objects can contain other data types, including other arrays and objects
- Always validate. Ensure JSON is well-formed. Comm errors: Trailing commas, missing quotes, and escape characters
