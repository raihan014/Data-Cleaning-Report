from pathlib import Path
import pandas as pd

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent
RAW_DATA_PATH = PROJECT_DIR / "data" / "raw" / "adult.data"
CLEANED_DATA_PATH = PROJECT_DIR / "data" / "processed" / "adult_cleaned.csv"
OUTPUT_DIR = PROJECT_DIR / "reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Column names for the original dataset
COLUMN_NAMES = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country",
    "income",
]

# Load original and cleaned datasets
raw_df = pd.read_csv(
    RAW_DATA_PATH,
    header=None,
    names=COLUMN_NAMES,
    skipinitialspace=True,
    na_values=["?"],
)

cleaned_df = pd.read_csv(CLEANED_DATA_PATH)

# Calculate data-quality metrics
summary = pd.DataFrame({
    "Metric": [
        "Number of rows",
        "Number of columns",
        "Missing cells",
        "Duplicate rows",
    ],
    "Before Cleaning": [
        len(raw_df),
        raw_df.shape[1],
        int(raw_df.isnull().sum().sum()),
        int(raw_df.duplicated().sum()),
    ],
    "After Cleaning": [
        len(cleaned_df),
        cleaned_df.shape[1],
        int(cleaned_df.isnull().sum().sum()),
        int(cleaned_df.duplicated().sum()),
    ],
})

print("Before and After Cleaning data comparison report")
print(summary.to_string(index=False))

# Save the comparison table
output_path = OUTPUT_DIR / "before_after_comparison.csv"
summary.to_csv(output_path, index=False)

print(f"\nComparison report saved to: {output_path}")


# Before-and-after numerical statistical profile

import os
import pandas as pd

column_names = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week",
    "native_country", "income"
]

raw_path = "data/raw/adult.data"
cleaned_path = "data/processed/adult_cleaned.csv"
report_path = "reports/numeric_profile_comparison.csv"

# Load the original dataset using the same missing-value rules
raw_df = pd.read_csv(
    raw_path,
    header=None,
    names=column_names,
    skipinitialspace=True,
    na_values=["?"]
)

cleaned_df = pd.read_csv(cleaned_path)

# Select numerical columns available in both datasets
numeric_columns = raw_df.select_dtypes(include="number").columns.intersection(
    cleaned_df.select_dtypes(include="number").columns
)

# Calculate descriptive statistics
before_stats = raw_df[numeric_columns].describe().T
after_stats = cleaned_df[numeric_columns].describe().T

statistics = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]

# Create a side-by-side comparison
profile_rows = []

for column in numeric_columns:
    for statistic in statistics:
        profile_rows.append({
            "Column": column,
            "Statistic": statistic,
            "Before Cleaning": before_stats.loc[column, statistic],
            "After Cleaning": after_stats.loc[column, statistic]
        })

profile_df = pd.DataFrame(profile_rows)

os.makedirs("reports", exist_ok=True)
profile_df.to_csv(report_path, index=False)

print("\nNumerical statistical profile comparison saved!")
print(f"File: {report_path}")
print(profile_df.head(16).to_string(index=False))
