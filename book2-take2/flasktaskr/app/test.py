# test.py


import os
import unittest

from views import app, db
from config import basedir
from models import User

TEST_DB = 'test.db'


class AllTests(unittest.TestCase):
    # ###################
    ########SETUP#######
    ####################

    #executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    #executed after each test
    def tearDown(self):
        db.drop_all()

    ####################
    ######HELPERS#######
    ####################

    def login(self, name, password):
        return self.app.post('/', data=dict(
            name=name, password=password), follow_redirects=True)

    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(
            name=name, email=email, password=password, confirm=confirm),
                             follow_redirects=True)

    ####################
    #######TESTS########
    ####################

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please sign in to access your task list', response.data)

    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn('Invalid username or password.', response.data)

    def test_users_can_login(self):
        self.register('Nicholas', 'nick@nicholastjohnson.com', 'python',
                      'python')
        response = self.login('Nicholas', 'python')
        self.assertIn('You are logged in. Go crazy', response.data)

    def test_invalid_form_data(self):
        self.register('Nicholas', 'nick@nicholastjohnson.com', 'python',
                      'python')
        response = self.login('alert("alert box!");', 'foo')
        self.assertIn('Invalid username or password', response.data)

    def test_form_is_present_on_register_page(self):
        response = self.app.get('register/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please register to start a task list', response.data)

    def test_user_registration(self):
        self.app.get('register/', follow_redirects=True)
        self.register('Nicholas', 'nick@nicholastjohnson.com',
                        'python', 'python')
        self.app.get('register/', follow_redirects=True)
        response = self.register('Nicholas', 'nick@nicholastjohnson.com',
                                 'python', 'python')
        self.assertIn('Oh no! That username and/or email already exist.',
                      response.data)

if __name__ == "__main__":
    unittest.main()