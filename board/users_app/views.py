from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render

# from users_app.forms import AuthForm


class UsersLoginView(LoginView):
    template_name = 'users/login.html'

class UsersLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = '/news/'