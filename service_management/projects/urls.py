from django.urls import path

from .views import(all_project_installation_assessement,
                   pai_create, details_pai, task_create, 
                   task_save, task_details, pai_comment,
                   comment_pai_delete,update_details_pai,update_pai,
                   CalendarView,delete_pai,task_pai_delete
                   )

app_name = 'projects'
urlpatterns = [
    path('overview', all_project_installation_assessement,
         name='all_project_installation_assessement'),
    path('pai/create', pai_create, name='pai_create'),
    path('pai/details/<int:pk>', details_pai, name='details_pai'),
    path('task/create/<int:user_id>/<int:pai_id>',
         task_create, name='task_create'),
    path('task/details/<int:user_id>/<int:pai_id>',
         task_details, name='task_details'),
    path('pai/update/<int:pk>', update_pai, name='update_pai'),
    path('task/save', task_save, name='task_save'),
    path('comment/post/<int:pk>', pai_comment, name='pai_comment'),
    path('comment/delete/<int:pk>', comment_pai_delete, name='comment_pai_delete'),
    path('pai/details/update/<int:pk>', update_details_pai, name='update_details_pai'),
    path('pai/calender',CalendarView.as_view(), name='calendar'),
    path('pai/delete/<int:pk>', delete_pai, name='delete_pai'),
    path('pai/task/delete/<int:pk>', task_pai_delete, name='task_pai_delete'),
]
