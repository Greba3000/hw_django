from django.urls import path

from users_app.views import UsersLoginView, UsersLogoutView

urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(), name='logout')
]