# Verificación · capítulo 21 — Viajar y vivir afuera

`guia/21-viajar-y-vivir-afuera.md`

## Pendientes abiertos

### 1. El listado de permisos electrónicos del consulado no tiene fecha ni cubre todos los destinos

- `guia/21-viajar-y-vivir-afuera.md` ítem 1, Notas
  Dato: el ítem cita el listado oficial de permisos electrónicos por país (ESTA, eTA, NZeTA, K-ETA,
  ETA-IL, e-Visa de Etiopía, declaración de Sudáfrica, visa electrónica de Cuba, autorización del
  Reino Unido, seguro obligatorio de Zanzibar, biometría en Moscú).
  Sospecha: (no hay valor sospechado) el listado está vigente al momento de la consulta, pero se
  actualiza sin fecha visible y no incluye todos los países con requisitos propios.
  Fuente que no se pudo leer: `https://www.consulado.gob.cl/informacion-para-chilenas-os-que-viajan-fuera-de-chile`
  abre correctamente, pero no publica fecha de última actualización ni un índice por país completo;
  el detalle por destino vive en el sitio oficial de cada país, que no se puede verificar en bloque.
  Cómo cerrarlo: consultar el consulado o la embajada del país de destino acreditado en Chile
  (`https://www.consulado.gob.cl/red/consulados-extranjeros-en-chile`) para cada destino concreto,
  y dejar en el ítem sólo la regla general. No corresponde convertir esto en una lista fija: la
  instrucción del encargo es explícitamente no dar listas de requisitos de entrada por país.

### 2. La página de pasaporte del Registro Civil no se puede leer por consulta automática

- `guia/21-viajar-y-vivir-afuera.md` ítem 2, Notas
  Dato: el ítem cita $69.660 por el pasaporte de 48 páginas y una vigencia de 10 años, y el
  procedimiento de agendamiento con ClaveÚnica.
  Sospecha: (no hay valor sospechado) los valores y la vigencia son los que publica el Registro
  Civil a través de ChileAtiende; no se descarta un cambio de precio posterior.
  Fuente que no se pudo leer: `https://www.registrocivil.cl/principal/servicio/pasaporte` responde
  200 con un desafío anti-robot (captcha) y devuelve un cuerpo vacío; `https://www.registrocivil.cl/`
  entrega la misma página de rechazo. El precio y la vigencia se citan desde
  `https://www.chileatiende.gob.cl/fichas/3445-pasaporte-obtencion-y-renovacion`, que es la ficha
  oficial del propio trámite y declara como fuente al Servicio de Registro Civil.
  Cómo cerrarlo: abrir la página del Registro Civil en un navegador con JavaScript y confirmar
  precio y vigencia vigentes; si el precio cambió, corregir el ítem y anotar la fecha.

### 3. No hay cifra oficial del costo de una evacuación o repatriación médica internacional

- `guia/21-viajar-y-vivir-afuera.md` ítem 5, Notas
  Dato: el ítem sostiene que lo que realmente pesa en una póliza es el tope de gastos médicos y el
  de evacuación o repatriación médica, y fija el nivel de beneficio en medio.
  Sospecha: (no hay valor sospechado) una evacuación médica internacional cuesta decenas de miles
  de dólares, pero no se encontró ninguna cifra oficial ni de la industria publicada por un
  organismo chileno.
  Fuente que no se pudo leer: la Superintendencia de Valores y Seguros / CMF no publica tarifas ni
  costos de referencia de seguros de asistencia en viaje; el Ministerio de Relaciones Exteriores
  (`https://www.consulado.gob.cl/seguro-de-asistencia-en-viaje`) explica la diferencia entre seguro
  y asistencia, pero no da montos ni exige coberturas mínimas.
  Cómo cerrarlo: pedir a la CMF el cuadro de coberturas y topes de los planes de asistencia en
  viaje comercializados en Chile, o tomar la cifra de un reasegurador con publicación oficial. Con
  esa cifra el nivel de beneficio sube de medio a alto.

### 4. El texto de la Ley 18.469 no contiene una regla de cobertura de salud fuera de Chile

- `guia/21-viajar-y-vivir-afuera.md` ítem 5, Notas
  Dato: el ítem no afirma nada sobre Fonasa en el extranjero y se apoya en la declaración del
  consulado ("los costos hospitalarios o asociados a la atención de salud deberán ser cubiertos por
  la persona afectada y/o su familia").
  Sospecha: (no hay valor sospechado) podría existir cobertura por convenio o por modalidad de
  libre elección en casos puntuales, o una norma en el reglamento y no en la ley.
  Fuente que no se pudo leer: la búsqueda de "fuera del territorio" y "extranjero" en el texto
  oficial de la Ley 18.469 descargado desde LeyChile no devolvió ninguna regla de atención en el
  exterior. El sitio de Fonasa no publicó en la sesión de escritura una ficha sobre atención fuera
  de Chile.
  Cómo cerrarlo: preguntar por escrito a Fonasa si existe cobertura de prestaciones realizadas en
  el extranjero y en qué casos; mientras no haya respuesta, el ítem se mantiene como está.

### 5. El MINSAL no publica el listado por país de vacunas exigidas ni los valores de cada vacuna

- `guia/21-viajar-y-vivir-afuera.md` ítem 6, Notas
  Dato: el ítem dice que las vacunas para viajeros son de costo del usuario y que el MINSAL no
  publica los valores; y que la lista de países con riesgo de fiebre amarilla y de países que
  exigen el certificado está en la OMS.
  Sospecha: (no hay valor sospechado) existe un arancel referencial de las vacunas internacionales
  en el sector privado, pero no es un valor oficial publicado por el MINSAL.
  Fuente que no se pudo leer: `https://www.minsal.cl/vacunatorios-internacionales/` dice
  textualmente "Las vacunas internacionales son de costo del usuario y nuestro servicio no maneja
  los valores" y no publica la lista de países con requisitos de vacunación;
  `https://www.minsal.cl/vacunacion-para-viajeros/` devuelve una imagen y no una página de texto.
  Cómo cerrarlo: consultar los vacunatorios internacionales autorizados por cada SEREMI (el listado
  está en la ficha del MINSAL) para obtener valores reales de fiebre amarilla, hepatitis A y
  fiebre tifoidea, y citarlos con fecha.
  La lista de países que exigen el certificado de fiebre amarilla se lee en la OMS,
  `https://www.who.int/travel-advice` (documento "Countries with risk of yellow fever transmission
  and countries requiring yellow fever vaccination"), que está en inglés y se actualiza sin aviso.

### 6. El arancel de la residencia temporal se publica por nacionalidad y sin monto

- `guia/21-viajar-y-vivir-afuera.md` ítem 8, Notas
  Dato: el ítem cita la residencia definitiva ($142.726), la carta de nacionalización ($39.742) y
  la prórroga de permanencia transitoria (US$100), y deja la residencia temporal sin monto.
  Sospecha: (no hay valor sospechado) el arancel de la residencia temporal se calcula por
  nacionalidad, con una tabla que la página no despliega en el HTML servido.
  Fuente que no se pudo leer: `https://serviciomigraciones.cl/aranceles-migratorios/` muestra el
  título "Aranceles según nacionalidad" sin los montos y con el dólar de referencia de $925,25
  (Diario Oficial N°44.413 del 28 de agosto de 2026, válido hasta el 30 de septiembre de 2026).
  Cómo cerrarlo: reservar la tabla completa desde el sitio de SERMIG o pedirla por su portal de
  ayuda, y anotar el monto con la fecha del dólar con que se calculó.

### 7. No se obtuvo el listado de los 27 países con convenio de seguridad social vigente

- `guia/21-viajar-y-vivir-afuera.md` ítem 10, Notas
  Dato: el ítem dice que Chile tiene 27 convenios de seguridad social vigentes y uno multilateral
  iberoamericano, sin nombrar los países.
  Sospecha: (no hay valor sospechado) el listado existe y debería estar publicado por la
  Superintendencia de Pensiones o por el Ministerio de Relaciones Exteriores.
  Fuente que no se pudo leer: `https://www.chileatiende.gob.cl/fichas/112097-prorroga-de-desplazamiento-del-convenio-internacional-de-seguridad-social`
  confirma el número y remite al sitio de la Superintendencia de Pensiones; las páginas de
  convenios probadas en `https://www.spensiones.cl/` devolvieron 398 o 220 bytes, sin contenido.
  Cómo cerrarlo: consultar la sección "Convenios de seguridad social" de la Superintendencia de
  Pensiones con navegador y agregar al ítem la lista o su enlace directo.

### 8. No se verificó si el Registro de Deudores de Alimentos afecta también la cédula de identidad

- `guia/21-viajar-y-vivir-afuera.md` ítem 12, Notas
  Dato: el ítem afirma que con inscripción vigente se rechaza el pasaporte y la licencia de
  conducir, y no se pronuncia sobre la cédula de identidad.
  Sospecha: (no hay valor sospechado) la ley 21.389 regula expresamente el pasaporte (artículo 32)
  y la licencia de conducir (artículo 33); no se encontró mención a la cédula.
  Fuente que no se pudo leer: se leyó el texto completo de la Ley 21.389 desde LeyChile
  (`https://www.bcn.cl/leychile/navegar?idLey=21389`) y el artículo 32 habla sólo del pasaporte;
  podría haber una regla en el reglamento o en una resolución del Servicio de Registro Civil que
  no se consultó.
  Cómo cerrarlo: revisar el reglamento de la Ley 21.389 y las instrucciones del Registro Civil
  sobre emisión de cédula de identidad.

### 9. Discrepancia entre dos páginas de Aduanas sobre el monto de las mercancías sin carácter comercial

- `guia/21-viajar-y-vivir-afuera.md` ítem 13, Notas
  Dato: el ítem cita los dos valores en disputa: US$4.050 y US$3.000 valor FOB.
  Sospecha: (no hay valor sospechado) el valor vigente sería US$4.050, que aparece en la página de
  equipaje de viajero y es el más reciente de las dos; el US$3.000 FOB viene de la sección de
  preguntas frecuentes, con fecha de 2007 en la URL.
  Fuente que no se pudo leer: no existe en el sitio de Aduanas una página única y fechada con el
  cuadro de franquicias del viajero; `https://www.aduana.cl/equipaje-de-viajero-y-viajera/aduana/2018-12-28/083959.html`
  dice US$4.050 y `https://www.aduana.cl/preguntas-frecuentes-viajeros/aduana/2007-02-28/143620.html`
  dice US$3.000 FOB.
  Cómo cerrarlo: preguntar a Aduanas por el valor vigente y la norma que lo fija, y dejar un solo
  número con su fecha. Mientras no haya respuesta, el ítem cita ambos.

### 10. El monto de la multa por declaración jurada falsa ante el SAG no está publicado

- `guia/21-viajar-y-vivir-afuera.md` ítem 14, Notas
  Dato: el ítem dice que declarar mal "será sancionado con multa de conformidad a la ley" y no da
  cifra.
  Sospecha: (no hay valor sospechado) la sanción debería estar en la ley 18.755 o en el reglamento
  de la declaración jurada, con monto en UTM.
  Fuente que no se pudo leer: la ficha del trámite
  (`https://www.sag.gob.cl/tramites/declaracion-jurada-sag-sobre-ingreso-de-productos-de-origen-vegetal-o-animal-chile`)
  remite a "multa de conformidad a la ley" sin indicar la norma ni el monto; la página de ingreso
  de productos
  (`https://www.sag.gob.cl/ambitos-de-accion/productos-de-origen-vegetal-yo-animal-artesanias-y-otros`)
  hace lo mismo.
  Cómo cerrarlo: buscar la sanción en la ley 18.755 (SAG) y en el decreto que fija la declaración
  jurada, o preguntar por escrito a oficina.informaciones@sag.gob.cl.

### 11. El arancel notarial de la autorización de viaje del menor no tiene valor oficial publicado

- `guia/21-viajar-y-vivir-afuera.md` ítem 17, Costo y Notas
  Dato: el ítem estima el costo en "decenas de miles de pesos" y lo marca como pendiente.
  Sospecha: (no hay valor sospechado) el arancel lo fija cada notaría dentro del arancel mínimo del
  Colegio de Notarios, y varía por región.
  Fuente que no se pudo leer: no existe una tabla oficial del arancel de la autorización notarial
  de viaje; el arancel del Colegio de Notarios de Santiago no se pudo abrir en la sesión de
  escritura.
  Cómo cerrarlo: consultar el arancel vigente del Colegio de Notarios o pedir el valor en una
  notaría concreta y citarlo como referencia, con la advertencia de que varía.

### 12. No se confirmó plazo de respuesta del trámite de localización internacional de familiares

- `guia/21-viajar-y-vivir-afuera.md` ítem 18, Notas
  Dato: el ítem describe el trámite de localización y el de información sobre personas detenidas,
  sin dar plazos.
  Sospecha: (no hay valor sospechado) el trámite se resuelve "según cada caso" y no hay un plazo
  publicado.
  Fuente que no se pudo leer: `https://www.consulado.gob.cl/servicios/localizacion-internacional-de-familiares`
  no indica plazos ni costos; el Servicio Social Consular remite al consulado respectivo.
  Cómo cerrarlo: preguntar al Departamento de Servicio Social Consular del Ministerio de
  Relaciones Exteriores cuál es el tiempo de tramitación típico y si existe un plazo máximo.

## Cifras que sí quedaron verificadas contra el texto oficial

Se dejan registradas para no tener que repetir la búsqueda, todas con el texto leído:

| Dato en el capítulo | Fuente leída |
|---|---|
| Cuatro categorías de ingreso (permanencia transitoria, residente oficial, temporal, definitivo) | Ley 21.325, artículo 26 (idLey=21325), texto completo desde LeyChile |
| Residencia temporal: hasta 2 años, prorrogable por 2 años más; plazo de 90 días corridos para ingresar si se otorgó fuera de Chile | Ley 21.325, artículo 72 |
| Residencia definitiva: radicarse indefinidamente, sin visa para reingresar; postulación con al menos 24 meses de residencia temporal; revocación tácita a los 2 años de ausencia | Ley 21.325, artículos 78, 79 y 83 |
| Permanencia transitoria: hasta 90 días, prorrogable por 90 más, una sola vez; su titular no puede trabajar | Ley 21.325, artículos 47, 48 y 50; SERMIG, `https://serviciomigraciones.cl/permanencia-transitoria/` |
| Multas migratorias: ½ a 10 UTM (vencido hasta 180 días), 1 a 10 UTM (más de 180 días), ½ a 5 UTM (trabajar sin autorización), ½ a 2 UTM (no pedir cédula en plazo); rebaja de 50% por autodenuncia y 25% por pago en 5 días hábiles; no sanción si el residente sale dentro de 30 días corridos | Ley 21.325, artículos 106, 107, 109, 119 y 121 |
| Impedimento de egreso por arraigo judicial o prohibición de salir del país | Ley 21.325, artículo 31 |
| Pasaporte rechazado sin más trámite con inscripción vigente en el Registro de Deudores de Alimentos; licencia de conducir igual; excepción por orden judicial con vigencia limitada de 6 meses a 1 año; cancelación por pago íntegro o acuerdo de pago | Ley 21.389, artículos 25, 26, 32, 33 y 34, texto completo desde LeyChile |
| Denegación de embarque por sobreventa: opciones del pasajero y tabla de compensación de 2 a 20 UF | Código Aeronáutico, artículo 133 (idNorma=30287); tabla publicada por SERNAC en `https://www.sernac.cl/portal/604/w3-article-89186.html` |
| Prestaciones asistenciales, restitución de tasas en 10 días, no uso de una fracción, modificación por certificado médico, asientos contiguos para menores de 14 años | Código Aeronáutico, artículos 133 A, 133 C, 133 H, 133 I y 133 J |
| Indemnización de 40 UF por pasajero por pérdida de equipaje en vuelo nacional | Código Aeronáutico, artículo 148 |
| Declaración de dinero sobre US$10.000 y retención total del efectivo con acción penal inmediata | Ley 19.913, artículo 4 (idLey=19913); Aduanas, `https://www.aduana.cl/declaracion-de-dinero/aduana/2018-12-28/084148.html` |
| Franquicia del viajero: equipaje sin carácter comercial, duty free hasta US$675, mercancías hasta US$4.050/US$1.000 facturado, plazo de 120 días | Aduanas, `https://www.aduana.cl/equipaje-de-viajero-y-viajera/aduana/2018-12-28/083959.html` y `https://www.aduana.cl/preguntas-frecuentes-viajeros/aduana/2007-02-28/143620.html` |
| Declaración jurada SAG obligatoria desde los 18 años, individual, en línea o en papel, con eliminación del producto de riesgo | SAG, `https://www.sag.gob.cl/tramites/declaracion-jurada-sag-sobre-ingreso-de-productos-de-origen-vegetal-o-animal-chile` |
| Certificado Zoosanitario de Exportación de mascotas: 0,41 UTM por una y 0,22 UTM por cada adicional; certificado de salud de no más de 10 días; inscripción en el Registro Nacional de Mascotas | SAG, `https://www.sag.gob.cl/tramites/solicitud-de-certificado-zoosanitario-de-exportacion-para-salir-de-chile-con-perros-gatos-y-hurones-mascotas` |
| Autorización notarial de viaje del menor, por escritura pública o privada ante notario, y autorización del progenitor que no lo acompaña | Ley 16.618, artículo 49 (idLey=16618), texto desde LeyChile; Consulado, `https://www.consulado.gob.cl/cuando-viaja-un-menor-de-edad` |
| Límites de lo que puede y no puede hacer un consulado, incluida la no asunción de gastos de hospitalización, abogados y repatriación | Consulado, `https://www.consulado.gob.cl/que-puede-y-que-no-puede-hacer-un-consulado` |
| Trata de personas: conducta y pena (reclusión mayor en grados mínimo a medio y multa de 50 a 100 UTM); residencia temporal mínima de 12 meses para las víctimas | Código Penal, artículo 411 quáter, incorporado por la Ley 20.507 (idLey=20507); Ley 21.325, artículo 71 |
| Convenios internacionales de seguridad social: 27 vigentes y uno multilateral iberoamericano; certificado de desplazamiento al menos un mes antes del viaje | ChileAtiende, ficha 112097, publicada por la Superintendencia de Pensiones |
| Vacunación del viajero: no se administra en atención primaria, requiere receta médica, se pide con un mes de anticipación, fiebre amarilla obligatoria para entrar a algunos países | MINSAL, `https://www.minsal.cl/vacunatorios-internacionales/` y `https://www.minsal.cl/recomendaciones-para-viajeros/` |
| Fiebre amarilla: 15% de formas graves, 50% de letalidad en esa fase, vacuna de por vida con una dosis, 27 países africanos y 13 latinoamericanos de alto riesgo | OMS, `https://www.who.int/news-room/fact-sheets/detail/yellow-fever` |

## Conversiones usadas

- UTM de septiembre de 2026: $71.721 (`https://www.sii.cl/valores_y_fechas/utm/utm2026.htm`).
- UF del 20 de septiembre de 2026: $40.975,41 (`https://www.sii.cl/valores_y_fechas/uf/uf2026.htm`).
- Dólar de referencia de SERMIG: $925,25 (Diario Oficial N°44.413 del 28 de agosto de 2026,
  `https://serviciomigraciones.cl/aranceles-migratorios/`).
