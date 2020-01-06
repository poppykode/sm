from django.urls import path

from .views import (all_faults, log_fault, details_fault,
                    fault_comment, update_details_fault, delete_comment,
                    delete_fault,user_faults,update_fault,faulty_logging_assignment)

app_name = 'faulty_logging'
urlpatterns = [
    path('overview/', all_faults, name='overview'),
    path('create/', log_fault, name="create"),
    path('details/<int:pk>', details_fault, name="fault_details"),
    path('comment/<int:pk>', fault_comment, name="fault_comment"),
    path('comment/delete/<int:pk>', delete_comment, name="delete_comment"),
    path('fault/delete/<int:pk>', delete_fault, name="delete_fault"),
    path('fault/edit/<int:pk>', update_fault, name="update_fault"),
    path('update-details-fault/<int:pk>',
         update_details_fault, name="update_details_fault"),
    path('faults/', user_faults, name="user_faults"),
    path('assigned/faults', faulty_logging_assignment, name="faulty_logging_assignment"),
]
