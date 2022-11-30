from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app import models
def home(req):
    return render(req,'home.html')
@login_required(login_url='/login')
def products(req):
    data = models.products.objects.all()
    return render(req,'products.html',{'data':data})    
def login(req):
    error = '' 
    if req.user.is_authenticated:
        return redirect('/products')
    else:
        if (req.method == "POST"):
            username = req.POST['username']
            password = req.POST['password']
            if username == "":
                error = "username can not left empty"
            elif password == "":
                error = "password can not left empty" 
            else:
                user = auth.authenticate(username = username,password=password)
                if user is None:
                    error = "Username or password error"
                else:
                    auth.login(req,user)
                    return redirect('/products')
    return render(req,'login.html',{'error':error})   

def signup(req):
    firstName = '' 
    lastName = ''
    email = ''
    username = ''
    error = ''
    if req.user.is_authenticated:
        return redirect("/products")
    else:
        if (req.method == "POST"):
            firstName = req.POST['first_name']
            lastName = req.POST['last_name']
            email = req.POST['email']
            username = req.POST['username']
            password = req.POST['password']
            confirmPassword = req.POST['confirm_password']
            if firstName == "":
                error = "First name can not left empty"
            elif lastName == "":
                error = "Last name can not left empty"
            elif email == "":
                error = "Email can not left empty"
            elif username == "":
                error = "username can not left empty"    
            elif password == "":
                error = "Password can not left empty"
            elif confirmPassword == "":
                error = "Confirm password can not left empty"
            elif password != confirmPassword:
                error = "password and confirm should match"
            elif User.objects.filter(username=username):
                error = "Username already exist"
            else:
                newRecord = User.objects.create_user(first_name=firstName,last_name=lastName,username=username,email=email,password=password)
                newRecord.save()
                return redirect("/login")
    return render(req,'register.html',{"error":error,"firstName":firstName,"lastName":lastName,"email":email,"username":username})  
def logout(req):
    auth.logout(req)
    return redirect("/")
def creators(req):
    return render(req,"creators.html")