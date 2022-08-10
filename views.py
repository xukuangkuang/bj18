from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('/index')

#这里加了一行注释

def login(request):
    return redirect('/login')




