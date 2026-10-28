# CAPSTONE 21 — AI Product Description and Ad Copy A/B Evaluation

A beginner-friendly project comparing three prompting styles for the fictional EcoSip Smart Bottle. **Status: AWAITING SURVEY DATA.** No participants or results have been fabricated; actual sample size is 0 and no winning style is declared.

## Contents
- `app.py`: Streamlit dashboard (8 pages)
- `data/ad_variants.csv`: all 15 generated ad variants
- `data/survey_responses_template.csv`: blank response template
- `eco_capstone.xlsx`: formulas, sheets, charts
- `docs/`: survey method, prompts, verification, before/after, imports, outline, demo, testing
- `assets/ad_creative.png`: social creative if image generation completed
- `summary.pdf`: one-page project summary

## Run locally
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Survey and analysis
Follow `docs/survey_methodology.md`. Enter only genuine responses in `data/survey_responses.csv`; never mix synthetic test rows into it. The dashboard does not declare a winner until actual responses exist. Minimum target: 20 genuine volunteers; disclose any shortfall.

## GitHub upload
Create a new repository on GitHub, then from this folder: `git init`, `git add .`, `git commit -m "Initial capstone project"`, `git branch -M main`, `git remote add origin <your-repository-URL>`, `git push -u origin main`. Do not commit names, emails, or identifiable survey data.

## Limitations
Google Forms/Sheets integration was not connected or tested. Workbook formulas and charts are local templates. No external verification, human participant research, or real response analysis has yet occurred.


A separate `data/SYNTHETIC_TEST_ONLY_responses.csv` file exists only for pipeline tests; it is conspicuously labeled and never loaded by the app or counted as genuine data.
