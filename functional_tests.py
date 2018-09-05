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

    # or or click an affordance and navigate to a login page and log in
    # def test_user_can_navigate_to_login_page(self):

if __name__ == '__main__':
        unittest.main(warnings='ignore')