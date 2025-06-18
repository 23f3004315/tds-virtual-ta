---
chunk_id: course_git_001
source_url: https://tds.s-anand.net/#/git
source_title: git
content_type: course
tokens: 558
---

 commits, and branches, and using command-line tools to initialize, track, and manage changes in a project. This knowledge builds a strong foundation for more advanced Git operations and is directly applicable in TDS projects where version control and collaboration are crucial. Familiarity with basic command-line operations is a prerequisite.)](https://youtu.be/HVsySz-h9r4)

---

[**[Course Image: Git and GitHub for Beginners - Crash Course (68 min)]** This material introduces Git and GitHub, covering fundamental concepts and workflows in a crash course format. Git is a distributed version control system for tracking changes in source code during software development, enabling collaboration among developers. GitHub is a web-based platform that hosts Git repositories, offering features for project management, code review, and collaboration. The course aims to equip beginners with the essential skills to use Git for local version control and GitHub for collaborative software development. Students will learn how to initialize repositories, commit changes, branch, merge, and collaborate on projects using GitHub's features.itHub Crash Course," designed to provide a quick introduction to version control using Git and collaboration through GitHub. This course aims to equip beginners with the essential skills for tracking changes in their code and collaborating effectively on software projects. Key concepts likely covered include creating repositories, committing changes, branching, merging, and pushing code to remote repositories on GitHub. By the end of the course, students should be able to manage their code effectively and contribute to collaborative projects using Git and GitHub. This knowledge is crucial for any TDS project that involves code development and teamwork.)](https://youtu.be/RGOj5yH7evk)

Essential Git Commands:

```bash
# Repository Setup
git init # Create new repo
git clone url # Clone existing repo
git remote add origin url # Connect to remote

# Basic Workflow
git status # Check status
git add . # Stage all changes
git commit -m "message" # Commit changes
git push origin main # Push to remote

# Branching
git branch # List branches
git checkout -b feature # Create/switch branch
git merge feature # Merge branch
git rebase main # Rebase on main

# History
git log --oneline # View history
git diff commit1 commit2 # Compare commits
git blame file # Show who changed what
```

Best Practices:

1. **Commit Messages**

```bash
 # Good commit message format
 type(scope): summary

Detailed description of changes.

# Examples
 feat(api): add user authentication
 fix(db): handle null values in query
 ```

2. **Branching Strategy**

- main: Production code
 - develop: Integration branch
 - feature/\*: New features
 - hotfix/\*: Emergency fixes
