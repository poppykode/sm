from django.urls import path
from .views import (
    contacts,
)

app_name='contacts'
urlpatterns = [
    path('list',contacts,name='contact_list'),
  
]
