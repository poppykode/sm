from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","email","first_name","last_name","is_superuser","is_sales","is_customer_services","is_sub_contractor","designation","password1", "password2")