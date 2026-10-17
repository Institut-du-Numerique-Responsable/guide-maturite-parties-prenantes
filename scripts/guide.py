"""Read the evaluation grid from the Markdown chapters and check its consistency.

The Markdown files in docs/<lang>/chapters/ are the single source of truth.
Every question is a level-2 heading ``## <chapter>.<n> <question> {#q<chapter>-<n>}``
followed by a criteria table of three columns: criterion, priority (P1-P3),
weight. The table header carries the question total: ``(total = N points)``.

Usage:
    python scripts/guide.py check         # consistency checks, non-zero exit on error
    python scripts/guide.py json OUT_DIR  # export grille-<lang>.json and .csv
"""

from __future__ import annotations

import csv
import json
import pathlib
import re
import sys
from dataclasses import asdict, dataclass, field

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LANGS = ("fr", "en")
CHAPTER_TOTAL = 100

QUESTION_RE = re.compile(r"^## (\d+)\.(\d+) (.+?) \{#q(\d+)-(\d+)\}$")
TOTAL_RE = re.compile(r"total\s*=\s*([\d.,]+)\s*points", re.I)
PRIORITY_RE = re.compile(r"^P[123]$")
RATIONALE_RE = re.compile(r"^### (Raison d'être|Rationale)\s*$")


@dataclass
class Criterion:
    text: str
    priority: str
    weight: float


@dataclass
class Question:
    id: str
    title: str
    rationale: str = ""
    total: float | None = None
    criteria: list[Criterion] = field(default_factory=list)


@dataclass
class Chapter:
    number: int
    title: str
    file: str
    questions: list[Question] = field(default_factory=list)


def number(text: str) -> float:
    return float(text.replace(",", "."))


def cells(line: str) -> list[str]:
    """Split a Markdown table row, honouring escaped pipes."""
    parts = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [p.strip().replace("\\|", "|") for p in parts]


def plain(markdown: str) -> str:
    """Markdown inline text to plain text (for spreadsheets)."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", markdown)
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    text = text.replace("<br>", "\n")
    return re.sub(r"[*_`]", "", text).strip()


def parse_chapter(path: pathlib.Path) -> Chapter:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = next(l[2:].strip() for l in lines if l.startswith("# "))
    chapter = Chapter(int(path.name[:2]), title, path.relative_to(ROOT).as_posix())
    question = None
    in_rationale = False
    for line in lines:
        m = QUESTION_RE.match(line)
        if m:
            question = Question(f"{m.group(1)}.{m.group(2)}", m.group(3).strip())
            chapter.questions.append(question)
            in_rationale = False
            continue
        if line.startswith("#"):
            in_rationale = question is not None and bool(RATIONALE_RE.match(line))
            continue
        if in_rationale and line.strip():
            item = re.sub(r"^\s*- ", "• ", line)
            question.rationale = (question.rationale + "\n" + plain(item)).strip()
            continue
        if question is None or not line.startswith("|") or re.match(r"^\|[-| ]+\|$", line):
            continue
        t = TOTAL_RE.search(line)
        if t:
            question.total = number(t.group(1))
            continue
        row = cells(line)
        if len(row) == 3 and PRIORITY_RE.match(row[1]):
            question.criteria.append(Criterion(row[0], row[1], number(row[2])))
    return chapter


def load(lang: str) -> list[Chapter]:
    return [parse_chapter(p) for p in sorted((DOCS / lang / "chapters").glob("*.md"))]


def check() -> list[str]:
    errors = []
    data = {lang: load(lang) for lang in LANGS}
    for lang, chapters in data.items():
        for ch in chapters:
            if not ch.questions:
                errors.append(f"{ch.file}: aucune question numérotée")
            for q in ch.questions:
                where = f"{ch.file} §{q.id}"
                if q.total is None:
                    errors.append(f"{where}: total de la question introuvable")
                if not q.criteria:
                    errors.append(f"{where}: aucun critère lu")
                s = sum(c.weight for c in q.criteria)
                if q.total is not None and abs(s - q.total) > 1e-9:
                    errors.append(f"{where}: somme des pondérations {s:g} ≠ total annoncé {q.total:g}")
            s = sum(c.weight for q in ch.questions for c in q.criteria)
            if abs(s - CHAPTER_TOTAL) > 1e-9:
                errors.append(f"{ch.file}: total du chapitre {s:g} ≠ {CHAPTER_TOTAL}")
    # both languages must describe the same grid
    for a, b in zip(data["fr"], data["en"]):
        if [q.id for q in a.questions] != [q.id for q in b.questions]:
            errors.append(f"chapitre {a.number}: questions différentes entre FR et EN")
            continue
        for qa, qb in zip(a.questions, b.questions):
            ra = [(c.priority, c.weight) for c in qa.criteria]
            rb = [(c.priority, c.weight) for c in qb.criteria]
            if ra != rb:
                errors.append(f"§{qa.id}: priorités/pondérations FR {ra} ≠ EN {rb}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) >= 1 and argv[0] == "check":
        errors = check()
        for e in errors:
            print(f"ERREUR  {e}")
        n = sum(len(ch.questions) for ch in load("fr"))
        print(f"{n} questions, {len(errors)} erreur(s)")
        return 1 if errors else 0
    if len(argv) == 2 and argv[0] == "json":
        out = pathlib.Path(argv[1])
        out.mkdir(parents=True, exist_ok=True)
        for lang in LANGS:
            payload = [asdict(ch) for ch in load(lang)]
            (out / f"grille-{lang}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
            with (out / f"grille-{lang}.csv").open("w", encoding="utf-8", newline="") as fh:
                w = csv.writer(fh)
                w.writerow(["chapter", "question_id", "question", "criterion", "priority", "weight"])
                for ch in load(lang):
                    for q in ch.questions:
                        for c in q.criteria:
                            w.writerow([ch.title, q.id, plain(q.title), plain(c.text), c.priority, f"{c.weight:g}"])
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
