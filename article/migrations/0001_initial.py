# Generated by Django 2.1 on 2018-08-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='文章标题')),
                ('md_content', models.TextField(verbose_name='文章markdown原始内容')),
                ('html_content', models.TextField(verbose_name='文章html渲染内容')),
                ('states', models.IntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_about', models.BooleanField(default=False, verbose_name='是否是About文章')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='图片地址')),
                ('type', models.IntegerField(choices=[(1, '文章列表大图'), (2, '文章列表小图'), (3, '文章内容插图')], default=3, verbose_name='图片所属类型')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
                'db_table': 'image',
            },
        ),
    ]