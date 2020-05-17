import sqlite3
from flask_restful import Resource, reqparse

database_name = 'data.db'


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        # parameters must be in tuple
        result = cursor.execute(query, (username,))
        print(result)
        row = result.fetchone()  # just get one
        if row:
            user = cls(*row)  # positional argument same as in init method
        else:
            user = None
        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        # parameters must be in tuple
        result = cursor.execute(query, (_id,))
        print(result)
        row = result.fetchone()  # just get one
        if row:
            user = cls(*row)  # positional argument same as in init method
        else:
            user = None
        connection.close()

        return user


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username', type=str, required=True, help="Username cannot be left blank."
    )
    parser.add_argument(
        'password', type=str, required=True, help="Password cannot be left blank."
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with {} already exists".format(data['username'])}, 400

        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User Created successfully."}, 201
