# Verificación · capítulo 28, No arruines tu salud por verte mejor

Marca `POR VERIFICAR` en `guia/28-no-arruines-tu-salud.md`. Se anota cada dato que no se pudo
confirmar contra una fuente oficial, con el ítem donde aparece y qué habría que consultar para
cerrarlo.

Hay tres tipos de pendiente en este capítulo: **(a)** precios y plazos de prestaciones y de
medicamentos que ningún organismo publica como arancel consultable, **(b)** autorizaciones sanitarias
y normas que existen pero no están publicadas como registro en línea, y **(c)** estadísticas
nacionales de un fenómeno que MINSAL e ISP documentan solo en notas de prensa antiguas, sin serie
de datos. En todos los casos se prefirió dejar la marca antes que rellenar con un valor plausible.

---

## a) Precios y plazos sin arancel oficial publicado

- `guia/28-no-arruines-tu-salud.md` ítem 6 (hormonas con receta), línea del campo `Costo`
  Dato: precio del frasco del medicamento hormonal y del panel de exámenes de seguimiento en Chile.
  Sospecha: ninguno (no se propone un valor).
  Fuente que no se pudo leer como arancel: la Superintendencia de Salud publica el promedio facturado
  de exámenes de laboratorio e imagenología y de prestaciones de salud sexual y reproductiva
  (<https://www.superdesalud.gob.cl/orientacion-en-salud/explorador-de-precios-de-examenes-de-laboratorio-e-imagenologia/>),
  pero esos exploradores no cubren medicamentos de farmacia ni un panel específico de control hormonal.
  Cómo cerrarlo: usar el arancel de la Modalidad de Libre Elección vigente de Fonasa para las consultas
  y los exámenes, y el precio de venta de la farmacia en convenio con fecha; registrar ambos con fecha
  de referencia, como exige §4 del contrato.

- `guia/28-no-arruines-tu-salud.md` ítem 11 (medicamentos por redes sin receta), línea del campo `Costo`
  Dato: monto de referencia de la consulta médica más el medicamento para adelgazar comprado con receta.
  Sospecha: ninguno.
  Fuente que no se pudo leer como arancel: el ISP no publica precios de medicamentos; ChileAtiende no
  tiene ficha de precios de consulta médica.
  Cómo cerrarlo: arancel MLE de Fonasa (consulta de especialidad) y precio facturado en farmacia con
  boleta de fecha.

- `guia/28-no-arruines-tu-salud.md` ítem 17 (evaluación antes de cirugía), línea del campo `Costo`
  Dato: precio de la consulta con psiquiatra o psicólogo clínico en el sistema privado.
  Sospecha: ninguno.
  Fuente que no se pudo leer como arancel: la Superintendencia publica precios facturados de exámenes
  y de prestaciones de salud sexual y reproductiva, no de consultas de salud mental.
  Cómo cerrarlo: arancel MLE de Fonasa para consulta de psiquiatría y de psicología; o el precio
  publicado por el prestador con fecha. En la red pública la vía es el consultorio y no hay precio
  que consignar.

## b) Autorización sanitaria y normativa que existe pero no se publica como registro en línea

- `guia/28-no-arruines-tu-salud.md` ítem 7 (verificar el local y el título de quien inyecta),
  campo `Notas`
  Dato: no existe registro público en línea de establecimientos con autorización sanitaria vigente
  para procedimientos estéticos.
  Sospecha: ninguno (es una ausencia, no un valor).
  Lo verificado: el artículo 124 del Código Sanitario exige autorización sanitaria previa y dirección
  técnica a un profesional de la salud a los establecimientos que, aun anunciando finalidad estética,
  usen instrumentos que penetren la piel o mucosas; el artículo 122 radica esa autorización en la
  Secretaría Regional Ministerial del territorio
  (<https://www.bcn.cl/leychile/navegar?idNorma=5595>). El ISP publica en cambio el listado de
  dispositivos médicos con registro sanitario y los registros de cosméticos.
  Cómo cerrarlo: pedir a la SEREMI de Salud correspondiente la nómina de establecimientos con
  autorización sanitaria vigente para procedimientos estéticos; si la respuesta llega, reemplazar la
  marca por la referencia al documento.

- `guia/28-no-arruines-tu-salud.md` ítem 16 (camas de bronceado), campo `Notas`
  Dato: no se encontró norma chilena específica que prohíba el uso de camas de bronceado en menores
  de edad, ni un registro sanitario de esos equipos.
  Sospecha: ninguno.
  Lo verificado: el Código Sanitario regula las instalaciones radiactivas y los equipos generadores de
  radiaciones ionizantes (artículos 89 y siguientes), y la radiación ultravioleta de una cama solar no
  es ionizante, de modo que no le aplica ese título.
  Cómo cerrarlo: revisar el Reglamento Sanitario de los Alimentos y los decretos y resoluciones de la
  SEREMI de Salud sobre equipos de bronceado artificial; consultar además si el proyecto de norma
  sobre radiación UV no ionizante llegó a publicarse en el Diario Oficial.

## c) Estadísticas nacionales sin serie publicada

- `guia/28-no-arruines-tu-salud.md` ítem 5 (esteroides anabólicos), campo `Notas`
  Dato: cifra oficial chilena de decomisos de esteroides anabólicos y de su prevalencia en gimnasios.
  Sospecha: ninguno.
  Fuente que no se pudo leer: ni el ISP ni la Comisión Nacional de Control de Dopaje publican una
  serie de decomisos de esteroides anabólicos. El ISP sí documenta operativos conjuntos con la SEREMI
  de Salud en gimnasios por suplementos que corresponden a fármacos
  (<https://www.ispch.gob.cl/noticia/isp-y-seremi-de-salud-rm-fiscalizaron-suplementos-alimenticios-que-podrian-contener-farmacos/>),
  sin cifra de esteroides.
  Cómo cerrarlo: solicitud de información pública al ISP (portal de denuncias y OIRS) y a la Comisión
  Nacional de Control de Dopaje, que la Ley 19.712 radica en el Ministerio del Deporte.

- `guia/28-no-arruines-tu-salud.md` ítem 2 (trastornos de la conducta alimentaria), campo `Notas`
  Dato: tiempo de espera y cupos de tratamiento público por trastorno de la conducta alimentaria.
  Sospecha: ninguno.
  Lo verificado y relevante: los trastornos de la conducta alimentaria **no** aparecen en el listado
  de 90 problemas de salud de las Garantías Explícitas en Salud publicado por MINSAL en
  <https://auge.minsal.cl/problemasdesalud/index> (revisado el 20 de septiembre de 2026). Lo
  garantizado en salud mental en ese listado es: depresión en personas de 15 años y más (N° 34),
  esquizofrenia (N° 15), trastorno bipolar en personas de 15 años y más (N° 75), consumo perjudicial
  o dependencia de riesgo bajo a moderado de alcohol y drogas en personas menores de 20 años (N° 53)
  y tratamiento hospitalario para personas menores de 15 años con depresión grave refractaria o
  psicótica con riesgo suicida (N° 89).
  Cómo cerrarlo: pedir a la SEREMI de Salud o al Servicio de Salud correspondiente los tiempos de
  espera y cupos del programa de trastornos de la conducta alimentaria. Hasta entonces no se pone
  cifra: el capítulo dice lo que sí está garantizado y aclara lo que no.

- `guia/28-no-arruines-tu-salud.md` ítem 13 (cirugía estética), campo `Notas`
  Dato: cuántos establecimientos están acreditados específicamente para cirugía estética.
  Sospecha: ninguno.
  Lo verificado: existe el Registro Público de Prestadores Acreditados de la Superintendencia de Salud,
  consultable por número de registro, en orden alfabético, nacional y regional
  (<https://www.superdesalud.gob.cl/tax-registros/registro-de-prestadores-acreditados-4329/por-n-de-registro-4710/>),
  y la Ley 19.937 ordena su existencia, pero el registro se ordena por establecimiento y número de
  registro, no por prestación o por especialidad.
  Cómo cerrarlo: consultar el registro por establecimiento cuando se sepa cuál es el que va a operar,
  que es de hecho la instrucción del ítem; una cifra agregada por prestación habría que pedirla a la
  Superintendencia.

---

## Notas de método

- El dominio `ispch.gob.cl` presenta un error de cadena de certificados que impide verificarlo con
  `urllib` desde este entorno (`CERTIFICATE_VERIFY_FAILED`), incluso sobre `http://`, que redirige a
  HTTPS. `tools/verificar.py --urls` lo reporta como no abrible. Los enlaces del ISP citados en este
  capítulo sí abren en navegador y su contenido se leyó y transcribió literalmente desde
  `curl -k` con agente de navegador.
- Todos los DOIs citados en el capítulo se verificaron contra Crossref y sus cifras se leyeron del
  resumen original en PubMed o Europe PMC, no de una nota secundaria.
- Los montos en pesos se calcularon con la UTM de septiembre de 2026 publicada por el SII
  ($71.721): 6 UTM = $430.326; 20 UTM = $1.434.420; 1.500 UTM = $107.581.500; 2.250 UTM =
  $161.372.250.
