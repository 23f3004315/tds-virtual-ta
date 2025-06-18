---
chunk_id: course_bash_000
source_url: https://tds.s-anand.net/#/bash
source_title: bash
content_type: course
tokens: 484
---

## Terminal: Bash

UNIX shells are the de facto standard in the data science world and [Bash](https://www.gnu.org/software/bash/) is the most popular.
This is available by default on Mac and Linux.

On Windows, install [Git Bash](https://git-scm.com/downloads) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to get a UNIX shell.

Watch this video to understand the basics of Bash and UNIX shell commands (75 min).

[**[Course Image: Beginner's Guide to the Bash Terminal (75 min)]** This video serves as a beginner's guide to the Bash terminal, teaching the fundamentals of interacting with the UNIX shell using Bash commands. The learning objective is to gain familiarity with basic command-line operations, understand the shell environment, and execute simple scripts. Students will learn about navigating the file system, manipulating files and directories, and running programs from the command line. Mastering these basics is crucial for more advanced shell scripting and system administration tasks in TDS projects. This video will help you avoid common pitfalls like incorrect syntax or misunderstanding file paths.s Guide to the Bash Terminal," aimed at providing foundational knowledge of Bash and UNIX shell commands. The guide is likely to cover basic navigation, file manipulation, and command execution within the Bash environment. Mastering these concepts is crucial for interacting with systems via the command line, a common task in TDS projects involving data science and software development. By working through this guide, students should be able to confidently execute simple tasks and understand the structure of Bash commands. This introductory material prepares students for more advanced topics in scripting and system administration.)](https://youtu.be/oxuRxtrO2Ag)

Essential Commands:

```bash
# File Operations
ls -la # List all files with details
cd path/to/dir # Change directory
pwd # Print working directory
cp source dest # Copy files
mv source dest # Move/rename files
rm -rf dir # Remove directory recursively

# Text Processing
grep "pattern" file # Search for pattern
sed 's/old/new/' f # Replace text
awk '{print $1}' f # Process text by columns
cat file | wc -l # Count lines

# Process Management
ps aux # List processes
kill -9 PID # Force kill process
top # Monitor processes
htop # Interactive process viewer
