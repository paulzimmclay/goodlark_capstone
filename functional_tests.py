from selenium import webdriver
import unittest
import time


class NewVisitorRegister(unittest.TestCase):

    url = 'http://localhost:8000'
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_new_user_creates_account_and_fills_out_form(self):
        # When Penny, a high school senior, goes to apply for a Goodlark scholarship, she navigates to
        # the goodlark homepage. 
        self.browser.get(self.url)
        self.assertIn('Goodlark Educational Foundation', self.browser.title)

        # Here she sees an affordance to register and create a profile. 
        self.browser.get(self.url)
        register_link = self.browser.find_element_by_id('register_button')
        self.assertIn(
            '/register',
            register_link.get_attribute('href')
        )

        # Clicking on the register affordance takes her to the register page. 
        self.browser.get(self.url)
        login_link = self.browser.find_element_by_id('register_button')
        login_link.click()
        self.assertIn('Register', self.browser.title)

        

    
    def test_user_can_revisit_login_and_edit_existing_application(self):
        self.browser.get(self.url)
        login_link = self.browser.find_element_by_id('login_button')
        self.assertIn(
            '/login',
            login_link.get_attribute('href')
        )
        


if __name__ == '__main__':
    unittest.main(warnings='ignore')
