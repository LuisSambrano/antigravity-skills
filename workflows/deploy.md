---
description: Deploy a Vercel con verificaciones automáticas
---

# /deploy - Deploy a Producción

Usa este workflow cuando quieras publicar tu trabajo.

## Lo que YO hago automáticamente

1. **Verifico calidad**
   - TypeScript: 0 errores
   - ESLint: 0 errores
   - Build: Exitoso

2. **Verifico seguridad**
   - No hay secretos expuestos
   - Variables de entorno correctas

3. **Ejecuto deploy**

   ```bash
   // turbo
   vercel --prod
   ```

4. **Te reporto resultado**
   - ✅ Deploy exitoso + URL
   - ❌ Falló + qué arreglar

## Cuándo usarlo

- Terminaste una feature y quieres publicar
- Arreglaste un bug y quieres que esté live
- Quieres mostrar el proyecto a alguien

## Ejemplo

Tú: `/deploy`

Yo:

```
🚀 Iniciando deploy a Vercel...

✅ TypeScript: 0 errores
✅ ESLint: 0 errores
✅ Build: Exitoso
✅ Deploy: Completado

🔗 URL: https://tu-proyecto.vercel.app

¿Necesitas algo más?
```
