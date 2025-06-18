---
chunk_id: discourse_topic_164277_post_223_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/223
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 333
username: 22f3002771
post_number: 223
topic_id: 164277
---

 querying GPT: {e}")
 raise HTTPException(status_code=400, detail=str(e))

except Exception as e:
 print(f"INSIDE EMBED_LIST IN A9. General Error while querying gpt: {str(e)}")
 raise HTTPException(status_code=500, detail=str(e))

---

def most_similar(embeddings):
 # Extract the phrases and their corresponding embeddings
 phrases = list(embeddings.keys())
 emb_values = list(embeddings.values())

# Initialize variables to track the maximum similarity
 max_similarity = -1 # Start with the smallest possible similarity value
 most_similar_pair = None

# Compute cosine similarity between each pair of embeddings
 for i in range(len(emb_values)):
 for j in range(i + 1, len(emb_values)): # Avoid repeating pairs
 similarity = get_similarity_from_embeddings(emb_values[i], emb_values[j])
 if similarity &gt; max_similarity:
 max_similarity = similarity
 most_similar_pair = (phrases[i], phrases[j])

return most_similar_pair

# async def get_similar_comments(input_file_path: str, output_file_path: str):
async def get_similar_comments(input_file_path: str, output_file_path: str):
 print(f"Reading the input file: {input_file_path}")
 with open(input_file_path, "r") as file:
 comments = file.readlines()

print(f"Embedding the comments")
 # embeddings = await embed_list(comments)
 embeddings = await embed_list(comments)
 embed_dict = dict(zip(comments, embeddings))
 most_similar_pair = most_similar(embed_dict)
 print(f"Most similar comments: {most_similar_pair}")
