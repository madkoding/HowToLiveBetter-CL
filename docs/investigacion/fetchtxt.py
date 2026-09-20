#!/usr/bin/env python3
"""Baja una URL y guarda el texto plano en _cache/. Solo texto, sin dependencias.

Uso:  python3 fetchtxt.py <nombre> <url> [<url> ...]
      python3 fetchtxt.py --batch archivo.txt   (una linea: nombre<TAB>url)
"""
import sys, re, pathlib, urllib.request, html

CASE = pathlib.Path(__file__).resolve().parent / "_cache"
CASE.mkdir(exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def limpiar_html(b: bytes) -> str:
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style|head|noscript|svg)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", t)
    t = re.sub(r"(?is)<t[dh][^>]*>", "\t", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
    return t.strip()


def a_texto_pdf(datos: bytes) -> str:
    import io
    try:
        from pypdf import PdfReader
    except ImportError:
        return "[pypdf no instalado]"
    r = PdfReader(io.BytesIO(datos))
    return "\n".join((p.extract_text() or "") for p in r.pages)


def trae(nombre: str, url: str, forzar: bool = False) -> str:
    destino = CASE / f"{nombre}.txt"
    if destino.exists() and destino.stat().st_size > 500 and not forzar:
        print(f"cache  {nombre}")
        return str(destino)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es-CL,es;q=0.9"})
    try:
        datos = urllib.request.urlopen(req, timeout=60).read()
    except Exception as e:
        print(f"ERROR  {nombre}  {url}  {e}")
        return ""
    es_pdf = datos[:5] == b"%PDF-" or url.lower().endswith(".pdf")
    txt = a_texto_pdf(datos) if es_pdf else limpiar_html(datos)
    (CASE / f"{nombre}.raw").write_bytes(datos)
    destino.write_text(txt, encoding="utf-8")
    print(f"ok     {nombre}  {len(datos)} bytes -> {len(txt)} chars  {url}")
    return str(destino)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--batch":
        for linea in pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").splitlines():
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            nombre, url = linea.split("\t", 1)
            trae(nombre.strip(), url.strip())
    else:
        nombre, urls = sys.argv[1], sys.argv[2:]
        for i, u in enumerate(urls):
            trae(f"{nombre}{'' if i == 0 else '_' + str(i)}", u)
