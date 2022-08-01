from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def main(request):
    return render(request, "main.html")

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
                # 비밀번호/아이디 찾기?????

        return render(request, "login.html", {"form": form})
    
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