import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from enquiries.models import Enquiry

# Create your views here.
@login_required
def contacts(request):
    template_name = 'contacts/contact.html'
    qs= Enquiry.objects.all()
    contacts_count = qs.count()
    context ={
        'obj':qs,
        'contacts_count':contacts_count,  
        }
    return render(request,template_name,context)