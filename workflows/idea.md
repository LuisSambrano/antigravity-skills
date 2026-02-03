---
description: Evalúo viabilidad de una idea de YouTube o cualquier fuente
---

# /idea - Evaluar Viabilidad de Ideas

Usa este workflow cuando veas algo interesante y quieras saber si podemos hacerlo.

## Lo que YO hago automáticamente

1. **Investigo la idea**
   - Qué es exactamente
   - Qué tecnología usa
   - Qué recursos necesita

2. **Evalúo viabilidad**
   - ¿Funciona con tu stack? (Next.js, Supabase, Vercel)
   - ¿Cuánto tiempo tomaría?
   - ¿Qué riesgos hay?

3. **Te doy veredicto**
   - ✅ SÍ: Plan de implementación
   - ⚠️ PARCIAL: Qué partes sí, cuáles no
   - ❌ NO: Por qué no y alternativas

## Cuándo usarlo

- Viste un video de YouTube sobre algo cool
- Leíste sobre una tecnología nueva
- Tienes una idea y no sabes si es posible
- Quieres saber si algo vale la pena antes de invertir tiempo

## Ejemplo

Tú: `/idea Quiero implementar autenticación con passkeys como vi en este video`

Yo:

```
🔍 Investigando passkeys...

## Análisis

**Qué es**: Autenticación sin contraseña usando biometría (Face ID, huella)

**Tu stack**:
- Next.js ✅ Soportado
- Supabase ⚠️ No nativo, pero hay workaround
- Vercel ✅ Soportado

## Veredicto: ⚠️ PARCIAL

**Lo que SÍ podemos hacer**:
- Implementar WebAuthn con librería `@simplewebauthn`
- Usar como método secundario (además de email/password)

**Lo que NO recomiendo**:
- Usar como único método (no todos los dispositivos lo soportan)

**Tiempo estimado**: 4-6 horas

**Alternativa más simple**: Magic links (ya soportado por Supabase)

¿Quieres que proceda con passkeys o prefieres la alternativa?
```

## TÚ NO necesitas

- ❌ Investigar antes de preguntarme
- ❌ Entender la tecnología
- ❌ Saber si es compatible
- ❌ Dar contexto técnico detallado

Solo dime qué viste/quieres y yo hago el trabajo.
