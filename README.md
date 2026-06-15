# AutoDataCleaner

An automated, modular Data Cleaning and Preprocessing Pipeline built in Python. 

In real-world data science, up to 80% of time is spent cleaning data. **AutoDataCleaner** streamlines this by taking raw, messy data and systematically transforming it into a mathematically sound, machine-learning-ready dataset. 

## Project Target
**Full automated Data Cleaning Pipeline script**.

---

## Features

The pipeline is divided into several modular scripts to handle specific parts of the data cleaning process:

* **Data Inspection & Cleaning (`src/inspection.py`)**:
  * Automatically detects numerical and categorical columns.
  * Drops duplicate rows.
  * Handles missing values by imputing the median for numerical columns and the mode for categorical columns.
  * Detects and caps outliers using the Interquartile Range (IQR) method.
  * Plots histograms to visualize data distribution.

* **Data Transformations (`src/transformations.py`)**:
  * Encodes categorical variables using One-Hot Encoding (for < 10 unique values) or Ordinal Encoding (factorizing for >= 10 unique values).
  * Handles skewness by applying a Log1p transformation to highly skewed numerical features.
  * Scales numerical features using scikit-learn's `StandardScaler`.

* **Data Structuring (`src/structuring.py`)**:
  * Parses temporal/cyclic features (like months) into cyclic sine and cosine waves.
  * Synthesizes new features by optionally adding or multiplying existing columns.
  * Automatically splits the dataset into training and testing sets (default 80/20 split).

* **Pipeline Orchestration (`src/pipeline.py`)**:
  * Combines all inspection, transformation, and structuring steps into a single executable workflow.
  * Exports the cleaned `X_train`, `X_test`, `y_train`, and `y_test` datasets to the `data/processed/` directory as ready-to-use CSV files.

---

## Repository Structure

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