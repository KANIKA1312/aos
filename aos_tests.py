import unittest
import aos_locators as locators
import aos_methods as methods

class AOSappPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_aos():
        try:
            methods.setUp()
            methods.create_new_user()
            methods.log_out()
            methods.log_in(locators.username,locators.password)
            methods.log_out()
        except Exception as error:
            print('Some Problem :', error)
        finally:
            methods.tearDown()