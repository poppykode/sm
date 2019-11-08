import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ProjectInstallationAssessement,Task,Comment
from .forms import ProjectInstallationAssessementForm,CommentForm,TaskForm

# Create your views here.
@login_required
def all_project_installation_assessement(request):
    template_name = "projects/overview.html"
    qs = ProjectInstallationAssessement.objects.all()
    all =qs.count()
    assements = qs.filter(type='assement').count()
    projects = qs.filter(type='project').count()
    installations = qs.filter(type='installation').count()
    pending = qs.filter(status='pending').count()
    in_progress = qs.filter(status='in-progress').count()
    on_hold = qs.filter(status='on-hold').count()
    completed = qs.filter(status='completed').count()
    abandoned = qs.filter(status='abandoned').count()
    context = {
        'obj':qs,
        'assements':assements,
        'projects':projects,
        'installations':installations,
        'pending':pending,
        'on_hold':on_hold,
        'completed':completed,
        'abandoned':abandoned,
        'in_progress':in_progress,
        'all':all
    }
    return render(request,template_name,context)

@login_required
def book_create(request):
    template = "projects/pai_create.html"
    form = ProjectInstallationAssessementForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fbv:index')
    context = {"form": form}
    return render(request, template, context)

