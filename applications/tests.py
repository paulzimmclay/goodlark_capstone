from django.urls import resolve
from django.test import TestCase
from applications.views import home, register
from django.http import HttpRequest


def = get_page_contents(view):
    request = HttpRequest()
    response = view(request)
    html = response.content.decode('utf8')
    return html

class HomePageTest(TestCase):

    def get_page_contents(self, view):
        request = HttpRequest()
        response = view(request)
        html = response.content.decode('utf8')
        return html

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        html = self.get_page_contents(home)
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Goodlark Educational Foundation</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_has_link_to_register(self):
        html = self.get_page_contents(home)
        self.assertIn('<a href="/register" id="register_button">Register</a>', html)

    def test_home_page_has_link_to_login(self):
        html = self.get_page_contents(home)
        self.assertIn('<a href="/login" id="login_button">Login</a>', html)

    def test_register_url_resolves_to_register_page(self):
        found = resolve('/register')
        self.assertEqual(found.func, register)

    def test_register_returns_correct_html(self):
        response = self.client.get('/register')
        self.assertTemplateUsed(response, 'register.html')

class RegistrationFormTest(TestCase):

    def test_register_has_registration_form(self):
        html = self.get_page_contents(register)
        self.assertIn('<form>', html)

    def test_form_has_user_inputs(self):
        html = self.get_page_contents(register)
        self.assertIn('<input type="">', html)

    def test_registration_form_is_using_correct_form(self):
        form = RegistrationForm()
        self.fail(form.as_p())
