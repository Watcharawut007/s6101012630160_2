from django.urls import path

from . import views

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf.urls import include
app_name = 'calculate'
urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about,name='about'),
]