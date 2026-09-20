#!/usr/bin/env python3
"""Trae una URL oficial y la deja en texto plano legible en .fuentes/<slug>.txt
Solo stdlib. Uso: python3 fetch.py <url> [<url> ...]
"""
import sys, os, re, hashlib, urllib.request, gzip, io, html

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".fuentes")


def slug(url: str) -> str:
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    base = re.sub(r"^https?://", "", url)
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", base)[:80]
    return f"{base}__{h}"


def clean(h: str) -> str:
    h = re.sub(r"(?is)<(script|style|noscript|svg|head)\b.*?</\1>", " ", h)
    h = re.sub(r"(?is)<!--.*?-->", " ", h)
    # block tags -> newline
    h = re.sub(r"(?i)<(br|/p|/div|/li|/tr|/h[1-6]|/td|/th|/table|/ul|/ol)\s*/?>", "\n", h)
    h = re.sub(r"(?is)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = h.replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in h.split("\n")]
    out, prev_blank = [], False
    for ln in lines:
        if not ln:
            if not prev_blank:
                out.append("")
            prev_blank = True
        else:
            out.append(ln)
            prev_blank = False
    return "\n".join(out).strip()


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/pdf,*/*",
        "Accept-Language": "es-CL,es;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            raw = gzip.decompress(raw)
        enc = r.headers.get_content_charset() or "utf-8"
    text = raw.decode(enc, errors="replace")
    if "%PDF" == text[:4] or url.lower().endswith(".pdf"):
        return text  # PDF: dejar como binario-decodificado, se maneja aparte
    return clean(text)


def main() -> int:
    os.makedirs(DEST, exist_ok=True)
    for url in sys.argv[1:]:
        s = slug(url)
        p = os.path.join(DEST, s + ".txt")
        try:
            t = fetch(url)
            with open(p, "w") as f:
                f.write(f"URL: {url}\n\n{t}\n")
            print(f"OK   {len(t):>7} chars  {p}")
        except Exception as e:
            print(f"FAIL {url} -> {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
