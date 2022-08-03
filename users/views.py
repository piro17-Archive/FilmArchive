from django.shortcuts import render, redirect
from django.views import View

from users.models import User
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

        return render(request, "login.html", {"form": form})


@login_required 
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


# from .forms import RecoveryIdForm
# from django.views.generic import View

# class RecoveryIdView(View):
#     template_name = 'recovery_id.html'
#     form = RecoveryIdForm

#     def get(self, request):
#         if request.method=='GET':
#             form = self.recovery_id(None)
#         return render(request, self.template_name, { 'form':form, })

# import json
# from django.core.serializers.json import DjangoJSONEncoder
# from django.http import HttpResponse

# def ajax_find_id_view(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     result_id = User.objects.get(name=name, email=email)
       
#     return HttpResponse(json.dumps({"result_id": result_id.user_username}, cls=DjangoJSONEncoder), content_type = "application/json")

