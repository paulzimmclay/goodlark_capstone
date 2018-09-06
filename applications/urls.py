from django.conf.urls import url
from django.urls import include, path


from . import views

app_name = "applications"
urlpatterns = [
    url(r'^$', views.home, name='home'),
]