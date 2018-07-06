from django.shortcuts import render
from resume.models import Visitor


# Create your views here.

def index(request):
    ip = False
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    elif 'REMOTE_ADDR' in request.META:
        ip = request.META['REMOTE_ADDR']
    if ip:
        Visitor.objects.create(ip=ip)
    return render(request, 'index.html')
