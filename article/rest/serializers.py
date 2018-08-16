# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
from rest_framework import serializers

from article.models import Article, Image
from categroy.rest.serializers import CategroySerializer
from tag.rest.serializers import TagSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'type', 'url')
        read_only_fields = ('id', 'url')


class ArticleListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    cate = CategroySerializer(read_only=True)
    big_pic = serializers.CharField(source='big_img.url')
    small_pic = serializers.CharField(source='small_img.url')
    author_name = serializers.CharField(source='author.username')

    class Meta:
        model = Article
        fields = ('id', 'title', 'tags', 'cate', 'author',
                  'author_name', 'big_pic', 'small_pic')


class ArticleDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    cate = CategroySerializer(read_only=True)
    big_img = ImageSerializer()
    small_img = ImageSerializer()
    author_name = serializers.CharField(source='author.username')

    class Meta:
        model = Article
        fields = ('id', 'title', 'tags', 'cate', 'author', 'author_name',
                  'md_content', 'html_content', 'states', 'create_time',
                  'update_time', 'is_about', 'big_img', 'small_img')
        read_only_fields = ('id', 'states')


class UploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Image
        fields = ('id', 'type', 'file')


class ArchiveSerializer(serializers.Serializer):
    year = serializers.CharField()
    month = serializers.CharField()
    article = ArticleListSerializer(many=True)