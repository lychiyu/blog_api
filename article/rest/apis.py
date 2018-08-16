# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.response import Response

from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView

from article.models import Article, Image
from article.rest.serializers import ArticleListSerializer, ArticleDetailSerializer, UploadSerializer, ImageSerializer, \
    ArchiveSerializer
from blog_api.utils import States, QiNiuUtil


class ArticleApiSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                    GenericViewSet):

    filter_fields = ('is_about', )

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(states=States.NORMAL, is_about=False)
        if self.request.user.is_authenticated:
            queryset = Article.objects.all()
        return queryset

    def perform_destroy(self, instance):
        instance.states = States.DELETE
        instance.save()


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


class ArchiveList(ListModelMixin, GenericViewSet):
    serializer_class = ArchiveSerializer
    queryset = Article.objects.archive()
