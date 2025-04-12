from django.db import models
from django.utils import timezone

from user.models import MyUser


# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("留言用户", max_length=50)
    email = models.CharField("留言邮箱", max_length=50)
    content = models.CharField("留言内容", max_length=500)
    create_time = models.DateTimeField("留言时间", default=timezone.now)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="用户")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "留言管理"
        verbose_name_plural = "留言管理"