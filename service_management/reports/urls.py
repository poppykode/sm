from django.urls import path

from .views import assigned_resources

app_name='reports'
urlpatterns = [
  path('resources',assigned_resources,name="assigned_resources"),
]
