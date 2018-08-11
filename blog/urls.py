from django.urls import path
from blog.views import PostListView, PostDetailView

from blog import views


app_name = 'blog'

urlpatterns = [
    path(r'', PostListView.as_view(), name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('edit/<slug:slug>', views.post_edit, name='post_edit'),
    path('remove/<slug:slug>', views.post_remove, name='post_remove'),
    path('comment/<slug:slug>', views.post_comment, name='post_comment'),
    path('tag/<int:pk>', views.tag_search_result, name='tag_search_result'),
    path('search/', views.search, name='search'),
]
