# 💻 Estándares de Código Antigravity

**Versión**: 1.0.0  
**Estado**: OBLIGATORIO  
**Nivel**: 1 (Código - Transversal)

---

## 🎯 Propósito

Este documento define los **estándares de código obligatorios** para todos los proyectos Antigravity. Estas reglas son **transversales** (aplican a frontend Y backend) y se aplican **automáticamente** en cada interacción.

---

## 📘 TypeScript Standards

### Configuración Obligatoria

**Archivo**: `tsconfig.json`

```json
{
  "compilerOptions": {
    "strict": true, // ← OBLIGATORIO
    "noUncheckedIndexedAccess": true, // ← OBLIGATORIO
    "noImplicitReturns": true, // ← OBLIGATORIO
    "noFallthroughCasesInSwitch": true, // ← OBLIGATORIO
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

**Verificación Automática**:

```bash
# Antes de cada commit
tsc --noEmit
```

---

### Reglas de Tipado

#### 1. Nunca usar `any`

```typescript
// ❌ INCORRECTO
function processData(data: any) {
  return data.value;
}

// ✅ CORRECTO: Usar unknown y type guard
function processData(data: unknown) {
  if (typeof data === "object" && data !== null && "value" in data) {
    return (data as { value: string }).value;
  }
  throw new Error("Invalid data structure");
}

// ✅ MEJOR: Definir tipo explícito
interface DataStructure {
  value: string;
}

function processData(data: DataStructure) {
  return data.value;
}
```

---

#### 2. Interfaces vs Types

**Regla**: Usar `interface` para objetos públicos, `type` para uniones/intersecciones.

```typescript
// ✅ CORRECTO: Interface para objetos
export interface User {
  id: string;
  name: string;
  email: string;
}

// ✅ CORRECTO: Type para uniones
export type Status = "draft" | "published" | "archived";

// ✅ CORRECTO: Type para intersecciones
export type AuthenticatedUser = User & {
  token: string;
  expiresAt: Date;
};

// ❌ INCORRECTO: Type para objeto simple
export type User = {
  id: string;
  name: string;
};
```

---

#### 3. Genéricos Descriptivos

```typescript
// ❌ INCORRECTO: Nombres crípticos
function map<T, U>(arr: T[], fn: (item: T) => U): U[] {
  return arr.map(fn);
}

// ✅ CORRECTO: Nombres descriptivos
function mapArray<TInput, TOutput>(
  array: TInput[],
  transformFn: (item: TInput) => TOutput,
): TOutput[] {
  return array.map(transformFn);
}

// ✅ MEJOR: Usar nombres de dominio
function transformArticles<TArticle extends Article, TViewModel>(
  articles: TArticle[],
  toViewModel: (article: TArticle) => TViewModel,
): TViewModel[] {
  return articles.map(toViewModel);
}
```

---

#### 4. Null vs Undefined

**Regla**: Preferir `null` para valores ausentes intencionales, `undefined` para valores no inicializados.

```typescript
// ✅ CORRECTO
interface User {
  id: string;
  name: string;
  avatar: string | null; // Puede no tener avatar (intencional)
  bio?: string; // Puede no estar definido (opcional)
}

// ❌ INCORRECTO: Mezclar null y undefined sin razón
interface User {
  avatar: string | null | undefined; // Confuso
}
```

---

## 💬 Comment Standards

### Cuándo Comentar

**Regla**: Comentar el **POR QUÉ**, no el **QUÉ**.

```typescript
// ❌ INCORRECTO: Comenta el QUÉ (obvio)
// Incrementa el contador en 1
count++;

// ✅ CORRECTO: Comenta el POR QUÉ (no obvio)
// Incrementamos el contador aquí en lugar de en el useEffect
// para evitar re-renders innecesarios cuando el usuario hace scroll
count++;
```

---

### Formato de Comentarios

#### 1. Comentarios de Línea

```typescript
// ✅ CORRECTO: Comentario arriba de la línea
// Cache de 5 minutos para reducir llamadas a la API
const CACHE_DURATION = 5 * 60 * 1000;

// ❌ INCORRECTO: Comentario al lado (dificulta lectura)
const CACHE_DURATION = 5 * 60 * 1000; // Cache de 5 minutos
```

---

#### 2. Comentarios de Bloque

```typescript
// ✅ CORRECTO: Explicar decisiones complejas
/**
 * Usamos un Map en lugar de un objeto porque:
 * 1. Necesitamos claves que no sean strings (UUIDs)
 * 2. Map preserva el orden de inserción
 * 3. Map tiene mejor performance para add/delete frecuente
 */
const userCache = new Map<string, User>();
```

---

#### 3. JSDoc para Funciones Públicas

````typescript
// ✅ OBLIGATORIO para funciones exportadas
/**
 * Fetches user data from Supabase with caching.
 *
 * Uses a 5-minute cache to reduce API calls and improve performance.
 * Cache is invalidated on user updates via Supabase realtime.
 *
 * @param userId - The UUID of the user to fetch
 * @returns User object or null if not found
 * @throws {Error} If Supabase client is not initialized
 *
 * @example
 * ```typescript
 * const user = await fetchUser('123e4567-e89b-12d3-a456-426614174000');
 * if (user) {
 *   console.log(user.name);
 * }
 * ```
 */
export async function fetchUser(userId: string): Promise<User | null> {
  // Implementation
}
````

---

### Comentarios en Español (Código Interno)

**Regla**: Código en inglés, comentarios complejos en español si ayuda a la claridad.

```typescript
// ✅ CORRECTO: Términos técnicos en inglés, explicación en español
/**
 * Implementa el patrón Singleton para el cliente de Supabase.
 *
 * Razón: Crear múltiples instancias causa memory leaks y conexiones
 * innecesarias. Este patrón garantiza una sola instancia compartida.
 */
let supabaseClient: SupabaseClient | null = null;

export function getSupabaseClient(): SupabaseClient {
  if (!supabaseClient) {
    supabaseClient = createClient(url, key);
  }
  return supabaseClient;
}
```

---

## 📦 Import Standards

### Orden Obligatorio

```typescript
// 1. React (si aplica)
import React, { useState, useEffect } from "react";
import type { FC, ReactNode } from "react";

// 2. Librerías externas (alfabético)
import { motion } from "framer-motion";
import { createClient } from "@supabase/supabase-js";
import { z } from "zod";

// 3. Imports internos (alfabético)
import { Button } from "@/components/ui/button";
import { useAuth } from "@/lib/hooks/useAuth";
import { cn } from "@/lib/utils/cn";

// 4. Types (separados)
import type { User } from "@/types/user.types";
import type { Article } from "@/types/article.types";

// 5. Estilos (último)
import "./styles.css";
```

---

### Barrel Exports

**Regla**: Usar `index.ts` para exportar públicamente.

```typescript
// ✅ CORRECTO: components/ui/index.ts
export { Button } from "./button";
export { Card, CardHeader, CardContent } from "./card";
export { Dialog } from "./dialog";
export { Input } from "./input";

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

### Imports Dinámicos

**Regla**: Usar `dynamic` de Next.js para componentes pesados.

```typescript
// ✅ CORRECTO: Lazy loading de componente pesado
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <Skeleton className="h-[400px]" />,
  ssr: false
});

// ❌ INCORRECTO: Import estático de componente pesado
import { HeavyChart } from './HeavyChart';
```

---

## 🔧 Function Standards

### Naming Conventions

```typescript
// ✅ CORRECTO: Verbos para funciones
function fetchUser() {}
function createArticle() {}
function deleteComment() {}

// ✅ CORRECTO: Prefijos para booleanos
function isAuthenticated() {}
function hasPermission() {}
function canEdit() {}

// ✅ CORRECTO: Prefijos para handlers
function handleClick() {}
function handleSubmit() {}
function handleChange() {}

// ✅ CORRECTO: Prefijos para callbacks
function onSuccess() {}
function onError() {}
function onComplete() {}

// ❌ INCORRECTO: Nombres ambiguos
function user() {} // ¿Qué hace? ¿Get? ¿Create?
function data() {} // Muy genérico
```

---

### Tamaño de Funciones

**Regla**: Máximo 50 líneas por función. Si es más larga, dividir.

```typescript
// ❌ INCORRECTO: Función de 100+ líneas
function processArticle(article: Article) {
  // 100 líneas de lógica mezclada
}

// ✅ CORRECTO: Dividir en funciones pequeñas
function processArticle(article: Article) {
  const validated = validateArticle(article);
  const enriched = enrichMetadata(validated);
  const published = publishToDatabase(enriched);
  return published;
}

function validateArticle(article: Article) {
  // 10-15 líneas
}

function enrichMetadata(article: Article) {
  // 10-15 líneas
}

function publishToDatabase(article: Article) {
  // 10-15 líneas
}
```

---

### Una Responsabilidad por Función

```typescript
// ❌ INCORRECTO: Función hace demasiado
function saveUserAndSendEmail(user: User) {
  // Guarda en DB
  database.save(user);

  // Envía email
  emailService.send(user.email, "Welcome!");

  // Actualiza analytics
  analytics.track("user_created", user.id);
}

// ✅ CORRECTO: Una responsabilidad por función
function saveUser(user: User) {
  return database.save(user);
}

function sendWelcomeEmail(user: User) {
  return emailService.send(user.email, "Welcome!");
}

function trackUserCreation(userId: string) {
  return analytics.track("user_created", userId);
}

// Composición
async function registerUser(user: User) {
  const savedUser = await saveUser(user);
  await sendWelcomeEmail(savedUser);
  await trackUserCreation(savedUser.id);
  return savedUser;
}
```

---

## 🚨 Error Handling

### Try-Catch Obligatorio

**Regla**: Toda operación asíncrona debe tener try-catch.

```typescript
// ❌ INCORRECTO: Sin error handling
async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// ✅ CORRECTO: Con try-catch
async function fetchUser(id: string): Promise<User | null> {
  try {
    const response = await fetch(`/api/users/${id}`);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Error fetching user:", error);
    return null;
  }
}
```

---

### Logging de Errores

```typescript
// ✅ CORRECTO: Log con contexto
try {
  await processPayment(orderId);
} catch (error) {
  console.error("Payment processing failed:", {
    orderId,
    error: error instanceof Error ? error.message : "Unknown error",
    timestamp: new Date().toISOString(),
  });
  throw error; // Re-throw si es crítico
}
```

---

### Return de Errores (No Throw en Producción)

```typescript
// ✅ CORRECTO: Return de errores en lugar de throw
type Result<T> = { success: true; data: T } | { success: false; error: string };

async function fetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await database.users.findById(id);

    if (!user) {
      return { success: false, error: "User not found" };
    }

    return { success: true, data: user };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error.message : "Unknown error",
    };
  }
}

// Uso
const result = await fetchUser("123");
if (result.success) {
  console.log(result.data.name);
} else {
  console.error(result.error);
}
```

---

## 🧪 Testing Standards

### Naming de Tests

```typescript
// ✅ CORRECTO: Descriptivo
describe("fetchUser", () => {
  it("should return user when ID exists", async () => {
    // Test
  });

  it("should return null when ID does not exist", async () => {
    // Test
  });

  it("should throw error when database is unavailable", async () => {
    // Test
  });
});

// ❌ INCORRECTO: Ambiguo
describe("fetchUser", () => {
  it("works", () => {});
  it("fails", () => {});
});
```

---

### Arrange-Act-Assert

```typescript
// ✅ CORRECTO: Estructura clara
it("should calculate total price correctly", () => {
  // Arrange
  const items = [
    { price: 10, quantity: 2 },
    { price: 5, quantity: 3 },
  ];

  // Act
  const total = calculateTotal(items);

  // Assert
  expect(total).toBe(35);
});
```

---

## 🔒 Security Standards

### Nunca Hardcodear Secretos

```typescript
// ❌ INCORRECTO: Secreto hardcodeado
const API_KEY = "sk_live_123456789";

// ✅ CORRECTO: Variable de entorno
const API_KEY = process.env.STRIPE_SECRET_KEY!;

// ✅ MEJOR: Con validación
const API_KEY = process.env.STRIPE_SECRET_KEY;
if (!API_KEY) {
  throw new Error("STRIPE_SECRET_KEY is not defined");
}
```

---

### Validación de Entrada

```typescript
// ✅ CORRECTO: Validar con Zod
import { z } from "zod";

const UserSchema = z.object({
  email: z.string().email(),
  age: z.number().min(18).max(120),
  name: z.string().min(1).max(100),
});

function createUser(input: unknown) {
  const validated = UserSchema.parse(input);
  // validated es type-safe
  return database.users.create(validated);
}
```

---

### Sanitización de Salida

```typescript
// ✅ CORRECTO: Sanitizar HTML
import DOMPurify from 'dompurify';

function renderUserContent(html: string) {
  const clean = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}
```

---

## 📊 Performance Standards

### Memoization

```typescript
// ✅ CORRECTO: Memoizar cálculos costosos
import { useMemo } from 'react';

function ExpensiveComponent({ items }: { items: Item[] }) {
  const sortedItems = useMemo(() => {
    return items.sort((a, b) => a.price - b.price);
  }, [items]);

  return <List items={sortedItems} />;
}
```

---

### useCallback para Funciones

```typescript
// ✅ CORRECTO: useCallback para funciones pasadas como props
import { useCallback } from 'react';

function ParentComponent() {
  const handleClick = useCallback(() => {
    console.log('Clicked');
  }, []);

  return <ChildComponent onClick={handleClick} />;
}
```

---

## 📚 Referencias

- [PROTOCOL_ZERO.md](./PROTOCOL_ZERO.md) - Nivel 0
- [ARCHITECTURE_STANDARDS.md](./ARCHITECTURE_STANDARDS.md) - Nivel 1
- [QUALITY_GATES.md](./QUALITY_GATES.md) - Nivel 1

---

**Última Actualización**: 2026-02-03  
**Mantenedor**: Luis Sambrano  
**Estado**: ACTIVO
