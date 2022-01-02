import time

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def view_cache(request):
    t = time.time()

    return HttpResponse(f't is {t}')
