<div align="center">

# 🌌 GOOGLE ANTIGRAVITY
### Sistema Operativo de Inteligencia Colectiva

![Status](https://img.shields.io/badge/ESTADO-OPERATIVO-success?style=for-the-badge&logo=statuspage)
![Version](https://img.shields.io/badge/VERSION-3.0.0--PREMIUM-gold?style=for-the-badge&logo=semver)
![Access](https://img.shields.io/badge/NIVEL-ROOT-red?style=for-the-badge&logo=riotgames)

<p align="center">
  <em>Arquitectura Modular • Protocolo Zero • Autonomía Agéntica</em>
</p>

[🏰 Dashboard](#-panel-de-control) • [⚖️ Gobernanza](docs/architecture/REPOSITORY_GOVERNANCE.md) • [🧱 Estructura](#-convenciones-del-repositorio)

</div>

---

## 🧭 Panel de Control

Bienvenido al mapa central de **Antigravity V3 Premium**. El sistema está indexado semánticamente por niveles de profundidad operativa.

### 🧬 Nivel 0: El Núcleo (Meta-Skills)
*Capacidades reflexivas que gobiernan, construyen y optimizan el sistema.*

| Módulo | Descripción | Tecnología | Acceso |
| :--- | :--- | :---: | :---: |
| **[CLAUDE CODE GUIDE](skills/meta-skills/claude-code-guide/SKILL.md)** | Master guide for using Claude Code effectively | `N/A` | 🔴 |
| **[BEHAVIORAL-MODES](skills/meta-skills/behavioral-modes/SKILL.md)** | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate) | `N/A` | 🔴 |
| **[CONCISE-PLANNING](skills/meta-skills/concise-planning/SKILL.md)** | Use when a user asks for a plan for a coding task, to generate a clear, actionable... | `N/A` | 🔴 |
| **[D3-VIZ](skills/meta-skills/claude-d3js-skill/SKILL.md)** | Creating interactive data visualisations using d3 | `N/A` | 🔴 |
| **[DESIGN-ORCHESTRATION](skills/meta-skills/design-orchestration/SKILL.md)** | > | `N/A` | 🔴 |
| **[EXECUTING-PLANS](skills/meta-skills/executing-plans/SKILL.md)** | Use when you have a written implementation plan to execute in a separate session w... | `N/A` | 🔴 |
| **[FINISHING-A-DEVELOPMENT-BRANCH](skills/meta-skills/finishing-a-development-branch/SKILL.md)** | Use when implementation is complete, all tests pass, and you need to decide how to... | `N/A` | 🔴 |
| **[GIT-PUSHING](skills/meta-skills/git-pushing/SKILL.md)** | Stage, commit, and push git changes with conventional commit messages | `N/A` | 🔴 |
| **[KAIZEN](skills/meta-skills/kaizen/SKILL.md)** | Guide for continuous improvement, error proofing, and standardization | `N/A` | 🔴 |
| **[LAST30DAYS](skills/meta-skills/last30days/SKILL.md)** | Research a topic from the last 30 days on Reddit + X + Web, become an expert, and ... | `N/A` | 🔴 |
| **[LOKI-MODE](skills/meta-skills/loki-mode/SKILL.md)** | Multi-agent autonomous startup system for Claude Code | `N/A` | 🔴 |
| **[PLANNING-WITH-FILES](skills/meta-skills/planning-with-files/SKILL.md)** | Implements Manus-style file-based planning for complex tasks | `N/A` | 🔴 |
| **[SKILL-CREATOR](skills/meta-skills/skill-creator/SKILL.md)** | Guide for creating effective skills | `N/A` | 🔴 |
| **[SKILL-DEVELOPER](skills/meta-skills/skill-developer/SKILL.md)** | Create and manage Claude Code skills following Anthropic best practices | `N/A` | 🔴 |
| **[USING-SUPERPOWERS](skills/meta-skills/using-superpowers/SKILL.md)** | Use when starting any conversation - establishes how to find and use skills, requi... | `N/A` | 🔴 |

### 🧠 Nivel 1: Inteligencia Artificial
*Orquestación de LLMs, arquitecturas de agentes y memoria persistente.*

| Habilidad AI | Función Principal | Stack |
| :--- | :--- | :---: |
| **[agent-evaluation](skills/ai-agents/agent-evaluation/SKILL.md)** | Testing and benchmarking LLM agents including behavioral testing, capability asses... | `TS` |
| **[agent-manager-skill](skills/ai-agents/agent-manager-skill/SKILL.md)** | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) wit... | `TS` |
| **[agent-memory-mcp](skills/ai-agents/agent-memory-mcp/SKILL.md)** | A hybrid memory system that provides persistent, searchable knowledge management f... | `TS` |
| **[agent-memory-systems](skills/ai-agents/agent-memory-systems/SKILL.md)** | Memory is the cornerstone of intelligent agents | `TS` |
| **[agent-tool-builder](skills/ai-agents/agent-tool-builder/SKILL.md)** | Tools are how AI agents interact with the world | `TS` |
| **[ai-agents-architect](skills/ai-agents/ai-agents-architect/SKILL.md)** | Expert in designing and building autonomous AI agents | `TS` |
| **[autonomous-agent-patterns](skills/ai-agents/autonomous-agent-patterns/SKILL.md)** | Design patterns for building autonomous coding agents | `TS` |
| **[autonomous-agents](skills/ai-agents/autonomous-agents/SKILL.md)** | Autonomous agents are AI systems that can independently decompose goals, plan acti... | `TS` |
| **[bullmq-specialist](skills/automation-tools/bullmq-specialist/SKILL.md)** | BullMQ expert for Redis-backed job queues, background processing, and reliable asy... | `N/A` |
| **[computer-use-agents](skills/ai-agents/computer-use-agents/SKILL.md)** | Build AI agents that interact with computers like humans do - viewing screens, mov... | `TS` |
| **[context-window-management](skills/ai-agents/context-window-management/SKILL.md)** | Strategies for managing LLM context windows including summarization, trimming, rou... | `TS` |
| **[conversation-memory](skills/ai-agents/conversation-memory/SKILL.md)** | Persistent memory systems for LLM conversations including short-term, long-term, a... | `TS` |
| **[crewai](skills/ai-agents/crewai/SKILL.md)** | Expert in CrewAI - the leading role-based multi-agent framework used by 60% of For... | `TS` |
| **[dispatching-parallel-agents](skills/ai-agents/dispatching-parallel-agents/SKILL.md)** | Use when facing 2+ independent tasks that can be worked on without shared state or... | `TS` |
| **[langfuse](skills/ai-agents/langfuse/SKILL.md)** | Expert in Langfuse - the open-source LLM observability platform | `TS` |
| **[langgraph](skills/ai-agents/langgraph/SKILL.md)** | Expert in LangGraph - the production-grade framework for building stateful, multi-... | `TS` |
| **[llm-app-patterns](skills/ai-agents/llm-app-patterns/SKILL.md)** | Production-ready patterns for building LLM applications | `TS` |
| **[multi-agent-brainstorming](skills/ai-agents/multi-agent-brainstorming/SKILL.md)** | > | `TS` |
| **[notebooklm](skills/ai-agents/notebooklm/SKILL.md)** | Use this skill to query your Google NotebookLM notebooks directly from Claude Code... | `TS` |
| **[parallel-agents](skills/ai-agents/parallel-agents/SKILL.md)** | Multi-agent orchestration patterns | `TS` |
| **[prompt-caching](skills/ai-agents/prompt-caching/SKILL.md)** | Caching strategies for LLM prompts including Anthropic prompt caching, response ca... | `TS` |
| **[prompt-engineer](skills/ai-agents/prompt-engineer/SKILL.md)** | Expert in designing effective prompts for LLM-powered applications | `TS` |
| **[prompt-engineering](skills/ai-agents/prompt-engineering/SKILL.md)** | Expert guide on prompt engineering patterns, best practices, and optimization tech... | `TS` |
| **[prompt-library](skills/ai-agents/prompt-library/SKILL.md)** | Curated collection of high-quality prompts for various use cases | `TS` |
| **[rag-engineer](skills/ai-agents/rag-engineer/SKILL.md)** | Expert in building Retrieval-Augmented Generation systems | `TS` |
| **[rag-implementation](skills/ai-agents/rag-implementation/SKILL.md)** | Retrieval-Augmented Generation patterns including chunking, embeddings, vector sto... | `TS` |
| **[research-engineer](skills/ai-agents/research-engineer/SKILL.md)** | An uncompromising Academic Research Engineer | `TS` |
| **[subagent-driven-development](skills/ai-agents/subagent-driven-development/SKILL.md)** | Use when executing implementation plans with independent tasks in the current session | `TS` |
| **[voice-agents](skills/ai-agents/voice-agents/SKILL.md)** | Voice agents represent the frontier of AI interaction - humans speaking naturally ... | `TS` |
| **[voice-ai-development](skills/ai-agents/voice-ai-development/SKILL.md)** | Expert in building voice AI applications - from real-time voice agents to voice-en... | `TS` |
| **[voice-ai-engine-development](skills/ai-agents/voice-ai-engine-development/SKILL.md)** | Build real-time conversational AI voice engines using async worker pipelines, stre... | `TS` |

### 💻 Nivel 2: Ingeniería & Web
*Sistemas de diseño inteligente, frameworks modernos y despliegue.*

| Dominio | Skill Destacada | Enfoque |
| :--- | :--- | :--- |
| **Game Development** | **[2d-games](skills/web-development/game-development/2d-games/SKILL.md)** | 2D game development principles |
| **Game Development** | **[3d-games](skills/web-development/game-development/3d-games/SKILL.md)** | 3D game development principles |
| **Web Development** | **[3d-web-experience](skills/web-development/3d-web-experience/SKILL.md)** | Expert in building 3D experiences for the web - Three |
| **Web Development** | **[algolia-search](skills/web-development/algolia-search/SKILL.md)** | Expert patterns for Algolia search implementation, indexing strategies, React Inst... |
| **Web Development** | **[api-patterns](skills/web-development/api-patterns/SKILL.md)** | API design principles and decision-making |
| **Web Development** | **[app-builder](skills/web-development/app-builder/SKILL.md)** | Main application building orchestrator |
| **Web Development** | **[avalonia-layout-zafiro](skills/web-development/avalonia-layout-zafiro/SKILL.md)** | Guidelines for modern Avalonia UI layout using Zafiro |
| **Web Development** | **[avalonia-viewmodels-zafiro](skills/web-development/avalonia-viewmodels-zafiro/SKILL.md)** | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and React... |
| **Web Development** | **[avalonia-zafiro-development](skills/web-development/avalonia-zafiro-development/SKILL.md)** | Mandatory skills, conventions, and behavioral rules for Avalonia UI development us... |
| **Web Development** | **[aws-serverless](skills/web-development/aws-serverless/SKILL.md)** | Specialized skill for building production-ready serverless applications on AWS |
| **Web Development** | **[azure-functions](skills/web-development/azure-functions/SKILL.md)** | Expert patterns for Azure Functions development including isolated worker model, D... |
| **Web Development** | **[backend-dev-guidelines](skills/web-development/backend-dev-guidelines/SKILL.md)** | Opinionated backend development standards for Node |
| **Coding Standards** | **[backend-patterns](skills/coding-standards/cc-skill-backend-patterns/SKILL.md)** | Backend architecture patterns, API design, database optimization, and server-side ... |
| **Web Development** | **[bun-development](skills/web-development/bun-development/SKILL.md)** | Modern JavaScript/TypeScript development with Bun runtime |
| **Web Development** | **[canvas-design](skills/web-development/canvas-design/SKILL.md)** | Create beautiful visual art in |
| **Web Development** | **[clerk-auth](skills/web-development/clerk-auth/SKILL.md)** | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks... |
| **Web Development** | **[core-components](skills/web-development/core-components/SKILL.md)** | Core component library and design system patterns |
| **Web Development** | **[database-design](skills/web-development/database-design/SKILL.md)** | Database design principles and decision-making |
| **Web Development** | **[deployment-procedures](skills/web-development/deployment-procedures/SKILL.md)** | Production deployment principles and decision-making |
| **Web Development** | **[discord-bot-architect](skills/web-development/discord-bot-architect/SKILL.md)** | Specialized skill for building production-ready Discord bots |
| **Web Development** | **[docker-expert](skills/web-development/docker-expert/SKILL.md)** | Docker containerization expert with deep knowledge of multi-stage builds, image op... |
| **Web Development** | **[firebase](skills/web-development/firebase/SKILL.md)** | Firebase gives you a complete backend in minutes - auth, database, storage, functi... |
| **Web Development** | **[frontend-design](skills/web-development/frontend-design/SKILL.md)** | Create distinctive, production-grade frontend interfaces with intentional aestheti... |
| **Web Development** | **[frontend-dev-guidelines](skills/web-development/frontend-dev-guidelines/SKILL.md)** | Opinionated frontend development standards for modern React + TypeScript applications |
| **Coding Standards** | **[frontend-patterns](skills/coding-standards/cc-skill-frontend-patterns/SKILL.md)** | Frontend development patterns for React, Next |
| **Game Development** | **[game-art](skills/web-development/game-development/game-art/SKILL.md)** | Game art principles |
| **Game Development** | **[game-audio](skills/web-development/game-development/game-audio/SKILL.md)** | Game audio principles |
| **Game Development** | **[game-design](skills/web-development/game-development/game-design/SKILL.md)** | Game design principles |
| **Web Development** | **[game-development](skills/web-development/game-development/SKILL.md)** | Game development orchestrator |
| **Web Development** | **[gcp-cloud-run](skills/web-development/gcp-cloud-run/SKILL.md)** | Specialized skill for building production-ready serverless applications on GCP |
| **Web Development** | **[graphql](skills/web-development/graphql/SKILL.md)** | GraphQL gives clients exactly the data they need - no more, no less |
| **Web Development** | **[hubspot-integration](skills/web-development/hubspot-integration/SKILL.md)** | Expert patterns for HubSpot CRM integration including OAuth authentication, CRM ob... |
| **Web Development** | **[i18n-localization](skills/web-development/i18n-localization/SKILL.md)** | Internationalization and localization patterns |
| **Web Development** | **[interactive-portfolio](skills/web-development/interactive-portfolio/SKILL.md)** | Expert in building portfolios that actually land jobs and clients - not just showi... |
| **Web Development** | **[javascript-mastery](skills/web-development/javascript-mastery/SKILL.md)** | Comprehensive JavaScript reference covering 33+ essential concepts every developer... |
| **Web Development** | **[mcp-builder](skills/web-development/mcp-builder/SKILL.md)** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable L... |
| **Web Development** | **[mobile-design](skills/web-development/mobile-design/SKILL.md)** | Mobile-first design and engineering doctrine for iOS and Android apps |
| **Game Development** | **[mobile-games](skills/web-development/game-development/mobile-games/SKILL.md)** | Mobile game development principles |
| **Web Development** | **[moodle-external-api-development](skills/web-development/moodle-external-api-development/SKILL.md)** | Create custom external web service APIs for Moodle LMS |
| **Game Development** | **[multiplayer](skills/web-development/game-development/multiplayer/SKILL.md)** | Multiplayer game development principles |
| **Web Development** | **[neon-postgres](skills/web-development/neon-postgres/SKILL.md)** | Expert patterns for Neon serverless Postgres, branching, connection pooling, and P... |
| **Web Development** | **[nestjs-expert](skills/web-development/nestjs-expert/SKILL.md)** | Nest |
| **Web Development** | **[nextjs-best-practices](skills/web-development/nextjs-best-practices/SKILL.md)** | Next |
| **Web Development** | **[nextjs-supabase-auth](skills/web-development/nextjs-supabase-auth/SKILL.md)** | Expert integration of Supabase Auth with Next |
| **Web Development** | **[nodejs-best-practices](skills/web-development/nodejs-best-practices/SKILL.md)** | Node |
| **Web Development** | **[nosql-expert](skills/web-development/nosql-expert/SKILL.md)** | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB) |
| **Game Development** | **[pc-games](skills/web-development/game-development/pc-games/SKILL.md)** | PC and console game development principles |
| **Web Development** | **[performance-profiling](skills/web-development/performance-profiling/SKILL.md)** | Performance profiling principles |
| **Web Development** | **[plaid-fintech](skills/web-development/plaid-fintech/SKILL.md)** | Expert patterns for Plaid API integration including Link token flows, transactions... |
| **Web Development** | **[prisma-expert](skills/web-development/prisma-expert/SKILL.md)** | Prisma ORM expert for schema design, migrations, query optimization, relations mod... |
| **Web Development** | **[python-patterns](skills/web-development/python-patterns/SKILL.md)** | Python development principles and decision-making |
| **Web Development** | **[react-patterns](skills/web-development/react-patterns/SKILL.md)** | Modern React patterns and principles |
| **Web Development** | **[react-ui-patterns](skills/web-development/react-ui-patterns/SKILL.md)** | Modern React UI patterns for loading states, error handling, and data fetching |
| **Web Development** | **[remotion-best-practices](skills/web-development/remotion-best-practices/SKILL.md)** | Best practices for Remotion - Video creation in React |
| **Web Development** | **[salesforce-development](skills/web-development/salesforce-development/SKILL.md)** | Expert patterns for Salesforce platform development including Lightning Web Compon... |
| **Web Development** | **[senior-architect](skills/web-development/senior-architect/SKILL.md)** | Comprehensive software architecture skill for designing scalable, maintainable sys... |
| **Web Development** | **[senior-fullstack](skills/web-development/senior-fullstack/SKILL.md)** | Comprehensive fullstack development skill for building complete web applications w... |
| **Web Development** | **[shopify-apps](skills/web-development/shopify-apps/SKILL.md)** | Expert patterns for Shopify app development including Remix/React Router apps, emb... |
| **Web Development** | **[shopify-development](skills/web-development/shopify-development/SKILL.md)** | | |
| **Web Development** | **[slack-bot-builder](skills/web-development/slack-bot-builder/SKILL.md)** | Build Slack apps using the Bolt framework across Python, JavaScript, and Java |
| **Web Development** | **[software-architecture](skills/web-development/software-architecture/SKILL.md)** | Guide for quality focused software architecture |
| **Web Development** | **[stripe-integration](skills/web-development/stripe-integration/SKILL.md)** | Get paid from day one |
| **Web Development** | **[supabase-postgres-best-practices](skills/web-development/postgres-best-practices/SKILL.md)** | Postgres performance optimization and best practices from Supabase |
| **Web Development** | **[tailwind-patterns](skills/web-development/tailwind-patterns/SKILL.md)** | Tailwind CSS v4 principles |
| **Web Development** | **[telegram-bot-builder](skills/web-development/telegram-bot-builder/SKILL.md)** | Expert in building Telegram bots that solve real problems - from simple automation... |
| **Web Development** | **[telegram-mini-app](skills/web-development/telegram-mini-app/SKILL.md)** | Expert in building Telegram Mini Apps (TWA) - web apps that run inside Telegram wi... |
| **App Builder** | **[templates](skills/web-development/app-builder/templates/SKILL.md)** | Project scaffolding templates for new applications |
| **Web Development** | **[theme-factory](skills/web-development/theme-factory/SKILL.md)** | Toolkit for styling artifacts with a theme |
| **Web Development** | **[trigger-dev](skills/web-development/trigger-dev/SKILL.md)** | Trigger |
| **Web Development** | **[typescript-expert](skills/web-development/typescript-expert/SKILL.md)** | >- |
| **Web Development** | **[ui-ux-pro-max](skills/web-development/ui-ux-pro-max/SKILL.md)** | UI/UX design intelligence |
| **Web Development** | **[upstash-qstash](skills/web-development/upstash-qstash/SKILL.md)** | Upstash QStash expert for serverless message queues, scheduled jobs, and reliable ... |
| **Web Development** | **[vercel-deployment](skills/web-development/vercel-deployment/SKILL.md)** | Expert knowledge for deploying to Vercel with Next |
| **Web Development** | **[vercel-react-best-practices](skills/web-development/react-best-practices/SKILL.md)** | React and Next |
| **Game Development** | **[vr-ar](skills/web-development/game-development/vr-ar/SKILL.md)** | VR/AR development principles |
| **Web Development** | **[web-artifacts-builder](skills/web-development/web-artifacts-builder/SKILL.md)** | Suite of tools for creating elaborate, multi-component claude |
| **Web Development** | **[web-design-guidelines](skills/web-development/web-design-guidelines/SKILL.md)** | Review UI code for Web Interface Guidelines compliance |
| **Game Development** | **[web-games](skills/web-development/game-development/web-games/SKILL.md)** | Web browser game development principles |
| **Web Development** | **[web-performance-optimization](skills/web-development/web-performance-optimization/SKILL.md)** | Optimize website and web application performance including loading speed, Core Web... |
| **Web Development** | **[webapp-testing](skills/web-development/webapp-testing/SKILL.md)** | Toolkit for interacting with and testing local web applications using Playwright |

### 🛡️ Nivel 3: Seguridad & Resiliencia
*Protocolos de seguridad ofensiva, pentesting y auditoría.*

| Vector | Objetivo | Criticidad |
| :--- | :--- | :---: |
| **Security** | **[API Fuzzing for Bug Bounty](skills/security/api-fuzzing-bug-bounty/SKILL.md)** | 🔥 |
| **Security** | **[AWS Penetration Testing](skills/security/aws-penetration-testing/SKILL.md)** | 🔥 |
| **Security** | **[Active Directory Attacks](skills/security/active-directory-attacks/SKILL.md)** | 🔥 |
| **Security** | **[Broken Authentication Testing](skills/security/broken-authentication/SKILL.md)** | 🔥 |
| **Security** | **[Burp Suite Web Application Testing](skills/security/burp-suite-testing/SKILL.md)** | 🔥 |
| **Security** | **[Cloud Penetration Testing](skills/security/cloud-penetration-testing/SKILL.md)** | 🔥 |
| **Security** | **[Cross-Site Scripting and HTML Injection Testing](skills/security/xss-html-injection/SKILL.md)** | 🔥 |
| **Security** | **[Ethical Hacking Methodology](skills/security/ethical-hacking-methodology/SKILL.md)** | 🔥 |
| **Security** | **[File Path Traversal Testing](skills/security/file-path-traversal/SKILL.md)** | 🔥 |
| **Security** | **[HTML Injection Testing](skills/security/html-injection-testing/SKILL.md)** | 🔥 |
| **Security** | **[IDOR Vulnerability Testing](skills/security/idor-testing/SKILL.md)** | 🔥 |
| **Security** | **[Linux Privilege Escalation](skills/security/linux-privilege-escalation/SKILL.md)** | 🔥 |
| **Security** | **[Metasploit Framework](skills/security/metasploit-framework/SKILL.md)** | 🔥 |
| **Security** | **[Network 101](skills/security/network-101/SKILL.md)** | 🔥 |
| **Security** | **[Pentest Checklist](skills/security/pentest-checklist/SKILL.md)** | 🔥 |
| **Security** | **[Pentest Commands](skills/security/pentest-commands/SKILL.md)** | 🔥 |
| **Security** | **[Privilege Escalation Methods](skills/security/privilege-escalation-methods/SKILL.md)** | 🔥 |
| **Security** | **[Red Team Tools and Methodology](skills/security/red-team-tools/SKILL.md)** | 🔥 |
| **Security** | **[SMTP Penetration Testing](skills/security/smtp-penetration-testing/SKILL.md)** | 🔥 |
| **Security** | **[SQL Injection Testing](skills/security/sql-injection-testing/SKILL.md)** | 🔥 |
| **Security** | **[SQLMap Database Penetration Testing](skills/security/sqlmap-database-pentesting/SKILL.md)** | 🔥 |
| **Security** | **[SSH Penetration Testing](skills/security/ssh-penetration-testing/SKILL.md)** | 🔥 |
| **Security** | **[Security Scanning Tools](skills/security/scanning-tools/SKILL.md)** | 🔥 |
| **Security** | **[Shodan Reconnaissance and Pentesting](skills/security/shodan-reconnaissance/SKILL.md)** | 🔥 |
| **Security** | **[Top 100 Web Vulnerabilities Reference](skills/security/top-web-vulnerabilities/SKILL.md)** | 🔥 |
| **Security** | **[Windows Privilege Escalation](skills/security/windows-privilege-escalation/SKILL.md)** | 🔥 |
| **Security** | **[Wireshark Network Traffic Analysis](skills/security/wireshark-analysis/SKILL.md)** | 🔥 |
| **Security** | **[WordPress Penetration Testing](skills/security/wordpress-penetration-testing/SKILL.md)** | 🔥 |
| **Security** | **[api-security-best-practices](skills/security/api-security-best-practices/SKILL.md)** | 🔥 |
| **Security** | **[red-team-tactics](skills/security/red-team-tactics/SKILL.md)** | 🔥 |
| **Coding Standards** | **[security-review](skills/coding-standards/cc-skill-security-review/SKILL.md)** | 🔥 |
| **Security** | **[vulnerability-scanner](skills/security/vulnerability-scanner/SKILL.md)** | 🔥 |

### 🚀 Nivel 4: Growth & Automatización
*Escalabilidad de producto, marketing técnico y flujos autónomos.*

| Categoría | Capacidad | Impacto |
| :--- | :--- | :---: |
| Automation Tools | **[Linux Production Shell Scripts](skills/automation-tools/linux-shell-scripting/SKILL.md)** | ⚡ |
| Product Growth | **[ab-test-setup](skills/product-growth/ab-test-setup/SKILL.md)** | ⚡ |
| Automation Tools | **[address-github-comments](skills/automation-tools/address-github-comments/SKILL.md)** | ⚡ |
| Product Growth | **[ai-product](skills/product-growth/ai-product/SKILL.md)** | ⚡ |
| Product Growth | **[ai-wrapper-product](skills/product-growth/ai-wrapper-product/SKILL.md)** | ⚡ |
| Automation Tools | **[analytics-tracking](skills/automation-tools/analytics-tracking/SKILL.md)** | ⚡ |
| Product Growth | **[app-store-optimization](skills/product-growth/app-store-optimization/SKILL.md)** | ⚡ |
| Automation Tools | **[bash-linux](skills/automation-tools/bash-linux/SKILL.md)** | ⚡ |
| Automation Tools | **[blockrun](skills/automation-tools/blockrun/SKILL.md)** | ⚡ |
| Product Growth | **[brainstorming](skills/product-growth/brainstorming/SKILL.md)** | ⚡ |
| Automation Tools | **[browser-automation](skills/automation-tools/browser-automation/SKILL.md)** | ⚡ |
| Automation Tools | **[browser-extension-builder](skills/automation-tools/browser-extension-builder/SKILL.md)** | ⚡ |
| Automation Tools | **[busybox-on-windows](skills/automation-tools/busybox-on-windows/SKILL.md)** | ⚡ |
| Product Growth | **[competitor-alternatives](skills/product-growth/competitor-alternatives/SKILL.md)** | ⚡ |
| Automation Tools | **[context7-auto-research](skills/automation-tools/context7-auto-research/SKILL.md)** | ⚡ |
| Automation Tools | **[daily-news-report](skills/automation-tools/daily-news-report/SKILL.md)** | ⚡ |
| Automation Tools | **[exa-search](skills/automation-tools/exa-search/SKILL.md)** | ⚡ |
| Automation Tools | **[file-organizer](skills/automation-tools/file-organizer/SKILL.md)** | ⚡ |
| Automation Tools | **[firecrawl-scraper](skills/automation-tools/firecrawl-scraper/SKILL.md)** | ⚡ |
| Product Growth | **[form-cro](skills/product-growth/form-cro/SKILL.md)** | ⚡ |
| Product Growth | **[free-tool-strategy](skills/product-growth/free-tool-strategy/SKILL.md)** | ⚡ |
| Product Growth | **[geo-fundamentals](skills/product-growth/geo-fundamentals/SKILL.md)** | ⚡ |
| Automation Tools | **[github-workflow-automation](skills/automation-tools/github-workflow-automation/SKILL.md)** | ⚡ |
| Automation Tools | **[inngest](skills/automation-tools/inngest/SKILL.md)** | ⚡ |
| Product Growth | **[launch-strategy](skills/product-growth/launch-strategy/SKILL.md)** | ⚡ |
| Product Growth | **[marketing-ideas](skills/product-growth/marketing-ideas/SKILL.md)** | ⚡ |
| Product Growth | **[marketing-psychology](skills/product-growth/marketing-psychology/SKILL.md)** | ⚡ |
| Product Growth | **[micro-saas-launcher](skills/product-growth/micro-saas-launcher/SKILL.md)** | ⚡ |
| Skills | **[n8n-automator](skills/n8n-automator/SKILL.md)** | ⚡ |
| Product Growth | **[notion-template-business](skills/product-growth/notion-template-business/SKILL.md)** | ⚡ |
| Automation Tools | **[obsidian-clipper-template-creator](skills/automation-tools/obsidian-clipper-template-creator/SKILL.md)** | ⚡ |
| Product Growth | **[onboarding-cro](skills/product-growth/onboarding-cro/SKILL.md)** | ⚡ |
| Product Growth | **[page-cro](skills/product-growth/page-cro/SKILL.md)** | ⚡ |
| Product Growth | **[paid-ads](skills/product-growth/paid-ads/SKILL.md)** | ⚡ |
| Product Growth | **[paywall-upgrade-cro](skills/product-growth/paywall-upgrade-cro/SKILL.md)** | ⚡ |
| Automation Tools | **[personal-tool-builder](skills/automation-tools/personal-tool-builder/SKILL.md)** | ⚡ |
| Automation Tools | **[playwright-skill](skills/automation-tools/playwright-skill/SKILL.md)** | ⚡ |
| Product Growth | **[popup-cro](skills/product-growth/popup-cro/SKILL.md)** | ⚡ |
| Automation Tools | **[powershell-windows](skills/automation-tools/powershell-windows/SKILL.md)** | ⚡ |
| Product Growth | **[pricing-strategy](skills/product-growth/pricing-strategy/SKILL.md)** | ⚡ |
| Product Growth | **[product-manager-toolkit](skills/product-growth/product-manager-toolkit/SKILL.md)** | ⚡ |
| Product Growth | **[programmatic-seo](skills/product-growth/programmatic-seo/SKILL.md)** | ⚡ |
| Product Growth | **[referral-program](skills/product-growth/referral-program/SKILL.md)** | ⚡ |
| Product Growth | **[schema-markup](skills/product-growth/schema-markup/SKILL.md)** | ⚡ |
| Product Growth | **[scroll-experience](skills/product-growth/scroll-experience/SKILL.md)** | ⚡ |
| Product Growth | **[segment-cdp](skills/product-growth/segment-cdp/SKILL.md)** | ⚡ |
| Product Growth | **[seo-audit](skills/product-growth/seo-audit/SKILL.md)** | ⚡ |
| Product Growth | **[seo-fundamentals](skills/product-growth/seo-fundamentals/SKILL.md)** | ⚡ |
| Automation Tools | **[server-management](skills/automation-tools/server-management/SKILL.md)** | ⚡ |
| Product Growth | **[signup-flow-cro](skills/product-growth/signup-flow-cro/SKILL.md)** | ⚡ |
| Automation Tools | **[slack-gif-creator](skills/automation-tools/slack-gif-creator/SKILL.md)** | ⚡ |
| Product Growth | **[social-content](skills/product-growth/social-content/SKILL.md)** | ⚡ |
| Automation Tools | **[tavily-web](skills/automation-tools/tavily-web/SKILL.md)** | ⚡ |
| Automation Tools | **[twilio-communications](skills/automation-tools/twilio-communications/SKILL.md)** | ⚡ |
| Automation Tools | **[using-git-worktrees](skills/automation-tools/using-git-worktrees/SKILL.md)** | ⚡ |
| Product Growth | **[viral-generator-builder](skills/product-growth/viral-generator-builder/SKILL.md)** | ⚡ |
| Automation Tools | **[workflow-automation](skills/automation-tools/workflow-automation/SKILL.md)** | ⚡ |
| Automation Tools | **[zapier-make-patterns](skills/automation-tools/zapier-make-patterns/SKILL.md)** | ⚡ |

---

## 🏗️ Convenciones del Repositorio

El sistema se rige por el documento de **[Gobernanza de Repositorio](docs/architecture/REPOSITORY_GOVERNANCE.md)**. Cualquier desviación del estándar disparará una alerta de mantenimiento.

```text
google-antigravity/
├── assets/                 # Activos visuales y multimedia
├── docs/                   # Estrategia y Planificación
├── rules/                  # Reglas de Comportamiento (Prompts)
├── skills/                 # CATÁLOGO DE CAPACIDADES
└── tools/                  # Herramientas de Soporte
```

<div align="center">

**[📚 Ver Gobernanza Completa](docs/architecture/REPOSITORY_GOVERNANCE.md)**
<br>
*Google Antigravity System © 2026 • Premium Dashboard V3*

</div>
