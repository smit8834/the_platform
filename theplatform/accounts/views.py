from django.contrib import messages
from taneek import views
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model, login, update_session_auth_hash
import sqlite3
from django.http import HttpResponse


# Create your views here.

#---------------------- Sign Up Part ------------------------#

def registration(request):
    if request.method =='POST':
        full_name=request.POST['name']
        username=request.POST['phone']
        useremail=request.POST['email']
        upassword=request.POST['password']
        user = User.objects.create_user(username=username, first_name=full_name, password=upassword,email=useremail)
        user.save();
        messages.success(request,'Your account has been created successfully')
        return redirect(login)
    else:
        return render(request,'registration.html')

#------------------------ Login Part ------------------------#
user_logged_in = False
def login(request):
    global user_logged_in
    if request.method =='POST':
        phone=request.POST['phone']
        password=request.POST['password']
        request.session['phone']=phone
        
        global user
        user= auth.authenticate(username=phone,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            user_logged_in=True
            return redirect(views.Home)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect(login)
    else:
        return render(request,'login.html')



#----------------------------- Log out Part ---------------------------------#
def logout(request):
    global user_logged_in
    user_logged_in = False
    auth.logout(request)
    messages.success(request,'Your have logged out successfully!!')
    return redirect(views.login)

#---------------------------------------------------- End -------------------------------------------------------------#