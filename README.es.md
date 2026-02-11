<div align="center">

# Antigravity Config

Un framework de configuración para entornos de desarrollo asistidos por IA.  
Reglas, skills y workflows que estandarizan cómo operan los agentes de código IA en tus proyectos.

<p>
  <a href="./README.md">English</a> •
  <a href="./README.es.md">Español</a> •
  <a href="./README.pt.md">Português</a>
</p>

<p>
  <a href="#"><img src="https://img.shields.io/badge/Licencia-MIT-blue?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/LuisSambrano/antigravity-config/stargazers"><img src="https://img.shields.io/github/stars/LuisSambrano/antigravity-config?style=flat-square" alt="Stars"/></a>
</p>

</div>

---

## Qué es esto

Este repositorio provee un directorio `.agent/` listo para usar con asistentes de código IA (Gemini, Cursor, Windsurf, etc.). Incluye:

- **Rules** — Estándares de código, patrones de arquitectura y quality gates que el agente IA aplica automáticamente.
- **Skills** — Archivos de conocimiento especializado que extienden la expertise del agente (44 skills en 8 categorías).
- **Workflows** — Scripts de comandos paso a paso que el agente sigue para tareas comunes como deployment y setup de proyectos.

El objetivo es directo: clonar, instalar, y tener un entorno de desarrollo consistente y opinionado donde tu asistente IA sigue estándares profesionales.

---

## Inicio Rápido

```bash
git clone https://github.com/LuisSambrano/antigravity-config.git
cd antigravity-config && chmod +x install.sh && ./install.sh
```

El instalador copia rules, skills y workflows a tu directorio `.agent/` del workspace y configura `GEMINI.md` como archivo de reglas globales.

---

## Estructura del Repositorio

```
antigravity-config/
├── GEMINI.md                  # Template de reglas globales (personalizable)
├── install.sh                 # Script de instalación
│
├── rules/                     # Estándares de código y arquitectura
│   ├── PROTOCOL_ZERO.md       # Filosofía base y principios
│   ├── ARCHITECTURE_STANDARDS.md
│   ├── CODE_STANDARDS.md
│   ├── QUALITY_GATES.md
│   ├── frontend/              # Reglas específicas de frontend
│   └── backend/               # Reglas específicas de backend
│
├── skills/                    # Conocimiento de dominio (44 skills)
│   ├── 1-core/                # Fundamentos de código
│   ├── 2-ai/                  # Agentes IA, RAG, prompting
│   ├── 3-web/                 # Desarrollo web (Next.js, React, Tailwind)
│   ├── 4-automation/          # Testing, CI/CD, scraping
│   ├── 5-security/            # Seguridad API, pentesting
│   ├── 6-content/             # Escritura técnica, SEO
│   ├── 7-meta/                # Creación y gestión de skills
│   └── 8-blockchain/          # Celo, EVM, DeFi
│
├── workflows/                 # Scripts de comandos del agente
│   ├── deploy.md              # /deploy — deployment a producción
│   ├── idea.md                # /idea — evaluar ideas de proyecto
│   ├── status.md              # /status — health check del proyecto
│   ├── create-component.md    # /create-component — scaffold de componentes
│   └── help.md                # /help — listar comandos disponibles
│
├── templates/                 # Templates de proyecto
├── research/                  # Log de decisiones y hallazgos
└── docs/                      # Documentación adicional
```

---

## Referencia de Skills

Los skills son archivos markdown que dan al agente IA conocimiento específico de dominio. Cada skill contiene instrucciones, patrones y referencias que el agente utiliza al trabajar en ese dominio.

### 1-core — Fundamentos

Convenciones de código, estándares de estructura de proyecto y patrones TypeScript aplicables a todos los proyectos.

### 2-ai — IA y Agentes (10 skills)

Orquestación multi-agente (LangGraph, CrewAI), sistemas RAG, ingeniería de prompts, desarrollo de Voice AI y frameworks de evaluación de agentes.

### 3-web — Desarrollo Web (8 skills)

Patrones de Next.js App Router, mejores prácticas de React, arquitectura Tailwind CSS, integración con Supabase, deployment en Vercel y principios de diseño UI/UX.

### 4-automation — Testing y DevOps (4 skills)

Testing con Playwright, workflows de GitHub Actions, procedimientos de deployment y web scraping con Firecrawl.

### 5-security — Seguridad (2 skills)

Mejores prácticas de seguridad API y checklists de penetration testing.

### 6-content — Creación de Contenido

Guías de escritura técnica, copywriting SEO y estándares de documentación.

### 7-meta — Gestión de Skills (3 skills)

Herramientas para crear nuevos skills, planificación con archivos y mejora continua (Kaizen).

### 8-blockchain — Celo y EVM (16 skills)

Stack completo de desarrollo Celo: integración con MiniPay, fee abstraction, direcciones de stablecoins, scaffolding con Celo Composer, librerías viem/wagmi, tooling Hardhat/Foundry, bridging cross-chain, integración con protocolos DeFi, protocolo de confianza ERC-8004 y protocolo de pagos HTTP x402.

> Ver [skills/INDEX.md](./skills/INDEX.md) para el desglose skill por skill.

---

## Resumen de Rules

Las rules definen cómo el agente IA escribe y valida código. Se cargan en el contexto del agente y se aplican automáticamente.

| Rule                        | Propósito                                                            |
| --------------------------- | -------------------------------------------------------------------- |
| `PROTOCOL_ZERO.md`          | Filosofía base: calidad sobre velocidad, local como fuente de verdad |
| `ARCHITECTURE_STANDARDS.md` | Estructura de proyecto, organización de componentes, nomenclatura    |
| `CODE_STANDARDS.md`         | TypeScript strict mode, orden de imports, error handling, JSDoc      |
| `QUALITY_GATES.md`          | Checks pre-commit, verificación de build, accesibilidad, performance |

---

## Personalización

`GEMINI.md` es el archivo de configuración principal. Agrega todas las rules en un solo documento que el agente IA lee. Edítalo para:

- Agregar o quitar rules
- Cambiar convenciones de nomenclatura
- Ajustar umbrales de calidad
- Agregar routing de workflows para tus propios comandos

Las secciones marcadas con `<!-- CUSTOMIZE -->` están diseñadas para ser modificadas.

---

## Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para pautas sobre agregar skills, workflows o rules.

```bash
git checkout -b feature/tu-feature
git commit -m 'feat(skills): add nombre-del-skill'
git push origin feature/tu-feature
```

---

## Investigación y Log de Decisiones

| Documento                                     | Propósito                                    |
| --------------------------------------------- | -------------------------------------------- |
| [KEY_FINDINGS.md](./research/KEY_FINDINGS.md) | Principios base y hallazgos de investigación |
| [prompts/](./research/prompts/)               | Prompts de definición de rules e iteraciones |
| [rules/](./rules/)                            | Los documentos de estándares resultantes     |

---

## Licencia

MIT — ver [LICENSE](LICENSE) para detalles.

---

<div align="center">

**Mantenido por [Luis Sambrano](https://github.com/LuisSambrano)**

</div>
