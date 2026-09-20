#!/usr/bin/env python3
"""Descarga el texto oficial de una norma desde LeyChile (BCN) y lo cachea en texto plano.

Fuente: https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?<ref>&agrupa_partes=1
(el mismo endpoint que consume el visor https://www.bcn.cl/leychile/navegar?idNorma=<id>)
`ref` puede ser `1984` (idNorma) o `idLey=21663` (leyes sin idNorma estable).

Uso:
    python3 tools/leychile.py meta 1984               # metadatos + URL oficial
    python3 tools/leychile.py fetch 1984              # baja y cachea
    python3 tools/leychile.py art 1984 446            # articulo 446 del Codigo Penal
    python3 tools/leychile.py art idLey=21663 8       # articulo 8 de la Ley 21.663
    python3 tools/leychile.py grep 1984 "hurto"       # busca en el texto cacheado
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

BASE = "https://nuevo.leychile.cl/servicios"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache", "leychile")
UA = "Mozilla/5.0 (X11; Linux x86_64) Hermes-Agent/leychile-fetch"
TAG = re.compile(r"<[^>]+>")


def ref_key(ref: str) -> str:
    ref = ref.strip()
    return ref if "=" in ref else f"idNorma={ref}"


def _cache_path(key: str) -> str:
    return os.path.join(CACHE, key.replace("=", "_") + ".json")


def fetch(ref: str, force: bool = False) -> dict:
    key = ref_key(ref)
    os.makedirs(CACHE, exist_ok=True)
    jpath = _cache_path(key)
    if os.path.exists(jpath) and not force:
        with open(jpath, encoding="utf-8") as fh:
            return json.load(fh)
    url = f"{BASE}/Navegar/get_norma_json?{urllib.parse.quote(key, safe='=')}&agrupa_partes=1"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept": "application/json",
                 "Referer": "https://www.bcn.cl/leychile/"},
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        raw = resp.read().decode("utf-8", "replace")
    data = json.loads(raw)
    if isinstance(data, str) or "html" not in data:
        raise RuntimeError(f"respuesta sin texto para {key}: {str(data)[:200]}")
    with open(jpath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)
    return data


def _clean(h: str) -> str:
    # las referencias a leyes modificatorias vienen en <span class="n">; no son texto del articulo
    h = re.sub(r'<span class="n".*?</span>', "", h, flags=re.S)
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


def text_of(ref: str, force: bool = False) -> str:
    key = ref_key(ref)
    data = fetch(ref, force)
    txt = "\n".join(_walk(data.get("html", []), []))
    with open(os.path.join(CACHE, key.replace("=", "_") + ".txt"), "w", encoding="utf-8") as fh:
        fh.write(txt)
    return txt


def metadatos(ref: str) -> dict:
    key = ref_key(ref)
    m = fetch(ref).get("metadatos", {})
    tipos = m.get("tipos_numeros") or [{}]
    url = (f"https://www.bcn.cl/leychile/navegar?idNorma={key.split('=')[1]}"
           if key.startswith("idNorma=") else
           f"https://www.bcn.cl/leychile/navegar?idLey={key.split('=')[1]}")
    return {
        "ref": key,
        "titulo": m.get("titulo_norma"),
        "numero": tipos[0].get("compuesto"),
        "organismo": m.get("organismo"),
        "publicacion": m.get("fecha_publicacion"),
        "inicio_vigencia": (m.get("vigencia") or {}).get("inicio_vigencia"),
        "version": m.get("version"),
        "url": url,
    }


HEAD = re.compile(r"^(?:ART[IÍ]CULO|ART\.?)\s*([0-9]+(?:\s?(?:BIS|TER|QU[ÁA]TER|QUINQUIES|[A-Z]))?)\s*[\.\-–\u00ba\u00b0]?", re.I)


def find_article(txt: str, art: str) -> str:
    """Bloque del articulo pedido: desde su encabezado hasta el proximo encabezado."""
    art = art.strip()
    target = re.compile(r"^(?:ART[IÍ]CULO|ART\.)\s*" + re.escape(art) + r"\s*(?:[\.\-–\u00ba\u00b0]|$)", re.I)
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
        if HEAD.match(lines[j]):
            end = j
            break
    return "\n".join(lines[start:end]).strip()


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    cmd, ref = sys.argv[1], sys.argv[2]
    if cmd in ("fetch", "meta"):
        print(json.dumps(metadatos(ref), ensure_ascii=False, indent=1))
        if cmd == "fetch":
            txt = text_of(ref, force="--force" in sys.argv)
            print(f"\n[texto] {len(txt)} caracteres")
            print(txt[:1500])
    elif cmd == "art":
        print(find_article(text_of(ref), sys.argv[3]))
    elif cmd == "grep":
        for i, line in enumerate(text_of(ref).split("\n")):
            if re.search(sys.argv[3], line, re.I):
                print(f"{i}: {line[:500]}")
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
