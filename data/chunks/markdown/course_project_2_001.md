---
chunk_id: course_project_2_001
source_url: https://tds.s-anand.net/#/project-2
source_title: project-2
content_type: course
tokens: 431
---

01-ga3)
- [Graded Assignment 4](https://exam.sanand.workers.dev/tds-2025-01-ga4)
- [Graded Assignment 5](https://exam.sanand.workers.dev/tds-2025-01-ga5)

... and responds with the answer to enter in the assignment.

---

## Create an API

Your application exposes an API endpoint. Let's assume that it is at `https://your-app.vercel.app/api/`.

The endpoint must accept a POST request, e.g. `POST https://your-app.vercel.app/api/` with the question as well as optional file attachments as multipart/form-data.

For example, here's how anyone can make a request:

```bash
curl -X POST "https://your-app.vercel.app/api/" \
 -H "Content-Type: multipart/form-data" \
 -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?" \
 -F "file=@abcd.zip"
```

The response must be a JSON object with a single text (string) field: `answer` that can be directly entered in the assignment. For example:

```json
{
 "answer": "1234567890"
}
```

## Deploy your application

Deploy your application to a public URL that can be accessed by anyone. You may use any platform, including Vercel.

(If you use ngrok, ensure that it is running continuously until you get your results.)

## Share your code

- [Create a new _public_ GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Add an MIT `LICENSE` file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)
- Commit and push your code

## Submit your URL

Submit your GitHub repository URL and your API endpoint URL in this Google Form: .
