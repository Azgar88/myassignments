from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def SignUp(request):
    if request.method=='POST':
        user_name=request.POST.get("username")
        user_mail=request.POST.get("email")
        user_password=request.POST.get("password")
        user_confirmpassword=request.POST.get("conpassword")
        if user_password!=user_confirmpassword:
            return HttpResponse("Invalid Confirm Password")
        else:
            user=User.objects.create_user(user_name,user_mail,user_password)
            user.save()
            return redirect(Login)
    return render (request,'registration.html')
def Login(request):
    if request.method=='POST':
        user_name=request.POST.get("username")
        user_password=request.POST.get("password")
        authenticate_user=authenticate(request,username=user_name,password=user_password)
        if authenticate_user is not None:
            login(request,authenticate_user)
            return redirect(HomePage)
        else:
            HttpResponse("invalid user")
    return render (request,'login.html')
@login_required(login_url="login")
def HomePage(request):

    return render (request,'home.html')

def Logout(request):
    logout(request)
    return redirect(Login)