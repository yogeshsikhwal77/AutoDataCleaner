# 🚀 AutoDataCleaner

<p align="center">
  <b>Automated Data Cleaning & Preprocessing Pipeline for Machine Learning</b>
  <br><br>
  Transform messy datasets into clean, structured, ML-ready data with a single pipeline.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/Pandas-Latest-green" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange" />
  <img src="https://img.shields.io/badge/License-MIT-red" />
</p>

---

## 📖 Overview

In real-world machine learning projects, data preparation often consumes more time than model development itself.

**AutoDataCleaner** is a modular preprocessing framework that automates the most common data cleaning tasks including:

✅ Missing Value Handling
✅ Duplicate Removal
✅ Outlier Detection
✅ Feature Encoding
✅ Feature Scaling
✅ Skewness Correction
✅ Feature Engineering
✅ Train-Test Splitting

The goal is simple:

> **Drop in a messy dataset and get back a machine-learning-ready dataset.**

---

## ✨ Features

### 🔍 Data Inspection & Cleaning

**Module:** `src/inspection.py`

* Automatic Numerical & Categorical Column Detection
* Missing Value Imputation

  * Median → Numerical Features
  * Mode → Categorical Features
* Duplicate Record Removal
* IQR-Based Outlier Detection & Capping
* Distribution Visualization using Histograms

---

### 🔄 Data Transformation

**Module:** `src/transformations.py`

* One-Hot Encoding for low-cardinality features
* Ordinal Encoding for high-cardinality features
* Log Transformation (`log1p`) for skewed distributions
* Standardization using `StandardScaler`

---

### 🧠 Data Structuring

**Module:** `src/structuring.py`

* Cyclic Feature Engineering
* Datetime Parsing
* Sine/Cosine Feature Generation
* Interaction Feature Creation
* Automatic Train/Test Split

---

### ⚙️ Pipeline Orchestration

**Module:** `src/pipeline.py`

* Executes all preprocessing stages automatically
* Generates clean train/test datasets
* Produces preprocessing reports
* Saves outputs in CSV format

---

## 🏗️ Project Architecture

```text
Raw Dataset
      │
      ▼
┌────────────────────┐
│ Data Inspection    │
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Missing Values     │
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Duplicate Removal  │
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Outlier Handling   │
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Feature Encoding   │
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Scaling & Skewness │
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Feature Engineering│
└────────────────────┘
      │
      ▼
┌────────────────────┐
│ Train/Test Split   │
└────────────────────┘
      │
      ▼
Machine Learning Ready Data
```

---

## 📂 Repository Structure

```text
AutoDataCleaner/
│
├── data/
│   ├── raw/
│   │   └── train.csv
│   │
│   └── processed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── src/
│   ├── __init__.py
│   ├── inspection.py
│   ├── transformations.py
│   ├── structuring.py
│   └── pipeline.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚡ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yogeshsikhwal77/AutoDataCleaner.git
cd AutoDataCleaner
```

### 2️⃣ Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Step 1: Add Dataset

Place your dataset inside:

```text
data/raw/
```

Example:

```text
data/raw/train.csv
```

---

### Step 2: Configure Pipeline

Edit `src/pipeline.py`

```python
if __name__ == "__main__":

    file_path = "data/raw/train.csv"
    target_col = "SalePrice"
    months_cols = ["MonthSold"]

    run_pipeline(
        file_path=file_path,
        target_col=target_col,
        months_cols=months_cols
    )
```

---

### Step 3: Run Pipeline

```bash
python src/pipeline.py
```

---

### Step 4: Get Processed Data

Generated files:

```text
data/processed/

├── X_train.csv
├── X_test.csv
├── y_train.csv
└── y_test.csv
```

---

## 📊 Example Output

| File        | Description       |
| ----------- | ----------------- |
| X_train.csv | Training Features |
| X_test.csv  | Testing Features  |
| y_train.csv | Training Labels   |
| y_test.csv  | Testing Labels    |

Additionally:

```text
cleaning_report.md
```

contains a detailed preprocessing summary.

---

## 📦 Dependencies

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
scipy
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Enhancements

* KNN Imputation
* Iterative Imputation
* Automatic Feature Selection
* Data Leakage Detection
* YAML Configuration Support
* Hyperparameter-Aware Preprocessing
* Excel & Parquet Support
* Pipeline Serialization
* Streamlit Web Interface
* Automated EDA Report Generation

---

## 🤝 Contributing

Contributions are welcome!

Feel free to:

* Fork the repository
* Create a feature branch
* Submit a pull request
* Report bugs or improvements

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Yogesh Sikhwal**

Machine Learning • Deep Learning • Data Science

GitHub: https://github.com/yogeshsikhwal77

---

<p align="center">
⭐ If you found this project useful, consider starring the repository!
</p>
