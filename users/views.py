from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from users.models import User, Profile
from . import forms
from users.forms import MyUpdateForm, ProfileUpdateForm, CheckPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages

#여기추가
from ctypes import wintypes
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta
from datetime import datetime
from framesharings.models import Frame
from django.http import HttpResponse
# Create your views here.

def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates
    

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
    today = date.today()
    dates = date_range(str(today-timedelta(weeks=1)+ timedelta(days=1)), str(today))
    frameinfo = Frame.objects.all()
    for weeklikecount in frameinfo:
        count = 0
        if weeklikecount.framelikedate != None:
            datesplit = weeklikecount.framelikedate.split('/')
        else:
            continue
        for day in dates:
            for pic in datesplit:
                if day in pic:
                    count += 1
        weeklikecount.frameweeklike = count
        weeklikecount.save()
    frameweekinfo = frameinfo.order_by('?').order_by('-frameweeklike','?')[:3]
    users=User.objects.all()
    context={
        "users": users,
        "frameweekinfo": frameweekinfo,
    }
    
    return render(request, "users/main.html", context=context)


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        ctx = {"forms": form} #스펠링 아래와 똑같이 
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
        messages.error(request, '아이디 또는 비밀번호를 잘못 입력했습니다.')
        messages.error(request, '입력하신 내용을 다시 확인해주세요.')
        messages.error(request, '회원가입을 하신 적이 없으시다면 회원가입 후 로그인창을 이용해주세요.')
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
        # else:
        if User.objects.filter(username=request.POST['username']).exists():
            messages.error(request, '이미 존재하는 아이디입니다.')
            messages.error(request, '다른 아이디를 입력해주세요.')
            return redirect('users:sign_up')
        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('users:sign_up')
        else:
            messages.error(request, '비밀번호가 올바르지 않습니다.')
            messages.error(request, '생성하신 비밀번호가 8자리 이상이며, 문자로만 이루어지지 않았는지 다시 한 번 확인해주세요.')
            return redirect('users:sign_up')
    # get
    else:
        form = forms.SignupForm()
        return render(request, "users/signup.html", {"form": form})


def mypage(request):
    users=User.objects.all()
    save = request.user.saveMany.all().order_by('-id')[:8]
    context={
        "users": users,
        "save": save,
    }
    return render(request, "users/mypage.html", context=context)

def saved_detail(request):
    save = request.user.saveMany.all().order_by('-id')
    context = {
        "save": save,
    }
    return render(request, "users/saved_detail.html", context=context)


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


@login_required(login_url='login')
def delete_user(request, username):
    context={}
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            u = User.objects.get(username=username)
            u.delete()
            logout(request)
            context['msg'] = '회원 탈퇴가 성공적으로 완료되었습니다.'     
            return redirect('users:main')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'users/delete_user.html', {'password_form':password_form})


def find_username(request):
    if request.method == "POST":
        form = forms.FindUsernameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            try:
                found_user = User.objects.get(email=email, name=name)
                context = {'found_user' : found_user}
                return render(request, 'users/find_username_complete.html', context=context)
            except User.DoesNotExist:
                messages.error(request, '다음과 같은 이름 및 아이디를 가진 회원이 존재하지 않습니다.')
                return redirect('users:find_username')
    # if get
    else:
        form = forms.FindUsernameForm()
        return render(request, "users/find_username.html", {"form": form})