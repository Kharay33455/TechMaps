from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path('', views.base, name='index')
]
from django.conf import settings
from django.conf.urls.static import static



urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)