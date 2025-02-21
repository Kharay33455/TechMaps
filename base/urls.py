from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path('', views.base, name='index')
]
from django.conf import settings
from django.conf.urls.static import static

