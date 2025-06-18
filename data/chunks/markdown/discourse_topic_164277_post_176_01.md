---
chunk_id: discourse_topic_164277_post_176_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/176
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 267
username: 22f3001315
post_number: 176
topic_id: 164277
---

 the extracted text and extract the credit card number
 prompt = f"""
 The following text was extracted from an image. It may contain a credit card number. 
 Extract the credit card number and return only the number without spaces or dashes. 
 If no credit card number is found, return "None".

---

Extracted text: {extracted_text}
 """
 try:
 response = chat_completion(prompt)
 card_number = response.get("choices", [])[0].get("message", {}).get("content", "").strip()

# Validate the card number (basic check for 16 digits)
 if card_number.lower() == "none" or not card_number.isdigit() or len(card_number) != 16:
 raise ValueError("No valid credit card number found in the image.")

# Write the card number to the output file
 output_path.parent.mkdir(parents=True, exist_ok=True)
 with open(output_path, "w") as f:
 f.write(card_number)

return f"A8 Completed: Credit card number extracted and written to {output_file}"
 except Exception as e:
 raise ValueError(f"Failed to process text with LLM: {str(e)}")
`
` /data/credit-card.txt
⚠️ EXPECTED:
4026399336539356
⚠️ RESULT:
4026399338539356
`
