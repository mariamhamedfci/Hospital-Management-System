
from django.shortcuts import render , redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import authenticate, login , logout # type: ignore

def About(request):
    return render(request , "about.html")

def Home(request):
    return render(request,'Home.html')

def contact(request):
    return render(request,'contact.html')

# Create your views here.
def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')


def Login(request):
    error = ""
    if request.method == "POST":
     u = request.POST['uname']
     p = request.POST['pwd']
     user =authenticate(username=u , password=p)
     try:
         if user.is_staff:
             login(request , user)
             error = "no"
         else:
             error = "yes"
     except:
       error = "yes"   
    d = {'error' : error} 
    return render(request,'Login.html' , d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')
