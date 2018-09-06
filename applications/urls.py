from django.conf.urls import url
from django.urls import include, path


from . import views

app_name = "applications"
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register')
]