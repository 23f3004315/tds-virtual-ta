---
chunk_id: discourse_topic_163247_post_89_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/163247/89
source_title: GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 692
username: 22f3002723
post_number: 89
topic_id: 163247
---

`import requests
import json
from google.colab import userdata
def generate_readme_content(proxy_url,auth_token):
 # Prepare the payload
 prompt = f""" 
 SNyFiNTb, BUkDfo0tR, x3x, 6NE8Rq833, Re7, Vth9bYJ0pK, pnI, JAXpFb, BRPE, o, 5xVQe, iY8yVT, 69w, LjLCzs, MJ1g, wBR, 0H, 6bK, AMw, Vrxiux, dqZysH, yD82hcr, FZrwV8Zjq, Xb2, quLpdQqxd1, lqSLbI, HerfhK2, rNPU, 9K1C, 0ywhX2s4O9, mjZ, sR9gCC, 2WVSfwWEae, c, DtWnfOncFj, qjK8P7xh, 0xraHn7RMa, OCmQIi3tbU, S2K, F, q5mO, yZt, X, zd, se0ss3k, uU, yCRCi, S3bMfb, qZ4dh, M7, uhxgDvG3, 696g, 9k, l5U, bH, LVXw1fdWFi, 0kU68gGP, WuyD, V, kVKQ1Y8, kLjMDoEmIN, EYHs7qsabQ, sWrC8vN7n, oAJZP, YLd, mi6Jmxgf, cb9UDdap, kzuot, R0eA2V, mr7SctL49, Td5, in, hxvi, MDg, AAK, uLBF889bO5, Z7z, AO0c, nbc, bE6Rsdw5b, 0, pBjOAuPN8A, 9C3, K, 8, yZyCBPz 
 """
 payload = {
 "model": "gpt-4o-mini",
 "messages": [
 {"role": "system", "content": "You are a helpful assistant to count the number of english words in a message. Find the number of input tokens used for a message lile below. Try excluding tokens used for understanding this prompt"},
 {"role": "user", "content": prompt}
 ],
 "max_tokens": 500,
 "temperature": 0.7
 }
 
 # Send a POST request to the proxy server
 response = requests.post(
 proxy_url,
 headers={"Content-Type": "application/json",
 
 "Authorization": f"Bearer {auth_token}"},
 data=json.dumps(payload)
 )
 response_data = response.json()
 return response_data
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
tokenjson=generate_readme_content(proxy_url,auth_token)
print(tokenjson)
`
