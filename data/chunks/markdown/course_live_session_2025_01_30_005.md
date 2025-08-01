---
chunk_id: course_live_session_2025_01_30_005
source_url: https://tds.s-anand.net/#/live-session-2025-01-30
source_title: live-session-2025-01-30
content_type: course
tokens: 547
---

: Can we use `httpie` instead of `requests`?**

**A28:** Yes, you can change it to `httpx`. `httpie` is a command-line tool, not a Python module. I'm not sure about `httpie`.

**Q29: Can we get the names of the words and their embeddings separately in the JSON?**

---

**A29:** No, it won't get you the name of the embedding. It will store embeddings for each word. You can pass three different values. You can calculate three embeddings. Then you can compute the cosine similarity between them. The first index would get the embedding for bicycle, the second for cycle, and the third for `biycle`.

**Q30: Can we get a 3x1,1056 dimensional array?**

**A30:** You won't get it directly, but you can store it in whatever format you want. You can store it in an array. I don't know how to convert JSON to an array.

**Q31: One more thing about embeddings. Can we go back to the writer pad?**

**A31:** Sure. Let's say I'm using a certain model for creating embeddings. Let's say that model contains a billion words. It will check the similarity of a word (like "kitten") with all those billion words. It will check the rate of similarity between this particular word and that word. These models vary in the number of words they carry. A small model has about a billion; a medium-sized model has around 50 billion; a large model has several more. These numbers might be a bit wrong, but that's the distinction. The larger the model, the better the embeddings. Here, we have 1,056. That means it's checking the similarity of a word with 1,056 words in its database. That's how embeddings work. For creating embeddings, there's a library in NLP, actually ML, with a module called `word2vec`. It's deployed on Hugging Face.

**Q32: Is Hugging Face part of the TDS course?**

**A32:** I think it's been removed. It would be too heavy for TDS.

**Q33: Can we create LLM applications on Google Colab?**

**A33:** Not exactly, but we can make API calls and get embeddings for words. For example, let's say we have the word "Anand".

**Q34: Sorry for interrupting, but is Hugging Face part of the TDS course?**

**A34:** I think it's been removed, probably because it's too heavy for the course.
