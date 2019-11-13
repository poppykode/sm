import datetime
from django.shortcuts import render,redirect,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from enquiries.models import Enquiry
from invoices.models import Invoice
from projects.models import ProjectInstallationAssessement,Task

# Create your views here.
@login_required
def admin_dashboard(request):
    template_name = 'dashboard/admin_dashboard.html'
    pai = ProjectInstallationAssessement.objects.all()
    qs = Enquiry.objects.all()
    inv = Invoice.objects.all()
    enq = qs.count()
    proj = pai.filter(type='project').count()
    installations = pai.filter(type='installation').count()   
    assessements_ = pai.filter(type='assement').count()
    inv_ =inv.count()
    context ={
        'enq':enq,
        'assessements':assessements_,
        'installations':installations,
        'proj':proj,
        'invoices':inv_
        }
    return render(request,template_name,context)

@login_required
def sales_dashboard(request):
    template_name = 'dashboard/sales_dashboard.html' 
    date = datetime.date.today()
    # events = Event.objects.filter(date__gt=datetime.now()).order_by('-date')
    qs = Enquiry.objects.filter(assigned_to=request.user.id).order_by('next_follow_up')
    enquiry_count = qs.count()
    context ={
        'obj':qs,
        'enquiry_count':enquiry_count,
        'date':date
    }
    return render(request,template_name,context)

@login_required
def technician_dashboard(request):
    template_name = 'dashboard/technician_dashboard.html'
    date = datetime.date.today()
    qs= ProjectInstallationAssessement.objects.filter(resources=request.user.id).order_by('end_date')
    print('apo')
    pai_count = qs.count()
    context ={
        'obj':qs,
        'pai_count':pai_count,
        'date':date
    }
    return render(request,template_name,context)

@login_required
def customer_services_dashboard(request):
    template_name = 'dashboard/customer_services__dashboard.html'
    context ={}
    return render(request,template_name,context)

@login_required
def toggle_task_status(request,pk):
    qs= get_object_or_404(Task,pk=pk)
    if qs.completed == False:
        qs.completed = True
        qs.save()
        messages.warning(request, 'Task status changed to not complete.')
        return redirect('projects:task_details', qs.user.id, qs.project_installation_assessement.id)
    else:
        qs.completed = False
        qs.save()
        messages.success(request, 'Task status changed to not complete.')
        return redirect('projects:task_details', qs.user.id, qs.project_installation_assessement.id)