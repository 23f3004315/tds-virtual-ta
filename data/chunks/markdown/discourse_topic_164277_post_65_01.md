---
chunk_id: discourse_topic_164277_post_65_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/65
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 370
username: 23f2005138
post_number: 65
topic_id: 164277
---

https://discourse.onlinedegree.iitm.ac.in/t/164277/65)

For the question #A8 on recognizing the credit card number in the image, Open AI doesn’t seem to be recognizing the number correctly and as a result the evaluation is failing. What should be the solution?

---

**[Discussion Image by 23f2005138]** This image shows a student's attempt to use an LLM to extract a credit card number from an image and write it to a file. The task description is displayed first, followed by the HTTP POST request used to trigger the LLM with the encoded task. The server responds with HTTP 200 OK and a JSON payload indicating the LLM should use the `extract_numbers_from_image` function, specifying the input and output file paths. A subsequent HTTP GET request retrieves the content of the output file `/data/credit-card.txt`, and shows a discrepancy between the expected and actual result of the extraction, indicating a bug or incorrect extraction.spaces to a file. The log shows the HTTP POST request to the LLM, specifying the "extract_numbers_from_image" function, the input image file path, and the output text file path. A subsequent HTTP GET request retrieves the content of the output file, revealing a discrepancy between the expected and actual results: The expected number is "4026399336539356", but the actual result is "402639933635936", indicating the LLM did not extract the full number. This signifies a potential issue with the LLM's extraction capability or configuration." alt="image" data-base62-sha1="xuadyQv9NXtkZL0HXLiqBWQ8yaf" width="690" height="376" data-dominant-color="282827">image913×498 13.6 KB
