import os

# Securely retrieve credentials from environment variables

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
USER_ID = os.getenv("USER_ID")


def login():
    if not API_KEY or not PASSWORD or not USER_ID:
        print("Credentials are missing!")
        return

    print("User logged in successfully")


login()
