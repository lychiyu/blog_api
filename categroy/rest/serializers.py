# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""

from rest_framework import serializers

from categroy.models import Categroy


class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categroy
        fields = '__all__'
        read_only_fields = ('id', 'states')
