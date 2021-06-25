from django.urls import path
from .views import enter, show_list, query_person_by_name, apply
from .views import  query_person_by_age, query_person_by_id, edit_person

urlpatterns = [
    path('enter/', enter),
    path('list/', show_list),
    path('query_by_name/', query_person_by_name),
    path('query_by_age/', query_person_by_age),
    path('query_by_id/', query_person_by_id),
    path('query_by_id/', query_person_by_id),
    path('edit_person/<int:pk>', edit_person),
    path('apply/<int:pk>', apply),

]
