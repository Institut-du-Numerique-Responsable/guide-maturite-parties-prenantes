"""Split one converted guide (fr|en) into the repository's Markdown files."""
import pathlib
import re
import sys

lang, src, dest = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
text = src.read_text()

CHAPTER_SLUGS = [
    "01-governance-strategy", "02-training-competences", "03-measuring",
    "04-end-of-life-circular-economy", "05-internal-infrastructures",
    "06-external-infrastructures", "07-usage-procurement",
    "08-ecosystem-contribution", "09-digital-services", "10-societal-impacts",
]
L = {
    "fr": dict(oq="Question ouverte", oqs="Questions ouvertes", rat="Raison d'être",
               crit="Critères d'évaluation", gloss="Glossaire", ch="Chapitre"),
    "en": dict(oq="Open question", oqs="Open questions", rat="Rationale",
               crit="Evaluation criteria", gloss="Glossary", ch="Chapter"),
}[lang]

# Word page breaks: empty headings and horizontal rules.
text = re.sub(r"(?m)^#+\s*$\n?", "", text)
text = re.sub(r"(?m)^-{10,}\s*$\n?", "", text)
text = re.sub(r"\n{3,}", "\n\n", text)

# Cut on level-1 headings (comment markers may wrap the title).
parts = re.split(r"(?m)^# (.*)$", text)
sections = [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def plain(h):
    return re.sub(r"⟦|⟧\{C\d+:[^}]*\}", "", h).strip()


def key(title):
    t = plain(title).lower()
    m = re.match(r"(chapitre|chapter) (\d+)", t)
    if m:
        return f"chapters/{CHAPTER_SLUGS[int(m.group(2)) - 1]}"
    for k, words in {
        "synthesis": ("synthèse", "synthesis"),
        "introduction": ("introduction",),
        "why": ("pourquoi", "why"),
        "how-to-use": ("comment utiliser", "how to use"),
        "glossary": ("glossary", "glossaire"),
        "bibliography": ("bibliograph",),
        "license": ("publication",),
    }.items():
        if t.startswith(words):
            return k
    return "about"


def chapter(num, title, body):
    """Number each open question and normalise sub-headings."""
    title = re.sub(r"^(⟦?)(Chapitre|Chapter)\s*\d+\s*:\s*", r"\1", title)
    out = [f"# {L['ch']} {num} : {title}" if lang == "fr" else f"# {L['ch']} {num}: {title}"]
    body = re.sub(r"(?m)^## .*$", f"## {L['oqs']}", body, count=1)
    q = 0
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r"### (Question ouverte|Open [Qq]uestion)\s*$", plain(ln)):
            # question text = next non-empty line(s) of the following bullet list
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            qs = []
            while j < len(lines) and lines[j].startswith(("- ", "  ")):
                qs.append(re.sub(r"^- ", "", lines[j]).strip())
                j += 1
            if not qs:  # question written as a plain paragraph
                qs = [lines[j].strip()]
                j += 1
            q += 1
            head, rest = qs[0], qs[1:]
            out.append(f"## {num}.{q} {head} {{#q{num}-{q}}}")
            out.extend(f"- {r}" for r in rest)
            i = j
            continue
        m = re.match(r"- \*\*(.+)\*\*\s*$", ln)
        nxt = next((x for x in lines[i + 1:] if x.strip()), "")
        if m and nxt.startswith("|"):
            # Chapter 6 sub-questions: bold bullet directly followed by a criteria table
            q += 1
            out.append(f"## {num}.{q} {m.group(1).replace('** **', ' ')} {{#q{num}-{q}}}")
            out.append("")
            out.append(f"### {L['crit']}")
            i += 1
            continue
        if re.match(r"### (Raison d'être|Rationale)", plain(ln)):
            ln = ln.replace(plain(ln)[4:], L["rat"]) if "⟦" not in ln else ln
        if re.match(r"### (Critères d'évaluation|Evaluation criteria)", plain(ln)):
            ln = ln if "⟦" in ln else f"### {L['crit']}"
        out.append(ln)
        i += 1
    return "\n".join(out)


files = {}
for title, body in sections:
    k = key(title)
    if k.startswith("chapters/"):
        num = CHAPTER_SLUGS.index(k.split("/")[1]) + 1
        content = chapter(num, title, body)
    elif k == "glossary":
        content = f"# {L['gloss']}\n\n{body}"
    else:
        content = f"# {title}\n\n{body}"
    files[k] = files.get(k, "") + ("\n\n" if k in files else "") + content

for k, content in files.items():
    p = dest / lang / f"{k}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(re.sub(r"\n{3,}", "\n\n", content).strip() + "\n")
    print(p)
