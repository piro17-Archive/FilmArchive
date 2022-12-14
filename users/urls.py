from django.urls import include, re_path
from users.forms import UserPasswordResetForm
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = "users"

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.Log_out, name="log_out"),
    re_path(r'^signup/$', views.sign_up, name="sign_up"),
    # re_path(r'^signup/check_username$', views.check_username, name='check_username'),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^mypage/$', views.mypage, name="mypage"),
    re_path(r'^mypage/myupdate$', views.user_update, name="user_update"),
    re_path(r'^mypage/changepw$', views.change_pw, name="change_pw"),
    re_path(r'^mypage/update-profpic$', views.profile_update, name="update_profpic"),
    re_path(r'^mypage/saved-detail$', views.saved_detail, name="saved_detail"),
    re_path(r'^password-reset/$', PasswordResetView.as_view(template_name='registration/password_reset_form.html', form_class=UserPasswordResetForm), name='reset_password'),
    re_path(r'^password-reset/done/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^password-reset-confirm/<uidb64>/<token>/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^password-reset-complete/$', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    re_path(r'^delete/(?P<username>[\w|\W.-]+)/$', views.delete_user, name='delete_user'),
    re_path(r'^find-username/$', views.find_username, name='find_username'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)