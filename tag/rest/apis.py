# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from rest_framework.viewsets import GenericViewSet

from blog_api.utils import States
from tag.models import Tag
from tag.rest.serializers import TagSerializer


class TagApiSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                GenericViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_queryset(self):
        queryset = Tag.objects.filter(states=States.NORMAL)
        if self.request.user.is_authenticated:
            queryset = Tag.objects.all()
        return queryset

    def perform_destroy(self, instance):
        instance.states = States.DELETE if instance.states == States.NORMAL else States.NORMAL
        instance.save()
