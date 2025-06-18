---
chunk_id: course_git_002
source_url: https://tds.s-anand.net/#/git
source_title: git
content_type: course
tokens: 180
---

 Messages**

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

---

3. **Code Review**
 - Keep PRs small (<400 lines)
 - Use draft PRs for WIP
 - Review your own code first
 - Respond to all comments

Essential Tools

- [GitHub Desktop](https://desktop.github.com/): GUI client
- [GitLens](https://gitlens.amod.io/): VS Code extension
- [gh](https://cli.github.com/): GitHub CLI
- [pre-commit](https://pre-commit.com/): Git hooks
