import pandas as pd

# Load all files from data folder
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)
df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["Sales"] = df["price"] * df["quantity"]
df = df[["Sales", "date", "region"]]
df.columns = ["Sales", "Date", "Region"]
df.to_csv("formatted_sales_data.csv", index=False)

