import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

os.makedirs("data/raw", exist_ok=True)

# -------------------
# Date Dimension
# -------------------
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

dates = pd.date_range(start_date, end_date)

dim_date = pd.DataFrame({
    "Date": dates,
    "Year": dates.year,
    "Month": dates.month,
    "MonthName": dates.strftime("%B"),
    "Quarter": dates.quarter
})

dim_date.to_csv("data/raw/dim_date.csv", index=False)

# -------------------
# Product Dimension
# -------------------
products = []
for i in range(1, 51):
    products.append([
        i,
        f"Product {i}",
        random.choice(["Electronics", "Furniture", "Office Supplies"]),
        random.choice(["A", "B", "C"]),
        random.choice(["BrandX", "BrandY"])
    ])

dim_product = pd.DataFrame(products, columns=[
    "ProductID", "ProductName", "Category", "Subcategory", "Brand"
])
dim_product.to_csv("data/raw/dim_product.csv", index=False)

# -------------------
# Customer Dimension
# -------------------
customers = []
for i in range(1, 101):
    customers.append([
        i,
        f"Customer {i}",
        random.choice(["Corporate", "Consumer", "SMB"]),
        random.choice(["Australia", "USA", "UK"])
    ])

dim_customer = pd.DataFrame(customers, columns=[
    "CustomerID", "CustomerName", "Segment", "Country"
])
dim_customer.to_csv("data/raw/dim_customer.csv", index=False)

# -------------------
# Region Dimension
# -------------------
regions = [
    [1, "NSW", "Australia"],
    [2, "VIC", "Australia"],
    [3, "QLD", "Australia"],
    [4, "CA", "USA"],
    [5, "TX", "USA"]
]

dim_region = pd.DataFrame(regions, columns=[
    "RegionID", "RegionName", "Country"
])
dim_region.to_csv("data/raw/dim_region.csv", index=False)

# -------------------
# Channel Dimension
# -------------------
channels = [
    [1, "Online"],
    [2, "Retail"],
    [3, "Partner"]
]

dim_channel = pd.DataFrame(channels, columns=[
    "ChannelID", "ChannelName"
])
dim_channel.to_csv("data/raw/dim_channel.csv", index=False)

# -------------------
# Fact Table
# -------------------
records = []

for i in range(5000):
    quantity = random.randint(1, 10)
    price = random.uniform(20, 500)
    cost = price * random.uniform(0.5, 0.8)
    discount = price * random.uniform(0, 0.2)

    gross = quantity * price
    discount_amt = quantity * discount
    net = gross - discount_amt
    total_cost = quantity * cost
    profit = net - total_cost

    records.append([
        i,
        random.choice(dates),
        random.randint(1, 50),
        random.randint(1, 100),
        random.randint(1, 5),
        random.randint(1, 3),
        quantity,
        round(price, 2),
        round(cost, 2),
        round(discount_amt, 2),
        round(net, 2),
        round(total_cost, 2),
        round(profit, 2)
    ])

fact_sales = pd.DataFrame(records, columns=[
    "OrderID", "OrderDate", "ProductID", "CustomerID",
    "RegionID", "ChannelID", "Quantity",
    "UnitPrice", "UnitCost", "DiscountAmount",
    "NetRevenue", "TotalCost", "Profit"
])

fact_sales.to_csv("data/raw/fact_sales.csv", index=False)

print("Data generated successfully!")