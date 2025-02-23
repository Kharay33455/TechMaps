from django.urls import path
from . import views
app_name = 'base'

urlpatterns = [
    path('', views.base, name='index'),
    path('logout', views.logout_request, name='logout')
]
