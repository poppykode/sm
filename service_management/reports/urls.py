from django.urls import path

from .views import assigned_resources,reports_overview

app_name='reports'
urlpatterns = [
  path('resources',assigned_resources,name="assigned_resources"),
  path('overview',reports_overview,name="reports_overview"),
]
