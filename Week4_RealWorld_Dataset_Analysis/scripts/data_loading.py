import pandas as pd
from pathlib import Path

# -----------------------------
# Load Dataset
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR \ "data" \ "raw" \ "air_quality_india_city_day.csv"

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Basic Inspection
# -----------------------------
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())
