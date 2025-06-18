---
chunk_id: discourse_topic_171141_post_48_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/48
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 427
username: 22f3001777
post_number: 48
topic_id: 171141
---

choices'"
}
`
This issue appears across all tasks, even though they were running fine before submission. I suspect there might be a problem with APIPROXY_TOKEN. Could you please look into this?

Additionally, my solution is very similar to the one shared by the System Commands team in their email.

---

**[Discussion Image by 22f3001777]** This image shows a log output indicating issues with running a datagen.py script in a TDS project, specifically related to file formatting. The log shows the script attempting to install `uv` (if required) and run the datagen.py script from a GitHub gist, but encountering "HTTP/1.1 500 Internal Server Error" during the POST request. Subsequently, it fails to read `/data/format.md`, resulting in "HTTP/1.1 404 Not Found" errors for both A1 and A2, and a failure to format the file using `prettier@3.4.2`. The student's confusion likely revolves around the inability to access or process the `format.md` file and the unexpected internal server errors, indicating a potential problem with the project's file system or server setup.500 Internal Server Error". Subsequently, the system fails to read `/data/format.md`, reporting "HTTP/1.1 404 Not Found" and "A1 failed: Cannot read /data/format.md". The system also attempts to format `/data/format.md` with prettier, but this again results in an Internal Server Error, followed by the system failing to read `/data/format.md` again, indicating a potential file path or permission issue preventing access to the necessary data file. The highlighted errors signify the student's points of confusion." alt="Screenshot 2025-03-29 103327" data-base62-sha1="3dAmgzuVyjwlNrp6pmYrmadLbHH" width="690" height="342" data-dominant-color="F9F9F9">Screenshot 2025-03-29 1033271511×749 29 KB
