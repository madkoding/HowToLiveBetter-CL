#!/usr/bin/env python3
"""Genera el esqueleto de un capitulo conforme al contrato.

    python3 scripts/nuevo_capitulo.py 07 "vivir sin plata" "Sin plata: qué hacer y qué reclamar"

Crea guia/07-vivir-sin-plata.md con el encabezado y un item de ejemplo que pasa el validador.
Sobrescribe solo con --forzar.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import unicodedata

RAIZ = pathlib.Path(__file__).resolve().parent.parent
GUIA = RAIZ / "guia"

PLANTILLA = """# {numero}. {titulo}

{intro}

### 1. {ejemplo_titulo}
<!-- costos: plata=0 tiempo=poco aguante=no beneficio=alto medida=muerte -->
- Costo: 待核实: cuanto cuesta en plata y en tiempo, en pesos con su anio.
- En simple: {ejemplo_simple}
- Beneficio: 待核实: el dato crudo con su intervalo, tal como esta en la fuente.
- Evidencia: A
- Fuentes: ORGANISMO (anio). Titulo del documento o de la ley, articulo. <https://url-oficial.gob.cl/>
- Notas: 待核实: que falta confirmar y donde habria que buscarlo.
"""


def slug(texto: str) -> str:
    plano = unicodedata.normalize("NFD", texto.lower())
    plano = "".join(c for c in plano if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", plano).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("numero", help="numero de capitulo, dos digitos (ej. 07)")
    ap.add_argument("clave", help="nombre corto, se usa en el nombre del archivo")
    ap.add_argument("titulo", nargs="?", default="", help="titulo visible del capitulo")
    ap.add_argument("--forzar", action="store_true")
    args = ap.parse_args()

    numero = args.numero.zfill(2)
    archivo = GUIA / f"{numero}-{slug(args.clave)}.md"
    if archivo.exists() and not args.forzar:
        print(f"Ya existe: {archivo} (usa --forzar para sobrescribir)")
        return 1
    GUIA.mkdir(parents=True, exist_ok=True)
    archivo.write_text(
        PLANTILLA.format(
            numero=int(numero),
            titulo=args.titulo or args.clave.capitalize(),
            intro="Una linea sobre que cubre este capitulo y que NO cubre (lo que esta en otro capitulo).",
            ejemplo_titulo="La accion, en imperativo y en una linea",
            ejemplo_simple="Una o dos frases en habla normal, sin siglas y sin numeros nuevos.",
        ),
        encoding="utf-8",
    )
    print(f"Creado: {archivo}")
    print("Siguiente: python3 tools/verificar.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
