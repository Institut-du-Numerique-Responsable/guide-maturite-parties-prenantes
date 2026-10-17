"""MkDocs hook: a meta description for every page and the guide version.

Material renders ``page.meta.description`` as <meta name="description">; pages
without front matter get one built from their first paragraph (or, for a
chapter, from its open questions). The version comes from CITATION.cff, the
single source also used by the PDF and Excel builds.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import guide  # noqa: E402

MAX_LEN = 155


def on_config(config):
    config.extra["guide_version"] = guide.version()
    return config


def _clean(text: str) -> str:
    text = guide.plain(text).replace("\n", " ")
    text = re.sub(r"\{#[^}]+\}", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _shorten(text: str) -> str:
    if len(text) <= MAX_LEN:
        return text
    return text[: MAX_LEN - 1].rsplit(" ", 1)[0].rstrip(" ,;:") + "…"


def _description(markdown: str) -> str:
    title = next((l[2:] for l in markdown.splitlines() if l.startswith("# ")), "")
    questions = re.findall(r"(?m)^## \d+\.\d+ (.+?) \{#q", markdown)
    if questions:
        lead = f"{_clean(title)}. " if title else ""
        return _shorten(lead + " ".join(_clean(q) for q in questions))
    for block in re.split(r"\n\s*\n", markdown):
        block = block.strip()
        if block and not block.startswith(("#", "|", "-", "!", "<", ">")):
            return _shorten(_clean(block))
    return ""


def on_page_markdown(markdown, page, config, files):
    if not page.meta.get("description"):
        description = _description(markdown)
        if description:
            page.meta["description"] = description
    return markdown
