import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from enquiries.models import Enquiry
from projects.models import Task,ProjectInstallationAssessement


# Create your views here.

@login_required
def reports_overview(request):
    template_name='reports/reports_overview.html'
    qs = ProjectInstallationAssessement.objects.all()
    overdue_projects = qs.filter(type='project',end_date__lte = datetime.date.today()).exclude(status='completed').count()
    overdue_installation = qs.filter(type='installation',end_date__lte = datetime.date.today()).exclude(status='completed').count()
    overdue_assemet = qs.filter(type='assement',end_date__lte = datetime.date.today()).exclude(status='completed').count()
    overdue_enquiry = Enquiry.objects.filter(next_follow_up__lte = datetime.date.today()).exclude(status='won').count()
    context ={
        'obj':qs,
        'overdue_projects':overdue_projects,
        'overdue_installation':overdue_installation,
        'overdue_assemet':overdue_assemet,
        'overdue_enquiry':overdue_enquiry
    }
    return render(request,template_name,context)

@login_required
def assigned_resources(request):
    template_name ='reports/resource_assignment_overview.html'
    qs_pai = Task.objects.all().distinct()
    print(qs_pai)
    for u in qs_pai:
        print(u.user.username +" "+ u.project_installation_assessement.type +" "+ u.project_installation_assessement.title +" "+ u.decription)
    context ={
        'obj':qs_pai
    }
    return render(request,template_name,context)



    


