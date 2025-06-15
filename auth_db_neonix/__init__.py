from auth_db_neonix.security.auth import login, signup, signup, verify_cookie_from_module, verify_cookie_from_https
from auth_db_neonix.security.cripto import encrypt, decrypt

from auth_db_neonix.services.fire_client_service import FirebaseClient
from auth_db_neonix.services.sqlite_service import SQLiteManager
from auth_db_neonix.services.data_retriver_service import DataRetriever

from auth_db_neonix.models.user import User
from auth_db_neonix.dto.user_settings_dto import DbSetting, BaseSettingsDto

from auth_db_neonix.version import __version__

# TODO:
# - Add session management helper for web frameworks (e.g., Flask, FastAPI)
# - Implement caching layer for Firebase reads
# - Add CLI wrapper for auth and settings commands
# - Add function to list all settings for a given user
# - Provide unified exception handling and logging utils

__all__ = [
    "login",
    "signup",
    "verify_cookie_from_module",
    "verify_cookie_from_https",
    "FirebaseClient",
    "SQLiteManager",
    "DataRetriever",
    "User",
    "DbSetting",
    "BaseSettingsDto",
    "encrypt",
    "decrypt",
    "__version__"
]
