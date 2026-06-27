# ============================================================
# READYNEST INTERNSHIP - WEEK 2 TASK
# Customer Insights & Segmentation
# Dataset: cleaned_data.csv (from Week 1)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 5)

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------
print("📥 Loading cleaned dataset...")
df = pd.read_csv("cleaned_data.csv", parse_dates=['InvoiceDate'])
print(f"✅ Loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")

# ------------------------------------------------------------
# 2. CUSTOMER-LEVEL AGGREGATION (RFM Analysis)
# ------------------------------------------------------------
print("\n📊 Building Customer Profile...")

# Reference date = day after last invoice
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

customer_df = df.groupby('CustomerID').agg(
    TotalSpend   = ('TotalSales',   'sum'),
    TotalOrders  = ('InvoiceNo',    'nunique'),
    TotalItems   = ('Quantity',     'sum'),
    AvgOrderValue= ('TotalSales',   'mean'),
    LastPurchase = ('InvoiceDate',  'max'),
    FirstPurchase= ('InvoiceDate',  'min'),
    Country      = ('Country',      'first')
).reset_index()

# Recency in days
customer_df['Recency'] = (reference_date - customer_df['LastPurchase']).dt.days

# Customer lifetime in days
customer_df['Lifetime'] = (customer_df['LastPurchase'] - customer_df['FirstPurchase']).dt.days

print(f"✅ Customer profiles created: {customer_df.shape[0]:,} customers")

# ------------------------------------------------------------
# 3. CUSTOMER SEGMENTATION (High / Medium / Low Value)
# ------------------------------------------------------------
print("\n🔀 Segmenting customers...")

# Based on Total Spend percentiles
high_thresh   = customer_df['TotalSpend'].quantile(0.75)
low_thresh    = customer_df['TotalSpend'].quantile(0.25)

def segment(spend):
    if spend >= high_thresh:
        return 'High Value'
    elif spend >= low_thresh:
        return 'Medium Value'
    else:
        return 'Low Value'

customer_df['Segment'] = customer_df['TotalSpend'].apply(segment)

seg_counts = customer_df['Segment'].value_counts()
print(f"\n📌 Segment Distribution:")
for seg, count in seg_counts.items():
    pct = count / len(customer_df) * 100
    print(f"   {seg:15s}: {count:,} customers ({pct:.1f}%)")

# ------------------------------------------------------------
# 4. NEW vs RETURNING CUSTOMERS
# ------------------------------------------------------------
customer_df['CustomerType'] = customer_df['TotalOrders'].apply(
    lambda x: 'New' if x == 1 else 'Returning'
)
new_count = (customer_df['CustomerType'] == 'New').sum()
ret_count = (customer_df['CustomerType'] == 'Returning').sum()
print(f"\n👤 New Customers      : {new_count:,}")
print(f"🔄 Returning Customers: {ret_count:,}")

# ------------------------------------------------------------
# 5. TOP & LOW SPENDING CUSTOMERS
# ------------------------------------------------------------
print("\n🏆 Top 10 Customers by Spend:")
top10 = customer_df.nlargest(10, 'TotalSpend')[
    ['CustomerID','TotalSpend','TotalOrders','Country','Segment']
]
print(top10.to_string(index=False))

print("\n⚠️  Bottom 10 Customers by Spend:")
bot10 = customer_df.nsmallest(10, 'TotalSpend')[
    ['CustomerID','TotalSpend','TotalOrders','Country','Segment']
]
print(bot10.to_string(index=False))

# ------------------------------------------------------------
# 6. VISUALIZATIONS
# ------------------------------------------------------------
print("\n📈 Generating charts...")

# --- Chart 1: Customer Segmentation Pie Chart ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Customer Segmentation", fontsize=16, fontweight='bold')

colors = ['#2ecc71', '#3498db', '#e74c3c']
axes[0].pie(seg_counts.values, labels=seg_counts.index,
            autopct='%1.1f%%', colors=colors, startangle=90,
            wedgeprops=dict(edgecolor='white', linewidth=2))
axes[0].set_title("Customer Segments by Count")

# Revenue by Segment
seg_revenue = customer_df.groupby('Segment')['TotalSpend'].sum().reindex(
    ['High Value', 'Medium Value', 'Low Value'])
axes[1].bar(seg_revenue.index, seg_revenue.values, color=colors, edgecolor='white')
axes[1].set_title("Revenue by Segment")
axes[1].set_ylabel("Total Spend (£)")
for i, v in enumerate(seg_revenue.values):
    axes[1].text(i, v, f'£{v:,.0f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig("chart6_segmentation.png", dpi=150)
plt.show()
print("💾 Saved: chart6_segmentation.png")

# --- Chart 2: New vs Returning ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("New vs Returning Customers", fontsize=16, fontweight='bold')

type_counts = customer_df['CustomerType'].value_counts()
axes[0].pie(type_counts.values, labels=type_counts.index,
            autopct='%1.1f%%', colors=['#3498db','#e67e22'],
            wedgeprops=dict(edgecolor='white', linewidth=2))
axes[0].set_title("Customer Type Distribution")

# Avg spend by type
avg_spend = customer_df.groupby('CustomerType')['TotalSpend'].mean()
axes[1].bar(avg_spend.index, avg_spend.values,
            color=['#3498db','#e67e22'], edgecolor='white')
axes[1].set_title("Avg Spend: New vs Returning")
axes[1].set_ylabel("Avg Total Spend (£)")
for i, v in enumerate(avg_spend.values):
    axes[1].text(i, v, f'£{v:,.0f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig("chart7_new_vs_returning.png", dpi=150)
plt.show()
print("💾 Saved: chart7_new_vs_returning.png")

# --- Chart 3: Top 10 Customers ---
plt.figure(figsize=(12, 6))
top10_plot = customer_df.nlargest(10, 'TotalSpend')
bars = plt.barh(top10_plot['CustomerID'].astype(str)[::-1],
                top10_plot['TotalSpend'][::-1],
                color='steelblue', edgecolor='white')
plt.title("Top 10 Customers by Total Spend", fontsize=14, fontweight='bold')
plt.xlabel("Total Spend (£)")
plt.ylabel("Customer ID")
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f' £{bar.get_width():,.0f}', va='center', fontsize=9)
plt.tight_layout()
plt.savefig("chart8_top_customers.png", dpi=150)
plt.show()
print("💾 Saved: chart8_top_customers.png")

# --- Chart 4: Customer Growth Trend ---
monthly_new = df.groupby(df['InvoiceDate'].dt.to_period('M'))['CustomerID'].nunique()
monthly_new.index = monthly_new.index.astype(str)

plt.figure(figsize=(12, 5))
plt.plot(monthly_new.index, monthly_new.values,
         marker='o', color='mediumseagreen', linewidth=2)
plt.fill_between(monthly_new.index, monthly_new.values, alpha=0.1, color='mediumseagreen')
plt.title("Monthly Active Customers Trend", fontsize=14, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Unique Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart9_customer_growth.png", dpi=150)
plt.show()
print("💾 Saved: chart9_customer_growth.png")

# ------------------------------------------------------------
# 7. SAVE CUSTOMER DATASET
# ------------------------------------------------------------
customer_df.to_csv("customer_segments.csv", index=False)
print("\n💾 Saved: customer_segments.csv")

# ------------------------------------------------------------
# 8. KEY INSIGHTS
# ------------------------------------------------------------
print("\n" + "="*55)
print("💡 KEY CUSTOMER INSIGHTS")
print("="*55)
print(f"1. Total Customers    : {len(customer_df):,}")
print(f"2. High Value Customers: {seg_counts.get('High Value',0):,} "
      f"({seg_counts.get('High Value',0)/len(customer_df)*100:.1f}%)")
print(f"3. Returning Customers : {ret_count:,} "
      f"({ret_count/len(customer_df)*100:.1f}%)")
print(f"4. Top Customer Spend  : £{customer_df['TotalSpend'].max():,.2f}")
print(f"5. Avg Customer Spend  : £{customer_df['TotalSpend'].mean():,.2f}")
print(f"6. Avg Orders/Customer : {customer_df['TotalOrders'].mean():.1f}")
print(f"7. Top Country         : {customer_df['Country'].value_counts().index[0]}")

print("\n✅ Step 1 Complete! customer_segments.csv ready for Power BI")
print("📁 Charts: chart6 to chart9 saved")
print("➡️  Next: Build Power BI Dashboard using customer_segments.csv")
