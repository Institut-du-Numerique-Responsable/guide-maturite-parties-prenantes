"""Read the evaluation grid from the Markdown chapters and check its consistency.

The Markdown files in docs/<lang>/chapters/ are the single source of truth.
Every question is a level-2 heading ``## <chapter>.<n> <question> {#q<chapter>-<n>}``
followed by a criteria table of three columns: criterion, priority (P1-P3),
weight. The table header carries the question total: ``(total = N points)``.

Usage:
    python scripts/guide.py check         # consistency checks, non-zero exit on error
    python scripts/guide.py json OUT_DIR  # export grille-<lang>.json and .csv
    python scripts/guide.py version       # print the guide version (CITATION.cff)
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


def version() -> str:
    """Guide version, defined once in CITATION.cff."""
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    return re.search(r'^version:\s*"?([^"\n]+)"?', text, re.M).group(1).strip()

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
    problems: list[str] = field(default_factory=list)


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
    """Parse one chapter; structural mistakes are collected in ``problems``."""
    lines = path.read_text(encoding="utf-8").splitlines()
    rel = path.relative_to(ROOT).as_posix()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    chapter = Chapter(int(path.name[:2]), title, rel)
    if not title:
        chapter.problems.append(f"{rel}: titre de chapitre (« # … ») introuvable")
    question = None
    in_rationale = in_table = False
    for n, line in enumerate(lines, start=1):
        where = f"{rel}:{n}"
        m = QUESTION_RE.match(line)
        if m:
            ch, num, title_, ach, anum = m.groups()
            question = Question(f"{ch}.{num}", title_.strip())
            chapter.questions.append(question)
            in_rationale = in_table = False
            if int(ch) != chapter.number:
                chapter.problems.append(f"{where}: question {ch}.{num} dans le fichier du chapitre {chapter.number}")
            if int(num) != len(chapter.questions):
                chapter.problems.append(f"{where}: question {ch}.{num}, numéro attendu {chapter.number}.{len(chapter.questions)}")
            if (ach, anum) != (ch, num):
                chapter.problems.append(f"{where}: ancre {{#q{ach}-{anum}}} différente du numéro {ch}.{num} (attendu {{#q{ch}-{num}}})")
            continue
        if line.startswith("#"):
            if re.match(r"^#+\s*\d+\.\d+", line):
                chapter.problems.append(f"{where}: titre de question mal formé, modèle attendu « ## {chapter.number}.N Question ? {{#q{chapter.number}-N}} »")
            in_rationale = question is not None and bool(RATIONALE_RE.match(line))
            in_table = False
            continue
        if in_rationale and line.strip() and not line.startswith("|"):
            item = re.sub(r"^\s*- ", "• ", line)
            question.rationale = (question.rationale + "\n" + plain(item)).strip()
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if question is None:
            continue
        if not in_table:  # header row: carries the question total
            in_table = True
            t = TOTAL_RE.search(line)
            if t:
                question.total = number(t.group(1))
            else:
                chapter.problems.append(f"{where} §{question.id}: en-tête du tableau sans « total = N points »")
            continue
        if re.match(r"^\|[-:| ]+\|$", line):
            continue
        row = cells(line)
        if len(row) != 3:
            chapter.problems.append(f"{where} §{question.id}: {len(row)} colonnes au lieu de 3 (barre verticale « | » à écrire « \\| » dans le texte ?)")
        elif not PRIORITY_RE.match(row[1]):
            chapter.problems.append(f"{where} §{question.id}: priorité « {row[1]} » invalide (P1, P2 ou P3 attendu)")
        else:
            try:
                question.criteria.append(Criterion(row[0], row[1], number(row[2])))
            except ValueError:
                chapter.problems.append(f"{where} §{question.id}: pondération « {row[2]} » illisible (nombre attendu, ex. 3 ou 1,5)")
    return chapter


def load(lang: str) -> list[Chapter]:
    return [parse_chapter(p) for p in sorted((DOCS / lang / "chapters").glob("*.md"))]


def check() -> list[str]:
    errors = []
    data = {lang: load(lang) for lang in LANGS}
    names = {lang: [pathlib.Path(ch.file).name for ch in chapters] for lang, chapters in data.items()}
    for lang, other in (("fr", "en"), ("en", "fr")):
        for name in sorted(set(names[other]) - set(names[lang])):
            errors.append(f"docs/{lang}/chapters/{name}: fichier manquant (présent en {other.upper()})")
    for lang, chapters in data.items():
        for ch in chapters:
            errors.extend(ch.problems)
            if not ch.questions:
                errors.append(f"{ch.file}: aucune question numérotée")
            for q in ch.questions:
                where = f"{ch.file} §{q.id}"
                if q.total is None:
                    errors.append(f"{where}: total de la question introuvable")
                if not q.criteria:
                    errors.append(f"{where}: aucun critère lu")
                # Only the chapter 6 sub-questions borrow their rationale from chapter 5.
                if not q.rationale and not (ch.number == 6 and int(q.id.split(".")[1]) >= 5):
                    errors.append(f"{where}: section « Raison d'être » / « Rationale » manquante")
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
            if len(qa.criteria) != len(qb.criteria):
                errors.append(f"§{qa.id}: {len(qa.criteria)} critères en FR, {len(qb.criteria)} en EN")
                continue
            for i, (ca, cb) in enumerate(zip(qa.criteria, qb.criteria), start=1):
                if (ca.priority, ca.weight) != (cb.priority, cb.weight):
                    errors.append(f"§{qa.id} critère {i}: FR {ca.priority}/{ca.weight:g} ≠ EN {cb.priority}/{cb.weight:g}")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) >= 1 and argv[0] == "check":
        errors = check()
        for e in errors:
            print(f"ERREUR  {e}")
        n = sum(len(ch.questions) for ch in load("fr"))
        print(f"{n} questions, {len(errors)} erreur(s)")
        return 1 if errors else 0
    if argv == ["version"]:
        print(version())
        return 0
    if len(argv) == 2 and argv[0] == "json":
        out = pathlib.Path(argv[1])
        out.mkdir(parents=True, exist_ok=True)
        for lang in LANGS:
            payload = [{k: v for k, v in asdict(ch).items() if k != "problems"} for ch in load(lang)]
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
