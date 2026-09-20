# Verificación · capítulo 01, No te mueras joven

Pendientes abiertos al escribir `guia/01-no-te-mueras-joven.md`. Cada uno calza con una marca
`POR VERIFICAR` en el ítem correspondiente.

---

- `guia/01-no-te-mueras-joven.md` ítem 9, Costo y Notas
  Dato: el precio de una glicemia en ayunas en Chile.
  Sospecha: (no hay valor sospechado) el valor debe estar en el explorador de precios de exámenes
  de laboratorio e imagenología de la Superintendencia de Salud, que se alimenta de los aranceles
  informados por los prestadores.
  Fuente que no se pudo leer: `https://www.superdesalud.gob.cl/orientacion-en-salud/explorador-de-precios-de-examenes-de-laboratorio-e-imagenologia/`
  abre (200), pero el buscador no entrega valores a la consulta automática: el HTML llega sin
  resultados y no expone una API consultable.
  Cómo cerrarlo: buscar "glicemia en ayunas" a mano en ese explorador, con fecha de consulta, o
  pedir el arancel a Fonasa (Modalidad Libre Elección). Hasta entonces el ítem no afirma un precio.

- `guia/01-no-te-mueras-joven.md` ítem 10, Notas
  Dato: la cobertura nacional de vacunación contra el VPH en Chile.
  Sospecha: (no hay valor sospechado) el dato debe estar en el informe trimestral de coberturas
  preliminares del Programa Nacional de Inmunizaciones, que se calcula desde el Registro Nacional
  de Inmunizaciones (RNI); los datos oficiales los publica después el DEIS.
  Fuente que no se pudo leer: `https://vacunas.minsal.cl/coberturas/` abre (200), pero es una
  página de menú: los informes van como archivos adjuntos y no se pudieron leer por consulta
  automática.
  Cómo cerrarlo: descargar el informe trimestral vigente desde esa página y citar la cobertura de
  la dosis de cuarto básico con su período. Mientras no exista, el ítem cita el estudio sueco y el
  esquema chileno, sin afirmar cobertura.

- `guia/01-no-te-mueras-joven.md` ítem 13, Notas
  Dato: cada cuánto corresponde el refuerzo de la vacuna antitetánica (toxoide diftérico
  tetánico) en un adulto sano en Chile.
  Sospecha: la pauta internacional habitual es cada 10 años; se sospecha que el PNI chileno usa el
  refuerzo dTp en primero y octavo básico más puesta al día en adultos, sin una campaña decenal
  universal, pero eso no se pudo leer.
  Fuente que no se pudo leer: la ficha del PNI en ChileAtiende
  (`https://www.chileatiende.gob.cl/fichas/105622-vacunas-del-programa-nacional-de-inmunizaciones-del-minsal`)
  lista los refuerzos por edad escolar y para embarazadas, y el Decreto Exento 50 de 2021 incluye
  el toxoide diftérico tetánico y la inmunoglobulina antitetánica entre las vacunas del programa,
  pero ninguna de las dos piezas leídas dice el intervalo de refuerzo en adultos sanos.
  Cómo cerrarlo: leer los "Lineamientos técnicos operativos" de vacunación de adultos del
  Departamento de Inmunizaciones, o el calendario de vacunación de población general del año en
  curso, en `https://vacunas.minsal.cl/`.

- `guia/01-no-te-mueras-joven.md` ítems 1, 15 y 16, Notas
  Dato: el número de artículo del texto vigente de la Ley de Tránsito para (a) el uso obligatorio
  del cinturón, (b) el sistema de retención infantil y (c) los límites máximos de velocidad
  urbanos, y el valor vigente de esos límites.
  Sospecha: CONASET publica 50 km/h en zona urbana, 100 y 120 km/h en zona rural y 30 km/h en zona
  de escuela, y 8 años inclusive (o 135 cm y 33 kg) para el sistema de retención infantil. En una
  copia antigua del texto de la ley, la regla de la silla decía "menores de cuatro años" y el
  límite urbano era 60 km/h, y la Ley 20.904 de 2016 dice expresamente que modifica "el artículo
  75" del texto refundido fijado por el DFL 1 de 2007.
  Fuente que no se pudo leer: la versión consolidada que publica LeyChile en
  `https://www.bcn.cl/leychile/navegar?idLey=18290` y en el servicio de datos
  (`https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=29708`) trae su sello de
  versión en 2009-11-07 y no incorpora las reformas posteriores: en ella la obligación de la silla
  dice "menores de cuatro años", el artículo se numera 79 y el límite urbano es de 60 km/h. El
  visor nuevo de LeyChile no publica la versión vigente en el servicio de consulta, y el endpoint
  `nuevo.leychile.cl/servicios/getVersiones` está deshabilitado.
  Cómo cerrarlo: abrir la versión vigente en el visor de LeyChile (selector de versión) o pedir a
  la Biblioteca del Congreso Nacional la versión actualizada del texto refundido, y citar el
  número de artículo y los valores exactos. Lo que sí está leído textualmente y por eso sí se cita:
  el umbral de alcohol (1,0 g/l para estado de ebriedad, más de 0,5 y menos de 1,0 g/l para bajo
  la influencia del alcohol), la escala de multas del artículo 201, el casco en el artículo 84 y
  el texto completo de la Ley 20.904.

- `guia/01-no-te-mueras-joven.md` ítems 3 y 4, Notas
  Dato: una cifra chilena de muertes por ahogamiento (ítem 3) y de muertes por incendio estructural
  (ítem 4), y una estimación de mortalidad de las alarmas de humo.
  Sospecha: (no hay valor sospechado) los dos primeros deberían poder construirse con las
  defunciones por causas externas de DEIS/MINSAL (CIE-10, grupo W65-W74 para ahogamiento y X00-X09
  para exposición al humo y al fuego). No se encontró una publicación oficial con el consolidado.
  Fuente que no se pudo leer: `https://deis.minsal.cl/` abre, pero los conjuntos de datos están en
  el repositorio de descargas; `https://repositoriodeis.minsal.cl/` responde 403 a la consulta
  automática. La página de datos abiertos de DEIS y el anuario del INE revisados no traen el
  desglose por causa externa.
  Cómo cerrarlo: descargar las defunciones por causa del año más reciente desde el repositorio de
  DEIS y sumar los códigos W65-W74 (ahogamiento) y X00-X09 (humo y fuego). Mientras no exista, los
  ítems 3 y 4 citan solo el dato internacional, el reglamento chileno de piscinas y las
  estadísticas de Estados Unidos, sin inventar un dato país.

## Cerrados

(nada cerrado todavía: el capítulo se escribió completo en una pasada)
