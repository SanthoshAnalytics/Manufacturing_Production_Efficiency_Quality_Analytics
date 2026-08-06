import pandas as pd
import numpy as np
from scipy import stats

print("✅ data_cleaning.py Loaded")
def clean_dataset(df):
    """
    Perform basic data cleaning.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with all missing values
    df = df.dropna(how="all")

    return df

# ==========================================================
# Detect Outliers using IQR
# ==========================================================

def detect_outliers_iqr(df):

    print("\n" + "=" * 60)
    print("OUTLIER DETECTION (IQR)")
    print("=" * 60)

    numeric_columns = df.select_dtypes(include="number").columns

    outlier_summary = {}

    for column in numeric_columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[(df[column] < lower) | (df[column] > upper)]

        outlier_summary[column] = len(outliers)

    return pd.DataFrame(
        outlier_summary.items(),
        columns=["Column", "Outliers"]
    )
    
    # ==========================================================
# Remove Outliers using IQR
# ==========================================================

def remove_outliers_iqr(df):

    numeric_columns = df.select_dtypes(include="number").columns

    cleaned_df = df.copy()

    for column in numeric_columns:

        Q1 = cleaned_df[column].quantile(0.25)
        Q3 = cleaned_df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        cleaned_df = cleaned_df[
            (cleaned_df[column] >= lower) &
            (cleaned_df[column] <= upper)
        ]

    return cleaned_df

# ==========================================================
# Detect Outliers using Z-Score
# ==========================================================

def detect_outliers_zscore(df):

    numeric_columns = df.select_dtypes(include="number").columns

    z_scores = np.abs(stats.zscore(df[numeric_columns]))

    outliers = (z_scores > 3).sum(axis=0)

    return pd.DataFrame({

        "Column": numeric_columns,
        "Outliers": outliers

    })