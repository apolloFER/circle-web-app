from django.conf.urls import url, include
# from django.contrib import admin

from .views import home

urlpatterns = [
    url(r'^', home, name='home')
]