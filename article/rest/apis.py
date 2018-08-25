# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from collections import defaultdict

from django.db.models import Count
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.response import Response
from django_filters import rest_framework as filters

from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView

from article.models import Article, Image
from article.rest.serializers import ArticleListSerializer, ArticleDetailSerializer, UploadSerializer, ImageSerializer, \
    ArchiveSerializer, ArticleUpdatdeSerializer
from blog_api.utils import States, QiNiuUtil
from categroy.models import Categroy
from tag.models import Tag


class ArticleFilter(filters.FilterSet):
    tag = filters.NumberFilter(field_name='tags__id')
    cate = filters.NumberFilter(field_name='cate__id')

    class Meta:
        model = Article
        fields = ('is_about', 'cate', 'tag')


class ArticleApiSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                    GenericViewSet):
    filter_class = ArticleFilter
    search_fields = ('html_content', 'cate__name')

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        if self.action == 'retrieve':
            return ArticleDetailSerializer
        return ArticleUpdatdeSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(states=States.NORMAL).order_by('-create_time')
        if self.request.user.is_authenticated:
            queryset = Article.objects.all().order_by('-create_time')
        return queryset

    def perform_destroy(self, instance):
        instance.states = States.DELETE if instance.states == States.NORMAL else States.NORMAL
        instance.save()

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()

    def list(self, request, *args, **kwargs):
        group = request.query_params.get('group')
        if group:
            groups = list(Article.objects.filter(is_about=False).
                             annotate(count=Count(group)).
                             values_list(group, flat=True).distinct())
            data = []
            id = request.query_params.get('id')
            if id:
                obj = Categroy.objects.get(pk=id)
                posts = Article.objects.filter(is_about=False, cate=id)
                if group == 'tags':
                    obj = Tag.objects.get(pk=id)
                    posts = Article.objects.filter(is_about=False, tags__in=id)
                post_list = []
                for post in posts:
                    post_info = {
                        'id': post.id,
                        'title': post.title,
                        'create_time': post.create_time,
                        'small_img': post.small_img.url,
                    }
                    post_list.append(post_info)
                data.append({
                    'id': obj.id,
                    'name': obj.name,
                    'posts': post_list
                })
                return Response(data)
            for i in groups:
                obj = Categroy.objects.get(pk=i)
                posts = Article.objects.filter(is_about=False, cate=i)
                if group == 'tags':
                    obj = Tag.objects.get(pk=i)
                    posts = Article.objects.filter(is_about=False, tags__in=(i, ))
                post_list = []
                for post in posts:
                    post_info = {
                        'id': post.id,
                        'title': post.title,
                        'create_time': post.create_time,
                        'small_img': post.small_img.url,
                    }
                    post_list.append(post_info)
                data.append({
                    'id': obj.id,
                    'name': obj.name,
                    'posts': post_list
                })
            return Response(data)
        else:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class UploadImg(GenericAPIView):
    """
    图片上传接口
    """
    serializer_class = UploadSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = serializer.validated_data['file']
        url = QiNiuUtil().upload(image.read(), mime_type=image.content_type)
        if not url:
            return Response({'detail': '上传失败'})
        Image.objects.create(url=url, type=serializer.validated_data['type'])
        return Response({'url': url})


class ImageApiSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    filter_fields = ('type',)
    search_fields = ('desc', )


class ArchiveList(ListModelMixin, GenericViewSet):
    serializer_class = ArchiveSerializer
    # queryset = Article.objects.archive()

    def get_queryset(self):
        date_list = Article.objects.exclude(is_about=True).datetimes('create_time', 'month', order='DESC')
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        archive_data = []
        for year, months in date_dict.items():
            for month in months:
                article_list = Article.objects.filter(create_time__year=year, create_time__month=month,
                                                      states=States.NORMAL)
                archive_data.append({
                    'date': '{}-{}'.format(year, month),
                    'article': article_list
                })
        return archive_data
