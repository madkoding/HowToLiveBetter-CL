# Cómo se hizo esta guía

Este archivo explica el método con el que se escribió la guía, para quien quiera
revisarla, corregirla o adaptarla a otro país. El método completo, en versión portable
a cualquier agente, está en [`skill/adapting-evidence-based-life-guides/`](skill/).

## Qué se adaptó y qué no

Esta guía no es una traducción del original chino. Una traducción habría conservado
leyes, agencias, montos y trámites que en Chile no existen, con el aspecto de ser
ciertos. Lo que se hizo fue separar el corpus original en tres categorías antes de
escribir una sola línea:

| Categoría | Qué es | Qué se hizo |
|---|---|---|
| **Evidencia universal** | Ensayos, metaanálisis y cohortes sobre fisiología: tabaco, presión, sueño, cinturón, casco, ahogamiento, vacunas | Se conservó el estudio **con sus cifras exactas y su DOI**. No se recalculó nada. |
| **Norma del país** | Leyes, organismos, montos, plazos, trámites | Se **borró y se reemplazó** por el equivalente chileno, verificado contra la fuente oficial. |
| **Relativo a la cultura** | Matrimonio, herencia, familia, deberes hacia desconocidos | Se **reescribió desde cero** con el derecho chileno. |

La tabla de sustitución completa está en [`ADAPTACION.md`](ADAPTACION.md). Ejemplos de
lo que cambió:

| Original (China) | Chile |
|---|---|
| 医保 (seguro médico) | Fonasa / Isapre, tramos A–D, plan GES |
| 失业保险 | Seguro de cesantía (AFC) + indemnización |
| 劳动仲裁 | Dirección del Trabajo → Tribunales del Trabajo |
| 社保 | AFP, cotizaciones previsionales, 7% de salud |
| 住房公积金 | Cuenta 2 / crédito hipotecario |
| 低保 / 救助站 | Registro Social de Hogares, subsidios, hospederías |
| 兵役登记 | Servicio militar e inscripción al registro de reclutamiento |
| 彩礼 (dote) | No existe: rigen el régimen de bienes y la compensación económica |
| 户口 | No existe: se eliminan todos los ítems que dependen de él |
| 12308 (consular) | Consulados de Chile, DIRAC |
| 12356 | Salud Responde 600 360 7777, *4141 |

Y hubo que **agregar** lo que el original no tiene porque no ocurre en China y en Chile
es central: sismos (con la regla de que en construcción no sismo resistente se evacúa
durante el movimiento, mientras en una sismo resistente se protege y se afirma),
tsunami con evacuación autónoma sin esperar aviso oficial, humo de leña, la jornada de
40 horas, el calendario de inmunizaciones y el copago cero de Fonasa.

## Los dos niveles de verificación

**Lo que prueba un script** (`tools/verificar.py`):

- Que cada ítem tenga sus campos, en orden, con la etiqueta de costos bajo el título.
- Que el grado de evidencia sea A, B o C, y que si está marcado en disputa traiga la
  evidencia contraria.
- Que **la línea «En simple» no introduzca números que no estén en «Beneficio»**. Esto
  es lo que impide que un dato inventado se cuele sin fuente.
- Que «En simple» no use siglas estadísticas.
- Que cada ítem cite al menos una URL, y que esas URLs abran.
- Que **cada DOI exista de verdad**, consultando Crossref y comparando el título real
  con el citado. Así se detectó un DOI inventado durante la escritura.
- Que los conteos del README calcen con lo que hay en `guia/`.

**Lo que solo prueba una persona leyendo la fuente**: que el artículo citado diga lo que
el ítem afirma. El script no puede saberlo. En el cierre se comprobó a mano, por ejemplo,
que el artículo 20 de la Ley 18.101 de arriendo dice literalmente que las firmas «serán
autorizadas por un notario público, quien deberá solicitar los títulos que habiliten al
arrendador a ceder el uso del inmueble», que es lo que el capítulo 15 afirma.

## Los datos marcados POR VERIFICAR

Hay 140 datos marcados así, y están marcados **a propósito**. Son cosas que no se
pudieron confirmar contra una fuente oficial: precios de farmacia que ningún organismo
publica, montos de subsidio sin año de referencia, o dos fuentes oficiales que se
contradicen entre sí (el deducible del CAEC, por ejemplo, difiere entre la ley y la
Superintendencia de Salud).

La regla del proyecto es que **un dato que no se puede verificar se marca y se anota,
nunca se rellena con un valor plausible**. Un número inventado es indetectable en
revisión, y basta uno para que el lector desconfíe de los otros 567. Cada marca tiene su
entrada en [`docs/verificacion/`](docs/verificacion/), con el dato, la sospecha, la
fuente que no se pudo leer y el camino para cerrarlo.

Un ejemplo de cómo se cierran: el capítulo 05 declaró honestamente que no pudo leer el
decreto que fija el umbral de la Ley 20.009; el redactor del capítulo 14 lo encontró
(decreto exento 473, del 30 de enero de 2026, umbral de 35 UF) y el pendiente se cerró
en los dos capítulos. **El registro es compartido, no privado de cada redactor**, y eso
es deliberado.

## Herramientas

```bash
python3 tools/verificar.py              # estructura: campos, etiquetas, grados, conteos
python3 tools/verificar.py --urls       # además prueba cada enlace y cada DOI (paralelo, con caché)
python3 tools/verificar.py --json       # informe para máquinas (CI)
python3 tools/construir.py              # regenera datos.json, que alimenta el buscador
python3 tools/sincronizar.py            # sincroniza los conteos del README con guia/
python3 tools/sincronizar.py --revisar   # solo comprueba (lo que corre el CI)
python3 tools/leychile.py art idNorma=207436 22   # trae un artículo del texto oficial
python3 tools/briefing.py 19            # dossier de redacción de un capítulo
```

Todo es Python 3 de biblioteca estándar: no hay nada que instalar.

## Cómo está ordenada la guía

Dentro de cada capítulo, los ítems van de mayor a menor conveniencia: primero lo gratis
que salva vidas. El nivel de beneficio no se asigna por olfato, sale de una tabla de
umbrales publicada en el contrato (por ejemplo, en la dimensión vida: una baja de 20% o
más es alto, entre 10% y 20% medio, menos de 10% bajo). Eso hace que el orden sea
comparable entre capítulos escritos por distintas manos.

Los cuatro «lo que ganas» —vida, plata, tiempo, libertad— **no se comparan ni se
suman entre sí**: un año de vida no se convierte en pesos. La guía lo dice en su propia
portada para que nadie fabrique esa equivalencia después.

## Qué no es esta guía

No es consejo médico, legal ni financiero: es información con su fuente para que decidas
tú. No reemplaza a la ley vigente: cita la norma y el artículo, y si algo cambió, manda
la ley. No está completa: los pendientes están visibles. Y no explica cómo delinquir: los
ítems de «línea roja» existen para advertir.
