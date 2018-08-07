from django.urls import path
from blog.views import PostListView, PostDetailView


app_name = 'blog'

urlpatterns = [
    path(r'', PostListView.as_view(), name='post_list'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
]
