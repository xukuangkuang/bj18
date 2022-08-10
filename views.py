from django.http import HttpResponse

def index(request):
    return HttpResponse('/index')

#这里加了一行注释


