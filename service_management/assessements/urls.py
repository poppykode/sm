from django.urls import path

from .views import assements_list

app_name='assessements'
urlpatterns = [
    path('view',assements_list,name="assements_list"),
]
