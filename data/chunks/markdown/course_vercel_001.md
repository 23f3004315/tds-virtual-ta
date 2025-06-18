---
chunk_id: course_vercel_001
source_url: https://tds.s-anand.net/#/vercel
source_title: vercel
content_type: course
tokens: 570
---

start](https://vercel.com/docs/functions/runtimes/python). [Sign-up with Vercel](https://vercel.com/signup). Create an empty `git` repo with this `api/index.py` file.

To deploy a FastAPI app, add a `requirements.txt` file with `fastapi` as a dependency.

```text
fastapi
```

---

Add your FastAPI code to a file, e.g. `main.py`.

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
 return {"message": "Hello, World!"}
```

Add a `vercel.json` file to the root of your repository.

```json
{
 "builds": [{ "src": "main.py", "use": "@vercel/python" }],
 "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}
```

On the command line, run:

- `npx vercel` to deploy a test version
- `npx vercel --prod` to deploy to production

**Environment Variables**. Use `npx vercel env add` to add environment variables. In your code, use `os.environ.get('SECRET_KEY')` to access them.

### Videos

[**[Course Image: Vercel Product Walkthrough]** This image provides a glimpse into the Vercel platform's dashboard, showcasing key features and UI elements. Specifically, it highlights the "Projects" section, which displays a list of your deployed Vercel projects like "vercel-times." You can see information such as the project name, the last update with its commit message (e.g., "update img src" from "change-logo"), and the time since the last deployment. The dashboard also provides a search bar and navigation to other sections such as "Integrations", "Activity", "Domains", "Usage", and "Settings", allowing you to manage your Vercel account and projects effectively. Understanding this interface is crucial for deploying and managing web applications with Vercel.iew of the Vercel platform interface, focusing on project management. The Vercel dashboard displays key navigation elements such as "Projects," "Integrations," "Activity," "Domains," "Usage," and "Settings," allowing users to configure and monitor their deployments. It also includes a search bar for easy project discovery and the ability to switch between different organizations (like "Acme"). The display highlights recent activity within a specific project, such as updates to image sources, providing a quick view of the project's development history and deployment status. Learning to navigate this dashboard is crucial for effectively managing and deploying web applications using Vercel.)](https://youtu.be/sPmat30SE4k)
