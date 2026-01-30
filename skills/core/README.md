<div align="center">

# ⚡ Antigravity Skills

**Enterprise-Grade AI Capabilities for Google Gemini Ecosystem**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E75B2?style=flat&logo=google&logoColor=white)](https://ai.google.dev)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](https://github.com/LuisSambrano/google-antigravity)

> _Clean-room engineered capabilities. Zero hallucination. Production-ready._

[📖 Catalog](#-skill-catalog) • [🚀 Quick Start](#-quick-start) • [💬 Support](#-support)

</div>

---

## 🎯 What is This?

**Antigravity Skills** is a curated library of **deterministic AI instruction sets** (skills) designed for Google Gemini and agentic workflows. Unlike generic prompt libraries, every skill here is:

- ✅ **Clean-room engineered** (written from scratch, no copy-paste)
- ✅ **Google-first** (optimized for Gemini 1.5 Pro/Flash context windows)
- ✅ **Production-tested** (used in real commercial projects)
- ✅ **Bilingual** (English + Spanish support)

Think of it as **"npm for AI capabilities"** — modular, reusable, and battle-tested.

---

## 📚 Skill Catalog

### 🏗️ **Antigravity Architect** `v2.1.0` 🆕

> Senior System Architect that transforms product ideas into technical blueprints using Socratic discovery.

**What it does**:

- 🔍 **Phase 1 (Discovery)**: Researches similar products, asks critical questions, challenges assumptions
- 🏛️ **Phase 2 (Blueprint)**: Generates complete architecture (Mermaid diagrams, tech stack, schema, risk assessment)

**Best for**: Founders, CTOs, or developers starting a new project who need a technical roadmap before writing code.

**Key Features**:

- Educational multiple-choice questions (novice-friendly)
- Red Team self-critique (identifies weaknesses in proposed architecture)
- Cost breakdowns and alternative approaches

**📺 See it in action**: [Live Demo on Gist](https://gist.github.com/LuisSambrano/8c7f188340296102543ca9e0aa2ca4b8) - MicroLearn AI Curator case study

📂 [View Skill](/.agent/skills/custom/antigravity-architect/SKILL.md) | 📖 [Question Framework](/.agent/skills/custom/antigravity-architect/QUESTION_FRAMEWORK.md)

---

### 🛠️ **Skill Forge** (Spanish) `v1.0.0`

> Meta-skill for creating new skills that meet Antigravity standards.

**What it does**: Guides you through the process of designing, documenting, and validating a new AI skill.

**Best for**: Developers building custom capabilities for their AI agents.

📂 [View Skill](/.agent/skills/custom/skill-creator-es/SKILL.md)

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/LuisSambrano/google-antigravity.git
cd google-antigravity
```

### Step 2: Use a Skill in Your Project

**Option A: Copy to your project**

```bash
# Copy a specific skill
cp -r .agent/skills/custom/antigravity-architect ./my-project/.agent/skills/

# Or copy all skills
cp -r .agent/skills/custom/* ./my-project/.agent/skills/
```

**Option B: Reference directly** (if using Antigravity agent)

```bash
# In your agent config, point to this repo
SKILLS_PATH=~/google-antigravity/.agent/skills/custom
```

### Step 3: Invoke the Skill

Example with **Antigravity Architect**:

```
User: "I need a platform for farmers to sell to restaurants."

Architect: [Generates Discovery Report with research, questions, and objections]

User: [Answers questions]

Architect: [Generates complete Blueprint with architecture, schema, and implementation plan]
```

---

## 📝 Featured Gists

Quick-reference guides and templates for common use cases:

- **[Antigravity Architect - Live Demo](https://gist.github.com/LuisSambrano/8c7f188340296102543ca9e0aa2ca4b8)** - See the skill in action (MicroLearn AI Curator case study)
- **[Gemini 1.5 Pro - Prompt Engineering Template](https://gist.github.com/LuisSambrano/0cf02751021ccd7de20a03201e739394)** - Production-ready prompt structure for reliable AI agents
- **[Supabase RLS Patterns](https://gist.github.com/LuisSambrano/d652308ab96b61ab2199d6264b670ec8)** - Real-world Row Level Security policies (SaaS, Social, Marketplace)

---

## 🧠 Philosophy: "Clean Room Engineering"

We don't copy-paste from the internet. Every skill is designed from first principles:

1. **Zero Hallucination**: Logic-driven, not creativity-driven
2. **Deterministic Outputs**: Same input → Same output structure
3. **Google Ecosystem**: Optimized for Gemini, GCP, and modern tooling (Vercel, Supabase)
4. **Novice-Friendly**: Educational, not intimidating (see [Question Framework](/.agent/skills/custom/antigravity-architect/QUESTION_FRAMEWORK.md))

---

## 📖 Documentation

- **[CATALOG.md](./CATALOG.md)**: Full list of skills with descriptions
- **[CONTRIBUTING.md](./CONTRIBUTING.md)**: How to submit new skills (coming soon)
- **Skill-specific docs**: Each skill has its own `SKILL.md` with usage examples

---

## 💬 Support

Have questions or want to request a new skill?

**📱 Telegram**: [@luissambrano_ux](https://t.me/luissambrano_ux)  
**🐛 Issues**: [GitHub Issues](https://github.com/LuisSambrano/google-antigravity/issues)

> _We're building a chatbot for automated support. For now, reach out via Telegram for fastest response._

---

## 🗺️ Roadmap

- [x] **v1.0**: Launch with `skill-forge` and `antigravity-architect`
- [ ] **v1.1**: Add `data-architect` skill (database schema design)
- [ ] **v1.2**: Add `api-designer` skill (REST/GraphQL API blueprints)
- [ ] **v2.0**: Web-based skill browser with interactive demos

---

## 📜 License

MIT License - See [LICENSE](./LICENSE) for details.

---

## 🙏 Acknowledgments

Built with ❤️ by **Luis Sambrano** ([Antigravity Engineering](https://github.com/LuisSambrano))

Powered by:

- [Google Gemini 1.5 Pro](https://ai.google.dev)
- [Supabase](https://supabase.com)
- [Vercel](https://vercel.com)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

[🔗 View on GitHub](https://github.com/LuisSambrano/google-antigravity) • [📧 Contact](https://t.me/luissambrano_ux)

</div>
