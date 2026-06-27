# 🛒 ReadyNest Internship — Data Analytics

<div align="center">

![ReadyNest](https://img.shields.io/badge/ReadyNest-Internship-028090?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-Public-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-02C39A?style=for-the-badge)

### 📊 E-Commerce Customer Insights & Sales Analytics
**Intern:** Harshit Saxena &nbsp;|&nbsp; **Organization:** ReadyNest Corp. &nbsp;|&nbsp; **Duration:** June 2026

</div>

---

## 🔗 Live Dashboards

<div align="center">

| Week | Dashboard | Link |
|------|-----------|------|
| 📦 Week 1 | Product Sales & Performance Dashboard | [![Tableau](https://img.shields.io/badge/View%20Dashboard-Tableau%20Public-E97627?style=flat-square&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/harshit.saxena4505/viz/readynesttasktrial1/Sheet1) |
| 👥 Week 2 | Customer Insights & Segmentation Dashboard | [![Tableau](https://img.shields.io/badge/View%20Dashboard-Tableau%20Public-E97627?style=flat-square&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/harshit.saxena4505/viz/Task2_17824998555060/Dashboard1) |

</div>

---

## 📁 Repository Structure

```
readynest-internship/
│
├── 📂 Week 1 - Dataset Analysis & Reporting/
│   ├── step1_data_loading.py          # Data loading & exploration
│   ├── step2_data_cleaning.py         # Data cleaning pipeline
│   ├── step3_eda.py                   # EDA & visualizations
│   ├── cleaned_data.csv               # Cleaned dataset output
│   └── charts/
│       ├── chart1_univariate.png
│       ├── chart2_top10.png
│       ├── chart3_timeseries.png
│       ├── chart4_bivariate.png
│       └── chart5_dayofweek.png
│
├── 📂 Week 2 - Customer Insights & Recommendations/
│   ├── week2_customer_segmentation.py # Customer segmentation script
│   ├── customer_segments.csv          # Customer profiles output
│   ├── ReadyNest_Week2_Business_Report.pptx
│   └── charts/
│       ├── chart6_segmentation.png
│       ├── chart7_new_vs_returning.png
│       ├── chart8_top_customers.png
│       └── chart9_customer_growth.png
│
└── README.md
```

---

## 📦 Week 1 — Dataset Analysis & Reporting

<details>
<summary><b>📋 Click to expand Week 1 details</b></summary>

### 🎯 Objective
Analyze a comprehensive E-Commerce dataset, perform data cleaning and EDA, and create an interactive Tableau dashboard.

### 📊 Dataset Overview
| Property | Value |
|----------|-------|
| 📄 Source | E-Commerce Online Retail (UCI / Kaggle) |
| 📏 Raw Rows | 541,909 |
| ✅ Cleaned Rows | 392,692 |
| 📌 Columns | 8 → 13 (after feature engineering) |
| 🌍 Countries | 37 |
| 📅 Date Range | Dec 2010 – Dec 2011 |

### 🧹 Data Cleaning Steps
- ✅ Removed **5,268 duplicate rows**
- ✅ Dropped rows with **missing CustomerID** (133,361 rows)
- ✅ Removed **cancelled orders** (InvoiceNo starting with 'C')
- ✅ Removed **negative/zero Quantity and UnitPrice**
- ✅ Converted `InvoiceDate` to datetime format
- ✅ Added derived columns: `TotalSales`, `Year`, `Month`, `Day`, `Hour`
- ✅ Standardized text in `Description` and `Country`

### 📈 Key Metrics
```
💰 Total Revenue      : £8,887,209
📦 Total Orders       : 25,900
👥 Unique Customers   : 4,338
🌍 Countries Served   : 37
📅 Peak Month         : November 2011
⏰ Peak Hour          : 12:00 PM
📆 Peak Day           : Thursday
```

### 📊 EDA Charts

#### 1️⃣ Univariate Analysis
> Distribution of Quantity, Unit Price and Total Sales

#### 2️⃣ Top 10 Analysis
> Top countries and products by revenue

#### 3️⃣ Monthly Revenue Trend
> Sales trend across all months

#### 4️⃣ Bivariate Analysis
> Correlation heatmap and scatter plot

#### 5️⃣ Sales by Day of Week
> Which day drives most sales

### 🖥️ Tableau Dashboard
[![Week 1 Dashboard](https://img.shields.io/badge/🔗%20Open%20Week%201%20Dashboard-Tableau%20Public-E97627?style=for-the-badge)](https://public.tableau.com/app/profile/harshit.saxena4505/viz/readynesttasktrial1/Sheet1)

**Dashboard includes:**
- 📈 Monthly Revenue Trend (Line Chart)
- 🌍 Top 10 Countries by Revenue (Bar Chart)
- 📦 Top 10 Products by Revenue (Bar Chart)
- ⏰ Sales by Hour of Day (Bar Chart)
- 📆 Sales by Day of Week (Bar Chart)
- 🗺️ Geographic Revenue Map
- 🔢 KPI Cards (Revenue, Orders, Customers)

</details>

---

## 👥 Week 2 — Customer Insights & Recommendation Project

<details>
<summary><b>📋 Click to expand Week 2 details</b></summary>

### 🎯 Objective
Analyze customer and sales data to uncover actionable insights, segment customers, and provide business recommendations.

### 👤 Customer Segmentation

| Segment | Customers | Threshold | Revenue Share |
|---------|-----------|-----------|---------------|
| 🏆 High Value | ~1,085 (25%) | Spend > £1,500 | Very High |
| ⭐ Medium Value | ~2,169 (50%) | £300 – £1,500 | Moderate |
| 🌱 Low Value | ~1,084 (25%) | Spend < £300 | Low |

### 📊 Customer Metrics
```
👥 Total Customers       : 4,338
🔄 Returning Customers   : 74.5%
🆕 New Customers         : 25.5%
💰 Avg Customer Spend    : £2,048
📦 Avg Orders/Customer   : 5.97
🏆 Top Customer Spend    : £280,206
```

### 📊 Customer Analysis Charts

#### 6️⃣ Customer Segmentation
> Pie chart and revenue bar by High/Medium/Low Value segments

#### 7️⃣ New vs Returning Customers
> Distribution and average spend comparison

#### 8️⃣ Top 10 Customers by Spend
> Horizontal bar chart of highest value customers

#### 9️⃣ Customer Growth Trend
> Monthly active customers over time

### 🖥️ Tableau Dashboard
[![Week 2 Dashboard](https://img.shields.io/badge/🔗%20Open%20Week%202%20Dashboard-Tableau%20Public-E97627?style=for-the-badge)](https://public.tableau.com/app/profile/harshit.saxena4505/viz/Task2_17824998555060/Dashboard1)

**Dashboard includes:**
- 👥 New vs Returning Customers
- 🥧 Customer Segment Distribution (Pie)
- 📈 Customer Growth Trend
- 🏆 Top 10 Customers by Spend
- 🗺️ Customer Geographic Analysis
- 💰 Revenue by Customer Segment
- 📊 Average Order Value by Segment

</details>

---

## 💡 Key Business Insights

<table>
<tr>
<td width="50%">

**01 🇬🇧 UK Market Dominance**
> UK accounts for **82% of total revenue** (£7.28M). Heavy reliance on one market creates risk — diversification needed.

**02 🔄 Strong Customer Loyalty**
> **74.5% of customers are returning buyers**, showing strong brand loyalty and product satisfaction.

**03 📅 Seasonal Revenue Spike**
> Revenue peaks in **Q4 (Oct–Dec)**. November alone contributes **12.7% of annual revenue** — driven by holiday shopping.

</td>
<td width="50%">

**04 🏆 High Value Customers Drive Revenue**
> Top 25% of customers contribute disproportionately. **Retaining them is the #1 priority.**

**05 ⏰ Midday & Weekday Sales Peak**
> Orders peak at **12 PM on Thursdays**. Marketing campaigns should target these windows.

**06 🌍 International Market Potential**
> Netherlands, EIRE and Germany show organic demand. Targeted expansion could drive **20%+ growth.**

</td>
</tr>
</table>

---

## 🎯 Business Recommendations

| # | Recommendation | Priority | Impact |
|---|---------------|----------|--------|
| 1 | 🏆 **VIP Loyalty Program** — Exclusive rewards for High Value customers | 🔴 HIGH | Revenue Retention |
| 2 | 🌍 **International Expansion** — Focus on Netherlands, Germany, France | 🔴 HIGH | Revenue Growth |
| 3 | 📅 **Seasonal Campaign Strategy** — Pre-plan Q4 campaigns 3 months in advance | 🔴 HIGH | Peak Revenue |
| 4 | 🔄 **Win-Back Low Value Customers** — Personalized email & bundle offers | 🟡 MEDIUM | Customer Growth |
| 5 | ⏰ **Time-Targeted Marketing** — Launch campaigns Thursday at 11 AM | 🟡 MEDIUM | Conversion Rate |
| 6 | 📦 **Bundle Top Products** — Gift sets for Q4 to increase avg order value | 🟡 MEDIUM | AOV Growth |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|----------|-------|
| 🐍 Language | Python 3.x |
| 📊 Data Analysis | Pandas, NumPy |
| 📈 Visualization | Matplotlib, Seaborn |
| 🖥️ Dashboard | Tableau Public |
| 🗄️ Data Format | CSV |
| 🔧 Version Control | Git & GitHub |

</div>

---

## ▶️ How to Run

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn
```

### Week 1
```bash
# Step 1: Load data
python step1_data_loading.py

# Step 2: Clean data
python step2_data_cleaning.py

# Step 3: EDA & visualizations
python step3_eda.py
```

### Week 2
```bash
# Customer segmentation
python week2_customer_segmentation.py
```

---

## 📬 Contact

<div align="center">

**Harshit Saxena**
ReadyNest Data Analytics Intern | June 2026

[![Tableau](https://img.shields.io/badge/Tableau%20Public-Profile-E97627?style=flat-square&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/harshit.saxena4505)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github&logoColor=white)](https://github.com)

---

*Built with ❤️ for ReadyNest Corp. Internship Program*
*"Learn. Analyze. Communicate. Get recognized!"*

</div>
