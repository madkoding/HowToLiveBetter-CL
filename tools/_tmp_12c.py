#!/usr/bin/env python3
"""Tercera pasada: articulos que faltan para el capitulo 12."""
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leychile import text_of, find_article, metadatos  # noqa: E402

SALIDA = "/tmp/12-fuentes3.txt"

with open(SALIDA, "w", encoding="utf-8") as out:
    # metadatos utiles
    for ref in ("idLey=21133", "idLey=20494", "idNorma=6368", "idLey=21141", "idLey=21504"):
        try:
            out.write(f"META {ref}: {metadatos(ref)}\n")
        except Exception as e:  # noqa: BLE001
            out.write(f"META {ref}: ERROR {type(e).__name__}: {e}\n")
    out.write("\n")

    # 1) Codigo Tributario art 97 completo
    ct = text_of('idNorma=6374')
    out.write("### CT art 97 (completo)\n" + find_article(ct, '97')[:6000] + "\n\n")

    # 2) Codigo de Comercio: sociedades colectivas responsabilidad
    com = text_of('idNorma=1974')
    for a in ['365', '366', '370', '371', '472', '473', '474']:
        out.write(f"### CCom art {a}\n{find_article(com, a)[:900]}\n\n")
    out.write("### CCom patron socios colectivos\n")
    for i, l in enumerate(com.split("\n")):
        if re.search(r'socios colectivos|sociedad colectiva', l, re.I) and re.search(r'responsab|solidar', l, re.I):
            out.write(f"{i}: {l[:400]}\n")

    # 3) Ley 19.857 EIRL arts 1, 13, 15, 17
    e = text_of('idLey=19857')
    for a in ['1', '13', '15', '17']:
        out.write(f"### EIRL art {a}\n{find_article(e, a)[:900]}\n\n")

    # 4) Ley 20.416: contexto del articulo que crea la patente provisoria
    p = text_of('idLey=20416').split("\n")
    out.write("### 20.416 contexto patente provisoria\n")
    out.write("\n".join(p[200:232]) + "\n\n")

    # 5) Ley 20.494
    try:
        q = text_of('idLey=20494')
        out.write("### Ley 20.494 (completa)\n" + q[:5000] + "\n\n")
    except Exception as e:  # noqa: BLE001
        out.write(f"### Ley 20.494 ERROR {type(e).__name__}\n")

    # 6) Ley 21.398: facultades del SERNAC
    l2 = text_of('idLey=21398')
    out.write("### 21.398 patrones SERNAC\n")
    for i, l in enumerate(l2.split("\n")):
        if re.search(r'58 bis|facultad|sancion|multa de hasta', l, re.I):
            out.write(f"{i}: {l[:400]}\n")

    # 7) Ley 20.720 art 273 y definicion micro/pequena
    x = text_of('idLey=20720')
    out.write("\n### 20.720 art 273\n" + find_article(x, '273')[:1200] + "\n")
    for i, l in enumerate(x.split("\n")):
        if re.search(r'article 273|micro o pequeña empresa de conformidad', l, re.I):
            out.write(f"{i}: {l[:400]}\n")

    # 8) LIR (DL 824) si existe
    try:
        r = text_of('idNorma=6368')
        for a in ['42', '20', '14']:
            out.write(f"\n### LIR art {a}\n{find_article(r, a)[:2000]}\n")
    except Exception as e:  # noqa: BLE001
        out.write(f"\n### LIR ERROR {type(e).__name__}: {e}\n")

print("listo", SALIDA)
