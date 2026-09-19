def build_prompt(role, task, context, output_format):
    # Hinglish: Reusable prompt template bana rahe hain.
    return f"""
ROLE:
{role}

TASK:
{task}

CONTEXT:
{context}

OUTPUT FORMAT:
{output_format}
""".strip()

prompt = build_prompt(
    "You are a Python teacher.",
    "Explain list comprehension.",
    "Student knows loops but is a beginner.",
    "Give explanation + 2 examples."
)

print(prompt)
