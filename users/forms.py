from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput, label="password")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                raise forms.ValidationError("비밀번호가 틀렸습니다.")

        except User.DoesNotExist:
            raise forms.ValidationError("다음과 같은 유저가 존재하지 않습니다. 회원가입을 하지 않으셨다면 회원가입을 해주십시오.")

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # , "first_name", "last_name", "nickname"