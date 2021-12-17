from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib import messages
import sqlite3
from taneek.models import *
from accounts.views import *
from django.http import HttpResponseRedirect
from .forms import *
from django.db.models import Q


def Home(request):
    return render(request, 'index.html')

def Connections(request):
    post1 = Posts.objects.all()
    context = {'post1': post1}
    return render(request, 'Connections.html',context)

def About(request):
    return render(request, 'about.html')

def about_edit(request):
    return render(request, 'about_edit.html')

def search(request):
    query=request.GET.get('query','')
    user = User.objects.filter(Q(__icontains= query))
    return render(request, 'search.html',{'query':query,'user': user})

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Connections')
    else:
        form = PostForm()
    return render(request,'post.html',{'form':form})


