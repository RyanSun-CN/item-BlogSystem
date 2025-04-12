from django.contrib import admin

from user.models import MyUser


# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass