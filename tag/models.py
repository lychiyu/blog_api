from django.db import models


# Create your models here.
from article.models import Article
from blog_api.utils import States


class Tag(models.Model):
    STATUS = (
        (0, '删除'),
        (1, '正常'),
    )
    name = models.CharField(verbose_name='标签名', max_length=50, unique=True)
    states = models.IntegerField(verbose_name='状态', choices=States.choices, default=States.NORMAL)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    class Meta:
        db_table = 'tag'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    @property
    def amount(self):
        return self.article_set.filter(is_about=False, states=States.NORMAL).count()

    def __str__(self):
        return self.name
