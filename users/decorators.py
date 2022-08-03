from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse


def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "접속중인 사용자입니다.")
            return redirect('/users/main/')

        return function(request, *args, **kwargs)

    return wrap

def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)

        return function(request, *args, **kwargs)

    return wrap
