---
description: List all available workflows and their purposes
---

# Help Workflow

## Available Commands

| Command             | Description                              |
| ------------------- | ---------------------------------------- |
| `/deploy`           | Deploy to Vercel with automatic checks   |
| `/idea`             | Evaluate the viability of a project idea |
| `/status`           | Show current project status summary      |
| `/create-component` | Create a new React/Next.js component     |
| `/help`             | Show this help message                   |

## How Workflows Work

Workflows are `.md` files in `.agent/workflows/`. Each defines step-by-step instructions that the AI agent follows automatically when triggered.

## Creating New Workflows

1. Create a new `.md` file in `.agent/workflows/`
2. Add YAML frontmatter with a `description` field
3. Write clear, numbered steps
4. Reference the workflow in your `GEMINI.md` routing section
