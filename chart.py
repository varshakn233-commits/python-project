import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path=r"D:\New folder\sample superstore datasets.csv"
df=pd.read_csv(file_path)

category_sales = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

state_sales=df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.barh(state_sales.index,state_sales.values,color="red")
plt.title("top 10 states by sales")
plt.xlabel("sales")
plt.ylabel("state")
plt.show()

df["Segment"].value_counts().plot(kind='pie',autopct='%1.1f%%',color=["yellow","green","skyblue"])
plt.title("sales by customer segment")
plt.show()

plt.scatter(df['Discount'],df['Profit'])
plt.xlabel("discount")
plt.ylabel("profit")
plt.title("discount vs profit")
plt.show()

plt.hist(df['Profit'],color="orange")
plt.xlabel("Profit")
plt.ylabel("frequency")
plt.title("distribution of Profit")
plt.show()

plt.figure(figsize=(6,5))
plt.boxplot(df["Sales"])
plt.title("Sales Distribution")
plt.ylabel("Sales")
plt.show()

heatmap_data = df.pivot_table(values="Sales",index="Region",columns="Category",aggfunc="sum")
plt.figure(figsize=(8,6))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".0f")
plt.title("Sales Heat Map by Region and Category")
plt.xlabel("Category")
plt.ylabel("Region")
plt.show()

stacked_data = df.pivot_table(values="Profit",index="Region",columns="Ship Mode",aggfunc="sum")
stacked_data.plot(kind="bar",stacked=True,figsize=(10,6))
plt.title("Profit by Region and Ship Mode")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.legend(title="Ship Mode")
plt.tight_layout()
plt.show()
                                  





