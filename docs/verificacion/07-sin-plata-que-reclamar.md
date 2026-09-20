# Registro de verificación · capítulo 07

`guia/07-sin-plata-que-reclamar.md` — capítulo **Sin plata: qué reclamar y dónde**.
Revisión: 20 de septiembre de 2026.

Aquí queda todo lo que **no se pudo confirmar** contra la fuente oficial. Son tres pendientes, y
ninguno es un número inventado: en los tres casos el ítem queda con lo que la fuente sí dice.

---

## Ítem 4, línea 48 — año de referencia de los montos del Subsidio de Cesantía

- `guia/07-sin-plata-que-reclamar.md` ítem 4, línea 48
  Dato: el ítem cita los montos por tramo del Subsidio de Cesantía: $17.338 entre los días 0 y 90,
  $11.560 entre los días 91 y 180 y $8.669 entre los días 181 y 360.
  Sospecha: (ninguna) los montos se leyeron íntegros de la ficha oficial; lo que falta es el año.
  Fuente que no se pudo leer: `https://www.chileatiende.gob.cl/fichas/33809-subsidio-de-cesantia-pagado-por-ips-o-cajas-de-compensacion`
  — la ficha se leyó completa y no indica el año de los valores; la única frase sobre vigencia es
  "su monto es fijado anualmente y varía según el período en que la persona beneficiaria se
  encuentre cesante".
  Cómo cerrarlo: pedir en una sucursal ChileAtiende o en la caja de compensación el decreto o la
  resolución que fija los valores del año en curso, y agregar la fecha al ítem.

## Ítem 11, línea 111 — vigencia del Subsidio Eléctrico más allá de 2026

- `guia/07-sin-plata-que-reclamar.md` ítem 11, línea 111
  Dato: el ítem afirma que el Subsidio Eléctrico del Ministerio de Energía está definido por ley
  para 2024, 2025 y 2026, y que en 2026 se paga en 6 cuotas desde septiembre.
  Sospecha: (ninguna) el dato de 2026 está confirmado; lo que falta es si habrá convocatoria para
  2027.
  Fuente que no se pudo leer: `https://www.chileatiende.gob.cl/fichas/124375-subsidio-electrico`
  — la ficha se leyó completa y no menciona 2027; no existe todavía una ficha oficial para el
  período siguiente.
  Cómo cerrarlo: revisar la Ley de Presupuestos del Sector Público de 2027 y el sitio del
  Ministerio de Energía cuando se abra la convocatoria, y actualizar el ítem con la fecha del
  llamado.

## Ítem 15, línea 147 — tarifa social o subsidio de internet (SUBTEL)

- `guia/07-sin-plata-que-reclamar.md` ítem 15, línea 147
  Dato: el ítem **no afirma** que exista una tarifa social de internet; deja constancia de que no
  se encontró ficha oficial que la describa.
  Sospecha: existe una tarifa social de internet móvil o fija administrada por SUBTEL, de la que se
  habla en prensa y en sitios de operadores, pero no se encontró el instrumento oficial.
  Fuente que no se pudo leer:
  - `https://www.chileatiende.gob.cl/buscar?query=tarifa+social` — la búsqueda no devuelve ninguna
    ficha de tarifa social de internet; solo el Registro Nacional de Conectividad.
  - `https://www.subtel.gob.cl/tarifa-social/` y
    `https://www.subtel.gob.cl/tarifa-social-de-internet/` — responden 404.
  - `https://www.subtel.gob.cl/beneficios/` — la página existe pero solo describe portabilidad
    numérica.
  Cómo cerrarlo: preguntar en Subtel o en el call center 101 de ChileAtiende si la tarifa social
  de internet sigue vigente, qué ley o resolución la creó, qué requisitos tiene y cuál es el
  descuento. Recién entonces se puede escribir un ítem propio con grado A.

---

## Notas de método

- **No se pudo usar el buscador general de LeyChile** (`bcn.cl/leychile/consulta/listado_n`): la
  página se carga por JavaScript y devuelve "Este proceso demora demasiado, es probable que su
  conexión esté muy lenta o que su navegador no sea compatible con nuestra aplicación". El
  endpoint `datos.bcn.cl/sparql` respondió vacío para las consultas por título "TARIFA SOCIAL" e
  "INTERNET". Por eso los datos legales de este capítulo se citan por `idLey` o `idNorma`
  conocido, y no por búsqueda temática.
- **Los montos en pesos se citan con su fuente y su fecha**, y los expresados en UF se convirtieron
  con la UF del 1 de octubre de 2026, publicada por el SII: **$41.065,38**
  (`https://www.sii.cl/valores_y_fechas/uf/uf2026.htm`). No se usó una UF de memoria.
- Todo monto legal (PGU, asignación familiar, subsidio de cesantía, subsidio eléctrico, bono de
  protección, tramos de Fonasa, límite de renegociación) queda referido al año o a la resolución
  que lo fija, porque se reajustan.
- **Las 42 URL citadas abren.** Se probaron una por una con agente de navegador: todas responden
  200. `https://www.fonasa.gob.cl/tramos` responde 403 al agente del verificador automático
  (`verificador HTLB-CL`) pero 200 con agente de navegador; el aviso del verificador queda
  anotado en las notas del ítem 8.
