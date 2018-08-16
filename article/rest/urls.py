# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from article.rest.apis import ArticleApiSet

router = DefaultRouter()

router.register('', ArticleApiSet, base_name='articles')

urlpatterns = [
    url(r'^', include(router.urls)),
]
