import pandas as pd
import requests
import json

# Hinglish flow: CSV -> clean -> summary -> JSON -> API
try:
    df = pd.read_csv("sales.csv")
    df = df.dropna(subset=["product"])
    df["quantity"] = df["quantity"].fillna(0)
    df["price"] = df["price"].fillna(0)
    df["product"] = df["product"].str.strip().str.title()
    df["revenue"] = df["quantity"] * df["price"]

    summary = {
        "total_rows": len(df),
        "total_quantity": float(df["quantity"].sum()),
        "total_revenue": float(df["revenue"].sum())
    }

    with open("sales_summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print(summary)

    response = requests.post("https://httpbin.org/post", json=summary, timeout=10)
    response.raise_for_status()
    print("API status:", response.status_code)
except Exception as error:
    print("Error:", error)
