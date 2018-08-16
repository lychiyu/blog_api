# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from rest_framework import serializers

from article.models import Article, Image


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Image
        fields = ('id', 'type', 'file')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'type', 'url')
        read_only_fields = ('id', 'url')


class ArchiveSerializer(serializers.Serializer):
    year = serializers.CharField()
    month = serializers.CharField()
    article = ArticleSerializer(many=True)
