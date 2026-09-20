# Registro de verificación

Un archivo por capítulo, con el mismo nombre que el capítulo de `guia/`.

Aquí se anota **todo** lo que no se pudo confirmar contra la fuente oficial. Cada línea lleva:

```
- `<guia/capitulo.md>` ítem N, línea M
  Dato: <qué afirma el ítem>
  Sospecha: <el valor que creemos correcto, si lo hay> (marcado como sospecha, no como dato)
  Fuente que no se pudo leer: <URL> — <por qué: 404, PDF ilegible, portal caído, versión no publicada>
  Cómo cerrarlo: <qué habría que consultar y dónde>
```

## Reglas

1. **El registro y las marcas `POR VERIFICAR` en los ítems tienen que calzar.** El verificador
   falla si un capítulo tiene marcas y no tiene su registro.
2. Un dato sin confirmar se marca en el ítem y se anota acá. **Nunca se rellena con un valor
   plausible.** Es la única falta inexcusable de este proyecto: un número inventado es
   indetectable en revisión y basta uno para que el lector desconfíe de todo el resto.
3. Cuando se cierra un pendiente: se corrige el ítem, se borra la marca y se anota la fecha de
   cierre en este archivo. El historial queda en git.
4. Los montos, plazos y trámites chilenos cambian con el calendario legislativo. Un dato sin año
   de referencia es, por definición, un pendiente.

## Índice

| Capítulo | Pendientes abiertos | Última revisión |
|---|---|---|
| (se completa al escribir cada capítulo) | | |

El verificador imprime el total de pendientes:

```bash
python3 tools/verificar.py | grep POR VERIFICAR
```
