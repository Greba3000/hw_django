from django.urls import path
from advertisements.views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('about', About.as_view(), name='about'),
    path('advertisements', AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisement_detail'),
]
