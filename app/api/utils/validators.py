import re

class Validators():

    def valid_email(self, email):
        ''' Check if email is valid '''
        return re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email)

    def valid_password(self, password):
        ''' Check if password is valid '''

        if len(password) < 8:
            return False

        scores = {}

        for letter in password:
            if letter.islower():
                scores['has_lower'] = 1

            if letter.isupper():
                scores['has_upper'] = 1

            if letter.isdigit():
                scores['has_digit'] = 1

        return sum(scores.values()) == 3