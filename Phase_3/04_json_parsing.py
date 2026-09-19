import json

person = {
    "name": "Tushar",
    "skills": ["Python", "AI"],
    "address": {"city": "Ludhiana", "state": "Punjab"}
}

# Hinglish: dumps Python object ko JSON string banata hai.
print(json.dumps(person, indent=4))

# dump JSON file me save karta hai.
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4)

# load JSON file ko Python object me convert karta hai.
with open("person.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("City:", data["address"]["city"])
print("First skill:", data["skills"][0])
