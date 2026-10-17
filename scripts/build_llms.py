"""Write llms.txt (index) and llms-full.txt (full text) for language models.

Both files are generated into docs/ before the MkDocs build, so the site
serves them at its root. See https://llmstxt.org.

Usage: python scripts/build_llms.py OUT_DIR
"""

from __future__ import annotations

import pathlib
import re
import sys

import guide
from build_pdf import PAGES

SITE = "https://institut-du-numerique-responsable.github.io/guide-maturite-parties-prenantes/"
REPO = "https://github.com/Institut-du-Numerique-Responsable/guide-maturite-parties-prenantes"
INR_PAGE = "https://institutnr.org/guide-maturite-parties-prenantes"
DL = SITE + "assets/downloads/"
CITATION = ("Institut du Numérique Responsable (INR) / Institute for Sustainable IT (ISIT), "
            "Guide d'évaluation et d'influence de la maturité numérique responsable des parties prenantes, "
            "version {v}. Licence CC BY-SA 4.0. " + INR_PAGE)


def page_url(lang: str, page: str) -> str:
    prefix = "" if lang == "fr" else "en/"
    return f"{SITE}{prefix}{page}/"


def page_title(lang: str, page: str) -> str:
    text = (guide.DOCS / lang / f"{page}.md").read_text(encoding="utf-8")
    return next(l[2:].strip() for l in text.splitlines() if l.startswith("# "))


def index(version: str) -> str:
    n = sum(len(ch.questions) for ch in guide.load("fr"))
    lines = [
        "# Guide de maturité numérique responsable des parties prenantes (INR)",
        "",
        f"> Guide public de l'Institut du Numérique Responsable (INR) et des Institutes for Sustainable IT (ISIT) "
        f"pour évaluer et influencer la maturité numérique responsable des parties prenantes (fournisseurs, prestataires, partenaires) : "
        f"{n} questions ouvertes, 10 familles de critères, critères pondérés (priorité P1 à P3, 100 points par famille). "
        f"Bilingue français / anglais, version {version}, licence CC BY-SA 4.0.",
        "",
        "Ce guide évalue la maturité (connaissance et capacité à appliquer les bonnes pratiques), pas la performance environnementale. "
        "Les questions ouvertes et leur raison d'être s'envoient aux parties prenantes ; les critères d'évaluation restent chez l'évaluateur. "
        "Le texte en Markdown du dépôt GitHub fait foi ; le site, les PDF et les classeurs en sont générés.",
        "",
        f"Citation requise pour toute réutilisation : {CITATION.format(v=version)}",
        "",
        "## Guide (français)",
        "",
    ]
    lines += [f"- [{page_title('fr', p)}]({page_url('fr', p)})" for p in PAGES]
    lines += ["", "## Guide (English)", ""]
    lines += [f"- [{page_title('en', p)}]({page_url('en', p)})" for p in PAGES]
    lines += [
        "",
        "## Téléchargements / Downloads",
        "",
        f"- [Guide complet, PDF (français)]({DL}guide-maturite-parties-prenantes-fr.pdf)",
        f"- [Full guide, PDF (English)]({DL}stakeholder-maturity-guide-en.pdf)",
        f"- [Grille d'évaluation, Excel (français)]({DL}grille-evaluation-fr.xlsx)",
        f"- [Evaluation grid, Excel (English)]({DL}evaluation-grid-en.xlsx)",
        f"- [Grille, données ouvertes JSON / CSV (français)]({DL}grille-fr.json): une ligne par critère, aussi en [CSV]({DL}grille-fr.csv)",
        f"- [Grid, open data JSON / CSV (English)]({DL}grille-en.json): one row per criterion, also as [CSV]({DL}grille-en.csv)",
        "",
        "## Optional",
        "",
        f"- [Texte intégral / full text]({SITE}llms-full.txt)",
        f"- [Page du guide sur le site de l'INR]({INR_PAGE})",
        f"- [Dépôt source, contributions]({REPO})",
        "",
    ]
    return "\n".join(lines)


def full(version: str) -> str:
    out = [
        "# Guide de maturité numérique responsable des parties prenantes (INR) : texte intégral",
        "",
        f"Version {version}. Licence CC BY-SA 4.0. Citation requise : {CITATION.format(v=version)}",
        f"Index : {SITE}llms.txt",
        "",
    ]
    for lang in guide.LANGS:
        for page in PAGES:
            text = (guide.DOCS / lang / f"{page}.md").read_text(encoding="utf-8")
            text = re.sub(r"\s*\{#q[\d-]+\}", "", text)
            text = re.sub(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?\n?", "", text)
            out += ["---", "", f"Source : {page_url(lang, page)}", f"Langue : {lang}", "", text.strip(), ""]
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    out = pathlib.Path(argv[0])
    out.mkdir(parents=True, exist_ok=True)
    version = guide.version()
    (out / "llms.txt").write_text(index(version), encoding="utf-8")
    (out / "llms-full.txt").write_text(full(version), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
