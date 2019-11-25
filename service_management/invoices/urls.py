from django.urls import path

from .views import(
    invoices_overview, 
    generate_pdf,
    invoice_create,
    invoice_save,
    invoices_delete,
    invoices_details,
    quotation_create,
    quotation_save,
    quotations_overview
    ) 

app_name='invoices'
urlpatterns = [
    path('overview/quotations',invoices_overview,name='overview'),
    path('overview/invoices',quotations_overview,name='quotations_overview'),
    path('generate/invoice',generate_pdf,name='generate_pdf'),
    path('quotation/create/<int:pk>',invoice_create,name='invoice_create'),
    path('invoice/create',quotation_create,name='quotation_create'),
    path('invoice/view/<int:pk>',invoices_details,name='invoices_details'),
    path('invoice/delete/<int:pk>',invoices_delete,name='invoices_delete'),
    path('quotation/generate-pdf',invoice_save,name='invoice_save'),
    path('invoice/generate-pdf',quotation_save,name='quotation_save'),
]
