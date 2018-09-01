import unittest
from flask import current_app
from app import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Method called to prepare the test fixture. This is called immediately before calling the test method; other than AssertionError or SkipTest, any exception raised by this method will be considered an error rather than a test failure.
        '''
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        '''
        tearDown method that executes a set of instructions after every test in the whole app
        tidies up after the test method has been run
        '''

        self.app_context.pop()

    def test_app_exists(self):
        '''
        Test that expr is true (or false).
        '''
        self.assertFalse(current_app is None)
