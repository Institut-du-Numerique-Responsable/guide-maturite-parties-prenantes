# Contribuer au guide

Le guide est écrit en **Markdown** dans ce dépôt. À chaque modification validée, un robot reconstruit le site bilingue, les PDF, les grilles Excel et les données ouvertes : **personne ne met en page à la main**.

Vous contribuez depuis votre navigateur, sans rien installer.

## 1. Signaler un problème ou proposer une idée

Ouvrez une [issue](https://github.com/Institut-du-Numerique-Responsable/guide-maturite-parties-prenantes/issues/new/choose) et choisissez le modèle : **correction**, **évolution d'un critère** ou **traduction**. C'est le plus simple si vous ne souhaitez pas modifier le texte vous-même.

## 2. Modifier le texte

1. Sur le site, cliquez sur l'icône **crayon** (« Modifier cette page ») en haut de la page concernée, ou ouvrez le fichier dans `docs/fr/` ou `docs/en/`.
2. Faites votre modification dans l'éditeur GitHub.
3. En bas : « Commit changes » → cochez **« Create a new branch and start a pull request »** → décrivez votre changement.
4. Les relecteurs du groupe de travail commentent, puis approuvent. Dès la fusion, GitHub Actions republie le site, les PDF et les classeurs.

## 3. Règles à respecter

### Les deux langues avancent ensemble

`docs/fr/` et `docs/en/` décrivent **la même grille**. Si vous modifiez un critère, une priorité ou une pondération dans une langue, faites-le dans l'autre (ou signalez dans la pull request qu'une traduction est nécessaire : le libellé `traduction` sera ajouté).

### Structure d'une question (ne pas casser)

Les scripts lisent les grilles Excel, le CSV et le JSON dans le Markdown. Chaque question suit ce modèle :

```markdown
## 3.2 Comment évaluez-vous l'impact environnemental … ? {#q3-2}

### Raison d'être

Texte libre.

### Critères d'évaluation

| Critère d'évaluation | Priorité recommandée | Pondération proposée (total = 18 points) |
|---|---|---|
| Texte du critère. | P1 | 4 |
```

- le titre `## <chapitre>.<n> … {#q<chapitre>-<n>}` numérote la question ;
- la priorité vaut `P1`, `P2` ou `P3` ;
- la somme des pondérations d'une question égale le total annoncé, et chaque chapitre totalise **100 points** ;
- dans une cellule, un retour à la ligne s'écrit `<br>` et une puce `<br>• `.

Le contrôle automatique (`python scripts/guide.py check`) vérifie ces règles sur chaque pull request et indique la page, la question et la ligne en cause.

### Écriture

- Une affirmation chiffrée = une source (référence dans la bibliographie).
- En français : « numérique responsable », « écoconception », « RSE », « devoir de vigilance », espaces insécables avant `: ; ? !` laissées au rendu.
- Pas de donnée interne d'entreprise, de nom de client ni d'information confidentielle : le dépôt est public.

## 4. Relecture et validation

```
proposition (issue ou pull request) → relecture (≥ 1 membre du groupe de travail) → fusion → publication automatique
```

- Un relecteur suffit pour fusionner une correction de forme.
- Une modification de **critère, priorité ou pondération** est une évolution de méthode : elle est discutée dans l'issue et validée par le groupe de travail avant fusion. Elle entre dans la prochaine version publiée (voir `CHANGELOG.md`).
- Les relecteurs par défaut sont définis dans `.github/CODEOWNERS`.

## 5. Travailler en local (facultatif)

Prérequis : Python 3.11+, [pandoc](https://pandoc.org) ≥ 3.12 et [Typst](https://typst.app) ≥ 0.15 (versions utilisées par la CI).

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
make check   # cohérence de la grille
make site    # données, Excel, PDF puis site (dans site/)
make serve   # aperçu sur http://127.0.0.1:8000
```

## 6. Pour les mainteneurs

- GitHub Pages est configuré en mode « GitHub Actions » (Settings → Pages → Source). À refaire si le dépôt est recréé ou forké.
- Publier une version : mettre à jour `version` dans `CITATION.cff` (source unique, reprise dans les PDF et les classeurs), `CHANGELOG.md` et la page « À propos », puis pousser l'étiquette correspondante, par exemple `git tag v1.3 && git push origin v1.3`. La release vérifie que l'étiquette et la version concordent.

## 7. Licence de vos contributions

En contribuant, vous acceptez que votre contribution soit publiée sous la licence du projet : **CC BY-SA 4.0** pour le contenu, **MIT** pour les scripts. Les contributeurs sont crédités dans `CONTRIBUTORS.md` et sur la page « À propos » du guide.
