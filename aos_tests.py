import unittest
import aos_locators as locators
import aos_methods as methods


class AOSappPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_aos():
        try:
            methods.setUp()
            #methods.validate_homepage_texts_links()
            #methods.top_menu_nav()
            #methods.contact_us_form()
            methods.create_new_user()
            methods.log_out()
            methods.log_in(locators.username, locators.password)
            methods.checkout_shopping_cart()
            methods.log_out()
        except Exception as error:
            print('Some Problem :', error)
        finally:
            methods.tearDown()
