---
description: Resumen del estado actual del proyecto
---

# /status - Estado del Proyecto

Usa este workflow cuando quieras saber cómo va el proyecto.

## Lo que YO hago automáticamente

1. **Reviso el código**
   - TypeScript errors
   - ESLint warnings
   - Build status

2. **Reviso Git**
   - Commits pendientes
   - Branch actual
   - Sincronización con GitHub

3. **Reviso calidad**
   - Accesibilidad
   - Performance
   - SEO (si aplica)

4. **Te doy resumen**
   - ✅ Lo que está bien
   - ⚠️ Lo que necesita atención
   - 📝 Recomendaciones

## Cuándo usarlo

- No recuerdas dónde quedaste
- Quieres saber si hay problemas
- Antes de mostrar a alguien
- Cuando retomas después de días/semanas

## Ejemplo

Tú: `/status`

Yo:

```
📊 Estado de venezuela-news-app

## ✅ Bien (5/7)
- TypeScript: 0 errores
- ESLint: 0 errores
- Build: Exitoso
- Git: Sincronizado con GitHub
- Accesibilidad: 95/100

## ⚠️ Atención (2 items)
- Performance: 78/100 (imagen hero muy grande)
- SEO: Falta meta description en /about

## 📝 Recomendaciones
1. Optimizar imagen hero (convertir a WebP)
2. Agregar meta description a /about

## 🔄 Último commit
`feat(carousel): add auto-play functionality` (hace 2 días)

¿Quieres que arregle alguno de los warnings?
```
