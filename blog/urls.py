from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.index, name='index'),
]
