"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    # http:127.0.0.1:8000/str/string
    path('str/<str:pg>', view.num_parameter),
    # http:127.0.0.1:8000/int/string/int
    path('<int:n>/<str:op>/<int:m>', view.cal_view),
    # http:127.0.0.1:8000/string/int(2)/int(2)
    re_path(r'^(?P<op>\w+)/(?P<x>\d{1,2})/(?P<y>\d{1,2})$', view.cal_re_view),
    path('<int:g>/', view.request_view),
    path('get/', view.get_view),
    path('post/', view.post_view),
    path('test-post', view.test_post_view),
    path('templates/', view.templates_view),
    path('templates2/', view.templates_view2),
    path('param/', view.param_view),
    path('myCal/', view.test_my_cal),
    path('music/', include('music.urls')),
    path('bookstore/', include('bookstore.urls'))
]
