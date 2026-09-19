import re

text = "Generative AI models text ko tokens me process karte hain."

# Hinglish: Ye sirf concept demo hai, real tokenizer zyada complex hota hai.
tokens = re.findall(r"\w+|[^\w\s]", text)

for i, token in enumerate(tokens, start=1):
    print(i, token)

print("Total tokens:", len(tokens))

MAX_CONTEXT = 100
print("Remaining demo context:", MAX_CONTEXT - len(tokens))
