from django.urls import path
from django.contrib.auth.views import login

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]
