from django.urls import path
from .views import (
    admin_dashboard,
    sales_dashboard,
    technician_dashboard,
    customer_services_dashboard,
)
app_name='dashboard'
urlpatterns = [
    path('admin',admin_dashboard,name='admin'),
    path('sales',sales_dashboard,name='sales'),
    path('technician',technician_dashboard,name='technician'),
    path('customer-services',customer_services_dashboard,name='customer_services'),  
]