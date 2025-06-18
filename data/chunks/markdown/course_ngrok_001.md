---
chunk_id: course_ngrok_001
source_url: https://tds.s-anand.net/#/ngrok
source_title: ngrok
content_type: course
tokens: 380
---

. Then run:

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

---

[**[Course Image: ngrok in 60 seconds]** This image introduces ngrok and its ability to create secure tunnels to expose local servers to the internet. It is designed to illustrate the simplicity and speed of setting up an ngrok tunnel, emphasizing the "60 seconds" aspect. Understanding how to use ngrok is crucial for TDS students to share their locally hosted web applications, APIs, or websites for testing and demonstration purposes. After setting up a local server (e.g., on port 8000), students can use the command `uvx ngrok http 8000` to create a secure tunnel, making their local server accessible via a public URL provided by ngrok. A key takeaway is ngrok's ability to streamline the sharing and testing of local projects, eliminating the need for complex deployment setups during the development phase.of ngrok, emphasizing its use for creating secure tunnels to expose local servers. Ngrok allows you to share your locally running applications with others over the internet by creating a public URL. To set up a basic HTTP tunnel, you would use a command like `uvx ngrok http 8000`, which forwards traffic from a public ngrok URL to your local server running on port 8000. Mastering ngrok is vital for testing webhooks, showcasing projects, and collaborating without deploying to a public server. It's a quick way to get a shareable link for your local development environment.)](https://youtu.be/dfMdLGZLXSg)
