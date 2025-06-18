---
chunk_id: course_live_session_2025_01_20_003
source_url: https://tds.s-anand.net/#/live-session-2025-01-20
source_title: live-session-2025-01-20
content_type: course
tokens: 570
---

 is GitHub, and how is it used in the project?**

**A16:** GitHub is a platform for hosting Git repositories. It allows for version control, collaboration, and code sharing. In the project, you will push your code to a GitHub repository, making it accessible to others and enabling collaboration.

**Q17: What is the difference between Git and GitHub?**

---

**A17:** Git is a version control system that you install and use on your local machine, while GitHub is a web-based platform that hosts Git repositories, allowing for remote collaboration and code sharing.

**Q18: What are the alternatives to using command-line tools for Git and GitHub operations?**

**A18:** You can use a graphical interface like VS Code with Git extensions to manage your Git repositories and interact with GitHub. This can be more user-friendly than using command-line tools.

**Q19: How does the `sed` editor work for replacing text in files?**

**A19:** The `sed` editor is a stream editor that can perform text transformations on input streams. You can use it with the `s` command for substitution, specifying the pattern to match and the replacement text. The `g` flag indicates global replacement (all occurrences), and the `I` flag enables case-insensitive matching.

**Q1: How can I use the `find` command to locate files for processing with `sed`?**

**A21:** The `find` command can locate files based on various criteria, such as name, type, and location. You can use the `-exec` option to execute a command, like `sed`, on each file found. For example, `find . -type f -exec sed -i 's/IITM/IIT Madras/gI' {} \;` will find all files in the current directory and its subdirectories and replace "IITM" with "IIT Madras" (case-insensitive) in each file.

**Q22: Why am I getting an "authentication failed" error when pushing to GitHub?**

**A22:** This could be because GitHub no longer supports password authentication for Git operations. You need to use a personal access token or set up SSH keys for authentication.

**Q23: How do I create and use a personal access token for GitHub authentication?**

**A23:** You can create a personal access token in your GitHub account settings under "Developer settings." When pushing to GitHub, use your GitHub username and the generated token instead of your password.

**Q24: How do I set up SSH keys for GitHub authentication?**

**A24:** You can generate SSH keys using the `ssh-keygen` command and then add the public key to your GitHub account settings. This allows you to authenticate without using a password or personal access token.
