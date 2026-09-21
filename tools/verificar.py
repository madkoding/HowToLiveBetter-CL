#!/usr/bin/env python3
"""Verificador de HowToLiveBetter-CL.

Revisa que cada capitulo de guia/ cumpla el contrato de ADAPTACION.md:
formato de item, etiqueta de costos, campos obligatorios, grados de evidencia,
fuentes con URL, y que "En simple" no meta estadistica cruda.

Uso:
    python3 tools/verificar.py              # formato + conteos
    python3 tools/verificar.py --urls       # ademas prueba que los enlaces respondan
    python3 tools/verificar.py --json       # salida para maquinas

Sale con codigo 0 si no hay errores, 1 si hay.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parent.parent
GUIA = RAIZ / "guia"
README = RAIZ / "README.md"

CAMPOS = ["Costo", "En simple", "Beneficio", "Evidencia", "Fuentes"]
CAMPOS_OPCIONALES = ["Notas"]

PLATA = {"0", "poco", "mucho"}
TIEMPO = {"poco", "medio", "mucho"}
AGUANTE = {"no", "algo", "si"}
BENEFICIO = {"alto", "medio", "bajo"}
MEDIDA = {"muerte", "plata", "tiempo", "libertad"}

RE_ITEM = re.compile(r"^### (\d+)\.\s+(.+)$")
RE_TAG = re.compile(
    r"^<!--\s*costos:\s*"
    r"plata=(\S+)\s+tiempo=(\S+)\s+aguante=(\S+)\s+beneficio=(\S+)\s+medida=(\S+)"
    r"\s*-->\s*$"
)
RE_CAMPO = re.compile(r"^-\s*([A-Za-zÁÉÍÓÚáéíóúñ ]+):\s*(.*)$")
RE_URL = re.compile(r"https?://[^\s<>\"']+?(?=[\s<>\"']|$)")
RE_MARCA = re.compile(r"POR VERIFICAR")

# Sitios oficiales que bloquean la verificacion automatica (403, TLS o DNS). No son enlaces
# muertos: abren normal en un navegador. Se reportan como aviso, nunca como error.
HOSTS_BLOQUEAN_BOTS = {
    "www.fonasa.gob.cl", "fonasa.gob.cl", "nuevo.fonasa.gob.cl",
    "www.shoa.cl", "shoa.cl",
    "www.sernageomin.cl", "sernageomin.cl", "rnvv.sernageomin.cl",
    "repositoriodeis.minsal.cl", "deis.minsal.cl",
    "www.conaset.cl", "conaset.cl",
    "www.leychile.cl", "www.bcn.cl",
    "www.dt.gob.cl", "dt.gob.cl",
    "www.suseso.gob.cl", "www.spensiones.cl",
    "www.ine.gob.cl", "www.afc.cl",
    "www.sml.gob.cl", "sml.gob.cl",
    "www.ispch.gob.cl", "www.anci.gob.cl",
    "www.pdichile.cl", "www.superintendenciadeeducacion.gob.cl",
}  # fmt: skip

# Palabras que no pueden aparecer en "En simple": el lector de esa linea no es estadistico.
# Se comparan con limites de palabra (regex \b): si se busca la subcadena "or:" pelada, aparece
# dentro de "mayor:", "menor:", "superior:", "peor:" y da falsos positivos.
PROHIBIDAS_SIMPLE = [
    r"\bRR\b", r"\bHR\b", r"\bOR\b", r"\bIC\b", r"\bCI\b",
    r"IC\s*95", r"IC95",
    r"\bcohorte\b", r"\bcohort\b", r"\bmetaan[aá]lisis\b", r"\bmeta-analysis\b", r"\bmeta analysis\b",
    r"\bensayo cl[ií]nico\b", r"\brandomi[sz]ed trial\b",
    r"\bodds ratio\b", r"\bhazard ratio\b",
    r"\bintervalo de confianza\b", r"\bconfidence interval\b",
    r"\bestad[ií]sticamente significativ[oa]\b", r"\bstatistically significant\b",
    r"\bp\s*[<=>]\s*0?[.,]\d",
]
PALABRAS_MARKETING = [
    "poderoso", "revolucionario", "increíble", "definitivo", "garantizado",
    "secreto", "milagroso", "impactante", "imprescindible",
]


class Hallazgo:
    __slots__ = ("nivel", "archivo", "linea", "mensaje")

    def __init__(self, nivel: str, archivo: str, linea: int, mensaje: str):
        self.nivel = nivel
        self.archivo = archivo
        self.linea = linea
        self.mensaje = mensaje

    def __str__(self) -> str:
        return f"{self.archivo}:{self.linea}: [{self.nivel}] {self.mensaje}"

    def as_dict(self) -> dict:
        return {
            "nivel": self.nivel,
            "archivo": self.archivo,
            "linea": self.linea,
            "mensaje": self.mensaje,
        }


def capitulos() -> list[pathlib.Path]:
    return sorted(GUIA.glob("*.md"))


def revisar_capitulo(ruta: pathlib.Path) -> tuple[list[Hallazgo], list[dict]]:
    hallazgos: list[Hallazgo] = []
    items: list[dict] = []
    nombre = ruta.name
    lineas = ruta.read_text(encoding="utf-8").splitlines()

    if not lineas:
        hallazgos.append(Hallazgo("ERROR", nombre, 1, "archivo vacio"))
        return hallazgos, items

    # Encabezado: "# N. Titulo" y una nota de posicion en la guia.
    if not lineas[0].startswith("# "):
        hallazgos.append(Hallazgo("ERROR", nombre, 1, "falta el titulo '# N. Titulo' en la linea 1"))
    if any(l.startswith("> Adaptado de") for l in lineas[:8]):
        pass  # nota de procedencia, opcional

    # Recorremos por bloques de item.
    i = 0
    esperado = 1
    while i < len(lineas):
        m = RE_ITEM.match(lineas[i])
        if not m:
            i += 1
            continue

        numero, titulo = int(m.group(1)), m.group(2).strip()
        inicio = i + 1
        j = inicio
        cuerpo: list[str] = []
        while j < len(lineas) and not RE_ITEM.match(lineas[j]) and not lineas[j].startswith("## "):
            cuerpo.append(lineas[j])
            j += 1

        item = {
            "numero": numero,
            "titulo": titulo,
            "archivo": nombre,
            "linea": i + 1,
        }

        if numero != esperado:
            hallazgos.append(
                Hallazgo("ERROR", nombre, i + 1, f"numeracion: se esperaba {esperado}, llego {numero}")
            )
        esperado = numero + 1

        # Etiqueta de costos.
        primera = next((l for l in cuerpo if l.strip()), "")
        mt = RE_TAG.match(primera.strip())
        if not mt:
            hallazgos.append(
                Hallazgo("ERROR", nombre, i + 2, f"falta o esta mal la etiqueta '<!-- costos: ... -->' (item {numero})")
            )
        else:
            plata, tiempo, aguante, beneficio, medida = (g.lower() for g in mt.groups())
            for valor, permitidos, campo in (
                (plata, PLATA, "plata"),
                (tiempo, TIEMPO, "tiempo"),
                (aguante, AGUANTE, "aguante"),
                (beneficio, BENEFICIO, "beneficio"),
                (medida, MEDIDA, "medida"),
            ):
                if valor not in permitidos:
                    hallazgos.append(
                        Hallazgo(
                            "ERROR",
                            nombre,
                            i + 2,
                            f"etiqueta costos (item {numero}): {campo}={valor} no permitido; usa {sorted(permitidos)}",
                        )
                    )
            item.update(
                {
                    "plata": plata,
                    "tiempo": tiempo,
                    "aguante": aguante,
                    "beneficio_nivel": beneficio,
                    "medida": medida,
                }
            )

        # Campos obligatorios y su orden.
        campos_vistos: list[str] = []
        valores: dict[str, str] = {}
        for k, linea in enumerate(cuerpo):
            mc = RE_CAMPO.match(linea.strip())
            if not mc:
                continue
            campo, valor = mc.group(1).strip(), mc.group(2).strip()
            if campo not in CAMPOS + CAMPOS_OPCIONALES:
                hallazgos.append(
                    Hallazgo("ERROR", nombre, inicio + k + 1, f"campo desconocido '- {campo}:' (item {numero})")
                )
                continue
            campos_vistos.append(campo)
            valores[campo] = valor

        for campo in CAMPOS:
            if campo not in campos_vistos:
                hallazgos.append(
                    Hallazgo("ERROR", nombre, i + 1, f"item {numero}: falta el campo '- {campo}:'")
                )

        orden = [c for c in campos_vistos if c in CAMPOS]
        if orden and orden != CAMPOS[: len(orden)] and orden != CAMPOS:
            hallazgos.append(
                Hallazgo(
                    "AVISO",
                    nombre,
                    i + 1,
                    f"item {numero}: los campos no siguen el orden del contrato ({', '.join(orden)})",
                )
            )

        for campo in CAMPOS:
            if campo in valores and not valores[campo]:
                hallazgos.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: '- {campo}:' esta vacio"))

        # Evidencia.
        ev = valores.get("Evidencia", "")
        if ev:
            base = ev.split("(")[0].strip().upper()
            if base not in {"A", "B", "C"}:
                hallazgos.append(
                    Hallazgo("ERROR", nombre, i + 1, f"item {numero}: evidencia '{ev}' no es A, B o C")
                )
            if "disputa" in ev.lower() and "Notas" not in valores:
                hallazgos.append(
                    Hallazgo(
                        "ERROR",
                        nombre,
                        i + 1,
                        f"item {numero}: marca evidencia en disputa pero no trae '- Notas:' con la evidencia contraria",
                    )
                )

        # Fuentes: al menos una URL y sin dominios vetados.
        fuentes = valores.get("Fuentes", "")
        urls = RE_URL.findall(fuentes)
        if not urls and fuentes:
            hallazgos.append(
                Hallazgo("ERROR", nombre, i + 1, f"item {numero}: '- Fuentes:' sin ninguna URL verificable")
            )
        if fuentes.strip().lower() in {"-", "n/a", "pendiente", "por definir"}:
            hallazgos.append(Hallazgo("ERROR", nombre, i + 1, f"item {numero}: fuentes vacias de mentira"))

        # "En simple": sin estadistica cruda ni marketing.
        simple = valores.get("En simple", "")
        for patron in PROHIBIDAS_SIMPLE:
            m = re.search(patron, simple, re.I)
            if m:
                hallazgos.append(
                    Hallazgo(
                        "ERROR",
                        nombre,
                        i + 1,
                        f"item {numero}: 'En simple' usa estadistica cruda ('{m.group(0)}'); traduce a lenguaje comun",
                    )
                )
        for palabra in PALABRAS_MARKETING:
            if palabra in simple.lower():
                hallazgos.append(
                    Hallazgo("AVISO", nombre, i + 1, f"item {numero}: 'En simple' usa lenguaje de marketing ('{palabra}')")
                )
        # Un numero que no este en Beneficio no deberia aparecer en En simple.
        def numeros(texto: str) -> set[str]:
            return {n.replace(",", ".") for n in re.findall(r"\d+(?:[.,]\d+)?", texto)}

        nuevos = numeros(simple) - numeros(valores.get("Beneficio", "")) - numeros(valores.get("Costo", ""))
        if nuevos:
            hallazgos.append(
                Hallazgo(
                    "ERROR",
                    nombre,
                    i + 1,
                    f"item {numero}: 'En simple' introduce numeros que no estan en Beneficio/Costo: {sorted(nuevos)}",
                )
            )

        # Largo del item.
        if len(cuerpo) > 20:
            hallazgos.append(
                Hallazgo("AVISO", nombre, i + 1, f"item {numero}: {len(cuerpo)} lineas de cuerpo (el contrato pide <= 10)")
            )

        item.update(valores)
        item["urls"] = urls
        item["sin_verificar"] = sorted(set(RE_MARCA.findall(" ".join(cuerpo))))
        items.append(item)
        i = j

    if not items:
        hallazgos.append(Hallazgo("ERROR", nombre, 1, "el capitulo no tiene ningun item '### N. ...'"))

    # Todo dato marcado como pendiente tiene que quedar registrado aparte.
    pendientes = [
        (n, l)
        for n, l in enumerate(lineas, 1)
        if RE_MARCA.search(l)
    ]
    if pendientes:
        registro = RAIZ / "docs" / "verificacion" / f"{ruta.stem}.md"
        if not registro.exists():
            hallazgos.append(
                Hallazgo(
                    "ERROR",
                    nombre,
                    pendientes[0][0],
                    f"hay {len(pendientes)} marcas POR VERIFICAR pero falta docs/verificacion/{ruta.stem}.md",
                )
            )

    return hallazgos, items


def revisar_readme(total: int, niveles: Counter) -> list[Hallazgo]:
    hallazgos: list[Hallazgo] = []
    if not README.exists():
        return [Hallazgo("ERROR", "README.md", 1, "no existe README.md")]

    texto = README.read_text(encoding="utf-8")
    numeros = {int(n) for n in re.findall(r"\b(\d{2,4})\b", texto)}
    if total and total not in numeros:
        hallazgos.append(
            Hallazgo(
                "ERROR",
                "README.md",
                1,
                f"el README no menciona el total de items ({total}). Debe aparecer y calzar con guia/.",
            )
        )

    for nivel in ("A", "B", "C"):
        if niveles[nivel] and re.search(rf"\b{niveles[nivel]}\b", texto) is None:
            hallazgos.append(
                Hallazgo("AVISO", "README.md", 1, f"el README no menciona el conteo de grado {nivel} ({niveles[nivel]})")
            )
    return hallazgos


def probar_urls(items: list[dict], limite: int = 400) -> list[Hallazgo]:
    hallazgos: list[Hallazgo] = []
    vistas: dict[str, tuple[str, int, int]] = {}
    for item in items:
        for url in item["urls"]:
            vistas.setdefault(url, (item["archivo"], item["linea"], item["numero"]))
    por_url = {url: item for item in items for url in item["urls"]}

    for n, (url, (archivo, linea, numero)) in enumerate(sorted(vistas.items())):
        if n >= limite:
            hallazgos.append(
                Hallazgo("AVISO", "—", 0, f"quedan {len(vistas) - limite} URLs sin probar (limite {limite})")
            )
            break
        # Los DOI se verifican contra Crossref: responde 200 si el DOI existe, y ademas
        # permite confirmar que el titulo real coincide con el citado.
        if "doi.org/" in url:
            doi = url.split("doi.org/", 1)[1].strip()
            try:
                pet = urllib.request.Request(
                    f"https://api.crossref.org/works/{urllib.parse.quote(doi)}",
                    headers={"User-Agent": "verificador-guia/1.0 (mailto:madkoding@gmail.com)"},
                )
                with urllib.request.urlopen(pet, timeout=25) as resp:
                    registro = json.load(resp)["message"]
                titulo = (registro.get("title") or ["?"])[0]
                anio = ((registro.get("issued", {}).get("date-parts") or [[None]])[0] or [None])[0]
                dueno = por_url[url]
                dueno["_doi_titulo"] = dueno.get("_doi_titulo", {})
                dueno["_doi_titulo"][doi] = {"titulo": titulo, "anio": anio}
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    hallazgos.append(
                        Hallazgo("ERROR", archivo, linea, f"item {numero}: el DOI no existe en Crossref (404): {doi}")
                    )
                else:
                    hallazgos.append(Hallazgo("AVISO", archivo, linea, f"item {numero}: Crossref respondio {e.code} para {doi}"))
            except Exception as e:  # noqa: BLE001
                hallazgos.append(Hallazgo("AVISO", archivo, linea, f"item {numero}: no se pudo verificar {doi} ({type(e).__name__})"))
            continue

        try:
            pet = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 (verificador HTLB-CL)"})
            with urllib.request.urlopen(pet, timeout=15) as resp:
                if resp.status >= 400:
                    hallazgos.append(
                        Hallazgo("ERROR", archivo, linea, f"item {numero}: la URL responde {resp.status}: {url}")
                    )
        except urllib.error.HTTPError as e:
            nivel = "AVISO" if e.code in (403, 429, 503) else "ERROR"
            hallazgos.append(Hallazgo(nivel, archivo, linea, f"item {numero}: HTTP {e.code} en {url}"))
        except Exception as e:  # noqa: BLE001 - red: cualquier fallo se reporta tal cual
            # Muchos sitios .gob.cl bloquean la consulta automatica o fallan por certificado,
            # pero abren en un navegador: no se reportan como error.
            host = urllib.parse.urlsplit(url).netloc.lower()
            nivel = "AVISO" if host in HOSTS_BLOQUEAN_BOTS else "ERROR"
            hallazgos.append(
                Hallazgo(nivel, archivo, linea, f"item {numero}: no se pudo abrir {url} ({type(e).__name__})")
            )
    return hallazgos


def main() -> int:
    ap = argparse.ArgumentParser(description="Verifica el formato y la integridad de la guia.")
    ap.add_argument("--urls", action="store_true", help="prueba que cada enlace responda")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    args = ap.parse_args()

    if not GUIA.exists():
        print(f"ERROR: no existe {GUIA}", file=sys.stderr)
        return 1

    todos: list[Hallazgo] = []
    items: list[dict] = []
    for ruta in capitulos():
        hallazgos, suyos = revisar_capitulo(ruta)
        todos.extend(hallazgos)
        items.extend(suyos)

    niveles = Counter((i.get("Evidencia", "?").split("(")[0].strip().upper() or "?") for i in items)
    medidas = Counter(i.get("medida", "?") for i in items)
    todos.extend(revisar_readme(len(items), niveles))

    if args.urls:
        todos.extend(probar_urls(items))

    errores = [h for h in todos if h.nivel == "ERROR"]
    avisos = [h for h in todos if h.nivel == "AVISO"]

    if args.json:
        print(
            json.dumps(
                {
                    "capitulos": len(capitulos()),
                    "items": len(items),
                    "evidencia": dict(niveles),
                    "medidas": dict(medidas),
                    "errores": [h.as_dict() for h in errores],
                    "avisos": [h.as_dict() for h in avisos],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1 if errores else 0

    print(f"Capitulos: {len(capitulos())}   Items: {len(items)}")
    print("Evidencia: " + ", ".join(f"{k}={v}" for k, v in sorted(niveles.items())))
    print("Medidas:   " + ", ".join(f"{k}={v}" for k, v in sorted(medidas.items())))
    pendientes = sum(len(i["sin_verificar"]) for i in items)
    if pendientes:
        print(f"Datos marcados POR VERIFICAR: {pendientes} (revisar docs/verificacion/)")
    print()

    for h in errores:
        print(f"  {h}")
    for h in avisos:
        print(f"  {h}")

    print()
    if errores:
        print(f"FALLA: {len(errores)} errores, {len(avisos)} avisos.")
        return 1
    print(f"OK: sin errores, {len(avisos)} avisos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
