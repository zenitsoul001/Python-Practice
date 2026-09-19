# Install: python -m pip install requests
import requests

# GET = server se data lena
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
    response.raise_for_status()
    users = response.json()
    print("First user:", users[0]["name"])
except requests.exceptions.RequestException as error:
    print("GET error:", error)

# POST = server ko data bhejna
payload = {"title": "Python Practice", "body": "Hello API", "userId": 1}
try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, timeout=10)
    response.raise_for_status()
    print("POST response:", response.json())
except requests.exceptions.RequestException as error:
    print("POST error:", error)
