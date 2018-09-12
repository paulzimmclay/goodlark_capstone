from django.conf.urls import url
from django.urls import include, path

from . import views

app_name = "applications"
urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('regular_application', views.regular_application, name='regular_application')
]
