import time
import unittest

from selenium import webdriver


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
        time.sleep(.5)

        # She fills out the form and submits it
        email_field = self.browser.find_element_by_id('id_email')
        email_field.send_keys('penny@pennyzc.com')
        time.sleep(.5)

        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys('unomoobubba')
        time.sleep(.5)

        first_name_field = self.browser.find_element_by_id('id_first_name')
        first_name_field.send_keys('penny')
        time.sleep(.5)

        last_name_field = self.browser.find_element_by_id('id_last_name')
        last_name_field.send_keys('zc')
        time.sleep(.5)

        username_field = self.browser.find_element_by_id('id_username')
        username_field.send_keys('pennyzc')
        time.sleep(.5)

        submit_button = self.browser.find_element_by_name('submit')
        submit_button.click()

        time.sleep(.5)

        # Penny is now logged in, and can click on the 'application form' affordance
        application_form_button = self.browser.find_element_by_id('application_form_button')
        application_form_button.click()

        time.sleep(.5)

    
    # def test_user_can_revisit_login_and_edit_existing_application(self):
        # self.browser.get(self.url)
        # login_link = self.browser.find_element_by_id('login_button')
        # self.assertIn(
        #     '/login',
        #     login_link.get_attribute('href')
        # )
        # pass


if __name__ == '__main__':
    unittest.main(warnings='ignore')
