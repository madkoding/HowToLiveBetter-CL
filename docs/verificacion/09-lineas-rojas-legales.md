# Verificación · capítulo 09 — Líneas rojas legales

Mismo nombre que el capítulo de `guia/`. Aquí queda anotado todo lo que no se pudo confirmar
contra la fuente oficial al escribir el capítulo. El texto de los ítems no se "rellena": queda
marcado con `POR VERIFICAR` y se anota acá.

Fecha de escritura: 20 de septiembre de 2026. UTM de referencia: $71.721 (septiembre de 2026),
valor publicado por el Servicio de Impuestos Internos,
`https://www.sii.cl/valores_y_fechas/utm/utm2026.htm` (leído el 20 de septiembre de 2026).

| Pendiente | Ítem | Dónde habría que buscarlo |
|---|---|---|
| Vigencia de la pena del artículo 9 de la Ley 17.798 | 10 | Versiones del artículo en LeyChile |
| Existencia de una "Ley 21.133" sobre drones | 11 | Buscador de normas de LeyChile por materia |
| Existencia de una "Ley 21.591" sobre juego en línea | 14 | Tramitación en el portal del Senado |
| Tipo penal general de "noticia falsa / alarma pública" | 22 | Tramitación del proyecto de noticias falsas |

Cerrado durante la escritura: el artículo 362 del Código Penal (ítem 4), que se leyó completo y
obligó a corregir la pena citada.

---

## 1. `guia/09-lineas-rojas-legales.md` ítem 10, Notas
- Dato: la Ley 17.798 sobre Control de Armas sanciona la posesión de armas y municiones sin
  autorización (artículo 9) con "la pena de prisión en cualquiera de sus grados o con multa de un
  sueldo vital mensual, escala A), del departamento de Santiago", y la descarga del texto oficial
  se usó para citar los artículos 2, 3, 5, 6, 11, 13 y 14.
- Sospecha: el artículo 9 conserva el texto de 1972 y la referencia a una unidad de cuenta en
  desuso (sueldo vital). No se pudo confirmar si una ley posterior lo modificó o si su multa se
  actualiza por otra vía, ni si hay jurisprudencia que la reconduzca a la escala del artículo 21
  del Código Penal.
- Fuente que no se pudo leer: `https://www.bcn.cl/leychile/navegar?idLey=17798` — el texto
  descargado corresponde a la versión publicada (inicio de vigencia 1972-10-21) y no trae
  versiones modificatorias ni notas de actualización para ese artículo.
- Cómo cerrarlo: revisar el historial de versiones del artículo 9 en LeyChile y los boletines de
  las leyes que hayan modificado la Ley 17.798 con posterioridad a 1972.

## 2. `guia/09-lineas-rojas-legales.md` ítem 11, Notas
- Dato: el encargo pide citar la "Ley 21.133" como norma de drones y zonas prohibidas.
- Sospecha: según el servicio de metadatos de LeyChile, el número 21.133 corresponde a la ley que
  "Modifica las normas para la incorporación de los trabajadores independientes a los regímenes de
  protección social", publicada el 2 de febrero de 2019. La materia de drones, en lo que se pudo
  leer, está en la Norma Aeronáutica DAN 151 de la DGAC y en el Código Aeronáutico (decreto 541
  exento, idNorma 30287), no en una ley con ese número.
- Fuente que no se pudo leer: no hay URL caída; la búsqueda por número en LeyChile y el SPARQL de
  `datos.bcn.cl` no devuelven una norma de drones con ese número, y el buscador de LeyChile
  (`https://www.bcn.cl/leychile/`) no responde a peticiones HTTP simples porque exige navegador
  con JavaScript.
- Cómo cerrarlo: consultar el buscador de normas de LeyChile por materia ("aeronaves") desde un
  navegador, o pedir a la DGAC el listado de normas aplicables a RPA.

## 3. `guia/09-lineas-rojas-legales.md` ítem 14, Notas
- Dato: el encargo pide citar la "Ley 21.591" como ley del juego online.
- Sospecha: según el servicio de metadatos de LeyChile, la ley 21.591 es la "Ley sobre royalty a
  la minería", publicada el 10 de agosto de 2023. Lo único vigente que se pudo leer sobre juegos
  de azar es la Ley 19.995, cuyo artículo 12 dispone que el permiso de operación de un casino "en
  ningún caso comprenderá juegos de azar en línea", y los artículos 276 a 279 y 496 numeral 14 del
  Código Penal.
- Fuente que no se pudo leer: `https://www.bcn.cl/leychile/navegar?idLey=21591` (el idLey 21591 se
  verificó como royalty minero por el servicio de metadatos, no como ley de apuestas). El buscador
  de LeyChile devuelve la página de la aplicación sin resultados por HTTP.
- Cómo cerrarlo: revisar el estado del proyecto de ley que regula las plataformas de apuestas en
  línea en el portal del Senado y confirmar si fue publicado antes de citar un número de ley.
  Mientras no haya ley publicada, el capítulo cita solo el texto de la Ley 19.995 y del Código
  Penal.

## 4. `guia/09-lineas-rojas-legales.md` ítem 22, Notas
- Dato: el original chino cubre "difundir información falsa que cause alarma pública". En Chile no
  se encontró un tipo penal general equivalente.
- Sospecha: lo que el Código Penal castiga en el texto leído es (a) dar falsa alarma de incendio,
  emergencia o calamidad pública a Bomberos u otros servicios de utilidad pública (artículo 268
  bis), (b) turbar gravemente la tranquilidad pública (artículo 269, inciso primero), (c)
  impedir o dificultar la actuación del personal de Bomberos o de un servicio de utilidad pública
  (artículo 269, inciso segundo) y (d) aportar antecedentes falsos a una investigación (artículo
  269 bis). Puede existir una ley posterior sobre noticias falsas.
- Fuente que no se pudo leer: `https://www.bcn.cl/leychile/navegar?idNorma=1984` — las búsquedas
  por "información falsa", "noticia falsa", "alarma pública" y "pánico" no devolvieron ningún
  artículo adicional a los citados.
- Cómo cerrarlo: consultar la tramitación de la ley que sanciona las noticias falsas en el portal
  del Senado y revisar si fue publicada; si lo fue, actualizar el ítem citando su artículo.

---

## Cerrado durante la escritura

- **Ítem 4** (`guia/09-lineas-rojas-legales.md` línea 47): el artículo 362 del Código Penal se
  leyó en el texto oficial —"será castigado con presidio mayor en sus grados medio a máximo, aunque
  no concurra circunstancia alguna de las enumeradas en el artículo anterior"— junto con los
  artículos 361, 365 bis, 366 y 366 bis. La pena citada en el primer borrador era incorrecta y se
  corrigió; la marca `POR VERIFICAR` se borró. Cierre: 20 de septiembre de 2026.
- **Ítem 17** (`guia/09-lineas-rojas-legales.md` línea 164): el bloque de abandono se localizó
  completo (artículos 346 a 352 del Código Penal, líneas 1726 a 1739 del volcado) y se corrigió la
  numeración: el abandono en lugar no solitario es el artículo 346, el de lugar solitario el
  artículo 349, las agravaciones por el parentesco de quien abandona están en los artículos 347 y
  350 y las agravaciones por lesiones graves o muerte en los artículos 348 y 351. Cierre: 20 de
  septiembre de 2026.

## Notas de método

- El buscador de LeyChile no responde a peticiones HTTP simples: devuelve la página de la
  aplicación. Los textos se obtuvieron por el servicio
  `nuevo.leychile.cl/servicios/Navegar/get_norma_json` (el que usa `tools/leychile.py`) y la
  traducción de número de ley a idNorma, por el SPARQL de `datos.bcn.cl`.
- La UTM de septiembre de 2026 ($71.721, valor del SII leído el 20 de septiembre de 2026) se usó
  para las conversiones a pesos. El valor cambia mensualmente y un monto sin su mes no sirve: cada
  ítem que convierte indica el mes y la equivalencia se recalcula si cambia la UTM.
