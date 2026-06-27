# ============================================================
# READYNEST INTERNSHIP - WEEK 1 TASK
# Step 3: Descriptive Statistics + EDA
# Dataset: cleaned_data.csv (output from step2_data_cleaning.py)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 5)
plt.rcParams['font.size'] = 12

# ------------------------------------------------------------
# 1. LOAD CLEANED DATA
# ------------------------------------------------------------
print("📥 Loading cleaned dataset...")
df = pd.read_csv("cleaned_data.csv", parse_dates=['InvoiceDate'])
print(f"✅ Loaded: {df.shape[0]:,} rows × {df.shape[1]} columns\n")

# ------------------------------------------------------------
# 2. DESCRIPTIVE STATISTICS
# ------------------------------------------------------------
print("="*55)
print("📊 DESCRIPTIVE STATISTICS")
print("="*55)

stats = df[['Quantity', 'UnitPrice', 'TotalSales']].describe()
print(stats)

print(f"\n💰 Total Revenue       : £{df['TotalSales'].sum():,.2f}")
print(f"📦 Total Orders        : {df['InvoiceNo'].nunique():,}")
print(f"👥 Unique Customers    : {df['CustomerID'].nunique():,}")
print(f"🛍️  Unique Products     : {df['StockCode'].nunique():,}")
print(f"🌍 Countries Served    : {df['Country'].nunique()}")
print(f"📅 Date Range          : {df['InvoiceDate'].min().date()} → {df['InvoiceDate'].max().date()}")

# ------------------------------------------------------------
# 3. UNIVARIATE ANALYSIS
# ------------------------------------------------------------
print("\n📈 Generating Univariate Analysis charts...")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Univariate Analysis", fontsize=16, fontweight='bold')

# Histogram - Quantity
axes[0].hist(df['Quantity'].clip(upper=50), bins=40, color='steelblue', edgecolor='white')
axes[0].set_title("Distribution of Quantity")
axes[0].set_xlabel("Quantity (clipped at 50)")
axes[0].set_ylabel("Frequency")

# Histogram - UnitPrice
axes[1].hist(df['UnitPrice'].clip(upper=20), bins=40, color='coral', edgecolor='white')
axes[1].set_title("Distribution of Unit Price")
axes[1].set_xlabel("Unit Price (clipped at £20)")
axes[1].set_ylabel("Frequency")

# Boxplot - TotalSales
axes[2].boxplot(df['TotalSales'].clip(upper=500), patch_artist=True,
                boxprops=dict(facecolor='mediumseagreen', color='black'))
axes[2].set_title("Boxplot of Total Sales")
axes[2].set_ylabel("Total Sales (clipped at £500)")

plt.tight_layout()
plt.savefig("chart1_univariate.png", dpi=150)
plt.show()
print("💾 Saved: chart1_univariate.png")

# ------------------------------------------------------------
# 4. TOP 10 ANALYSIS
# ------------------------------------------------------------
print("\n🏆 Generating Top 10 charts...")

fig, axes = plt.subplots(1, 2, figsize=(18, 6))
fig.suptitle("Top 10 Analysis", fontsize=16, fontweight='bold')

# Top 10 Countries by Revenue
top_countries = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head(10)
axes[0].barh(top_countries.index[::-1], top_countries.values[::-1], color='steelblue')
axes[0].set_title("Top 10 Countries by Revenue")
axes[0].set_xlabel("Total Sales (£)")
for i, v in enumerate(top_countries.values[::-1]):
    axes[0].text(v, i, f' £{v:,.0f}', va='center', fontsize=9)

# Top 10 Products by Revenue
top_products = df.groupby('Description')['TotalSales'].sum().sort_values(ascending=False).head(10)
axes[1].barh(top_products.index[::-1], top_products.values[::-1], color='coral')
axes[1].set_title("Top 10 Products by Revenue")
axes[1].set_xlabel("Total Sales (£)")
axes[1].tick_params(axis='y', labelsize=8)

plt.tight_layout()
plt.savefig("chart2_top10.png", dpi=150)
plt.show()
print("💾 Saved: chart2_top10.png")

# ------------------------------------------------------------
# 5. TIME SERIES ANALYSIS
# ------------------------------------------------------------
print("\n📅 Generating Time Series charts...")

fig, axes = plt.subplots(1, 2, figsize=(18, 5))
fig.suptitle("Sales Over Time", fontsize=16, fontweight='bold')

# Monthly Revenue
monthly = df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalSales'].sum()
monthly.index = monthly.index.astype(str)
axes[0].plot(monthly.index, monthly.values, marker='o', color='steelblue', linewidth=2)
axes[0].set_title("Monthly Revenue Trend")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Total Sales (£)")
axes[0].tick_params(axis='x', rotation=45)
axes[0].fill_between(monthly.index, monthly.values, alpha=0.1, color='steelblue')

# Sales by Hour of Day
hourly = df.groupby('Hour')['TotalSales'].sum()
axes[1].bar(hourly.index, hourly.values, color='mediumseagreen', edgecolor='white')
axes[1].set_title("Sales by Hour of Day")
axes[1].set_xlabel("Hour")
axes[1].set_ylabel("Total Sales (£)")
axes[1].set_xticks(range(0, 24))

plt.tight_layout()
plt.savefig("chart3_timeseries.png", dpi=150)
plt.show()
print("💾 Saved: chart3_timeseries.png")

# ------------------------------------------------------------
# 6. BIVARIATE ANALYSIS - CORRELATION HEATMAP
# ------------------------------------------------------------
print("\n🔗 Generating Bivariate Analysis (Correlation Heatmap)...")

fig, axes = plt.subplots(1, 2, figsize=(18, 6))
fig.suptitle("Bivariate Analysis", fontsize=16, fontweight='bold')

# Correlation Heatmap
corr = df[['Quantity', 'UnitPrice', 'TotalSales']].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm',
            square=True, linewidths=1, ax=axes[0])
axes[0].set_title("Correlation Heatmap")

# Scatter Plot - Quantity vs TotalSales
sample = df.sample(n=2000, random_state=42)
axes[1].scatter(sample['Quantity'], sample['TotalSales'],
                alpha=0.4, color='coral', edgecolors='none', s=20)
axes[1].set_title("Quantity vs Total Sales (sample 2000)")
axes[1].set_xlabel("Quantity")
axes[1].set_ylabel("Total Sales (£)")
axes[1].set_xlim(0, 100)
axes[1].set_ylim(0, 1000)

plt.tight_layout()
plt.savefig("chart4_bivariate.png", dpi=150)
plt.show()
print("💾 Saved: chart4_bivariate.png")

# ------------------------------------------------------------
# 7. DAY OF WEEK ANALYSIS
# ------------------------------------------------------------
print("\n📆 Generating Day of Week chart...")

day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day_sales = df.groupby('Day')['TotalSales'].sum().reindex(day_order)

plt.figure(figsize=(10, 5))
bars = plt.bar(day_sales.index, day_sales.values, color='mediumpurple', edgecolor='white')
plt.title("Total Sales by Day of Week", fontsize=14, fontweight='bold')
plt.xlabel("Day")
plt.ylabel("Total Sales (£)")
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'£{bar.get_height():,.0f}', ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig("chart5_dayofweek.png", dpi=150)
plt.show()
print("💾 Saved: chart5_dayofweek.png")

# ------------------------------------------------------------
# 8. SUMMARY INSIGHTS
# ------------------------------------------------------------
print("\n" + "="*55)
print("💡 KEY BUSINESS INSIGHTS")
print("="*55)
print(f"1. Top Country     : {top_countries.index[0]} (£{top_countries.values[0]:,.2f})")
print(f"2. Top Product     : {top_products.index[0][:40]}...")
print(f"3. Peak Month      : {monthly.idxmax()} (£{monthly.max():,.2f})")
print(f"4. Peak Hour       : {hourly.idxmax()}:00 hrs")
print(f"5. Peak Day        : {day_sales.idxmax()}")
print(f"6. Avg Order Value : £{df.groupby('InvoiceNo')['TotalSales'].sum().mean():,.2f}")

print("\n✅ Step 3 Complete! All charts saved.")
print("📁 Files: chart1_univariate.png, chart2_top10.png,")
print("          chart3_timeseries.png, chart4_bivariate.png, chart5_dayofweek.png")
print("\n➡️  Next: Build your Power BI / Tableau Dashboard using cleaned_data.csv")
