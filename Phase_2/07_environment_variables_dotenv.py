# ==========================================
# Environment Variables
# ==========================================

"""
File 7: 07_environment_variables_dotenv.py

First install:

pip install python-dotenv

Create file:

.env

Inside:

DATABASE_PASSWORD=12345
API_KEY=mysecretkey

"""


from dotenv import load_dotenv
import os



# .env file load karna

load_dotenv()



# Environment variable read karna


api_key = os.getenv(
    "API_KEY"
)


password = os.getenv(
    "DATABASE_PASSWORD"
)



print(api_key)

print(password)