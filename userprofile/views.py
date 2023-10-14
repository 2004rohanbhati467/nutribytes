from django.shortcuts import render

# Create your views here.
def username(request):
    return render(request,'username.html')