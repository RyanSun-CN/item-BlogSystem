from django.db import models

from user.models import MyUser


# Create your models here.
class LinkInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("链接名称", max_length=50)
    url = models.CharField("链接地址", max_length=200)
    remark = models.CharField("备注", max_length=500, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="用户")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "友情链接管理"
        verbose_name_plural = "友情链接管理"
