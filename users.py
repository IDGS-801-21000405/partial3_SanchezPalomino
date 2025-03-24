from flask_login import UserMixin

usuarios = {
    "admin": {"id": "1", "username": "admin"},
    "usuario": {"id": "2", "username": "usuario"}
}

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

def get_user(username):
    user_data = usuarios.get(username)
    if user_data:
        return User(user_data["id"], user_data["username"])
    return None