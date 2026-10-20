
# CodeNova Data Science Internship — Task 2: Data Cleaning Report

## Project Overview

This project focuses on cleaning and validating the Adult Census Income dataset as part of the CodeNova Data Science Internship, Batch 01.

The goal is to identify and handle missing values, remove exact duplicate records, standardize text values, detect potential statistical outliers, and validate data quality.

The project uses Python and Pandas to create a reproducible data-cleaning workflow. The original dataset is preserved, and the cleaned dataset and quality reports are saved separately.

## Project Objectives

- Inspect the dataset's structure, columns, and data types.
- Identify missing values and duplicate records.
- Handle missing categorical values using the label `Unknown`.
- Standardize text values by removing leading and trailing whitespace.
- Detect potential outliers using the Interquartile Range (IQR) method.
- Validate numerical values against defined rules.
- Compare data quality before and after cleaning.
- Generate reports to document the cleaning process and results.

## Technology Stack

- **Python** — Main programming language.
- **Pandas** — Data loading, cleaning, validation, and analysis.
- **NumPy** — Numerical computing support.
- **Matplotlib / Seaborn** — Data visualization.
- **VS Code** — Development environment.

## Dataset Overview

The original dataset contains 32,561 rows and 15 columns. It includes demographic, education, employment, financial, and income information. 

Dataset link: https://archive.ics.uci.edu/dataset/2/adult

The raw dataset is stored in `data/raw/adult.data`. The cleaned dataset is saved separately at `data/processed/adult_cleaned.csv`.

The original dataset was not modified during cleaning.

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Visual Studio Code (recommended)

### 1. Clone or Download the Project

If the project is hosted on GitHub, clone it using:

```bash
git clone <github-repo-url>
cd Task-2
```

Alternatively, open the project folder directly in VS Code.

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Required Packages

```powershell
python -m pip install pandas numpy matplotlib seaborn missingno
```

### 4. Run the Data Cleaning Workflow

Run the scripts from the project root directory in the following order:

```powershell
python inspect_data.py
python clean_data.py
python verify_cleaned_data.py
python cleaning_summary.py
python detect_outliers.py
python validate_data.py
```

The cleaning script creates the processed dataset. The remaining scripts inspect, verify, compare, and validate the data and generate reports.

## Output Files
- `data/processed/adult_cleaned.csv` — Cleaned dataset.
- `reports/before_after_comparison.csv` — Before-and-after data quality metrics.
- `reports/numeric_profile_comparison.csv` — Compares numerical statistics before and after cleaning, including count, mean, standard deviation, minimum, quartiles, and maximum.
- `reports/iqr_outlier_report.csv` — Potential outliers identified using IQR.
- `reports/data_validity_report.csv` — Results of the defined data-validity checks.
- `Data_Quality_Audit.md` — Detailed explanation of the cleaning process and findings.


## Results

The data-cleaning workflow produced the following results:

| Metric | Before Cleaning | After Cleaning |
|---|---:|---:|
| Rows | 32,561 | 32,537 |
| Columns | 15 | 15 |
| Missing cells | 4,262 | 0 |
| Exact duplicate rows | 24 | 0 |

### Key Findings

- Missing values in `workclass`, `occupation`, and `native_country` were replaced with `Unknown`.
- Leading and trailing whitespace was removed from text columns.
- Twenty-four exact duplicate rows were removed, retaining the first occurrence.
- Six numerical columns were assessed using the IQR method.
- Nine basic data-validity checks reported zero invalid records.
- The cleaned dataset was reloaded and verified successfully.

### Outlier Handling

The IQR method identified potential outliers in numerical columns.

The outlier findings are documented in `reports/iqr_outlier_report.csv`.

## Limitations

- Missing values replaced with `Unknown` remain unknown; their original values cannot be recovered from the available data.
- IQR-based outlier detection can flag legitimate observations.
- The validation rules cover only the conditions explicitly checked by the scripts.
- Identical records do not necessarily represent the same individual.

## Reproducibility

The workflow uses Python scripts to perform data inspection, cleaning, verification, outlier detection, and validation.

The original dataset is preserved in `data/raw/`, while the cleaned dataset is saved separately in `data/processed/`.

## Author

**Marfi Hasan Raihan**

- **LinkedIn:** https://www.linkedin.com/in/marfi-hasan-raihan-8853a8283
- **Portfolio:** https://sites.google.com/view/raihanmarfi/home

*Prepared as part of the **CodeNova Data Science Internship — Batch 01**, Task 2.*
