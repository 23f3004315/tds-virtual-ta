---
chunk_id: discourse_topic_171141_post_316_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/316
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 334
username: carlton
post_number: 316
topic_id: 171141
---

latest_sha}.zip"

# Create the directory if it doesn't exist
 os.makedirs (save_path, exist_ok=True)

with open (save_path + zip_filename, "wb") as f:
 f.write (zip_response.content)
 print (f"Downloaded zip file: {zip_filename}")

---

# Create the directory if it doesn't exist
 os.makedirs (extract_path, exist_ok=True)

# Extract the zip file
 with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
 zip_ref.extractall (extract_path)
 print (f"Extracted zip file to: {extract_path}")

else:
 print (f"No commits found before {deadline_str}")

except:
 print(f"Error fetching commits: {response.status_code} - {response.text}")
`
Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.

`docker build -t &lt;your image name&gt; .`

Run new docker image using

`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 &lt;your image name&gt;`

Keep datagen.py and evaluate.py in same folder

`uv run evaluate.py --email &lt;any email&gt; --token_counter 1 --external_port 8000`

This then re-produces the exact environment how your application was tested.

You have to provide a token from your environment for testing.

These instructions are same for everyone. So check first before posting here.
