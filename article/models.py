from collections import defaultdict

from django.db import models

# Create your models here.

from blog_api.utils import States, NamedConst


class Image(models.Model):
    class TYPES(NamedConst):
        BIG = 1
        SMALL = 2
        POST = 3
        choices = (
            (BIG, '文章列表大图'),
            (SMALL, '文章列表小图'),
            (POST, '文章内容插图'),
        )

    url = models.CharField('图片地址', max_length=100)
    desc = models.CharField('图片描述', max_length=50, default='')
    type = models.IntegerField('图片所属类型', choices=TYPES.choices, default=TYPES.POST)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'image'
        verbose_name = '图片'
        verbose_name_plural = verbose_name

    @property
    def type_name(self):
        return self.get_type_display()

    def __str__(self):
        return str(self.url)


class ArticleManage(models.Manager):
    def archive(self):
        date_list = Article.objects.exclude(is_about=True).datetimes('create_time', 'month', order='DESC')
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        archive_data = []
        for year, months in date_dict.items():
            for month in months:
                article_list = Article.objects.filter(create_time__year=year, create_time__month=month,
                                                      states=States.NORMAL)
                archive_data.append({
                    'year': year,
                    'month': month,
                    'article': article_list
                })
        return archive_data


class Article(models.Model):
    objects = ArticleManage()

    title = models.CharField('文章标题', max_length=200, unique=True)
    summary = models.CharField('文章摘要', max_length=300, default='')
    big_img = models.ForeignKey('Image', verbose_name='文章列表展示大图', on_delete=models.CASCADE, related_name='article_big')
    small_img = models.ForeignKey('Image', verbose_name='文章列表展示小图', on_delete=models.CASCADE,
                                  related_name='article_small')
    author = models.ForeignKey('user.User', verbose_name='文章作者', on_delete=models.CASCADE)
    cate = models.ForeignKey('categroy.Categroy', verbose_name='文章类型', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tag.Tag', verbose_name='文章标签')
    md_content = models.TextField('文章markdown原始内容', default='')
    html_content = models.TextField('文章html渲染内容', default='')
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
