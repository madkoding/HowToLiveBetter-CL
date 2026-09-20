#!/usr/bin/env python3
"""Genera fichas de articulos oficiales desde LeyChile para el capitulo 'No te metas en líos'.

Salida: docs/investigacion/_fichas-leychile.md (borrador de trabajo, no se publica)
Uso: python3 tools/fichas.py
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import leychile as L  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "docs", "investigacion", "_fichas-leychile.md")

# (etiqueta, ref, [articulos], patron de busqueda opcional)
BLOCKS = [
    ("Código Penal · delitos y penas (arts. base)", "1984",
     ["1", "2", "3", "21", "15", "16", "17", "50", "10"], None),
    ("Código Penal · hurto y robo", "1984",
     ["432", "433", "436", "440", "443", "446", "447", "448", "456 bis A", "494 bis", "447 bis"], None),
    ("Código Penal · estafa, apropiación indebida, mal uso de tarjetas", "1984",
     ["467", "468", "470", "470 bis", "473", "474"], None),
    ("Código Penal · lesiones, amenazas, honra", "1984",
     ["296", "297", "391", "395", "397", "399", "400", "412", "413", "416", "417", "418", "494",
      "494 ter"], None),
    ("Código Penal · falsedades y desobediencia", "1984",
     ["193", "196", "199", "210", "269 bis", "292", "293", "318"], None),
    ("Código Penal · conducción en estado de ebriedad (arts. 196 y sgtes.)", "1984",
     ["196", "196 bis", "196 C", "196 D"], None),
    ("Ley 20.000 · drogas", "idLey=20000",
     ["1", "2", "3", "4", "5", "8", "50", "51", "52"], None),
    ("Ley 20.066 · violencia intrafamiliar", "idLey=20066",
     ["1", "5", "8", "14", "15"], None),
    ("Ley 21.459 · delitos informáticos", "idLey=21459",
     ["1", "2", "3", "4", "6", "7", "8", "9", "10", "11", "12"], None),
    ("Ley 19.913 · lavado de activos (UAF)", "idLey=19913",
     ["1", "3", "27", "40"], None),
    ("Ley 17.798 · control de armas", "idLey=17798",
     ["1", "2", "3", "9", "14", "16", "17", "18"], None),
    ("Ley 19.925 · alcoholes", "idLey=19925",
     ["26", "29", "42", "43", "44"], None),
    ("Ley 18.290 · tránsito (pruebas y alcohol)", "idLey=18290",
     ["110", "111", "193", "194"], None),
    ("Ley 20.609 · no discriminación", "idLey=20609",
     ["1", "2", "12"], None),
    ("Ley 17.336 · propiedad intelectual", "idLey=17336",
     ["77", "78", "79", "80", "81"], None),
    ("Ley 21.719 · datos personales (vigencia 1-12-2026)", "idLey=21719",
     ["1", "2", "25", "46"], None),
    ("Ley 21.325 · migración", "idLey=21325",
     ["1", "5", "157", "158"], None),
    ("Ley 21.595 · delitos económicos (ámbito)", "idLey=21595",
     ["1", "2", "3"], None),
    ("Ley 21.663 · ciberseguridad (sanciones)", "idLey=21663",
     [], r"sanci|presidio|multa a beneficio fiscal"),
    ("Ley 21.643 · acoso laboral (ámbito)", "idLey=21643",
     ["1", "2"], None),
]

SKIP = re.compile(r"^(?:NOTA|NOTAS|LEY \d|Decreto|D\.O\.|Ley \d)", re.I)


def main() -> int:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    chunks = ["# Fichas crudas LeyChile (borrador de trabajo)\n",
              "Extraidas automaticamente del texto oficial vigente. NO publicar sin editar.\n"]
    found = 0
    missing = []
    for label, ref, arts, patron in BLOCKS:
        meta = L.metadatos(ref)
        txt = L.text_of(ref)
        chunks.append(f"\n---\n\n## {label}\n")
        chunks.append(f"`{meta['titulo']}` · publicación {meta['publicacion']} · "
                      f"inicio vigencia {meta['inicio_vigencia']} · {meta['url']}\n")
        if patron:
            for i, line in enumerate(txt.split("\n")):
                if re.search(patron, line, re.I):
                    chunks.append("\n> " + line[:600])
                    found += 1
            continue
        for a in arts:
            blk = L.find_article(txt, a)
            if not blk:
                missing.append(f"{label} art {a}")
                chunks.append(f"\n### art. {a}\n\n**NO ENCONTRADO**\n")
                continue
            blk = "\n".join(l for l in blk.split("\n") if not SKIP.match(l))
            chunks.append(f"\n### art. {a}\n\n```\n{blk[:2500]}\n```\n")
            found += 1
    chunks.append("\n---\n\n## NO ENCONTRADOS\n\n" + "\n".join(f"- {m}" for m in missing) + "\n")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("".join(chunks))
    print(f"fichas: {found} bloques -> {OUT}")
    print(f"no encontrados: {len(missing)}")
    for m in missing:
        print("  -", m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
