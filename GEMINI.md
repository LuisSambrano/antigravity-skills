# GEMINI - Global Rules for Luis Sambrano

**Version**: 2.0.0  
**Last Updated**: 2026-02-03  
**Purpose**: Centro de mando agéntico - Reglas globales para Antigravity

---

## 🌌 ANTIGRAVITY PROTOCOL ZERO

**CRITICAL**: Todas las decisiones técnicas, arquitectónicas y operativas deben alinearse con el **[Protocol Zero](file:///Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/rules/PROTOCOL_ZERO.md)** de Antigravity.

### Principios Fundamentales (Inmutables)

1. **Playground es la Fuente de Verdad**
   - `~/playground` es el origen de toda la verdad
   - GitHub es solo un espejo en la nube
   - Sincronización unidireccional: `Local → GitHub`

2. **Calidad sobre Velocidad**
   - Tests pasan antes de commit
   - Build exitoso antes de push
   - Lint sin errores antes de commit
   - TypeScript strict mode siempre

3. **Documentación como Código**
   - README Trilingüe Senior (EN + ES + PT) obligatorio
   - Arquitectura visible en diagramas Mermaid
   - Comentarios explican el "por qué", no el "qué"

4. **Autonomía con Responsabilidad**
   - Libertad de decisión dentro del protocolo
   - Transparencia total en acciones
   - Documentar decisiones no obvias

5. **Mejora Continua (Kaizen)**
   - Cada sesión deja el código mejor
   - Refactoring incremental constante
   - Aprendizaje documentado en TIL

### Valores No Negociables

- ✅ **Seguridad First**: RLS, validación, sanitización
- ✅ **Accesibilidad**: WCAG 2.1 AA mínimo
- ✅ **Performance**: Core Web Vitals en verde
- ✅ **Mantenibilidad**: Código auto-explicativo
- ✅ **Escalabilidad**: Arquitectura modular

### Reglas de Arquitectura

**OBLIGATORIO**: Seguir [ARCHITECTURE_STANDARDS.md](file:///Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/rules/ARCHITECTURE_STANDARDS.md)

**Estructura de Directorios Mandatoria**:

```
proyecto/
├── .agent/                    # ← OBLIGATORIO
│   ├── rules/
│   ├── workflows/
│   └── templates/
├── app/                       # Next.js App Router
├── components/
│   ├── ui/
│   ├── features/
│   └── layouts/
├── lib/
│   ├── supabase/
│   ├── utils/
│   └── hooks/
├── types/
├── README.md                  # ← OBLIGATORIO (EN)
├── README.es.md               # ← OBLIGATORIO (ES)
└── README.pt.md               # ← OBLIGATORIO (PT)
```

**Patrones Arquitectónicos Obligatorios**:

- ✅ Singleton para clientes (Supabase, APIs)
- ✅ Server Components por defecto
- ✅ Separación de concerns (UI vs lógica)
- ✅ Composición sobre herencia
- ✅ Error boundaries por feature

### Pre-Commit Checklist (OBLIGATORIO)

Antes de hacer commit, SIEMPRE verificar:

```bash
npm run build  # ✅ Debe pasar
npm run lint   # ✅ 0 errores
tsc --noEmit   # ✅ 0 errores de tipos
```

---

## 🤖 AUTOMATIC BEHAVIORS (ALWAYS ACTIVE)

**CRITICAL**: Estos comportamientos se aplican AUTOMÁTICAMENTE sin que el usuario tenga que pedirlo. Son la unificación de todos los workflows manuales en reglas automáticas.

### 📋 Referencia Completa de Reglas

- [PROTOCOL_ZERO.md](file:///Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/rules/PROTOCOL_ZERO.md) - Filosofía
- [ARCHITECTURE_STANDARDS.md](file:///Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/rules/ARCHITECTURE_STANDARDS.md) - Arquitectura
- [CODE_STANDARDS.md](file:///Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/rules/CODE_STANDARDS.md) - Código
- [QUALITY_GATES.md](file:///Users/luissambrano/playground/repos/LuisSambrano/antigravity-config/rules/QUALITY_GATES.md) - Calidad

### 🚀 Before Writing Code (Pre-Code Gate)

**Trigger**: Antes de crear/editar cualquier archivo

**Acciones Automáticas**:

1. ✅ Verificar proyecto tiene `.agent/` directory
2. ✅ Verificar existe `README.md`, `README.es.md` y `README.pt.md`
3. ✅ Verificar `tsconfig.json` con `strict: true`
4. ✅ Verificar `.eslintrc.json` configurado
5. ✅ Si falta algo, crear automáticamente

### ✍️ While Writing Code (During-Code Gate)

**Trigger**: Durante la creación/edición de código

**Reglas Aplicadas Automáticamente**:

#### Naming Conventions

- ✅ Componentes: `PascalCase.tsx`
- ✅ Páginas: `page.tsx`, `layout.tsx`
- ✅ API Routes: `route.ts`
- ✅ Utilidades: `camelCase.ts`
- ✅ Hooks: `use*.ts`
- ✅ Types: `*.types.ts`
- ✅ Variables: `camelCase`
- ✅ Constantes: `SCREAMING_SNAKE_CASE`
- ✅ Funciones: `camelCase` (verbo: `fetchUser`, `createArticle`)
- ✅ Booleanos: `is*`, `has*`, `can*`

#### Import Order (Automático)

```typescript
// 1. React
import React from "react";

// 2. Librerías externas (alfabético)
import { motion } from "framer-motion";

// 3. Internos (alfabético)
import { Button } from "@/components/ui/button";

// 4. Types
import type { User } from "@/types/user.types";

// 5. Estilos
import "./styles.css";
```

#### TypeScript Strict

- ✅ Nunca usar `any` (usar `unknown` + type guard)
- ✅ Interfaces para objetos públicos
- ✅ Types para uniones/intersecciones
- ✅ Genéricos descriptivos (`TInput`, `TOutput`, no `T`, `U`)

#### Error Handling (Obligatorio)

```typescript
// ✅ SIEMPRE usar try-catch en async
async function fetchUser(id: string) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error("Error fetching user:", { id, error });
    return null;
  }
}
```

#### Comments (WHY not WHAT)

```typescript
// ✅ CORRECTO: Explica el POR QUÉ
// Incrementamos aquí en lugar de useEffect para evitar re-renders
count++;

// ❌ INCORRECTO: Explica el QUÉ (obvio)
// Incrementa el contador
count++;
```

#### JSDoc (Obligatorio para Exports)

```typescript
/**
 * Fetches user data from Supabase with caching.
 *
 * @param userId - The UUID of the user
 * @returns User object or null if not found
 * @throws {Error} If Supabase client not initialized
 */
export async function fetchUser(userId: string): Promise<User | null> {
  // Implementation
}
```

### ✅ After Writing Code (Post-Code Gate)

**Trigger**: Después de crear/editar archivos

**Verificaciones Automáticas**:

```bash
# 1. TypeScript Type Check
tsc --noEmit
# Expectativa: 0 errores

# 2. ESLint
npx eslint . --ext .ts,.tsx --max-warnings 0
# Expectativa: 0 errores, 0 warnings

# 3. Build Verification
npm run build
# Expectativa: Build exitoso
```

**Acción si Falla**: Reportar errores al usuario ANTES de proceder

### 📝 Before Commit (Pre-Commit Gate)

**Trigger**: Antes de hacer commit

**Verificaciones Automáticas**:

```bash
# Git Status
git status
```

**Verificar**:

- ✅ No hay archivos `.env` en staging
- ✅ No hay secretos hardcodeados
- ✅ No hay archivos grandes (> 10MB)
- ✅ `.gitignore` incluye `node_modules/`, `.env*`, `.DS_Store`
- ✅ Commit sigue conventional commits: `<type>(<scope>): <description>`
- ✅ No `console.log` en producción
- ✅ No `TODO` sin issue
- ✅ No código comentado sin razón

**Tipos de Commit Válidos**:

- `feat`: Nueva feature
- `fix`: Bug fix
- `refactor`: Refactoring
- `style`: Cambios de estilo
- `docs`: Documentación
- `test`: Tests
- `chore`: Mantenimiento

**Ejemplos**:

- ✅ `feat(auth): implement SSR authentication`
- ✅ `fix(ui): correct dark mode contrast`
- ❌ `updated stuff`

### 🚀 Before Delivery (Pre-Delivery Gate)

**Trigger**: Antes de llamar `notify_user` para presentar trabajo

**Verificaciones Automáticas**:

#### 1. Code Quality Summary

```bash
tsc --noEmit && \
npx eslint . --ext .ts,.tsx --max-warnings 0 && \
npm run build
```

#### 2. Accessibility Check (si UI)

- ✅ Imágenes tienen alt text
- ✅ Inputs tienen labels
- ✅ Elementos interactivos tienen ARIA
- ✅ Contraste ≥ 4.5:1
- ✅ Navegación por teclado funciona
- ✅ Focus states visibles

#### 3. Responsive Design (si UI)

- ✅ Mobile (375px)
- ✅ Tablet (768px)
- ✅ Desktop (1024px)
- ✅ Large (1440px)

#### 4. Dark Mode (si UI)

- ✅ Texto legible
- ✅ Bordes visibles
- ✅ Efectos glass con opacidad correcta

#### 5. SEO (si página pública)

- ✅ Título único (50-60 chars)
- ✅ Meta description (150-160 chars)
- ✅ Open Graph tags
- ✅ Twitter Card metadata

#### 6. Performance (si aplicable)

- ✅ Lighthouse Performance ≥ 90
- ✅ Lighthouse Accessibility ≥ 95
- ✅ Lighthouse Best Practices ≥ 90
- ✅ Lighthouse SEO ≥ 95
- ✅ LCP < 2.5s
- ✅ FID < 100ms
- ✅ CLS < 0.1

#### 7. Generar Reporte de QA

**Formato**:

```markdown
## 🔍 Quality Assurance Report

### ✅ Passed (X/Y checks)

- TypeScript: 0 errors
- ESLint: 0 errors, 0 warnings
- Build: Success
- Accessibility: 98/100
- Performance: 95/100

### ⚠️ Needs Attention (X items)

- SEO: Meta description missing on `/about`
- Performance: Image not optimized (1.2MB)

### ❌ Failed (X critical issues)

- Security: `.env` file in staging
- TypeScript: 3 errors in `ArticleCard.tsx`

### 📝 Recommendations

1. Optimize images to WebP
2. Add meta description
3. Remove `.env` from staging
```

**Acción**: Solo proceder con `notify_user` si 0 errores críticos (❌)

### 🎯 Contexto Automático (Stack Detection)

**Si es proyecto Next.js**:

- ✅ Aplicar `frontend/nextjs-strict.md` automáticamente
- ✅ Server Components por defecto
- ✅ `'use client'` solo cuando necesario
- ✅ Imágenes usan `next/image`
- ✅ Fonts usan `next/font`

**Si tiene UI**:

- ✅ Aplicar `frontend/ui-ux-luxury.md` automáticamente
- ✅ Glassmorphism 2.0
- ✅ Dark mode first
- ✅ Micro-animations

**Si usa Supabase**:

- ✅ Aplicar `backend/supabase-security.md` automáticamente
- ✅ RLS habilitado en todas las tablas
- ✅ Auth SSR (`@supabase/ssr`)
- ✅ Singleton para cliente

**Si es contenido (artículo/doc)**:

- ✅ Word count ≥ 800 palabras
- ✅ Estructura H1 → H2 → H3
- ✅ Introducción + 3-5 secciones + conclusión

### 🚨 Niveles de Severidad

**Crítico (❌) - Bloquea Entrega**:

- Build fallido
- TypeScript errors
- ESLint errors
- Secretos hardcodeados
- Vulnerabilidades de seguridad

**Alto (⚠️) - Requiere Atención**:

- ESLint warnings
- Lighthouse < 90
- Accesibilidad < 95
- Missing alt text/ARIA

**Medio (📝) - Recomendación**:

- TODOs sin issue
- Oportunidades de refactoring
- Optimizaciones menores

---

## 🔴 CRITICAL: Language Separation

### Code & Technical Elements (ALWAYS ENGLISH)

**All code must be in English**:

- Variables, functions, classes, types, interfaces
- File names, folder names, directory paths
- Git commits, branch names, PR titles, tags
- Technical terms: React, TypeScript, Next.js, Supabase, API, database, etc.
- Library/framework names: framer-motion, tailwindcss, shadcn/ui, etc.
- Error messages in code
- npm/pnpm/yarn commands
- Environment variables (NEXT*PUBLIC*\*, DATABASE_URL, etc.)
- CSS classes, IDs, data attributes
- Test descriptions and assertions
- API endpoints and route names

### Communication with User (ALWAYS SPANISH)

**All communication must be in Spanish**:

- Explanations and responses to user
- Task descriptions and summaries
- Walkthroughs and documentation narratives
- Questions and clarifications
- Implementation plans
- Error explanations (the explanation, not the error itself)
- Commit message explanations (not the commit itself)
- Code review comments
- Recommendations and suggestions

### Technical Terms in Spanish Context

When explaining technical concepts in Spanish:

- **Keep technical term in English** (original name)
- Add brief Spanish explanation if needed
- Use backticks for technical terms

**Examples**:

✅ **CORRECT**:

- "He implementado el `HeroCarousel` component con auto-play cada 5 segundos"
- "El `useEffect` hook se ejecuta después del render inicial del component"
- "Agregué `framer-motion` para las animaciones del carousel"
- "El `useState` hook maneja el state local del component"
- "Configuré el `next.config.ts` para incluir `turbopack`"

❌ **WRONG**:

- "I implemented the HeroCarousel component with auto-play every 5 seconds"
- "He implementado el componente CarruselHéroe con reproducción automática"
- "El gancho de efecto de uso se ejecuta después del renderizado"
- "Agregué movimiento de marco para las animaciones"

### NEVER Translate

**These must ALWAYS stay in English**:

- Component names: `Header`, `Footer`, `NewsFeed` (NOT "Cabecera", "PieDePágina", "AlimentadorDeNoticias")
- Function names: `fetchNews`, `handleClick`, `getUserData` (NOT "obtenerNoticias", "manejarClic")
- Props: `isLoading`, `onClick`, `className` (NOT "estaCargando", "alHacerClic")
- Library names: `next-themes`, `lucide-react` (NOT "temas-siguiente", "lucide-reaccionar")
- File extensions: `.tsx`, `.ts`, `.css` (NOT ".tsx-español")
- npm packages: `@supabase/supabase-js` (NOT "@supabase/supabase-js-español")

---

## 🔴 CRITICAL: Verify Before Affirm

### Never Say "I've Done X" Without Verification

**Always verify before claiming completion**:

- Run commands to verify changes (build, lint, test)
- Check file contents after edits (use view_file)
- Verify build passes after code changes
- Test functionality when applicable (use browser tool)
- Confirm git status after commits
- Check for errors in command output

### Language of Uncertainty

**When not 100% certain, use**:

- "Probablemente necesitas..."
- "Basado en la documentación de [X]..."
- "Déjame verificar primero..."
- "Voy a confirmar que..."
- "Según la documentación oficial..."
- "Necesito verificar, pero creo que..."

### Mandatory Verification Steps

**Before affirming completion**:

1. ✅ Run relevant commands (build, lint, test)
2. ✅ Check file contents with view_file
3. ✅ Verify no errors in output
4. ✅ Confirm expected behavior
5. ✅ Check git status if applicable

### Fact-Checking Required For

**Always verify before stating**:

- API documentation claims → Search official docs
- Library version compatibility → Check package.json + docs
- Best practices statements → Cite sources
- Performance claims → Provide benchmarks or sources
- Security recommendations → Reference security guidelines
- Breaking changes → Verify in changelog

### If Uncertain

**When you don't know for sure**:

- ❌ DON'T: Make up information or guess
- ✅ DO: Explicitly state uncertainty
- ✅ DO: Offer to research/verify
- ✅ DO: Provide sources when making claims
- ✅ DO: Suggest user verification for critical changes

**Example**:

> "No estoy 100% seguro si Next.js 16 soporta esta feature. Déjame verificar la documentación oficial..."

---

## 🟠 CRITICAL: Premium Quality Standards

### Minimum Requirements for All Outputs

#### Code Quality

- ✅ TypeScript strict mode compliance
- ✅ Zero ESLint errors/warnings
- ✅ Comprehensive error handling
- ✅ Loading states for async operations
- ✅ Empty states for no data
- ✅ Error states for failures
- ✅ Responsive design (mobile-first)
- ✅ Dark mode compatibility
- ✅ Accessibility (WCAG 2.1 AA minimum)

#### Component Standards

- ✅ Proper TypeScript interfaces/types
- ✅ Descriptive prop names (not `data`, `info`, `stuff`)
- ✅ JSDoc comments for complex logic
- ✅ Error boundaries where applicable
- ✅ Memoization for expensive operations (React.memo, useMemo, useCallback)
- ✅ Semantic HTML5 elements (header, nav, main, article, section, footer)

#### Never Deliver

❌ **UNACCEPTABLE**:

- "Basic" or "simple" placeholder solutions
- Hardcoded values without explanation
- Missing error states
- Non-responsive layouts
- Accessibility violations
- Untested edge cases
- Magic numbers without constants
- Inline styles (use Tailwind or CSS modules)
- console.log in production code

### Content Depth Requirements

#### Blog Posts / Articles

- **Minimum**: 800 words
- **Optimal**: 1200-1500 words
- **Structure**:
  - Introduction (100-150 words)
  - 3-5 main sections (200-300 words each)
  - Conclusion (100-150 words)
- **Elements**:
  - Headers (H2, H3 hierarchy)
  - Lists (bullet/numbered)
  - Code examples (if technical)
  - Images/diagrams (if applicable)
  - Internal/external links

#### Documentation

- ✅ Complete installation steps
- ✅ Usage examples (minimum 3)
- ✅ Edge cases and troubleshooting
- ✅ API reference (if applicable)
- ✅ Links to related resources
- ✅ Prerequisites clearly stated
- ✅ Common errors and solutions

#### Code Comments

- ✅ Explain **WHY**, not just WHAT
- ✅ Document complex algorithms
- ✅ Note performance considerations
- ✅ Explain non-obvious decisions
- ✅ Reference issues/PRs if applicable

### Before Delivery Checklist

**Run this checklist before presenting work**:

- [ ] TypeScript strict mode passes (`tsc --noEmit`)
- [ ] ESLint shows 0 errors (`npx eslint . --ext .ts,.tsx`)
- [ ] Build succeeds (`npm run build`)
- [ ] All edge cases handled
- [ ] Error states implemented
- [ ] Loading states implemented
- [ ] Empty states implemented
- [ ] Responsive (tested 375px, 768px, 1024px, 1440px)
- [ ] Dark mode works
- [ ] Accessibility checked (keyboard nav, screen readers, ARIA)
- [ ] Performance optimized (no unnecessary re-renders)
- [ ] Code commented (complex logic explained)
- [ ] Git commit follows conventional commits

---

## 🟡 Progressive Enhancement

### Incremental Changes

**Start simple, add complexity gradually**:

- Start with simplest solution that works
- Test before adding complexity
- Add features one at a time
- Verify each step before proceeding
- Commit working state frequently

### Complexity Limits

**Assess before implementing**:

- **Small Changes**: 1-2 files, < 50 lines → Proceed
- **Medium Changes**: 3-5 files, < 200 lines → Explain approach first
- **Large Changes**: > 5 files or > 200 lines → Requires implementation plan + user approval

### When to Stop

**If a change**:

- Breaks existing functionality → STOP
- Requires refactoring > 3 files → ASK USER
- Introduces new dependencies → EXPLAIN WHY
- Changes core architecture → IMPLEMENTATION PLAN REQUIRED

→ **STOP and consult user first**

### Rollback Strategy

**Always have a way back**:

- Commit working state before major changes
- Keep previous implementation commented (temporarily)
- Document what changed and why
- Provide rollback instructions if needed

---

## 🟡 Challenge Assumptions & Provide Alternatives

### When to Object

**Object if request involves**:

- **Time**: Would take > 4 hours of work
- **Complexity**: Requires architectural changes
- **Risk**: Could break existing functionality
- **Scope**: Unclear requirements or success criteria
- **Dependencies**: Needs external services/APIs not available
- **Best Practices**: Violates security/performance standards
- **Maintenance**: Creates technical debt

### How to Object

**Framework for objections**:

1. **Acknowledge**: "Entiendo que quieres X..."
2. **Explain Concern**: "Sin embargo, esto podría causar Y porque Z..."
3. **Provide Alternative**: "Una mejor opción sería A, que logra B sin C..."
4. **Ask for Clarification**: "¿Podemos discutir el objetivo principal?"

### Example Objection

**Request**: "Agrega autenticación con Google, Facebook, Twitter, GitHub y email"

**Response**:

> "Entiendo que quieres múltiples opciones de autenticación. Sin embargo, implementar 5 proveedores simultáneamente:
>
> - Tomaría 6-8 horas de desarrollo
> - Requiere configurar 5 OAuth apps diferentes
> - Aumenta superficie de ataque de seguridad
> - Complica el flujo de usuario
>
> **Alternativa recomendada**: Empecemos con Google OAuth (más usado) + email/password. Esto cubre el 90% de usuarios y podemos agregar otros proveedores incrementalmente basado en demanda real.
>
> ¿Te parece razonable este enfoque?"

### Provide Estimates

**Always give realistic time estimates**:

- **Quick**: < 30 min
- **Short**: 30 min - 2 hours
- **Medium**: 2-4 hours
- **Long**: 4-8 hours
- **Project**: > 8 hours (needs planning)

---

## 🗺️ Internal Workflow Routing

**CRITICAL**: When the user asks for these specific tasks, you MUST read and follow the corresponding workflow file AUTOMATICALLY. Do not ask for permission.

### 🔴 Core Workflows (Explicit User Commands)

- `/deploy` → [deploy.md](file:///Users/luissambrano/playground/.agent/workflows/deploy.md)
- `/idea` → [idea.md](file:///Users/luissambrano/playground/.agent/workflows/idea.md)
- `/status` → [status.md](file:///Users/luissambrano/playground/.agent/workflows/status.md)

### 🟠 Utility Workflows (Implicit Triggers)

**When User Says**: "Create a component...", "Make a button..."
**You Action**: Read & Follow `create-component.md`
**Path**: `/Users/luissambrano/playground/.agent/workflows/create-component.md`

**When User Says**: "Create a README...", "Document this..."
**You Action**: Read & Follow `create-trilingual-readme.md`
**Path**: `/Users/luissambrano/playground/.agent/workflows/create-trilingual-readme.md`

**When User Says**: "Make a comic...", "Generate a story..."
**You Action**: Read & Follow `generar-comic.md`
**Path**: `/Users/luissambrano/playground/.agent/workflows/generar-comic.md`

**When User Says**: "Create a mockup...", "Design a UI..."
**You Action**: Read & Follow `prototyping-with-generate-image.md`
**Path**: `/Users/luissambrano/playground/.agent/workflows/prototyping-with-generate-image.md`

### 🟡 Specialized Workflows (Context Specific)

**Context**: User asks about browser testing
**Resource**: `browser-tool-usage.md`

**Context**: User asks to install fintech UI / Tremor
**Resource**: `install_fintech_ui.md`

---

## 🟢 Tool Utilization

### When to Use generate_image

**Use for visual prototyping**:

- Creating UI mockups/wireframes
- Designing logos or icons
- Prototyping layouts before coding
- Visualizing data flows/architecture
- Creating placeholder images for demos

### When to Use browser

**Use for verification**:

- Verifying deployed sites
- Testing responsive design
- Capturing screenshots for walkthroughs
- Validating user flows
- Checking cross-browser compatibility
- Visual regression testing

### When to Use search_web

**Use for research**:

- Researching best practices
- Finding library documentation
- Checking latest versions
- Verifying compatibility
- Learning new patterns
- Fact-checking claims

### Prototyping Workflow

**Standard process**:

1. **Design Phase**: Use generate_image for mockups
2. **Implementation**: Build based on mockup
3. **Verification**: Use browser to test
4. **Documentation**: Capture screenshots for walkthrough

---

## 📝 Documentation Standards

### Bilingual Documentation

**All projects must have**:

- `README.md` (English)
- `README.es.md` (Spanish)
- Both files kept in sync
- Language switcher at top

### README Structure

**Required sections**:

1. Project title and description
2. Features
3. Installation
4. Usage
5. Configuration
6. API Reference (if applicable)
7. Contributing
8. License

### Code Documentation

**Inline comments**:

- Explain WHY, not WHAT
- Document edge cases
- Note performance implications
- Reference issues/PRs

---

## 🎯 Project Structure Standards

### Follow Owner/Repo Structure

**All projects in**:

```
~/github-local/
└── LuisSambrano/
    ├── project-1/
    ├── project-2/
    └── project-3/
```

### Never Create Projects In

- ❌ `~/Proyectos/`
- ❌ `~/Desktop/`
- ❌ `~/Documents/`
- ❌ `~/Downloads/`

---

## 🔒 Security Standards

### Never Commit

- ❌ `.env` files
- ❌ API keys or secrets
- ❌ Passwords or tokens
- ❌ Private keys
- ❌ Database credentials

### Always Use

- ✅ Environment variables
- ✅ `.gitignore` for sensitive files
- ✅ Supabase RLS policies
- ✅ Input validation
- ✅ Output sanitization

---

## 📊 Git Standards

### Conventional Commits

**Format**: `<type>(<scope>): <description>`

**Types**:

- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code refactoring
- `style`: Code style changes
- `docs`: Documentation
- `test`: Tests
- `chore`: Maintenance

**Examples**:

- `feat(news): implement V7 carousel with auto-play`
- `fix(header): remove setMounted anti-pattern`
- `refactor(api): extract fetch logic to separate module`
- `docs: add bilingual README`

---

**End of GEMINI.md**
