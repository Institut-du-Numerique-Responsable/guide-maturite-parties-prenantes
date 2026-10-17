// Gabarit Typst du guide (utilisé par Pandoc). Inspiré de la mise en page
// du document Word d'origine : titres en Caladea (Cambria), texte en Carlito (Calibri).

#let brand = rgb("#00668b")
#let light = rgb("#e6f1f5")

#set document(title: "$title$", author: "Institut du Numérique Responsable (INR / ISIT)")
#set text(font: "Carlito", size: 10.5pt, lang: "$lang$")
#set par(justify: true, leading: 0.62em, spacing: 0.9em)
#set page(
  paper: "a4",
  margin: (x: 2.2cm, top: 2.2cm, bottom: 2.4cm),
  footer: context {
    if counter(page).get().first() > 1 [
      #set text(size: 8pt, fill: luma(90))
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        [$footer$],
        counter(page).display(),
      )
    ]
  },
)

#show heading: set text(font: "Caladea", fill: brand)
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  set text(size: 20pt)
  block(below: 1.1em, it)
}
#show heading.where(level: 2): it => {
  set text(size: 13pt)
  block(above: 1.4em, below: 0.7em, breakable: false, it)
}
#show heading.where(level: 3): it => {
  set text(size: 11pt, fill: black)
  block(above: 1em, below: 0.5em, it)
}
#show link: set text(fill: brand)

#set table(
  stroke: 0.5pt + luma(180),
  inset: 5pt,
  fill: (_, y) => if y == 0 { brand } else if calc.even(y) { light },
)
#show table.cell.where(y: 0): set text(fill: white, weight: "bold", size: 9pt)
#show table: set text(size: 9pt)
#show table: set par(justify: false)
#show figure.where(kind: table): set block(breakable: true)
#show figure: set block(breakable: true)

#let horizontalRule = line(start: (25%, 0%), end: (75%, 0%))
#let divider = horizontalRule

$if(highlighting-definitions)$
$highlighting-definitions$
$endif$

// Couverture
#page(footer: none)[
  #v(1fr)
  #align(center)[
    #grid(
      columns: 3,
      gutter: 0.8cm,
      image("$assets$/logo-inr.png", width: 4.2cm),
      image("$assets$/logo-isit-be.png", width: 4.2cm),
      image("$assets$/logo-isit-ch.png", width: 4.2cm),
    )
    #v(2cm)
    #text(font: "Caladea", size: 28pt, weight: "bold", fill: brand)[$title$]
    #v(0.8cm)
    #text(size: 15pt)[$subtitle$]
    #v(1.5cm)
    #text(size: 12pt, weight: "bold")[$report$]
    #v(0.3cm)
    #text(size: 11pt)[$version$]
  ]
  #v(1fr)
  #align(center, text(size: 10pt, fill: luma(80))[Institutes for Sustainable IT – INR / ISIT · CC BY-SA 4.0])
]

// Sommaire
#page(footer: none)[
  #outline(title: [$toc-title$], depth: 1, indent: auto)
]
#counter(page).update(1)

$body$
