from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app13.models import Student,Login

def show(request):
    qs = Student.objects.all()
    length = len(qs)
    return render(request,"main.html",{"data":qs,"l":length})

def saveDetails(request):
    uname = request.POST.get("name")
    upass = request.POST.get("pass")
    uemail = request.POST.get("email")
    Student(name=uname,password=upass,email=uemail).save()
    Login(email=uemail,password=upass).save()
    qs = Student.objects.all()
    length = len(qs)
    return render(request, "main.html", {"data": qs, "l": length,"mess":"Successfully registered"})

def login(request):
    try:
        if request.COOKIES["status"]:
            return render(request,"welcome.html",{"mess":"Welcome To "})
        else:
            return render(request,"login.html")
    except KeyError:
        return render(request,"login.html")

def loginCheck(request):
    s_email = request.POST.get("email")
    s_pass = request.POST.get("pass")
    try:
        Login.objects.get(email=s_email,password=s_pass)
        response = render(request,"welcome.html",{"mess":"Welcome To "})
        response.set_cookie("status",True)  #set_cookie
        return response
    except Login.DoesNotExist:
        messages.error(request,"invalid Email or Password")
        return redirect('login')
        # return render(request,"login.html",{"message":"Invalid User"})  @rendering to welcome page@

def userLogout(request):
    del request.COOKIES["status"]
    return login(request)