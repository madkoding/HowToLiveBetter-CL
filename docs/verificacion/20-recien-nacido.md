# Verificación · capítulo 20, El recién nacido

Pendientes abiertos al escribir `guia/20-recien-nacido.md`. Cada uno calza con una marca
`POR VERIFICAR` en el ítem correspondiente.

---

- `guia/20-recien-nacido.md` ítem 1, Notas
  Dato: el ítem no da un precio de referencia 2026 para una cuna y un colchón firmes, y remite el
  costo de comprarlos a la nota.
  Sospecha: (no hay valor sospechado) una cuna corral con colchón en comercio establecido debería
  costar del orden de las decenas de miles a los cientos de miles de pesos, pero no se pudo
  confirmar ningún valor.
  Fuente que no se pudo leer: no existe lista oficial de precios de artículos de puericultura. El
  Servicio Nacional del Consumidor publica estudios de precios de productos específicos, no un
  catálogo permanente de cunas; el explorador de precios de la Superintendencia de Salud cubre
  prestaciones de salud, no bienes de comercio. La cuna corral que entrega el Programa de Apoyo al
  Recién Nacido se cita desde su propia ficha, no con precio.
  Cómo cerrarlo: cotizar una cuna corral con colchón y una cuna fija con colchón en dos o tres
  tiendas de comercio establecido y dejar el rango con su fecha de referencia, o bien citar el
  precio del bien cuando exista en el catálogo de ChileCompra. Mientras no exista, el ítem no cita
  ninguna cifra de precio y dice explícitamente que no se pudo verificar.

- `guia/20-recien-nacido.md` ítem 13, Notas
  Dato: el ítem afirma que "en los hospitales donde se hace de rutina no te tienes que preocupar de
  nada" y advierte que eso hay que confirmarlo si el parto fue fuera de un hospital, pero no afirma
  que el sistema público chileno administre vitamina K de rutina ni por qué vía.
  Sospecha: (no hay valor sospechado) la profilaxis con vitamina K intramuscular al nacer es
  práctica estándar en las maternidades chilenas, pero no se encontró la norma que lo instruya.
  Fuente que no se pudo leer: la Norma Técnica para la Supervisión de Salud Integral de Niños y
  Niñas de 0 a 9 años en la Atención Primaria de Salud (MINSAL, 2021, capítulo 3,
  <https://www.minsal.cl/wp-content/uploads/2021/12/Capi%CC%81tulo-3-Web.pdf>) lista, entre los
  procedimientos de la maternidad que se verifican en el control de la díada, el tamizaje de
  hipotiroidismo congénito (TSH), la evaluación auditiva con emisiones otoacústicas, la muestra de
  fenilcetonuria (PKU) y las vacunas BCG y hepatitis B; no menciona la vitamina K. Que no la liste
  no prueba que no se aplique en la maternidad: esa norma regula la atención primaria, y la
  profilaxis se administra en el nivel hospitalario, fuera de su alcance. No se encontró una
  resolución, circular o protocolo de MINSAL publicada sobre administración de vitamina K al recién
  nacido.
  Cómo cerrarlo: consultar a MINSAL (Departamento de Ciclo Vital, Programa Nacional de Salud de la
  Infancia) o a la Sociedad Chilena de Pediatría la norma o protocolo de profilaxis con vitamina K
  del recién nacido en Chile, con la vía y la dosis oficiales, y agregarla al ítem con esa fuente.
  Mientras no exista, el ítem cita solo el consenso belga con su DOI y no afirma nada sobre el
  protocolo chileno.

- `guia/20-recien-nacido.md` ítem 18, Notas
  Dato: el ítem cita la prohibición de exigir dinero, cheques u otros instrumentos financieros para
  garantizar el pago de una atención de urgencia, tomada del texto de la Ley 19.650 que modifica el
  DFL 1 de 2005 del Ministerio de Salud, pero no indica el número del artículo del texto refundido
  vigente donde quedó.
  Sospecha: (no hay valor sospechado) la frase quedó en el artículo 24 y siguientes del DFL 1 de
  2005 según el texto de la ley modificatoria, y en guia/07-sin-plata-que-reclamar.md el mismo
  contenido se cita como modificación a la Ley 18.469.
  Fuente que no se pudo leer: el texto refundido del DFL 1 de 2005 del Ministerio de Salud no se
  pudo descargar con `tools/leychile.py`; hay que ir con un `idNorma` conocido y la búsqueda
  temática de LeyChile no sirve para buscar por materia, como está anotado en
  `docs/investigacion/anclas-verificadas.md`. El texto de la Ley 19.650 sí se descargó y se leyó
  completo.
  Cómo cerrarlo: abrir el texto refundido del DFL 1 de 2005 en LeyChile y ubicar el artículo que
  contiene la prohibición en su numeración definitiva. Mientras no exista, el ítem cita la ley
  modificatoria tal como se leyó y no afirma un número de artículo.

## Notas de fuentes que sí abrieron pero conviene tener presentes

- Los documentos de la Norma Técnica 2021 se citan por sus dos capítulos, que abren los dos:
  capítulo 3 (supervisión por edades y banderas rojas) y capítulo 4 (instrumentos, curvas de
  fototerapia y cartilla de colores de deposiciones). El capítulo 3 se leyó completo en PDF.
- `https://www.cdc.gov/` responde 403 a la consulta automática en todos sus caminos (muerte súbita,
  trauma craneal abusivo, botulismo), así que no se cita como fuente de nada: el botulismo infantil
  se cita por la ficha de la OMS, que abre, y la evidencia sobre trauma craneal infligido por el
  estudio de Keenan y cols. con su DOI.
- `https://www.conaset.cl/` no respondió a la consulta automática en el momento de escribir; la
  normativa de sillas de retención infantil se cita a través del capítulo 01, que ya la verificó y
  dejó su propio pendiente sobre el número de artículo vigente de la Ley de Tránsito.

## Cerrados

(nada cerrado todavía: el capítulo se escribió completo en una pasada)

## Pendiente que se cerró al reescribir el ítem 18

El ítem 18 original era "En una urgencia vital no te pueden pedir cheque ni dinero por adelantado,
ni negarte la atención", y tenía una marca `POR VERIFICAR` sobre el número de artículo del texto
refundido del DFL 1 de 2005 donde quedó la prohibición de exigir dinero, cheques u otros
instrumentos financieros en garantía. Se **eliminó el ítem completo** y se reemplazó por el ítem
18 actual, sobre el equipo de cabecera y la derivación asistida del recién nacido, que es
específico de este capítulo y aporta algo que no estaba en otro lado. La razón es que el contenido
de la ley de urgencia ya estaba cubierto en `guia/07-sin-plata-que-reclamar.md` ítem 8, y el
contrato prohíbe duplicar: un capítulo no repite lo que está en otro, pone una línea cruzada. La
prohibición de exigir cheques o dinero en garantía se cita ahora como referencia cruzada al
capítulo 07, que es donde corresponde. Los datos no se perdieron: siguen en el capítulo 07.

