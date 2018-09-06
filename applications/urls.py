from django.conf.urls import url
from django.urls import include, path


from . import views

app_name = "applications"
urlpatterns = [
    url('', views.home, name='home'),
    url('/register', views.register, name='register')
]