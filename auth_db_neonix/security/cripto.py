from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

load_dotenv()


def get_fernet():
    try:
        key = os.getenv("FERNET_KEY")
        return Fernet(key.encode())
    except Exception as ex:
        print(ex)


def encrypt(text: str) -> str:
    return get_fernet().encrypt(text.encode()).decode()


def decrypt(token: str) -> str:
    return get_fernet().decrypt(token.encode()).decode()

