import os
import re

def parse_skill_md(file_path):
    """Parses a SKILL.md file to extract name and description."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to parse YAML frontmatter with regex
        yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            name_match = re.search(r'^name:\s*(.+)$', yaml_content, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', yaml_content, re.MULTILINE)
            
            name = name_match.group(1).strip() if name_match else None
            description = desc_match.group(1).strip() if desc_match else None
            
            if name and description:
                name = name.strip('"').strip("'")
                description = description.strip('"').strip("'")
                return name, description

        # Fallback to H1
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip(), "Sin descripción."
            
        return os.path.basename(os.path.dirname(file_path)).title(), "Sin descripción."
    except:
        return None, None

def get_level(path):
    """Maps path to Nivel for Dashboard V2."""
    path_lower = path.lower()
    if "meta-skills" in path_lower: return 0
    if any(k in path_lower for k in ["ai-agents", "llm", "intelligence"]): return 1
    if any(k in path_lower for k in ["web-development", "frontend", "backend"]): return 2
    if "security" in path_lower: return 3
    if any(k in path_lower for k in ["product-growth", "automation", "n8n"]): return 4
    return 5

def generate_dashboard():
    skills_dir = "skills"
    levels = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            path = os.path.join(root, "SKILL.md")
            name, desc = parse_skill_md(path)
            if name:
                # Sanitize description
                desc = desc.split('.')[0].strip()[:100] + "..." if len(desc) > 100 else desc
                levels[get_level(root)].append({
                    "name": name,
                    "path": path,
                    "desc": desc,
                    "cat": os.path.basename(os.path.dirname(root)).replace("-", " ").title()
                })

    header = """<div align="center">

# 🌌 GOOGLE ANTIGRAVITY
### Sistema Operativo de Inteligencia Colectiva

![Status](https://img.shields.io/badge/ESTADO-OPERATIVO-success?style=for-the-badge&logo=statuspage)
![Version](https://img.shields.io/badge/VERSION-2.1.0-blue?style=for-the-badge&logo=semver)
![Access](https://img.shields.io/badge/NIVEL-ROOT-red?style=for-the-badge&logo=riotgames)

<p align="center">
  <em>Arquitectura Modular • Protocolo Zero • Autonomía Agéntica</em>
</p>

</div>

---

## 🧭 Panel de Control

Bienvenido al mapa central. Este repositorio monorepo está organizado por **Dominios de Competencia**. Seleccione un módulo para desplegar sus capacidades.
"""

    # Nivel 0
    lv0 = "\n### 🧬 Nivel 0: El Núcleo (Meta-Skills)\n*Capacidades reflexivas que gobiernan, crean y mejoran el sistema.*\n\n| Módulo | Descripción | Tecnología | Acceso |\n| :--- | :--- | :---: | :---: |\n"
    for s in sorted(levels[0], key=lambda x: x['name']):
        lv0 += f"| **[{s['name'].upper()}]({s['path']})** | {s['desc']} | `System` | 🔴 |\n"

    # Nivel 1
    lv1 = "\n### 🧠 Nivel 1: Inteligencia Artificial\n*Cerebros digitales, memoria y motores cognitivos.*\n\n| Skill | Función Principal | Stack |\n| :--- | :--- | :---: |\n"
    for s in sorted(levels[1], key=lambda x: x['name']):
        lv1 += f"| **[{s['name']}]({s['path']})** | {s['desc']} | `Python` |\n"

    # Nivel 2
    lv2 = "\n### 💻 Nivel 2: Ingeniería & Web\n*Estándares de construcción de software y sistemas de diseño.*\n\n| Dominio | Skill Destacada | Enfoque |\n| :--- | :--- | :--- |\n"
    for s in sorted(levels[2], key=lambda x: x['name']):
        lv1_cat = s['cat']
        lv2 += f"| **{lv1_cat}** | **[{s['name']}]({s['path']})** | {s['desc']} |\n"

    # Nivel 3
    lv3 = "\n### 🛡️ Nivel 3: Seguridad (Red Team)\n*Protocolos ofensivos y defensivos.*\n\n| Vector | Herramienta/Guía | Criticidad |\n| :--- | :--- | :---: |\n"
    for s in sorted(levels[3], key=lambda x: x['name']):
        lv3 += f"| **{s['cat']}** | **[{s['name']}]({s['path']})** | 🔥 |\n"

    # Nivel 4
    lv4 = "\n### 🚀 Nivel 4: Growth & Automatización\n*Expansión del producto y eficiencia operativa.*\n\n"
    # Group by category for Nivel 4
    n4_cats = {}
    for s in levels[4]:
        n4_cats.setdefault(s['cat'], []).append(s)
    
    for cat, items in n4_cats.items():
        lv4 += f"* **{cat}:**\n"
        for s in sorted(items, key=lambda x: x['name']):
            lv4 += f"    * [{s['name']}]({s['path']}) ({s['desc']})\n"

    footer = """
---

<div align="center">

**[📚 Ver Gobernanza del Repositorio](docs/architecture/REPOSITORY_GOVERNANCE.md)**
<br>
*Google Antigravity System © 2026*

</div>
"""

    with open("README_MASTER.md", "w") as f:
        f.write(header + lv0 + lv1 + lv2 + lv3 + lv4 + footer)
    print("Dashboard V2 generado.")

if __name__ == "__main__":
    generate_dashboard()
