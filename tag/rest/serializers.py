# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""

from rest_framework import serializers

from tag.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id', 'states')

