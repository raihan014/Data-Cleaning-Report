
# Data Quality Audit Report

## 1. Project Overview

**Project:** CodeNova Data Science Internship — Batch 01  
**Task:** Data Cleaning Report  
**Dataset:** Adult Census Income Dataset  
**Tools:** Python, Pandas, NumPy, and the IQR method

### Objective

The objective of this project is to inspect a raw dataset, identify missing values and duplicate records, detect potential outliers, validate data, and produce a clean dataset while preserving the original source file.

## 2. Dataset Overview

The original dataset contains 32,561 rows and 15 columns. It includes demographic, education, employment, financial, and income information. 

Dataset link: https://archive.ics.uci.edu/dataset/2/adult

The raw dataset is stored in `data/raw/adult.data`. The cleaned dataset is saved separately at `data/processed/adult_cleaned.csv`.

The original dataset was not modified during cleaning.

## 3. Initial Data Quality Assessment

The initial inspection identified the following issues:

| Data Quality Metric | Before Cleaning |
|---|---:|
| Total rows | 32,561 |
| Total columns | 15 |
| Missing cells | 4,262 |
| Exact duplicate rows | 24 |

Missing values were found in three columns:

| Column | Missing Values |
|---|---:|
| workclass | 1,836 |
| occupation | 1,843 |
| native_country | 583 |
| **Total** | **4,262** |

## 4. Data Cleaning Procedures

### 4.1 Handling Missing Values

Missing values were represented by `?` in the raw dataset. During import, these markers were converted to Pandas missing values.

The missing values in `workclass`, `occupation`, and `native_country` were replaced with the label `Unknown`.

**Justification:** These are categorical columns, and the original values cannot be reliably inferred from the available data. Using `Unknown` preserves the records without inventing information.

### 4.2 Standardizing Text Values

Leading and trailing whitespace was removed from text columns using Pandas string operations.

**Justification:** Unnecessary whitespace can cause inconsistent category labels and interfere with grouping and analysis.

### 4.3 Removing Duplicate Records

Exact duplicate rows were removed using Pandas `drop_duplicates()`, keeping the first occurrence.

| Metric | Result |
|---|---:|
| Rows before duplicate removal | 32,561 |
| Exact duplicate rows removed | 24 |
| Rows after duplicate removal | 32,537 |

**Justification:** Removing exact duplicate rows prevents identical records from being counted more than once. However, identical rows do not necessarily prove that the records belong to the same person.

### 4.4 Data Type and Validity Checks

The dataset was loaded using Pandas, and numerical columns were examined using descriptive statistics. Basic validity checks were also performed.

The checks covered age, `fnlwgt`, education number, capital gain, capital loss, and hours worked per week.

All nine implemented validity checks reported zero invalid records.

These results indicate that no values violated the specific validation rules defined for this project.

## 5. Statistical Outlier Detection

Potential outliers were identified using the Interquartile Range (IQR) method.

The IQR is calculated as:

IQR = Q3 - Q1

The lower and upper thresholds are:

- Lower bound = Q1 - 1.5 × IQR
- Upper bound = Q3 + 1.5 × IQR

Values outside these bounds were flagged as potential outliers.

| Column | Potential Outliers | Percentage |
|---|---:|---:|
| age | 142 | 0.44% |
| fnlwgt | 993 | 3.05% |
| education_num | 1,193 | 3.67% |
| capital_gain | 2,712 | 8.34% |
| capital_loss | 1,519 | 4.67% |
| hours_per_week | 9,002 | 27.67% |

### Outlier Treatment Decision

The IQR results were used to identify unusual values, not to automatically classify them as errors.

For `capital_gain` and `capital_loss`, the first and third quartiles are both zero. Consequently, the IQR is zero, and positive values are flagged by this method.

Potential outliers were retained because the current checks did not establish that these values were invalid. Removing or replacing legitimate observations could distort the dataset.

## 6. Before-and-After Comparison

| Metric | Before Cleaning | After Cleaning |
|---|---:|---:|
| Number of rows | 32,561 | 32,537 |
| Number of columns | 15 | 15 |
| Missing cells | 4,262 | 0 |
| Exact duplicate rows | 24 | 0 |

The final dataset contains 24 fewer rows than the original dataset. All identified missing cells were handled, and no exact duplicate rows remain.

### Numerical Statistical Profile Comparison

The numerical statistical profile was compared before and after cleaning using count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum for each numerical column.

The comparison is saved in `reports/numeric_profile_comparison.csv`. It helps assess how removing duplicate records affected the numerical distributions. Since the cleaning process did not remove potential outliers, those observations remain included in the statistical profile.

## 7. Validation Results

The following checks were performed on the cleaned dataset:

| Validation Rule | Invalid Records |
|---|---:|
| Age below 17 | 0 |
| Age above 100 | 0 |
| Non-positive fnlwgt | 0 |
| Education number below 1 | 0 |
| Education number above 16 | 0 |
| Negative capital gain | 0 |
| Negative capital loss | 0 |
| Hours per week below 1 | 0 |
| Hours per week above 168 | 0 |

The cleaned dataset was also reloaded from disk and verified. The verification confirmed 32,537 rows, 15 columns, zero missing cells, and zero duplicate rows.

## 8. Generated Reports and Files

| File | Purpose |
|---|---|
| `clean_data.py` | Cleans the dataset, handles missing values, removes exact duplicates, standardizes text values, and saves the processed output |
| `inspect_data.py` | Inspects the original dataset, including dimensions, missing values, duplicate records, data types, and numerical statistics |
| `verify_cleaned_data.py` | Verifies the saved cleaned dataset's dimensions, missing values, and duplicate records |
| `cleaning_summary.py` | Creates the before-and-after data quality comparison and numerical statistical profile |
| `detect_outliers.py` | Detects potential numerical outliers using the Interquartile Range (IQR) method |
| `validate_data.py` | Checks the defined data-validity rules and saves the validation results |
| `outputs/baseline_quality.csv` | Records column-level data types, missing-value counts, missing percentages, and unique-value counts for the original dataset |
| `outputs/baseline_numeric_summary.csv` | Contains numerical descriptive statistics for the original dataset |
| `outputs/baseline_summary.csv` | Summarizes the original dataset's row count, column count, missing cells, and duplicate rows |
| `reports/before_after_comparison.csv` | Compares row counts, column counts, missing cells, and duplicate rows before and after cleaning |
| `reports/numeric_profile_comparison.csv` | Compares numerical statistics before and after cleaning, including count, mean, standard deviation, minimum, quartiles, and maximum |
| `reports/iqr_outlier_report.csv` | Records potential outliers identified using the IQR method |
| `reports/data_validity_report.csv` | Records the results of the defined data-validity checks |
| `data/processed/adult_cleaned.csv` | Contains the cleaned dataset, saved separately from the original raw data |

## 9. Conclusion

The data-cleaning workflow successfully addressed the identified missing values, removed exact duplicate rows, standardized text fields, and generated statistical outlier and validity reports.

The final dataset contains 32,537 rows and 15 columns, with zero missing cells and zero exact duplicate rows. Potential outliers were retained because unusual values are not automatically invalid.

The cleaning process is implemented in Python scripts and produces separate output files, supporting reproducibility and review.

## 10. Limitations

- The `Unknown` label indicates unavailable information and does not recover the original missing values.
- IQR flags unusual observations but does not establish that they are erroneous.
- The validity checks cover the rules explicitly implemented in this project.
