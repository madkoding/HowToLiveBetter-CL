# Guía de la Vida Rentable · Chile
### Cómo sacarle el mayor provecho a tu plata, tu tiempo y tu vida

Adaptación chilena de [**HowToLiveBetter**](https://github.com/dlgrv/HowToLiveBetter) — la guía
ordenada por costo/beneficio que reúne 528 recomendaciones con su evidencia y su fuente.

**Estado:** 26 de 32 capítulos escritos, **462 ítems** (371 grado A, 74 grado B, 17 grado C).

**Cada recomendación dice lo mismo, siempre:** cuánto cuesta (en plata y en tiempo), qué te
devuelve, **qué tan dura es la evidencia** (A, B o C), y **de dónde sale el dato**. Si no hay
fuente oficial que lo respalde, no está acá.

> **Esto no es una traducción.** El original es chino y describe leyes, instituciones, montos y
> trámites de China. Acá todo eso se borró y se reemplazó por la realidad chilena, verificado
> contra la fuente oficial: la ley en LeyChile, MINSAL, la Dirección del Trabajo, la CMF, el
> SERNAC, la SUSESO, el SII, el Registro Civil y el INE.
> Lo que sí se conservó tal cual son los **estudios internacionales** (ensayos, metaanálisis,
> cohortes) sobre tabaco, presión, ejercicio, sueño, cinturón, casco y demás: eso vale igual en
> Chile y no se toca.

---

## Cómo está ordenada

Dentro de cada capítulo, los ítems van **de mayor a menor conveniencia**: primero lo que es gratis
y salva vidas, después lo que cuesta plata o tiempo. No está ordenada por tema, está ordenada por
lo que te devuelve.

- **Grado de evidencia**
  - **A** — hay cifras: metaanálisis, cohorte grande, ensayo aleatorizado, o el texto oficial de
    una ley. Puedes confiar en el número.
  - **B** — hay estudio que lo respalda, pero no se puede cuantificar bien, o es un solo estudio.
  - **C** — consenso o práctica generalizada, sin literatura directa. La guía lo dice cuando es C.

- **Lo que ganas** (cada ítem declara una sola cosa principal, y esas cosas **no se comparan
  entre sí**): vida, plata, tiempo o libertad. Un año de vida no se "convierte" en pesos.

- **Los costos** (los tres que importan): plata, tiempo y aguante. Un consejo gratis que exige
  pelearse con uno mismo todos los días es más caro que uno que cuesta unos pesos una vez.

## Buscador

`index.html` es la página de búsqueda: filtra por palabra, capítulo, grado de evidencia y las
dimensiones de costo (plata, tiempo, aguante, beneficio). Los datos se leen del propio texto de
`guia/`: si corriges el texto, el buscador cambia solo.

Para verlo en local:

```bash
python3 tools/construir.py        # regenera datos.json desde guia/
python3 -m http.server 8000       # abre http://localhost:8000
```

Con los capítulos escritos hasta ahora: **363 ítems**, de los cuales **288 son grado A**, 61 grado B
y 14 grado C.

En GitHub, activar Pages (Deploy from a branch → main → /) y queda online.

---

## Los 32 capítulos

| # | Capítulo | Qué resuelve |
|---|---|---|
| 01 | [No te mueras joven](guia/01-no-te-mueras-joven.md) | Causas externas: cinturón, casco, fuego, agua, vacunas, tamizaje |
| 02 | [No te mueras lento](guia/02-no-te-mueras-lento.md) | Tabaco, alcohol, sedentarismo, dieta, aire, sueño |
| 03 | [No gastes tu energía](guia/03-no-gastes-tu-energia.md) | Atención, interrupciones, notificaciones, decisiones cansadas |
| 04 | [No gastes tu tiempo](guia/04-no-gastes-tu-tiempo.md) | Costo hundido, proyectos sin retorno, postergación |
| 05 | [No gastes tu plata](guia/05-no-gastes-tu-plata.md) | Deuda cara, comisiones, fraude, ahorro |
| 06 | [La lista negra](guia/06-la-lista-negra.md) | Lo que parece buena idea y no lo es |
| 07 | [Sin plata: qué reclamar](guia/07-sin-plata-que-reclamar.md) | Cesantía, beneficios, salud, deuda impagable |
| 08 | [No te metas en líos](guia/08-no-te-metas-en-lios.md) | Tránsito, estafas, acusaciones, contratos y deudas |
| 09 | [Líneas rojas legales](guia/09-lineas-rojas-legales.md) | Lo que la gente común cruza sin saber que es delito |
| 10 | [Pololeo y matrimonio](guia/10-pololeo-y-matrimonio.md) | Régimen de bienes, AUC, divorcio, violencia en el pololeo |
| 11 | [Líneas rojas para informáticos](guia/11-lineas-rojas-tech.md) | Datos personales, delitos informáticos, código y contratos |
| 12 | [Emprender sin perder la casa](guia/12-emprender.md) | Constituir, impuestos, boletas, patentes, deudas |
| 13 | [Emergencias: qué hacer primero](guia/13-emergencias.md) | Sismo, tsunami, incendio, RCP, ACV, monóxido |
| 14 | [Cuentas y seguridad](guia/14-cuentas-y-seguridad.md) | ClaveÚnica, contraseñas, fraude con tarjetas, datos |
| 15 | [Arrendar y comprar vivienda](guia/15-arrendar-y-comprar.md) | Contrato, garantía, copropiedad, subsidios |
| 16 | [Vivir con una enfermedad crónica](guia/16-enfermedad-cronica.md) | GES, adherencia, remedios, no abandonar el tratamiento |
| 17 | [Los viejos en la casa](guia/17-los-viejos-en-la-casa.md) | Herencia, PGU, fraudes a adultos mayores, caídas |
| 18 | [¿Conviene tener hijos?](guia/18-conviene-tener-hijos.md) | Los costos reales y los beneficios estatales |
| 19 | [Pega, despido y accidentes](guia/19-pega-despido-accidentes.md) | Contrato, finiquito, horas extra, Ley 16.744 |
| 20 | [El recién nacido](guia/20-recien-nacido.md) | Sueño seguro, lactancia, vacunas, señales de alarma |
| 21 | [Viajar y vivir afuera](guia/21-viajar-y-vivir-afuera.md) | Consulados, seguros, estafas de empleo en el extranjero |
| 22 | [Cómo descansar](guia/22-como-descansar.md) | Ejercicio, estrés, sueño, carrete seguro |
| 23 | [Qué aprender](guia/23-que-aprender.md) | Retorno de estudiar, capacitación estatal, oficios |
| 24 | [Ver al médico](guia/24-ver-al-medico.md) | Fonasa, GES, listas de espera, urgencias |
| 25 | [Cuando alguien muere](guia/25-cuando-alguien-muere.md) | Certificado, testamento, posesión efectiva, pensiones |
| 26 | [Sitios y plataformas](guia/26-sitios-y-plataformas.md) | Datos personales, ciberseguridad, boleta electrónica |
| 27 | [Embarazo y parto](guia/27-embarazo-y-parto.md) | Control prenatal, subsidio maternal, parto, permisos |
| 28 | [No arruines tu salud por verte mejor](guia/28-no-arruines-tu-salud.md) | Dietas extremas, esteroides, estética sin acreditación |
| 29 | [Después de un golpe duro](guia/29-despues-de-un-golpe-duro.md) | Duelo, cesantía, diagnóstico grave, primeros meses |
| 30 | [Los niños en edad escolar](guia/30-ninos-en-edad-escolar.md) | Colegio, bullying, sueño, alimentación, pantallas |
| 31 | [Después de los 18](guia/31-despues-de-los-18.md) | Estudiar, trabajar, servicio militar, rutas disponibles |
| 32 | [Estudiar afuera](guia/32-estudiar-afuera.md) | Becas, convalidación, costos, seguros |

---

## Cómo se lee un ítem

```
### N. La acción, en imperativo
<!-- costos: plata=0 tiempo=poco aguante=no beneficio=alto medida=muerte -->
- Costo:       lo que sale de tu bolsillo y de tu día
- En simple:   lo mismo que Beneficio, pero en habla normal, sin siglas
- Beneficio:   los números crudos, con su intervalo, tal como están en la fuente
- Evidencia:   A, B o C
- Fuentes:     de dónde sale, con enlace que abre
- Notas:       a quién aplica, qué no cubre, y qué está pendiente de verificar
```

La línea **En simple** es la que decide. La de abajo está con los números crudos para quien
quiera revisar por su cuenta.

---

## Lo que esta guía NO es

- **No es consejo médico, legal ni financiero.** Es información con su fuente para que decidas tú.
- **No reemplaza a la ley vigente.** Cita la norma y el artículo; si algo cambió, manda la ley.
- **No está completa.** Los datos marcados `POR VERIFICAR` no se pudieron confirmar contra la
  fuente oficial en el momento de escribir. Están así a propósito: preferimos dejar el hueco
  visible antes que rellenarlo con un número inventado.
- **No dice cómo delinquir.** Los ítems de "línea roja" existen para advertir.

## Reglas del proyecto

- [ADAPTACION.md](ADAPTACION.md) — el contrato: qué se conserva, qué se reemplaza, formato de
  ítem, grados de evidencia, fuentes aceptadas y prohibiciones.
- [PLAN.md](PLAN.md) — los 32 capítulos y qué los alimenta.
- [docs/verificacion/](docs/verificacion/) — registro de todo lo que quedó pendiente y por qué.
- [skill/](skill/) — la **skill universal** para cualquier agente: cómo adaptar una guía de este
  tipo a otro país. Es el método, no el contenido.

## Herramientas

```bash
python3 tools/verificar.py          # valida formato, etiquetas, grados, conteos
python3 tools/verificar.py --urls   # además prueba cada enlace y cada DOI
python3 tools/construir.py          # regenera datos.json del buscador
python3 tools/briefing.py           # dossier de redacción de cada capítulo
python3 tools/leychile.py art 1984 490   # trae un artículo del texto oficial de la ley
python3 scripts/nuevo_capitulo.py 33 "clave" "Título"
```

El validador revisa, entre otras cosas, que la línea `En simple` **no introduzca números que no
estén en `Beneficio`**: así un dato inventado no se cuela sin fuente.

## Licencia

[Unlicense](LICENSE) — dominio público, igual que el original. Úsala, cópiala, modifícala.