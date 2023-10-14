from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout,authenticate

@login_required
def home(request):
    if request.user.is_authenticated:
        print("Hello,user")
    else:
        print("Please log in via username and password or register yourself!")
    user=authenticate(username='username',password='password')

    return render(request,'home.html')