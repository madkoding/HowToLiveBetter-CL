# Verificación — 08. No te metas en líos: ley y patrimonio

Datos marcados `POR VERIFICAR` en `guia/08-no-te-metas-en-lios.md`, con lo que falta y dónde
buscarlo. Ninguno de estos huecos se rellenó con un valor plausible.

---

## Ítem 10 · Aviso por tarjeta o cuenta robada — umbral de retención del artículo 5 de la Ley 20.009

**Línea del ítem:**
> POR VERIFICAR: el artículo 5 deja el monto desde el cual el banco puede retener y discutir en un
> umbral que fija un reglamento del Ministerio de Hacienda, entre 15 y 35 unidades de fomento; no
> revisé ese decreto, así que el umbral vigente queda pendiente.

**Lo que sí está verificado, leído del texto oficial:**

- Ley 20.009, artículo 5, inciso final: "Un reglamento emitido por el Ministerio de Hacienda,
  suscrito además por el Ministerio de Economía, Fomento y Turismo, a través de uno o más decretos
  supremos [...] definirá uno o más umbrales de restitución [...]. Con todo, el o los umbrales
  establecidos no podrán ser inferiores a 15 unidades de fomento, ni superiores a 35 unidades de
  fomento."
- Ley 20.009, artículo 5, incisos primero y segundo: los plazos de cancelación de cargos o
  restitución de fondos son de diez días hábiles, y de quince días hábiles cuando se trata de giros
  en avances en efectivo o cajeros automáticos.

**Qué falta:** el decreto supremo vigente del Ministerio de Hacienda que fija el umbral concreto
dentro del rango legal de 15 a 35 unidades de fomento (y si hay umbrales diferenciados por medio de
pago o producto).

**Dónde habría que buscarlo:** LeyChile, normas del Ministerio de Hacienda y de Economía publicadas
entre el 30 de mayo de 2024 y la fecha; la sección de normas de la CMF.

**URL que no se pudo resolver:** el texto de la ley no remite a un número de decreto, y no se
encontró el decreto en el texto consolidado leído:
<https://www.bcn.cl/leychile/navegar?idLey=20009>

---

## Ítem 12 · Antes de firmar — tasa de interés corriente y máximo convencional vigentes

**Línea del ítem:**
> POR VERIFICAR: el valor vigente de la tasa de interés corriente y del máximo convencional lo
> publica la CMF cada mes en su sitio y en el Diario Oficial, y no revisé la publicación del mes,
> así que no se da una cifra.

**Lo que sí está verificado, leído del texto oficial:**

- Ley 18.010, artículo 6, inciso final: "No podrá estipularse un interés que exceda el producto del
  capital respectivo y la cifra mayor entre: 1) 1,5 veces la tasa de interés corriente que rija al
  momento de la convención [...] y 2) la tasa de interés corriente que rija al momento de la
  convención incrementada en 2 puntos porcentuales anuales [...]. Este límite de interés se denomina
  interés máximo convencional."
- Ley 18.010, artículo 6, inciso penúltimo: "No se podrá cobrar intereses por sobre aquella parte de
  la deuda que ya esté pagada."
- Ley 18.010, artículo 8: "Se tendrá por no escrito todo pacto de intereses que exceda el máximo
  convencional."

**Qué falta:** el porcentaje de la tasa de interés corriente y del interés máximo convencional del
período vigente, por segmento de crédito.

**Dónde habría que buscarlo:** Comisión para el Mercado Financiero, publicación mensual de tasas de
interés corriente (sitio web y Diario Oficial, dentro de la primera quincena del mes siguiente).

**URL que no se pudo leer con el dato dentro:** <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
(la página abre, pero la tabla de tasas del período no se pudo extraer del texto de la ley, que
remite a la publicación de la CMF y no la reproduce).

---

## Nota de método

Los demás números del capítulo —penas, plazos, montos en unidades tributarias mensuales y unidades
de fomento— salen del texto oficial vigente leído vía `tools/leychile.py` (endpoint
`nuevo.leychile.cl/servicios`) y de las publicaciones del Servicio de Impuestos Internos para el
valor de la unidad tributaria mensual ($71.721, septiembre de 2026) y de la unidad de fomento
($40.975,41, 20 de septiembre de 2026). Unidades tributarias y unidades de fomento cambian todos los
meses: cualquier conversión a pesos que se haga con este capítulo tiene que rehacerse con el valor
del día.
