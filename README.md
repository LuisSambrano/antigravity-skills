<div align="center">

# Antigravity Config

A configuration framework for AI-assisted development environments.  
Rules, skills, and workflows that standardize how AI coding agents operate across projects.

<p>
  <a href="./README.md">English</a> •
  <a href="./README.es.md">Español</a> •
  <a href="./README.pt.md">Português</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Stars"/></a>
</p>

</div>

---

## What This Is

This repository provides a ready-to-use `.agent/` configuration directory for AI coding assistants (Gemini, Cursor, Windsurf, etc.). It includes:

- **Rules** — Coding standards, architecture patterns, and quality gates that the AI agent enforces automatically.
- **Skills** — Domain-specific knowledge files that extend the agent's expertise (44 skills across 8 categories).
- **Workflows** — Step-by-step command scripts the agent follows for common tasks like deployment and project setup.

The goal is simple: clone once, install, and have a consistent, opinionated development environment where your AI assistant follows professional standards.

---

## Quick Start

```bash
git clone https://github.com/LuisSambrano/antigravity-config.git
cd antigravity-config && chmod +x install.sh && ./install.sh
```

The installer copies rules, skills, and workflows into your workspace's `.agent/` directory and sets up `GEMINI.md` as the global rules file.

---

## Repository Structure

```
antigravity-config/
├── GEMINI.md                  # Global rules template (customize for your needs)
├── install.sh                 # Installer script
│
├── rules/                     # Coding and architecture standards
│   ├── PROTOCOL_ZERO.md       # Core philosophy and principles
│   ├── ARCHITECTURE_STANDARDS.md
│   ├── CODE_STANDARDS.md
│   ├── QUALITY_GATES.md
│   ├── frontend/              # Frontend-specific rules
│   └── backend/               # Backend-specific rules
│
├── skills/                    # Domain knowledge (44 skills)
│   ├── 1-core/                # Coding fundamentals
│   ├── 2-ai/                  # AI agents, RAG, prompting
│   ├── 3-web/                 # Web development (Next.js, React, Tailwind)
│   ├── 4-automation/          # Testing, CI/CD, scraping
│   ├── 5-security/            # API security, pentesting
│   ├── 6-content/             # Technical writing, SEO
│   ├── 7-meta/                # Skill creation and management
│   └── 8-blockchain/          # Celo, EVM, DeFi
│
├── workflows/                 # Agent command scripts
│   ├── deploy.md              # /deploy — production deployment
│   ├── idea.md                # /idea — evaluate project ideas
│   ├── status.md              # /status — project health check
│   ├── create-component.md    # /create-component — scaffold components
│   └── help.md                # /help — list available commands
│
├── templates/                 # Project templates
├── research/                  # Decision log and key findings
└── docs/                      # Additional documentation
```

---

## Skills Reference

Skills are markdown files that give the AI agent domain-specific knowledge. Each skill contains instructions, patterns, and references the agent uses when working in that domain.

### 1-core — Fundamentals

Coding conventions, project structure standards, and TypeScript patterns that apply to all projects.

### 2-ai — AI & Agents (10 skills)

Multi-agent orchestration (LangGraph, CrewAI), RAG systems, prompt engineering, voice AI development, and agent evaluation frameworks.

### 3-web — Web Development (8 skills)

Next.js App Router patterns, React best practices, Tailwind CSS architecture, Supabase integration, Vercel deployment, and UI/UX design principles.

### 4-automation — Testing & DevOps (4 skills)

Playwright browser testing, GitHub Actions workflows, deployment procedures, and web scraping with Firecrawl.

### 5-security — Security (2 skills)

API security best practices and penetration testing checklists.

### 6-content — Content Creation

Technical writing guidelines, SEO copywriting, and documentation standards.

### 7-meta — Skill Management (3 skills)

Tools for creating new skills, planning with files, and continuous improvement (Kaizen).

### 8-blockchain — Celo & EVM (16 skills)

Full Celo development stack: MiniPay integration, fee abstraction, stablecoin addresses, Celo Composer scaffolding, viem/wagmi libraries, Hardhat/Foundry tooling, cross-chain bridging, DeFi protocol integration, ERC-8004 agent trust protocol, and x402 HTTP payment protocol.

> See [skills/INDEX.md](./skills/INDEX.md) for the complete skill-by-skill breakdown.

---

## Rules Overview

The rules define how the AI agent writes and validates code. They are loaded into the agent's context and enforced automatically.

| Rule                        | Purpose                                                           |
| --------------------------- | ----------------------------------------------------------------- |
| `PROTOCOL_ZERO.md`          | Core philosophy: quality over speed, local as source of truth     |
| `ARCHITECTURE_STANDARDS.md` | Project structure, component organization, file naming            |
| `CODE_STANDARDS.md`         | TypeScript strict mode, import order, error handling, JSDoc       |
| `QUALITY_GATES.md`          | Pre-commit checks, build verification, accessibility, performance |

---

## Customization

`GEMINI.md` is the main configuration file. It aggregates all rules into a single document that the AI agent reads. Edit it to:

- Add or remove rules
- Change naming conventions
- Adjust quality thresholds
- Add workflow routing for your own commands

Sections marked with `<!-- CUSTOMIZE -->` are designed to be modified.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding skills, workflows, or rules.

```bash
git checkout -b feature/your-feature
git commit -m 'feat(skills): add new-skill-name'
git push origin feature/your-feature
```

---

## Research & Decision Log

| Document                                      | Purpose                                |
| --------------------------------------------- | -------------------------------------- |
| [KEY_FINDINGS.md](./research/KEY_FINDINGS.md) | Core principles and research findings  |
| [prompts/](./research/prompts/)               | Rule definition prompts and iterations |
| [rules/](./rules/)                            | The resulting standards documents      |

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Maintained by [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
