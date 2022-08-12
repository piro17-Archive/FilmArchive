from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "framesharings"

urlpatterns = [
    path('frame',views.frame,name='frame'),
    path('framedetail/<int:id>',views.framedetail,name='framedetail'),
    path('framecreate', views.framecreate,name='framecreate'),
    path('frameupdate/<int:id>', views.frameupdate,name='frameupdate'),
    path('framedelete/<int:id>',views.framedelete,name='framedelete'),
    path('like_ajax/', views.like_ajax, name = 'like_ajex'),
    path('save_ajax/', views.save_ajax, name = 'save_ajex'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)