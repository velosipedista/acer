from django.urls import path
from .views import enter, show_list

urlpatterns = [
    path('enter/', enter),
    path('list/', show_list),
]
