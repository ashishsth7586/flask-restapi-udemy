from user import User
from werkzeug.security import safe_str_cmp
users = [
    User(1, 'ashish', 'admin')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # we can provide a default value if doesnt exists
    user = username_mapping.get(username, None)
    # replace this with `==` operator
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
