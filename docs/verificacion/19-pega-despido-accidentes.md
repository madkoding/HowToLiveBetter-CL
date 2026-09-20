# Verificación · capítulo 19 — Pega, despido y accidentes

`guia/19-pega-despido-accidentes.md`

## Pendientes abiertos

### 1. Comisiones de AFP vigentes en 2026

- `guia/19-pega-despido-accidentes.md` ítem 3, línea 33
  Dato: el ítem dice que "sobre el 10% del DL 3.500, cada AFP cobra además su comisión, que se suma
  al descuento", sin dar el rango de comisiones.
  Sospecha: el rango estaría entre 0,58% y 1,45% de la remuneración imponible según la
  administradora (valor citado por fuentes secundarias, no confirmado en el sitio oficial).
  Fuente que no se pudo leer: la Superintendencia de Pensiones publica el ranking de comisiones en
  su portal, pero no se obtuvo la página oficial con el cuadro vigente 2026 en la sesión de
  escritura; el buscador del sitio no devolvió el listado de comisiones.
  Cómo cerrarlo: consultar el cuadro de comisiones vigentes de la Superintendencia de Pensiones
  (<https://www.spensiones.cl/>) — sección Sistema de Pensiones, comisiones de AFP — y, si el rango
  calza, escribirlo en el ítem con su año.

## Cifras que sí quedaron verificadas contra el texto oficial

Se dejan registradas para no tener que repetir la búsqueda, todas con el texto leído:

| Dato en el capítulo | Fuente leída |
|---|---|
| Contrato por escrito en 15 días (5 si es por obra o de duración inferior a 30 días); presunción de las estipulaciones que declare el trabajador | Código del Trabajo, artículos 9 y 10 (DFL 1, idNorma=207436), texto oficial completo |
| Multa de 1 a 5 UTM por no escriturar; conversión con la UTM de septiembre de 2026 ($71.721) | Código del Trabajo artículo 9; SII, valores UTM 2026 <https://www.sii.cl/valores_y_fechas/utm/utm2026.htm> |
| Jornada ordinaria de 40 horas; 44/42/40 horas graduales; rebaja a 42 desde el 26 de abril de 2026 y a 40 el 26 de abril de 2028 | Código del Trabajo artículo 22 y artículo primero transitorio de la Ley 21.561; Dirección del Trabajo "Ley de 40 horas" <https://www.dt.gob.cl/portal/1626/w3-propertyname-2556.html> |
| Jornada 4x3: distribución en cuatro días para empresas que ya tengan 40 horas o menos | Ley 21.561, artículo octavo transitorio (idLey=21561); artículo 28 del Código del Trabajo modificado por el numeral 9 de la misma ley |
| Regla supletoria de la rebaja sin acuerdo (una hora en dos días, o 50 minutos en dos días y 20 en un tercero) | Ley 21.755, artículo 24 (consultado por API de LeyChile) y Dictamen N°253/21 de la Dirección del Trabajo, 16 de abril de 2026 |
| Ingreso mínimo de $553.553 desde el 1 de mayo de 2026 (Ley 21.830, D.O. 22.06.2026) | Dirección del Trabajo, consulta "¿Cuál es el valor del ingreso mínimo mensual?" |
| Cotización de AFP 10% y de salud 7%; comprobante de pago y límites a las deducciones (15% y 45%) | Código del Trabajo artículos 54 y 58; DL 3.500 artículos 17 y 84; Superintendencia de Salud, cotización legal para salud |
| Descuentos sobre el mínimo: $97.425 en total y líquido de $456.128 | aritmética propia sobre las tasas oficiales (10% + 7% + 0,6% de $553.553), verificada con el intérprete de Python |
| Recargo del 50% de las horas extraordinarias; máximo de 2 por día; tope de 52 horas en la modalidad del artículo 22 bis; compensación con días de feriado | Código del Trabajo artículos 30, 31 y 32; Dirección del Trabajo, consulta sobre horas extraordinarias |
| Feriado de 15 días hábiles; feriado progresivo con 10 años; sábado inhábil; feriado proporcional 15 ÷ 12 = 1,25 | Código del Trabajo artículos 67 a 73; consultas de la Dirección del Trabajo sobre feriado anual y proporcional |
| Permisos por matrimonio (5 días hábiles), muerte de hijo (10 corridos), cónyuge o conviviente civil (7 corridos), hermano, padre o madre (4 hábiles), medio día para exámenes preventivos; fuero de un mes | Código del Trabajo artículos 66, 66 bis y 207 bis |
| Fuero maternal de un año desde el descanso de maternidad; desafuero con autorización judicial previa | Código del Trabajo artículos 174 y 201 |
| Causales 159, 160, 161 y 163 bis; comunicación en 3 días hábiles (6 en el 159 N°6); aviso de 30 días en el 161 | Código del Trabajo artículos 159, 160, 161 y 162; consultas de la Dirección del Trabajo sobre causales y cómputo del aviso |
| Indemnización de 30 días por año con tope de 330 días; base con tope de 90 UF; reajuste por IPC e interés | Código del Trabajo artículos 163, 172 y 173; Dirección del Trabajo sobre el límite de 90 UF |
| Tope de 90 UF convertido a $3.695.148 | UF del 30 de septiembre de 2026 = $41.057,20, SII <https://www.sii.cl/valores_y_fechas/uf/uf2026.htm> |
| Finiquito en 10 días hábiles; ratificación ante ministro de fe; reserva de derechos; pago en un solo acto e incremento de hasta 150% | Código del Trabajo artículos 169 y 177; Dirección del Trabajo sobre la oportunidad de pago |
| Nulidad del despido por cotizaciones impagas; multa de 2 a 20 UTM | Código del Trabajo artículo 162; SUSESO, articulado del artículo 162 en el Compendio |
| Plazo de 60 días hábiles (máximo 90) y recargos de 30%, 50%, 80% y 100%; despido indirecto; procedimiento monitorio con 15 ingresos mínimos; prescripciones | Código del Trabajo artículos 168, 171, 496, 497 y 510; consultas de la Dirección del Trabajo sobre plazo para demandar y despido indirecto |
| Quince ingresos mínimos convertidos a $8.303.295 | aritmética propia sobre el ingreso mínimo de mayo de 2026 |
| Concepto de accidente del trabajo y de trayecto; denuncia en 24 horas (DIAT y DIEP); reclamo en 90 días hábiles ante la Comisión Médica | Ley 16.744 artículos 5, 76 y 77; SUSESO, Compendio de Normas, Libro III |
| Enfermedad profesional y traslado de faena; exámenes de control como tiempo trabajado | Ley 16.744 artículos 7 y 71 |
| Prestaciones médicas gratuitas; subsidio hasta 52 semanas prorrogables por 52; invalidez parcial desde 15%; indemnización global hasta 15 sueldos base; pensión del 35%, invalidez total 70%, gran invalidez +30% | Ley 16.744 artículos 29 a 41 |
| Cotización básica 0,90% y adicional de hasta 3,4% de cargo del empleador; elementos de protección sin costo; responsabilidad solidaria en subcontratación | Ley 16.744 artículos 15, 16, 56 y 68; Código del Trabajo artículos 184, 183-B y 183-D |
| Seguro de cesantía: cotizaciones 0,6% / 2,4% / 3%; 10 cotizaciones (5 a plazo fijo); Fondo de Cesantía Solidario con 10 cotizaciones en 24 meses; imputación a la indemnización | Ley 19.728 artículos 5, 12, 13, 15 y 24; AFC, beneficios y montos vigentes hasta el 28 de febrero de 2027 |
| Primer pago del Fondo de Cesantía Solidario entre $301.201 y $1.004.003 (contrato indefinido); primer pago a los 30 días corridos | AFC Chile, "Beneficios y opciones de pago del Seguro de Cesantía", valores vigentes hasta el 28 de febrero de 2027 (resolución exenta N°383 de la Superintendencia de Pensiones, de 6 de marzo de 2026) |
| Presunción de contrato de trabajo en la prestación de servicios bajo subordinación y dependencia; honorarios que encubren una relación laboral | Código del Trabajo artículos 7 y 8; Dirección del Trabajo, "Contrato Individual de Trabajo" y "¿Cuáles son los derechos de las personas contratadas a honorarios?" |
| Ley 21.643: protocolo de prevención; denuncia verbal con acta; medidas de resguardo inmediatas y en 2 días hábiles; investigación en 30 días; sanciones en 15 días | Código del Trabajo artículos 211-A, 211-B bis, 211-C y 211-E; consultas de la Dirección del Trabajo sobre la Ley Karin |

## Nota de método

Los artículos del Código del Trabajo se leyeron en el texto oficial completo de LeyChile
(`idNorma=207436`, versión 2026-07-23) y se contrastaron con las consultas y dictámenes de la
Dirección del Trabajo cuando la ley deja el punto al criterio administrativo (por ejemplo, el
cómputo de los días hábiles y la fecha de la rebaja de jornada). Los artículos de la Ley 16.744 y de
la Ley 19.728 se leyeron en LeyChile y, en los casos en que el Compendio de la SUSESO fija plazos
operativos que la ley no detalla —las 24 horas de la DIAT y de la DIEP—, se citó el Compendio y no
la ley.
