# blog/urls.py

from django.urls import path
from .views import PostListView, post_detail_view

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
]
