from django.db import models

# Create your models here.
from blog_api.utils import States


class Article(models.Model):
    title = models.CharField('文章标题', max_length=200, unique=True)
    big_img = models.CharField('文章列表展示大图', max_length=128, null=True, blank=True)
    small_img = models.CharField('文章列表展示小图', max_length=128, null=True, blank=True)
    author = models.ForeignKey('user.User', verbose_name='文章作者', on_delete=models.CASCADE)
    cate = models.ForeignKey('categroy.Categroy', verbose_name='文章类型', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tag.Tag', verbose_name='文章标签')
    md_content = models.TextField('文章markdown原始内容')
    html_content = models.TextField('文章html渲染内容')
    states = models.IntegerField('状态', choices=States.choices, default=States.NORMAL)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    is_about = models.BooleanField('是否是About文章', default=False)

    class Meta:
        db_table = 'article'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pk)
