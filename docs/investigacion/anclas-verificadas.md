# Anclas verificadas

Datos que quedaron **confirmados leyendo la fuente oficial** durante este proyecto. No son
investigación pendiente: son hechos con su fuente, listos para citar. Si escribes un capítulo que
los usa, no los vuelvas a buscar ni los cambies: cita la fuente tal como está acá.

Si un dato de este archivo resulta estar equivocado, corrígelo acá **y** en los capítulos que lo
usen, y anótalo en `docs/verificacion/`.

---

## Jornada laboral (capítulos 03, 19)

- **Ley 21.561**, "Modifica el Código del Trabajo con el objeto de reducir la jornada laboral".
  Publicada **2023-04-26**, plena vigencia **2025-07-11**.
- Artículo 22 del Código del Trabajo, texto vigente: *"La duración de la jornada ordinaria de
  trabajo no excederá de cuarenta horas semanales y su distribución se podrá efectuar en cada
  semana calendario o sobre la base de promedios semanales en lapsos de hasta cuatro semanas"*.
- Artículo 22 bis: en la modalidad de promedio en ciclo de hasta 4 semanas, la jornada no puede
  exceder **45 horas** en una semana, ni extenderse con ese tope por más de dos semanas continuas;
  por negociación colectiva o pacto con sindicatos el tope puede ampliarse a **52 horas**.
- Artículo 31, oración final agregada: en la modalidad del art. 22 bis, la suma de jornada
  ordinaria y extraordinaria **en ningún caso** puede superar las **52 horas semanales**.
- Fuente: <https://www.bcn.cl/leychile/navegar?idLey=21561>

## Calendario de inmunizaciones 2026 (capítulos 01, 20, 27)

Calendario del Programa Nacional de Inmunizaciones del MINSAL, según el documento oficial 2026:

- **Recién nacido:** BCG (dosis única) y Hepatitis B (dosis única).
- **2, 4 y 6 meses:** Hexavalente (Hepatitis B, Difteria, Tétanos, Tos Convulsiva, Hib,
  Poliomielitis) — 1ª, 2ª y 3ª dosis.
- **2 y 4 meses:** Meningocócica recombinante serogrupo B — 1ª y 2ª dosis; refuerzo posterior.
- **2, 4 y 6 meses:** Neumocócica conjugada 13 valente — 1ª y 2ª dosis, y 3ª **solo para
  prematuros**; refuerzo posterior.
- **12 meses:** SRP (sarampión, rubéola, parotiditis) 1ª dosis; Neumocócica conjugada 13 valente
  refuerzo; Meningocócica conjugada tetravalente (A, C, W-135, Y) dosis única; Hepatitis A dosis
  única.
- **18 meses:** Hexavalente refuerzo; Varicela 1ª dosis; Meningocócica B refuerzo; SRP 2ª dosis.
- **36 meses:** Varicela 2ª dosis.
- **1° básico:** dTpa (difteria, tétanos, tos convulsiva acelular) refuerzo.
- **4° básico:** dTpa refuerzo.
- **5° básico:** VPH **dosis única**.
- **8° básico:** Neumocócica polisacárida 23 valente, dosis única.
- **Gestantes:** dTpa **desde la semana 28 de gestación**.
- **≥60 años:** dTpa; **≥65 años:** Neumocócica polisacárida 23 valente.
- **Fiebre amarilla:** dosis única, **solo en Rapa Nui**.
- Campañas según grupos objetivos de MINSAL: influenza, COVID-19, VRS (anticuerpo monoclonal para
  nacidos desde el 01-10-2025 y lactantes de riesgo), MPOX (dos dosis en personas de alto riesgo).
- Fuente: MINSAL, Calendario de Inmunizaciones 2026.
  <https://saludresponde.minsal.cl/wp-content/uploads/2025/08/CALENDARIO-INMUNIZACIONES-2026.pdf>

## Emergencias: números y protocolos (capítulo 13)

- **131** SAMU · **132** Bomberos · **133** Carabineros · **134** PDI · **137** emergencias
  marítimas (DIRECTEMAR) · **130** CONAF (incendios forestales).
- **600 360 7777** Salud Responde (MINSAL, 24 horas). ***4141** línea de prevención del suicidio
  (MINSAL, gratuita y confidencial). **1412** SENDA. **+56 22 635 3800** CITUC (intoxicaciones).
- **Sismo:** el protocolo depende del tipo de construcción. En construcción no sismo resistente
  (adobe, autoconstrucción) **no hay lugares seguros adentro: se evacúa durante el sismo**. En
  construcción sismo resistente: protegerse y afirmarse debajo de un elemento firme o junto a él.
- **Tsunami:** la evacuación es **autónoma**: si el sismo impide mantenerse en pie, se evacúa de
  inmediato a terreno elevado sin esperar aviso oficial. Si el mar se retira y expone el fondo
  marino, también se evacúa. Evacuación horizontal primero; la vertical (edificios de 8 pisos o
  más, subiendo lo más alto posible) es **segunda alternativa**. No cruzar esteros ni ríos.
- Fuentes: SENAPRED <https://www.senapred.cl/sismos/> y <https://www.senapred.cl/tsunami/> ;
  DIRECTEMAR para el 137; MINSAL para el 131 y Salud Responde.

## Dato que corrigió un error nuestro

- **No existe una "Ley 21.133" sobre drones.** La Ley 21.133 trata de la incorporación de
  trabajadores independientes a los regímenes de protección social. La materia de aeronaves
  pilotadas a distancia está en la **Norma Aeronáutica DAN 151** de la DGAC (y DAN 91 para áreas
  no pobladas): registro obligatorio del RPA en la DGAC antes de operar
  (<https://www.dgac.gob.cl/como-operar-un-dron-en-chile/>).
- **No existe una "Ley 21.591" sobre apuestas en línea.** La Ley 21.591 es de royalty a la
  minería. Al cierre de la guía, la ley de plataformas de apuestas en línea seguía en tramitación
  en el Congreso; lo aplicable es la Ley 19.995 y el Código Penal.

Estos dos son el ejemplo de por qué existe el contrato: un número de ley inventado o mal recordado
produce un ítem que parece impecable y es falso. Si te encuentras con un dato así, **no lo
arregles a mano: búscalo en LeyChile**.

## Herramientas que funcionan

- `python3 tools/leychile.py meta idLey=21561` — metadatos oficiales de una norma (título, fecha de
  publicación, inicio de vigencia, URL).
- `python3 tools/leychile.py art idNorma=207436 22` — el texto de un artículo del Código del
  Trabajo.
- `python3 tools/leychile.py grep idLey=19496 "garantía"` — busca dentro del texto ya cacheado.
- El buscador temático de LeyChile y el SPARQL de datos.bcn.cl **no sirven** hoy para buscar por
  materia: hay que ir con el `idLey`/`idNorma` conocido.
