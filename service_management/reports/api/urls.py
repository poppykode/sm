from django.urls import path

from .views import sales_funel,project_overview

urlpatterns = [
    path('sale-funel',sales_funel),
    path('project-overview',project_overview), 
]
