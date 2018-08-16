# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from tag.rest.apis import TagApiSet

router = DefaultRouter()

router.register('', TagApiSet, base_name='tags')

urlpatterns = [
    url(r'^', include(router.urls)),
]
