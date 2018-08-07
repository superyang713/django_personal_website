from django.urls import path
from home.views import AboutView, HomeView

app_name = 'home'

urlpatterns = [
    path(r'', HomeView.as_view(), name='index'),
    path(r'about', AboutView.as_view(), name='about'),
]
