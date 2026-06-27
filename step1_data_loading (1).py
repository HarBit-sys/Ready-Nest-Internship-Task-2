# ============================================================
# READYNEST INTERNSHIP - WEEK 1 TASK
# Step 1: Data Loading
# Dataset: E-Commerce Online Retail (data.csv)
# ============================================================

import pandas as pd
import os

# ------------------------------------------------------------
# SET YOUR FILE PATH
# ------------------------------------------------------------
FILE_PATH = "data.csv"   # <-- Make sure data.csv is in the same folder

# ------------------------------------------------------------
# LOAD THE DATASET
# ------------------------------------------------------------
def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return None
    try:
        df = pd.read_csv(filepath, encoding='utf-8')
        print(f"✅ File loaded successfully!")
        return df
    except UnicodeDecodeError:
        print("⚠️  Retrying with latin-1 encoding...")
        df = pd.read_csv(filepath, encoding='latin-1')
        print(f"✅ File loaded with latin-1 encoding!")
        return df

# ------------------------------------------------------------
# BASIC EXPLORATION
# ------------------------------------------------------------
def explore_data(df):
    print("\n" + "="*55)
    print("📋  DATASET OVERVIEW — E-Commerce Online Retail")
    print("="*55)

    print(f"\n🔢  Shape         : {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"\n📌  Columns       : {list(df.columns)}")
    print(f"\n🔍  Data Types:\n{df.dtypes}")
    print(f"\n👀  First 5 Rows:\n{df.head()}")
    print(f"\n📊  Basic Statistics:\n{df.describe(include='all')}")

    missing = df.isnull().sum()
    print(f"\n❓  Missing Values:")
    print(missing[missing > 0] if missing.sum() > 0 else "✅ No missing values!")

    print(f"\n🔁  Duplicate Rows : {df.duplicated().sum():,}")
    print(f"\n🌍  Countries      : {df['Country'].nunique()} unique")
    print(f"🗓️   Date Range     : {df['InvoiceDate'].min()} → {df['InvoiceDate'].max()}")

    print("\n" + "="*55)
    print("✅  Step 1 Complete! Proceed to step2_data_cleaning.py")
    print("="*55)

# ------------------------------------------------------------
# RUN
# ------------------------------------------------------------
if __name__ == "__main__":
    df = load_data(FILE_PATH)
    if df is not None:
        explore_data(df)
