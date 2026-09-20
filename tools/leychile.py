#!/usr/bin/env python3
"""Descarga el texto oficial de una norma desde LeyChile (BCN) y lo cachea en texto plano.

Fuente: https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=<id>
(mismo endpoint que consume el visor https://www.bcn.cl/leychile/navegar?idNorma=<id>)

Uso:
    python3 tools/leychile.py meta 1984               # metadatos + URL
    python3 tools/leychile.py fetch 1984              # baja y cachea
    python3 tools/leychile.py art 1984 446            # imprime el articulo 446 completo
    python3 tools/leychile.py art 21.663 1            # en una ley, el articulo 1
    python3 tools/leychile.py grep 1984 "hurto"       # busca en el texto cacheado
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.request

BASE = "https://nuevo.leychile.cl/servicios"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache", "leychile")
UA = "Mozilla/5.0 (X11; Linux x86_64) Hermes-Agent/leychile-fetch"
TAG = re.compile(r"<[^>]+>")


def _cache_path(id_norma: int) -> str:
    return os.path.join(CACHE, f"{id_norma}.json")


def fetch(id_norma: int, force: bool = False) -> dict:
    os.makedirs(CACHE, exist_ok=True)
    jpath = _cache_path(id_norma)
    if os.path.exists(jpath) and not force:
        with open(jpath, encoding="utf-8") as fh:
            return json.load(fh)
    url = f"{BASE}/Navegar/get_norma_json?idNorma={id_norma}&agrupa_partes=1"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept": "application/json",
                 "Referer": "https://www.bcn.cl/leychile/"},
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        raw = resp.read().decode("utf-8", "replace")
    data = json.loads(raw)
    with open(jpath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)
    return data


def _clean(h: str) -> str:
    # las referencias a leyes modificatorias vienen en <span class="n">; no son texto del articulo
    h = re.sub(r'<span class="n".*?</span>', '', h, flags=re.S)
    h = re.sub(r"<(br|/div|/p)\s*/?>", "\n", h)
    h = TAG.sub("", h)
    h = html.unescape(h)
    h = h.replace("\xa0", " ")
    lines = []
    for line in h.split("\n"):
        line = re.sub(r"[ \t]+", " ", line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def _walk(nodes, out):
    for x in nodes:
        if not isinstance(x, dict):
            continue
        t = x.get("t")
        if isinstance(t, str) and t.strip():
            out.append(_clean(t))
        if x.get("h"):
            _walk(x["h"], out)
    return out


def text_of(id_norma: int, force: bool = False) -> str:
    data = fetch(id_norma, force)
    txt = "\n".join(_walk(data.get("html", []), []))
    with open(os.path.join(CACHE, f"{id_norma}.txt"), "w", encoding="utf-8") as fh:
        fh.write(txt)
    return txt


def metadatos(id_norma: int) -> dict:
    m = fetch(id_norma).get("metadatos", {})
    tipos = m.get("tipos_numeros") or [{}]
    return {
        "idNorma": id_norma,
        "titulo": m.get("titulo_norma"),
        "numero": tipos[0].get("compuesto"),
        "organismo": m.get("organismo"),
        "publicacion": m.get("fecha_publicacion"),
        "inicio_vigencia": (m.get("vigencia") or {}).get("inicio_vigencia"),
        "version": m.get("version"),
        "url": f"https://www.bcn.cl/leychile/navegar?idNorma={id_norma}",
    }


def find_article(txt: str, art: str) -> str:
    """Bloque del articulo pedido: desde su encabezado hasta el proximo encabezado."""
    art = art.strip()
    heads = re.compile(r"^(?:ART[IÍ]CULO|ART\.)\s*([0-9]+(?:\s?(?:BIS|TER|QU[ÁA]TER|QUINQUIES|[A-Z]))?)\s*[\.\-–]?", re.I)
    target = re.compile(r"^(?:ART[IÍ]CULO|ART\.)\s*" + re.escape(art) + r"\s*(?:[\.\-–]|$)", re.I)
    lines = txt.split("\n")
    start = None
    for i, line in enumerate(lines):
        if target.match(line):
            start = i
            break
    if start is None:
        return ""
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if heads.match(lines[j]):
            end = j
            break
    return "\n".join(lines[start:end]).strip()


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    cmd, idn = sys.argv[1], sys.argv[2]
    if cmd in ("fetch", "meta"):
        print(json.dumps(metadatos(int(idn)), ensure_ascii=False, indent=1))
        if cmd == "fetch":
            txt = text_of(int(idn), force="--force" in sys.argv)
            print(f"\n[texto] {len(txt)} caracteres -> {CACHE}/{idn}.txt")
            print(txt[:1500])
    elif cmd == "art":
        txt = text_of(int(idn))
        print(find_article(txt, sys.argv[3]))
    elif cmd == "grep":
        txt = text_of(int(idn))
        for i, line in enumerate(txt.split("\n")):
            if re.search(sys.argv[3], line, re.I):
                print(f"{i}: {line[:500]}")
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
