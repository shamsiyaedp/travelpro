from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import travel
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    a=travel.objects.all()
    return render(request,'index.html',{'b':a})

