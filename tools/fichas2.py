#!/usr/bin/env python3
"""Segunda tanda de fichas crudas LeyChile (borrador de trabajo).

Uso: python3 tools/fichas2.py
Salida: docs/investigacion/_fichas-leychile-2.md
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import leychile as L  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "docs", "investigacion", "_fichas-leychile-2.md")

BLOCKS = [
    ("Ley 20.084 · responsabilidad penal adolescente", "idLey=20084",
     ["1", "3", "6", "7", "22", "23"], None),
    ("Ley 21.325 · migración y extranjería", "idLey=21325",
     ["1", "41", "42", "157", "158"], None),
    ("Ley 17.336 · propiedad intelectual (penas)", "idLey=17336",
     ["77", "78", "79", "80"], None),
    ("Ley 19.925 · alcoholes (expendio)", "idLey=19925",
     ["3", "26", "42", "43", "44"], None),
    ("Ley 19.913 · UAF obligados a informar", "idLey=19913",
     ["3", "4", "5"], None),
    ("Ley 20.609 · no discriminación", "idLey=20609",
     ["1", "2", "12", "13"], None),
    ("Ley 21.595 · delitos económicos", "idLey=21595",
     ["1", "2"], None),
    ("Ley 17.798 · control de armas (versión publicada)", "idLey=17798",
     ["2", "4", "5", "6", "11", "12", "13", "15", "18", "19"], None),
    ("Ley 20.009 · tarjetas de pago", "idLey=20009",
     ["1", "4", "5", "6", "7"], None),
    ("Ley 21.719 · datos personales (sanciones)", "idLey=21719", [],
     r"presidio|multa a beneficio fiscal|infracci[oó]n grav[ií]sima"),
    ("Ley 21.663 · ciberseguridad (sanciones)", "idLey=21663", [],
     r"presidio|multa a beneficio fiscal"),
    ("Ley 21.643 · acoso laboral y sexual (ámbito)", "idLey=21643", [],
     r"Art[íi]culo 2|acoso laboral|acoso sexual"),
]

SKIP = re.compile(r"^(?:NOTA|NOTAS|LEY \d|Decreto|D\.O\.|Ley \d)", re.I)


def main() -> int:
    chunks = ["# Fichas crudas LeyChile, segunda tanda (borrador)\n"]
    found, missing = 0, []
    for label, ref, arts, patron in BLOCKS:
        meta = L.metadatos(ref)
        txt = L.text_of(ref)
        chunks.append(f"\n---\n\n## {label}\n")
        chunks.append(f"`{meta['titulo']}` · publicación {meta['publicacion']} · "
                      f"inicio vigencia {meta['inicio_vigencia']} · {meta['url']}\n")
        if patron:
            for line in txt.split("\n"):
                if re.search(patron, line, re.I):
                    chunks.append("\n> " + line[:700])
                    found += 1
            continue
        for a in arts:
            blk = L.find_article(txt, a)
            if not blk:
                missing.append(f"{label} art {a}")
                chunks.append(f"\n### art. {a}\n\n**NO ENCONTRADO**\n")
                continue
            blk = "\n".join(l for l in blk.split("\n") if not SKIP.match(l))
            chunks.append(f"\n### art. {a}\n\n```\n{blk[:2600]}\n```\n")
            found += 1
    chunks.append("\n---\n\n## NO ENCONTRADOS\n\n" + "\n".join(f"- {m}" for m in missing) + "\n")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("".join(chunks))
    print(f"fichas: {found} -> {OUT}")
    print("no encontrados:", missing)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
