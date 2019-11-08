from django.urls import path
from .views import (
    all_enquiries,
    register_enquiry,
    delete_enquiry,
    update_enquiry,
    details_enquiries,
    update_details_enquiry,
    enquiry_comment,
    delete_comment,
)

app_name='enquiries'
urlpatterns = [
    path('overview/',all_enquiries, name="overview"),
    path('create/',register_enquiry, name="create"),
    path('delete/enquiry/<int:pk>',delete_enquiry , name='enquiry_delete'),
    path('delete/comment/<int:pk>',delete_comment , name='delete_comment'),
    path('edit/<int:pk>',update_enquiry, name='enquiry_update'),
    path('d/edit/<int:pk>',update_details_enquiry, name='update_details_enquiry'),
    path('view/<int:pk>',details_enquiries, name='enquiry_details'),
    path('comment/<int:pk>',enquiry_comment, name="enquiry_comment"),
]
