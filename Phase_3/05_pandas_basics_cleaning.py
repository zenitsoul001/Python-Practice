# Install: python -m pip install pandas
import pandas as pd

data = {
    "name": [" Aman ", "simran", "RAHUL", "Neha"],
    "age": [21, 20, None, 23],
    "city": ["Ludhiana", "Chandigarh", "Delhi", None],
    "score": [85, 91, 72, None]
}

df = pd.DataFrame(data)
print("Original:\n", df)

# Hinglish: string cleaning
df["name"] = df["name"].str.strip().str.title()

# Missing values handle karna
df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna("Unknown")
df["score"] = df["score"].fillna(0)

# Filtering: score 80 se zyada
print("\nHigh scores:\n", df[df["score"] > 80])

df.to_csv("clean_students.csv", index=False)
