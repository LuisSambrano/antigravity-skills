# 🌌 PROTOCOL ZERO: Filosofía de Antigravity

**Versión**: 1.0.0  
**Estado**: INMUTABLE  
**Nivel**: 0 (Fundacional)

---

## 🎯 Propósito

Este documento define los **principios fundamentales** y **valores no negociables** del ecosistema Antigravity. Todas las decisiones técnicas, arquitectónicas y operativas deben alinearse con estos principios.

---

## 🧬 Principios Fundamentales

### 1. Playground es la Fuente de Verdad

**Filosofía**: El entorno local (`~/playground`) es el origen de toda la verdad. GitHub es solo un espejo en la nube.

**Implicaciones**:

- ✅ Todos los cambios se originan localmente
- ✅ La sincronización es unidireccional: `Local → GitHub`
- ✅ Los nombres de directorios locales son autoritativos
- ✅ GitHub se adapta al local, nunca al revés
- ❌ Nunca editar directamente en GitHub (excepto emergencias)
- ❌ Nunca renombrar localmente para coincidir con GitHub

**Ejemplo**:

```bash
# ✅ CORRECTO
cd ~/playground/repos/LuisSambrano/mi-proyecto
# Hacer cambios localmente
git push origin main

# ❌ INCORRECTO
# Editar en GitHub Web UI
# Hacer pull para sincronizar
```

---

### 2. Calidad sobre Velocidad

**Filosofía**: Nunca sacrificar calidad por rapidez. El código roto no se sube.

**Implicaciones**:

- ✅ Tests pasan antes de commit
- ✅ Build exitoso antes de push
- ✅ Lint sin errores antes de commit
- ✅ TypeScript strict mode siempre
- ✅ Code review (aunque sea auto-review)
- ❌ "Lo arreglo después" (no existe)
- ❌ Commits con TODOs sin issue
- ❌ Código comentado sin razón

**Checklist Pre-Commit**:

```bash
npm run build  # ✅ Debe pasar
npm run lint   # ✅ 0 errores
tsc --noEmit   # ✅ 0 errores de tipos
```

---

### 3. Documentación como Código

**Filosofía**: Todo debe estar documentado. La documentación es tan importante como el código.

**Implicaciones**:

- ✅ README bilingüe (EN + ES) obligatorio
- ✅ Arquitectura visible en diagramas Mermaid
- ✅ Comentarios explican el "por qué", no el "qué"
- ✅ CHANGELOG.md actualizado en cada release
- ✅ API pública documentada con JSDoc
- ❌ Código sin README
- ❌ Funciones públicas sin documentación
- ❌ Cambios breaking sin documentar

**Ejemplo**:

```typescript
/**
 * Fetches user data from Supabase with caching.
 *
 * Uses a 5-minute cache to reduce API calls and improve performance.
 * Cache is invalidated on user updates via Supabase realtime.
 *
 * @param userId - The UUID of the user to fetch
 * @returns User object or null if not found
 * @throws {Error} If Supabase client is not initialized
 */
export async function fetchUser(userId: string): Promise<User | null> {
  // Implementation
}
```

---

### 4. Autonomía con Responsabilidad

**Filosofía**: Los agentes (humanos o IA) tienen libertad de decisión, pero deben seguir el protocolo y ser transparentes.

**Implicaciones**:

- ✅ Libertad para elegir implementación
- ✅ Obligación de seguir estándares
- ✅ Transparencia total en acciones
- ✅ Documentar decisiones no obvias
- ✅ Pedir clarificación si hay ambigüedad
- ❌ Desviarse del protocolo sin justificación
- ❌ Cambios silenciosos sin documentar
- ❌ Asumir sin preguntar

**Ejemplo de Transparencia**:

```markdown
## Decisión: Usar Zustand en lugar de Context API

**Razón**: El estado global es complejo (>5 slices) y Context API
causaría re-renders innecesarios. Zustand ofrece mejor performance
y developer experience.

**Alternativas Consideradas**:

- Context API: Descartado por performance
- Redux Toolkit: Demasiado boilerplate para este caso
- Jotai: Menos maduro que Zustand

**Fecha**: 2026-02-03
**Autor**: Luis Sambrano
```

---

### 5. Mejora Continua (Kaizen)

**Filosofía**: Cada sesión debe dejar el código mejor que como lo encontró. Refactoring incremental constante.

**Implicaciones**:

- ✅ Refactorizar al tocar código legacy
- ✅ Mejorar tests al encontrar bugs
- ✅ Actualizar documentación al cambiar API
- ✅ Documentar aprendizajes en TIL
- ✅ Simplificar complejidad innecesaria
- ❌ "Si funciona, no lo toques"
- ❌ Dejar código peor que antes
- ❌ Ignorar code smells

**Boy Scout Rule**:

> "Deja el código más limpio de lo que lo encontraste"

---

## 🔒 Valores No Negociables

### 1. Seguridad First

**Mandatorio**:

- ✅ Row Level Security (RLS) en todas las tablas Supabase
- ✅ Validación de entrada (nunca confiar en el cliente)
- ✅ Sanitización de salida (prevenir XSS)
- ✅ Variables de entorno para secretos
- ✅ HTTPS en producción
- ❌ Secretos hardcodeados
- ❌ SQL injection vulnerable
- ❌ Autenticación sin rate limiting

**Ejemplo RLS**:

```sql
-- ✅ CORRECTO: RLS habilitado
ALTER TABLE articles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can only read published articles"
ON articles FOR SELECT
USING (status = 'published' OR auth.uid() = author_id);

-- ❌ INCORRECTO: Sin RLS
-- Tabla sin políticas = acceso total
```

---

### 2. Accesibilidad (A11y)

**Mandatorio**:

- ✅ WCAG 2.1 AA mínimo
- ✅ Contraste de colores adecuado (4.5:1 texto, 3:1 UI)
- ✅ Navegación por teclado 100%
- ✅ Screen reader compatible
- ✅ ARIA labels donde sea necesario
- ❌ Elementos sin texto alternativo
- ❌ Botones sin labels
- ❌ Formularios sin labels

**Ejemplo**:

```tsx
// ✅ CORRECTO
<button
  aria-label="Close dialog"
  onClick={handleClose}
>
  <X className="h-4 w-4" />
</button>

// ❌ INCORRECTO
<button onClick={handleClose}>
  <X className="h-4 w-4" />
</button>
```

---

### 3. Performance

**Mandatorio**:

- ✅ Core Web Vitals en verde
  - LCP (Largest Contentful Paint): < 2.5s
  - FID (First Input Delay): < 100ms
  - CLS (Cumulative Layout Shift): < 0.1
- ✅ Lighthouse Performance: > 90
- ✅ Bundle size optimizado (code splitting)
- ✅ Imágenes optimizadas (WebP, lazy loading)
- ❌ Bundles > 500KB sin justificación
- ❌ Imágenes sin optimizar
- ❌ Re-renders innecesarios

**Ejemplo**:

```tsx
// ✅ CORRECTO: Lazy loading
import dynamic from "next/dynamic";

const HeavyComponent = dynamic(() => import("./HeavyComponent"), {
  loading: () => <Skeleton />,
  ssr: false,
});

// ❌ INCORRECTO: Todo en el bundle inicial
import { HeavyComponent } from "./HeavyComponent";
```

---

### 4. Mantenibilidad

**Mandatorio**:

- ✅ Código auto-explicativo (nombres descriptivos)
- ✅ Funciones pequeñas (< 50 líneas)
- ✅ Separación de concerns (UI vs lógica)
- ✅ DRY (Don't Repeat Yourself)
- ✅ Consistencia en naming y estructura
- ❌ Funciones > 100 líneas
- ❌ Lógica de negocio en componentes UI
- ❌ Copy-paste de código

**Ejemplo**:

```typescript
// ✅ CORRECTO: Código auto-explicativo
function calculateDiscountedPrice(
  originalPrice: number,
  discountPercentage: number,
): number {
  const discountAmount = originalPrice * (discountPercentage / 100);
  return originalPrice - discountAmount;
}

// ❌ INCORRECTO: Nombres crípticos
function calc(p: number, d: number): number {
  return p - p * (d / 100);
}
```

---

### 5. Escalabilidad

**Mandatorio**:

- ✅ Arquitectura modular (features independientes)
- ✅ Separación frontend/backend clara
- ✅ API versionada (v1, v2)
- ✅ Database indexing apropiado
- ✅ Caching estratégico
- ❌ Monolitos acoplados
- ❌ Queries N+1
- ❌ Sin paginación en listas grandes

**Ejemplo**:

```typescript
// ✅ CORRECTO: Modular
app/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── api/
│   └── articles/
│       ├── components/
│       ├── hooks/
│       └── api/

// ❌ INCORRECTO: Todo mezclado
app/
├── components/
│   ├── LoginForm.tsx
│   ├── ArticleCard.tsx
│   └── UserProfile.tsx
```

---

## 🚨 Violaciones del Protocolo

### Severidad Crítica (Bloquea Deploy)

- Código sin tests que pasan
- Build fallido
- Secretos hardcodeados
- Vulnerabilidades de seguridad
- RLS deshabilitado en producción

### Severidad Alta (Requiere Fix Inmediato)

- Lint errors
- TypeScript errors
- Performance < 70 en Lighthouse
- Accesibilidad < 90 en Lighthouse
- Código duplicado > 10%

### Severidad Media (Fix en Próximo Sprint)

- Comentarios desactualizados
- TODOs sin issue
- Funciones > 50 líneas
- Falta de documentación

### Severidad Baja (Nice to Have)

- Nombres de variables mejorables
- Oportunidades de refactoring
- Optimizaciones menores

---

## 📚 Referencias

- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md) - Nivel 1
- [CODE_STANDARDS.md](./CODE_STANDARDS.md) - Nivel 2
- [QUALITY_GATES.md](./QUALITY_GATES.md) - Nivel 3
- [Workflows](../workflows/) - Nivel 4

---

**Última Actualización**: 2026-02-03  
**Mantenedor**: Luis Sambrano  
**Estado**: ACTIVO
