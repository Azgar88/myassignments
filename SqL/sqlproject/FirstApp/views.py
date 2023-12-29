from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .models import Employee
# Create your views here.
def SignUp(request):
    if request.method=='POST':
        user_name=request.POST["username"]
        user_mail=request.POST["email"]
        user_password=request.POST["password"]
        user_confirmpassword=request.POST["confirmpassword"]
        if user_password!=user_confirmpassword:
            return HttpResponse("Invalid Confirm Password")
        else:
            user_credentials=Employee(name=user_name,mailid=user_mail,password=user_password,confirmpassword=user_confirmpassword)
            user_credentials.save()
            return redirect(Login)
    return render (request,'registration.html')
def Login(request):
    if request.method=='POST':
        user_name=request.POST["username"]
        user_password=request.POST["password"]
        stored_data=Employee.objects.all()
        for i in stored_data:
            if i.name==user_name and i.password==user_password:
                return redirect(HomePage)

        # if stored_data
    return render (request,'login.html')
def HomePage(request):
    if request.method=="POST":
        return redirect(Login)
    return render (request,'homepage.html')

# def Logout(request):
#     logout(request)
#     return redirect(Login)