#!/usr/bin/env python3
"""Construye datos.json desde guia/ para el buscador index.html.

Uso:  python3 tools/construir.py
"""

from __future__ import annotations

import json
import pathlib
import re
import unicodedata

RAIZ = pathlib.Path(__file__).resolve().parent.parent
GUIA = RAIZ / "guia"
SALIDA = RAIZ / "datos.json"

RE_ITEM = re.compile(r"^### (\d+)\.\s+(.+)$")
RE_TAG = re.compile(
    r"^<!--\s*costos:\s*plata=(\S+)\s+tiempo=(\S+)\s+aguante=(\S+)\s+beneficio=(\S+)\s+medida=(\S+)\s*-->\s*$"
)
RE_CAMPO = re.compile(r"^-\s*([A-Za-zÁÉÍÓÚáéíóúñ ]+):\s*(.*)$")
RE_URL = re.compile(r"https?://[^\s<>)\]]+")
RE_TITULO = re.compile(r"^#\s+(.+)$")


def sin_acentos(texto: str) -> str:
    """Normaliza para que la busqueda ignore tildes y mayusculas."""
    plano = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in plano if unicodedata.category(c) != "Mn")


def main() -> None:
    items: list[dict] = []
    capitulos: list[dict] = []

    for ruta in sorted(GUIA.glob("*.md")):
        lineas = ruta.read_text(encoding="utf-8").splitlines()
        titulo_cap = ""
        for linea in lineas:
            if linea.startswith("# "):
                titulo_cap = linea[2:].strip()
                break
        capitulos.append({"archivo": ruta.name, "titulo": titulo_cap})

        i = 0
        while i < len(lineas):
            m = RE_ITEM.match(lineas[i])
            if not m:
                i += 1
                continue
            numero, titulo = int(m.group(1)), m.group(2).strip()
            j = i + 1
            cuerpo: list[str] = []
            while j < len(lineas) and not RE_ITEM.match(lineas[j]):
                cuerpo.append(lineas[j])
                j += 1

            registro: dict = {
                "capitulo": titulo_cap,
                "archivo": ruta.name,
                "numero": numero,
                "titulo": titulo,
                "linea": i + 1,
            }
            for k, linea in enumerate(cuerpo):
                limpia = linea.strip()
                mt = RE_TAG.match(limpia)
                if mt:
                    plata, tiempo, aguante, beneficio, medida = (g.lower() for g in mt.groups())
                    registro.update(
                        {
                            "plata": plata,
                            "tiempo": tiempo,
                            "aguante": aguante,
                            "beneficio_nivel": beneficio,
                            "medida": medida,
                        }
                    )
                    continue
                mc = RE_CAMPO.match(limpia)
                if mc:
                    campo = sin_acentos(mc.group(1).strip())
                    valor = mc.group(2).strip()
                    if campo in {"costo", "beneficio", "evidencia", "fuentes", "notas"}:
                        registro[campo] = valor
                        if campo == "costo" and k == 0:
                            registro["costo"] = valor
                    elif campo == "en simple":
                        registro["simple"] = valor
            registro["urls"] = RE_URL.findall(registro.get("fuentes", ""))
            registro["busqueda"] = sin_acentos(
                " ".join(
                    [
                        registro["titulo"],
                        titulo_cap,
                        registro.get("simple", ""),
                        registro.get("costo", ""),
                        registro.get("beneficio", ""),
                        registro.get("notas", ""),
                    ]
                )
            )
            items.append(registro)
            i = j

    SALIDA.write_text(
        json.dumps({"capitulos": capitulos, "items": items, "total": len(items)}, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    print(f"datos.json: {len(items)} items, {len(capitulos)} capitulos")


if __name__ == "__main__":
    main()
