import os
import re

def parse_skill_md(file_path):
    """Parses a SKILL.md file to extract name, description, and stack."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to parse YAML frontmatter with regex
        yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        name, description, stack = None, None, None
        
        if yaml_match:
            yaml_content = yaml_match.group(1)
            name_match = re.search(r'^name:\s*(.+)$', yaml_content, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', yaml_content, re.MULTILINE)
            stack_match = re.search(r'^stack:\s*(.+)$', yaml_content, re.MULTILINE)
            
            if name_match: name = name_match.group(1).strip().strip('"').strip("'")
            if desc_match: description = desc_match.group(1).strip().strip('"').strip("'")
            if stack_match: stack = stack_match.group(1).strip().strip('"').strip("'")
            
        # Fallback for name: H1
        if not name:
            h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if h1_match: name = h1_match.group(1).strip()
            else: name = os.path.basename(os.path.dirname(file_path)).title()

        # Fallback for description
        if not description:
            # Look for a paragraph after the header or frontmatter
            body = content
            if yaml_match: body = content[yaml_match.end():]
            desc_match = re.search(r'^(?!#)(.+)$', body, re.MULTILINE)
            description = desc_match.group(1).strip() if desc_match else "Capacidad modular del sistema."

        # Fallback for stack based on path
        if not stack:
            path_lower = file_path.lower()
            if "react" in path_lower: stack = "React"
            elif "python" in path_lower: stack = "Python"
            elif "nextjs" in path_lower: stack = "Next.js"
            elif "typescript" in path_lower or "ts" in path_lower: stack = "TS"
            else: stack = "N/A"

        return name, description, stack
    except:
        return None, None, None

def get_level(path):
    """Maps path to Nivel/Domain."""
    path_lower = path.lower()
    if "meta-skills" in path_lower: return 0
    if any(k in path_lower for k in ["ai-agents", "llm", "intelligence"]): return 1
    if any(k in path_lower for k in ["web-development", "frontend", "backend", "fullstack", "game"]): return 2
    if "security" in path_lower: return 3
    if any(k in path_lower for k in ["product-growth", "automation", "n8n"]): return 4
    return 5

def generate_dashboard_v3():
    skills_dir = "skills"
    levels = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    icons = {
        0: "🧬", 1: "🧠", 2: "💻", 3: "🛡️", 4: "🚀", 5: "📦"
    }

    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            path = os.path.join(root, "SKILL.md")
            name, desc, stack = parse_skill_md(path)
            if name:
                # Sanitize description
                desc = desc.split('.')[0].strip()
                if len(desc) > 85: desc = desc[:82] + "..."
                
                lvl = get_level(root)
                levels[lvl].append({
                    "name": name,
                    "path": path,
                    "desc": desc,
                    "stack": stack,
                    "cat": os.path.basename(os.path.dirname(root)).replace("-", " ").title()
                })

    header = """<div align="center">

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
"""
    for s in sorted(levels[0], key=lambda x: x['name']):
        header += f"| **[{s['name'].upper()}]({s['path']})** | {s['desc']} | `{s['stack']}` | 🔴 |\n"

    lv1 = """
### 🧠 Nivel 1: Inteligencia Artificial
*Orquestación de LLMs, arquitecturas de agentes y memoria persistente.*

| Habilidad AI | Función Principal | Stack |
| :--- | :--- | :---: |
"""
    for s in sorted(levels[1], key=lambda x: x['name']):
        lv1 += f"| **[{s['name']}]({s['path']})** | {s['desc']} | `{s['stack']}` |\n"

    lv2 = """
### 💻 Nivel 2: Ingeniería & Web
*Sistemas de diseño inteligente, frameworks modernos y despliegue.*

| Dominio | Skill Destacada | Enfoque |
| :--- | :--- | :--- |
"""
    for s in sorted(levels[2], key=lambda x: x['name']):
        lv2 += f"| **{s['cat']}** | **[{s['name']}]({s['path']})** | {s['desc']} |\n"

    lv3 = """
### 🛡️ Nivel 3: Seguridad & Resiliencia
*Protocolos de seguridad ofensiva, pentesting y auditoría.*

| Vector | Objetivo | Criticidad |
| :--- | :--- | :---: |
"""
    for s in sorted(levels[3], key=lambda x: x['name']):
        lv3 += f"| **{s['cat']}** | **[{s['name']}]({s['path']})** | 🔥 |\n"

    lv4 = """
### 🚀 Nivel 4: Growth & Automatización
*Escalabilidad de producto, marketing técnico y flujos autónomos.*

| Categoría | Capacidad | Impacto |
| :--- | :--- | :---: |
"""
    for s in sorted(levels[4], key=lambda x: x['name']):
        lv4 += f"| {s['cat']} | **[{s['name']}]({s['path']})** | ⚡ |\n"

    footer = """
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
"""

    with open("README_MASTER.md", "w", encoding="utf-8") as f:
        f.write(header + lv1 + lv2 + lv3 + lv4 + footer)
    print("Dashboard V3 Premium generado con éxito.")

if __name__ == "__main__":
    generate_dashboard_v3()
