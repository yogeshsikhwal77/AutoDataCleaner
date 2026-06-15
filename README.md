# AutoDataCleaner

An automated, modular Data Cleaning and Preprocessing Pipeline built in Python. 

In real-world data science, up to 80% of time is spent cleaning data. **AutoDataCleaner** streamlines this by taking raw, messy data and systematically transforming it into a mathematically sound, machine-learning-ready dataset. 

## 🎯 Project Target
**Full automated Data Cleaning Pipeline script.**

---

## 📂 Repository Structure

```text
AutoDataCleaner/
│
├── data/
│   ├── raw/                 # Drop dirty .csv files here (e.g., sample.csv)
│   └── processed/           # Cleaned, split datasets are exported here
│
├── src/
│   ├── __init__.py
│   ├── inspection.py        # EDA, Imputation, Outliers, Deduplication
│   ├── transformations.py   # Encodings, Scaling, Skewness, Binning
│   ├── structuring.py       # Datetime parsing, Interactions, Splits
│   └── pipeline.py          # The main orchestrator script
│
├── requirements.txt         # Dependencies (pandas, scikit-learn, etc.)
├── .gitignore               # Ignores __pycache__, venv, and raw data
└── README.md                # Project documentation