from django.shortcuts import render
from .models import TimeTracker
from django.http import HttpResponse, HttpResponseRedirect
from .forms import JobForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

def index(request):
    jobs = TimeTracker.objects.all()
    form = JobForm
    # user = User.objects.get(username = username)
    # jobs = TimeTracker.objects.filter(user = user)
    return render(request, 'index.html', {'jobs': jobs, 'form': form })

def post_job(request, username):
    form = JobForm(request.POST)
    if form.is_valid():
        job = form.save(commit = False)
        job.user = request.user
        job.save()
    return HttpResponseRedirect("/user/" + username + "/")

def profile(request, username):
    form = JobForm
    user = User.objects.get(username = username)
    jobs = TimeTracker.objects.filter(user = user)
    today = date.today()
    return render(request, 'profile.html', {'username': username, 'jobs': jobs, 'form': form, 'today': today })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password= p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/' + u)
                else:
                    print('The acount has been disabled!')
            else:
                return print('The username and password are incorrect.')
    else:
        form = LoginForm()
        return render(request, 'login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
