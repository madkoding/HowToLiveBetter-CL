#!/usr/bin/env python3
"""Sincroniza los conteos del README con lo que hay realmente en guia/.

Cuenta los items y los grados de evidencia, y reescribe la linea de estado del README.
Se corre antes de cada commit: es mas confiable que editar el numero a mano.

    python3 tools/sincronizar.py           # reescribe la linea de estado
    python3 tools/sincronizar.py --revisar # solo informa si esta desincronizado (para CI)
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from collections import Counter

RAIZ = pathlib.Path(__file__).resolve().parent.parent
GUIA = RAIZ / "guia"
README = RAIZ / "README.md"
RE_ESTADO = re.compile(r"^\*\*Estado:\*\*.*$", re.M)


def contar() -> tuple[int, int, Counter]:
    capitulos = sorted(GUIA.glob("*.md"))
    total = 0
    niveles: Counter = Counter()
    for ruta in capitulos:
        texto = ruta.read_text(encoding="utf-8")
        total += len(re.findall(r"^### \d+\.", texto, re.M))
        niveles.update(re.findall(r"^-\s*Evidencia:\s*([ABC])", texto, re.M))
    return len(capitulos), total, niveles


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--revisar", action="store_true", help="solo comprueba, sin escribir")
    args = ap.parse_args()

    caps, total, niveles = contar()
    lineas = README.read_text(encoding="utf-8")

    if caps == 32:
        nueva = (
            f"**Estado:** los 32 capítulos completos, **{total} ítems** "
            f"({niveles['A']} grado A, {niveles['B']} grado B, {niveles['C']} grado C)."
        )
    else:
        nueva = (
            f"**Estado:** {caps} de 32 capítulos escritos, **{total} ítems** "
            f"({niveles['A']} grado A, {niveles['B']} grado B, {niveles['C']} grado C)."
        )

    actual = RE_ESTADO.search(lineas)
    if actual is None:
        print("ERROR: el README no tiene linea '**Estado:**'", file=sys.stderr)
        return 1

    if args.revisar:
        if actual.group(0).strip() != nueva:
            print(f"DESINCRONIZADO\n  README: {actual.group(0).strip()}\n  real:   {nueva}")
            return 1
        print(f"OK: {caps} capítulos, {total} ítems, A={niveles['A']} B={niveles['B']} C={niveles['C']}")
        return 0

    README.write_text(RE_ESTADO.sub(nueva, lineas, count=1), encoding="utf-8")
    print(f"README actualizado: {caps} capítulos, {total} ítems, A={niveles['A']} B={niveles['B']} C={niveles['C']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
