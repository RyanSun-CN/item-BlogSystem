from django.contrib import admin

from link.models import LinkInfo


# Register your models here.
@admin.register(LinkInfo)
class LinkInfoAdmin(admin.ModelAdmin):
    pass