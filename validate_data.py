from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent
CLEANED_DATA_PATH = PROJECT_DIR / "data" / "processed" / "adult_cleaned.csv"
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(CLEANED_DATA_PATH)

# Define basic validity checks
checks = {
    "Age below 17": df["age"] < 17,
    "Age above 100": df["age"] > 100,
    "Non-positive fnlwgt": df["fnlwgt"] <= 0,
    "Education number below 1": df["education_num"] < 1,
    "Education number above 16": df["education_num"] > 16,
    "Negative capital gain": df["capital_gain"] < 0,
    "Negative capital loss": df["capital_loss"] < 0,
    "Hours per week below 1": df["hours_per_week"] < 1,
    "Hours per week above 168": df["hours_per_week"] > 168,
}

# Count violations for each rule
results = []

for check_name, condition in checks.items():
    results.append({
        "Validation Check": check_name,
        "Invalid Records": int(condition.sum()),
        "Status": "PASS" if not condition.any() else "REVIEW REQUIRED",
    })

validation_report = pd.DataFrame(results)

print("Data Validity Report")
print(validation_report.to_string(index=False))

# Save report
output_path = REPORTS_DIR / "data_validity_report.csv"
validation_report.to_csv(output_path, index=False)

print(f"\nValidation report saved to: {output_path}")
