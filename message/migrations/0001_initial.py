# Generated by Django 5.1.7 on 2025-04-12 08:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50, verbose_name="留言用户")),
                ("email", models.CharField(max_length=50, verbose_name="留言邮箱")),
                ("content", models.CharField(max_length=500, verbose_name="留言内容")),
                (
                    "create_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="留言时间"
                    ),
                ),
            ],
            options={
                "verbose_name": "留言管理",
                "verbose_name_plural": "留言管理",
            },
        ),
    ]
