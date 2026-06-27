# ============================================================
# READYNEST INTERNSHIP - WEEK 1 TASK
# Step 2: Data Cleaning
# Dataset: E-Commerce Online Retail (data.csv)
# ============================================================

import pandas as pd

FILE_PATH = "data.csv"   # <-- Same folder as this script

# ------------------------------------------------------------
# 1. LOAD
# ------------------------------------------------------------
print("📥 Loading dataset...")
df = pd.read_csv(FILE_PATH, encoding='latin1')
print(f"✅ Loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")

# ------------------------------------------------------------
# 2. BEFORE CLEANING SUMMARY
# ------------------------------------------------------------
print("\n" + "="*55)
print("🔍 BEFORE CLEANING")
print("="*55)
print(f"Total Rows       : {df.shape[0]:,}")
print(f"Missing Values   :\n{df.isnull().sum()}")
print(f"Duplicate Rows   : {df.duplicated().sum():,}")
print(f"Negative Quantity: {(df['Quantity'] < 0).sum():,}")
print(f"Negative Price   : {(df['UnitPrice'] <= 0).sum():,}")

# ------------------------------------------------------------
# 3. REMOVE DUPLICATES
# ------------------------------------------------------------
before = df.shape[0]
df.drop_duplicates(inplace=True)
print(f"\n🧹 Removed {before - df.shape[0]:,} duplicate rows")

# ------------------------------------------------------------
# 4. HANDLE MISSING VALUES
# ------------------------------------------------------------
# Drop rows where CustomerID is missing (can't analyze by customer)
before = df.shape[0]
df.dropna(subset=['CustomerID'], inplace=True)
print(f"🧹 Removed {before - df.shape[0]:,} rows with missing CustomerID")

# Fill missing Description with 'Unknown'
missing_desc = df['Description'].isnull().sum()
df['Description'].fillna('Unknown', inplace=True)
print(f"🧹 Filled {missing_desc} missing Description values with 'Unknown'")

# ------------------------------------------------------------
# 5. FIX DATA TYPES
# ------------------------------------------------------------
# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print("✅ InvoiceDate converted to datetime")

# Convert CustomerID to integer
df['CustomerID'] = df['CustomerID'].astype(int)
print("✅ CustomerID converted to int")

# ------------------------------------------------------------
# 6. REMOVE INVALID TRANSACTIONS
# ------------------------------------------------------------
# Remove cancelled orders (InvoiceNo starting with 'C')
before = df.shape[0]
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
print(f"🧹 Removed {before - df.shape[0]:,} cancelled orders (InvoiceNo starts with 'C')")

# Remove rows with negative or zero Quantity
before = df.shape[0]
df = df[df['Quantity'] > 0]
print(f"🧹 Removed {before - df.shape[0]:,} rows with Quantity ≤ 0")

# Remove rows with zero or negative UnitPrice
before = df.shape[0]
df = df[df['UnitPrice'] > 0]
print(f"🧹 Removed {before - df.shape[0]:,} rows with UnitPrice ≤ 0")

# ------------------------------------------------------------
# 7. ADD USEFUL COLUMNS
# ------------------------------------------------------------
# Total Sales = Quantity × UnitPrice
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Extract Year, Month, Day, Hour from InvoiceDate
df['Year']  = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Day']   = df['InvoiceDate'].dt.day_name()
df['Hour']  = df['InvoiceDate'].dt.hour

print("✅ Added columns: TotalSales, Year, Month, Day, Hour")

# ------------------------------------------------------------
# 8. STANDARDIZE TEXT
# ------------------------------------------------------------
df['Description'] = df['Description'].str.strip().str.upper()
df['Country']     = df['Country'].str.strip().str.title()
print("✅ Standardized text in Description and Country")

# ------------------------------------------------------------
# 9. AFTER CLEANING SUMMARY
# ------------------------------------------------------------
print("\n" + "="*55)
print("✅ AFTER CLEANING")
print("="*55)
print(f"Total Rows       : {df.shape[0]:,}")
print(f"Missing Values   : {df.isnull().sum().sum()}")
print(f"Duplicate Rows   : {df.duplicated().sum()}")
print(f"Columns          : {list(df.columns)}")
print(f"Date Range       : {df['InvoiceDate'].min()} → {df['InvoiceDate'].max()}")
print(f"Countries        : {df['Country'].nunique()} unique")
print(f"Total Revenue    : £{df['TotalSales'].sum():,.2f}")

# ------------------------------------------------------------
# 10. SAVE CLEANED DATASET
# ------------------------------------------------------------
df.to_csv("cleaned_data.csv", index=False)
print("\n💾 Cleaned dataset saved as: cleaned_data.csv")
print("✅ Step 2 Complete! Proceed to step3_eda.py")
