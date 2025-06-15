import requests
import os
from dotenv import load_dotenv
from fastapi import Response, Request
from datetime import timedelta
from firebase_admin import auth


load_dotenv("auth_db_neonix/.env")

API_KEY = os.getenv("FIREBASE_API_KEY")


def signup(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
    r = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True})
    return r.json()


def login(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    r = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True})
    return r.json()


def create_session_container(id_token) -> bytes:
    expire_delta_time = timedelta(days=3)
    return auth.create_session_cookie(id_token, expire_delta_time)


def verify_cookie_from_https(req: Request) -> ():
    cookie = req.cookies.get("session")
    valid: bool = False
    user_id = None
    try:
        decoded_claims = auth.verify_session_cookie(cookie, check_revoked=True)
        user_id = decoded_claims["uid"]
        valid = True
    except Exception as ex:
        print(ex)
        valid = False
    finally:
        return cookie, valid, user_id


def verify_cookie_from_module(cookie: bytes) -> ():
    valid: bool = False
    user_id = None\

    try:
        decoded_claims = auth.verify_session_cookie(cookie, check_revoked=True)
        user_id = decoded_claims["uid"]
        valid = True
    except Exception as ex:
        print(ex)
        valid = False

    finally:
        return cookie, valid, user_id


def generate_api_secure_cookie(session_cookie: bytes):
    response = Response()

    response.set_cookie(
        key="session",
        value=str(session_cookie),
        max_age=3*60*24,
        secure=True,
        httponly=True,
        samesite="strict"
    )




