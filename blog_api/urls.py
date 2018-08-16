"""blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from article.rest.apis import UploadImg, ImageApiSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/img', ImageApiSet, base_name='img')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='blog api文档')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/article/', include('article.rest.urls')),
    path('api/cate/', include('categroy.rest.urls')),
    path('api/tag/', include('tag.rest.urls')),
    path('api/login/', obtain_jwt_token),
    path('api/upload/', UploadImg.as_view()),
]
