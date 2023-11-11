from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def Signin(request):
    return render(request,'signin.html')

def password(request):
    return render(request,'password.html')
