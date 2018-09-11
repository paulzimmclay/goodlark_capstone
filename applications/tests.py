from django.urls import resolve
from django.test import TestCase
from applications.views import home, register
from django.http import HttpRequest
from applications.forms import RegistrationForm
from django.contrib.auth.models import User

### Cross-test Helper Functions:

def get_page_contents(view):
    request = HttpRequest()
    response = view(request)
    html = response.content.decode('utf8')
    return html

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        html = get_page_contents(home)
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Goodlark Educational Foundation</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_has_link_to_register(self):
        html = get_page_contents(home)
        self.assertIn('<a href="/register" id="register_button">Register</a>', html)

    def test_home_page_has_link_to_login(self):
        html = get_page_contents(home)
        self.assertIn('<a href="/login" id="login_button">Login</a>', html)

    def test_register_url_resolves_to_register_page(self):
        found = resolve('/register')
        self.assertEqual(found.func, register)

    def test_register_returns_correct_html(self):
        response = self.client.get('/register')
        self.assertTemplateUsed(response, 'register.html')

class RegistrationFormTest(TestCase):

    def test_registration_page_has_register_in_title(self):
        html = get_page_contents(register)
        self.assertIn('<title>Register</title>', html)
    
    def test_register_has_registration_form(self):
        html = get_page_contents(register)
        self.assertIn('<form', html)

    def test_form_has_user_inputs(self):
        html = get_page_contents(register)
        self.assertIn('<input', html)

    def test_registration_form_valid_submission_is_valid(self):
        form = RegistrationForm({
            'first_name':'coffee',
            'last_name':'coffee',
            'username':'coffee',
            'email':'coffee@coffee.com',
            'password':'coffeecoffee',
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.first_name, 'coffee')
        self.assertEqual(user.last_name, 'coffee')
        self.assertEqual(user.username, 'coffee')
        self.assertEqual(user.email, 'coffee@coffee.com')
        self.assertEqual(user.password, 'coffeecoffee')

    # def test_user_can_be_created_in_database(self):
    #     new_user = User.objects.create_user({
    #         'first_name':'coffee',
    #         'last_name':'coffee',
    #         'username':'coffee',
    #         'email':'coffee@coffee.com',
    #         'password':'coffeecoffee',
    #     })
    #     new_user.save()
    #     print(new_user)
    #    self.assertEqual

        

