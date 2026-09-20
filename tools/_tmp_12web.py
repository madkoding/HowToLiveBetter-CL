#!/usr/bin/env python3
"""Descarga (curl) paginas oficiales para el capitulo 12 y las guarda en texto plano.

Uso: python3 tools/_tmp_12web.py <archivo_con_urls>
Guarda el resultado en /tmp/12-web/<slug>.txt y resume estado por URL.
"""
from __future__ import annotations

import html
import os
import re
import subprocess
import sys

DEST = "/tmp/12-web"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
TAG = re.compile(r"<(script|style|noscript)[^>]*>.*?</\1>", re.S | re.I)
ANY = re.compile(r"<[^>]+>")


def limpia(h: str) -> str:
    h = TAG.sub(" ", h)
    h = re.sub(r"<(br|/p|/div|/li|/tr|/h[1-6])\s*/?>", "\n", h, flags=re.I)
    h = ANY.sub("", h)
    h = html.unescape(h).replace("\xa0", " ")
    out = []
    for line in h.split("\n"):
        line = re.sub(r"[ \t]+", " ", line).strip()
        if line:
            out.append(line)
    return "\n".join(out)


def slug(url: str) -> str:
    s = re.sub(r"^https?://", "", url)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return s[:110]


def main() -> int:
    urls = [u.strip() for u in open(sys.argv[1], encoding="utf-8") if u.strip() and not u.startswith("#")]
    os.makedirs(DEST, exist_ok=True)
    for url in urls:
        dest = os.path.join(DEST, slug(url) + ".txt")
        cmd = ["curl", "-sSL", "--max-time", "45", "--compressed", "-A", UA,
               "-H", "Accept-Language: es-CL,es;q=0.9", "-w", "%{http_code} %{size_download}",
               url, "-o", dest + ".raw"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        estado = (r.stdout or "").strip().splitlines()[-1] if r.stdout else f"falla: {r.stderr[:80]}"
        try:
            with open(dest + ".raw", encoding="utf-8", errors="replace") as fh:
                crudo = fh.read()
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(limpia(crudo))
            os.remove(dest + ".raw")
            print(f"{estado}  {len(crudo)}  -> {dest}")
        except Exception as e:  # noqa: BLE001
            print(f"{estado}  error: {type(e).__name__}  {url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
