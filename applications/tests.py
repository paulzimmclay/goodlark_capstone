from django.urls import resolve
from django.test import TestCase
from applications.views import home
from django.http import HttpRequest

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
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Goodlark Educational Foundation</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_has_link_to_register(self):
        home_html = self.get_page_contents(home)
        print(home_html)
        self.assertIn('<a href="/register">Register</a>'))