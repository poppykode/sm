from django import forms

from .models import ProjectInstallationAssessement, Comment, Task


class ProjectInstallationAssessementForm(forms.ModelForm):
    class Meta:
        model = ProjectInstallationAssessement
        labels = {
            "resources": "Team Member(s)",
            "end_date": "Closing Date",
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            'description': forms.Textarea(attrs={'rows': 4, },),
        }
        fields = ("title", "client", "start_date", "end_date", "resources",
                  "description", "status", "value", )


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
