from django.urls import path
from . import views
urlpatterns = [
    path('cache/', views.view_cache),
    path('mv/', views.view_mv)
]