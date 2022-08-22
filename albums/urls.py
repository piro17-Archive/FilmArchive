from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "albums"

urlpatterns = [
    path('album/<int:id>',views.album,name='album'),
    path('albumdetail/<int:id>',views.albumdetail,name='albumdetail'),
    path('albumcreate', views.albumcreate,name='albumcreate'),
    path('albumupdate/<int:id>', views.albumupdate,name='albumupdate'),
    path('albumdelete/<int:id>',views.albumdelete,name='albumdelete'),
    path('albumdcalendar/<int:id>',views.albumcalendar,name='albumcalendar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)