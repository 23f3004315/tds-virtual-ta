---
chunk_id: discourse_topic_167172_post_1_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/1
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 357
username: Sakshi6479
post_number: 1
topic_id: 167172
---

"],
 allow_credentials=True,
 allow_methods=["GET", "POST"],
 allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
load_dotenv()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "enter your token here")

---

def sort_contacts(contacts_file_path: str, output_file_path: str):
 try:
 contacts = pd.read_json(contacts_file_path)
 contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
 return {"message": f"Contacts sorted and saved to {output_file_path}"}
 except Exception as e:
 return {"error": f"Failed to sort contacts: {str(e)}"}

a4_tool = {
 "type": "function",
 "function": {
 "name": "sort_contacts",
 "description": "This function takes data from a json file and sorts the data first by last name and then by first name, then it stores it inside the speicfied location.",
 "parameters": {
 "type": "object",
 "properties": {
 "contacts_file_path": {
 "type": "string",
 "description": "The relative path to the input JSON file containing the contacts."
 },
 "output_file_path": {
 "type": "string",
 "description": "The relative path to the output JSON file to store the sorted contacts."
 }
 },
 "required": ["contacts_file_path", "output_file_path"],
 "additionalProperties": False
 },
 "strict": True
 },
}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]
