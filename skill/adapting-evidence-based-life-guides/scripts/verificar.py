#!/usr/bin/env python3
"""Validator for a cost/benefit life guide.

Adapt the CONFIG block below to your country's field names and cost-tag vocabulary, then run it
against your chapter directory. Everything else is country-independent.

    python3 verificar.py                # structure, tags, fields, grades, counts
    python3 verificar.py --urls         # also probe every cited link
    python3 verificar.py --json         # machine-readable audit (for CI)

Exit code 0 = no errors, 1 = errors found. Warnings do not fail the run.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
from collections import Counter

# ─────────────────────────── CONFIG: edit for your guide ───────────────────────────
RAIZ = pathlib.Path(__file__).resolve().parent.parent
GUIA = RAIZ / "guia"                     # directory holding the chapter markdown
README = RAIZ / "README.md"
LOG_DIR = RAIZ / "docs" / "verificacion" # verification log, one file per chapter

# Mandatory fields, in required order. Localize the labels, keep the count.
CAMPOS = ["Costo", "En simple", "Beneficio", "Evidencia", "Fuentes"]
CAMPOS_OPCIONALES = ["Notas"]

# Cost-tag vocabulary. Keep exactly five keys, in this order; localize the values if you wish.
PLATA = {"0", "poco", "mucho"}
TIEMPO = {"poco", "medio", "mucho"}
AGUANTE = {"no", "algo", "si"}
BENEFICIO = {"alto", "medio", "bajo"}
MEDIDA = {"muerte", "plata", "tiempo", "libertad"}

# Marker used for a datum you could not verify against its source. Never invent a value instead.
# Keep it a fixed token so scripts can find it; localize the wording if you like.
MARCA = "VERIFY"

# Words that must not appear in the plain-language field: the reader there is not a statistician.
# Matched as word-boundary regexes. A bare substring search for "or:" fires on "mayor:",
# "menor:", "superior:" — the checker then cries wolf and gets ignored, which defeats it.
PROHIBIDAS_SIMPLE = [
    r"\bRR\b", r"\bHR\b", r"\bOR\b", r"\bIC\b", r"\bCI\b",
    r"IC\s*95", r"IC95", r"CI\s*95", r"CI95",
    r"\bcohorte\b", r"\bcohort\b", r"\bmetaan[aá]lisis\b", r"\bmeta-analysis\b", r"\bmeta analysis\b",
    r"\bensayo cl[ií]nico\b", r"\brandomi[sz]ed trial\b",
    r"\bodds ratio\b", r"\bhazard ratio\b",
    r"\bintervalo de confianza\b", r"\bconfidence interval\b",
    r"\bestad[ií]sticamente significativ[oa]\b", r"\bstatistically significant\b",
    r"\bp\s*[<=>]\s*0?[.,]\d",
]
PALABRAS_MARKETING = [
    "poderoso", "revolucionario", "increíble", "definitivo", "garantizado",
    "secreto", "milagroso", "impactante", "imprescindible", "powerful",
    "revolutionary", "amazing", "definitive", "guaranteed",
]

# Minimum evidence grade for which a primary/official source is required.
FUENTE_MINIMA_PARA_A = True
# ───────────────────────────────────────────────────────────────────────────────────

RE_ITEM = re.compile(r"^### (\d+)\.\s+(.+)$")
RE_TAG = re.compile(
    r"^<!--\s*costos:\s*"
    r"plata=(\S+)\s+tiempo=(\S+)\s+aguante=(\S+)\s+beneficio=(\S+)\s+medida=(\S+)"
    r"\s*-->\s*$"
)
RE_CAMPO = re.compile(r"^-\s*([A-Za-zÁÉÍÓÚáéíóúñÑ ]+):\s*(.*)$")
RE_URL = re.compile(r"https?://[^\s<>)\]]+")
RE_BLOQUEANTE = re.compile(r"^## ")


class Hallazgo:
    __slots__ = ("nivel", "archivo", "linea", "mensaje")

    def __init__(self, nivel: str, archivo: str, linea: int, mensaje: str):
        self.nivel, self.archivo, self.linea, self.mensaje = nivel, archivo, linea, mensaje

    def __str__(self) -> str:
        return f"{self.archivo}:{self.linea}: [{self.nivel}] {self.mensaje}"

    def as_dict(self) -> dict:
        return {"nivel": self.nivel, "archivo": self.archivo, "linea": self.linea, "mensaje": self.mensaje}


def numeros(texto: str) -> set[str]:
    return {n.replace(",", ".") for n in re.findall(r"\d+(?:[.,]\d+)?", texto)}


def revisar_capitulo(ruta: pathlib.Path) -> tuple[list[Hallazgo], list[dict]]:
    h: list[Hallazgo] = []
    items: list[dict] = []
    nombre = ruta.name
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    if not lineas:
        return [Hallazgo("ERROR", nombre, 1, "archivo vacio")], items
    if not lineas[0].startswith("# "):
        h.append(Hallazgo("ERROR", nombre, 1, "falta el titulo '# N. Titulo' en la linea 1"))

    i, esperado = 0, 1
    while i < len(lineas):
        m = RE_ITEM.match(lineas[i])
        if not m:
            i += 1
            continue
        numero, titulo = int(m.group(1)), m.group(2).strip()
        inicio = i + 1
        j = inicio
        cuerpo: list[str] = []
        while j < len(lineas) and not RE_ITEM.match(lineas[j]) and not RE_BLOQUEANTE.match(lineas[j]):
            cuerpo.append(lineas[j])
            j += 1

        item = {"numero": numero, "titulo": titulo, "archivo": nombre, "linea": i + 1}
        if numero != esperado:
            h.append(Hallazgo("ERROR", nombre, i + 1, f"numeracion: se esperaba {esperado}, llego {numero}"))
        esperado = numero + 1

        primera = next((l for l in cuerpo if l.strip()), "")
        mt = RE_TAG.match(primera.strip())
        if not mt:
            h.append(Hallazgo("ERROR", nombre, i + 2, f"falta o esta mal la etiqueta de costos (item {numero})"))
        else:
            vals = [g.lower() for g in mt.groups()]
            for valor, permitidos, campo in zip(
                vals, (PLATA, TIEMPO, AGUANTE, BENEFICIO, MEDIDA), ("plata", "tiempo", "aguante", "beneficio", "medida")
            ):
                if valor not in permitidos:
                    h.append(
                        Hallazgo("ERROR", nombre, i + 2, f"etiqueta (item {numero}): {campo}={valor} fuera de {sorted(permitidos)}")
                    )
            item.update(dict(zip(("plata", "tiempo", "aguante", "beneficio_nivel", "medida"), vals)))

        vistos: list[str] = []
        valores: dict[str, str] = {}
        for k, linea in enumerate(cuerpo):
            mc = RE_CAMPO.match(linea.strip())
            if not mc:
                continue
            campo, valor = mc.group(1).strip(), mc.group(2).strip()
            if campo not in CAMPOS + CAMPOS_OPCIONALES:
                h.append(Hallazgo("ERROR", nombre, inicio + k + 1, f"campo desconocido '- {campo}:' (item {numero})"))
                continue
            vistos.append(campo)
            valores[campo] = valor

        for campo in CAMPOS:
            if campo not in vistos:
                h.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: falta el campo '- {campo}:'"))
            elif not valores[campo]:
                h.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: '- {campo}:' esta vacio"))

        orden = [c for c in vistos if c in CAMPOS]
        if orden and orden != CAMPOS[: len(orden)]:
            h.append(Hallazgo("AVISO", nombre, i + 1, f"item {numero}: campos fuera de orden ({', '.join(orden)})"))

        ev = valores.get("Evidencia", "")
        if ev:
            base = ev.split("(")[0].strip().upper()
            if base not in {"A", "B", "C"}:
                h.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: evidencia '{ev}' no es A, B ni C"))
            if ("disputa" in ev.lower() or "disputed" in ev.lower()) and not valores.get("Notas"):
                h.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: evidencia en disputa sin contra-evidencia en Notas"))

        fuentes = valores.get("Fuentes", "")
        urls = RE_URL.findall(fuentes)
        if fuentes and not urls:
            h.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: '- Fuentes:' sin URL verificable"))
        if fuentes.strip().lower() in {"-", "n/a", "pendiente", "por definir", "todo"}:
            h.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: fuentes de relleno"))

        simple = valores.get("En simple", "")
        bajo = simple.lower()
        for patron in PROHIBIDAS_SIMPLE:
            m = re.search(patron, simple, re.I)
            if m:
                h.append(
                    Hallazgo("ERROR", nombre, i + 1, f"item {numero}: 'En simple' usa estadistica cruda ('{m.group(0)}')")
                )
        for palabra in PALABRAS_MARKETING:
            if palabra.lower() in bajo:
                h.append(Hallazgo("AVISO", nombre, i + 1, f"item {numero}: 'En simple' usa lenguaje de marketing ('{palabra}')"))
        nuevos = numeros(simple) - numeros(valores.get("Beneficio", "")) - numeros(valores.get("Costo", ""))
        if nuevos:
            h.append(
                Hallazgo("ERROR", nombre, i + 1, f"item {numero}: 'En simple' introduce numeros sin fuente: {sorted(nuevos)}")
            )

        if len(cuerpo) > 20:
            h.append(Hallazgo("AVISO", nombre, i + 1, f"item {numero}: {len(cuerpo)} lineas de cuerpo"))

        item.update(valores)
        item["urls"] = urls
        item["pendientes"] = len(re.findall(MARCA, " ".join(cuerpo)))
        items.append(item)
        i = j

    if not items:
        h.append(Hallazgo("ERROR", nombre, 1, "el capitulo no tiene ningun item"))

    if any(re.search(MARCA, l) for l in lineas):
        registro = LOG_DIR / f"{ruta.stem}.md"
        if not registro.exists():
            h.append(
                Hallazgo("ERROR", nombre, 1, f"hay marcas {MARCA} pero falta el registro {LOG_DIR.name}/{ruta.stem}.md")
            )
    return h, items


def revisar_readme(total: int, niveles: Counter) -> list[Hallazgo]:
    h: list[Hallazgo] = []
    if not README.exists():
        return [Hallazgo("ERROR", "README.md", 1, "no existe README.md")]
    texto = README.read_text(encoding="utf-8")
    if total and str(total) not in texto:
        h.append(Hallazgo("ERROR", "README.md", 1, f"el README no menciona el total de items ({total})"))
    for nivel in ("A", "B", "C"):
        if niveles[nivel] and not re.search(rf"\b{niveles[nivel]}\b", texto):
            h.append(Hallazgo("AVISO", "README.md", 1, f"el README no menciona los items de grado {nivel} ({niveles[nivel]})"))
    return h


def probar_urls(items: list[dict], limite: int = 500) -> list[Hallazgo]:
    h: list[Hallazgo] = []
    vistas: dict[str, tuple[str, int, int]] = {}
    for it in items:
        for url in it["urls"]:
            vistas.setdefault(url, (it["archivo"], it["linea"], it["numero"]))
    if len(vistas) > limite:
        h.append(Hallazgo("AVISO", "—", 0, f"{len(vistas) - limite} URLs sin probar (limite {limite})"))
    for url, (archivo, linea, numero) in sorted(vistas.items())[:limite]:
        try:
            pet = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (guide-url-check)"})
            with urllib.request.urlopen(pet, timeout=15) as resp:
                if resp.status >= 400:
                    h.append(Hallazgo("ERROR", archivo, linea, f"item {numero}: HTTP {resp.status} en {url}"))
        except urllib.error.HTTPError as e:
            h.append(
                Hallazgo("AVISO" if e.code in (403, 429, 503) else "ERROR", archivo, linea, f"item {numero}: HTTP {e.code} en {url}")
            )
        except Exception as e:  # noqa: BLE001
            h.append(Hallazgo("AVISO", archivo, linea, f"item {numero}: no se pudo abrir {url} ({type(e).__name__})"))
    return h


def main() -> int:
    ap = argparse.ArgumentParser(description="Valida la estructura y la integridad de la guia.")
    ap.add_argument("--urls", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not GUIA.exists():
        print(f"ERROR: no existe {GUIA}", file=sys.stderr)
        return 1

    todos: list[Hallazgo] = []
    items: list[dict] = []
    for ruta in sorted(GUIA.glob("*.md")):
        hallazgos, suyos = revisar_capitulo(ruta)
        todos.extend(hallazgos)
        items.extend(suyos)

    niveles = Counter((i.get("Evidencia", "?").split("(")[0].strip().upper() or "?") for i in items)
    medidas = Counter(i.get("medida", "?") for i in items)
    todos.extend(revisar_readme(len(items), niveles))
    if args.urls:
        todos.extend(probar_urls(items))

    errores = [x for x in todos if x.nivel == "ERROR"]
    avisos = [x for x in todos if x.nivel == "AVISO"]

    if args.json:
        print(
            json.dumps(
                {
                    "capitulos": len(list(GUIA.glob("*.md"))),
                    "items": len(items),
                    "evidencia": dict(niveles),
                    "medidas": dict(medidas),
                    "errores": [x.as_dict() for x in errores],
                    "avisos": [x.as_dict() for x in avisos],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1 if errores else 0

    print(f"Capitulos: {len(list(GUIA.glob('*.md')))}   Items: {len(items)}")
    print("Evidencia: " + ", ".join(f"{k}={v}" for k, v in sorted(niveles.items())))
    print("Medidas:   " + ", ".join(f"{k}={v}" for k, v in sorted(medidas.items())))
    pend = sum(i["pendientes"] for i in items)
    if pend:
        print(f"Datos marcados {MARCA}: {pend} (revisar {LOG_DIR.name}/)")
    print()
    for x in errores + avisos:
        print(f"  {x}")
    print()
    if errores:
        print(f"FALLA: {len(errores)} errores, {len(avisos)} avisos.")
        return 1
    print(f"OK: sin errores, {len(avisos)} avisos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
