import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import FaultyLogForm,FaultyLogForm2
from .models import FaultyLogging,Comment
from accounts.models import User
from enquiries.forms import CommentForm

# Create your views here.
@login_required
def all_faults(request):
    template_name = 'faulty_logging/fault_list.html'
    qs = FaultyLogging.objects.all()
    all = qs.count()
    due = qs.filter(faulty_close_date__lt =datetime.date.today()).exclude(status='closed').count()
    closed = qs.filter(status='closed').count()
    wip = qs.filter(status='wip').count()
    open = qs.filter(status='open').count()
    context = {
        'obj': qs,
        'all':all,
        'due':due,
        'closed':closed,
        'wip':wip,
        'open':open
    }
    return render(request, template_name, context)

@login_required
def details_fault(request,pk):
    template_name = 'faulty_logging/fault_details.html'
    qs = get_object_or_404(FaultyLogging, pk=pk)
    qs_ = Comment.objects.filter(fault=pk)
    # i = qs.invoice_set.filter(enquiry=pk)
    # is_assessement =qs.assessment_date
    print("tasting the waters")
    r = qs.assigned_to.all()
    context ={
        'obj':qs,
        'obj_':qs_,
        'form':FaultyLogForm2(instance=qs),
        'form_1':CommentForm(),
        'assigned':r,
    }
    return render(request,template_name,context)

@login_required
def update_details_fault(request,pk):
    qs= get_object_or_404(FaultyLogging, pk=pk)
    if request.method =='POST':
        form = FaultyLogForm2(request.POST,instance=qs)
        print(form.errors.as_data())
        if form.is_valid():                          
            form.save()
            messages.success(request, 'Fault has been successfully updated!')
            return redirect('faulty_logging:fault_details',pk=pk)
    messages.error(request, 'Please assign a resource to project!') 
    return redirect('faulty_logging:fault_details',pk=pk)


@login_required
def log_fault(request):
    template_name = 'faulty_logging/fault_create.html'
    if request.method == 'POST':
        form = FaultyLogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fault logged successfully.')
            return redirect(reverse('faulty_logging:overview'))
    else:
        form = FaultyLogForm()
    return render(request, template_name, {'form': form})

@login_required
def fault_comment(request,pk):
    qs = get_object_or_404(FaultyLogging, pk=pk)
    current_user = get_object_or_404(User,pk=request.user.id)
    print(current_user)
    desc = request.POST.get('decription')
    print(desc)
    print(type(desc))
    if desc: 
        qs.comment_set.create(
            decription= desc,
            user= current_user,
        )
        messages.success(request, 'Comment successfully added')
        return redirect('faulty_logging:fault_details',pk=pk)
    elif not desc:
        messages.error(request, 'Description/Notes Cant be empty')
        return redirect('faulty_logging:fault_details',pk=pk)
    else:
        messages.error(request, 'something went wrong')
        return redirect('faulty_logging:fault_details',pk=pk)

@login_required
def delete_comment(request,pk):
    template_name ='faulty_logging/comment_delete.html'
    qs= get_object_or_404(Comment,pk=pk) 
    print(qs.fault.id)   
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Comment has been successfully Deleted!')
        return redirect('faulty_logging:fault_details',pk=qs.fault.id)
    return render(request,template_name, {'obj':qs})

@login_required
def delete_fault(request,pk):
    template_name ='faulty_logging/fault_delete.html'
    qs= get_object_or_404(FaultyLogging,pk=pk)    
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Fault has been successfully Deleted!')
        return redirect('faulty_logging:overview')
    return render(request,template_name, {'obj':qs})