from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#home view
def base(request):
    if request.user.is_authenticated and request.user != None:
        context = {}
        return render(request, 'base/index.html', context)
    else:
        return HttpResponse('NOT FOUND')