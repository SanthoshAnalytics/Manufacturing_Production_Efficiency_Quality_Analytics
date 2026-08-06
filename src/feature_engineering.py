import numpy as np
import pandas as pd


# ==========================================================
# Feature Engineering
# ==========================================================

def create_features(df):
    """
    Create business features for manufacturing analytics.
    """

    df = df.copy()

    # ------------------------------------------------------
    # Production Efficiency (%)
    # ------------------------------------------------------
    if {"ProductionVolume", "ProductionCost"}.issubset(df.columns):
        df["Production_Efficiency"] = (
            df["ProductionVolume"] / df["ProductionCost"]
        ).round(2)

    # ------------------------------------------------------
    # Defect Percentage (%)
    # ------------------------------------------------------
    if {"DefectRate"}.issubset(df.columns):
        df["Defect_Percentage"] = (
            df["DefectRate"] * 100
        ).round(2)

    # ------------------------------------------------------
    # Machine Utilization
    # ------------------------------------------------------
    if {"ProductionVolume", "EnergyConsumption"}.issubset(df.columns):
        df["Machine_Utilization"] = (
            df["ProductionVolume"] /
            df["EnergyConsumption"]
        ).round(2)

    # ------------------------------------------------------
    # Productivity Score
    # ------------------------------------------------------
    if {"ProductionVolume", "QualityScore"}.issubset(df.columns):
        df["Productivity_Score"] = (
            df["ProductionVolume"] *
            df["QualityScore"]
        ).round(2)

    # ------------------------------------------------------
    # Machine Health
    # ------------------------------------------------------
    if "MaintenanceHours" in df.columns:

        conditions = [
            df["MaintenanceHours"] <= 10,
            (df["MaintenanceHours"] > 10) &
            (df["MaintenanceHours"] <= 30),
            df["MaintenanceHours"] > 30
        ]

        choices = [
            "Excellent",
            "Good",
            "Needs Maintenance"
        ]

        df["Machine_Health"] = np.select(
            conditions,
            choices,
            default="Unknown"
        )

    # ------------------------------------------------------
    # Risk Category
    # ------------------------------------------------------
    if "DefectRate" in df.columns:

        conditions = [
            df["DefectRate"] < 0.03,
            (df["DefectRate"] >= 0.03) &
            (df["DefectRate"] < 0.07),
            df["DefectRate"] >= 0.07
        ]

        choices = [
            "Low",
            "Medium",
            "High"
        ]

        df["Risk_Category"] = np.select(
            conditions,
            choices,
            default="Unknown"
        )

    print("✅ Feature Engineering Completed.")

    return df


# ==========================================================
# Save Engineered Dataset
# ==========================================================

def save_feature_dataset(df, path):

    df.to_csv(path, index=False)

    print(f"Dataset saved to:\n{path}")