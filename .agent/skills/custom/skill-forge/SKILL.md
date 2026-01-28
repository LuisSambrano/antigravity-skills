---
name: skill-forge
description: El "Meta-Skill" oficial de Antigravity. Úsalo para diseñar, validar y empaquetar nuevos skills siguiendo los estándares de calidad "Google AI Pro".
---

# ⚡ Antigravity Skill Forge

Bienvenido a **Skill Forge**, la fundición donde creamos capacidades cognitivas nuevas para el ecosistema Antigravity.

Este no es un simple creador de plantillas. Es un **sistema de ingeniería de prompts** diseñado para producir skills robustos, deterministas y compatibles con la infraestructura de Google Cloud y Gemini.

## 🎯 Filosofía de Diseño: "Precision over Creativity"

En Antigravity, un skill no es un chat casual. Es una **función ejecutable en lenguaje natural**.
Debe comportarse con la fiabilidad de una API:

- **Input claro** -> **Proceso Determinista** -> **Output Estructurado**.

---

## 🛠️ Estructura del Ecosistema

Todos los skills deben residir en `.agent/skills/custom/` y seguir esta jerarquía estricta:

```text
nombre-del-skill/
├── SKILL.md          (OBLIGATORIO: Lógica de ejecución)
├── references/        (OPCIONAL: Conocimiento estático)
│   ├── api-docs.md
│   └── architecture.md
└── scripts/           (OPCIONAL: Ejecución determinista)
    ├── validate.py
    └── deploy.sh
```

---

## ⚡ Workflow de Creación (The Forge Protocol)

Para forjar un nuevo skill, sigue estrictamente este protocolo:

### Fase 1: Definición del "Contrato"

Antes de escribir el prompt, define qué problema resuelve y sus límites.

- **Trigger:** ¿Qué debe decir el usuario o qué debe pasar en el sistema para que esto se active?
- **Input:** ¿Qué información necesita el skill para empezar? (Archivos, texto, URLs).
- **Output:** ¿Qué entrega al final? (Código, reporte, diagrama).

### Fase 2: Ingeniería del `SKILL.md`

Usa esta plantilla maestra. No la copies ciegamente; adáptala manténiendo la estructura.

```markdown
---
name: nombre-tecnico-skil (kebab-case)
description: Descripción operativa precisa. NO uses marketing. Di exactamente qué hace y cuándo debe activarse.
---

# [Nombre Legible del Skill]

## 🎯 Objetivo

1-2 frases que definan el éxito de esta operación.

## 🛡️ Protocolos de Seguridad (Safety First)

Define qué NO debe hacer el skill bajo ninguna circunstancia.

- Ejemplo: "Nunca borrar archivos sin confirmación explícita."
- Ejemplo: "Nunca subir credenciales a logs."

## ⚙️ Procedimiento Ejecutable

Instrucciones imperativas, paso a paso. No uses "por favor" o "podrías". Sé un sistema operativo.

1.  **Ingesta de Contexto**:
    - Lee el archivo X.
    - Analiza la estructura Y.

2.  **Procesamiento (Logic Core)**:
    - Si A, entonces ejecuta B.
    - Para cada elemento en C, genera D.

3.  **Generación de Entregables**:
    - Escribe el código en el archivo Z.
    - Aplica el formato JSON estricto.

## 🧪 Verificación (Quality Gate)

Instrucciones para que el propio agente verifique su trabajo antes de terminar.

- "Ejecuta el linter."
- "Verifica que el JSON sea válido."
```

### Fase 3: Integración de Recursos

- **Referencias:** Si el skill necesita saber sobre las APIs de Google Maps o Supabase, NO lo pongas en el `SKILL.md`. Crea un archivo `references/google-maps-api.md` y enlázalo.
- **Scripts:** Si hay una tarea mecánica (ej. redimensionar 100 imágenes), no le pidas al LLM que lo haga. Escribe un script de Python en `scripts/` y haz que el skill lo ejecute.

---

## 🚀 Mejores Prácticas (Antigravity Standard)

1.  **Idempotencia:** Si ejecuto el skill dos veces, el resultado debe ser consistente y no duplicar cosas destructivamente.
2.  **Atomicidad:** Un skill debe hacer UNA cosa bien. Si es muy complejo, divídelo en sub-skills.
3.  **Observabilidad:** El skill debe reportar qué está haciendo ("Analizando 5 archivos...", "Generando reporte...").

---

_"Forged in the fires of Antigravity."_
