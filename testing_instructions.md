# Testing instructions

1. Create/activate a Python 3.10+ virtual environment.
2. Run `pip install -r requirements.txt`.
3. Run `streamlit run app.py`.
4. Confirm the overview says AWAITING SURVEY DATA, 15 ads are searchable, charts are empty/pending, and downloads work.
5. For real response analysis, import genuine rows to `data/survey_responses.csv` using columns shown in the app. Keep synthetic test data separate and never combine it with genuine observations.
6. Run `python -m unittest discover -s tests` for basic validation.

This package was checked for file-generation integrity and syntax; live Google Forms/Sheets integrations and actual survey collection were not tested.


`data/SYNTHETIC_TEST_ONLY_responses.csv` is an explicitly synthetic, non-real fixture for exercising parsing/formula paths. It is excluded from the app and is not survey evidence. Never import it into genuine survey response analysis.
