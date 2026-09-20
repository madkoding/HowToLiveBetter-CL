# Registro de verificación · capítulo 02

`guia/02-no-te-mueras-lento.md` — capítulo **No te mueras lento**.
Revisión: 20 de septiembre de 2026.

Aquí queda todo lo que **no se pudo confirmar** contra la fuente oficial. Todos los pendientes son
montos o cifras que se decidió **no escribir** en vez de rellenar con un valor plausible: el ítem
queda solo con lo que la fuente sí respalda.

---

## Ítem 1, línea 6 — precio del paquete de cigarrillos en Chile

- `guia/02-no-te-mueras-lento.md` ítem 1 ("Deja el cigarrillo, y déjalo antes de los 40")
  Dato: el ítem dice que dejar de fumar es costo $0 y que además "deja de gastar la plata del
  paquete", pero **no cita ningún monto**.
  Sospecha: el paquete de cigarrillos en Chile estaría en el orden de los $5.000 a $7.000 en 2026.
  Fuente que no se pudo leer: no se encontró ninguna fuente oficial de precios de tabaco. El
  Servicio de Impuestos Internos publica los impuestos específicos al tabaco del decreto ley 828
  (la Ley 20.780 introdujo cambios en ese régimen), pero no un precio de venta al público; el
  portal de precios del Ministerio de Agricultura (ODEPA) publica precios mayoristas de alimentos
  y no incluye tabaco.
  Cómo cerrarlo: usar los precios de un panel oficial de precios al consumidor (INE, base del IPC,
  división de bebidas alcohólicas y tabaco) con su fecha, y citar el impuesto del decreto ley 828
  con el artículo que lo fija. Recién entonces se puede poner un monto en el ítem.

## Ítem 8, línea 84 — umbrales de alcohol de la Ley de Tránsito en el texto consolidado de LeyChile

- `guia/02-no-te-mueras-lento.md` ítem 8 ("Si vas a tomar, no manejes")
  Dato: el ítem **no cita los umbrales legales** y remite al capítulo 08. La nota del ítem deja la
  advertencia escrita.
  Sospecha: (ninguna sobre el fondo) los umbrales vigentes son 0,8 gramos por mil para el estado de
  ebriedad y más de 0,3 y menos de 0,8 para la conducción bajo la influencia del alcohol, según la
  Ley 20.580, publicada el 15 de marzo de 2012.
  Fuente que no se pudo leer con el valor actualizado:
  - `https://www.bcn.cl/leychile/navegar?idNorma=29708` — el texto consolidado de la Ley 18.290 que
    publica LeyChile (última versión, inicio de vigencia 7 de noviembre de 2009) mantiene el
    artículo 115 B con los valores **anteriores** a la Ley 20.580: "igual o superior a 1,0 gramos
    por mil" para el estado de ebriedad y "superior a 0,5 e inferior a 1,0 gramos por mil" para la
    conducción bajo la influencia del alcohol. Se revisó el XML oficial completo
    (`https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=29708`, 338.901 caracteres,
    fechaVersion 2009-11-07) y no contiene las expresiones "0,8" ni "0,3". Los parámetros
    `idVersion` y `tipoVersion` de la API no devuelven otra versión.
  - `https://www.bcn.cl/leychile/navegar?idLey=20580` — esta sí abre y su texto dice textualmente:
    "En el artículo 111: a) Reemplázase en el inciso segundo el guarismo \\"1,0\\" por \\"0,8\\".
    b) Reemplázase en el inciso tercero la frase \\"superior a 0,5 e inferior a 1,0 gramos por mil\\"
    por \\"superior a 0,3 e inferior a 0,8 gramos por mil\\"". Esta es la fuente que el ítem cita.
  Cómo cerrarlo: pedir en la mesa de ayuda de LeyChile (BCN) la actualización del texto refundido de
  la Ley de Tránsito, o citar una resolución del Ministerio de Transportes que aplique los umbrales
  vigentes. El capítulo 08 usa la misma fuente modificatoria y tiene el mismo pendiente.

## Ítem 8, línea 84 — cifras chilenas de siniestros por alcohol en el conductor (CONASET)

- `guia/02-no-te-mueras-lento.md` ítem 8 ("Si va a tomar, no manejes")
  Dato: el ítem **no cita** el número de fallecidos ni de siniestros por alcohol al volante en Chile.
  Sospecha: la Comisión Nacional de Seguridad de Tránsito informa una disminución del 37% en los
  fallecidos por "alcohol en conductor (Ley Tolerancia Cero)" respecto del período previo a la ley
  de 2012; ese dato aparecía en un informe descargado durante la investigación, pero no se pudo
  volver a abrir la fuente en el momento de cerrar el ítem.
  Fuente que no se pudo leer:
  - `https://www.conaset.cl/` — el sitio no responde a la verificación de certificados: `openssl
    s_client` devuelve "unable to verify the first certificate / Verify return code: 21" (cadena
    incompleta del servidor). `curl` sin verificación responde 200 desde 163.247.52.183, y
    `urllib` —el cliente que usa `tools/verificar.py`— falla con
    `SSL: CERTIFICATE_VERIFY_FAILED`. Una URL que no abre con el verificador del repo no se puede
    citar.
  - `https://www.conaset.cl/estadisticas/` y `https://www.conaset.cl/ley-tolerancia-cero/` — mismo
    problema de cadena de certificados.
  Cómo cerrarlo: usar el informe de siniestros de tránsito alojado en un dominio que sí abra
  (por ejemplo el repositorio de datos abiertos del Ministerio de Transportes) y citar el número
  con su año. También se puede pedir la base a CONASET por transparencia activa.

## Ítem 9, línea 96 — precio de la sal con menos sodio en Chile

- `guia/02-no-te-mueras-lento.md` ítem 9 ("Cambia la sal de tu casa por sal con menos sodio")
  Dato: el ítem dice "la sal con menos sodio cuesta algo más por paquete que la sal común" y **no
  cita monto**.
  Sospecha: estaría en el orden de dos a tres veces el precio de la sal común por kilo.
  Fuente que no se pudo leer: no se encontró fuente oficial de precios de sal. El Reglamento
  Sanitario de los Alimentos regula el producto, pero no su precio, y la sal no aparece en el
  portal de precios mayoristas de ODEPA.
  Cómo cerrarlo: usar la base de precios del IPC del INE (división de alimentos) o una boleta de
  compra de supermercado con fecha, y anotar la fecha de referencia.

## Ítem 14, línea 138 — precio de los frutos secos en Chile

- `guia/02-no-te-mueras-lento.md` ítem 14 ("Come un puñado de frutos secos al día")
  Dato: el ítem describe la compra por kilo y **no cita monto**.
  Sospecha: (ninguna concreta) el precio varía mucho por tipo de fruto seco y por si es salado o
  natural.
  Fuente que no se pudo leer: `https://www.odepa.gob.cl/precios/precios-mayoristas` abre, pero no
  publica frutos secos importados en la lista consultada; no hay ficha oficial de precio de
  consumo.
  Cómo cerrarlo: usar la serie de precios del INE o un precio de referencia con su fecha, del mismo
  modo que los demás montos del capítulo.

## Ítem 17, línea 182 — costo del recambio de calefactor y monto del subsidio

- `guia/02-no-te-mueras-lento.md` ítem 17 ("No calefacciones con leña; si puedes, cambia de
  combustible")
  Dato: el ítem dice que cambiar de calefactor "es el gasto grande del capítulo" y **no cita
  ningún monto** ni el monto del subsidio estatal de recambio.
  Sospecha: existiría un subsidio del programa de recambio de calefactores del Ministerio del Medio
  Ambiente que cubre parte del equipo nuevo, con porcentajes según el tramo del Registro Social de
  Hogares.
  Fuente que no se pudo leer:
  - `https://calefaccionsustentable.mma.gob.cl/` — la página oficial sí abre y dice "Por medio de
    este programa, los beneficiarios pueden acceder a un nuevo calefactor siempre y cuando hagan
    entrega de su antiguo calefactor y/o cocina el cuál debe estar instalado y en uso en la
    vivienda", y remite a `recambiodecalefactores.cl`. No publica montos.
  - `https://recambiodecalefactores.cl/` — responde 200 pero el contenido servido no corresponde al
    programa: la página devuelve un listado de casinos en línea con bonos de apuesta. No se puede
    usar como fuente.
  Cómo cerrarlo: pedir a la SEREMI del Medio Ambiente correspondiente las bases de la convocatoria
  vigente del programa de recambio de calefactores, con el porcentaje de cobertura y los montos, y
  citar la resolución que las aprueba.

---

## Notas de método

- **Los 52 DOI citados existen y resuelven en Crossref**, y además se descargó el resumen de cada
  estudio desde PubMed y se contrastaron una por una las cifras del campo `Beneficio` contra el
  texto del resumen. Ninguna cifra de este capítulo se tomó de memoria ni se recalculó.
- **Los datos chilenos salen del texto, no de la prensa**: el 33,3% de población fumadora, el 15,2%
  de exposición al humo en el hogar, el 20,3% en el lugar de trabajo o estudio, el 11,7% de consumo
  riesgoso de alcohol, el 86,7% de sedentarismo, el 15,0% que llega a cinco porciones de frutas y
  verduras, el 39,8% de sobrepeso, el 31,2% de obesidad y el 3,2% de obesidad mórbida se leyeron
  del PDF oficial de la ENS 2016-2017 del MINSAL, página por página.
- **Los textos legales se leyeron completos** con `tools/leychile.py` desde el servicio oficial de
  LeyChile. Se usaron: Ley 19.419 (tabaco, texto vigente), Ley 20.660 (ambientes libres de humo),
  Ley 20.606 (etiquetado), Ley 21.210 (impuesto a las bebidas), Ley 21.499 (biocombustibles
  sólidos), Ley 18.290 y Ley 20.580 (tránsito y alcohol).
- **Las 23 URL distintas citadas abren** con el mismo cliente que usa `tools/verificar.py`
  (`urllib` con agente de navegador). Se probaron una por una. El sitio de CONASET queda fuera por
  el problema de cadena de certificados descrito arriba, y por eso no se cita.
- **No se pudo usar el buscador general de LeyChile**
  (`bcn.cl/leychile/consulta/listado_n_sel`): la página se carga por JavaScript y desde consola
  devuelve "Este proceso demora demasiado...". El endpoint SPARQL `datos.bcn.cl/sparql` sí responde,
  pero solo devuelve recursos por etiqueta ("Ley 18290") y no el `idNorma` del decreto con fuerza de
  ley que fija el texto refundido de la Ley de Tránsito en 2009; por eso ese texto se citó por el
  `idNorma` que sí está publicado.
- **Los montos en pesos del capítulo se citan con su año.** La UTM de septiembre de 2026 es
  $71.721 y sale del Servicio de Impuestos Internos
  (`https://www.sii.cl/valores_y_fechas/utm/utm2026.htm`).
- **Ítems por los que se decidió no escribir un dato**: el efecto de la sal sobre la presión ya está
  en el capítulo 01 y no se repite acá; el sueño como recurso de energía está en el 03; el examen
  médico y la adherencia a tratamientos están en el 24.
