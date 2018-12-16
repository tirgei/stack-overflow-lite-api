import re

class Validators():

    def valid_email(self, email):
        ''' Check if email is valid '''
        return re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email)

    def valid_password(self, password):
        ''' Check if password is valid '''
        return re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', password)