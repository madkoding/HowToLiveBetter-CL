# Verificación · capítulo 05 — No gastes tu plata

Registro de lo que no se pudo confirmar contra la fuente oficial al escribir
`guia/05-no-gastes-tu-plata.md`. Cada línea corresponde a una marca `POR VERIFICAR` en el capítulo.

## Índice

| Capítulo | Pendientes abiertos | Última revisión |
|---|---|---|
| `guia/05-no-gastes-tu-plata.md` | 5 | 2026-09-21 |

## Cerrado

- **Ítem 1 — umbral de restitución de la Ley 20.009. CERRADO el 2026-09-21.**
  El dato que faltaba lo encontró el redactor del capítulo 14 y quedó verificado:
  **decreto exento 473 del Ministerio de Hacienda, publicado el 30 de enero de 2026**, que fija el
  umbral en **35 unidades de fomento** (≈ $1.434.139 con la UF de $40.975,41 al 20-09-2026).
  Fuente oficial: <https://www.bcn.cl/leychile/navegar?idNorma=1220909>
  Se corrigió el ítem 1 (el texto ya nombra el decreto con su número y fecha, en vez de atribuir
  el valor a la CMF) y se agregó la fuente al campo `Fuentes`. Sin marca `POR VERIFICAR`.
  Vale la pena anotar cómo se cerró: **no lo resolvió el capítulo que lo declaró, sino otro
  capítulo escrito en paralelo**. Por eso el registro es compartido y no un archivo privado de
  cada redactor.

## Nota de fuente (no es una marca en el capítulo)

- La copia de la Ley 19.496 que sirve el servicio JSON de LeyChile
  (`https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idLey=19496`) corresponde a la
  versión vigente desde el 20 de abril de 2021, es decir, **anterior a la Ley 21.398** (publicada
  el 24 de diciembre de 2021). Por eso en esa copia el artículo 21 todavía dice "tres meses" y no
  aparece el artículo 17 N. El capítulo se apoya en el **texto de la Ley 21.398** (que sí se pudo
  leer completo) y en las páginas oficiales del SERNAC, que informan la garantía legal como de
  seis meses. Cómo cerrarlo: pedir la versión vigente de la Ley 19.496 al visor de LeyChile con
  la fecha actual (`https://www.bcn.cl/leychile/navegar?idNorma=61438`) y confirmar ahí el
  artículo 21 refundido.

---

- `guia/05-no-gastes-tu-plata.md` ítem 1, línea 24
  Dato: el umbral de restitución de la Ley 20.009 sería de 35 unidades de fomento, equivalentes a
  $1.434.139 con la UF de $40.975,41 al 20 de septiembre de 2026.
  Sospecha: la ley deja el umbral en un rango (entre 15 y 35 unidades de fomento) y manda fijarlo
  por decreto supremo de Hacienda y Economía, revisable al menos anualmente. El valor de 35
  unidades de fomento es el que publica la CMF al explicar la ley, pero no se pudo leer el decreto
  que lo fija.
  Fuente que no se pudo leer: el decreto supremo del Ministerio de Hacienda que define el o los
  umbrales, señalado en el inciso final del artículo 5 de la Ley 20.009 —
  <https://www.bcn.cl/leychile/navegar?idLey=20009> (el texto legal abre; la referencia al decreto
  no incluye número ni fecha, y la búsqueda en el SPARQL de datos.bcn.cl por título no devolvió
  resultados para "umbral de restitución").
  Cómo cerrarlo: buscar en el Diario Oficial (<https://www.diariooficial.interior.gob.cl/>) los
  decretos supremos del Ministerio de Hacienda dictados bajo la fórmula "Por orden del Presidente
  de la República" posteriores al 30 de mayo de 2024 (fecha de la Ley 21.673), o consultar la
  sección de normativa bancaria de la CMF.

- `guia/05-no-gastes-tu-plata.md` ítem 4, línea 66
  Dato: no existe cifra oficial del crecimiento de la deuda cuando se paga solo el mínimo de la
  tarjeta de crédito.
  Sospecha: la CMF describe el mecanismo (intereses desde el día de la transacción en avances, y
  que la deuda no baja si el mínimo no cubre cuotas, intereses, impuestos y comisiones) pero no
  publica un porcentaje ni un ejemplo numérico estándar; el cálculo depende del monto y de la tasa
  de cada tarjeta.
  Fuente que no se pudo leer: página temática de CMF Educa sobre el pago mínimo
  <https://www.cmfeduca.cl/educa/621/w3-article-26994.html> — abre, pero es la ficha de un video,
  sin cifras.
  Cómo cerrarlo: usar el simulador "Calcula cuánto demorarás en pagar la Tarjeta" con un monto y
  una tasa concretos, en <https://www.cmfeduca.cl/educa/621/w3-propertyvalue-44674.html>, y citar
  el resultado como ejemplo, no como promedio.

- `guia/05-no-gastes-tu-plata.md` ítem 6, línea 96
  Dato: no se verificó el rango de comisiones de fondos mutuos vigente en Chile ni un tope
  regulatorio vigente.
  Sospecha: existe un comparador oficial de costos de fondos mutuos, pero el capítulo no puede
  afirmar un porcentaje ni un tope sin leer el dato del día.
  Fuente que no se pudo leer: los comparadores de la CMF se cargan como aplicación interactiva y no
  entregan cifras en el HTML —
  <https://www.cmfeduca.cl/educa/621/w3-propertyvalue-44674.html> (la página listado abre; los
  valores solo aparecen al ejecutar el comparador).
  Cómo cerrarlo: leer el comparador de costos de fondos mutuos de la CMF y citar el rango con la
  fecha de consulta, o el informe de comisiones máximas del portal de la CMF.

- `guia/05-no-gastes-tu-plata.md` ítem 9, línea 128
  Dato: contenido de la Norma de Carácter General N° 484 de la CMF sobre comisiones en operaciones
  de crédito de dinero (proporcionalidad al costo, servicios reales, aceptación expresa, todo
  cobro que no cumpla se considera interés).
  Sospecha: el texto normativo no se pudo descargar; la descripción proviene íntegramente de la
  página oficial de la CMF que la explica.
  Fuente que no se pudo leer: no se ubicó el archivo de la NCG 484 en el buscador de normativa de
  la CMF (<https://www.cmfchile.cl/>); la página que sí abre y fundamenta el ítem es
  <https://www.cmfeduca.cl/educa/621/w3-article-71770.html>.
  Cómo cerrarlo: buscar la NCG N° 484 en el buscador de normativa de la CMF o en el Diario Oficial
  y citar el numeral de la norma en lugar de la página explicativa.

- `guia/05-no-gastes-tu-plata.md` ítem 18, línea 240
  Dato: no hay cifra oficial ni estudio chileno citable sobre la diferencia entre contratar un
  seguro con ahorro y, alternativamente, contratar protección pura e invertir el resto.
  Sospecha: la CMF describe la estructura de la póliza (parte de la prima a gastos y cobertura,
  parte al ahorro; capital asegurado APV con tope de 3.000 unidades de fomento) pero no compara
  resultados.
  Fuente que no se pudo leer: fichas de CMF Educa sobre seguros con ahorro
  <https://www.cmfeduca.cl/educa/621/w3-propertyvalue-1421.html> y
  <https://www.cmfeduca.cl/educa/621/w3-propertyvalue-1356.html> — abren, pero no contienen
  comparación de rentabilidad contra alternativas.
  Cómo cerrarlo: consultar los informes estadísticos del mercado de seguros de la CMF o una
  publicación actuarial chilena revisada por pares; no reemplazar por una estimación propia.

- `guia/05-no-gastes-tu-plata.md` ítem 21, línea 264
  Dato: no se encontró norma chilena vigente sobre cómo debe determinarse el precio de referencia
  de una promoción, ni informe oficial que mida la brecha entre el precio tachado y el precio
  efectivamente cobrado.
  Sospecha: existe regulación comparada sobre la materia (por ejemplo, la exigencia de que el
  precio de referencia sea el menor precio efectivamente cobrado en los días previos), pero no se
  confirmó una regla equivalente y vigente en Chile; citarla como si fuera local sería inventarla.
  Fuente que no se pudo leer: no se identificó una fuente chilena oficial sobre la materia. El
  respaldo del ítem es el estudio de anclaje citado en `Fuentes`.
  Cómo cerrarlo: revisar la Ley 19.496 y sus reglamentos, el anteproyecto o las guías del SERNAC
  sobre publicidad y precios, y el sitio del Servicio Nacional del Consumidor sobre información
  básica comercial.
