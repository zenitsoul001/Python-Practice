# ==========================================
# Protecting API Keys
# ==========================================


import os
from dotenv import load_dotenv



load_dotenv()



# API key directly code me nahi likhni


OPENAI_KEY = os.getenv(
    "OPENAI_API_KEY"
)



if OPENAI_KEY:

    print(
        "API Key Loaded Successfully"
    )


else:

    print(
        "API Key Missing"
    )