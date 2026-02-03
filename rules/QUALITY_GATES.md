# ✅ Quality Gates Antigravity

**Versión**: 1.0.0  
**Estado**: OBLIGATORIO  
**Nivel**: 1 (Calidad - Transversal)

---

## 🎯 Propósito

Este documento define los **quality gates obligatorios** que se aplican **automáticamente** en diferentes momentos del ciclo de desarrollo. Estos gates unifican todos los workflows de QA en checklists automáticos.

**Origen**: Unifica `auto-qa.md` y otros workflows de calidad.

---

## 🚦 Quality Gates (Por Momento)

### 1. Pre-Code Gate (Antes de Escribir Código)

**Trigger**: Antes de crear/editar cualquier archivo de código

**Verificaciones Automáticas**:

#### Estructura de Proyecto

- [ ] ✅ Proyecto tiene directorio `.agent/`
- [ ] ✅ Existe `.agent/rules/architecture.md`
- [ ] ✅ Existe `README.md` y `README.es.md`
- [ ] ✅ Existe `.gitignore` configurado

#### Configuración TypeScript

- [ ] ✅ `tsconfig.json` existe
- [ ] ✅ `strict: true` habilitado
- [ ] ✅ `noUncheckedIndexedAccess: true`

#### Configuración ESLint

- [ ] ✅ `.eslintrc.json` o `eslint.config.js` existe
- [ ] ✅ Reglas de TypeScript habilitadas

**Acción si Falla**: Crear archivos faltantes automáticamente

---

### 2. During-Code Gate (Mientras Escribo Código)

**Trigger**: Durante la creación/edición de código

**Reglas Aplicadas Automáticamente**:

#### Naming Conventions

- ✅ Componentes: `PascalCase.tsx`
- ✅ Utilidades: `camelCase.ts`
- ✅ Hooks: `use*.ts`
- ✅ Types: `*.types.ts`
- ✅ Variables: `camelCase`
- ✅ Constantes: `SCREAMING_SNAKE_CASE`
- ✅ Funciones: `camelCase` (verbo)
- ✅ Booleanos: `is*`, `has*`, `can*`

#### Import Order

```typescript
// 1. React
import React from "react";

// 2. Librerías externas
import { motion } from "framer-motion";

// 3. Internos
import { Button } from "@/components/ui/button";

// 4. Types
import type { User } from "@/types/user.types";

// 5. Estilos
import "./styles.css";
```

#### TypeScript Strict

- ✅ Nunca usar `any`
- ✅ Interfaces para objetos públicos
- ✅ Types para uniones
- ✅ Genéricos descriptivos

#### Error Handling

- ✅ Try-catch en operaciones async
- ✅ Logging con contexto
- ✅ Return de errores (no throw en producción)

#### Comments

- ✅ Comentar el WHY, no el WHAT
- ✅ JSDoc para funciones exportadas
- ✅ Código en inglés, comentarios complejos en español

**Acción si Falla**: Advertir al usuario antes de guardar

---

### 3. Post-Code Gate (Después de Escribir Código)

**Trigger**: Después de crear/editar archivos

**Verificaciones Automáticas**:

#### TypeScript Type Check

```bash
// turbo
tsc --noEmit
```

**Expectativa**: 0 errores de tipos

#### ESLint

```bash
// turbo
npx eslint . --ext .ts,.tsx --max-warnings 0
```

**Expectativa**: 0 errores, 0 warnings

#### Build Verification

```bash
// turbo
npm run build
```

**Expectativa**: Build exitoso sin errores

**Acción si Falla**: Bloquear commit, mostrar errores al usuario

---

### 4. Pre-Commit Gate (Antes de Hacer Commit)

**Trigger**: Antes de `git commit`

**Verificaciones Automáticas**:

#### Git Status

```bash
// turbo
git status
```

**Verificar**:

- [ ] ✅ No hay archivos `.env` en staging
- [ ] ✅ No hay secretos hardcodeados
- [ ] ✅ No hay archivos grandes (> 10MB)
- [ ] ✅ `.gitignore` incluye `node_modules/`, `.env*`, `.DS_Store`

#### Conventional Commits

```bash
// Formato obligatorio
<type>(<scope>): <description>

# Tipos válidos
feat, fix, refactor, style, docs, test, chore
```

**Ejemplos**:

- ✅ `feat(auth): implement SSR authentication`
- ✅ `fix(ui): correct dark mode contrast`
- ✅ `refactor(api): extract fetch logic to service`
- ❌ `updated stuff`
- ❌ `fix bug`

#### Code Quality

- [ ] ✅ No `console.log` en producción
- [ ] ✅ No `TODO` sin issue asociado
- [ ] ✅ No código comentado sin razón
- [ ] ✅ No imports no utilizados

**Acción si Falla**: Bloquear commit, solicitar correcciones

---

### 5. Pre-Deploy Gate (Antes de Deploy)

**Trigger**: Antes de hacer deploy a producción

**Verificaciones Automáticas**:

#### Tests

```bash
// turbo
npm run test
```

**Expectativa**: Todos los tests pasan

#### Build de Producción

```bash
// turbo
npm run build
```

**Expectativa**: Build exitoso

#### Variables de Entorno

- [ ] ✅ `.env.example` actualizado
- [ ] ✅ Todas las variables necesarias documentadas
- [ ] ✅ No hay secretos en `.env.example`

#### Database Migrations (si aplica)

- [ ] ✅ Migraciones aplicadas
- [ ] ✅ RLS policies verificadas
- [ ] ✅ Indexes creados

#### Security

- [ ] ✅ Dependencias actualizadas (`npm audit`)
- [ ] ✅ No vulnerabilidades críticas
- [ ] ✅ HTTPS configurado

**Acción si Falla**: Bloquear deploy, solicitar correcciones

---

### 6. Pre-Delivery Gate (Antes de notify_user)

**Trigger**: Antes de presentar trabajo al usuario

**Verificaciones Automáticas**:

#### Code Quality Summary

```bash
# Ejecutar todos los checks
tsc --noEmit && \
npx eslint . --ext .ts,.tsx --max-warnings 0 && \
npm run build
```

#### Content Quality (si aplica)

**Para Artículos/Docs**:

- [ ] ⚠️ Word count ≥ 800 palabras
- [ ] ⚠️ Estructura: H1 → H2 → H3 (sin saltos)
- [ ] ⚠️ Listas usadas apropiadamente
- [ ] ⚠️ Código formateado correctamente
- [ ] ⚠️ Links válidos y descriptivos

**Para Componentes UI**:

- [ ] ⚠️ Responsive (4 breakpoints: 375px, 768px, 1024px, 1440px)
- [ ] ⚠️ Dark mode funciona
- [ ] ⚠️ Accesibilidad (alt text, ARIA, contraste, keyboard nav)

#### Accessibility Check

**Obligatorio**:

- [ ] ✅ Imágenes tienen alt text descriptivo
- [ ] ✅ Inputs tienen labels asociados
- [ ] ✅ Elementos interactivos tienen ARIA apropiado
- [ ] ✅ Contraste de color ≥ 4.5:1 (texto)
- [ ] ✅ Navegación por teclado funciona
- [ ] ✅ Focus states visibles

**Herramienta**: Lighthouse Accessibility Score ≥ 95

#### SEO Check (si aplica)

**Metadata**:

- [ ] ✅ Título único (50-60 chars)
- [ ] ✅ Meta description (150-160 chars)
- [ ] ✅ Open Graph tags
- [ ] ✅ Twitter Card metadata

**Structured Data**:

- [ ] ⚠️ JSON-LD schema (si es artículo)
- [ ] ⚠️ Schema válido (schema.org validator)

**Herramienta**: Lighthouse SEO Score ≥ 95

#### Performance Check

**Core Web Vitals**:

- [ ] ✅ LCP (Largest Contentful Paint) < 2.5s
- [ ] ✅ FID (First Input Delay) < 100ms
- [ ] ✅ CLS (Cumulative Layout Shift) < 0.1

**Lighthouse Scores**:

- [ ] ✅ Performance ≥ 90
- [ ] ✅ Accessibility ≥ 95
- [ ] ✅ Best Practices ≥ 90
- [ ] ✅ SEO ≥ 95

**Optimizaciones**:

- [ ] ✅ Imágenes optimizadas (WebP, lazy loading)
- [ ] ✅ Code splitting aplicado
- [ ] ✅ No re-renders innecesarios
- [ ] ✅ No `console.log` en producción

#### Git Clean State

```bash
// turbo
git status
```

**Verificar**:

- [ ] ✅ Todos los cambios commiteados
- [ ] ✅ Commits siguen conventional commits
- [ ] ✅ No archivos grandes
- [ ] ✅ Branch actualizado con main

**Acción**: Generar reporte de QA automático

---

## 📊 Reporte de QA Automático

### Formato del Reporte

```markdown
## 🔍 Quality Assurance Report

**Fecha**: 2026-02-03  
**Proyecto**: venezuela-news-app  
**Branch**: feature/new-carousel

---

### ✅ Passed (X/Y checks)

- TypeScript: 0 errors
- ESLint: 0 errors, 0 warnings
- Build: Success
- Git Status: Clean
- Conventional Commits: ✅
- Accessibility: 98/100
- Performance: 95/100

---

### ⚠️ Needs Attention (X items)

- **SEO**: Meta description missing on `/about` page
- **Performance**: Image on homepage not optimized (1.2MB)
- **Content**: Article word count is 650 (target: 800+)

---

### ❌ Failed (X critical issues)

- **Security**: `.env` file found in git staging area
- **TypeScript**: 3 type errors in `components/ArticleCard.tsx`

---

### 📝 Recommendations

1. **Optimize Images**: Convert homepage hero image to WebP and add lazy loading
2. **Expand Content**: Add 150+ words to article to meet minimum requirement
3. **Fix SEO**: Add meta description to About page
4. **Remove .env**: Unstage `.env` file and add to `.gitignore`

---

### 🎯 Next Steps

1. Fix critical issues (❌)
2. Address warnings (⚠️)
3. Re-run QA checks
4. Proceed with delivery
```

---

## 🤖 Automatización en GEMINI.md

### Triggers Automáticos

```markdown
## AUTOMATIC QUALITY GATES

### Before Writing Code

1. Verify project structure (.agent/, README, tsconfig.json)
2. Check TypeScript strict mode enabled
3. Check ESLint configured

### While Writing Code

1. Apply naming conventions automatically
2. Order imports automatically
3. Add JSDoc to exported functions
4. Use try-catch for async operations

### After Writing Code

1. Run `tsc --noEmit` automatically
2. Run `npx eslint` automatically
3. Run `npm run build` automatically
4. Report issues to user

### Before Commit

1. Check git status
2. Verify conventional commit format
3. Check for secrets/large files
4. Verify .gitignore

### Before Delivery (notify_user)

1. Run full QA checklist
2. Generate QA summary report
3. List critical issues (❌)
4. List warnings (⚠️)
5. Provide recommendations (📝)
6. Only proceed if 0 critical issues
```

---

## 🎨 Quality Gates por Tipo de Proyecto

### Frontend (Next.js + React)

**Adicionales**:

- [ ] ✅ Server Components por defecto
- [ ] ✅ `'use client'` solo cuando necesario
- [ ] ✅ Imágenes usan `next/image`
- [ ] ✅ Fonts usan `next/font`
- [ ] ✅ Suspense boundaries para loading
- [ ] ✅ Error boundaries por feature
- [ ] ✅ Glassmorphism aplicado (si UI luxury)
- [ ] ✅ Dark mode funciona
- [ ] ✅ Responsive (4 breakpoints)

### Backend (Supabase)

**Adicionales**:

- [ ] ✅ RLS habilitado en todas las tablas
- [ ] ✅ Policies definidas (SELECT, INSERT, UPDATE, DELETE)
- [ ] ✅ Auth SSR implementado (`@supabase/ssr`)
- [ ] ✅ Middleware protege rutas
- [ ] ✅ Foreign keys con cascade apropiado
- [ ] ✅ Indexes en columnas frecuentes
- [ ] ✅ Singleton para cliente Supabase

### Content (Artículos/Docs)

**Adicionales**:

- [ ] ✅ Word count ≥ 800 (artículos)
- [ ] ✅ Estructura H1 → H2 → H3
- [ ] ✅ Introducción (100-150 palabras)
- [ ] ✅ 3-5 secciones principales
- [ ] ✅ Conclusión (100-150 palabras)
- [ ] ✅ Código formateado con syntax highlighting
- [ ] ✅ Imágenes/diagramas (si aplica)
- [ ] ✅ Links internos/externos

---

## 🚨 Niveles de Severidad

### Crítico (❌) - Bloquea Entrega

- Build fallido
- TypeScript errors
- ESLint errors
- Secretos hardcodeados
- Vulnerabilidades de seguridad
- RLS deshabilitado (producción)
- Lighthouse Performance < 70

**Acción**: NO proceder hasta resolver

### Alto (⚠️) - Requiere Atención

- ESLint warnings
- Lighthouse scores < 90
- Accesibilidad < 95
- Código duplicado > 10%
- Funciones > 50 líneas
- Missing alt text
- Missing ARIA labels

**Acción**: Resolver antes de delivery o documentar razón

### Medio (📝) - Recomendación

- Comentarios desactualizados
- TODOs sin issue
- Nombres de variables mejorables
- Oportunidades de refactoring
- Optimizaciones menores

**Acción**: Considerar para próximo sprint

### Bajo (💡) - Nice to Have

- Mejoras de performance menores
- Refactorings cosméticos
- Documentación adicional

**Acción**: Backlog

---

## 📚 Referencias

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md) - Nivel 0
- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md) - Nivel 1
- [CODE_STANDARDS.md](./CODE_STANDARDS.md) - Nivel 1
- [auto-qa.md](../../venezuela-news-app/.agent/workflows/auto-qa.md) - Workflow original

---

**Última Actualización**: 2026-02-03  
**Mantenedor**: Luis Sambrano  
**Estado**: ACTIVO
