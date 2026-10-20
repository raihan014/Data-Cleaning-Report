from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent

RAW_DATA_PATH = PROJECT_DIR / "data" / "raw" / "adult.data"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

# Create the processed-data folder if it does not exist.
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

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

# Load the raw dataset
df = pd.read_csv(
    RAW_DATA_PATH,
    header=None,
    names=COLUMN_NAMES,
    skipinitialspace=True,
    na_values=["?"],
)

# Validate the dataset
print("Raw dataset validation.")

print(f"Dataset loaded successfully: {RAW_DATA_PATH.exists()}")
print(f"Number of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing cells:", int(df.isnull().sum().sum()))
print("Exact duplicate rows:", int(df.duplicated().sum()))

print("\nFirst five records:")
print(df.head().to_string(index=False))

print("\nValidation completed.")

# Standardize whitespace in text columns

text_columns = df.select_dtypes(include=["str", "object"]).columns

for column in text_columns:
    df[column] = df[column].str.strip()

print("\nWhitespace standardization completed.")

print("\nSample categorical values after standardization:")
for column in ["workclass", "education", "occupation", "income"]:
    print(f"{column}: {df[column].dropna().unique()[:5].tolist()}")

# Handle the missing values

missing_columns = [
    "workclass",
    "occupation",
    "native_country",
]

print("\nMissing values before cleaning:")

for column in missing_columns:
    print(f"{column}: {df[column].isnull().sum()}")

# Replace missing values with an explicit category.
for column in missing_columns:
    df[column] = df[column].fillna("Unknown")

print("\nMissing values after cleaning:")

for column in missing_columns:
    print(f"{column}: {df[column].isnull().sum()}")

print("\nTotal missing cells remaining:", int(df.isnull().sum().sum()))


# Remove exact duplicate records from the dataset.

rows_before_deduplication = len(df)
duplicates_before_deduplication = int(df.duplicated().sum())

print("\nDuplicate analysis before removal:")
print(f"Rows before removal: {rows_before_deduplication}")
print(f"Exact duplicates found: {duplicates_before_deduplication}")

# Keep the first occurrence of each exact duplicate record.
df = df.drop_duplicates(keep="first").copy()

rows_after_deduplication = len(df)
rows_removed = rows_before_deduplication - rows_after_deduplication

print("\nDuplicate analysis after removal:")
print(f"Rows after removal: {rows_after_deduplication}")
print(f"Rows removed: {rows_removed}")
print(f"Remaining exact duplicates: {int(df.duplicated().sum())}")

# Check the Numerical Value
numeric_columns = [
    "age",
    "fnlwgt",
    "education_num",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
]

print("\nNumerical validation:")
print(df[numeric_columns].describe().round(2))

print("\nChecking basic numerical rules:")

print("Age below 17:", (df["age"] < 17).sum())
print("Age above 100:", (df["age"] > 100).sum())

print("Non-positive fnlwgt:", (df["fnlwgt"] <= 0).sum())
print("Education number outside 1-16:",(~df["education_num"].between(1, 16)).sum(),)

print("Negative capital gain:", (df["capital_gain"] < 0).sum())
print("Negative capital loss:", (df["capital_loss"] < 0).sum())

print("Hours below 1:", (df["hours_per_week"] < 1).sum())
print("Hours above 168:", (df["hours_per_week"] > 168).sum())

# Save the clean dataset

CLEANED_DATA_PATH = PROCESSED_DIR / "adult_cleaned.csv"

df.to_csv(CLEANED_DATA_PATH, index=False)

print("\nCleaned dataset saved successfully.")
print(f"File location: {CLEANED_DATA_PATH}")
print(f"Final number of rows: {df.shape[0]}")
print(f"Final number of columns: {df.shape[1]}")
print(f"Missing cells remaining: {df.isnull().sum().sum()}")
print(f"Duplicate rows remaining: {df.duplicated().sum()}")
