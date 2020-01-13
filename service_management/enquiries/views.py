import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EnquiryForm,EnquiryDetailForm,CommentForm
from .models import Enquiry,Comment
from accounts.models import User

# Create your views here.
@login_required
def all_enquiries(request):
    template_name ='enquiries/enquiry_list.html'
    qs = Enquiry.objects.all()
    assigned = qs.exclude(assigned_to__isnull =True)
    un_assigned = qs.exclude(assigned_to__isnull =False)
    due = qs.filter(next_follow_up__lte = datetime.date.today()).exclude(attended_to='attended',state =True)
    un_attended = qs.exclude(attended_to='un-attended')
    all_ = qs.count()
    assigned_ = assigned.count()
    un_assigned_ = un_assigned.count()
    due_ = due.count()
    un_attended_ =un_attended.count()
    context ={
        'obj':qs,
        'all':all_,
        'assigned':assigned_,
        'un_assigned':un_assigned_,
        'due':due_,
        'un_attended':un_attended_
        }
    return render(request,template_name,context)

@login_required
def register_enquiry(request):
    template_name ='enquiries/enquiry_create.html'
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry successfully created.')
            return redirect(reverse('enquiries:overview'))
    else:
        form = EnquiryForm()
    return render(request,template_name,{'form':form})

@login_required
def delete_enquiry(request,pk):
    template_name ='enquiries/enquiry_delete.html'
    qs= get_object_or_404(Enquiry,pk=pk)    
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Enquiry has been successfully Deleted!')
        return redirect('enquiries:overview')
    return render(request,template_name, {'obj':qs})


@login_required
def update_enquiry(request,pk):
    template_name = 'enquiries/enquiry_edit.html'
    qs= get_object_or_404(Enquiry, pk=pk)
    print(request.POST.get('priority'))
    if request.method =='POST':
        form = EnquiryForm(request.POST,instance=qs)
        if form.is_valid():                          
            form.save()
            messages.success(request, 'Enquiry has been successfully updated!')
            return redirect('enquiries:enquiry_details',pk=pk)
        else:
            messages.error(request, 'Something Went Wrong!')
            return redirect('enquiries:enquiry_details',pk=pk)
    else:     
        context = {'form': EnquiryForm(instance=qs)}
    return render(request, template_name, context)

@login_required
def update_details_enquiry(request,pk):
    qs= get_object_or_404(Enquiry, pk=pk)
    if request.method =='POST':
        form = EnquiryForm(request.POST,instance=qs)
        print(form.errors.as_data())
        if form.is_valid():                          
            form.save()
            messages.success(request, 'Enquiry has been successfully updated!')
            return redirect('enquiries:enquiry_details',pk=pk)
        else:
            messages.error(request, 'Please assign a resource to project!')
            return redirect('enquiries:enquiry_details',pk=pk)
    else:     
        context = {'form': EnquiryDetailForm(instance=qs)}
    return redirect('enquiries:enquiry_details',pk=pk)

@login_required
def details_enquiries(request,pk):
    template_name = 'enquiries/enquiry_details.html'
    qs = get_object_or_404(Enquiry, pk=pk)
    qs_ = Comment.objects.filter(enquiry=pk)
    i = qs.invoice_set.filter(enquiry=pk)
    i_=i.count()
    context ={
        'obj':qs,
        'obj_':qs_,
        'form':EnquiryDetailForm(instance=qs),
        'form_1':CommentForm(),
        'generated_invoices':i_

    }
    return render(request,template_name,context)

@login_required
def enquiry_comment(request,pk):
    qs = get_object_or_404(Enquiry, pk=pk)
    current_user = get_object_or_404(User,pk=request.user.id)
    desc = request.POST.get('decription')
    if desc: 
        qs.comment_set.create(
            decription= desc,
            user= current_user,
        )
        messages.success(request, 'Comment successfully added')
        return redirect('enquiries:enquiry_details',pk=pk)
    elif not desc:
        messages.error(request, 'Description/Notes Cant be empty')
        return redirect('enquiries:enquiry_details',pk=pk)
    else:
        messages.error(request, 'something went wrong')
        return redirect('enquiries:enquiry_details',pk=pk)
        
@login_required
def delete_comment(request,pk):
    template_name ='enquiries/comment_delete.html'
    qs= get_object_or_404(Comment,pk=pk) 
    print('id yaho ka')
    print(qs.enquiry.id)   
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Comment has been successfully Deleted!')
        return redirect('enquiries:enquiry_details',pk=qs.enquiry.id)
    return render(request,template_name, {'obj':qs})

