from django import forms

from .models import ProjectInstallationAssessement, Comment, Task
from accounts.models import User


class ProjectInstallationAssessementForm(forms.ModelForm):
    class Meta:
        model = ProjectInstallationAssessement
        labels = {
            "resources": "Team Member(s)",
            "end_date": "Closing Date",
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'datetime-local'},format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'datetime-local'},format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 4, },),
        }
        fields = ("type","title", "client", "start_date", "end_date", "resources",
                  "description", "status", "value", )

    def __init__(self, *args, **kwargs):
        super(ProjectInstallationAssessementForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['resources'].queryset = User.objects.filter(designation="tech")


class ProjectInstallationAssessementForm1(forms.ModelForm):
    class Meta:
        model = ProjectInstallationAssessement
        labels = {
            "resources": "Team Member(s)",
            "end_date": "Closing Date",
            "resources":"",
        }
        widgets = {
            'type': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'title': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'status':forms.Select(attrs={'onchange':'submit();'},),
            'client': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'value': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
            'resources': forms.SelectMultiple(attrs={'onchange':'submit();','type':'hidden','id':'div_id_resources2'},),
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'hidden', 'data-date-format': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'hidden', 'data-date-format': 'YYYY-MM-DD'}),
            'description': forms.TextInput(attrs={'onchange':'submit();','type':'hidden'},),
        }
        fields = ("type","title", "client", "start_date", "end_date", "resources",
                  "description", "status", "value", )

    def __init__(self, *args, **kwargs):
        super(ProjectInstallationAssessementForm1, self).__init__(*args, **kwargs)
        self.fields['resources'].queryset = User.objects.filter(designation="tech")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {
            "decription": "Enter your comments/notes",
        }
        widgets = {
            'project_installation_assessement': forms.TextInput(attrs={'type': 'hidden', },),
            'user': forms.TextInput(attrs={'type': 'hidden', },),
        }
        fields = ('project_installation_assessement', 'decription', 'user')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        labels = {
            "decription": "Enter Task",
        }
        widgets = {
            'project_installation_assessement': forms.TextInput(attrs={'type': 'hidden', },),
            'user': forms.TextInput(attrs={'type': 'hidden', },),
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
        }
        fields = ('project_installation_assessement',
                  'decription', 'user', 'start_date', 'end_date')
