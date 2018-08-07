from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'about', views.about, name='about'),
]
