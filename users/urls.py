#!/usr/bin/python
from django.urls import path
from . import views
# from django.contrib.auth.views import login 旧版本
from django.contrib.auth.views import LoginView

app_name = 'user'
urlpatterns = [
    # path('login/', login, {'template_name', 'user/login.html'}, name='admin'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
