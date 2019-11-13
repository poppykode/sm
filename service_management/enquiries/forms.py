from django import forms
from django.contrib.admin import widgets 
from .models import Enquiry,Comment
from accounts.models import User


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        labels = {
        "next_follow_up": "Next Follow Up Date",
        "service_mode":"Follow Up Mode",
        }
        widgets = {
            'next_follow_up': forms.DateInput(attrs={'class':'datepicker','type':'date','data-date-format':'YYYY-MM-DD'}),
            'attended_to': forms.TextInput(attrs={'type':'hidden','class':'datepicker'}),
            'address': forms.Textarea(attrs={'rows':1,},),
            'status': forms.TextInput(attrs={'readonly':True},),
        }
        fields = ('title','company','contact_name','email','phone_number','priority','assigned_to','channel','service','status','next_follow_up','attended_to','decription','website','service_mode','address') 

    # def __init__(self, user, *args, **kwargs):
    #     super(EnquiryForm, self).__init__(*args, **kwargs)
    #     self.fields['assigned_to'].queryset = User.designation.filter(user="sales")

class EnquiryDetailForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        labels = {
        "next_follow_up": "Next Follow Up Date",
        "service_mode":"Follow Up Mode",
        }
        widgets = {
            'next_follow_up': forms.DateInput(attrs={'onchange':'submit();','class':'datepicker','type':'hidden','data-date-format':'YYYY-MM-DD HH:mm'}),
            'address': forms.TextInput(attrs={'onchange':'submit();','type':'hidden',},),
            'status':forms.Select(attrs={'onchange':'submit();'},),
            'attended_to':forms.Select(attrs={'onchange':'submit();'},),
            'priority':forms.Select(attrs={'onchange':'submit();'},),
            'title':forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'company': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'contact_name': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'email': forms.EmailInput(attrs={'onchange':'submit();','type':'hidden'},),
            'phone_number': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'assigned_to': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'channel': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'service': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'decription': forms.TextInput(attrs={'onchange':'submit();','type':'hidden',},),
            'website': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'service_mode': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
        }
        fields = ('title','company','contact_name','email','phone_number','priority','assigned_to','channel','service','status','next_follow_up','attended_to','decription','website','service_mode','address')

       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        labels = {
        "decription": "Enter your comments/notes",
        }
        widgets ={
            'enquiry': forms.TextInput(attrs={'type':'hidden',},),
            'user': forms.TextInput(attrs={'type':'hidden',},),
        }
        fields = ('enquiry','decription','user')