from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, UpdateProfile
from django.views import generic
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.models import auth
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if User.objects.filter(username=form.data.get('username')).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=form.data.get('email')).exists():
            messages.error(request, 'Email already exists')
        elif form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.info(request, 'regestration success please login')
            return redirect("/accounts/login")
        return redirect("/accounts/signup")
    else:
        form = UserForm()
        print(form.media)
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("/home")
        else :
            messages.error(request, 'Invalid credentials!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.info(request, 'Please login to see your profile')
        return redirect("/accounts/login")

def editprofile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = UpdateProfile(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
            return redirect("/home")
        else:
            form = UpdateProfile(instance = request.user)
            return render(request, 'editprofile.html', {'form':form})
    else:
        messages.info(request, 'Please login to edit your profile')
        return redirect("/accounts/login")

def changepassword(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Password changed succesfully! Please login with new password')
            return redirect("/accounts/login")
        else :
            return redirect("/accounts/changepassword")
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'changepassword.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect("/home")