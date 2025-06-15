from .user_setting import User_setting
from datetime import  datetime
class User():
    def __init__(self):
        self.profile: dict = {"Username": None, "Email": None}
        self.userId = None
        self.jwt = None
        self.j_refresh_token = None
        self.j_expiration_datetime: datetime
        self.settings: [User_setting]

