from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from enquiries.models import Enquiry
from projects.models import Task


# Create your views here.
@login_required
def assigned_resources(request):
    template_name ='reports/resource_assignment_overview.html'
    qs_pai = Task.objects.all()
    print(qs_pai)
    for u in qs_pai:
        print(u.user.username +" "+ u.project_installation_assessement.type +" "+ u.project_installation_assessement.title +" "+ u.decription)
    context ={
        'obj':qs_pai
    }
    return render(request,template_name,context)



    


