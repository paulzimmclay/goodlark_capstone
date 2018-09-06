from selenium import webdriver
import unittest
import time

class NewVisitorRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # When a prospective goodlark recipient arrives at the homepage...
    def test_user_can_load_the_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Goodlark Educational Foundation', self.browser.title)
    
    # user can click an affordance and navigate to a register page
    # def test_user_can_navitage_to_register_page(self):
    def test_home_has_a_link_to_register_page(self):
        register_link = self.browser.find_element_by_id('register_button')
        self.assertEqual(
            register_link.get_attribute('href'),
            '/register'
        )
    
    # or or click an affordance and navigate to a login page and log in
    # def test_user_can_navigate_to_login_page(self):
    def test_home_has_a_link_to_login_page(self):
        login_link = self.browser.find_element_by_id('login_button')
        self.assertEqual(
            login_link.get_attribute('href'),
            '/login'
        )

if __name__ == '__main__':
        unittest.main(warnings='ignore')