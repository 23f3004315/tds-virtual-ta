---
chunk_id: course_live_session_2025_01_29_007
source_url: https://tds.s-anand.net/#/live-session-2025-01-29
source_title: live-session-2025-01-29
content_type: course
tokens: 432
---

ed it on Discourse. If not, we can always ask him to provide it.

**Q24: I've taken one more course, something on business BA or something like that. There is no GA at all for this. There is a GA, but you don't submit here. These two courses are somewhat different.**

**A24:** Right, right.

---

**Q25: When I joined (late), an ngrok error was being shown by someone. I'm also getting a very similar error. I couldn't follow the discussion at all. I joined towards the end. Shall I share my screen?**

**A25:** Just before you share your screen, was it giving you a Cloudflare error? (The student describes the error.) You can share your screen. I think your problem is slightly different. (The instructor then guides the student through troubleshooting steps, including checking the ngrok URL and restarting the Lama server. The issue is that ngrok is running outside of the Ubuntu environment, and the Lama server is running inside the Ubuntu environment. The instructor suggests installing ngrok in the Windows machine and then creating a tunnel from there. The student tries this, but it's still giving an error. The instructor then suggests using the directly executable file for ngrok.)

**Q26: I tried all this, same issue. I'm getting an error. I think I've tried all this, same issue.**

**A26:** The account is limited to one simultaneous session. You've got another session running somewhere. I think that is inside VS WSL. You'll have to stop that. You'll have to check for that. The output that your code is generating is wrong. It's generating null, null, which is wrong. Just try to check for... can you go back to the question once? It is sending some URL-encoded parameter. There might be a mistake while reading those parameters. Just changing that code will help. There's a problem with my code where it's fetching null for all the data, which it should not. You can either ask on Discourse or try to fix it yourself.
