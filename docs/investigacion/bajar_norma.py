#!/usr/bin/env python3
"""Descarga el texto oficial de una norma desde la API XML pública de LeyChile (BCN).

Uso:  python3 bajar_norma.py <idNorma> [--version AAAA-MM-DD]

API:  https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=<idNorma>
Salida: fuentes/<idNorma>.xml  y  fuentes/<idNorma>.txt  (texto plano de los artículos)
"""
import sys, os, re, html, urllib.request, xml.etree.ElementTree as ET

BASE = "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma={}"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120 Safari/537.36")
NS = {"n": "http://www.leychile.cl/esquemas"}
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "fuentes")
os.makedirs(OUT, exist_ok=True)


def fetch(idnorma, version=None):
    url = BASE.format(idnorma)
    if version:
        url += "&idVersion=" + version
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def flatten(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    idnorma = sys.argv[1]
    version = None
    if "--version" in sys.argv:
        version = sys.argv[sys.argv.index("--version") + 1]
    raw = fetch(idnorma, version)
    xp = os.path.join(OUT, f"{idnorma}.xml")
    with open(xp, "wb") as f:
        f.write(raw)

    root = ET.fromstring(raw)
    print("normaId        :", root.get("normaId"))
    print("fechaVersion   :", root.get("fechaVersion"))
    print("derogado       :", root.get("derogado"))
    ident = root.find("n:Identificador", NS)
    print("tipo/numero    :", ident.find("n:TiposNumeros/n:TipoNumero/n:Tipo", NS).text,
          ident.find("n:TiposNumeros/n:TipoNumero/n:Numero", NS).text)
    print("organismo      :", ident.find("n:Organismos/n:Organismo", NS).text)
    print("fechaPublicacion:", ident.get("fechaPublicacion"))
    print("titulo         :", root.find("n:Metadatos/n:TituloNorma", NS).text)

    partes = []
    WANT = ("Texto", "Encabezado", "Titulo", "Subtitulo", "FechaVersion")
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag in WANT:
            # evita duplicados: sólo nodos hoja de su propio tipo
            if not any(c.tag.split("}")[-1] in WANT for c in el):
                t = flatten("".join(el.itertext()))
                if t:
                    partes.append(t)
    txt = flatten("\n".join(partes))
    tp = os.path.join(OUT, f"{idnorma}.txt")
    with open(tp, "w", encoding="utf-8") as f:
        f.write(txt)
    print("chars          :", len(txt))
    print("guardado en    :", tp)


if __name__ == "__main__":
    main()
