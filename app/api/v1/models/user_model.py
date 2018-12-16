from app.api.utils.base_model import Model

users = []

class User(Model):

    def __init__(self):
        super().__init__(users)
