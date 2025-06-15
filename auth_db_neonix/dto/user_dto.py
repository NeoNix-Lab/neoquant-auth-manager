from ..models.user import User_setting,  User
class User_Dto():
    def __init__(self, username, email, userid, settings=None):
        self.profile: dict = {"Username": username, "Email": email}
        self.userId = userid
        self.settings = settings

 