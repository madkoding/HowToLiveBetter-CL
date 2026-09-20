#!/usr/bin/env python3
"""Segunda pasada de extraccion para el capitulo 12."""
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leychile import text_of, find_article  # noqa: E402

SALIDA = "/tmp/12-fuentes2.txt"

OBJETIVO = [
    ("idNorma=1974", "CCom SpA", [str(n) for n in range(428, 448)], []),
    ("idLey=19857", "EIRL 19.857", [str(n) for n in range(5, 19)], []),
    ("idNorma=172986", "CC", ["1514", "2369", "2370", "2445", "2452", "2465"], []),
    ("idLey=19496", "LPDC", ["28", "55", "55 bis", "56", "56 bis", "57"], []),
    ("idLey=21210", "21210 contexto", [], ["Régimen Pro Pyme", "Artículo 2.-", "Artículo 3.-"]),
    ("idNorma=6374", "CT", [], ["boleta", "no otorgar", "documentos tributarios"]),
    ("idLey=20720", "20.720", ["1", "2"], ["microempresa|micro y pequeña|simplificada"]),
    ("idNorma=28650", "16744", ["2", "3", "68"], []),
    ("idNorma=7054", "DL3063", ["29", "30", "31", "32", "33"], []),
    ("idLey=21398", "21398 mas", ["1"], ["artículo 23", "artículo 24", "artículo 56"]),
]

with open(SALIDA, "w", encoding="utf-8") as out:
    for ref, etiqueta, arts, patrones in OBJETIVO:
        out.write(f"\n\n########## {etiqueta} ({ref}) ##########\n")
        out.flush()
        try:
            txt = text_of(ref)
        except Exception as e:  # noqa: BLE001
            out.write(f"ERROR: {type(e).__name__}: {e}\n")
            continue
        for a in arts:
            out.write(f"\n--- art {a} ---\n{find_article(txt, a)[:1500]}\n")
        for pat in patrones:
            out.write(f"\n--- patron {pat} ---\n")
            for i, line in enumerate(txt.split("\n")):
                if re.search(pat, line, re.I):
                    out.write(f"{i}: {line[:400]}\n")
        out.flush()
print("listo", SALIDA)
