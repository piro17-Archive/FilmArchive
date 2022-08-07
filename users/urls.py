from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = "users"

urlpatterns = [
    path("", views.start, name="start"),
    path("main", views.main, name="main"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.Log_out, name="log_out"),
    path("signup/", views.sign_up, name="sign_up"),
    path("accounts/", include('allauth.urls')),
    path("mypage/", views.mypage, name="mypage"),
    path("mypage/myupdate", views.user_update, name="user_update"),
    path("mypage/changepw", views.change_pw, name="change_pw"),
    path("mypage/update-profpic", views.profile_update, name="update_profpic"),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
