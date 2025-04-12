from django.db import models
from django.utils import timezone

from user.models import MyUser


# Create your models here.
class BlogType(models.Model):
    """
    博客类型实体
    """
    id = models.AutoField(primary_key=True)
    typename = models.CharField("类别名称", max_length=50)

    def __str__(self):
        return self.typename

    # 内部类，用于定义模型的元数据
    class Meta:
        # 定义模型的 单/复数 详细名称，在 Django 管理后台（Admin）中用于显示这个模型的名称，而不是默认的 BlogType
        verbose_name = "博客类别管理"
        verbose_name_plural = "博客类别管理"


class Blog(models.Model):
    """
    博客帖子实体
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField("博客标题", max_length=100)
    type = models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name="博客类别")
    content = models.CharField("博客内容", max_length=1000)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="用户（博客作者）")
    image = models.ImageField("文章图片", blank=True, upload_to="blog/")
    reads = models.IntegerField("阅读人数", default=0)
    abstract = models.CharField("博客摘要", max_length=300)
    create_time = models.DateTimeField("创建时间", default=timezone.now())
    update_time = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博客帖子管理"
        verbose_name_plural = "博客帖子管理"


# 博客评论
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="评论所属博客")
    user = models.CharField("评论用户", max_length=60)
    content = models.TextField("评论内容")
    create_time = models.DateTimeField("评论创建时间", default=timezone.now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="博客作者")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "博客评论管理"
        verbose_name_plural = "博客评论管理"


