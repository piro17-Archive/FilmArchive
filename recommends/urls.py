from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "recommends"

urlpatterns = [
    path('recommends/',views.recommends,name='recommend_list'),
    path('recommends/<int:id>',views.rec_detail,name='rec_detail'),
    path('recommends/create', views.rec_create,name='rec_create'),
    path('update/<int:id>', views.rec_update,name='rec_update'),
    path('delete/<int:id>',views.rec_delete,name='rec_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)