#!/usr/bin/env python3
"""Extrae articulos clave para el capitulo 12 desde LeyChile (cache en tools/.cache)."""
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leychile import text_of, find_article  # noqa: E402

OBJETIVO = [
    # (ref, etiqueta, [articulos], [patrones extra])
    ("idNorma=172986", "Codigo Civil", ["2316", "2317", "2320", "2321", "2322"], []),
    ("idNorma=1974", "Codigo de Comercio", ["424", "425", "426"], ["responsabilidad de los accionistas", "acciones y a prorrata"]),
    ("idLey=19857", "Ley 19.857 EIRL", ["1", "2", "3", "4"], ["responsabilidad", "patrimonio propio distinto"]),
    ("idLey=3918", "Ley 3918 SRL", ["1", "2", "3", "5"], ["responsabilidad"]),
    ("idLey=18046", "Ley 18.046 SA", ["1", "2", "3"], []),
    ("idLey=19983", "Ley 19.983 factura", ["1", "2", "3", "4"], []),
    ("idLey=19886", "Ley 19.886 compras", ["9"], []),
    ("idLey=825", "DL 825 IVA", ["2", "3", "9", "12", "14", "54", "64"], ["exento", "activo fijo"]),
    ("idLey=21713", "Ley 21713 cumplimiento tributario", ["1", "2", "3"], ["declarar", "boletas de honorarios", "retencion", "retención", "reserva de boletas"]),
    ("idLey=19799", "Ley 19799 firma electronica", ["1", "2", "3"], []),
    ("idLey=18695", "Ley 18695 municipalidades", ["1", "5", "63", "65"], ["patente"]),
    ("idLey=20255", "Ley 20255 rentas municipales", ["1", "2", "3", "4", "23", "24", "25", "26", "27", "28"], ["patente", "unidades tributarias"]),
    ("idLey=21210", "Ley 21210 modernizacion", ["1"], ["14 D", "Pro Pyme", "tres millones", "capital efectivo"]),
    ("idLey=20416", "Ley 20416 pyme", ["1", "2", "11", "12", "13"], []),
    ("idLey=19496", "Ley 19496 consumidor", ["1", "3", "12", "23", "24", "50", "50 B", "51", "56", "58", "61"], []),
    ("idLey=21398", "Ley 21398", ["1"], ["interes", "interés", "multa", "SERNAC"]),
    ("idNorma=28650", "Ley 16744", ["15", "16", "76"], []),
    ("idNorma=207436", "Codigo del Trabajo", ["7", "9", "10", "58", "161", "162"], []),
    ("idNorma=6374", "Codigo Tributario", ["97", "109", "161"], []),
]

SALIDA = "/tmp/12-fuentes.txt"


def main() -> int:
    with open(SALIDA, "w", encoding="utf-8") as out:
        for ref, etiqueta, arts, patrones in OBJETIVO:
            out.write(f"\n\n########## {etiqueta} ({ref}) ##########\n")
            out.flush()
            try:
                txt = text_of(ref)
            except Exception as e:  # noqa: BLE001
                out.write(f"ERROR al bajar: {type(e).__name__}: {e}\n")
                out.flush()
                continue
            for a in arts:
                blk = find_article(txt, a)
                out.write(f"\n--- art {a} ---\n{blk[:2600]}\n")
            for pat in patrones:
                out.write(f"\n--- patron {pat} ---\n")
                for i, line in enumerate(txt.split("\n")):
                    if re.search(re.escape(pat), line, re.I):
                        out.write(f"{i}: {line[:900]}\n")
            out.flush()
    print("listo", SALIDA)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
