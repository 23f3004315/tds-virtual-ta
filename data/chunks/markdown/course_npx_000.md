---
chunk_id: course_npx_000
source_url: https://tds.s-anand.net/#/npx
source_title: npx
content_type: course
tokens: 500
---

## JavaScript tools: npx

[npx](https://docs.npmjs.com/cli/v8/commands/npx) is a command-line tool that comes with npm (Node Package Manager) and allows you to execute npm package binaries and run one-off commands without installing them globally. It's essential for modern JavaScript development and data science workflows.

For data scientists, npx is useful when:

- Running JavaScript-based data visualization tools
- Converting notebooks and documents
- Testing and formatting code
- Running development servers

Here are common npx commands:

```bash
# Run a package without installing
npx http-server . # Start a local web server
npx prettier --write . # Format code or docs
npx eslint . # Lint JavaScript
npx typescript-node script.ts # Run TypeScript directly
npx esbuild app.js # Bundle JavaScript
npx jsdoc . # Generate JavaScript docs

# Run specific versions
npx prettier@3.2 --write . # Use prettier 3.2

# Execute remote scripts (use with caution!)
npx github:user/repo # Run from GitHub
```

Watch this introduction to npx (6 min):

[**[Course Image: What you can do with npx (6 min)]** This image is the thumbnail of a video introducing the capabilities of npx. It serves as a visual entry point to learning about how npx simplifies the execution of Node.js packages. The image aims to convey the broad range of tasks that npx can handle, such as running executables without global installation. Students should watch the video to understand npx and then be able to run commands as shown in the materials. The video shows the many capabilities of using npx.n to the capabilities of `npx`, a command-line tool that comes bundled with `npm`. It answers the question: "What can you do with npx?". `npx` simplifies the process of running Node.js-based executables, especially those that are not globally installed, by automatically downloading and executing them. This allows you to use various tools and packages without the need for global installation, keeping your global environment clean and avoiding version conflicts between projects. Therefore, the video linked from this image is intended to give you an overview of how `npx` works and the different scenarios where it can be applied in your projects.)](https://youtu.be/55WaAoZV_tQ)
