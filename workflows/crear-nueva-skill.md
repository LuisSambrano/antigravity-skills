# Workflow: Creación de Nueva Skill

Este flujo describe los pasos para expandir la inteligencia del workspace añadiendo una nueva habilidad especializada.

## Pasos del Workflow

1.  **Identificar la Necesidad**: Definir qué tarea específica resolverá la nueva skill.
2.  **Categorizar**: Determinar en qué carpeta de `skills/` encaja mejor (ej: `skills/security` o `skills/ai-agents`).
3.  **Crear Directorio**:
    ```bash
    mkdir -p skills/[categoria]/[nombre-skill]
    ```
4.  **Redactar SKILL.md**:
    - Usar el formato estándar de Antigravity.
    - Definir el propósito, las instrucciones expertas y ejemplos de uso.
5.  **Verificación**:
    - Validar que el archivo `SKILL.md` sea legible.
    - Probar una tarea corta usando la nueva skill para confirmar que el agente entiende las instrucciones.

## // turbo

6.  **Indexación**: Actualizar el `README.md` maestro de la raíz para incluir la nueva capacidad si es de alto nivel.
