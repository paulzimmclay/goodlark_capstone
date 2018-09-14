from django.conf.urls import url
from django.urls import include, path

from .views import *

app_name = "applications"
urlpatterns = [
    path('', home, name='home'),
    path('login_user', login_user, name='login_user'),
    path('logout_user', logout_user, name='logout_user'),
    path('register', register, name='register'),
    path('regular_application', regular_application, name='regular_application')
]
