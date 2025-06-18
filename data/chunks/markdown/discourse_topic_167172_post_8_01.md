---
chunk_id: discourse_topic_167172_post_8_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167172/8
source_title: Regarding project1 for file not detecting after sending post request
content_type: discourse
tokens: 317
username: Sakshi6479
post_number: 8
topic_id: 167172
---

XY_TOKEN = os.getenv("AIPROXY_TOKEN")
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
def cakebake(no_people: int, flavor: str):
 return {"message": f"Making a {flavor} cake for {no_people} people"}

---

bakecake = {
 "type": "function",
 "function": {
 "name": "cakebake",
 "description": "Make a cake for all iitm students contain its emailids",
 "parameters": {
 "type": "object",
 "properties": {
 "no_people": {
 "type": "integer",
 "description": "Number of people"
 },
 "flavor": {
 "type": "string",
 "description": "Flavor of the cake"
 }
 },
 "required": ["no_people", "flavor"],
 "additionalProperties": False
 },
 "strict": True
 }
}

def sort_contacts(contacts_file_path: str, output_file_path: str):
 try:
 contacts = pd.read_json(contacts_file_path)
 contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
 return {"message": f"Contacts sorted and saved to {output_file_path}"}
 except Exception as e:
 return {"error": f"Failed to sort contacts: {str(e)}"}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]
