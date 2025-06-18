---
chunk_id: course_ngrok_000
source_url: https://tds.s-anand.net/#/ngrok
source_title: ngrok
content_type: course
tokens: 212
---

## Tunneling: ngrok

[Ngrok](https://ngrok.com/) is a tool that creates secure tunnels to your localhost, making your local development server accessible to the internet. It's essential for testing webhooks, sharing work in progress, or debugging applications in production-like environments.

Run the command `uvx ngrok http 8000` to create a tunnel to your local server on port 8000. This generates a public URL that you can share with others.

To get started, log into `ngrok.com` and [get an authtoken from the dashboard](https://dashboard.ngrok.com/get-started/your-authtoken). Copy it. Then run:

```bash
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

Now you can forward any local port to the internet. For example:

```bash
# Start a local server on port 8000
uv run -m http.server 8000

# Start HTTP tunnel
uvx ngrok http 8000
```
