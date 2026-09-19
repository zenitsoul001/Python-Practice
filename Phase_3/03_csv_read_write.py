import csv

rows = [
    ["name", "age", "city"],
    ["Aman", 21, "Ludhiana"],
    ["Simran", 20, "Chandigarh"],
]

# Hinglish: CSV simple table format hota hai.
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["city"])
