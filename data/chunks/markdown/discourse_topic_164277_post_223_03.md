---
chunk_id: discourse_topic_164277_post_223_03
source_url: https://discourse.onlinedegree.iitm.ac.in/t/164277/223
source_title: Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 166
username: 22f3002771
post_number: 223
topic_id: 164277
---

()

print(f"Embedding the comments")
 # embeddings = await embed_list(comments)
 embeddings = await embed_list(comments)
 embed_dict = dict(zip(comments, embeddings))
 most_similar_pair = most_similar(embed_dict)
 print(f"Most similar comments: {most_similar_pair}")

---

with open(output_file_path, "w") as file:
 for comment in most_similar_pair:
 file.write(f"{comment.strip()}\n")
 # file.write(f"Most similar comments: {most_similar_pair}")

if __name__ == "__main__":
 # import asyncio

input_file_path = "/data/comments.txt"
 output_file_path = "/data/similar_comments.txt"
 # asyncio.run(get_similar_comments(input_file_path, output_file_path))
 get_similar_comments(input_file_path, output_file_path)
`
