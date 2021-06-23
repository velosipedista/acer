from django.contrib import admin
from django.urls import path, include
from .views import index, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('create/', create),
    path('db/', include('db.urls')),
]
