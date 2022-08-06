from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "limitedframes"

urlpatterns = [
    path('limited',views.limited,name='limited'),
    path('limitedlife',views.limitedlife,name='limitedlife'),
    path('limitedlifedetail/<int:id>',views.limitedlifedetail,name='limitedlifedetail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)