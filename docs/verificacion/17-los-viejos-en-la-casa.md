# Verificación · capítulo 17 — Los viejos en la casa

`guia/17-los-viejos-en-la-casa.md`

Pendientes abiertos al escribir el capítulo. Cada uno calza con una marca `POR VERIFICAR` en el
ítem correspondiente.

---

## 1. Precio en Chile de una barra de apoyo y de una cinta antideslizante

- `guia/17-los-viejos-en-la-casa.md` ítem 1, campo `Costo` y `Notas`
  Dato: el ítem dice que las adaptaciones de la casa —barras de apoyo, superficies
  antideslizantes, luces de noche— "se pagan aparte", sin dar ningún monto.
  Sospecha: no hay valor sospechado. Los precios de ayudas técnicas deben estar en el catálogo de
  ayudas técnicas de Fonasa o en el sondeo de precios de productos para el adulto mayor del SERNAC.
  Fuente que no se pudo leer: el catálogo de ayudas técnicas de Fonasa y el buscador de precios del
  SERNAC no se consultaron para este capítulo; el sondeo del SERNAC que sí se leyó (noviembre de
  2017) está declarado desactualizado por el propio Servicio ("Los datos de este estudio
  corresponden a una fecha pasada y no están vigentes"), así que no sirve para citar un precio
  vigente. El informe del SERNAC usado está en
  <https://www.sernac.cl/portal/619/w3-article-7601.html>.
  Cómo cerrarlo: consultar el listado de ayudas técnicas y su aporte estatal (Fonasa, sección
  ayudas técnicas) y el sondeo de precios vigente del SERNAC para productos dirigidos a personas
  mayores; si hay un precio publicado con su año, escribirlo en `Costo` con la fecha y borrar la
  marca.

## 2. Arancel notarial por otorgar un testamento

- `guia/17-los-viejos-en-la-casa.md` ítem 3, campo `Costo` y `Notas`
  Dato: el ítem dice "lo que cobre el notario por autorizar el testamento abierto o cerrado",
  sin monto.
  Sospecha: los aranceles notariales están fijados en el decreto que establece el arancel de los
  notarios, y el valor del testamento abierto suele quedar en la banda de las decenas de miles de
  pesos (no verificado; es una sospecha, no un dato).
  Fuente que no se pudo leer: el arancel de notarios no está publicado en el Código Civil ni en
  LeyChile como texto único consultado en esta sesión, y el sitio del Colegio de Notarios no se
  consultó. La única cifra notarial confirmada en el capítulo es el informe del Registro Nacional
  de Testamentos ($290), que sí está publicado en la ficha de ChileAtiende.
  Cómo cerrarlo: buscar en LeyChile el decreto que fija el arancel de los notarios (materia de
  aranceles notariales, Ministerio de Justicia) y leer dentro de él la partida correspondiente al
  otorgamiento de testamento; si el monto aparece, escribirlo con su año y borrar la marca.

## 3. Plazo de resolución de la posesión efectiva intestada

- `guia/17-los-viejos-en-la-casa.md` ítem 4, campo `Notas`
  Dato: el ítem no afirma ningún plazo de tramitación; la marca existe justamente porque no se
  pudo confirmar un plazo.
  Sospecha: la Ley 19.903 no fija un plazo de días para que el Director Regional resuelva —solo
  dice que la resolución es fundada y que puede pedir que se complementen los antecedentes, caso en
  el cual se suspende la tramitación (artículo 5)—, de modo que probablemente no existe un plazo
  legal y el dato habría que buscarlo en estadísticas de tiempo de tramitación del propio Servicio.
  Fuente que no se pudo leer: la ficha oficial de ChileAtiende "Posesión efectiva de herencias
  intestadas (sin testamento)"
  (<https://www.chileatiende.gob.cl/fichas/3364-posesion-efectiva-de-herencias-intestadas-sin-testamento>)
  describe el trámite, los documentos, los herederos y los aranceles, pero no publica un plazo de
  respuesta. El texto de la Ley 19.903 se leyó completo vía API de LeyChile.
  Cómo cerrarlo: revisar si el Reglamento de la Ley 19.903 (decreto 237) fija un plazo, o pedir la
  estadística de tiempo de tramitación al Servicio de Registro Civil e Identificación. Si no existe
  plazo legal, dejarlo dicho así en las Notas y borrar la marca.

## 4. Monto de la PGU para personas de 75 años o más y calendario de Dipreca y Capredena

- `guia/17-los-viejos-en-la-casa.md` ítem 6, campo `Notas`
  Dato: el ítem consigna el monto de $231.732 mensuales desde el 1 de febrero de 2026 (hasta
  pensión base de $789.139) y menciona que con la reforma el máximo sube a $250.275 para las
  personas de 75 años o más.
  Sospecha: el valor de $250.275 para 75 años o más es el que publica el calendario de la reforma
  de pensiones para septiembre de 2026; queda por confirmar cuál rija el 1 de octubre de 2026 y
  después, y si el calendario de incorporación de los pensionados de Dipreca y Capredena (que el
  mismo calendario anuncia para septiembre de 2027) sigue igual.
  Fuente que no se pudo leer: el calendario oficial "Reforma de Pensiones: fechas clave" de
  ChileAtiende (<https://chileatiende.gob.cl/reformadepensiones/fechas-clave>) sí se leyó y es la
  fuente de las fechas, pero la ficha de la PGU y el calendario entregan el monto y las fechas por
  tramos anuales, y en ambos hay más de un monto simultáneo vigente según la edad, de modo que no
  se pudo fijar un único valor sin riesgo de equivocarse ni dar por cerrado el tramo siguiente.
  Cómo cerrarlo: consultar el monto vigente de la PGU en la ficha de ChileAtiende
  (<https://www.chileatiende.gob.cl/fichas/102077-pension-garantizada-universal-pgu>) una vez
  publicado el valor de octubre de 2026 y siguientes, y revisar el mismo calendario de la reforma
  para la incorporación de los pensionados de Dipreca y Capredena. Escribir el monto con su fecha y
  borrar la marca.

## 5. Fecha desde la cual es exigible la inscripción en el Registro Nacional de Prestadores de Servicios de Apoyos y Cuidados

- `guia/17-los-viejos-en-la-casa.md` ítem 14, campo `Notas`
  Dato: el ítem transcribe el artículo 39 de la Ley 21.805, que sanciona a las personas jurídicas
  privadas que no se inscriban en el registro "desde que esta obligación sea exigible", sin precisar
  desde cuándo lo es.
  Sospecha: la obligación depende del reglamento que el artículo 41 encarga al Ministerio de
  Desarrollo Social y Familia; los reglamentos de la ley debían dictarse en los seis meses
  siguientes a su publicación (16 de febrero de 2026), o sea hacia agosto de 2026. Es una sospecha
  basada en el plazo legal de dictación, no en el reglamento mismo.
  Fuente que no se pudo leer: no se encontró publicado el reglamento del Registro Nacional de
  Prestadores de Servicios de Apoyos y Cuidados en la sesión de escritura; el texto de la Ley 21.805
  se leyó completo vía API de LeyChile, y en él la exigibilidad queda subordinada al reglamento.
  Cómo cerrarlo: revisar el sitio del Ministerio de Desarrollo Social y Familia y su Secretaría de
  Apoyos y Cuidados
  (<https://apoyosycuidados.ministeriodesarrollosocial.gob.cl/>) y el Diario Oficial, buscando el
  reglamento del artículo 41 de la Ley 21.805. Una vez publicado, escribir la fecha de exigibilidad
  en el ítem y borrar la marca.

---

## Cifras que sí quedaron verificadas contra el texto oficial

Se dejan registradas para no repetir la búsqueda. Todas con el texto leído.

| Dato en el capítulo | Fuente leída |
|---|---|
| Ejercicio: caídas -23% (razón de tasas 0,77; IC 95% 0,71 a 0,83) y 15% menos personas que caen (RR 0,85; IC 95% 0,81 a 0,89); fracturas RR 0,73 (0,56 a 0,95); caídas con atención médica RR 0,61 (0,47 a 0,79); 108 ensayos, 23.407 participantes | Sherrington y cols. (2019), Cochrane CD012424.pub2, resumen leído en Europe PMC y DOI confirmado en Crossref |
| Seguridad en la casa RR 0,81 (0,68 a 0,97); taichí RR 0,71 (0,57 a 0,87); multifactorial razón de tasas 0,76 (0,67 a 0,86); 159 ensayos, 79.193 participantes | Gillespie y cols. (2012), Cochrane CD007146.pub3, resumen leído en Europe PMC |
| 684.000 muertes por caída al año; segunda causa mundial de muerte por lesión no intencional; tasa más alta en mayores de 60 años; 37,3 millones de caídas con atención médica al año | OMS, "Falls" (fact sheet) <https://www.who.int/news-room/fact-sheets/detail/falls> |
| Cuartas: mitad legitimaria, cuarta de mejoras y cuarta de libre disposición; legitimarios; acción de reforma en cuatro años | Código Civil, artículos 959, 1167, 1182, 1184, 1195 y 1216 (idNorma=172986), texto oficial leído |
| Donaciones en vida se acumulan imaginariamente al acervo para calcular las cuartas | Código Civil, artículos 1185, 1186 y 1187 |
| Testamento es acto solemne y revocable; testamento abierto ante notario y tres testigos o ante cinco testigos; cerrado ante notario y tres testigos; el testamento solemne es siempre escrito; inhabilidades de los testigos; menciones del artículo 1016; lectura en alta voz; el que no sabe leer ni escribir no puede testar cerrado | Código Civil, artículos 999, 1001, 1008, 1011, 1012, 1014, 1016, 1017, 1021, 1022 y 1215 |
| No existe en Chile el testamento ológrafo (escrito de puño y letra por el testador): el único testamento escrito por el testador sin solemnidades es el privilegiado del artículo 1030 (verbal, militar, marítimo) | Código Civil, artículos 1011, 1030 y 1031 (comparado con el original chino, que sí reconoce el testamento manuscrito) |
| Registro Nacional de Testamentos público, con nóminas de lo otorgado o protocolizado ante notario; informe a $290 | Ley 19.903, artículos 13 y 14 (idLey=19903); artículo 439 del Código Orgánico de Tribunales; ficha ChileAtiende 13922 |
| Posesión efectiva intestada ante el Registro Civil sin abogado; testada o con último domicilio en el extranjero ante tribunal civil con abogado; se otorga a todos los herederos aunque no hayan sido incluidos; publicación en diario regional los días 1 o 15; certificado e inscripciones especiales | Ley 19.903, artículos 1, 2, 3, 6, 7 y 8; ficha ChileAtiende 3364 |
| Aranceles de la posesión efectiva: gratis hasta 15 UTA; 1,6 UTM entre 15 y 45 UTA; 2,5 UTM sobre 45 UTA | Ley 19.903, artículo 11, leído |
| Conversión de esos aranceles: $12.909.780 (15 UTA), $114.754 (1,6 UTM), $179.303 (2,5 UTM) | aritmética propia sobre la UTM de septiembre de 2026 ($71.721) y la UTA 2026 ($860.652), publicadas por el SII en <https://www.sii.cl/valores_y_fechas/utm/utm2026.htm> |
| Beneficio de inventario: se declara en el formulario de la solicitud; se pierde por ocultar bienes de mala fe; responsabilidad limitada al valor de lo recibido | Ley 19.903, artículo 4; Código Civil, artículos 1252, 1256 y 1257 |
| Requisitos de la PGU: 65 años, no estar en el 10% más rico, 20 años de residencia desde los 20 años y 4 en los últimos 5 | Ley 21.419, artículo 10 (idLey=21419), texto oficial leído |
| Monto PGU desde el 1 de febrero de 2026: $231.732 hasta pensión base de $789.139; variable entre $789.140 y $1.252.602; sin derecho desde $1.252.603; $250.275 para 75 años o más con la reforma; causales de suspensión y extinción | ficha ChileAtiende 102077 (HTML descargado y leído) y Superintendencia de Pensiones, preguntas generales <https://www.spensiones.cl/portal/institucional/594/w3-article-15170.html> |
| PGU solicitable desde los 64 años y 9 meses | ficha ChileAtiende 102077 |
| Ley de Fraudes: lo posterior al aviso lo paga el emisor y las cláusulas de prueba se tienen por no escritas; reclamo en 30 días hábiles e incluye 60 días corridos anteriores; denuncia obligatoria y retractación si no se presenta en 30 días corridos; devolución en 10 días hábiles (15 en cajeros automáticos) | Ley 20.009, artículos 3, 4 y 5 (idLey=20009), texto oficial leído |
| Presunción de dolo o culpa grave del usuario: operaciones entre cuentas propias o de parientes, fondos enviados a cuentas registradas con 48 horas de anticipación, claves entregadas voluntariamente, autenticación reforzada con factor de inherencia | Ley 20.009, artículo 5 ter, leído |
| Umbral de restitución de 35 UF (equivalente a $1.437.002) | decreto exento N°473 del Ministerio de Hacienda, de 31 de diciembre de 2025, publicado en el Diario Oficial de 30 de enero de 2026 — PDF descargado y texto extraído |
| Canales de aviso 24/7, número de recepción con fecha y hora, bloqueo y comprobante | CMF, "Ley de Fraudes" <https://www.cmfchile.cl/educa/621/w3-article-29826.html> |
| Información de movimientos de la cuenta de capitalización individual cada cuatro meses, más comisiones y rentabilidad comparadas | Decreto Ley 3.500, artículo 31 (idNorma=7147), texto oficial leído |
| Estafa: engaño que provoca error y disposición patrimonial perjudicial, con la escala de penas según el monto | Código Penal, artículo 467 (idNorma=1984), texto oficial leído |
| Estafa por nombre fingido, poder supuesto, negociación imaginaria, claves ajenas y uso no autorizado de tarjeta de pago | Código Penal, artículo 468 |
| Apropiación indebida de dinero recibido en administración; defraudación abusando de firma en blanco; hacer suscribir un documento con engaño; obtención fraudulenta de pensiones, subsidios o devoluciones del Estado | Código Penal, artículo 470, números 1, 3, 4 y 8 |
| Violencia intrafamiliar incluye el daño a la subsistencia o autonomía económica y cubre expresamente a la persona adulta mayor bajo cuidado o dependencia del grupo familiar | Ley 20.066, artículo 5 (idLey=20066), texto oficial leído |
| Protección con el solo mérito de la denuncia; maltrato habitual con presidio menor en su grado mínimo a medio; maltrato no habitual con multa de 5 a 30 UTM ($358.605 a $2.151.630) | Ley 20.066, artículos 7, 8 y 14, leídos |
| Medidas cautelares del juez de familia: prohibición de acercarse, restricción en el hogar, prohibición de celebrar actos o contratos, medidas de protección para adultos mayores, internación del adulto mayor en situación de abandono, duración de 180 días hábiles renovables por una vez | Ley 19.968, artículo 92 (idLey=19968), texto oficial leído |
| Supervisión del alejamiento por monitoreo telemático | Ley 21.378, que incorpora el artículo 92 bis a la Ley 19.968 (idLey=21378), leída |
| Maltrato relevante a persona mayor con prisión o multa de 1 a 4 UTM ($71.721 a $287.484); trato degradante; inhabilitación para cargos en salud o con relación habitual con adultos mayores; delitos de acción penal pública; agravante cuando el autor tiene encomendado el cuidado | Ley 21.013, Código Penal, artículos 39 ter, 400 y 403 bis a 403 septies (idLey=21013), texto oficial leído |
| Dónde denunciar el maltrato: Carabineros (149 o 133 y Plan Cuadrante), PDI (134), Fiscalía local, Denuncia Seguro 600 400 0101, programa de apoyo a víctimas 600 818 1000, y Tribunal de Familia de la comuna de residencia o por conecta.pjud.cl | SENAMA, "¿Dónde se debe realizar la denuncia?" <https://www.senama.gob.cl/storage/docs/2.pdf> — PDF descargado y texto extraído |
| Concepto de maltrato a las personas mayores, negligencia (activa, pasiva y auton egligencia), abandono y abandono en lugares públicos | SENAMA, "Concepto de Maltrato a las Personas Mayores" <https://www.senama.gob.cl/storage/docs/1.pdf> — PDF descargado y texto extraído |
| Fono Mayor 800 400 035, de 09:00 a 18:00 horas; programa Buen Trato al Adulto Mayor con asesoría y coordinación de casos de maltrato | <https://www.senama.gob.cl/fono-mayor> y <https://www.senama.gob.cl/programa-buen-trato-al-adulto-mayor>, leídos |
| EMPAM: examen periódico voluntario y gratuito, parte de las prestaciones del GES para Fonasa e isapres, una vez al año, para personas de 65 años o más; incluye peso y talla, presión arterial y cuestionarios de riesgo de dependencia; EFAM como evaluación funcional | MINSAL, DIPRECE, "Personas Mayores — Comunidad" <https://diprece.minsal.cl/personas-mayores-comunidad/>, leído |
| El EMPAM evalúa el riesgo de caídas y deriva a un plan de intervención; se repite cada 6 meses o al año según el riesgo de dependencia; deriva al programa Más Adultos Mayores Autovalentes y a ayudas técnicas | Servicio de Salud Metropolitano Occidente, "Examen de Medicina Preventiva del Adulto Mayor" (caché de investigación del repo, `docs/investigacion/_cache/ssmoc_empam.txt`) |
| Manual de aplicación del EMPAM y manual de prevención de caídas en el adulto mayor entre los documentos oficiales del MINSAL | MINSAL, DIPRECE, "Información al Profesional Salud del Adulto Mayor" <https://diprece.minsal.cl/programas-de-salud/programas-ciclo-vital/salud-de-las-personas-mayores-informacion-para-equipos-de-salud/>, leído |
| Talleres del programa Más Adultos Mayores Autovalentes: estimulación de funciones motoras y prevención de caídas, estimulación cognitiva y autocuidado, con duración de tres meses | Ventanilla Única Social, ficha 299 <https://www.ventanillaunicasocial.gob.cl/ficha/299/mas-adultos-mayores-autovalentes>, leída; y Elige Vivir Sano <https://eligevivirsano.gob.cl/programas/23-programa-mas-adultos-mayores-autovalentes/> |
| Pensión de vejez: 65 años hombres y 60 mujeres | Decreto Ley 3.500, artículo 3, leído |
| Trámite de pensión de vejez en la AFP o en sucursal ChileAtiende; documentos; certificado de saldo; envío al SCOMP; ofertas de modalidades de pago | ficha ChileAtiende 5256 (HTML descargado y leído) |
| Reclamos contra AFP, IPS y AFC por la plataforma de atención de la Superintendencia de Pensiones | Superintendencia de Pensiones, consultas y reclamos <https://www.spensiones.cl/apps/consultasWEB/formConsulta.php>, leído |
| Reclamo del dictamen de invalidez por escrito en 15 días hábiles desde la notificación, sin abogado | Decreto Ley 3.500, artículo 11, letra a), leído |
| Papel firmado en blanco: defraudación abusando de firma en blanco | Código Penal, artículo 470, número 3, leído |
| Mandato: definición, formas de constitución, causales de término y revocación expresa o tácita | Código Civil, artículos 2116, 2123, 2163 y 2164, leídos |
| Ley Chile Cuida: derecho al cuidado, cuidados no remunerados reconocidos como trabajo, titulares incluyen a las personas cuidadoras y a las personas mayores, programa nacional de acompañamiento a la dependencia severa, Registro Nacional de Personas Cuidadoras No Remuneradas | Ley 21.805, artículos 1, 2, 3, 8, 23 y 42 (idLey=21805), texto oficial leído; publicada el 16 de febrero de 2026 según metadatos de LeyChile |
| Atención preferente en salud para mayores de 60 años, personas con discapacidad y cuidadores o cuidadoras | Ley 20.584, artículo 5° bis, modificado por la Ley 21.380; ambas leídas. La Ley 21.168 creó el derecho original |
| Registro de Prestadores de Servicios de Apoyos y Cuidados; multa de 5 a 10 UTM ($358.605 a $717.210) a las personas jurídicas privadas que no se inscriban | Ley 21.805, artículos 38, 39 y 41, leídos |
| Programa Cuidados Domiciliarios del SENAMA: 60 años y más, dependencia moderada o severa, sin red de apoyo eficaz, 60% según calificación socioeconómica del Registro Social de Hogares, seis horas semanales, un asistente por cada cinco personas | SENAMA, "Cuidados Domiciliarios" <https://www.senama.gob.cl/cuidados-domiciliarios>, leído |
| Consentimiento informado libre, voluntario, expreso e informado; por escrito en intervenciones quirúrgicas y procedimientos invasivos; prohibición de la eutanasia y del auxilio al suicidio | Ley 20.584, artículo 14, leído |
| Derecho a rechazar tratamiento que prolongue artificialmente la vida en estado terminal, manteniendo soporte ordinario; derecho a vivir con dignidad, a cuidados paliativos, a compañía y asistencia espiritual; alta voluntaria | Ley 20.584, artículos 15, 16 y 18, leídos |
| Comité de ética cuando el profesional duda de la competencia o ve daño grave evitable; su pronunciamiento es solo recomendación; revisión por la Corte de Apelaciones | Ley 20.584, artículo 17, leído |
| Enfermedad terminal: progresiva e irreversible, sin tratamiento curativo, con expectativa de vida inferior a doce meses; derechos a paliativos, a ser informado y a ser acompañado | Ley 21.375, artículos 2 y 5 (idLey=21375), leídos |
| Declaraciones de voluntad anticipadas y acompañantes para la toma de decisiones en salud mental | Ley 21.331, artículo 4 (idLey=21331), texto oficial leído |
| Interdicción por demencia: privación de la administración de los bienes; orden de preferencia para la curaduría (cónyuge, descendientes, ascendientes, hermanos, colaterales hasta cuarto grado, y a falta de todos, curaduría dativa); nulidad de los actos posteriores al decreto | Código Civil, artículos 456, 462 y 465, leídos |
| La declaración de interdicción no se somete a mediación | Ley 19.968, texto oficial leído |
| Polifarmacia: DME -0,22 (IC 95% -0,38 a -0,05) en medicamentos potencialmente inapropiados; RR 0,79 (0,61 a 1,02) en la proporción de pacientes con uno o más; DME -0,81 (-0,98 a -0,64) en omisiones de prescripción; hospitalizaciones y calidad de vida con poca o ninguna diferencia; certeza de baja a muy baja | Rankin y cols. (2018), Cochrane CD008165.pub4 — resumen leído en Europe PMC y DOI confirmado en Crossref |
| Concepto de polifarmacia como cuatro o más medicamentos en personas de 65 años o más (criterio de elegibilidad de la revisión) | Rankin y cols. (2018), Cochrane CD008165.pub4, criterios de selección |

## Notas de método

- El texto de todas las leyes citadas se leyó a través de la API pública de LeyChile
  (`tools/leychile.py`), que devuelve el mismo texto que el visor `bcn.cl/leychile`. En los casos en
  que el extracto venía con notación de versiones, se verificó que el artículo estuviera en la
  versión vigente.
- Los tres PDF que no se pudieron leer con las herramientas del sistema (SENAMA "Concepto de
  Maltrato", SENAMA "¿Dónde se debe realizar la denuncia?" y el decreto de umbral de restitución
  del Diario Oficial) se abrieron extrayendo el texto de los flujos comprimidos del PDF con Python;
  los tres devolvieron texto legible y de ahí salen las citas.
- El original chino reconoce seis formas de testamento (incluido uno manuscrito) y un sistema de
  "tutela designada por escrito" que no existe en Chile. Ninguno de los dos se adaptó por analogía:
  se reemplazaron por el testamento solemne chileno y por la voluntad anticipada del artículo 4 de
  la Ley 21.331 y la interdicción del Código Civil, con sus propios efectos y sus propios límites.
- El ítem de la casa de reposo y el seguro de cuidados de largo plazo del original no tienen
  equivalente chileno equivalente y se eliminaron: en Chile no existe un seguro público de
  dependencia con prestaciones monetarias. Lo que sí existe —el programa de cuidados domiciliarios
  del SENAMA y el Sistema Nacional de Apoyos y Cuidados— está en el ítem 13.
