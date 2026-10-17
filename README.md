# Guide de maturité numérique responsable des parties prenantes

**Évaluer et influencer la maturité numérique responsable de ses parties prenantes** (fournisseurs, prestataires, partenaires) : 10 familles de critères, 48 questions ouvertes, une grille pondérée. Rapport public du groupe de travail de l'[Institut du Numérique Responsable](https://institutnr.org) (INR) et des European Institutes for Sustainable IT (ISIT).

🌐 **Site** : <https://institut-du-numerique-responsable.github.io/guide-maturite-parties-prenantes/> · 🇬🇧 [English version](https://institut-du-numerique-responsable.github.io/guide-maturite-parties-prenantes/en/)
📄 **Page du guide sur le site de l'INR** : <https://institutnr.org/guide-maturite-parties-prenantes>

## Ce que contient le dépôt

Le texte du guide, en **Markdown**, est la source unique. À chaque modification de `main`, la chaîne de publication produit automatiquement :

| Livrable | Français | Anglais |
|---|---|---|
| Site web | `/` | `/en/` |
| Guide complet (PDF) | `guide-maturite-parties-prenantes-fr.pdf` | `stakeholder-maturity-guide-en.pdf` |
| Grille d'évaluation (Excel, pour l'évaluateur) | `grille-evaluation-fr.xlsx` | `evaluation-grid-en.xlsx` |
| Questionnaire (Excel, à envoyer, sans les critères) | `questionnaire-fr.xlsx` | `questionnaire-en.xlsx` |
| Données ouvertes | `grille-fr.json`, `grille-fr.csv` | `grille-en.json`, `grille-en.csv` |

Les fichiers sont téléchargeables depuis la page d'accueil du site ; chaque version validée est aussi archivée dans les [releases](https://github.com/Institut-du-Numerique-Responsable/guide-maturite-parties-prenantes/releases).

```
docs/fr/, docs/en/     le guide (une page par section, un fichier par chapitre)
docs/assets/           logos et feuille de style du site
scripts/guide.py       lecture de la grille depuis le Markdown, contrôles, export JSON/CSV
scripts/build_xlsx.py  grilles et questionnaires Excel
scripts/build_pdf.py   PDF (pandoc → Typst), gabarit et polices dans pdf/
tools/conversion/      scripts de la conversion initiale Word/PDF → Markdown (historique)
mkdocs.yml             site bilingue (MkDocs Material + mkdocs-static-i18n)
.github/workflows/     publication, releases, vérification mensuelle des liens
```

## Contribuer

Les adhérents de l'INR et toute personne intéressée peuvent proposer des corrections, des traductions ou des évolutions de critères, directement depuis le navigateur. Les propositions sont relues par le groupe de travail avant publication. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le [code de conduite](CODE_OF_CONDUCT.md).

## Licence et citation

- **Contenu du guide** : [CC BY-SA 4.0](LICENSE). Vous pouvez le partager et l'adapter, y compris à des fins commerciales, à condition de **citer l'Institut du Numérique Responsable** et de partager vos adaptations sous la même licence.
- **Scripts** : [MIT](LICENSE-CODE).

Citation recommandée :

> Institut du Numérique Responsable (INR) / Institute for Sustainable IT (ISIT), *Guide d'évaluation et d'influence de la maturité numérique responsable des parties prenantes*, version 1.2, 2026. Licence CC BY-SA 4.0. <https://institutnr.org/guide-maturite-parties-prenantes>

Voir aussi [CITATION.cff](CITATION.cff) et la liste des [contributeurs](CONTRIBUTORS.md).

---

## English

**Evaluate and influence the Sustainable IT maturity of your stakeholders**: 10 families of criteria, 48 open questions and a weighted grid, published by the Institut du Numérique Responsable (INR) and the European Institutes for Sustainable IT (ISIT). The Markdown text in `docs/en/` and `docs/fr/` is the single source; the website, PDFs, Excel grids, questionnaires and open data are rebuilt automatically on every change.

Content is licensed under **CC BY-SA 4.0**: any reuse must **cite the Institut du Numérique Responsable** (see [CITATION.cff](CITATION.cff)). Scripts are under MIT. Contributions are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) (in French; issues and pull requests in English are welcome too).
