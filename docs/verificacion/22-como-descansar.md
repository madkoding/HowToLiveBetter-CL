# Verificación · capítulo 22 — Cómo descansar

Mismo nombre que el capítulo de `guia/`. Aquí queda anotado todo lo que no se pudo confirmar
contra la fuente oficial al escribir el capítulo. El texto de los ítems no se "rellena": queda
marcado con `POR VERIFICAR` y se anota acá.

Fecha de escritura: 20 de septiembre de 2026. UTM de referencia: $71.721 (septiembre de 2026),
valor publicado por el Servicio de Impuestos Internos,
`https://www.sii.cl/valores_y_fechas/utm/utm2026.htm` (leído el 20 de septiembre de 2026).

| Pendiente | Ítem | Dónde habría que buscarlo |
|---|---|---|
| Referencia cruzada a la Ley 20.000 en el capítulo 09 | 6 | `guia/09-lineas-rojas-legales.md` |
| Precio en Chile de una lámpara de luz brillante de 10.000 lux | 10 | Comercio establecido / arancel del ISP |
| Tiempo de espera publicado en atención primaria por consulta de salud mental | 17 | MINSAL / Superintendencia de Salud |

---

## 1. `guia/22-como-descansar.md` ítem 6, Notas
- Dato: el capítulo cita la Ley 20.000 (drogas) en su artículo 5, que castiga al que "sin el
  consentimiento de la persona afectada le administre a ésta alguna de las sustancias referidas",
  y en su artículo 50, que sanciona el consumo o porte de drogas en lugares públicos y abiertos al
  público.
- Sospecha: el encargo del capítulo 22 indica que "la línea roja está en el 09 y el tratamiento en
  el 29, acá solo el riesgo del entorno (no aceptar tragos de desconocidos)". Al leer
  `guia/09-lineas-rojas-legales.md` completo, ese capítulo **no contiene ningún ítem de la Ley
  20.000**: lo único que la menciona es el artículo 27 de la Ley 19.913 (lavado de activos), que la
  toma como delito base. La Ley 20.000 sí está cacheada y leída en
  `tools/.cache/leychile/idLey_20000.txt` y los artículos 3, 5 y 50 están citados textualmente en el
  ítem 6 de este capítulo.
- Fuente que no se pudo leer: `https://www.bcn.cl/leychile/navegar?idLey=20000` — la URL abre (200),
  así que el problema no es el enlace sino la ausencia del ítem en el capítulo 09.
- Cómo cerrarlo: agregar en el capítulo 09 un ítem de la Ley 20.000 (portar para vender, el límite
  entre consumo personal y tráfico, el artículo 4), o dejar en el capítulo 22 la referencia cruzada
  corregida apuntando a que el régimen de la Ley 20.000 se cita en ese mismo capítulo.

## 2. `guia/22-como-descansar.md` ítem 10, Costo y Notas
- Dato: la terapia de luz brillante tiene respaldo para la depresión mayor no estacional
  (Tong y cols., 2024: SMD 0,48; IC 95% 0,22 a 0,74; p<0,001, en 15 ensayos aleatorizados y 883
  pacientes) y la dosis mejor evaluada es de 60 minutos o más de exposición diaria.
- Sospecha: el encargo pide informar el costo de la lámpara de 10.000 lux, que es el dispositivo
  estándar de la terapia. No se encontró un precio oficial: no hay arancel del ISP ni listado
  público del MINSAL para ese tipo de equipo, y las tiendas que lo venden son comercio electrónico
  sin publicación de precios en fuente oficial citable.
- Fuente que no se pudo leer: no hay URL caída. La búsqueda del precio se hizo en el comercio
  establecido y en aranceles de prestaciones, sin resultado citable según §2.5 del contrato.
- Cómo cerrarlo: revisar si el ISP tiene registro sanitario de "lámparas de fototerapia" con
  arancel asociado, o si alguna prestación GES/AUGE publica el equipo dentro de su canasta.

## 3. `guia/22-como-descansar.md` ítem 17, Notas
- Dato: el ítem usa la estadística de la OMS de que "en los países de ingreso alto solamente un
  tercio de las personas que padecen depresión reciben cuidados de salud mental" y ofrece como
  puerta de entrada el consultorio y Salud Responde 600 360 77 77.
- Sospecha: para que el lector decida cuándo consultar importa cuánto se espera. No se encontró un
  indicador oficial publicado y vigente de tiempo de espera por consulta de salud mental en
  atención primaria. Los tiempos de espera que el capítulo 24 sí usa son de lista de espera de
  especialidad y de garantías GES, no de una consulta de morbilidad en el CESFAM.
- Fuente que no se pudo leer: `https://www.minsal.cl/eje-salud-mental/` abre (200) y publica el Plan
  de acción de Salud Mental 2019-2025 y las guías ciudadanas, pero no trae un dato de tiempo de
  espera de atención primaria en salud mental. La página del MINSAL de listas de espera publica
  espera de especialidad, no de APS.
- Cómo cerrarlo: consultar los reportes de tiempos de espera de la Superintendencia de Salud y las
  orientaciones técnicas del MINSAL para el Programa de Salud Mental en atención primaria.

---

## Cerrado durante la escritura

- **Ítem 1** (`guia/22-como-descansar.md`): el original chino se apoya en el reglamento de locales
  de entretenimiento de ese país (国令第 458 号, arts. 20 y 21). No existe equivalente chileno con
  esa estructura. Se reemplazó por el informe técnico oficial del NIST sobre el incendio de The
  Station (mediciones reales de tiempo de evacuación) más el artículo 144 de la Ley General de
  Urbanismo y Construcciones y el artículo 20 de la Ley 19.925. La Ley General de Urbanismo y
  Construcciones se leyó en `idNorma=13560` (DFL 458, inicio de vigencia 2026-08-12): el ítem cita
  el inciso del artículo 144 que exige el plan de emergencia ingresado a Bomberos para las
  edificaciones con carga de ocupación igual o superior a 100 personas. Cierre: 20 de septiembre de
  2026.
- **Ítem 3** (patente y horario): la sección de horarios del artículo 21 de la Ley 19.925 se leyó en
  el texto oficial vigente (inicio de vigencia 2026-07-08). El dato del original sobre "horario de
  cierre" chino no se tradujo. Cierre: 20 de septiembre de 2026.
- **Ítem 4** (alcohol dentro del vehículo): se encontró un ítem que ningún otro capítulo cubría —el
  artículo 115 A prohíbe el consumo también a los pasajeros— y se dejó fuera todo el detalle de
  umbrales y penas de la conducción ebria, que está leído en el 08. Cierre: 20 de septiembre de 2026.
- **Ítem 7** (juego y apuestas): la referencia cruzada del capítulo 09 anota que la "Ley 21.591"
  sobre apuestas en línea no existe (es la ley de royalty minero) y que la materia seguía en
  tramitación. Este capítulo conserva esa constancia y agrega lo que sí se leyó: el artículo 12 de
  la Ley 19.995, que excluye los juegos de azar en línea del permiso de operación de casino, más el
  Sistema Nacional de Autoexclusión Voluntaria de la SCJ. No se cita ningún número de ley de
  apuestas en línea. Cierre: 20 de septiembre de 2026.

## Notas de método

- Los textos legales se obtuvieron por el servicio
  `nuevo.leychile.cl/servicios/Navegar/get_norma_json` (el que usa `tools/leychile.py`). Normas
  leídas para este capítulo: Ley 19.925 (idLey 19925), Ley 18.290 (idLey 18290), Ley 19.496
  (idLey 19496), Ley 20.000 (idLey 20000), Ley 19.995 (idLey 19995), Ley General de Urbanismo y
  Construcciones (idNorma 13560) y Código del Trabajo (idNorma 207436, consultado sin uso final).
- Los DOI se verificaron uno por uno contra la API de Crossref: los once citados devuelven registro
  con el título y el año que aparecen en el capítulo. El detalle de los estudios que no tenían el
  dato pedido (magnitud exacta del efecto en el ensayo de redes sociales de 143 personas) se
  resolvió usando la cifra del resumen publicado del propio estudio y la del texto completo del
  estudio de Facebook (0,085 desviaciones estándar, error estándar 0,033, 359.827 observaciones).
- El valor de la unidad tributaria mensual de septiembre de 2026 ($71.721) se usó para todas las
  conversiones a pesos. El valor cambia mensualmente y un monto sin su mes no sirve: cada ítem que
  convierte indica el mes.
- La estadística chilena de salud mental de la Encuesta Nacional de Salud 2016-2017 **no se citó**
  porque el documento de "primeros resultados" publicado por el MINSAL no incluye el capítulo de
  salud mental: el instrumento CIDI se aplicó (3.500 encuestados de 18 años y más) pero los
  resultados del módulo no están en ese PDF. La prevalencia se sustituyó por la cifra internacional
  de la OMS, que sí está leída.
