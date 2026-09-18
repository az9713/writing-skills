#!/usr/bin/env python3
"""Check links between chapter files of an HTML book.

rigorous-explainer's check_links.py resolves href="#id" inside ONE file. A book
has many files, so a link like href="ch03.html#vn-stability" can point to a
missing file or a missing id. This script checks every relative .html link in
every .html file under BOOK_DIR (recursive).

  - href="other.html"       -> the file must exist
  - href="other.html#id"    -> the file must exist and contain id="id"
  - href="#id"              -> the same file must contain id="id"
  - http(s):, mailto:, data:, and non-.html targets are skipped

Usage:     python check_book_links.py BOOK_DIR
Self-test: python check_book_links.py --selftest
Exits 1 if any link is broken.
"""
import os
import re
import sys
import tempfile

ID_RE = re.compile(r'\bid\s*=\s*["\']([^"\']+)["\']')
HREF_RE = re.compile(r'\bhref\s*=\s*["\']([^"\']+)["\']')
SKIP = ("http:", "https:", "mailto:", "data:", "javascript:")


def check(book_dir):
    files = {}
    for root, _, names in os.walk(book_dir):
        for n in names:
            if n.lower().endswith(".html"):
                p = os.path.normpath(os.path.join(root, n))
                files[p] = open(p, encoding="utf-8", errors="replace").read()
    ids = {p: set(ID_RE.findall(s)) for p, s in files.items()}
    broken = []
    for p, s in files.items():
        for m in HREF_RE.finditer(s):
            href = m.group(1).strip()
            if href.lower().startswith(SKIP):
                continue
            target, _, frag = href.partition("#")
            target = target.split("?")[0]
            if target and not target.lower().endswith(".html"):
                continue
            tp = os.path.normpath(os.path.join(os.path.dirname(p), target)) if target else p
            line = s.count("\n", 0, m.start()) + 1
            if tp not in files:
                broken.append((p, line, href, "file not found"))
            elif frag and frag not in ids[tp]:
                broken.append((p, line, href, "id not found"))
    return len(files), broken


def selftest():
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "ch01.html"), "w", encoding="utf-8").write(
            '<h2 id="a">A</h2><a href="ch02.html#b">ok</a>'
            '<a href="ch02.html#zzz">bad id</a><a href="ch09.html">bad file</a>'
            '<a href="#a">ok</a><a href="https://x.org/y.html#q">skip</a>')
        open(os.path.join(d, "ch02.html"), "w", encoding="utf-8").write(
            '<h2 id="b">B</h2><a href="ch01.html">ok</a>')
        n, broken = check(d)
        assert n == 2, n
        assert sorted(b[2] for b in broken) == ["ch02.html#zzz", "ch09.html"], broken
    print("selftest passed")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == "--selftest":
        selftest()
        return
    n, broken = check(sys.argv[1])
    for p, line, href, why in broken:
        print(f"{p}:{line}: {href} -> {why}")
    print(f"{n} files, {len(broken)} broken links")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
