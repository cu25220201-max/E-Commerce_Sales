import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")

print(df)
df["Revenue"] = df["Quantity"] * df["Price"]

print(df)
total_revenue = df["Revenue"].sum()

print("Total Revenue =", total_revenue)
df["Profit"] = df["Revenue"] * 0.20

print(df[["Product","Revenue","Profit"]])
total_profit = df["Profit"].sum()

print("Total Profit =", total_profit)
category_sales = df.groupby("Category")["Revenue"].sum()

print(category_sales)
best = category_sales.idxmax()

print("Best Selling Category =", best)
import matplotlib.pyplot as plt

category_sales.plot(
    kind="bar"
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.show()
profit_category = df.groupby("Category")["Profit"].sum()

profit_category.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Profit Distribution")
plt.ylabel("")

plt.show()
