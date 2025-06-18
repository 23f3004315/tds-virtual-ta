---
chunk_id: discourse_topic_167172_post_8_04
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/8
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 176
username: Sakshi6479
post_number: 8
topic_id: 167172
---

 response")
 except KeyError as e:
 raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
 except Exception as e:
 raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
 
 return output

---

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)
`
and also i am sending postman request as http://localhost:8000/run?task=The file ./data/dates.txt contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to ./data/dates-wednesdays.txt

do I need to use dockerfile for this? i am still getting the same error as
