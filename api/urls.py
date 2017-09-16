from django.conf.urls import url, include
# from django.contrib import admin

from .views import in_circle

urlpatterns = [
    url(r'^in_circle', in_circle, name='in_circle')
]