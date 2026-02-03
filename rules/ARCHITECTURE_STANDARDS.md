# 🏗️ Estándares de Arquitectura Antigravity

**Versión**: 1.0.0  
**Estado**: OBLIGATORIO  
**Nivel**: 1 (Arquitectura)

---

## 🎯 Propósito

Este documento define la **estructura de directorios obligatoria**, **convenciones de naming** y **patrones arquitectónicos** que todos los proyectos Antigravity deben seguir.

---

## 📁 Estructura de Directorios Obligatoria

### Para Proyectos Next.js (App Router)

```
proyecto/
├── .agent/                          # ← OBLIGATORIO
│   ├── rules/                       # Reglas específicas del proyecto
│   │   ├── architecture.md          # Arquitectura del proyecto
│   │   ├── workspace-standards.md   # Copiado de antigravity-config
│   │   ├── nextjs-strict.md         # Si es Next.js
│   │   ├── ui-ux-luxury.md          # Si tiene UI
│   │   └── supabase-security.md     # Si usa Supabase
│   ├── workflows/                   # Flujos automatizables
│   │   ├── auto-qa.md               # QA antes de entregar
│   │   ├── deploy.md                # Deployment
│   │   └── create-component.md      # Crear componentes
│   └── templates/                   # Plantillas del proyecto
│       ├── component-template.tsx   # Template de componente
│       └── api-route-template.ts    # Template de API route
├── app/                             # Next.js App Router
│   ├── (auth)/                      # Grupo de rutas: autenticación
│   │   ├── login/
│   │   ├── register/
│   │   └── layout.tsx
│   ├── (dashboard)/                 # Grupo de rutas: dashboard
│   │   ├── profile/
│   │   ├── settings/
│   │   └── layout.tsx
│   ├── (public)/                    # Grupo de rutas: público
│   │   ├── about/
│   │   ├── contact/
│   │   └── layout.tsx
│   ├── api/                         # API routes
│   │   ├── auth/
│   │   ├── users/
│   │   └── articles/
│   ├── layout.tsx                   # Root layout
│   ├── page.tsx                     # Home page
│   ├── error.tsx                    # Error boundary
│   ├── loading.tsx                  # Loading UI
│   └── not-found.tsx                # 404 page
├── components/                      # Componentes React
│   ├── ui/                          # Componentes base (shadcn/ui)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── input.tsx
│   ├── features/                    # Componentes de features
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   └── RegisterForm.tsx
│   │   └── articles/
│   │       ├── ArticleCard.tsx
│   │       └── ArticleList.tsx
│   └── layouts/                     # Layouts reutilizables
│       ├── Header.tsx
│       ├── Footer.tsx
│       └── Sidebar.tsx
├── lib/                             # Utilidades y configuración
│   ├── supabase/                    # Cliente Supabase
│   │   ├── client.ts                # Cliente browser
│   │   ├── server.ts                # Cliente server
│   │   └── middleware.ts            # Middleware auth
│   ├── utils/                       # Utilidades generales
│   │   ├── cn.ts                    # Class name merger
│   │   ├── date.ts                  # Formateo de fechas
│   │   └── validation.ts            # Validación
│   ├── hooks/                       # Custom hooks
│   │   ├── useAuth.ts
│   │   ├── useArticles.ts
│   │   └── useDebounce.ts
│   └── constants/                   # Constantes
│       ├── routes.ts
│       └── config.ts
├── types/                           # TypeScript types
│   ├── database.types.ts            # Tipos generados de Supabase
│   ├── user.types.ts
│   └── article.types.ts
├── public/                          # Assets estáticos
│   ├── images/
│   ├── icons/
│   └── fonts/
├── .env.local                       # Variables de entorno (NO COMMITEAR)
├── .env.example                     # Ejemplo de variables (SÍ COMMITEAR)
├── .gitignore
├── next.config.ts                   # Configuración Next.js
├── tailwind.config.ts               # Configuración Tailwind
├── tsconfig.json                    # Configuración TypeScript
├── package.json
├── README.md                        # ← OBLIGATORIO (Inglés)
├── README.es.md                     # ← OBLIGATORIO (Español)
└── CHANGELOG.md                     # Historial de cambios
```

---

## 🏷️ Convenciones de Naming

### Archivos

| Tipo                  | Convención                | Ejemplo                  |
| --------------------- | ------------------------- | ------------------------ |
| **Componentes React** | `PascalCase.tsx`          | `ArticleCard.tsx`        |
| **Páginas Next.js**   | `page.tsx`, `layout.tsx`  | `app/about/page.tsx`     |
| **API Routes**        | `route.ts`                | `app/api/users/route.ts` |
| **Utilidades**        | `camelCase.ts`            | `formatDate.ts`          |
| **Hooks**             | `use*.ts`                 | `useAuth.ts`             |
| **Types**             | `*.types.ts`              | `user.types.ts`          |
| **Constants**         | `*.constants.ts`          | `routes.constants.ts`    |
| **Config**            | `*.config.ts`             | `next.config.ts`         |
| **Tests**             | `*.test.ts` o `*.spec.ts` | `ArticleCard.test.tsx`   |

### Carpetas

| Tipo                      | Convención     | Ejemplo                               |
| ------------------------- | -------------- | ------------------------------------- |
| **Rutas Next.js**         | `kebab-case`   | `app/user-profile/`                   |
| **Grupos de rutas**       | `(kebab-case)` | `app/(dashboard)/`                    |
| **Componentes agrupados** | `PascalCase`   | `components/ArticleList/`             |
| **Utilidades**            | `camelCase`    | `lib/utils/`                          |
| **Features**              | `kebab-case`   | `components/features/article-editor/` |

### Variables y Funciones

| Tipo            | Convención                   | Ejemplo                                        |
| --------------- | ---------------------------- | ---------------------------------------------- |
| **Variables**   | `camelCase`                  | `const userName = 'Luis';`                     |
| **Constantes**  | `SCREAMING_SNAKE_CASE`       | `const MAX_RETRIES = 3;`                       |
| **Funciones**   | `camelCase` (verbo)          | `function fetchUser() {}`                      |
| **Componentes** | `PascalCase`                 | `function ArticleCard() {}`                    |
| **Clases**      | `PascalCase`                 | `class UserService {}`                         |
| **Interfaces**  | `PascalCase` (sin prefijo I) | `interface User {}`                            |
| **Types**       | `PascalCase`                 | `type ArticleStatus = 'draft' \| 'published';` |
| **Enums**       | `PascalCase`                 | `enum Role { Admin, User }`                    |
| **Privadas**    | `_prefijo`                   | `const _internalCache = {};`                   |
| **Booleanos**   | `is*`, `has*`, `can*`        | `const isLoading = true;`                      |
| **Handlers**    | `handle*`                    | `const handleClick = () => {};`                |
| **Callbacks**   | `on*`                        | `const onSuccess = () => {};`                  |

---

## 🏛️ Patrones Arquitectónicos Obligatorios

### 1. Singleton para Clientes (Supabase, APIs)

**Problema**: Crear múltiples instancias de clientes causa memory leaks y conexiones innecesarias.

**Solución**: Patrón Singleton.

```typescript
// ✅ CORRECTO: lib/supabase/client.ts
import { createClient, SupabaseClient } from "@supabase/supabase-js";
import type { Database } from "@/types/database.types";

let supabaseClient: SupabaseClient<Database> | null = null;

export function getSupabaseClient(): SupabaseClient<Database> {
  if (!supabaseClient) {
    const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
    const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;

    supabaseClient = createClient<Database>(supabaseUrl, supabaseKey);
  }

  return supabaseClient;
}

// Uso
import { getSupabaseClient } from "@/lib/supabase/client";

const supabase = getSupabaseClient();
```

```typescript
// ❌ INCORRECTO: Crear nueva instancia cada vez
import { createClient } from "@supabase/supabase-js";

// Esto crea una nueva conexión en cada llamada
export const supabase = createClient(url, key);
```

---

### 2. Server Components por Defecto

**Filosofía**: Next.js App Router usa Server Components por defecto. Solo usar Client Components cuando sea necesario.

**Cuándo usar Client Components**:

- ✅ Necesitas hooks (`useState`, `useEffect`, `useContext`)
- ✅ Necesitas event handlers (`onClick`, `onChange`)
- ✅ Necesitas browser APIs (`window`, `localStorage`)
- ✅ Necesitas librerías client-only (framer-motion, react-hot-toast)

**Cuándo usar Server Components**:

- ✅ Fetching de datos
- ✅ Acceso directo a backend
- ✅ Renderizado de contenido estático
- ✅ SEO crítico

```tsx
// ✅ CORRECTO: Server Component (por defecto)
// app/articles/page.tsx
import { getSupabaseServer } from "@/lib/supabase/server";
import { ArticleCard } from "@/components/features/articles/ArticleCard";

export default async function ArticlesPage() {
  const supabase = getSupabaseServer();
  const { data: articles } = await supabase
    .from("articles")
    .select("*")
    .eq("status", "published");

  return (
    <div>
      {articles?.map((article) => (
        <ArticleCard key={article.id} article={article} />
      ))}
    </div>
  );
}
```

```tsx
// ✅ CORRECTO: Client Component (cuando es necesario)
// components/features/articles/ArticleCard.tsx
"use client";

import { useState } from "react";
import { motion } from "framer-motion";

export function ArticleCard({ article }) {
  const [isLiked, setIsLiked] = useState(false);

  return (
    <motion.div whileHover={{ scale: 1.02 }}>
      <button onClick={() => setIsLiked(!isLiked)}>
        {isLiked ? "❤️" : "🤍"}
      </button>
    </motion.div>
  );
}
```

---

### 3. Separación de Concerns (UI vs Lógica)

**Filosofía**: Los componentes UI deben ser tontos. La lógica de negocio va en hooks, services o server actions.

```tsx
// ✅ CORRECTO: Lógica separada en hook
// lib/hooks/useArticles.ts
export function useArticles() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    async function fetchArticles() {
      try {
        const supabase = getSupabaseClient();
        const { data, error } = await supabase
          .from("articles")
          .select("*")
          .eq("status", "published");

        if (error) throw error;
        setArticles(data);
      } catch (err) {
        setError(err as Error);
      } finally {
        setIsLoading(false);
      }
    }

    fetchArticles();
  }, []);

  return { articles, isLoading, error };
}

// components/features/articles/ArticleList.tsx
("use client");

import { useArticles } from "@/lib/hooks/useArticles";
import { ArticleCard } from "./ArticleCard";

export function ArticleList() {
  const { articles, isLoading, error } = useArticles();

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {articles.map((article) => (
        <ArticleCard key={article.id} article={article} />
      ))}
    </div>
  );
}
```

```tsx
// ❌ INCORRECTO: Lógica mezclada en componente
export function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Lógica de negocio directamente en el componente
    const supabase = createClient(url, key);
    supabase
      .from("articles")
      .select("*")
      .then(({ data }) => {
        setArticles(data);
        setIsLoading(false);
      });
  }, []);

  // Renderizado mezclado con lógica
  return isLoading ? (
    <div>Loading...</div>
  ) : (
    <div>
      {articles.map((a) => (
        <div>{a.title}</div>
      ))}
    </div>
  );
}
```

---

### 4. Composición sobre Herencia

**Filosofía**: Preferir composición de componentes sobre herencia de clases.

```tsx
// ✅ CORRECTO: Composición
interface CardProps {
  children: React.ReactNode;
  variant?: "default" | "outlined" | "elevated";
}

export function Card({ children, variant = "default" }: CardProps) {
  return (
    <div className={cn("rounded-lg", variantStyles[variant])}>{children}</div>
  );
}

export function CardHeader({ children }: { children: React.ReactNode }) {
  return <div className="p-4 border-b">{children}</div>;
}

export function CardContent({ children }: { children: React.ReactNode }) {
  return <div className="p-4">{children}</div>;
}

// Uso
<Card variant="elevated">
  <CardHeader>
    <h2>Title</h2>
  </CardHeader>
  <CardContent>
    <p>Content</p>
  </CardContent>
</Card>;
```

---

### 5. Error Boundaries

**Filosofía**: Cada feature debe tener su propio error boundary.

```tsx
// ✅ CORRECTO: Error boundary por feature
// app/(dashboard)/articles/error.tsx
"use client";

export default function ArticlesError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <h2 className="text-2xl font-bold mb-4">Error al cargar artículos</h2>
      <p className="text-muted-foreground mb-4">{error.message}</p>
      <button onClick={reset} className="btn-primary">
        Intentar de nuevo
      </button>
    </div>
  );
}
```

---

## 🗂️ Organización por Features

**Filosofía**: Agrupar código por feature, no por tipo de archivo.

```
// ✅ CORRECTO: Por feature
components/
└── features/
    ├── auth/
    │   ├── LoginForm.tsx
    │   ├── RegisterForm.tsx
    │   ├── useAuth.ts
    │   └── auth.types.ts
    └── articles/
        ├── ArticleCard.tsx
        ├── ArticleList.tsx
        ├── ArticleEditor.tsx
        ├── useArticles.ts
        └── article.types.ts

// ❌ INCORRECTO: Por tipo
components/
├── forms/
│   ├── LoginForm.tsx
│   └── ArticleForm.tsx
├── cards/
│   └── ArticleCard.tsx
└── lists/
    └── ArticleList.tsx
```

---

## 📦 Barrel Exports

**Filosofía**: Usar `index.ts` para exportar públicamente.

```typescript
// ✅ CORRECTO: components/ui/index.ts
export { Button } from "./button";
export { Card, CardHeader, CardContent } from "./card";
export { Dialog } from "./dialog";

// Uso
import { Button, Card, Dialog } from "@/components/ui";
```

```typescript
// ❌ INCORRECTO: Imports individuales
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Dialog } from "@/components/ui/dialog";
```

---

## 🔐 Variables de Entorno

**Estructura Obligatoria**:

```bash
# .env.example (SÍ COMMITEAR)
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# App
NEXT_PUBLIC_APP_URL=http://localhost:3000
NODE_ENV=development

# Analytics (opcional)
NEXT_PUBLIC_GA_ID=
```

```bash
# .env.local (NO COMMITEAR)
# Valores reales
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGc...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGc...
```

**Convenciones**:

- ✅ `NEXT_PUBLIC_*` para variables accesibles en el cliente
- ✅ Sin prefijo para variables solo del servidor
- ✅ `.env.example` con valores de ejemplo (commitear)
- ✅ `.env.local` con valores reales (NO commitear)
- ❌ Nunca hardcodear secretos en el código

---

## 📚 Referencias

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md) - Nivel 0
- [CODE_STANDARDS.md](./CODE_STANDARDS.md) - Nivel 2
- [QUALITY_GATES.md](./QUALITY_GATES.md) - Nivel 3

---

**Última Actualización**: 2026-02-03  
**Mantenedor**: Luis Sambrano  
**Estado**: ACTIVO
