import pandas as pd 
import matplotlib.pyplot as plt
# import seaborn as sns
df = pd.read_csv(r'C:\Users\ishug\Downloads\ECOMM DATA.csv')
# print(df)
# print(df.shape)
# print(df.info())
# print(df.columns)
# print(df.head())
# print(df.tail())
# -----------Convert dates---------
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)
# print(df.info())
# ----------Missing values-----------
print(df.isnull().sum())
# ----------Duplicate rows------------
print(df.duplicated().sum())
# --------Statistical summary--------
print(df.describe())

# -------- Basic Business Analysis --------
# -total sales-
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# -total profit-
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

#  -average sales-
average_sales = df["Sales"].mean()
print("Average Sales:", average_sales)

# -average profit-
average_profit = df["Profit"].mean()
print("Average profit:", average_profit)

# ------- Sales and Profit by Category -------

category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()
print(category_analysis)
#  ------ Highest Sales and Profit Category -------
highest_sales_category=category_analysis["Sales"].idxmax()
print("Highest Sales Category:", highest_sales_category)

highest_profit_category=category_analysis["Profit"].idxmax()
print("Highest Profit Category:", highest_profit_category)

# ---------- Sales and Profit by Region ----------
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()
print(region_analysis)


# ---------- Highest Sales and Profit Region ----------

highest_sales_region = region_analysis["Sales"].idxmax()
print("Highest Sales Region:", highest_sales_region)

highest_profit_region = region_analysis["Profit"].idxmax()
print("Highest Profit Region:", highest_profit_region)

# ---------- Monthly Sales Trend ----------

df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

# ---------- Highest Sales Month ----------
highest_sales_month = monthly_sales.idxmax()
print("Highest Sales Month:", highest_sales_month)

highest_sales_value = monthly_sales.max()
print("Highest Sales:", highest_sales_value)

# ---------- Sales by Customer Segment ----------
segment_sales = df.groupby("Segment")["Sales"].sum()
print(segment_sales)

# ---------- Highest Sales Segment ----------
highest_sales_segment = segment_sales.idxmax()
print("Highest Sales Segment:", highest_sales_segment)

highest_segment_sales = segment_sales.max()
print("Highest Segment Sales:", highest_segment_sales)

# ---------- Discount vs Profit ----------
discount_profit = df.groupby("Discount")["Profit"].mean()
print(discount_profit)
# top 10 products by sales
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(top_products)


import matplotlib.pyplot as plt
# --- Sales by Category---
fig,ax=plt.subplots(figsize=(12, 6))
bars=ax.bar(category_analysis.index, 
            category_analysis["Sales"])
ax.bar_label(bars, padding=3, fontsize=12)
ax.set_title("profit by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_category.png")
plt.show()

# ---Profit by Category---
fig,ax=plt.subplots(figsize=(12, 6))
bars=ax.bar(category_analysis.index, 
            category_analysis["Profit"],
            color="orange")
ax.bar_label(bars, padding=3, fontsize=12)
ax.set_title("profit by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_category.png")
plt.show()



# ---Monthly Sales Trend---
plt.figure(figsize=(12, 6))
plt.plot(category_analysis.index, 
         category_analysis["Sales"],marker="o",
         markerfacecolor="yellow",
         markeredgecolor="black",color="red")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# ---------- Sales by Segment ----------
plt.figure(figsize=(8, 8))
plt.pie(segment_sales.values,
    labels=segment_sales.index,
    autopct="%1.1f%%", 
    wedgeprops={"edgecolor": "black", "linewidth": 2}
)

plt.title("Sales by Customer Segment")
plt.tight_layout()
plt.legend()
plt.savefig("sales_segment.png")
plt.show()


# ---------- Discount vs Profit ----------

plt.figure(figsize=(12, 6))
plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("discount_profit.png")
plt.show()


# ---------- Top 10 Products by Sales ----------

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(top_products.index, top_products.values)
ax.bar_label(bars, padding=3, fontsize=10)
ax.set_title("Top 10 Products by Sales")
ax.set_xlabel("Sales")
ax.set_ylabel("Product Name")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()
