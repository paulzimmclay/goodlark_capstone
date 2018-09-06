from selenium import webdriver
import unittest
import time


class NewVisitorRegister(unittest.TestCase):

    url = 'http://localhost:8000'
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # When a prospective goodlark recipient arrives at the homepage...
    def test_user_can_load_the_homepage(self):
        self.browser.get(self.url)
        self.assertIn('Goodlark Educational Foundation', self.browser.title)

    # there is an affordance to navigate to a register page, and
    def test_home_has_a_link_to_register_page(self):
        self.browser.get(self.url)
        register_link = self.browser.find_element_by_id('register_button')
        print('this is the register link', register_link.get_attribute('href'))
        self.assertIn(
            '/register',
            register_link.get_attribute('href')
        )

    # there is an affordance to navigate to a login page and log in.
    def test_home_has_a_link_to_login_page(self):
        self.browser.get(self.url)
        login_link = self.browser.find_element_by_id('login_button')
        self.assertIn(
            '/login',
            login_link.get_attribute('href')
        )

    # Clicking on the register affordance navigates to a register page...
    def test_clicking_register_goes_to_a_registration_form(self):
        self.browser.get(self.url)
        login_link = self.browser.find_element_by_id('register_button')
        login_link.click()
        self.assertIn('Register', self.browser.title)

    #  with a form for creating a new user
    def test_register_submit_creates_a_new_user(self):
        pass


if __name__ == '__main__':
    unittest.main(warnings='ignore')
