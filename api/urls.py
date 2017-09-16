from django.conf.urls import url, include
# from django.contrib import admin

from .views import validate

urlpatterns = [
    url(r'^in_circle', validate, name='in_circle')
]