# Contrato de adaptación a Chile · HowToLiveBetter-CL

Este archivo es la **regla del repo**. Rige sobre cualquier trabajo de contenido: escribir,
traducir, revisar o ampliar ítems. Si una instrucción de este archivo choca con lo que dice
un capítulo, manda este archivo.

---

## 1. Qué es esto

Adaptación chilena de [dlgrv/HowToLiveBetter](https://github.com/dlgrv/HowToLiveBetter)
(guía de vida ordenada por costo/beneficio, 528 ítems, dominio público · Unlicense).

La estructura, el método y el formato de ítem se conservan. **El contenido normativo,
institucional y económico se reemplaza completo por el chileno.** Lo que en el original es
`中国疾控中心` acá es MINSAL; lo que es `失业保险` acá es el seguro de cesantía de la AFC;
lo que es `元` acá es CLP con sueldos y precios chilenos reales.

Lo que se conserva del original, porque es evidencia sanitaria internacional y sigue valiendo
en Chile: los estudios (RCT, metaanálisis, cohortes) sobre tabaco, presión arterial, ejercicio,
sueño, caídas, cinturón, casco, ahogamiento, vacunas, etc. Eso **no se reescribe ni se
recalcula**: se cita el estudio tal cual y se cambia el dato país cuando corresponde.

> Regla de oro: **el número es internacional o es chileno, nunca inventado.**
> Si no encuentras el dato chileno, se escribe `POR VERIFICAR` (pendiente de verificación) y se deja
> constancia en `docs/verificacion/`. No se rellena con un valor plausible.

---

## 2. Formato obligatorio de cada ítem

Cada recomendación es un bloque que empieza con `### N. <título imperativo>` y lleva
**exactamente** estas líneas, en este orden:

```markdown
### 7. Mídete la presión; si está alta, tómala hasta llegar a la meta
<!-- costos: plata=0 tiempo=poco aguante=algo beneficio=alto medida=muerte -->
- Costo: $0; 1 minuto por medición. Un monitor de presión cuesta entre $25.000 y $60.000.
- En simple: Por cada 10 mmHg que baja la presión, la probabilidad de un infarto o un ACV baja cerca de un quinto y la de morir, cerca de un 13%. En Chile, 1 de cada 4 adultos es hipertenso y la mayoría no lo sabe.
- Beneficio: metaanálisis (123 ensayos, más de 610.000 personas): cada 10 mmHg de baja en la presión sistólica da eventos cardiovasculares mayores RR 0,80 (IC 95% 0,77 a 0,83), ACV RR 0,73, insuficiencia cardíaca RR 0,72, mortalidad total RR 0,87 (IC 95% 0,84 a 0,91).
- Evidencia: A
- Fuentes: Ettehad D y cols. (2016). Blood pressure lowering for prevention of cardiovascular disease and death. Lancet. <https://doi.org/10.1016/S0140-6736(15)01225-8> ; MINSAL. Encuesta Nacional de Salud 2016-2017, resultados de presión arterial. <https://www.minsal.cl/>
- Notas: La meta (130 vs 140) sigue en disputa; lo que no está en disputa es saber que la tienes y bajarla. La mayoría de los hipertensos en Chile no está en tratamiento o no está compensado.
```

### 2.1 La etiqueta de costos (obligatoria, invisible en GitHub)

Va en la línea inmediatamente después del título, antes de `- Costo:`:

```
<!-- costos: plata=0|poco|mucho tiempo=poco|medio|mucho aguante=no|algo|si beneficio=alto|medio|bajo medida=muerte|plata|tiempo|libertad -->
```

Valores permitidos, sin excepciones:

| Campo | Valores | Significado |
|---|---|---|
| `plata` | `0` / `poco` / `mucho` | `0` = gratis o ahorra; `poco` = decenas de miles de pesos o hasta ~$30.000/mes; `mucho` = cientos de miles o gasto mensual significativo |
| `tiempo` | `poco` / `medio` / `mucho` | `poco` = minutos o de paso; `medio` = una vez unas horas, o horas por semana; `mucho` = todos los días |
| `aguante` | `no` / `algo` / `si` | `no` = se hace una vez y listo; `algo` = cambiar un hábito o aguantar una molestia; `si` = pelear contra la costumbre todos los días |
| `beneficio` | `alto` / `medio` / `bajo` | Se asigna mecánicamente desde la línea `Beneficio` con los umbrales de §2.4 |
| `medida` | `muerte` / `plata` / `tiempo` / `libertad` | Qué se gana principalmente. **No se comparan entre sí.** |

La etiqueta alimenta el buscador (`index.html`). Si falta, el ítem no aparece al filtrar.
El buscador se rompe con un valor fuera de la lista: valida antes de commitear.

### 2.2 Los cinco campos

- **`- Costo:`** qué sale de tu bolsillo y de tu día, en pesos chilenos y en tiempo.
  Sé concreto: "entre $25.000 y $60.000", "3 minutos por lectura".
- **`- En simple:`** una o dos frases que traducen el campo Beneficio a habla normal.
  **Prohibido** que aparezcan `HR`, `RR`, `OR`, `IC`, `cohorte`, `metaanálisis`, `ensayo`,
  `significativo` ni ningún número que no esté ya en `Beneficio`. Se escribe para alguien que
  decide y no es estadístico. Ejemplos válidos: "la mitad menos", "cerca de un quinto",
  "de cada 10 personas, 1 muere".
- **`- Beneficio:`** los números **crudos**, tal como están en la fuente, con IC y todo.
  Si el ítem es legal o de plata, es el resultado concreto ("te devuelven el 100% del finiquito
  más un 30% de recargo si el despido es injustificado"). Este campo no se "simplifica".
- **`- Evidencia:`** `A`, `B` o `C` (ver §2.3). Si hay disputa en la literatura, va
  `A (en disputa)` o `B (en disputa)` y las notas tienen que listar la evidencia contraria.
- **`- Fuentes:`** ver §2.5.
- **`- Notas:`** límites, a quién aplica, qué no cubre, y `POR VERIFICAR:` con lo que no se pudo
  verificar. Es el campo más honesto del ítem: si algo está mal, se dice acá.

Un ítem no pasa de 10 líneas de cuerpo. Lo que no cabe va a `docs/`.

### 2.3 Grados de evidencia

| Grado | Cuándo |
|---|---|
| **A** | Hay cifra cuantificable: metaanálisis, cohorte grande, ensayo aleatorizado, o estadística oficial verificada contra el texto original |
| **B** | Hay estudio que lo respalda pero no se puede cuantificar bien, o viene de un solo estudio o de muestra chica |
| **C** | Consenso o práctica generalizada sin literatura directa que lo respalde |

En temas legales y de plata, `A` requiere **el texto oficial leído**: la ley en LeyChile,
el dictamen de la Dirección del Trabajo, el instructivo de la CMF, la resolución de la SMA.
Un blog de abogados, un medio de prensa o una cuenta de Instagram **no** dan grado A,
y en general no se aceptan como fuente (ver §2.5).

### 2.4 Cómo se asigna `beneficio` (mecánico, no por olfato)

| Medida | `alto` | `medio` | `bajo` |
|---|---|---|---|
| `muerte` | baja ≥ 20% | baja 10–20% | baja < 10% o solo indicador intermedio |
| `plata` | millones de pesos | cientos de miles | decenas de miles |
| `libertad` | evita una condena penal | evita detención o multa | evita un juicio civil |
| `tiempo` | horas al día | horas a la semana | una vez |

Si los datos no alcanzan para aplicar la tabla, se decide con criterio y **se anota en la
nota por qué** (`POR VERIFICAR` no sirve para esto: hay que justificarlo).

### 2.5 Fuentes: qué sirve y qué no

**Sí:**

- Leyes y reglamentos: LeyChile (`bcn.cl/leychile`), Diario Oficial.
- Organismos: MINSAL, ISP, FONASA/Isapres/CMF, SUSESO, Dirección del Trabajo, SERNAC,
  SII, Registro Civil, SP (Superintendencia de Pensiones), AFC, JUNAEB, MINEDUC,
  Carabineros/PDI, ONEMI/SENAPRED, MTT, MINVU, ChileAtiende.
- Estadísticas: INE, DEIS/MINSAL, Banco Central, Casen.
- Salud internacional: OMS, OPS, CDC, USPSTF, Cochrane, y **las publicaciones originales
  con DOI**.
- Municipalidades y universidades, solo para datos locales concretos.

**No:**

- Prensa, blogs, "estudios" de clínicas, cuentas de redes sociales, comparadores de
  productos, agregadores de trámites (esos copian de otros y se desactualizan).
- Ninguna fuente sin URL o identificador verificable.
- Cifras de memoria. Si no hay fuente, no hay cifra.

Cada URL citada tiene que abrir. La herramienta `tools/verificar.py` revisa los enlaces y el
formato; el trabajo de que el contenido sea correcto es humano.

---

## 3. Tratamiento de lo que no existe en Chile

El original describe realidades que en Chile no son. No se traducen: se **reemplazan por su
equivalente chileno** o se eliminan si no hay equivalente.

| Original (China) | Chile |
|---|---|
| 医保 (seguro médico) | Fonasa / Isapre, tramos A–D, plan Auge-GES, CAEC |
| 失业保险 | Seguro de cesantía (AFC) + indemnización por años de servicio |
| 劳动仲裁 | Dirección del Trabajo (DT) → Tribunales del Trabajo, procedimiento monitorio |
| 社保 (cotizaciones) | AFP + cotizaciones previsionales, 7% salud, Ley 21.735 (reforma) |
| 住房公积金 | Cuenta 2 / crédito hipotecario (no hay fondo obligatorio de vivienda) |
| 低保 / 救助站 | Registro Social de Hogares, Chile Seguridades y Oportunidades, subsidios, hospederías |
| 兵役登记 | Servicio militar: inscripción, Ley 21.674 (sorteo), no hay conscripción obligatoria |
| 彩礼 | No existe; pero sí régimen de bienes, compensación económica (Ley 20.152), unión civil |
| 户口 (hukou) | No existe registro domiciliario |
| 12308 (consular) | Consulados de Chile, DIRAC, asistencia consular |
| 12356 (salud mental) | Salud Responde 600 360 7777, fono 1510 de Carabineros, *4141 de prevención del suicidio |
| 消费者权益 (12315) | SERNAC, Ley 19.496, Ley 21.398 (Pro-Consumidor), Juzgado de Policía Local |
| 交通事故处理 | Ley 18.290 Tránsito, SOAP, seguro obligatorio, Carga de la prueba |
| 工伤 (work injury) | Ley 16.744: mutual, DIAT/DIEP, subsidio, invalidez, pensiones |
| 医保异地结算 | Bono Fonasa, modalidad libre elección, tramos, convenios |
| 殡葬 | Registro Civil (defunción), Registro Civil + cementerios, Ley 20.585 |
| 学区房 | Sistema de admisión escolar (SAE), Ley 20.845, copago |
| 三支一扶 / 公务员 | Carrera funcionaria, servicio civil, municipios, prácticas |
| 平台合规 (ICP 备案) | Ley 19.628 (datos), Ley 21.719 (nueva), Ley 21.398, SII (boleta electrónica), patente municipal |

Lo que **no** tiene equivalente se elimina sin reemplazo. Lo que tenga un equivalente
aproximado pero distinto (p. ej. matrimonio vs. Acuerdo de Unión Civil) se explica la
diferencia en una nota; no se fuerza la simetría.

---

## 4. Cifras: dónde va cada una

- **Salud y mortalidad:** la cifra internacional del estudio + el dato país de MINSAL/INE si
  existe. Ejemplo: "cepillarse los dientes" (internacional) + "en Chile X% de los niños de 6
  años tiene caries" (DEIS/MINSAL).
- **Plata:** pesos chilenos nominales y fecha de referencia. Un valor sin fecha no sirve:
  escribir "sueldo mínimo $529.000 (2026)" y no "$500.000".
- **Legal:** artículo y ley citados textualmente en `Fuentes`. El cuerpo del ítem dice qué
  hacer, no qué artículo. Ej.: "no tienes que firmar el finiquito; si el despido es
  injustificado puedes reclamar en la Inspección del Trabajo dentro de 60 días hábiles."
- **Tiempo:** días hábiles vs. días corridos importa, y mucho. Especificar siempre.

---

## 5. Tono

- Español de Chile, registro escrito serio, **sin modismos forzados**. Los modismos chilenos
  entran cuando son el nombre real de algo (`AFP`, `finiquito`, `boleta`, `pase escolar`,
  `bono`, `fondo de cesantía`, `clave única`, `TNE`) — no para decorar.
- Nunca "weón", "bacán", "cuático" ni chilenismos de conversación en el texto.
- Nada de exclamaciones. Nada de moralizar, nada de "deberías". Se muestran costos y
  beneficios y se deja decidir.
- Verbos en imperativo o en "tú" cuando la acción es del lector; en impersonal cuando es
  información ("el finiquito se firma en la Inspección del Trabajo").
- Sin anglicismos innecesarios. Sin abreviaturas de estadística en `En simple`.
- Los tramos de edad, montos y plazos se escriben completos: "mayores de 65 años",
  "$529.000", "30 días corridos". No "65+", no "530k", no "30d".

---

## 6. Prohibiciones duras

Falla de revisión automática, sin importar qué tan bueno sea el resto del ítem:

1. Un número, DOI o URL alterado, inventado o "redondeado a mejor".
2. Un valor `HR`/`RR`/`OR`/`IC` distinto del que está en la fuente.
3. Contenido inventado: una recomendación, una prestación, un plazo o un trámite que no
   existe en la fuente citada. **Esta es la falta más grave del repo.** Es preferible un
   capítulo con 6 ítems verificados que uno con 20 rellenos.
4. La etiqueta `costos` con un valor fuera de la lista, o ausente.
5. Falta de alguna de las líneas obligatorias (`Costo`, `En simple`, `Beneficio`, `Evidencia`,
   `Fuentes`). `Notas` es opcional pero se espera.
6. Palabras estadísticas o números nuevos en `En simple`.
7. Recomendaciones médicas que contradigan MINSAL/OPS, o legales que contradigan la ley
   vigente.
8. Consejo sobre cómo evadir impuestos, cómo cometer fraude, cómo drogarse, cómo hacer daño,
   o cómo saltarse las reglas de entrada a otro país. Los ítems de "línea roja" existen para
   advertir, no para instruir.

---

## 7. Verificación: cómo marcar lo que no pudiste comprobar

Cuando no se puede confirmar un dato contra la fuente oficial:

- En el ítem: `- Notas: POR VERIFICAR: <qué falta y dónde habría que buscarlo>.`
- En `docs/verificacion/<capitulo>.md`: la línea completa, el dato sospechado y la URL que
  no se pudo leer o no existía.

`POR VERIFICAR` es una salida legítima y esperada. Inventar es la única falta inexcusable.

---

## 8. Antes de hacer commit

1. `python3 tools/verificar.py` → debe dar 0 errores.
2. Contar los ítems y revisar que el número en `README.md` calce.
3. Revisar que cada URL nueva abre (la herramienta lo hace).
4. Si cambió un monto legal, revisar que las notas de fecha estén actualizadas.
