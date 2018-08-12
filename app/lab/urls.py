from django.urls import path
from lab import views

app_name = 'lab'

urlpatterns = [
    path('pressure_monitor', views.pressure_monitor, name='pressure_monitor'),
]
