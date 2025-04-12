from django.db import models

from user.models import MyUser


# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="用户")
    title = models.CharField("图片名", max_length=50, blank=True)
    info = models.CharField("信息", max_length=100, blank=True)
    pic = models.ImageField("图片", blank=True,upload_to="album/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "相册管理"
        verbose_name_plural = "相册管理"
