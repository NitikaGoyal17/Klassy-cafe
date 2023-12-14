from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/login')
def home(request):
     if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        number_guests= request.POST.get('number_guests')
        date= request.POST.get('date')
        time= request.POST.get('time')
        message= request.POST.get('message')
        
        user = Contact(name= name, email= email,  phone= phone, number_guests= number_guests, date= date, time= time, message= message)
        user.save()
     return render(request,"home.html")

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,"login.html")

def signup(request):
    frm= UserCreationForm()
    if request.method=='POST':
        frm= UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('login')
    return render(request,"signup.html", {'fm': frm})

def logoutuser(request):
    logout(request)
    return redirect("login")