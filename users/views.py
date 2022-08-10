from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from users.models import User, Profile
from . import forms
from users.forms import MyUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
    
    return render(request, "users/start.html", context=context)

def main(request):
    # return render(request, "main.html")
    #새로추가
    users=User.objects.all()
    context={
        "users": users,
    }
    
    return render(request, "users/main.html", context=context)


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        ctx = {"form": form}
        return render(request, "users/login.html", ctx)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "users/main.html")
        context = {
            "forms":form,
        }
        return render(request, "users/login.html", context=context)

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
            return render(request, "users/main.html")
        return redirect("users:sign_up")
    else:
        form = forms.SignupForm()
        return render(request, "users/signup.html", {"form": form})


def mypage(request):
    users=User.objects.all()
    context={
        "users": users,
    }
    return render(request, "users/mypage.html", context=context)


@login_required(login_url='login')
def user_update(request):
    if request.method == "POST":
        form = MyUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:mypage')

    else:
        form = MyUpdateForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/user_update.html', args)


@login_required(login_url='login')
def change_pw(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('users:mypage')
        else:
            return redirect('users:change_pw')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'users/change_pw.html', args)



@login_required(login_url='login')
def profile_update(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=profile)
        if p_form.is_valid():
            prof = p_form.save()
            prof.save()
            return redirect('users:mypage')

    else:
        p_form = ProfileUpdateForm(instance=profile)
    
    context = {
        'p_form': p_form,
    }

    return render(request, 'users/update_profpic.html', context)


def check_username(request):
    username = request.GET.get("username")
    data = {
       'username_exists':
       User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def delete_user_view(request):
    if request.method == "GET":
        user = User.objects.all()
        return render(request, 'users/delete_user.html', {'user': user})


def delete_user(request, username):
    try:
        u = User.objects.get(username=username)
        u.delete()
        context['msg'] = '회원 탈퇴가 성공적으로 완료되었습니다.'       
    except User.DoesNotExist: 
        context['msg'] = '존재하지 않는 회원입니다.'
    except Exception as e: 
        context['msg'] = e.message

    return render(request, 'users/main.html', context=context) 