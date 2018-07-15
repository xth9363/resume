from django.shortcuts import render
from resume.models import Visitor

from django.views.decorators.cache import cache_page


# Create your views here.
# 缓存30天
@cache_page(60 * 60 * 24 * 30)
def index(request):
    return render(request, 'index.html')
