from app.api.utils.base_model import Model
from datetime import datetime, timedelta
import os
import jwt

users = [
    {
        "id" : 1,
        "name" : "John Doe",
        "email" : "doej@sdfs.com",
    },
    {
        "id" : 2,
        "name" : "Ricky Dave",
        "email" : "dave@gmail.com",
    },
    {
        "id" : 3,
        "name" : "Elliot Reed",
        "email" : "elly@yahoo.com",
    },
    {
        "id" : 4,
        "name" : "Carla Turk",
        "email" : "turkster@sdfs.com",
    }
]

class User(Model):

    def __init__(self):
        super().__init__(users)

    def update(self, id, data):
        """ Function to update user details """

        user = [u for u in super().all() if id == u['id']][0]

        for key, value in data.items():
            if key in user:
                user.update({key: value})

            if not hasattr(user, key):
                user[key] = value

        user['updated_on'] = datetime.now()
        return user

    def generate_token(self, id):
        """ Function to generate the authentication token """

        try:
            payload = {
                'exp' : datetime.utcnow() + timedelta(days=0, seconds=30),
                'iat' : datetime.utcnow(),
                'sub' : id
            }

            return jwt.encode(
                payload,
                os.getenv('SECRET_KEY', 'canttouchthis'),
                algorithm='HS256'
            )

        except Exception as e:
            return e

        @staticmethod
        def decode_token(token):
            """ Decodes the auth token and returns the user ID """

            try:
                payload = jwt.decode(token, os.getenv('SECRET_KEY'))
                return payload['sub']
            
            except jwt.ExpiredSignatureError:
                return 'Signature expired. Please log in again'

            except jwt.InvalidTokenError:
                return 'Invalid token. Please log in again'