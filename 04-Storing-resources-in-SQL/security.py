from werkzeug.security import safe_str_cmp
from user import User
import sqlite3


def authenticate(username, password):
    # we can provide a default value if doesnt exists
    user = User.find_by_username(username)
    # replace this with `==` operator
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
