# Chaîne de publication locale. Prérequis : Python 3.11+, pandoc >= 3.12, typst >= 0.15.
# La même chaîne tourne dans GitHub Actions (.github/workflows/).

PYTHON ?= python3
OUT := docs/assets/downloads

.PHONY: all check data xlsx pdf llms site serve clean

all: check data xlsx pdf llms site

check:      ## Cohérence de la grille (totaux, parité FR/EN)
	$(PYTHON) scripts/guide.py check

data:       ## Grille en JSON et CSV
	$(PYTHON) scripts/guide.py json $(OUT)

xlsx:       ## Grille d'évaluation et questionnaire Excel
	$(PYTHON) scripts/build_xlsx.py $(OUT)

pdf:        ## Guides PDF français et anglais
	$(PYTHON) scripts/build_pdf.py $(OUT)

llms:       ## llms.txt et llms-full.txt pour les moteurs génératifs
	$(PYTHON) scripts/build_llms.py docs

site: data xlsx pdf llms  ## Site bilingue (les téléchargements doivent exister : build strict)
	mkdocs build --strict

serve: data xlsx pdf llms
	mkdocs serve

clean:
	rm -rf site build $(OUT) docs/llms.txt docs/llms-full.txt
