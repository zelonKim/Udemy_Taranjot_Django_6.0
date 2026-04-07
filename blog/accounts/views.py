from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/posts/home') 
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                homeurl = reverse('basic')
                return HttpResponseRedirect(homeurl)
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form':form})





def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/posts/home')
    else:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            
            if form.is_valid():
                id = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                user = authenticate(username=id, password=pw)
                
                if user is not None:
                    login(request, user)
                    homeurl = reverse('basic')
                    return HttpResponseRedirect(homeurl)
        else:  
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})
    
    

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
