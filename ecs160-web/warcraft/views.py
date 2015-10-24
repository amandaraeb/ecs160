from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserProfileForm
from .models import UserProfile
from django.core.files.uploadedfile import SimpleUploadedFile

import re
media = '/home/apmishra100/ecs160/media'
# Create your views here.

def index(request):
    template = loader.get_template('warcraft/index.html')
    return HttpResponse(template.render())
    

def prototype_form(request):
    template = loader.get_template('warcraft/prototype_form.html')
    return HttpResponse(template.render())

def prototype(request):
    error = False
    message=""
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            message = "BAD INPUT"
            return render(request, 'warcraft/prototype_form.html', {'error':error, 'message':message})
        else:
            message = '%s' %request.GET['q']
            if message == "":
                message = "BAD INPUT"
                return render(request, 'warcraft/prototype_form.html', {'error':True, 'message':message})
            else:
                return render(request, 'warcraft/prototype_form.html', {'error':error, 'message':message})
    else:
        return render(request, 'warcraft/prototype_form.html', {'error':error, 'message':message})


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('warcraft/login.html', c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
        
def logout(request):
    auth.logout(request)
    return render_to_response('warcraft/logout.html')

def loggedin(request):
    profile = request.user.userprofile
    picture = profile.picture
    return render(request, 'warcraft/loggedin.html', {'full_name': request.user.get_full_name(), 'avatar':picture})

def invalid_login(request):
    return render_to_response('warcraft/invalid_login.html')
    
    
def register_user(request):
    context = RequestContext(request)
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.picture = request.FILES['picture']
            profile.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('warcraft/register.html', {'user_form': user_form, 'profile_form': profile_form}, context)

def register_success (reqest):
    return render_to_response('warcraft/register_success.html')

def internalLogin (request):
    if request.method == 'GET':
        username = request.META['HTTP_USERNAME']
        password = request.META['HTTP_PASSWORD']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/loggedin')
        else:
            return HttpResponseRedirect('/accounts/invalid')
        return render(request, 'warcraft/internalLogin.html', {'username': dummy, 'password': passdummy})

def edit_name (request):
  name = request.user.first_name + " " +  request.user.last_name
  return render(request, 'warcraft/edit_name.html', {'name': name})

def edit_name_success (request):
  request.user.first_name = request.POST.get("firstname", "")
  request.user.last_name = request.POST.get("lastname", "")
  request.user.save()
  name = request.user.first_name + " " + request.user.last_name
  return render(request, 'warcraft/edit_name_success.html', {'name': name})


def change_password(request):
  return render(request, 'warcraft/change_password.html', {'name': "nothing"})

def change_password_success(request):
  request.user.set_password(request.POST.get("new_password", ""))
  request.user.save()
  return render(request, 'warcraft/change_password_success.html', {'name': "nada"})
