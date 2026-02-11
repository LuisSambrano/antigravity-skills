---
description: Create new React/Next.js components following best practices
---

# Create Component Workflow

## Steps

1. **Determine component type**: UI (reusable) or Feature (specific)
2. **Create file** in the correct location:
   - UI components: `components/ui/ComponentName.tsx`
   - Feature components: `components/features/ComponentName.tsx`
   - Layout components: `components/layouts/ComponentName.tsx`
3. **Define TypeScript interface** for props
4. **Implement the component** with:
   - Semantic HTML
   - Accessibility attributes (ARIA)
   - Responsive design
   - Dark mode support
5. **Add JSDoc** for complex logic
6. **Export** from the component file
7. **Verify**: Run `tsc --noEmit` to check types
