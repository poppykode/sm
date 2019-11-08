from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import User

# Create your views here.
def login_page(request):
    if request.user:
        return redirect('accounts:redirect_to_dashboard')
    template_name = 'registration/login.html'
    return render(request,template_name,{})

def login(request):
    template_name='registration/login.html'
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    print('God is in it')
    print(username)
    print(password)
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return  redirect(reverse('accounts:redirect_to_dashboard'))  
    else:
        messages.error(request,'Invalid username or password.') 
        return render(request,template_name) 

@login_required
def sign_up_page(request):
    template_name = 'registration/sign_up.html'
    form = SignUpForm()
    return render(request,template_name,{'form':form})

@login_required
def sign_up(request):
    template_name = 'registration/sign_up.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            designation = request.POST.get('designation')
            if designation == 'admin':
                new_form.is_superuser = True
            elif designation == 'sales':
                new_form.is_sales = True
            elif designation =='tech':
                new_form.is_technician = True
            else:
                new_form.is_customer_services =True
            new_form.save()       
            messages.success(request, 'User has been created')
            return redirect(reverse('accounts:users'))
    else:
        form = SignUpForm()    
    return render(request,template_name,{'form':form})

@login_required
def redirect_to_dashboard(request):
    user = request.user
    if user.is_superuser:
        messages.success(request, 'Welcome ' + user.username)
        return redirect('dashboard:admin')
    elif user.is_sales:
        messages.success(request, 'Welcome ' + user.username)
        return redirect('dashboard:sales')
    elif user.is_technician:
        messages.success(request, 'Welcome ' + user.username)
        return redirect('dashboard:technican')
    elif user.is_customer_services:
        messages.success(request,'Welcome ' + user.username)
        return redirect('enquiries:overview')
    messages.error(request,'please login.')
    return redirect('accounts:login')

@login_required
def users(request):
    template_name = 'registration/users/users.html' 
    # to exclude logged in user
    qs = User.objects.filter().exclude(username = request.user.username)
    return render(request,template_name,{'obj':qs})

@login_required
def toggle_user_status(request,pk):
    qs= get_object_or_404(User,pk=pk) 
    print('users')
    print(qs.is_active)
    if qs.is_active == True:
        qs.is_active = False
        qs.save()
        messages.warning(request, 'Status successfully deacivated.')
        return redirect(reverse('accounts:users'))
    else:
        qs.is_active = True
        qs.save()
        messages.success(request, 'Status successfully activated.')
        return redirect(reverse('accounts:users'))


