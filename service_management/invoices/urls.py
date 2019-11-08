from django.urls import path

from .views import(
    invoices_overview, 
    generate_pdf,
    invoice_create,
    invoice_save,
    invoices_delete,
    invoices_details
    ) 

app_name='invoices'
urlpatterns = [
    path('overview',invoices_overview,name='overview'),
    path('generate/invoice',generate_pdf,name='generate_pdf'),
    path('invoice/create/<int:pk>',invoice_create,name='invoice_create'),
    path('invoice/view/<int:pk>',invoices_details,name='invoices_details'),
    path('invoice/delete/<int:pk>',invoices_delete,name='invoices_delete'),
    path('invoice/generate-pdf',invoice_save,name='invoice_save')
]
