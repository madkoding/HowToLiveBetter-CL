# Verificación · capítulo 06, La lista negra

Marca `POR VERIFICAR` en `guia/06-la-lista-negra.md`. Se anota cada dato que no se pudo confirmar
contra una fuente oficial, con el ítem donde aparece y qué habría que consultar para cerrarlo.

Todos los pendientes de este capítulo son del mismo tipo: **precio oficial de un producto de venta
en farmacia o de una prestación privada**. La regla del contrato (§4) es que un valor sin fecha de
referencia no sirve, y la única fuente aceptada para plata es un organismo oficial. Los sondeos de
precios de SERNAC sí son fuente oficial, pero el último que cubre suplementos alimentarios es de
octubre de 2017 y cubre solo complejos de omega 3 y fórmulas nutricionales en polvo, no
multivitamínicos, vitamina D, vitamina C, glucosamina ni probióticos. La Superintendencia de Salud
publica el precio promedio facturado de exámenes y de prestaciones de salud sexual y reproductiva,
no de productos de farmacia ni de sesiones de cámara hiperbárica. Por eso esos ítems quedan sin
cifra de costo en vez de llevar un valor plausible.

---

- `guia/06-la-lista-negra.md` ítem 6 (rehabilitación y salud mental), línea del campo `Costo`
  Dato: no hay precios oficiales publicados de los programas privados de "internación" ni de las
  terapias sin respaldo en salud mental y adicciones que se cobran al mes.
  Sospecha: ninguno (no se propone un valor).
  Fuente que no se pudo leer como precio oficial: el tratamiento de SENDA se documenta como sin
  costo (<https://www.ventanillaunicasocial.gob.cl/ficha/243/tratamiento-rehabilitacion-senda>) pero
  SENDA no publica un arancel de programas privados; MINSAL no publica precios de prestaciones de
  salud mental privadas.
  Cómo cerrarlo: consultar el arancel MLE vigente de Fonasa y las circulares de precios de la
  Superintendencia de Salud, o pedir cotización formal a prestadores y registrarla con fecha.

- `guia/06-la-lista-negra.md` ítem 10 (multivitamínicos), línea del campo `Costo`
  Dato: precio del multivitamínico en Chile.
  Sospecha: la banda de decenas a cientos de miles de pesos al año se infiere del sondeo de SERNAC
  de octubre de 2017 y del precio de otros suplementos, no de un precio propio del multivitamínico.
  Fuente que no se pudo leer: SERNAC (2017) *Informe de precios: productos para el adulto mayor*,
  <https://www.sernac.cl/portal/619/w3-article-7601.html> — el informe cubre complejos de omega 3 y
  batidos saborizados (Ensure, Glucerna), no multivitamínicos. No hay sondeo posterior publicado.
  Cómo cerrarlo: solicitar a SERNAC un sondeo actualizado de suplementos alimentarios, o usar el
  precio de lista del fabricante con fecha.

- `guia/06-la-lista-negra.md` ítem 12 (vitamina D), línea del campo `Costo`
  Dato: precio del frasco de vitamina D en Chile.
  Sospecha: ninguno.
  Fuente que no se pudo leer: el sondeo de SERNAC de octubre de 2017 y su versión de 2015 no
  incluyen vitamina D; MINSAL no publica lista de precios de referencia de suplementos de venta
  directa.
  Cómo cerrarlo: precio de lista del fabricante con fecha, o pedido de información a MINSAL vía Ley
  de Transparencia.

- `guia/06-la-lista-negra.md` ítem 14 (glucosamina y condroitina), línea del campo `Costo`
  Dato: precio de glucosamina y condroitina en Chile.
  Sospecha: ninguno.
  Fuente que no se pudo leer: ningún sondeo oficial de SERNAC cubre estos productos; no hay listado
  oficial de precios.
  Cómo cerrarlo: sondeo de precios en farmacias con fecha, o solicitud de información a SERNAC.

- `guia/06-la-lista-negra.md` ítem 15 (probióticos), línea del campo `Costo`
  Dato: precio de los probióticos en Chile.
  Sospecha: ninguno.
  Fuente que no se pudo leer: el sondeo de SERNAC de octubre de 2017 no incluye probióticos.
  Cómo cerrarlo: sondeo de precios en farmacias con fecha, o solicitud de información a SERNAC.

- `guia/06-la-lista-negra.md` ítem 18 (cámara hiperbárica), línea del campo `Costo`
  Dato: precio de la sesión de cámara hiperbárica en Chile.
  Sospecha: ninguno.
  Fuente que no se pudo leer: el Explorador de precios de exámenes de la Superintendencia de Salud
  cubre 10 exámenes de laboratorio y 14 prestaciones de imagenología,
  <https://www.superdesalud.gob.cl/orientacion-en-salud/explorador-de-precios-de-examenes-de-laboratorio-e-imagenologia/>
  — la cámara hiperbárica no está entre ellas; tampoco aparece en el Radar de precios en salud
  sexual y reproductiva.
  Cómo cerrarlo: consultar el arancel MLE vigente de Fonasa y el arancel del prestador, con fecha.

---

## Cierres

Ninguno todavía. Cuando se cierre un pendiente: se corrige el ítem, se borra la marca
`POR VERIFICAR` y se anota la fecha acá. El historial queda en git.

## Última revisión

20 de septiembre de 2026.
