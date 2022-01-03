from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('contacts', views.Contacts.as_view(), name='contacts'),
    path('about', views.About.as_view(), name='about'),
    path('advertisements', views.Advertisements.as_view(), name='advertisements'),
]
