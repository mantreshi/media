from django.urls import path
from .views import add_person,show_person,update_person


urlpatterns = [
    path('add-person/',add_person,name='add-person'),
    path('person-list/',show_person,name='person-list'),
    path('person-update/<pk>/',update_person,name='person-update'),
]