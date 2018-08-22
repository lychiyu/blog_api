# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""

from rest_framework import serializers

from tag.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'states', 'amount', 'name', 'create_time', 'update_time')
        read_only_fields = ('id', 'states', 'amount')

