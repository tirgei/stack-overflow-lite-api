from app.tests.v1.base_test import BaseTest

class TestUser(BaseTest):

    def setUp(self):
        self.signup = '/api/v1/auth/signup'
        self.login = '/api/v1/auth/login'

        self.user1 = {
            "name" : "John Doe",
            "email" : "jd@gmail.com"
        }

        self.user2 = {
            "name" : "John Doe",
            "email" : "jd@gmail",
            "password" : "afaweffwewef"
        }

        self.user3 = {
            "name" : "John Doe",
            "email" : "jd@gmail.com",
            "password" : "afaweffwewef"
        }

        self.user4 = {
            "name" : "John Doe",
            "email" : "jd@gmail.com",
            "password" : "afsef4wrfsD$"
        }

        self.user5 = {
            "name" : "Elliot Reed",
            "email" : "jd@gmail.com",
            "password" : "csd68sF#d"
        }

        self.user6 = {
            "name" : "John Dorian",
            "email" : "jd@gmail.com",
            "password" : "afsef4wrfsD$"
        }

        super().setUp()

    def test_signup_no_data(self):
        """ Test sign up with no data sent """
        res = self.client.post(self.signup)
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Please provide valid data')

    def test_signup_missing_fields(self):
        """ Test sign up with missing fields in the request """
        res = self.client.post(self.signup, json=self.user1, content_type='application/json')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], "Please fill in all details")

    def test_signup_invalid_email(self):
        """ Test signup with an invalid email """
        res = self.client.post(self.signup, json=self.user2, content_type='application/json')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], "Invalid email")

    def test_signup_weak_password(self):
        """ Test signup with a weak password """
        res = self.client.post(self.signup, json=self.user3, content_type='application/json')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], "Invalid password")

    def test_signup(self):
        """ Test user signup with correct information """
        res = self.client.post(self.signup, json=self.user4, content_type='application/json')
        data = res.get_json()

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], "User successfully created")

    def test_signup_with_existing_email(self):
        """ Test user signup with existing email """

        # Register first user
        self.client.post(self.signup, json=self.user4, content_type='application/json')

        # Register second user with same email
        res = self.client.post(self.signup, json=self.user5, content_type='application/json')
        data = res.get_json()

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], "Email jd@gmail.com already exists")

    def test_fetch_all_users(self):
        """ Test fetching all users """

        res = self.client.get('/api/v1/users')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)

    def test_update_user_details(self):
        """ Test updating user details """

        res = self.client.post(self.signup, json=self.user5, content_type='application/json')
        data = res.get_json()

        self.assertEqual(data['message'], "Email jd@gmail.com already exists")


