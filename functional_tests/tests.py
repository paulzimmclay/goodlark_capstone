from django.test import LiveServerTestCase
import time


from selenium import webdriver


class NewVisitorRegister(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    def url(self):
        return self.live_server_url
    
    def test_new_user_creates_account_and_fills_out_form(self):
        # When Penny, a high school senior, goes to apply for a Goodlark scholarship, she navigates to
        # the goodlark homepage. 
        self.browser.get(self.url())
        self.assertIn('Goodlark Educational Foundation', self.browser.title)

        # Here she sees an affordance to register and create a profile. 
        self.browser.get(self.url())
        register_link = self.browser.find_element_by_id('register_button')
        self.assertIn(
            '/register',
            register_link.get_attribute('href')
        )

        # Clicking on the register affordance takes her to the register page. 
        self.browser.get(self.url())
        login_link = self.browser.find_element_by_id('register_button')
        login_link.click()
        self.assertIn('Register', self.browser.title)
        time.sleep(.5)

        # She fills out the form and submits it
        email_field = self.browser.find_element_by_id('id_email')
        email_field.send_keys('penny@pennyzc.com')
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

        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys('unomoobubba')
        time.sleep(.5)

        submit_button = self.browser.find_element_by_name('submit')
        submit_button.click()

        time.sleep(.5)

        # Penny is now logged in, and can click on the 'application form' affordance
        application_form_button = self.browser.find_element_by_id('regular_application_button')
        application_form_button.click()

        time.sleep(.5)

        # Penny sees a new page with the application form. Some of the fields are already filled out:
        first_name = self.browser.find_element_by_id('id_first_name')
        first_name_value = first_name.get_attribute('value')
        self.assertIsNotNone(first_name_value)
        
        last_name = self.browser.find_element_by_id('id_last_name')
        last_name_value = last_name.get_attribute('value')
        self.assertIsNotNone(last_name_value)

        # There are empty fields that she fills out:
        mailing_address = self.browser.find_element_by_id('id_mailing_address')
        mailing_address_value = mailing_address.get_attribute('value')
        self.assertEqual('', mailing_address_value)

        mailing_address.send_keys('123 Scholar St.')

        # She submits the form
        save_button = self.browser.find_element_by_id('application_save')
        save_button.click()

        # She logs out, then logs back in:
        logout_button = self.browser.find_element_by_id('logout_button')
        logout_button.click()

        login_button = self.browser.find_element_by_id('login_button')
        login_button.click()

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('pennyzc')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('unomoobubba')

        login_submit = self.browser.find_element_by_id('login_submit')
        login_submit.click()

        application_form_button = self.browser.find_element_by_id('regular_application_button')
        application_form_button.click()

        # Her work having been saved, she continues to fill out the form...
        

        


if __name__ == '__main__':
    unittest.main(warnings='ignore')
