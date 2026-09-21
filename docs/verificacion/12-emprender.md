# Verificación · capítulo 12 — Emprender sin perder la casa

Registro de lo que no se pudo confirmar contra la fuente oficial al momento de escribir.
El ítem respectivo lleva la marca `POR VERIFICAR` en `- Notas:`.

---

## Ítem 11 — Patente municipal: tope máximo en unidades tributarias mensuales

**Línea del ítem 11 (`- Notas:`).** Texto marcado:

> POR VERIFICAR: el tope superior del valor de la patente se cita desde el texto del artículo 24
> del Decreto Ley 3.063 que entrega la API de LeyChile (cuatro mil unidades tributarias
> mensuales); no se pudo leer artículo por artículo el texto refundido del decreto 2.385 de 1996,
> del Ministerio del Interior, que es el que rige según la referencia del propio SII, así que el
> techo puede diferir.

**Dato sospechado:** el tope superior del valor de doce meses de la patente municipal.

**Qué se pudo leer:**

| Fuente | Cifra del tope |
|---|---|
| Decreto Ley 3.063, artículo 24, texto entregado por la API de LeyChile (`tools/leychile.py meta idNorma=7054`, con la marca de modificación `LEY 19388 Art.2°,10.a)` junto a la frase) | 4.000 unidades tributarias mensuales |
| Ficha de formalización publicada por el propio SII, "Inicio de actividades y formalización de un negocio", sección Patente Municipal | el valor fluctúa "entre un 0,25% y un 0,5% del capital inicial declarado" (2,5 por mil a 5 por mil), sin mencionar tope |

El artículo 1 de la Ley 20.494 (publicada el 27 de enero de 2011) modificó el artículo 26 del
decreto 2.385, de 1996, y no el artículo 24, de modo que ese decreto sigue siendo el texto
refundido que rige y no se pudo consultar completo por la API de LeyChile en esta sesión.

**URL que no se pudo resolver:**

- El texto refundido vigente del decreto N° 2.385, de 1996, del Ministerio del Interior
  (Rentas Municipales), que es el que rige según la referencia que el propio SII hace en esa
  sección, no se pudo identificar con un idNorma estable en LeyChile ni leer artículo por
  artículo. El artículo 24 se citó desde el texto del DL 3.063 que entrega la API de LeyChile.
- Fichas de ChileAtiende sobre patente comercial: las URL probadas
  (`https://www.chileatiende.gob.cl/fichas/1669-patente-comercial` y
  `https://www.chileatiende.gob.cl/fichas/63134`) responden 404 y no se citaron.
- `https://www.sii.cl/destacados/empresa/`, `https://www.sii.cl/destacados/boleta_electronica/`,
  `https://www.sii.cl/preguntas_frecuentes/boleta_honorarios/` y
  `https://www.sii.cl/destacados/regimenes_tributarios/` responden 404 y no se citaron.
- El texto refundido de la Ley 19.496 publicado en `https://www.bcn.cl/leychile/navegar?idNorma=1160403`
  no se pudo cargar por la API en esta sesión; los artículos de esa ley se citaron desde el
  texto de la Ley 19.496 obtenido con `idLey=19496`.
- `https://www.bcn.cl/leychile/navegar?idLey=21133` respondió 502 al probarse con `curl` el
  20 de septiembre de 2026; el servidor de LeyChile sí entregó el texto por la vía de la API
  (`tools/leychile.py`), que es de donde salió el artículo quinto citado en el ítem 10.

**Cómo se resolvió en el texto:** el ítem cita el rango legal completo (2,5 por mil a 5 por mil
del capital propio, mínimo una unidad tributaria mensual y máximo cuatro mil unidades tributarias
mensuales) tal como está en el texto consultado, y el monto en pesos se calcula solo sobre el
piso de una unidad tributaria mensual, que es el dato que no está en disputa. El techo no se
convirtió a pesos.

---

## Ítems 1 a 20 — verificación general

- Todos los artículos citados se leyeron desde el texto que entrega la API de LeyChile
  (`https://nuevo.leychile.cl/servicios/Navegar/get_norma_json`), no desde resúmenes ni prensa.
- Todos los montos en pesos se calcularon a partir de la unidad tributaria mensual de septiembre
  de 2026 ($71.721, SII) y de la unidad de fomento al 20 y al 30 de septiembre de 2026
  ($40.975,41 y $41.057,20, SII).
- El DOI del ítem 16 se verificó contra Crossref: el registro existe y su título y año coinciden
  con los citados.
- El artículo 74 número 2 de la Ley sobre Impuesto a la Renta quedó citado con la tasa del 17%
  que figura en el texto, y a continuación se explicita en el campo Beneficio que el 15,25%
  vigente en 2026 es el que informa el SII conforme al calendario del artículo quinto de la
  Ley 21.133 (0,75% anual a partir del año siguiente a la publicación, 1% el noveno año).
