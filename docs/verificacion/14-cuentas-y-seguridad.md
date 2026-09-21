# Verificación · capítulo 14, Cuentas y seguridad

Pendientes abiertos al escribir `guia/14-cuentas-y-seguridad.md`. Cada uno calza con una marca
`POR VERIFICAR` en el ítem correspondiente.

---

- `guia/14-cuentas-y-seguridad.md` ítem 4, Notas
  Dato: el ítem dice que la ClaveÚnica es la llave de los trámites del Estado y que el Registro
  Civil entrega, en la misma ficha, el procedimiento para activarle un segundo factor.
  Sospecha: debería existir una página oficial con el catálogo de trámites que usan ClaveÚnica y
  con el trámite de suspensión o bloqueo de la ClaveÚnica cuando se pierde o se compromete.
  Fuente que no se pudo leer: `https://claveunica.gob.cl/` y
  `https://claveunica.gob.cl/preguntas-frecuentes` abren, pero son una aplicación de una sola
  página: el HTML que entrega el servidor son 5.840 bytes con el texto
  `{"title":"Portal ciudadano ClaveÚnica"}` y nada del contenido, que se arma con JavaScript.
  La búsqueda temática no devolvió una ficha de ChileAtiende para "bloquear ClaveÚnica" ni un
  listado de los trámites habilitados; la página `https://claveunica.gob.cl/tramites` que aparece
  en los resultados de búsqueda responde con el mismo esqueleto vacío.
  Cómo cerrarlo: llamar al Registro Civil (600 360 33 03) o pedir por Ley de Transparencia al
  Servicio de Registro Civil e Identificación el listado de trámites que habilitan ClaveÚnica y
  el procedimiento vigente de suspensión o bloqueo. Mientras no exista ese documento, el ítem
  solo cita lo que sí está leído: la descripción, el requisito de edad y cédula, los canales de
  solicitud y los pasos del segundo factor.

- `guia/14-cuentas-y-seguridad.md` ítem 6, Notas
  Dato: el teléfono para pedir el bloqueo temporal de la cédula de identidad, y en particular el
  vigente desde el extranjero.
  Sospecha: la única cifra que el capítulo escribe es el 600 370 2000, opción uno, que publica
  ChileAtiende y que sirve dentro de Chile. Los números para llamar desde el extranjero no
  coinciden entre las fuentes que los publican:
  - `https://www.chileatiende.gob.cl/fichas/3430-cedula-de-identidad` : +56 2 2712 06 90.
  - `https://www.registrosciviles.cl/bloqueos/` : +56 2 2429 7705.
  - `https://www.gob.cl/noticias/como-bloquear-la-cedula-de-identidad/` (publicación de 2023):
    +56 2 2782 24 84.
  Fuente que no se pudo leer: `https://www.registrocivil.cl/` y sus rutas de servicios en línea
  (incluida la del bloqueo de cédula) responden 200 a la consulta automática pero entregan un muro
  de seguridad ("Request Rejected ... your support ID is ..."), así que la página del propio
  servicio de bloqueo no se pudo leer. `https://www.registrosciviles.cl/bloqueos/` sí abre, pero
  esa misma página declara por escrito "no es un sitio web oficial", así que no se usa como
  fuente del ítem: se reemplazó por la ficha de ChileAtiende y por la Ley 19.948, que es la que
  crea el bloqueo y su presunción de no uso.
  Cómo cerrarlo: confirmar el número vigente en cualquier oficina del Registro Civil o por
  Ley de Transparencia, y recién entonces reponer el dato para el extranjero.

- `guia/14-cuentas-y-seguridad.md` ítem 9, Notas
  Dato: "en Chile se roban cerca de 500 mil teléfonos al año y solo el 50% de los equipos
  solicita el bloqueo".
  Sospecha: la cifra debería tener una fuente estadística primaria; un valor del orden de
  500.000 equipos al año es plausible frente a las cifras de robos con violencia e intimidación,
  pero no se pudo contrastar.
  Fuente que no se pudo leer: el dato está citado textualmente de la campaña oficial
  `https://www.gob.cl/noticias/telefono-robado-telefono-bloqueado-guia-que-hacer--victima-delito/`
  (8 de julio de 2026, Subsecretaría de Prevención del Delito y Subtel), que es una noticia del
  Gobierno y no una estadística del INE ni del Ministerio Público. No se encontró la fuente
  primaria en el sitio de Subtel ni en el de la Subsecretaría de Prevención del Delito.
  Cómo cerrarlo: buscar la serie de denuncias por robo de teléfono en las estadísticas del
  Ministerio Público o en la ENUSC del INE; si la cifra no se puede reponer, dejarla solo como
  afirmación de la campaña, que es como está redactada.

- `guia/14-cuentas-y-seguridad.md` ítem 11, Notas
  Dato: si existe un canal o una unidad específica de la PDI para denunciar delitos informáticos
  y suplantación de identidad.
  Sospecha: la PDI tiene unidades especializadas y un canal de denuncia en línea, pero no se pudo
  confirmar su nombre ni el procedimiento vigente, así que el ítem cita solo la ficha de
  ChileAtiende, que describe la denuncia general ante cualquier unidad.
  Fuente que no se pudo leer: `https://www.pdichile.cl/` responde 403 a la consulta automática
  (bloqueo del servidor). La alternativa leída fue la ficha de ChileAtiende
  `https://www.chileatiende.gob.cl/fichas/1795-denunciar-un-delito`, publicada por la PDI, que sí
  abre y cita los artículos 173 y 174 del Código Procesal Penal.
  Cómo cerrarlo: confirmar en el sitio institucional de la PDI (o por Ley de Transparencia) si
  existe una unidad de ciberdelitos con atención al público y su canal de denuncia, y agregarlo
  al ítem si existe.

- `guia/14-cuentas-y-seguridad.md` ítem 12, Notas
  Dato: si sigue existiendo un buscador oficial para comprobar si una tienda en línea es el sitio
  verdadero.
  Sospecha: el buscador de sitios comerciales oficiales que lanzaron el SERNAC y el CSIRT en 2020
  ("No hagas click") parece descontinuado, y una guía no puede mandar a un sitio que ya no está.
  Fuente que no se pudo leer: `nohagasclick.csirt.gob.cl` no resuelve (el nombre de dominio no
  existe), `csirt.gob.cl/nohagasclick` responde 404 y el sitio del CSIRT (200) no enlaza ese
  buscador. La única fuente que queda es la noticia de 2020 del SERNAC
  `https://www.sernac.cl/portal/604/w3-article-60009.html`, que sí abre y describe la herramienta;
  ese enlace queda en Fuentes del ítem como constancia histórica, no como instrucción vigente, y
  la recomendación de comprobar el dominio ahí se sacó del texto y de las Notas.
  Cómo cerrarlo: preguntar al SERNAC o al CSIRT Nacional si existe un reemplazo vigente del
  buscador; si lo hay, reponer la recomendación con su dirección.

- `guia/14-cuentas-y-seguridad.md` ítem 16, Notas
  Dato: si alguna fuente oficial chilena recomienda revisar la lista de aparatos con la sesión
  abierta de cada cuenta.
  Sospecha: esa lista existe en la configuración de las cuentas y era la base del ítem en el
  primer borrador, pero al revisar las fuentes no aparece respaldada por ninguna recomendación
  institucional chilena, así que el ítem se reescribió sobre lo que sí está publicado.
  Fuente que no se pudo leer: se revisaron los Ciberconsejos de la ANCI
  (`https://anci.gob.cl/ciberconsejos/`) y la guía de los 9 básicos
  (`https://anci.gob.cl/9basicos/` y su PDF
  `https://anci.gob.cl/documents/4808/Guia_9_basicos_en_Ciberseguridad_2025_OK.pdf`), leída
  completa: ninguno menciona la revisión de sesiones abiertas. Lo que sí está leído y ahora
  sostiene el ítem es el punto "Minimizar privilegios" de esa guía (permisos mínimos, retiro de
  permisos al terminar la tarea, baja de cuentas inactivas tras un período de inactividad) y el
  Ciberconsejo sobre aprobar solicitudes en la app de segundo factor.
  Cómo cerrarlo: revisar la Guía de los 9 básicos y los Ciberconsejos vigentes al actualizar el
  capítulo; si aparece una recomendación institucional sobre sesiones abiertas, agregarla y subir
  la evidencia del ítem a B o A según lo que diga la fuente.

- `guia/14-cuentas-y-seguridad.md` ítem 14, Notas
  Dato: el canal para reclamar ante la Agencia de Protección de Datos Personales por el tratamiento
  de datos biométricos.
  Sospecha: la Agencia la crea la Ley 21.719 (publicada el 13 de diciembre de 2024), con entrada
  en vigencia el 1 de diciembre de 2026; al escribir este capítulo todavía no debería existir su
  sitio ni su procedimiento de reclamo publicado, pero hay que confirmarlo y no suponerlo.
  Fuente que no se pudo leer: `https://www.agenciaprotecciondedatos.gob.cl/` no resuelve
  (error de resolución de nombre) y la búsqueda no devolvió un sitio oficial de la Agencia; los
  resultados que aparecen son sitios privados de asesoría. Lo único oficial leído es el texto de
  la ley en LeyChile (`https://www.bcn.cl/leychile/navegar?idLey=21719`, artículos 30 y 30 bis,
  que crean la Agencia y fijan sus funciones, y el artículo 15 ter, que exige evaluación de
  impacto cuando el tratamiento implique datos sensibles o biométricos).
  Cómo cerrarlo: revisar el sitio institucional de la Agencia y el Diario Oficial en los meses
  previos al 1 de diciembre de 2026 y reponer en el ítem el canal de reclamo cuando esté
  publicado.

- `guia/14-cuentas-y-seguridad.md` ítems 14 y 15, Fuentes
  Dato: la guía de la Secretaría de Gobierno Digital sobre la Ley 21.719
  (`https://wikiguias.digital.gob.cl/datos-personales/guia-practica-implementacion-nueva-ley-datos-personales`)
  se citó en un primer borrador y se sacó del capítulo.
  Motivo: con la consulta de `tools/verificar.py --urls` (urllib, agente `Mozilla/5.0
  (verificador HTLB-CL)`) responde HTTP 404, aunque con `curl` y con un agente de navegador
  responde 200. Como el verificador del repo usa urllib y reportarlo daría error, los dos ítems
  quedaron apoyados solo en el texto de la ley en LeyChile, que sí abre por las dos vías. La
  página de la guía se cita acá como referencia útil, no como fuente de los ítems.

---

## Fuentes que se revisaron y sí abren

Todas las siguientes respondieron 200 a la consulta automática (agente
`Mozilla/5.0 (verificador HTLB-CL)`, GET, sin redirecciones a muros de pago):

- ClaveÚnica del Registro Civil: <https://www.chileatiende.gob.cl/fichas/11331-clave-unica>,
  <https://www.claveunica.gob.cl/>
- Cédula y bloqueo: <https://www.chileatiende.gob.cl/fichas/3430-cedula-de-identidad>,
  Ley 19.948 en LeyChile <https://www.bcn.cl/leychile/navegar?idLey=19948>. El sitio
  `https://www.registrocivil.cl/` y `https://www.registrosciviles.cl/bloqueos/` no se usan como
  fuentes del capítulo (el primero responde con un muro de seguridad y el segundo declara no ser
  oficial): ver ítem 6.
- Denuncia: <https://www.chileatiende.gob.cl/fichas/1795-denunciar-un-delito>
- Informe de deudas: <https://www.chileatiende.gob.cl/fichas/2614-informe-de-deudas-del-sistema-financiero>,
  <https://conocetudeuda.cmfchile.cl/> y
  <https://www.cmfchile.cl/portal/principal/623/w4-article-78824.html> (acceso con ClaveÚnica)
- CMF: <https://www.cmfeduca.cl/educa/621/w3-article-29826.html>,
  <https://www.cmfeduca.cl/educa/621/w3-article-52008.html>
- Leyes en LeyChile: 20.009 (`idLey=20009`), decreto 473 exento del umbral
  (`idNorma=1220909`), 19.628 (`idLey=19628`), 21.719 (`idLey=21719`),
  19.496 (`idLey=19496`), Reglamento de Comercio Electrónico (`idNorma=1165504`),
  19.948 (`idLey=19948`) y Ley 21.729 sobre registro e individualización de usuarios telefónicos
  (`idNorma=1211063`, no citada en el capítulo pero leída para el bloqueo de IMEI).
- SERNAC: <https://www.sernac.cl/portal/607/w3-article-56289.html>,
  <https://www.sernac.cl/portal/604/w3-propertyvalue-20982.html>,
  <https://www.sernac.cl/portal/617/w3-propertyvalue-64530.html>,
  <https://www.sernac.cl/portal/604/w3-article-60009.html> (noticia de 2020, ver ítem 12)
- Subtel y campaña de bloqueo: <https://www.subtel.gob.cl/robo-de-equipos-a-usuarios/>,
  <https://www.gob.cl/noticias/telefono-robado-telefono-bloqueado-guia-que-hacer--victima-delito/>
- ANCI: <https://anci.gob.cl/ciberconsejos/ciberconsejos-mejor-un-gestor-que-en-el-navegador/>,
  <https://anci.gob.cl/ciberconsejos/ciberconsejos-fijate-en-lo-que-autorizas/>,
  <https://anci.gob.cl/ciberconsejos/ciberconsejos-el-fraude-de-la-cuenta-bancaria-bloqueada/>,
  <https://anci.gob.cl/ciberconsejos/ciberconsejos-cuando-cambiar-nuestras-claves/>,
  <https://anci.gob.cl/9basicos/>,
  <https://anci.gob.cl/documents/4808/Guia_9_basicos_en_Ciberseguridad_2025_OK.pdf>,
  <https://ciberlupa.anci.gob.cl/>
- Datos personales: <https://wikiguias.digital.gob.cl/datos-personales/guia-practica-implementacion-nueva-ley-datos-personales>
- Estudios y cifras: <https://doi.org/10.1145/3308558.3313481> (el DOI resuelve por Crossref; la
  URL de doi.org responde 403 a la consulta automática), el mismo estudio en Semantic Scholar
  <https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3308558.3313481> (de ahí salen el
  resumen y las cifras de 350.000 intentos, 1,2 millones de usuarios, 94%, 10%, 100%, 73%, 52% y
  97%), <https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html> (cifras
  de SMS, confirmación en el aparato y desafíos de conocimiento),
  <https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf>
  (tabla 1, formas de segundo factor de más fuerte a más débil),
  <https://pages.nist.gov/800-63-3/sp800-63b.html> (secciones 5.1.1.2 y 5.2.10),
  <https://www.ndss-symposium.org/wp-content/uploads/2017/09/06_1_1.pdf>,
  <https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-florencio.pdf>
  (las cifras de 6,5 claves, 3,9 sitios y 25 cuentas son de Florêncio y Herley 2007, citadas
  dentro de este trabajo, no de este trabajo: ver correcciones abajo)
- Valores: <https://www.sii.cl/valores_y_fechas/uf/uf2026.htm> (UF de $40.975,41 al 20 de
  septiembre de 2026; el valor está leído en la tabla del SII).

---

## Correcciones aplicadas al editar el capítulo

Todas salieron de leer la fuente oficial y compararla con el texto, no de memoria.

- Ítem 1, Beneficio: los códigos por mensaje de texto estaban citados "solo el 96% de los de
  phishing y el 76% de los dirigidos", omitiendo el 100% de los intentos automatizados que sí
  publica la fuente (Google Security Blog, 2019). Se agregó el dato faltante y el blog de Google
  como fuente, para que las tres cifras del mensaje de texto estén citadas juntas.
- Ítem 2, Beneficio: las cifras "6,5 claves, 3,9 sitios, 25 cuentas" venían atribuidas a Florêncio
  y cols. 2014, que no las publica. Las publica Florêncio y Herley (2007). Corregida la autoría y
  el año.
- Ítem 6: se sacaron las dos fuentes que no eran del Registro Civil —`registrosciviles.cl` dice
  por escrito que no es un sitio oficial, y `registrocivil.cl` solo entrega un muro de seguridad— y
  se repuso el fundamento legal real: la Ley 19.948, leída en LeyChile, con la presunción de no
  uso desde la hora del bloqueo y la ratificación del definitivo dentro de los dos días hábiles.
- Ítem 14: la letra g) del artículo 2 citada como definición vigente es la de la Ley 19.628, y la
  que incluye los biométricos es la del artículo primero número 5 de la Ley 21.719; se explicitó
  para que la lectura no confunda las dos versiones.
- Ítem 16: se reescribió completo. Estaba sostenido en dos fuentes que no respaldan la
  recomendación de revisar los aparatos con sesión abierta; ahora se apoya en el punto "Minimizar
  privilegios" de la Guía de los 9 básicos de la ANCI y en el Ciberconsejo sobre autorizaciones,
  ambos leídos. El pendiente quedó arriba.
- Ítem 12: se quitó de Notas la recomendación de comprobar el dominio en el buscador de sitios
  oficiales del SERNAC y el CSIRT, porque ese buscador ya no existe; el enlace a la noticia de
  2020 queda solo como constancia.
- Ítem 5: se quitó la afirmación "es gratuito" sobre el informe de deudas, que aparece en la
  descripción del portal pero no en el texto de la ficha oficial, y se acotó en Notas qué deudas
  muestra ese informe y qué no.
- Ítem 9: se eliminó una cita ("sin denuncia previa") que no está en el texto leído de Subtel; en
  su lugar quedó la frase textual de la campaña del Gobierno. El desbloqueo del equipo, que sí
  está en la disposición de Subtel, se movió al costo.

