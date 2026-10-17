"""Build the French and English PDFs from the Markdown pages.

Requires pandoc (>= 3.12) and typst (>= 0.15) on the PATH.

Usage: python scripts/build_pdf.py OUT_DIR
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

import guide

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PDF = ROOT / "pdf"
VERSION = guide.version()

# Page order in the PDF (the home page is site-only).
PAGES = ["about", "synthesis", "introduction", "why", "how-to-use"] + [
    f"chapters/{p.stem}" for p in sorted((DOCS / "fr" / "chapters").glob("*.md"))
] + ["glossary", "bibliography", "license"]

META = {
    "fr": dict(
        file="guide-maturite-parties-prenantes-fr.pdf",
        title="Guide d'évaluation et d'influence de la maturité numérique responsable des parties prenantes",
        subtitle="Meilleures pratiques pour évaluer et influencer la maturité de ses parties prenantes en matière de numérique responsable",
        report="Rapport public du groupe de travail – année 2024",
        version=f"Version {VERSION} – édition bilingue",
        toc="Table des matières",
        footer="INR / ISIT – Guide de maturité des parties prenantes – CC BY-SA 4.0, toute réutilisation doit citer l'INR",
    ),
    "en": dict(
        file="stakeholder-maturity-guide-en.pdf",
        title="Guide to evaluating and influencing the maturity of stakeholders in Sustainable IT",
        subtitle="Best practices for evaluating and influencing the maturity of its stakeholders in Sustainable IT",
        report="Public report of the workgroup – year 2024",
        version=f"Version {VERSION} – bilingual edition",
        toc="Table of contents",
        footer="INR / ISIT – Stakeholder maturity guide – CC BY-SA 4.0, any reuse must cite the INR",
    ),
}


def build(lang: str, out: pathlib.Path) -> pathlib.Path:
    m = META[lang]
    sources = [str(DOCS / lang / f"{page}.md") for page in PAGES]
    target = out / m["file"]
    # The intermediate Typst file must sit under --root to reach the images.
    work = ROOT / "build"
    work.mkdir(exist_ok=True)
    typ = work / f"guide-{lang}.typ"
    subprocess.run(
        [
            "pandoc", *sources,
            "--from", "markdown+autolink_bare_uris-implicit_figures",
            "--to", "typst",
            "--template", str(PDF / "template.typ"),
            "--lua-filter", str(PDF / "filter.lua"),
            "--resource-path", str(DOCS / lang),
            "--metadata", f"title={m['title']}",
            "--metadata", f"subtitle={m['subtitle']}",
            "--variable", f"lang={lang}",
            "--variable", f"report={m['report']}",
            "--variable", f"version={m['version']}",
            "--variable", f"toc-title={m['toc']}",
            "--variable", f"footer={m['footer']}",
            "--variable", "assets=/docs/assets/images",
            "--output", str(typ),
        ],
        check=True,
    )
    # Images use paths relative to the page (../assets/...): make them root-relative.
    text = typ.read_text(encoding="utf-8").replace('"../assets/', '"/docs/assets/')
    typ.write_text(text, encoding="utf-8")
    subprocess.run(
        ["typst", "compile", "--root", str(ROOT), "--font-path", str(PDF / "fonts"),
         "--ignore-system-fonts", str(typ), str(target)],
        check=True,
    )
    return target


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    out = pathlib.Path(argv[0]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    for lang in META:
        print(build(lang, out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
