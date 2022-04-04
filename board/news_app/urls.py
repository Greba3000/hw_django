from django.urls import path
from news_app.views import *


urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:profile_id>/', NewsDetailView.as_view(), name='news_detail'),  # откуда прилетает значение в pk?
    path('news/add_news1/', AddNews.as_view(), name='add_news'),
    path('news/<int:profile_id>/edit/', UpdNews.as_view(), name='upd_news'),
    path('news/<int:profile_id>/leave_comment/', LeaveComment.as_view(), name='leave_comment'),
]
