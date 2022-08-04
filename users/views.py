from django.shortcuts import render, redirect
from django.views import View

from users.models import User
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User

#여기추가
from ctypes import wintypes
from django.contrib.auth.decorators import login_required

# Create your views here.
def start(request):
    # return render(request, "main.html")
    #새로추가
    users=User.objects.all()
    context={
        "users": users,
    }
    
    return render(request, "start.html", context=context)

def main(request):
    # return render(request, "main.html")
    #새로추가
    users=User.objects.all()
    context={
        "users": users,
    }
    
    return render(request, "main.html", context=context)


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        ctx = {"form": form}
        return render(request, "login.html", ctx)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "main.html")
        context = {
            "forms":form,
        }
        return render(request, "login.html", context=context)

@login_required(login_url='login')
def Log_out(request):
    logout(request)
    return redirect("users:main")

def sign_up(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "main.html")
        return redirect("users:sign_up")
    else:
        form = forms.SignupForm()
        return render(request, "signup.html", {"form": form})


