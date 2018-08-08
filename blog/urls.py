from django.urls import path
from blog.views import PostListView, PostDetailView

from blog import views


app_name = 'blog'

urlpatterns = [
    path(r'', PostListView.as_view(), name='post_list'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]
