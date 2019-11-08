from django.urls import path

from .views import all_project_installation_assessement

app_name='projects'
urlpatterns = [
    path('overview',all_project_installation_assessement, name='all_project_installation_assessement') 
]
