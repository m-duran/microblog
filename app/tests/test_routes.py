import unittest
from app.tests.config import TestConfig

from app import app, db


class RouteTests(unittest.TestCase):

    def setUp(self) -> None:
        app.config.from_object(TestConfig)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    def register(self, username, email, password, confirm):
        return self.app.post(
            '/register',
            data=dict(username=username, email=email, password=password, password2=confirm),
            follow_redirects=True
        )

    def login(self, username, password):
        return self.app.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def test_valid_user_registration(self):
        response = self.register('test_user', 'test_user@test.com', 'password', 'password')
        self.assertEqual(200, response.status_code)

    def test_login_page_loads_for_anonymous_user(self):
        response = self.app.get(
            '/login',
            follow_redirects=True
        )
        self.assertEqual(200, response.status_code)

    def test_logging_in_user(self):
        register_response = self.register('test_user', 'test_user@test.com', 'password', 'password')
        self.assertEqual(200, register_response.status_code)

        login_response = self.login('test_user', 'password')
        self.assertEqual(200, login_response.status_code)

    def test_username_must_be_unique(self):
        response = self.register('test_user', 'test_user@test.com', 'password', 'password')
        self.assertEqual(200, response.status_code)
        self.assertNotIn(b'Please use a different username', response.data)

        response2 = self.register('test_user', 'test_user2@test.com', 'password', 'password')
        self.assertIn(b'Please use a different username', response2.data)

    def test_email_must_be_unique(self):
        response = self.register('test_user', 'test_user@test.com', 'password', 'password')
        self.assertEqual(200, response.status_code)
        self.assertNotIn(b'Please use a different email', response.data)

        response2 = self.register('test_user2', 'test_user@test.com', 'password', 'password')
        self.assertIn(b'Please use a different email', response2.data)


if __name__ == '__main__':
    unittest.main()
