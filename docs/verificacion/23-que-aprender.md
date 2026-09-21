# Verificación · capítulo 23 — Qué aprender

`guia/23-que-aprender.md`

Este capítulo es el que más tienta a inventar cifras: sueldos por carrera, aranceles, empleabilidad.
**No hay ninguna cifra de esas en el capítulo.** Donde no se pudo confirmar el dato oficial, dice
`POR VERIFICAR` y queda anotado acá.

## Pendientes abiertos

### 1. Aranceles de referencia y aranceles reales por carrera

- `guia/23-que-aprender.md` ítem 5, línea 47 (Notas)
  Dato: el ítem dice que el costo de una carrera se calcula como arancel anual por años de carrera
  más el ingreso mediano anual por los mismos años, sin dar ningún arancel.
  Sospecha: no se formula ninguna; el capítulo evita la cifra a propósito porque cambia todos los
  años.
  Fuente que no se pudo leer: la tabla de aranceles de referencia de la Comisión Ingresa
  (<https://portal.ingresa.cl/el-credito/aranceles-de-referencia/>) enlaza al listado de valores
  2026 pero no publica la tabla en la página; el buscador de carreras de Mi Futuro
  (<https://www.mifuturo.cl/buscador-de-carreras/>) carga los valores por consulta y no entrega la
  tabla a una lectura directa.
  Cómo cerrarlo: abrir el enlace de «Aranceles de Referencia 2026» del portal de la Comisión Ingresa
  y el buscador de carreras de Mi Futuro —uno por uno, con la carrera y la institución concretas— y
  anotar el valor con su año y su institución antes de escribir cualquier monto.

### 2. Montos de las becas de arancel y mantención del Mineduc

- `guia/23-que-aprender.md` ítem 8, línea 74 (Notas)
  Dato: el ítem describe los requisitos de la gratuidad (60% de menores ingresos según el Registro
  Social de Hogares, institución adscrita, carrera presencial, sin título previo) y las fechas del
  FUAS, sin mencionar becas ni sus montos.
  Sospecha: ninguna.
  Fuente que no se pudo leer: el portal de Beneficios Estudiantiles
  (<https://portal.beneficiosestudiantiles.cl/>) no publica los montos de la Beca Bicentenario, la
  Beca Juan Gómez Millas ni las becas de mantención en su portada ni en una página de resumen; hay
  que entrar a la ficha de cada beca.
  Cómo cerrarlo: leer la sección de cada beca de arancel y de mantención de la admisión 2027 en el
  portal de Beneficios Estudiantiles y anotar el monto anual con su año.

### 3. Retorno del inglés en los ingresos, cálculo chileno

- `guia/23-que-aprender.md` ítem 14, línea 122 (Notas)
  Dato: el ítem cita el 34% de mayor salario por hora entre quienes hablan inglés fluido en la India
  (estudio internacional, con DOI); no da ninguna cifra chilena.
  Sospecha: ninguna. No se encontró estimación chilena publicada.
  Fuente que no se pudo leer: no hay una fuente oficial chilena con el retorno del inglés en los
  ingresos que se pudiera citar; se buscó en las publicaciones del INE y del Mineduc sin resultado.
  Cómo cerrarlo: revisar publicaciones del Banco Central, del Mineduc y de universidades chilenas, o
  calcular la estimación con los microdatos de la Encuesta Suplementaria de Ingresos del INE
  (<https://www.ine.gob.cl/estadisticas-por-tema/mercado-laboral/encuesta-suplementaria-de-ingresos>).

### 4. Ingresos y empleabilidad por carrera; ingresos por ocupación u oficio

- `guia/23-que-aprender.md` ítem 15, línea 130 (Notas)
  Dato: el ítem cita el ingreso medio de $962.945 y el ingreso mediano de $680.000 de los ocupados
  (Encuesta Suplementaria de Ingresos 2025) como el dato oficial para comparar la plata, y dice
  explícitamente que el INE no publica sueldos por carrera.
  Sospecha: ninguna; el capítulo no da sueldos por carrera ni por oficio.
  Fuente que no se pudo leer: el buscador de empleabilidad e ingresos de Mi Futuro
  (<https://www.mifuturo.cl/buscador-de-empleabilidad-e-ingresos/>) devuelve la página pero los
  valores por carrera se cargan por consulta; el sitio del INE entrega los ingresos por ocupación en
  agregados y por sector, no en una tabla de sueldos por oficio legible de forma directa.
  Cómo cerrarlo: consultar el buscador de empleabilidad e ingresos de Mi Futuro carrera por carrera
  (y su metodología) y, para oficios, revisar los cuadros de la Encuesta Suplementaria de Ingresos en
  SIMEL (<https://www.ine.gob.cl/simel>) antes de escribir una cifra de sueldo.

## Sitios oficiales que abren en el navegador pero no en consulta automática

No son enlaces muertos: abren con cualquier navegador. Se anotan para que nadie los dé por caídos.

- **Comisión Nacional de Acreditación** (<https://www.cnachile.cl/>): el certificado TLS no
  encadena al emisor (DigiCert, GeoTrust EV RSA CA G2) y falla la verificación automática; con
  `curl -k` responde 200 y el sitio carga completo, con el buscador de acreditaciones institucional,
  de pregrado y de posgrado. El capítulo lo cita igual, con esa advertencia en las Notas del ítem 6.
- **FUAS** (<https://www.fuas.cl/>): responde 200 en la portada, pero una de sus páginas internas
  (preguntas frecuentes) agotó el tiempo de espera en la comprobación automática.

## Cifras que sí quedaron verificadas contra el texto oficial

Se dejan registradas para no repetir la búsqueda. Todas con el texto leído, no con prensa.

| Dato en el capítulo | Fuente leída |
|---|---|
| Edad para trabajar: 15 a 18 años; prohibición de contratar menores de 15; autorización escrita del padre, madre o cuidador; certificado de alumno regular actualizado cada 6 meses; jornada máxima de 30 horas semanales y 6 horas diarias en el año escolar; prohibición de horas extraordinarias; 13 horas consecutivas sin trabajo nocturno (de 21:00 a 8:00) | Código del Trabajo (DFL 1, idNorma=207436), artículos 13, 14 y 18, texto oficial completo |
| Educación básica y media obligatorias y financiadas por el Estado en un sistema gratuito; básica de 6 años y media de 6 años (4 + 2) | Ley 20.370, artículo 4, inciso tercero, y artículo 25 (idLey=20370) |
| Cada año adicional de educación baja 1,9% el riesgo de muerte adulta (2,9% entre 18 y 49 años, 0,8% sobre 70 años); sesgo de publicación p<0,0001 declarado por los autores | IHME-CHAIN Collaborators (2024), Lancet Public Health, <https://doi.org/10.1016/S2468-2667(23)00306-7> |
| Retorno privado promedio mundial de 9% al año por año adicional de educación; 139 países y 1.120 estimaciones | Psacharopoulos & Patrinos (2018), <https://doi.org/10.1080/09645292.2018.1484426> |
| Interés real de 2% anual; garantía estatal de hasta 90% del capital más intereses; crédito no exigible antes de 18 meses desde el término del plan de estudios; suspensión por cesantía; retención de la devolución de impuestos por la Tesorería | Ley 20.027, artículos 3, 11 bis, 12, 13 y 17 (idLey=20027) |
| CAE en UF, tasa fija subsidiada del 2% anual, plazo de pago de 5 a 20 años, cobro 18 meses después del egreso, rebaja de cuota al 10% de la renta, «la garantía no significa condonación de la deuda» | Comisión Ingresa, <https://portal.ingresa.cl/preguntas-frecuentes/> y <https://portal.ingresa.cl/el-credito/que-es-el-credito-cae/> |
| El arancel de referencia «por lo general es menor que el valor anual que cobra tu institución por la carrera»; la diferencia la financia el estudiante | Comisión Ingresa, <https://portal.ingresa.cl/el-credito/aranceles-de-referencia/> |
| Acreditación institucional obligatoria en Chile; dimensiones evaluadas; niveles excelencia, avanzada y básica; no se otorga a quien no cumple los criterios; acreditación obligatoria de Medicina, Odontología y pedagogías; apelación ante el Consejo Nacional de Educación en 30 días hábiles | Ley 20.129, artículos 15, 17, 20, 22, 23, 27 y 28 (idLey=20129), texto oficial completo |
| Obligatoriedad de la acreditación institucional a contar del 1 de enero de 2020 | Ley 21.091, artículo vigésimo primero transitorio, y Ley 21.186 |
| 135 instituciones vigentes a diciembre de 2024, 85 acreditadas (62%); períodos de acreditación de 3 a 7 años; 62% de las instituciones acreditadas concentra el 96,9% de la matrícula de pregrado | Mineduc, <https://www.mifuturo.cl/la-importancia-de-la-calidad/> |
| Gratuidad: 60% de menores ingresos según el Registro Social de Hogares; institución adscrita; carrera de pregrado presencial; sin licenciatura ni título previo; nacionalidad chilena o permanencia definitiva; postulación FUAS admisión 2027 del 1 al 22 de octubre de 2026; resultados desde el 15 de octubre de 2026 | ChileAtiende, ficha 43203, <https://www.chileatiende.gob.cl/fichas/43203-gratuidad-en-la-educacion-superior> |
| Requisito de gratuidad para la institución: «Contar con acreditación institucional avanzada o de excelencia» | Ley 21.091, artículo 83, letra a (idLey=21091) |
| Cursos en línea del SENCE: 18 años o más, cédula vigente, RUN chileno y ClaveÚnica; áreas; rutas de inglés con eClass; 6 cursos de IA con Microsoft de 2 horas; cupos ilimitados | ChileAtiende, ficha 48867, <https://www.chileatiende.gob.cl/fichas/48867-programa-cursos-en-linea> |
| Certificación de competencias «independientemente de la forma en que hayan sido adquiridas y de si tienen o no un título o grado académico»; certificados con calidad de instrumentos públicos; centros acreditados por la Comisión; registros públicos | Ley 20.267, artículos 1, 16, 18 y 25 (idLey=20267) |
| Certificación gratuita para beneficiarios del Fondo de Cesantía Solidario con experiencia en oficios de comercio, construcción y gastronomía; evaluación en una jornada, en la capital regional; apoyo para movilización | ChileValora, <https://chilevalora.gob.cl/certifica-experiencia> |
| Franquicia tributaria: tope de 1% de las remuneraciones imponibles al año; tramos de 7 UTM (planilla entre 35 y 45 UTM) y 9 UTM (45 UTM o más); planillas bajo 35 UTM no pueden usarla; asistencia mínima de 75% (100% en e-learning); comité bipartito desde 15 trabajadores | Ley 19.518, artículo 36 (idLey=19518) y SENCE, <https://sence.gob.cl/empresas/franquicia-tributaria> |
| La franquicia no puede financiar formación conducente a título o grado académico, salvo módulos de formación en competencias laborales conducentes a título técnico de CFT autorizados; sí puede financiar nivelación de estudios básicos y medios | Ley 19.518, artículos 1 (inciso segundo y siguientes), 12 y 36 |
| La franquicia financia también evaluación y certificación de competencias laborales | Ley 20.267, artículos 28 a 30 |
| 47% del empleo en la banda de alto riesgo en el modelo de 702 ocupaciones de EE.UU.; los tres cuellos de botella son percepción y manipulación, inteligencia creativa e inteligencia social | Frey & Osborne (2017), <https://doi.org/10.1016/j.techfore.2016.08.019> |
| 34% más de salario por hora para hombres que hablan inglés fluido y 13% para quienes hablan un poco, en la India, controlando por edad, grupo social, escolaridad, geografía y proxies de habilidad; el retorno del inglés fluido equivale al de completar secundaria y a la mitad del de una licenciatura | Azam, Chin & Prakash (2013), <https://doi.org/10.1086/668277> |
| Inglés y mayores ingresos en Sudáfrica con datos del panel nacional de 2008 | Casale & Posel (2011), <https://doi.org/10.1016/j.socec.2011.04.009> |
| Ingreso medio mensual de los ocupados $962.945 e ingreso mediano $680.000 (año 2025); la ESI se levanta una vez al año en el trimestre octubre-diciembre, urbano y rural, en todas las regiones; sin desagregación por carrera | INE, <https://www.ine.gob.cl/estadisticas-por-tema/mercado-laboral/encuesta-suplementaria-de-ingresos> |

## Sobre las etiquetas de beneficio de este capítulo

El capítulo es de plata en casi todos sus ítems, y la tabla del contrato (§2.4) exige millones de
pesos para `beneficio=alto`. Ningún ítem llega a esa cifra aplicando la tabla, así que:
`beneficio=alto` se asignó solo al ítem de gratuidad (cubre matrícula y arancel de una carrera
completa, esto es, millones de pesos en varios años); el resto quedó en `medio`, con la justificación
anotada ítem por ítem en sus Notas cuando el cálculo no era evidente.
