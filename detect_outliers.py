from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent
CLEANED_DATA_PATH = PROJECT_DIR / "data" / "processed" / "adult_cleaned.csv"
REPORTS_DIR = PROJECT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv(CLEANED_DATA_PATH)

# Numerical columns to check
numeric_columns = df.select_dtypes(include="number").columns

outlier_results = []

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outlier_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
    outlier_count = int(outlier_mask.sum())

    outlier_results.append({
        "Column": column,
        "Q1": round(Q1, 2),
        "Q3": round(Q3, 2),
        "IQR": round(IQR, 2),
        "Lower Bound": round(lower_bound, 2),
        "Upper Bound": round(upper_bound, 2),
        "Outlier Count": outlier_count,
        "Outlier Percentage": round(outlier_count / len(df) * 100, 2),
    })

# Create and display the report
outlier_report = pd.DataFrame(outlier_results)

print("IQR Outlier Detection Report")
print(outlier_report.to_string(index=False))

# Save the results
output_path = REPORTS_DIR / "iqr_outlier_report.csv"
outlier_report.to_csv(output_path, index=False)

print(f"\nOutlier report saved to: {output_path}")
