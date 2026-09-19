# Hinglish: Strong prompt me role + task + context + output format clear rakho.

system_prompt = """
You are a helpful data analysis assistant.
Explain results simply.
"""

user_prompt = """
TASK:
Analyze the sales data.

CONTEXT:
Laptop = 10
Mouse = 30
Keyboard = 20

INSTRUCTIONS:
- Find highest selling product
- Find total units

OUTPUT FORMAT:
Return JSON only.
"""

print(system_prompt)
print(user_prompt)
