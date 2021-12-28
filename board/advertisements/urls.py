from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisements_list, name='advertisements_list'),
    path('курс1/', views.course1, name='advertisements_list'),
    path('курс 2', views.course2, name='advertisements_list'),
    path('course3/', views.course3, name='advertisements_list'),
    # path('course4/', views.course4, name='advertisements_list'),
    # path('course5/', views.course5, name='advertisements_list'),
]
