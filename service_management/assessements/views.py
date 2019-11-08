from django.shortcuts import render,redirect,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from enquiries.models import Enquiry


# Create your views here.
@login_required
def assements_list(request):
    template_name ='assessements/assessements_list.html'
    qs = Enquiry.objects.filter(status='assement')
    context ={
        'obj':qs
    }
    return render(request,template_name,context)


