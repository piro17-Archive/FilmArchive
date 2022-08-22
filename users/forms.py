from cProfile import Profile
from django import forms
from .models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.hashers import check_password


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
        fields = ["username", "email", "password1", "password2", "name", "nickname"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username']
        self.fields['email'].widget.attrs.update({'placeholder': 'example@example.com'})
        self.fields['password1'].widget.attrs.update({'placeholder':'숫자+ 대/소문자 8자리 이상'})        
        self.fields['password2'].widget.attrs.update()
        self.fields['name'].widget.attrs.update()
        self.fields['nickname'].widget.attrs.update()


class MyUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        # if you're excluding only a few fields, 
        # use exclude and list the fields that are being excluded instaed
        fields = {
            'name',
            'email',
            'nickname',
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            'image',
        }


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')


class FindUsernameForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com',}))

    class Meta:
        model = User
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(FindUsernameForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_name',
        })
        self.fields['email'].label = 'email'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_email' 
        })


# placeholder 생성을 위한 django form 커스텀
class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'example@example.com',
        'name': 'email'
        }))