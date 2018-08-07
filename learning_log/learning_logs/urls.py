# In foo/urls/blog.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
