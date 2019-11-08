import datetime
from django.shortcuts import render,redirect,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from enquiries.models import Enquiry
from invoices.models import Invoice

# Create your views here.
@login_required
def admin_dashboard(request):
    template_name = 'dashboard/admin_dashboard.html'
    qs = Enquiry.objects.all()
    inv = Invoice.objects.all()
    assessements = qs.filter(status='assement')
    contacts=qs.count()
    inv_ =inv.count()
    assessements_ = assessements.count()
    context ={
        'contacts':contacts,
        'assessements':assessements_,
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
    context ={}
    return render(request,template_name,context)

@login_required
def customer_services_dashboard(request):
    template_name = 'dashboard/customer_services__dashboard.html'
    context ={}
    return render(request,template_name,context)

