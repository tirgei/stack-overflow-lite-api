from app.api.utils.base_model import Model

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
        user = [u for u in super().all() if id == u['id']][0]

        for key, value in data.items():
            if key in user:
                user.update({key: value})

            if not hasattr(user, key):
                user[key] = value
            
        return user