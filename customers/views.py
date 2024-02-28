from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
# Create your views here.
def login_customer(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in ... quack! quack!")
            return redirect('shop:home')
        else:
            messages.success(request,("There was an error logging in, Try Again..."))
            return redirect('customers:login_customer')
    else:
        return render(request, 'registration/login.html', {})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration complete"))
            # return redirect('shop:home')
            return redirect('shop:update_profile')
    else:
        form = RegisterUserForm()
    
    return render(request, 'registration/register.html', {'form':form})
            
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('shop:home') 