from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=='POST':
        pass
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def forget_password(request):
    return render(request,'forget_password.html')