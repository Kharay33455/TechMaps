from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.

#home view
def base(request):
    if request.user.is_authenticated and request.user != None:
        context = {}        
        return render(request, 'base/index.html', context)
    else:
        context = {}
        return render(request, 'base/index.html', context)
    
# log out user
def logout_request(request):
    logout(request)    
    return HttpResponseRedirect(reverse('base:index'))
