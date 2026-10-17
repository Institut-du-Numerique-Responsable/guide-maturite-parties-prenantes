"""Convert the English PDF guide to Markdown (headings, lists, criteria tables)."""
import re
import sys

import pdfplumber

SRC, OUT = sys.argv[1], sys.argv[2]
FOOTER_Y = 780  # page numbers sit below this line


def style(w):
    f, s = w["fontname"].split("+")[-1], round(w["size"])
    if f.startswith("Cambria"):
        return "h1"
    if f == "Calibri-Bold" and s >= 12:
        return "h3"
    if "Bold" in f:
        return "b"
    if "Italic" in f:
        return "i"
    return "n"


def lines_of(words):
    rows = []
    for w in sorted(words, key=lambda w: (round(w["top"]), w["x0"])):
        if rows and abs(rows[-1][0]["top"] - w["top"]) < 3:
            rows[-1].append(w)
        else:
            rows.append([w])
    return [sorted(r, key=lambda w: w["x0"]) for r in rows]


def render(line):
    out, cur, buf = [], None, []

    def flush():
        if not buf:
            return
        t = " ".join(buf)
        out.append(f"**{t}**" if cur == "b" else f"*{t}*" if cur == "i" else t)

    for w in line:
        s = style(w)
        s = s if s in ("b", "i") else "n"
        if s != cur:
            flush()
            cur, buf = s, []
        buf.append(w["text"])
    flush()
    return " ".join(out).replace("** **", " ")


def clean_cell(c):
    c = (c or "").strip()
    c = re.sub(r"-\n(?=[a-z])", "", c)
    c = re.sub(r"\s*\n\s*([•▪o]|-)\s+", r"<br>• ", c)
    return re.sub(r"\s*\n\s*", " ", c)


blocks = []  # ("h1"|"h2"|"h3"|"p"|"li"|"li2"|"table", payload)
pdf = pdfplumber.open(SRC)
for page in pdf.pages:
    tables = page.find_tables()
    boxes = [t.bbox for t in tables]
    items = []
    for t in tables:
        items.append((t.bbox[1], "table", t.extract()))
    words = [
        w for w in page.extract_words(extra_attrs=["fontname", "size"])
        if w["top"] < FOOTER_Y
        and not any(b[0] - 1 <= w["x0"] and w["x1"] <= b[2] + 1 and b[1] - 1 <= w["top"] <= b[3] + 1 for b in boxes)
    ]
    for ln in lines_of(words):
        items.append((ln[0]["top"], "line", ln))
    items.sort(key=lambda x: x[0])
    prev_bottom = None
    for top, kind, data in items:
        if kind == "table":
            rows = [[clean_cell(c) for c in r] for r in data]
            if blocks and blocks[-1][0] == "table" and rows and not rows[0][0].lower().startswith("evaluation criteria"):
                prev = blocks[-1][1]
                if rows and len(rows[0]) > 2 and not rows[0][1] and not rows[0][2]:
                    prev[-1][0] += " " + rows.pop(0)[0]
                prev.extend(rows)
            else:
                blocks.append(["table", rows])
            prev_bottom = None
            continue
        ln = data
        st = style(ln[0])
        text = render(ln)
        first = ln[0]["text"]
        gap = (top - prev_bottom) if prev_bottom is not None else 99
        prev_bottom = ln[0]["bottom"]
        if st == "h1":
            if blocks and blocks[-1][0] == "h1" and gap < 30:
                blocks[-1][1] += " " + " ".join(w["text"] for w in ln)
            else:
                blocks.append(["h1", " ".join(w["text"] for w in ln)])
            continue
        if st == "h3":
            plain = " ".join(w["text"] for w in ln)
            if blocks and blocks[-1][0] == "h3" and gap < 8:
                blocks[-1][1] += " " + plain
            else:
                blocks.append(["h3", plain])
            continue
        if first in ("•", "▪"):
            blocks.append(["li", render(ln[1:])])
        elif first == "o" and ln[0]["fontname"].endswith("CourierNewPSMT"):
            blocks.append(["li2", render(ln[1:])])
        elif blocks and blocks[-1][0] in ("p", "li", "li2") and gap < 6:
            sep = "" if blocks[-1][1].endswith("-") else " "
            blocks[-1][1] = blocks[-1][1].rstrip("-") + sep + text if sep == "" else blocks[-1][1] + sep + text
        else:
            blocks.append(["p", text])


def table_md(rows):
    head, body = rows[0], rows[1:]
    esc = lambda c: c.replace("|", "\\|")
    out = ["| " + " | ".join(esc(c) for c in head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(esc(c) for c in r) + " |" for r in body]
    return "\n".join(out)


md = []
for kind, data in blocks:
    if kind == "h1":
        md.append(f"# {data}")
    elif kind == "h3":
        md.append(f"## {data}" if data.lower() == "open questions" else f"### {data}")
    elif kind == "li":
        md.append(f"- {data}")
    elif kind == "li2":
        md.append(f"    - {data}")
    elif kind == "table":
        md.append(table_md(data))
    else:
        md.append(data)
text = "\n\n".join(md)
text = re.sub(r"\*\* \*\*", " ", text)
text = re.sub(r" ([’,.;:?)])", r"\1", text).replace("( ", "(")
text = re.sub(r"(?m)^(- .*)\n\n(?=(- |    - ))", r"\1\n", text)
text = re.sub(r"(?m)^(    - .*)\n\n(?=(- |    - ))", r"\1\n", text)
open(OUT, "w").write(text + "\n")
