from pathlib import Path
import pandas as pd

# Locate the saved cleaned dataset.
PROJECT_DIR = Path(__file__).resolve().parent

CLEANED_DATA_PATH = (
    PROJECT_DIR / "data" / "processed" / "adult_cleaned.csv"
)

# Confirm that the file exists before reading it.
if not CLEANED_DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found: {CLEANED_DATA_PATH}"
    )

# Load the saved CSV independently.
cleaned_df = pd.read_csv(CLEANED_DATA_PATH)

# Check the saved file.
print("Clean Dataset Verification")
print(f"File exists: {CLEANED_DATA_PATH.exists()}")
print(f"Rows: {cleaned_df.shape[0]}")
print(f"Columns: {cleaned_df.shape[1]}")
print(f"Missing cells: {cleaned_df.isnull().sum().sum()}")
print(f"Duplicate rows: {cleaned_df.duplicated().sum()}")

print("\nColumn names:")
print(cleaned_df.columns.tolist())

print("\nFirst five records:")
print(cleaned_df.head().to_string(index=False))

# Basic verification assertions.
assert cleaned_df.shape == (32537, 15), "Unexpected dataset dimensions"
assert cleaned_df.isnull().sum().sum() == 0, "Missing values remain"
assert cleaned_df.duplicated().sum() == 0, "Duplicate rows remain"

print("\nAll verification checks passed!")
