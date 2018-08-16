# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from rest_framework.viewsets import GenericViewSet

from blog_api.utils import States
from categroy.models import Categroy
from categroy.rest.serializers import CategroySerializer


class CategroyApiSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                     GenericViewSet):
    serializer_class = CategroySerializer
    queryset = Categroy.objects.all()

    def get_queryset(self):
        queryset = Categroy.objects.filter(states=States.NORMAL)
        if self.request.user.is_authenticated:
            queryset = Categroy.objects.all()
        return queryset

    def perform_destroy(self, instance):
        instance.states = States.DELETE
        instance.save()
