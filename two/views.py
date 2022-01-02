import time

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


# Create your views here.

@cache_page(10)
def view_cache(request):
    t = time.time()

    return HttpResponse(f't is {t}')


def view_mv(request):
    print('--- test_mv view in ---')
    return HttpResponse('--- test_mv ---')
