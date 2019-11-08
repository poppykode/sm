from django.urls import path
from .views import (
    login,
    redirect_to_dashboard,
    sign_up,
    sign_up_page,
    users,
    toggle_user_status,
)

app_name='accounts'
urlpatterns = [
    path('login',login,name='login'),
    path('redirect',redirect_to_dashboard,name='redirect_to_dashboard'),
    path('sign-up',sign_up_page,name='sign_up_page'), 
    path('sign-up-url',sign_up,name='sign_up'),
    path('users',users,name='users'),
    path('status/<int:pk>',toggle_user_status,name='toggle_user_status')
]
