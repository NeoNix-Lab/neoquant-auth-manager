from auth_db_neonix import (
    login,
    signup,
    verify_cookie_from_module,
    verify_cookie_from_https,
    FirebaseClient,
    SQLiteManager,
    DataRetriever,
    User,
    DbSetting,
    BaseSettingsDto
)
from typing import Union
from fastapi import Request
import os
import json
import base64
from firebase_admin import credentials, initialize_app
from dotenv import load_dotenv

load_dotenv("auth_db_neonix/.env")

firebase_b64 = os.getenv("FIREBASE_CONFIG_B64")
if firebase_b64:
    decoded = base64.b64decode(firebase_b64)
    cred_dict = json.loads(decoded)
    cred = credentials.Certificate(cred_dict)
    initialize_app(cred)
else:
    raise RuntimeError("Missing FIREBASE_CONFIG_B64 environment variable")



def sign_up(email: str, password: str) -> User:
    """
    Handles user registration and returns a User instance.
    """
    return signup(email, password)


def sign_in(email: str, password: str) -> User:
    """
    Handles user login and returns a User instance.
    """
    return login(email, password)


def create_user_setting(user: User, setting: BaseSettingsDto):
    """
    Saves user settings to Firebase.
    """
    FirebaseClient.create_settings(user.userId, setting)


def update_user_settings(user: User, setting: BaseSettingsDto):
    """
    Updates existing user settings in Firebase.
    """
    FirebaseClient.update_settings(user.userId, setting)


def validate_session_cookie(token: Union[bytes, Request]) -> bool:
    """
    Validates session JWT and returns whether it is valid.
    """
    if isinstance(token, bytes):
        _, valid, _ = verify_cookie_from_module(token)
        return valid
    else:
        _, valid, = verify_cookie_from_https(token)
        return valid


def init_sqlite_manager(setting: DbSetting) -> SQLiteManager:
    """
    Initializes SQLite manager with path from setting.
    """
    return SQLiteManager(setting)


def init_data_retriever(setting: DbSetting) -> DataRetriever:
    """
    Initializes DataRetriever with path from setting.
    """
    return DataRetriever(setting)


if __name__ == "__main__":
    print("Main module placeholder - can be expanded with CLI or script execution logic.")
