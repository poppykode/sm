import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ProjectInstallationAssessement, Task, Comment
from .forms import ProjectInstallationAssessementForm, CommentForm, TaskForm, ProjectInstallationAssessementForm1
from accounts.models import User

# Create your views here.
@login_required
def all_project_installation_assessement(request):
    template_name = "projects/overview.html"
    qs = ProjectInstallationAssessement.objects.all()
    all = qs.count()
    assements = qs.filter(type='assement').count()
    projects = qs.filter(type='project').count()
    installations = qs.filter(type='installation').count()
    pending = qs.filter(status='pending').count()
    in_progress = qs.filter(status='in-progress').count()
    on_hold = qs.filter(status='on-hold').count()
    completed = qs.filter(status='completed').count()
    abandoned = qs.filter(status='abandoned').count()
    context = {
        'obj': qs,
        'assements': assements,
        'projects': projects,
        'installations': installations,
        'pending': pending,
        'on_hold': on_hold,
        'completed': completed,
        'abandoned': abandoned,
        'in_progress': in_progress,
        'all': all
    }
    return render(request, template_name, context)


@login_required
def pai_create(request):
    template = "projects/pai_create.html"
    form = ProjectInstallationAssessementForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projects:all_project_installation_assessement')
    context = {"form": form}
    return render(request, template, context)


@login_required
def details_pai(request, pk):
    template_name = 'projects/pai_details.html'
    qs = get_object_or_404(ProjectInstallationAssessement, pk=pk)
    qs_ = Comment.objects.filter(project_installation_assessement=pk)
    r = qs.resources.all()
    tasks = qs.task_set.all()

    context = {
        'obj': qs,
        'obj_': qs_,
        'form': ProjectInstallationAssessementForm1(instance=qs),
        'form_1': CommentForm(),
        'resoures': r,
        'task':tasks
    }
    return render(request, template_name, context)

@login_required
def task_details(request,user_id,pai_id):
    template_name = 'projects/task_details.html'
    pai =get_object_or_404(ProjectInstallationAssessement, pk=pai_id)
    user = get_object_or_404(User, pk=user_id)
    print('user who has the tasks')
    print(user.username)
    print('currently logged in user')
    print(request.user.username)
    tasks = Task.objects.filter(user=user,project_installation_assessement=pai)
    context ={
        'obj' :tasks,
        'pai':pai,
        'user_':user
    }
    return render(request,template_name,context)


@login_required
def task_create(request, user_id, pai_id):
    template_name = 'projects/user_task.html'
    qs = get_object_or_404(ProjectInstallationAssessement, pk=pai_id)
    usr = get_object_or_404(User, pk=user_id)
    context = {
        'obj': qs,
        'usr': usr
    }
    return render(request, template_name, context)


@login_required
def task_save(request):
    if request.method == 'POST':
        start_date = request.POST.getlist('start_date')
        end_date = request.POST.getlist('end_date')
        description = request.POST.getlist('description')
        pai_id = int(request.POST.get('pai_id'))
        usr_id = int(request.POST.get('usr_id'))
        user = get_object_or_404(User, pk=usr_id)
        pai =get_object_or_404(ProjectInstallationAssessement, pk=pai_id)
        c = min([len(description), len(start_date), len(end_date)])
        for i in range(c):
            tc = Task.objects.create(
                user=user,
                project_installation_assessement=pai,
                start_date = start_date[i],
                end_date =end_date[i],
                decription =description[i]
            )
        
        messages.success(request, 'Task/s successfully added')
        return redirect('projects:task_details',user_id = usr_id,pai_id=pai_id)
    messages.success(request,'Something went wrong')
    return redirect('projects:all_project_installation_assessement')

@login_required
def pai_comment(request,pk):
    qs = get_object_or_404(ProjectInstallationAssessement, pk=pk)
    current_user = get_object_or_404(User,pk=request.user.id)
    desc = request.POST.get('decription')
    if desc: 
        qs.comment_set.create(
            decription= desc,
            user= current_user,
        )
        messages.success(request, 'Comment successfully added')
        return redirect('projects:details_pai',pk=pk)
    elif not desc:
        messages.error(request, 'Description/Notes Cant be empty')
        return redirect('projects:details_pai',pk=pk)
    else:
        messages.error(request, 'something went wrong')
        return redirect('projects:details_pai',pk=pk)

# HAS ISSUES
@login_required
def delete_comment(request,pk):
    template_name ='projects/comment_delete.html'
    qs= get_object_or_404(Comment,pk=pk)
    print('apo')
    print(qs.decription) 
    print(qs.project_installation_assessement.id)   
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Comment has been successfully Deleted!')
        return redirect('projects:all_project_installation_assessement')
    return render(request,template_name, {'obj':qs})

@login_required
def update_details_pai(request,pk):
    qs= get_object_or_404(ProjectInstallationAssessement, pk=pk)
    if request.method =='POST':
        form = ProjectInstallationAssessementForm1(request.POST,instance=qs)
        print(form.errors.as_data())
        if form.is_valid():                          
            form.save()
            messages.success(request, 'Successfully updated!')
            return redirect('projects:details_pai',pk=pk)
        else:
            messages.error(request, 'Please assign a resource to project!')
            return redirect('projects:details_pai',pk=pk)
    else:     
        context = {'form': ProjectInstallationAssessementForm1(instance=qs)}
    return redirect('projects:details_pai',pk=pk)

@login_required
def update_pai(request,pk):
    template_name = 'projects/pai_edit.html'
    qs= get_object_or_404(ProjectInstallationAssessement, pk=pk)
    if request.method =='POST':
        form = ProjectInstallationAssessementForm(request.POST,instance=qs)
        print(form.errors.as_data())
        if form.is_valid():                          
            form.save()
            messages.success(request, 'Update succesfull.')
            return redirect('projects:details_pai',pk=pk) 
    else:   
        context = {'form': ProjectInstallationAssessementForm(instance=qs)}
    return render(request, template_name, context)