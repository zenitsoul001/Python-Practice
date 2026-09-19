import os
import requests

# Hinglish: API key code me hard-code mat karo. Environment variable better hai.
API_KEY = os.getenv("MY_API_KEY")

if not API_KEY:
    print("MY_API_KEY set nahi hai.")
else:
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.get("https://example.com/api/data", headers=headers, timeout=10)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as error:
        print("API error:", error)

# PowerShell:
# $env:MY_API_KEY="your_secret_key"
