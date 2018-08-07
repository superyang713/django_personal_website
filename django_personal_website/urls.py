from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('lab/', include('lab.urls', namespace='lab')),
    path('blog/', include('blog.urls', namespace='blog')),
]
