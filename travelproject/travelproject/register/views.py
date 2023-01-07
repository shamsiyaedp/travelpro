from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth


# Create your views here.

def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return render(request,'forms.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'you are logged in')
            return redirect('/')  
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    return render(request,'login.html')
   

def forms(request):
    return render(request,'forms.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password1']
        cpassword=request.POST['password2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return render(request,'forms.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return render(request,'forms.html')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                messages.info(request,'success')
                return redirect('/')
                
        else:
            messages.info(request,'password not matching')
            return render(request,'forms.html')
    return redirect('/')

    