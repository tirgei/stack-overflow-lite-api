from app.api.utils.base_model import Model

users = []

class User(Model):

    def __init__(self):
        super().__init__(users)

    def update(self, id, data):
        user = [u for u in super().all() if id == u['id']][0]

        for key, value in data.items():
            if key in user:
                user.update({key: value})

        return user