# ============================================================
# READYNEST INTERNSHIP - WEEK 1 TASK
# Create Summary Dataset for Looker Studio
# (Lighter file - faster dashboard)
# ============================================================

import pandas as pd

print("📥 Loading cleaned data...")
df = pd.read_csv("cleaned_data.csv", parse_dates=['InvoiceDate'])
print(f"✅ Loaded: {df.shape[0]:,} rows")

# ------------------------------------------------------------
# 1. MONTHLY REVENUE SUMMARY
# ------------------------------------------------------------
monthly = df.groupby(df['InvoiceDate'].dt.to_period('M')).agg(
    TotalSales=('TotalSales', 'sum'),
    TotalOrders=('InvoiceNo', 'nunique'),
    TotalCustomers=('CustomerID', 'nunique')
).reset_index()
monthly['InvoiceDate'] = monthly['InvoiceDate'].astype(str)
monthly.to_csv("summary_monthly.csv", index=False)
print("💾 Saved: summary_monthly.csv")

# ------------------------------------------------------------
# 2. COUNTRY SUMMARY
# ------------------------------------------------------------
country = df.groupby('Country').agg(
    TotalSales=('TotalSales', 'sum'),
    TotalOrders=('InvoiceNo', 'nunique'),
    TotalCustomers=('CustomerID', 'nunique')
).reset_index().sort_values('TotalSales', ascending=False)
country.to_csv("summary_country.csv", index=False)
print("💾 Saved: summary_country.csv")

# ------------------------------------------------------------
# 3. TOP 10 PRODUCTS SUMMARY
# ------------------------------------------------------------
products = df.groupby('Description').agg(
    TotalSales=('TotalSales', 'sum'),
    TotalQuantity=('Quantity', 'sum')
).reset_index().sort_values('TotalSales', ascending=False).head(10)
products.to_csv("summary_products.csv", index=False)
print("💾 Saved: summary_products.csv")

# ------------------------------------------------------------
# 4. HOUR SUMMARY
# ------------------------------------------------------------
hourly = df.groupby('Hour').agg(
    TotalSales=('TotalSales', 'sum'),
    TotalOrders=('InvoiceNo', 'nunique')
).reset_index()
hourly.to_csv("summary_hourly.csv", index=False)
print("💾 Saved: summary_hourly.csv")

# ------------------------------------------------------------
# 5. DAY OF WEEK SUMMARY
# ------------------------------------------------------------
daily = df.groupby('Day').agg(
    TotalSales=('TotalSales', 'sum'),
    TotalOrders=('InvoiceNo', 'nunique')
).reset_index()
daily.to_csv("summary_daily.csv", index=False)
print("💾 Saved: summary_daily.csv")

# ------------------------------------------------------------
# 6. OVERALL KPIs
# ------------------------------------------------------------
print("\n" + "="*40)
print("📊 OVERALL KPIs")
print("="*40)
print(f"💰 Total Revenue   : £{df['TotalSales'].sum():,.2f}")
print(f"📦 Total Orders    : {df['InvoiceNo'].nunique():,}")
print(f"👥 Unique Customers: {df['CustomerID'].nunique():,}")
print(f"🌍 Countries       : {df['Country'].nunique()}")
print("\n✅ All summary files created!")
print("📁 Upload these to Looker Studio instead of cleaned_data.csv")
