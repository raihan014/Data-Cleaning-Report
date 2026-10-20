from pathlib import Path
import pandas as pd

# Define the project path
PROJECT_DIR = Path(__file__).resolve().parent

DATA_PATH = PROJECT_DIR / "data" / "raw" / "adult.data"
OUTPUT_DIR = PROJECT_DIR / "outputs"

# Create the outputs folder if it does not exist.
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Define the column names
COLUMN_NAMES = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income",
]

# Load the dataset 
df = pd.read_csv(
    DATA_PATH,
    header=None,
    names=COLUMN_NAMES,
    skipinitialspace=True,
    na_values=["?"],
)

# Inspect the dataset
print("Dataset Overview")

print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"Total missing cells: {int(df.isnull().sum().sum())}")
print(f"Exact duplicate rows: {int(df.duplicated().sum())}")

print("\nFirst 5 rows")
print(df.head().to_string(index=False))

print("\nData Types")
print(df.dtypes.to_string())

print("\nMissing Values")
print(df.isnull().sum().to_string())

print("\nDuplicate Rows")
print(f"Exact duplicate rows: {df.duplicated().sum()}")

print("\nNumerical Summary")
print(df.describe().round(2).to_string())

# Create a baseline data quality profile
missing_counts = df.isnull().sum()

quality_profile = pd.DataFrame({
    "column": df.columns,
    "data_type": [str(dtype) for dtype in df.dtypes],
    "missing_count": missing_counts.values,
    "missing_percentage": (
        missing_counts.values / len(df) * 100
    ).round(2),
    "unique_values": [
        df[column].nunique(dropna=True)
        for column in df.columns
    ],
})

# Save the column-level quality profile.
quality_path = OUTPUT_DIR / "baseline_quality.csv"

quality_profile.to_csv(
    quality_path,
    index=False,
)

# Save the numerical summary to a CSV file
numeric_summary = df.describe().T.round(2)

numeric_summary_path = (
    OUTPUT_DIR / "baseline_numeric_summary.csv"
)

numeric_summary.to_csv(numeric_summary_path)

# Save a baseline summary of the dataset
total_rows = len(df)
total_columns = len(df.columns)
total_missing = int(df.isnull().sum().sum())
total_duplicates = int(df.duplicated().sum())

baseline_summary = pd.DataFrame({
    "metric": [
        "total_rows",
        "total_columns",
        "total_missing_cells",
        "exact_duplicate_rows",
    ],
    "value": [
        total_rows,
        total_columns,
        total_missing,
        total_duplicates,
    ],
})

baseline_summary_path = OUTPUT_DIR / "baseline_summary.csv"

baseline_summary.to_csv(
    baseline_summary_path,
    index=False,
)

# Display the paths of the saved files
print("BASELINE AUDIT FILES SAVED")

print(f"Quality profile: {quality_path}")
print(f"Numerical summary: {numeric_summary_path}")
print(f"Baseline summary: {baseline_summary_path}")

print("\nInspection completed successfully.")

print("\n--------------------------------------------------------------------")

# Inspect the duplicate records
duplicate_rows = df[df.duplicated(keep=False)]

print("Duplicate Records Overview")

print(f"Rows involved in duplicate groups: {len(duplicate_rows)}")
print(duplicate_rows.head(10).to_string(index=False))
