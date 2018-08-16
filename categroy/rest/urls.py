# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from categroy.rest.apis import CategroyApiSet

router = DefaultRouter()

router.register('', CategroyApiSet, base_name='cate')

urlpatterns = [
    url(r'^', include(router.urls)),
]
