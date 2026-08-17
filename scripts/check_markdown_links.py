"""Check relative file links in repository Markdown files."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        for target in LINK.findall(markdown.read_text(encoding="utf-8")):
            target = target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            if path_text and not (markdown.parent / path_text).resolve().exists():
                failures.append(f"{markdown.relative_to(ROOT)} -> {target}")
    if failures:
        print("Broken relative Markdown links:")
        print("\n".join(failures))
        return 1
    print("All relative Markdown links resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
