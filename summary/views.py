from django.shortcuts import render
from .models import *


def base(request):
    post = Intro.objects.all()
    return render(request, 'summary/base.html', {'post': post})
