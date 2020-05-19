from werkzeug.security import safe_str_cmp
from models.user import UserModel
import sqlite3


def authenticate(username, password):
    # we can provide a default value if doesnt exists
    user = UserModel.find_by_username(username)
    # replace this with `==` operator
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
