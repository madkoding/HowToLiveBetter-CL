#!/usr/bin/env python3
"""Genera el briefing de redaccion de cada capitulo.

Junta, en un solo archivo, todo lo que un redactor (humano o agente) necesita para escribir un
capitulo conforme al contrato: las reglas, la investigacion aplicable y el capitulo original del
que se conservan los items de evidencia internacional.

    python3 tools/briefing.py               # todos los capitulos del PLAN.md
    python3 tools/briefing.py 19 07         # solo esos
    python3 tools/briefing.py --list        # muestra el plan sin generar nada

Salida: guia/_brief/<NN>.md
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PLAN = RAIZ / "PLAN.md"
INVEST = RAIZ / "docs" / "investigacion"
ORIGEN = pathlib.Path("/tmp/HowToLiveBetter/book/en")  # corpus fuente, solo lectura
SALIDA = RAIZ / "guia" / "_brief"

RE_FILA = re.compile(r"^\|\s*(\d{2})\s*\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|$")


def leer_plan() -> list[dict]:
    if not PLAN.exists():
        sys.exit(f"No existe {PLAN}")
    filas = []
    for linea in PLAN.read_text(encoding="utf-8").splitlines():
        m = RE_FILA.match(linea.strip())
        if not m:
            continue
        num, titulo, investiga, conserva, reemplaza = (g.strip() for g in m.groups())
        filas.append(
            {
                "num": num,
                "titulo": titulo,
                "investiga": [x.strip() for x in investiga.split("+")],
                "conserva": conserva,
                "reemplaza": reemplaza,
            }
        )
    return filas


def capitulo_origen(num: str) -> pathlib.Path | None:
    """El capitulo del corpus original que corresponde por numero."""
    if not ORIGEN.exists():
        return None
    coincidencias = sorted(ORIGEN.glob(f"{int(num):02d}-*.md"))
    return coincidencias[0] if coincidencias else None


def informe_investigacion(nombre: str) -> pathlib.Path | None:
    limpio = nombre.strip().lower().replace(" ", "-")
    if limpio in {"—", "-", ""}:
        return None
    ruta = INVEST / f"{limpio}.md"
    return ruta if ruta.exists() else None


def generar(fila: dict, con_origen: bool = True) -> tuple[pathlib.Path, list[str]]:
    avisos: list[str] = []
    partes: list[str] = []

    partes.append(f"# Briefing · capítulo {fila['num']} — {fila['titulo']}\n")
    partes.append(
        "Estás escribiendo un capítulo de la guía chilena **HowToLiveBetter-CL**, adaptación de\n"
        "`dlgrv/HowToLiveBetter`. Antes de escribir una sola línea, lee el contrato completo:\n"
        "`ADAPTACION.md`. Manda sobre este briefing.\n"
    )

    partes.append("## Qué conservar del original\n")
    partes.append(f"{fila['conserva']}\n")
    partes.append(
        "\nLos ítems marcados como conservados **mantienen su estudio y sus cifras tal cual**, con su\n"
        "DOI. No se recalculan ni se \"traducen\" los números. Solo se les agrega el dato chileno si\n"
        "existe uno oficial.\n"
    )

    partes.append("## Qué reemplazar por la realidad chilena\n")
    partes.append(f"{fila['reemplaza']}\n")

    partes.append("\n## Investigación aplicable\n")
    hubo = False
    for nombre in fila["investiga"]:
        ruta = informe_investigacion(nombre)
        if ruta:
            hubo = True
            partes.append(f"### `{ruta.relative_to(RAIZ)}`\n")
            partes.append(ruta.read_text(encoding="utf-8"))
            partes.append("\n")
        elif nombre.strip() not in {"—", "-", ""}:
            avisos.append(f"falta el informe de investigación '{nombre}'")
            partes.append(f"### (falta `docs/investigacion/{nombre}.md`)\n")
    if not hubo:
        partes.append(
            "_Este capítulo no depende de un informe de investigación: usa el capítulo original y\n"
            "las fuentes internacionales que ya trae._\n"
        )

    if con_origen:
        origen = capitulo_origen(fila["num"])
        if origen and origen.exists():
            texto = origen.read_text(encoding="utf-8")
            partes.append(f"\n## Capítulo original (fuente, en inglés)\n")
            partes.append(
                f"`{origen}` — de aquí salen los ítems de evidencia internacional que se conservan.\n"
                "Los ítems chinos se **borran**, no se traducen.\n\n"
            )
            partes.append("<details>\n<summary>Texto completo del capítulo original</summary>\n\n")
            partes.append(texto)
            partes.append("\n</details>\n")
        else:
            avisos.append(f"no se encontró el capítulo original {fila['num']} en {ORIGEN}")

    partes.append(
        "\n## Formato de entrega\n\n"
        f"Escribe `guia/{fila['num']}-<clave>.md`. Estructura:\n\n"
        "```markdown\n"
        f"# {int(fila['num'])}. {fila['titulo']}\n\n"
        "Una línea sobre qué cubre y qué no (lo que está en otro capítulo).\n\n"
        "### 1. <acción en imperativo>\n"
        "<!-- costos: plata=0 tiempo=poco aguante=no beneficio=alto medida=muerte -->\n"
        "- Costo: ...\n- En simple: ...\n- Beneficio: ...\n- Evidencia: A\n- Fuentes: ...\n- Notas: ...\n"
        "```\n\n"
        "Reglas duras (el validador falla si no se cumplen):\n\n"
        "1. Cinco campos exactos y en ese orden; la etiqueta de costos va inmediatamente bajo el título.\n"
        "2. Numeración de ítems continua desde 1, sin saltos.\n"
        "3. `En simple` sin siglas estadísticas y sin números que no estén en `Beneficio` o `Costo`.\n"
        "4. Cada ítem con al menos una URL de fuente oficial que abra.\n"
        "5. Ordenados por costo/beneficio: primero lo gratis que salva vidas.\n"
        "6. **Lo que no puedas verificar se marca `POR VERIFICAR` y se anota en\n"
        f"   `docs/verificacion/{fila['num']}-<clave>.md`. Inventar un dato está prohibido.**\n\n"
        "Al terminar: `python3 tools/verificar.py` debe dar 0 errores para tu capítulo.\n"
    )

    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / f"{fila['num']}-brief.md"
    destino.write_text("".join(partes), encoding="utf-8")
    return destino, avisos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("capitulos", nargs="*", help="números de capítulo (ej. 19 07)")
    ap.add_argument("--list", action="store_true", help="muestra el plan y sale")
    ap.add_argument("--sin-origen", action="store_true", help="no incrusta el capítulo original")
    args = ap.parse_args()

    plan = leer_plan()
    if not plan:
        print("No se pudo leer el plan. Revisa PLAN.md", file=sys.stderr)
        return 1

    if args.list:
        print(f"{len(plan)} capítulos en PLAN.md:")
        for fila in plan:
            marca = " ".join(fila["investiga"])
            print(f"  {fila['num']}  {fila['titulo']:<42} ← {marca}")
        return 0

    seleccion = plan
    if args.capitulos:
        pedidos = {c.zfill(2) for c in args.capitulos}
        seleccion = [f for f in plan if f["num"] in pedidos]
        faltan = pedidos - {f["num"] for f in seleccion}
        if faltan:
            print(f"No están en el plan: {sorted(faltan)}", file=sys.stderr)

    total_avisos = 0
    for fila in seleccion:
        destino, avisos = generar(fila, con_origen=not args.sin_origen)
        kb = destino.stat().st_size / 1024
        estado = f"  ({'; '.join(avisos)})" if avisos else ""
        print(f"{destino.relative_to(RAIZ)}  {kb:.0f} kB{estado}")
        total_avisos += len(avisos)

    if total_avisos:
        print(f"\n{total_avisos} avisos: investigación aún no disponible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
