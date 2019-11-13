from django import forms
from .models import FaultyLogging
from .models import Comment


class FaultyLogForm(forms.ModelForm):
    class Meta:
        model = FaultyLogging
        labels = {
            "necompanyxt_follow_up": "Client",
            "faulty_close_date": "Fault Closing Date",
        }
        widgets = {
            'faulty_close_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            'faulty_decription': forms.Textarea(attrs={'rows': 4, },),
        }
        fields = ("title", "priority", "company", "email", "phone_number",
                  "assigned_to", "status", "service", "faulty_decription", "faulty_close_date")

class FaultyLogForm2(forms.ModelForm):
    class Meta:
        model = FaultyLogging
        labels = {
            "company": "Client",
            "faulty_close_date": "Fault Closing Date",
            "assigned_to":"",
        }
        widgets = {
            'status':forms.Select(attrs={'onchange':'submit();'},),
            'faulty_close_date': forms.DateInput(attrs={'onchange':'submit();','class': 'datepicker', 'type': 'hidden', 'data-date-format': 'YYYY-MM-DD'}),    
            'faulty_decription': forms.TextInput(attrs={'onchange':'submit();','type':'hidden',},),
            'title':forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'priority': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'company': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'email': forms.EmailInput(attrs={'onchange':'submit();','type':'hidden'},),
            'phone_number': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'assigned_to': forms.SelectMultiple(attrs={'onchange':'submit();','type':'hidden','id':'div_id_assigned_to2'},),
            'service': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
        }
        fields = ("title", "priority", "company", "email", "phone_number",
                  "assigned_to", "status", "service", "faulty_decription", "faulty_close_date")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        labels = {
        "decription": "Enter your comments/notes",
        }
        widgets ={
            'fault': forms.TextInput(attrs={'type':'hidden',},),
            'user': forms.TextInput(attrs={'type':'hidden',},),
        }
        fields = ('fault','decription','user')
